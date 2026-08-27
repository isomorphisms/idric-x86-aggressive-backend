# VMOVUPS

`VMOVUPS` copies packed single-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 20 normalized encoding records and 17 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VMOVUPS_MEMdq_XMMdq` — `VMOVUPS`
- `VMOVUPS_MEMf32_MASKmskw_XMMf32_AVX512` — `VMOVUPS`
- `VMOVUPS_MEMf32_MASKmskw_YMMf32_AVX512` — `VMOVUPS`
- `VMOVUPS_MEMf32_MASKmskw_ZMMf32_AVX512` — `VMOVUPS`
- `VMOVUPS_MEMqq_YMMqq` — `VMOVUPS`
- `VMOVUPS_XMMdq_MEMdq` — `VMOVUPS`
- `VMOVUPS_XMMdq_XMMdq_10` — `VMOVUPS`
- `VMOVUPS_XMMdq_XMMdq_11` — `VMOVUPS`
- `VMOVUPS_XMMf32_MASKmskw_MEMf32_AVX512` — `VMOVUPS`
- `VMOVUPS_XMMf32_MASKmskw_XMMf32_AVX512` — `VMOVUPS`
- `VMOVUPS_YMMf32_MASKmskw_MEMf32_AVX512` — `VMOVUPS`
- `VMOVUPS_YMMf32_MASKmskw_YMMf32_AVX512` — `VMOVUPS`
- … 5 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
