# VPCOMPRESSW

`VPCOMPRESSW` packs mask-selected active 16-bit word elements contiguously into low lanes or memory. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `COMPRESS`
- ISA set(s): `AVX512_VBMI2_128`, `AVX512_VBMI2_256`, `AVX512_VBMI2_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPCOMPRESSW_MEMu16_MASKmskw_XMMu16_AVX512` — `VPCOMPRESSW`
- `VPCOMPRESSW_MEMu16_MASKmskw_YMMu16_AVX512` — `VPCOMPRESSW`
- `VPCOMPRESSW_MEMu16_MASKmskw_ZMMu16_AVX512` — `VPCOMPRESSW`
- `VPCOMPRESSW_XMMu16_MASKmskw_XMMu16_AVX512` — `VPCOMPRESSW`
- `VPCOMPRESSW_YMMu16_MASKmskw_YMMu16_AVX512` — `VPCOMPRESSW`
- `VPCOMPRESSW_ZMMu16_MASKmskw_ZMMu16_AVX512` — `VPCOMPRESSW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
