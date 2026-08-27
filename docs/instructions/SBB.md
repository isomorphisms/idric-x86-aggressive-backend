# SBB

`SBB` subtracts the source and incoming borrow from the destination. The pinned XED inventory represents it with 62 normalized encoding records and 42 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `SBB_AL_IMMb` — `SBB`
- `SBB_GPR8_GPR8_18` — `SBB`
- `SBB_GPR8_GPR8_1A` — `SBB`
- `SBB_GPR8_IMMb_80r3` — `SBB`
- `SBB_GPR8_IMMb_82r3` — `SBB`
- `SBB_GPR8_MEMb` — `SBB`
- `SBB_GPR8i8_GPR8i8_APX` — `SBB`
- `SBB_GPR8i8_GPR8i8_GPR8i8_APX_N3` — `SBB`
- `SBB_GPR8i8_GPR8i8_IMM8_APX_N3` — `SBB`
- `SBB_GPR8i8_GPR8i8_MEMi8_APX_N3` — `SBB`
- `SBB_GPR8i8_IMM8_APX` — `SBB`
- `SBB_GPR8i8_MEMi8_APX` — `SBB`
- … 30 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
