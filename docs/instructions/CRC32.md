# CRC32

`CRC32` updates a CRC-32C checksum accumulator using the Castagnoli polynomial. The pinned XED inventory represents it with 10 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `APXEVEX`, `SSE4`
- XED category/categories: `APX`, `SSE`
- ISA set(s): `APX_F`, `SSE42`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPRy GPR8`; `GPRy GPRv`; `GPRy MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `CRC32_GPRy_GPR8i8_APX` — `CRC32`
- `CRC32_GPRy_GPRv_APX` — `CRC32`
- `CRC32_GPRy_MEMi8_APX` — `CRC32`
- `CRC32_GPRy_MEMv_APX` — `CRC32`
- `CRC32_GPRyy_GPR8b` — `CRC32`
- `CRC32_GPRyy_GPRv` — `CRC32`
- `CRC32_GPRyy_MEMb` — `CRC32`
- `CRC32_GPRyy_MEMv` — `CRC32`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
