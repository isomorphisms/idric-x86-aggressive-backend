# VSM4RNDS4

`VSM4RNDS4` implements the distinct architectural operation named VSM4RNDS4 in XED category AVX512, VEX; the pinned Intel/AMD reference defines its exact data transformation. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`, `SM4`
- XED category/categories: `AVX512`, `VEX`
- ISA set(s): `SM4`, `SM4_128`, `SM4_256`, `SM4_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VSM4RNDS4_XMMu32_XMMu32_MEMu32` — `VSM4RNDS4`
- `VSM4RNDS4_XMMu32_XMMu32_MEMu32_AVX512` — `VSM4RNDS4`
- `VSM4RNDS4_XMMu32_XMMu32_XMMu32` — `VSM4RNDS4`
- `VSM4RNDS4_XMMu32_XMMu32_XMMu32_AVX512` — `VSM4RNDS4`
- `VSM4RNDS4_YMMu32_YMMu32_MEMu32` — `VSM4RNDS4`
- `VSM4RNDS4_YMMu32_YMMu32_MEMu32_AVX512` — `VSM4RNDS4`
- `VSM4RNDS4_YMMu32_YMMu32_YMMu32` — `VSM4RNDS4`
- `VSM4RNDS4_YMMu32_YMMu32_YMMu32_AVX512` — `VSM4RNDS4`
- `VSM4RNDS4_ZMMu32_ZMMu32_MEMu32_AVX512` — `VSM4RNDS4`
- `VSM4RNDS4_ZMMu32_ZMMu32_ZMMu32_AVX512` — `VSM4RNDS4`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
