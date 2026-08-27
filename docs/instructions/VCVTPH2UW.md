# VCVTPH2UW

`VCVTPH2UW` converts values between the source and destination numerical formats encoded by the mnemonic. The pinned XED inventory represents it with 7 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `CONVERT`
- ISA set(s): `AVX512_FP16_128`, `AVX512_FP16_256`, `AVX512_FP16_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `XMM MASK1 XMM`; `YMM MASK1 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VCVTPH2UW_XMMu16_MASKmskw_MEMf16_AVX512` — `VCVTPH2UW`
- `VCVTPH2UW_XMMu16_MASKmskw_XMMf16_AVX512` — `VCVTPH2UW`
- `VCVTPH2UW_YMMu16_MASKmskw_MEMf16_AVX512` — `VCVTPH2UW`
- `VCVTPH2UW_YMMu16_MASKmskw_YMMf16_AVX512` — `VCVTPH2UW`
- `VCVTPH2UW_ZMMu16_MASKmskw_MEMf16_AVX512` — `VCVTPH2UW`
- `VCVTPH2UW_ZMMu16_MASKmskw_ZMMf16_AVX512` — `VCVTPH2UW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
