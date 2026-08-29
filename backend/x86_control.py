"""Small x86-64 control-flow encoder for inspectable follower-backend probes.

This sits below Idriç's checked one-step-at-a-time handoff. It deliberately
implements only ordinary baseline integer/data/branch forms earned by the
first search fixture; it is not a source recognizer and does not claim general
x86 support.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass

from backend.idric_x86 import write_elf


@dataclass(frozen=True)
class Fixup:
    displacement_at: int
    instruction_end: int
    label: str


@dataclass(frozen=True)
class ListingEntry:
    start: int
    end: int
    text: str


class CodeBuilder:
    """Encode a deliberately tiny x86-64 baseline with named rel32 labels."""

    def __init__(self) -> None:
        self.code = bytearray()
        self.labels: dict[str, int] = {}
        self.fixups: list[Fixup] = []
        self.entries: list[ListingEntry] = []

    def _emit(self, raw: bytes, text: str) -> None:
        start = len(self.code)
        self.code.extend(raw)
        self.entries.append(ListingEntry(start, len(self.code), text))

    def label(self, name: str) -> None:
        if name in self.labels:
            raise ValueError(f"duplicate label {name!r}")
        self.labels[name] = len(self.code)

    def mov_r32_imm32(self, register: int, value: int, text: str) -> None:
        if not 0 <= register <= 7:
            raise ValueError("only legacy r32 registers are in this first slice")
        if not 0 <= value <= 0xFFFFFFFF:
            raise ValueError("mov r32 immediate must fit 32 bits")
        self._emit(bytes([0xB8 + register]) + struct.pack("<I", value), text)

    def lea_rsi_rip(self, label: str) -> None:
        start = len(self.code)
        self._emit(b"\x48\x8d\x35\x00\x00\x00\x00", f"lea rsi, [rip + {label}]")
        self.fixups.append(Fixup(start + 3, start + 7, label))

    def xor_eax_eax(self) -> None:
        self._emit(b"\x31\xc0", "xor eax, eax")

    def xor_ecx_ecx(self) -> None:
        self._emit(b"\x31\xc9", "xor ecx, ecx")

    def cmp_rcx_rdx(self) -> None:
        self._emit(b"\x48\x39\xd1", "cmp rcx, rdx")

    def movzx_ebx_byte_rsi_rcx_disp8(self, displacement: int) -> None:
        if not 0 <= displacement <= 0x7F:
            raise ValueError("first indexed-byte slice supports offsets 0..127")
        self._emit(
            b"\x0f\xb6\x5c\x0e" + bytes([displacement]),
            f"movzx ebx, byte [rsi + rcx + {displacement}]",
        )

    def cmp_ebx_byte_value(self, value: int) -> None:
        if not 0 <= value <= 0xFF:
            raise ValueError("byte comparison value must fit 8 bits")
        self._emit(b"\x81\xfb" + struct.pack("<I", value), f"cmp ebx, {value}")

    def add_eax_1(self) -> None:
        self._emit(b"\x83\xc0\x01", "add eax, 1")

    def add_rcx_1(self) -> None:
        self._emit(b"\x48\x83\xc1\x01", "add rcx, 1")

    def mov_edi_eax(self) -> None:
        self._emit(b"\x89\xc7", "mov edi, eax")

    def syscall(self) -> None:
        self._emit(b"\x0f\x05", "syscall")

    def jump(self, label: str) -> None:
        start = len(self.code)
        self._emit(b"\xe9\x00\x00\x00\x00", f"jmp {label}")
        self.fixups.append(Fixup(start + 1, start + 5, label))

    def jump_equal(self, label: str) -> None:
        self._jump_condition(b"\x0f\x84", "je", label)

    def jump_not_equal(self, label: str) -> None:
        self._jump_condition(b"\x0f\x85", "jne", label)

    def jump_above_or_equal(self, label: str) -> None:
        self._jump_condition(b"\x0f\x83", "jae", label)

    def _jump_condition(self, opcode: bytes, mnemonic: str, label: str) -> None:
        start = len(self.code)
        self._emit(opcode + b"\x00\x00\x00\x00", f"{mnemonic} {label}")
        self.fixups.append(Fixup(start + len(opcode), start + len(opcode) + 4, label))

    def data(self, label: str, payload: bytes) -> None:
        self.label(label)
        self.code.extend(payload)

    def finish(self) -> tuple[bytes, str]:
        for fixup in self.fixups:
            try:
                target = self.labels[fixup.label]
            except KeyError as exc:
                raise ValueError(f"undefined label {fixup.label!r}") from exc
            displacement = target - fixup.instruction_end
            struct.pack_into("<i", self.code, fixup.displacement_at, displacement)

        lines = []
        image = bytes(self.code)
        for entry in self.entries:
            raw = image[entry.start:entry.end]
            lines.append(f"{entry.start:04x}  {raw.hex(' '):<28} {entry.text}")
        return image, "\n".join(lines) + "\n"


def fixed_string_count_code(haystack: bytes, needle: bytes) -> tuple[bytes, str]:
    """Specialize an overlapping exact fixed-string count over embedded bytes.

    The semantic fixture is intentionally small. Its purpose is to exercise
    ordinary indexed loads, FLAGS-based control flow, and rel32 fixups without
    inventing a grep runtime or argv/file ABI before the checked compiler seam
    and runtime boundary are ready.
    """
    if not needle:
        raise ValueError("empty-pattern semantics are not chosen for this probe")
    if len(needle) > 128:
        raise ValueError("first probe limits the specialized needle to 128 bytes")

    positions = max(0, len(haystack) - len(needle) + 1)
    if positions > 255:
        raise ValueError(
            "first native oracle reports through process exit status; "
            "limit candidate starts to 255"
        )

    builder = CodeBuilder()
    builder.lea_rsi_rip("haystack")
    builder.mov_r32_imm32(2, positions, f"mov edx, {positions} ; candidate starts")
    builder.xor_eax_eax()
    builder.xor_ecx_ecx()

    builder.label("loop")
    builder.cmp_rcx_rdx()
    builder.jump_above_or_equal("done")
    for offset, expected in enumerate(needle):
        builder.movzx_ebx_byte_rsi_rcx_disp8(offset)
        builder.cmp_ebx_byte_value(expected)
        builder.jump_not_equal("next")
    builder.add_eax_1()

    builder.label("next")
    builder.add_rcx_1()
    builder.jump("loop")

    builder.label("done")
    builder.mov_edi_eax()
    builder.mov_r32_imm32(0, 60, "mov eax, 60 ; SYS_exit")
    builder.syscall()
    builder.data("haystack", haystack)
    return builder.finish()


def fixed_string_count_elf(haystack: bytes, needle: bytes) -> tuple[bytes, str]:
    code, listing = fixed_string_count_code(haystack, needle)
    return write_elf(code), listing
