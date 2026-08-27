# VMOVDQU8

`VMOVDQU8` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 12 normalized encoding records and 9 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX512BW_128`, `AVX512BW_256`, `AVX512BW_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VMOVDQU8_MEMu8_MASKmskw_XMMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_MEMu8_MASKmskw_YMMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_MEMu8_MASKmskw_ZMMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_XMMu8_MASKmskw_MEMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_XMMu8_MASKmskw_XMMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_YMMu8_MASKmskw_MEMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_YMMu8_MASKmskw_YMMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_ZMMu8_MASKmskw_MEMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_ZMMu8_MASKmskw_ZMMu8_AVX512` — `VMOVDQU8`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
