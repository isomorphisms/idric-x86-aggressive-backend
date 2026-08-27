# VSHUFI32X4

`VSHUFI32X4` reorders its encoded scalar or vector elements according to an immediate, index vector, or fixed permutation. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `YMM MASK1 YMM MEM IMM`; `YMM MASK1 YMM YMM IMM`; `ZMM MASK1 ZMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VSHUFI32X4_YMMu32_MASKmskw_YMMu32_MEMu32_IMM8_AVX512` — `VSHUFI32X4`
- `VSHUFI32X4_YMMu32_MASKmskw_YMMu32_YMMu32_IMM8_AVX512` — `VSHUFI32X4`
- `VSHUFI32X4_ZMMu32_MASKmskw_ZMMu32_MEMu32_IMM8_AVX512` — `VSHUFI32X4`
- `VSHUFI32X4_ZMMu32_MASKmskw_ZMMu32_ZMMu32_IMM8_AVX512` — `VSHUFI32X4`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
