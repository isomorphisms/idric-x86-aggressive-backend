# VINSERTF64X2

`VINSERTF64X2` inserts a scalar or subvector into selected positions of a destination containing its encoded scalar or vector elements. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX512DQ_256`, `AVX512DQ_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `YMM MASK1 YMM MEM IMM`; `YMM MASK1 YMM XMM IMM`; `ZMM MASK1 ZMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VINSERTF64X2_YMMf64_MASKmskw_YMMf64_MEMf64_IMM8_AVX512` — `VINSERTF64X2`
- `VINSERTF64X2_YMMf64_MASKmskw_YMMf64_XMMf64_IMM8_AVX512` — `VINSERTF64X2`
- `VINSERTF64X2_ZMMf64_MASKmskw_ZMMf64_MEMf64_IMM8_AVX512` — `VINSERTF64X2`
- `VINSERTF64X2_ZMMf64_MASKmskw_ZMMf64_XMMf64_IMM8_AVX512` — `VINSERTF64X2`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
