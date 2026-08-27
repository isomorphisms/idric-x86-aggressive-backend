# VFPCLASSSH

`VFPCLASSSH` implements the distinct architectural operation named VFPCLASSSH in XED category FP16; the pinned Intel/AMD reference defines its exact data transformation. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `FP16`
- ISA set(s): `AVX512_FP16_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `MASK MASK1 MEM IMM`; `MASK MASK1 XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VFPCLASSSH_MASKmskw_MASKmskw_MEMf16_IMM8_AVX512` — `VFPCLASSSH`
- `VFPCLASSSH_MASKmskw_MASKmskw_XMMf16_IMM8_AVX512` — `VFPCLASSSH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
