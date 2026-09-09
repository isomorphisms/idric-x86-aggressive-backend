"""Minimal deterministic ELF64 packaging owned by the x86-64 backend."""

from __future__ import annotations

import struct

ELF_BASE = 0x400000
CODE_OFFSET = 0x1000


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
    if len(headers) > CODE_OFFSET:
        raise ValueError("ELF headers exceed the deterministic code offset")
    return headers + bytes(CODE_OFFSET - len(headers)) + code_and_data
