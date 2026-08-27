# VPSRAVD

`VPSRAVD` shifts packed signed integer elements right arithmetically, replicating each element's sign bit into the vacated high positions. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX2`, `AVX512EVEX`
- XED category/categories: `AVX2`, `AVX512`
- ISA set(s): `AVX2`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPSRAVD_XMMdq_XMMdq_MEMdq` — `VPSRAVD`
- `VPSRAVD_XMMdq_XMMdq_XMMdq` — `VPSRAVD`
- `VPSRAVD_XMMu32_MASKmskw_XMMu32_MEMu32_AVX512` — `VPSRAVD`
- `VPSRAVD_XMMu32_MASKmskw_XMMu32_XMMu32_AVX512` — `VPSRAVD`
- `VPSRAVD_YMMqq_YMMqq_MEMqq` — `VPSRAVD`
- `VPSRAVD_YMMqq_YMMqq_YMMqq` — `VPSRAVD`
- `VPSRAVD_YMMu32_MASKmskw_YMMu32_MEMu32_AVX512` — `VPSRAVD`
- `VPSRAVD_YMMu32_MASKmskw_YMMu32_YMMu32_AVX512` — `VPSRAVD`
- `VPSRAVD_ZMMu32_MASKmskw_ZMMu32_MEMu32_AVX512` — `VPSRAVD`
- `VPSRAVD_ZMMu32_MASKmskw_ZMMu32_ZMMu32_AVX512` — `VPSRAVD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
