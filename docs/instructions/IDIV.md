# IDIV

`IDIV` performs signed division of the implicit double-width dividend, producing quotient and remainder. The pinned XED inventory represents it with 16 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR8`; `GPRv`; `MEM`. Representative implicit state: `AX`; `OrAX OrDX`.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `IDIV_GPR8` — `IDIV`
- `IDIV_GPR8i8_APX` — `IDIV`
- `IDIV_GPR8i8_APX_N3` — `IDIV`
- `IDIV_GPRv` — `IDIV`
- `IDIV_GPRv_APX` — `IDIV`
- `IDIV_GPRv_APX_N3` — `IDIV`
- `IDIV_MEMb` — `IDIV`
- `IDIV_MEMi8_APX` — `IDIV`
- `IDIV_MEMi8_APX_N3` — `IDIV`
- `IDIV_MEMv` — `IDIV`
- `IDIV_MEMv_APX` — `IDIV`
- `IDIV_MEMv_APX_N3` — `IDIV`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
