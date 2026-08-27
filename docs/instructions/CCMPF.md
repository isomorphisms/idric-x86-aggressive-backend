# CCMPF

`CCMPF` performs the architecture's conditional compare operation when the condition-code state denotes false; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `CCMPF_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPF`
- `CCMPF_GPR8i8_IMM8_DFV_APX_N3` — `CCMPF`
- `CCMPF_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPF`
- `CCMPF_GPRv_GPRv_DFV_APX_N3` — `CCMPF`
- `CCMPF_GPRv_IMM8_DFV_APX_N3` — `CCMPF`
- `CCMPF_GPRv_IMMz_DFV_APX_N3` — `CCMPF`
- `CCMPF_GPRv_MEMv_DFV_APX_N3` — `CCMPF`
- `CCMPF_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPF`
- `CCMPF_MEMi8_IMM8_DFV_APX_N3` — `CCMPF`
- `CCMPF_MEMv_GPRv_DFV_APX_N3` — `CCMPF`
- `CCMPF_MEMv_IMM8_DFV_APX_N3` — `CCMPF`
- `CCMPF_MEMv_IMMz_DFV_APX_N3` — `CCMPF`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
