# VFNMADD132PH

`VFNMADD132PH` computes a fused multiply/add-or-subtract operation on packed IEEE binary16 floating-point elements with one rounding step for each fused result. The pinned XED inventory represents it with 7 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `FP16`
- ISA set(s): `AVX512_FP16_128`, `AVX512_FP16_256`, `AVX512_FP16_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `YMM MASK1 YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VFNMADD132PH_XMMf16_MASKmskw_XMMf16_MEMf16_AVX512` — `VFNMADD132PH`
- `VFNMADD132PH_XMMf16_MASKmskw_XMMf16_XMMf16_AVX512` — `VFNMADD132PH`
- `VFNMADD132PH_YMMf16_MASKmskw_YMMf16_MEMf16_AVX512` — `VFNMADD132PH`
- `VFNMADD132PH_YMMf16_MASKmskw_YMMf16_YMMf16_AVX512` — `VFNMADD132PH`
- `VFNMADD132PH_ZMMf16_MASKmskw_ZMMf16_MEMf16_AVX512` — `VFNMADD132PH`
- `VFNMADD132PH_ZMMf16_MASKmskw_ZMMf16_ZMMf16_AVX512` — `VFNMADD132PH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
