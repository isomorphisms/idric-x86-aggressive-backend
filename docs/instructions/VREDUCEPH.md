# VREDUCEPH

`VREDUCEPH` reduces packed IEEE binary16 floating-point elements by subtracting an integer multiple of a power of two selected by immediate control, using the instruction's explicit rounding mode. The pinned XED inventory represents it with 7 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `FP16`
- ISA set(s): `AVX512_FP16_128`, `AVX512_FP16_256`, `AVX512_FP16_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 MEM IMM`; `XMM MASK1 XMM IMM`; `YMM MASK1 MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VREDUCEPH_XMMf16_MASKmskw_MEMf16_IMM8_AVX512` — `VREDUCEPH`
- `VREDUCEPH_XMMf16_MASKmskw_XMMf16_IMM8_AVX512` — `VREDUCEPH`
- `VREDUCEPH_YMMf16_MASKmskw_MEMf16_IMM8_AVX512` — `VREDUCEPH`
- `VREDUCEPH_YMMf16_MASKmskw_YMMf16_IMM8_AVX512` — `VREDUCEPH`
- `VREDUCEPH_ZMMf16_MASKmskw_MEMf16_IMM8_AVX512` — `VREDUCEPH`
- `VREDUCEPH_ZMMf16_MASKmskw_ZMMf16_IMM8_AVX512` — `VREDUCEPH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
