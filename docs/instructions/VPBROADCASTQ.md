# VPBROADCASTQ

`VPBROADCASTQ` replicates a scalar or smaller source value across destination lanes as 64-bit quadword elements. The pinned XED inventory represents it with 13 normalized encoding records and 13 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX2`, `AVX512EVEX`
- XED category/categories: `BROADCAST`
- ISA set(s): `AVX2`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 GPR64`; `XMM MASK1 MEM`; `XMM MASK1 XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPBROADCASTQ_XMMdq_MEMq` — `VPBROADCASTQ`
- `VPBROADCASTQ_XMMdq_XMMq` — `VPBROADCASTQ`
- `VPBROADCASTQ_XMMu64_MASKmskw_GPR64u64_AVX512` — `VPBROADCASTQ`
- `VPBROADCASTQ_XMMu64_MASKmskw_MEMu64_AVX512` — `VPBROADCASTQ`
- `VPBROADCASTQ_XMMu64_MASKmskw_XMMu64_AVX512` — `VPBROADCASTQ`
- `VPBROADCASTQ_YMMqq_MEMq` — `VPBROADCASTQ`
- `VPBROADCASTQ_YMMqq_XMMq` — `VPBROADCASTQ`
- `VPBROADCASTQ_YMMu64_MASKmskw_GPR64u64_AVX512` — `VPBROADCASTQ`
- `VPBROADCASTQ_YMMu64_MASKmskw_MEMu64_AVX512` — `VPBROADCASTQ`
- `VPBROADCASTQ_YMMu64_MASKmskw_XMMu64_AVX512` — `VPBROADCASTQ`
- `VPBROADCASTQ_ZMMu64_MASKmskw_GPR64u64_AVX512` — `VPBROADCASTQ`
- `VPBROADCASTQ_ZMMu64_MASKmskw_MEMu64_AVX512` — `VPBROADCASTQ`
- … 1 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
