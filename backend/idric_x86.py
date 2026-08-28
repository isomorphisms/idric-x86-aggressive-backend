#!/usr/bin/env python3
"""Tiny, direct Idriç-to-ELF64 bootstrap backend.

The source recognizer is deliberately limited to the print-X acceptance fixture.
The validated IR, instruction encoder, and ELF writer are real backend pieces.
"""

from __future__ import annotations

import argparse
import re
import struct
from dataclasses import dataclass
from pathlib import Path

ELF_BASE = 0x400000
CODE_OFFSET = 0x1000


@dataclass(frozen=True)
class WriteByte:
    value: int


@dataclass(frozen=True)
class Exit:
    status: int


def lower_bootstrap_source(source: str) -> tuple[WriteByte, Exit]:
    """Recognize only the frozen IO bootstrap form; this is not general IO lowering."""
    normalized = re.sub(r"--.*$", "", source, flags=re.MULTILINE)
    match = re.fullmatch(
        r"\s*module\s+[A-Z][A-Za-z0-9_.]*\s+"
        r"main\s*:\s*IO\s*\(\s*\)\s+"
        r"main\s*=\s*putChar\s+'([^'\\])'\s*",
        normalized,
    )
    if not match:
        raise ValueError("unsupported bootstrap source; expected main = putChar '<byte>'")
    value = ord(match.group(1))
    if value > 0x7F:
        raise ValueError("bootstrap output must be one ASCII byte")
    return WriteByte(value), Exit(0)


def mov_imm64(register_opcode: int, value: int) -> bytes:
    if not 0 <= value <= 0x7FFFFFFF:
        raise ValueError("bootstrap immediate does not fit sign-extended imm32")
    return b"\x48\xc7" + bytes([register_opcode]) + struct.pack("<I", value)


def select_instructions(program: tuple[WriteByte, Exit]) -> tuple[bytes, list[str]]:
    write, exit_ = program
    code = bytearray()
    listing: list[str] = []

    def emit(raw: bytes, text: str) -> None:
        code.extend(raw)
        listing.append(f"{len(code) - len(raw):04x}  {raw.hex(' '):<24} {text}")

    emit(mov_imm64(0xC0, 1), "mov rax, 1        ; SYS_write")
    emit(mov_imm64(0xC7, 1), "mov rdi, 1        ; stdout")
    lea_at = len(code)
    emit(b"\x48\x8d\x35\x00\x00\x00\x00", "lea rsi, [rip + output]")
    emit(mov_imm64(0xC2, 1), "mov rdx, 1")
    emit(b"\x0f\x05", "syscall")
    emit(b"\x48\x31\xff", "xor rdi, rdi      ; status 0")
    emit(mov_imm64(0xC0, 60), "mov rax, 60       ; SYS_exit")
    emit(b"\x0f\x05", "syscall")

    output_at = len(code)
    displacement = output_at - (lea_at + 7)
    code[lea_at + 3 : lea_at + 7] = struct.pack("<i", displacement)
    listing[2] = f"{lea_at:04x}  {bytes(code[lea_at:lea_at + 7]).hex(' '):<24} lea rsi, [rip + {displacement}] ; output"
    code.append(write.value)
    return bytes(code), listing


def write_elf(code_and_data: bytes) -> bytes:
    entry = ELF_BASE + CODE_OFFSET
    file_size = CODE_OFFSET + len(code_and_data)
    ident = b"\x7fELF\x02\x01\x01" + b"\x00" * 9
    elf_header = ident + struct.pack(
        "<HHIQQQIHHHHHH", 2, 62, 1, entry, 64, 0, 0, 64, 56, 1, 0, 0, 0
    )
    program_header = struct.pack(
        "<IIQQQQQQ", 1, 5, 0, ELF_BASE, ELF_BASE, file_size, file_size, 0x1000
    )
    headers = elf_header + program_header
    return headers + bytes(CODE_OFFSET - len(headers)) + code_and_data


def compile_file(source_path: Path, output_path: Path, listing_path: Path | None) -> None:
    program = lower_bootstrap_source(source_path.read_text())
    machine, listing = select_instructions(program)
    output_path.write_bytes(write_elf(machine))
    output_path.chmod(0o755)
    if listing_path:
        listing_path.write_text("\n".join(listing) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    parser.add_argument("--listing", type=Path)
    args = parser.parse_args()
    compile_file(args.source, args.output, args.listing)


if __name__ == "__main__":
    main()
