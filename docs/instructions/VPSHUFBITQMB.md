# VPSHUFBITQMB

`VPSHUFBITQMB` reorders byte elements according to an immediate, index vector, or fixed permutation. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`, `AVX512_BITALG`
- ISA set(s): `AVX512_BITALG_128`, `AVX512_BITALG_256`, `AVX512_BITALG_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `MASK MASK1 XMM MEM`; `MASK MASK1 XMM XMM`; `MASK MASK1 YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPSHUFBITQMB_MASKmskw_MASKmskw_XMMu64_MEMu8_AVX512` — `VPSHUFBITQMB`
- `VPSHUFBITQMB_MASKmskw_MASKmskw_XMMu64_XMMu8_AVX512` — `VPSHUFBITQMB`
- `VPSHUFBITQMB_MASKmskw_MASKmskw_YMMu64_MEMu8_AVX512` — `VPSHUFBITQMB`
- `VPSHUFBITQMB_MASKmskw_MASKmskw_YMMu64_YMMu8_AVX512` — `VPSHUFBITQMB`
- `VPSHUFBITQMB_MASKmskw_MASKmskw_ZMMu64_MEMu8_AVX512` — `VPSHUFBITQMB`
- `VPSHUFBITQMB_MASKmskw_MASKmskw_ZMMu64_ZMMu8_AVX512` — `VPSHUFBITQMB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
