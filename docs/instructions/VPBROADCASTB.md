# VPBROADCASTB

`VPBROADCASTB` replicates a scalar or smaller source value across destination lanes as byte elements. The pinned XED inventory represents it with 13 normalized encoding records and 13 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX2`, `AVX512EVEX`
- XED category/categories: `BROADCAST`
- ISA set(s): `AVX2`, `AVX512BW_128`, `AVX512BW_256`, `AVX512BW_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 GPR32`; `XMM MASK1 MEM`; `XMM MASK1 XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPBROADCASTB_XMMdq_MEMb` — `VPBROADCASTB`
- `VPBROADCASTB_XMMdq_XMMb` — `VPBROADCASTB`
- `VPBROADCASTB_XMMu8_MASKmskw_GPR32u8_AVX512` — `VPBROADCASTB`
- `VPBROADCASTB_XMMu8_MASKmskw_MEMu8_AVX512` — `VPBROADCASTB`
- `VPBROADCASTB_XMMu8_MASKmskw_XMMu8_AVX512` — `VPBROADCASTB`
- `VPBROADCASTB_YMMqq_MEMb` — `VPBROADCASTB`
- `VPBROADCASTB_YMMqq_XMMb` — `VPBROADCASTB`
- `VPBROADCASTB_YMMu8_MASKmskw_GPR32u8_AVX512` — `VPBROADCASTB`
- `VPBROADCASTB_YMMu8_MASKmskw_MEMu8_AVX512` — `VPBROADCASTB`
- `VPBROADCASTB_YMMu8_MASKmskw_XMMu8_AVX512` — `VPBROADCASTB`
- `VPBROADCASTB_ZMMu8_MASKmskw_GPR32u8_AVX512` — `VPBROADCASTB`
- `VPBROADCASTB_ZMMu8_MASKmskw_MEMu8_AVX512` — `VPBROADCASTB`
- … 1 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
