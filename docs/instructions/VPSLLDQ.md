# VPSLLDQ

`VPSLLDQ` implements the distinct architectural operation named VPSLLDQ in XED category AVX, AVX2, AVX512; the pinned Intel/AMD reference defines its exact data transformation. The pinned XED inventory represents it with 8 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX2`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX2`, `AVX512`
- ISA set(s): `AVX`, `AVX2`, `AVX512BW_128`, `AVX512BW_256`, `AVX512BW_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`; `YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPSLLDQ_XMMdq_XMMdq_IMMb` — `VPSLLDQ`
- `VPSLLDQ_XMMu8_MEMu8_IMM8_AVX512` — `VPSLLDQ`
- `VPSLLDQ_XMMu8_XMMu8_IMM8_AVX512` — `VPSLLDQ`
- `VPSLLDQ_YMMqq_YMMqq_IMMb` — `VPSLLDQ`
- `VPSLLDQ_YMMu8_MEMu8_IMM8_AVX512` — `VPSLLDQ`
- `VPSLLDQ_YMMu8_YMMu8_IMM8_AVX512` — `VPSLLDQ`
- `VPSLLDQ_ZMMu8_MEMu8_IMM8_AVX512` — `VPSLLDQ`
- `VPSLLDQ_ZMMu8_ZMMu8_IMM8_AVX512` — `VPSLLDQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
