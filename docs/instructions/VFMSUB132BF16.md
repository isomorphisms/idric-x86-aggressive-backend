# VFMSUB132BF16

`VFMSUB132BF16` computes a fused multiply/add-or-subtract operation on bfloat16 elements with one rounding step for each fused result. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `VFMA`
- ISA set(s): `AVX10_2_BF16_128`, `AVX10_2_BF16_256`, `AVX10_2_BF16_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `YMM MASK1 YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VFMSUB132BF16_XMMbf16_MASKmskw_XMMbf16_MEMbf16_AVX512` — `VFMSUB132BF16`
- `VFMSUB132BF16_XMMbf16_MASKmskw_XMMbf16_XMMbf16_AVX512` — `VFMSUB132BF16`
- `VFMSUB132BF16_YMMbf16_MASKmskw_YMMbf16_MEMbf16_AVX512` — `VFMSUB132BF16`
- `VFMSUB132BF16_YMMbf16_MASKmskw_YMMbf16_YMMbf16_AVX512` — `VFMSUB132BF16`
- `VFMSUB132BF16_ZMMbf16_MASKmskw_ZMMbf16_MEMbf16_AVX512` — `VFMSUB132BF16`
- `VFMSUB132BF16_ZMMbf16_MASKmskw_ZMMbf16_ZMMbf16_AVX512` — `VFMSUB132BF16`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
