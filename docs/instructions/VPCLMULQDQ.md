# VPCLMULQDQ

`VPCLMULQDQ` performs carry-less multiplication of selected binary-polynomial operands for CRC and finite-field arithmetic. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`, `VPCLMULQDQ`
- XED category/categories: `AVX`, `VPCLMULQDQ`
- ISA set(s): `AVX`, `AVX512_VPCLMULQDQ_128`, `AVX512_VPCLMULQDQ_256`, `AVX512_VPCLMULQDQ_512`, `VPCLMULQDQ`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`; `YMM YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPCLMULQDQ_XMMdq_XMMdq_MEMdq_IMMb` — `VPCLMULQDQ`
- `VPCLMULQDQ_XMMdq_XMMdq_XMMdq_IMMb` — `VPCLMULQDQ`
- `VPCLMULQDQ_XMMu128_XMMu64_MEMu64_IMM8_AVX512` — `VPCLMULQDQ`
- `VPCLMULQDQ_XMMu128_XMMu64_XMMu64_IMM8_AVX512` — `VPCLMULQDQ`
- `VPCLMULQDQ_YMMu128_YMMu64_MEMu64_IMM8` — `VPCLMULQDQ`
- `VPCLMULQDQ_YMMu128_YMMu64_MEMu64_IMM8_AVX512` — `VPCLMULQDQ`
- `VPCLMULQDQ_YMMu128_YMMu64_YMMu64_IMM8` — `VPCLMULQDQ`
- `VPCLMULQDQ_YMMu128_YMMu64_YMMu64_IMM8_AVX512` — `VPCLMULQDQ`
- `VPCLMULQDQ_ZMMu128_ZMMu64_MEMu64_IMM8_AVX512` — `VPCLMULQDQ`
- `VPCLMULQDQ_ZMMu128_ZMMu64_ZMMu64_IMM8_AVX512` — `VPCLMULQDQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
