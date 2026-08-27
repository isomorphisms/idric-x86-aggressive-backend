# VPSUBQ

`VPSUBQ` subtracts corresponding 64-bit quadword elements and writes the lane-wise result. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX2`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX2`, `AVX512`
- ISA set(s): `AVX`, `AVX2`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPSUBQ_XMMdq_XMMdq_MEMdq` — `VPSUBQ`
- `VPSUBQ_XMMdq_XMMdq_XMMdq` — `VPSUBQ`
- `VPSUBQ_XMMu64_MASKmskw_XMMu64_MEMu64_AVX512` — `VPSUBQ`
- `VPSUBQ_XMMu64_MASKmskw_XMMu64_XMMu64_AVX512` — `VPSUBQ`
- `VPSUBQ_YMMqq_YMMqq_MEMqq` — `VPSUBQ`
- `VPSUBQ_YMMqq_YMMqq_YMMqq` — `VPSUBQ`
- `VPSUBQ_YMMu64_MASKmskw_YMMu64_MEMu64_AVX512` — `VPSUBQ`
- `VPSUBQ_YMMu64_MASKmskw_YMMu64_YMMu64_AVX512` — `VPSUBQ`
- `VPSUBQ_ZMMu64_MASKmskw_ZMMu64_MEMu64_AVX512` — `VPSUBQ`
- `VPSUBQ_ZMMu64_MASKmskw_ZMMu64_ZMMu64_AVX512` — `VPSUBQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
