# VPROLVD

`VPROLVD` implements the distinct architectural operation named VPROLVD in XED category AVX512; the pinned Intel/AMD reference defines its exact data transformation. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `YMM MASK1 YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPROLVD_XMMu32_MASKmskw_XMMu32_MEMu32_AVX512` — `VPROLVD`
- `VPROLVD_XMMu32_MASKmskw_XMMu32_XMMu32_AVX512` — `VPROLVD`
- `VPROLVD_YMMu32_MASKmskw_YMMu32_MEMu32_AVX512` — `VPROLVD`
- `VPROLVD_YMMu32_MASKmskw_YMMu32_YMMu32_AVX512` — `VPROLVD`
- `VPROLVD_ZMMu32_MASKmskw_ZMMu32_MEMu32_AVX512` — `VPROLVD`
- `VPROLVD_ZMMu32_MASKmskw_ZMMu32_ZMMu32_AVX512` — `VPROLVD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
