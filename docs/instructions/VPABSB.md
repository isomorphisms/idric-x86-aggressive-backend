# VPABSB

`VPABSB` takes absolute values of byte elements and writes the lane-wise result. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX2`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX2`, `AVX512`
- ISA set(s): `AVX`, `AVX2`, `AVX512BW_128`, `AVX512BW_256`, `AVX512BW_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `XMM MASK1 XMM`; `XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPABSB_XMMdq_MEMdq` — `VPABSB`
- `VPABSB_XMMdq_XMMdq` — `VPABSB`
- `VPABSB_XMMi8_MASKmskw_MEMi8_AVX512` — `VPABSB`
- `VPABSB_XMMi8_MASKmskw_XMMi8_AVX512` — `VPABSB`
- `VPABSB_YMMi8_MASKmskw_MEMi8_AVX512` — `VPABSB`
- `VPABSB_YMMi8_MASKmskw_YMMi8_AVX512` — `VPABSB`
- `VPABSB_YMMqq_MEMqq` — `VPABSB`
- `VPABSB_YMMqq_YMMqq` — `VPABSB`
- `VPABSB_ZMMi8_MASKmskw_MEMi8_AVX512` — `VPABSB`
- `VPABSB_ZMMi8_MASKmskw_ZMMi8_AVX512` — `VPABSB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
