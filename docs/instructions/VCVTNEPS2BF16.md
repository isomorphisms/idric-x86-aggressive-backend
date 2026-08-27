# VCVTNEPS2BF16

`VCVTNEPS2BF16` converts values between the source and destination numerical formats encoded by the mnemonic. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`, `AVX_NE_CONVERT`
- XED category/categories: `CONVERT`
- ISA set(s): `AVX512_BF16_128`, `AVX512_BF16_256`, `AVX512_BF16_512`, `AVX_NE_CONVERT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `XMM MASK1 XMM`; `XMM MASK1 YMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VCVTNEPS2BF16_XMMbf16_MASKmskw_MEMf32_AVX512_VL128` — `VCVTNEPS2BF16`
- `VCVTNEPS2BF16_XMMbf16_MASKmskw_MEMf32_AVX512_VL256` — `VCVTNEPS2BF16`
- `VCVTNEPS2BF16_XMMbf16_MASKmskw_XMMf32_AVX512` — `VCVTNEPS2BF16`
- `VCVTNEPS2BF16_XMMbf16_MASKmskw_YMMf32_AVX512` — `VCVTNEPS2BF16`
- `VCVTNEPS2BF16_XMMbf16_MEMf32_VL128` — `VCVTNEPS2BF16`
- `VCVTNEPS2BF16_XMMbf16_MEMf32_VL256` — `VCVTNEPS2BF16`
- `VCVTNEPS2BF16_XMMbf16_XMMf32` — `VCVTNEPS2BF16`
- `VCVTNEPS2BF16_XMMbf16_YMMf32` — `VCVTNEPS2BF16`
- `VCVTNEPS2BF16_YMMbf16_MASKmskw_MEMf32_AVX512_VL512` — `VCVTNEPS2BF16`
- `VCVTNEPS2BF16_YMMbf16_MASKmskw_ZMMf32_AVX512` — `VCVTNEPS2BF16`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
