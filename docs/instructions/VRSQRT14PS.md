# VRSQRT14PS

`VRSQRT14PS` computes square roots of packed single-precision floating-point elements. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `XMM MASK1 XMM`; `YMM MASK1 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VRSQRT14PS_XMMf32_MASKmskw_MEMf32_AVX512` — `VRSQRT14PS`
- `VRSQRT14PS_XMMf32_MASKmskw_XMMf32_AVX512` — `VRSQRT14PS`
- `VRSQRT14PS_YMMf32_MASKmskw_MEMf32_AVX512` — `VRSQRT14PS`
- `VRSQRT14PS_YMMf32_MASKmskw_YMMf32_AVX512` — `VRSQRT14PS`
- `VRSQRT14PS_ZMMf32_MASKmskw_MEMf32_AVX512` — `VRSQRT14PS`
- `VRSQRT14PS_ZMMf32_MASKmskw_ZMMf32_AVX512` — `VRSQRT14PS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
