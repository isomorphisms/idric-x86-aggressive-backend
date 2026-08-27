# VPEXTRW

`VPEXTRW` extracts the packed 16-bit word lane selected by an immediate index and writes it to a general-purpose register or memory destination. The pinned XED inventory represents it with 5 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512BW_128N`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR32 XMM IMM`; `MEM XMM IMM`; `VGPR32 XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPEXTRW_GPR32d_XMMdq_IMMb_15` — `VPEXTRW`
- `VPEXTRW_GPR32d_XMMdq_IMMb_C5` — `VPEXTRW`
- `VPEXTRW_GPR32u16_XMMu16_IMM8_AVX512` — `VPEXTRW`
- `VPEXTRW_MEMu16_XMMu16_IMM8_AVX512` — `VPEXTRW`
- `VPEXTRW_MEMw_XMMdq_IMMb` — `VPEXTRW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
