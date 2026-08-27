# VFMADD132SD

`VFMADD132SD` computes a fused multiply/add-or-subtract operation on a scalar double-precision floating-point element with one rounding step for each fused result. The pinned XED inventory represents it with 5 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`, `FMA`
- XED category/categories: `VFMA`
- ISA set(s): `AVX512F_SCALAR`, `FMA`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VFMADD132SD_XMMdq_XMMq_MEMq` — `VFMADD132SD`
- `VFMADD132SD_XMMdq_XMMq_XMMq` — `VFMADD132SD`
- `VFMADD132SD_XMMf64_MASKmskw_XMMf64_MEMf64_AVX512` — `VFMADD132SD`
- `VFMADD132SD_XMMf64_MASKmskw_XMMf64_XMMf64_AVX512` — `VFMADD132SD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
