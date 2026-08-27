# VPGATHERDD

`VPGATHERDD` loads non-contiguous memory elements selected by vector indices into 32-bit doubleword elements lanes. The pinned XED inventory represents it with 5 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX2GATHER`, `AVX512EVEX`
- XED category/categories: `AVX2GATHER`, `GATHER`
- ISA set(s): `AVX2GATHER`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASKNOT0 MEM`; `XMM MEM XMM`; `YMM MASKNOT0 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPGATHERDD_XMMu32_MASKmskw_MEMu32_AVX512_VL128` — `VPGATHERDD`
- `VPGATHERDD_XMMu32_MEMd_XMMi32_VL128` — `VPGATHERDD`
- `VPGATHERDD_YMMu32_MASKmskw_MEMu32_AVX512_VL256` — `VPGATHERDD`
- `VPGATHERDD_YMMu32_MEMd_YMMi32_VL256` — `VPGATHERDD`
- `VPGATHERDD_ZMMu32_MASKmskw_MEMu32_AVX512_VL512` — `VPGATHERDD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
