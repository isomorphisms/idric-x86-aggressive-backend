# VGF2P8AFFINEQB

`VGF2P8AFFINEQB` applies a packed affine transformation over GF(2^8) to bytes. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`, `GFNI`
- XED category/categories: `GFNI`
- ISA set(s): `AVX512_GFNI_128`, `AVX512_GFNI_256`, `AVX512_GFNI_512`, `AVX_GFNI`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM IMM`; `XMM MASK1 XMM XMM IMM`; `XMM XMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VGF2P8AFFINEQB_XMMu8_MASKmskw_XMMu8_MEMu64_IMM8_AVX512` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_XMMu8_MASKmskw_XMMu8_XMMu64_IMM8_AVX512` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_XMMu8_XMMu8_MEMu64_IMM8` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_XMMu8_XMMu8_XMMu64_IMM8` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_YMMu8_MASKmskw_YMMu8_MEMu64_IMM8_AVX512` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_YMMu8_MASKmskw_YMMu8_YMMu64_IMM8_AVX512` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_YMMu8_YMMu8_MEMu64_IMM8` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_YMMu8_YMMu8_YMMu64_IMM8` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_ZMMu8_MASKmskw_ZMMu8_MEMu64_IMM8_AVX512` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_ZMMu8_MASKmskw_ZMMu8_ZMMu64_IMM8_AVX512` — `VGF2P8AFFINEQB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
