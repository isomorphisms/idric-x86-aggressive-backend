# TCVTROWD2PS

`TCVTROWD2PS` converts an AMX tile row between the floating-point formats encoded by the mnemonic. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AMX_TILE`
- XED category/categories: `AMX_TILE`
- ISA set(s): `AMX_AVX512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `ZMM TMM GPR32`; `ZMM TMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `TCVTROWD2PS_ZMMf32_TMMu32_GPR32u32` — `TCVTROWD2PS`
- `TCVTROWD2PS_ZMMf32_TMMu32_IMM8` — `TCVTROWD2PS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
