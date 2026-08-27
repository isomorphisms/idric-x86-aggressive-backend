# VUNPCKHPD

`VUNPCKHPD` interleaves high or low portions of source vectors containing packed double-precision floating-point elements. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VUNPCKHPD_XMMdq_XMMdq_MEMdq` — `VUNPCKHPD`
- `VUNPCKHPD_XMMdq_XMMdq_XMMdq` — `VUNPCKHPD`
- `VUNPCKHPD_XMMf64_MASKmskw_XMMf64_MEMf64_AVX512` — `VUNPCKHPD`
- `VUNPCKHPD_XMMf64_MASKmskw_XMMf64_XMMf64_AVX512` — `VUNPCKHPD`
- `VUNPCKHPD_YMMf64_MASKmskw_YMMf64_MEMf64_AVX512` — `VUNPCKHPD`
- `VUNPCKHPD_YMMf64_MASKmskw_YMMf64_YMMf64_AVX512` — `VUNPCKHPD`
- `VUNPCKHPD_YMMqq_YMMqq_MEMqq` — `VUNPCKHPD`
- `VUNPCKHPD_YMMqq_YMMqq_YMMqq` — `VUNPCKHPD`
- `VUNPCKHPD_ZMMf64_MASKmskw_ZMMf64_MEMf64_AVX512` — `VUNPCKHPD`
- `VUNPCKHPD_ZMMf64_MASKmskw_ZMMf64_ZMMf64_AVX512` — `VUNPCKHPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
