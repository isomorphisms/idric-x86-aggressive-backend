# VPSHUFLW

`VPSHUFLW` reorders 16-bit word elements according to an immediate, index vector, or fixed permutation. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX2`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX2`, `AVX512`
- ISA set(s): `AVX`, `AVX2`, `AVX512BW_128`, `AVX512BW_256`, `AVX512BW_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 MEM IMM`; `XMM MASK1 XMM IMM`; `XMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPSHUFLW_XMMdq_MEMdq_IMMb` — `VPSHUFLW`
- `VPSHUFLW_XMMdq_XMMdq_IMMb` — `VPSHUFLW`
- `VPSHUFLW_XMMu16_MASKmskw_MEMu16_IMM8_AVX512` — `VPSHUFLW`
- `VPSHUFLW_XMMu16_MASKmskw_XMMu16_IMM8_AVX512` — `VPSHUFLW`
- `VPSHUFLW_YMMqq_MEMqq_IMMb` — `VPSHUFLW`
- `VPSHUFLW_YMMqq_YMMqq_IMMb` — `VPSHUFLW`
- `VPSHUFLW_YMMu16_MASKmskw_MEMu16_IMM8_AVX512` — `VPSHUFLW`
- `VPSHUFLW_YMMu16_MASKmskw_YMMu16_IMM8_AVX512` — `VPSHUFLW`
- `VPSHUFLW_ZMMu16_MASKmskw_MEMu16_IMM8_AVX512` — `VPSHUFLW`
- `VPSHUFLW_ZMMu16_MASKmskw_ZMMu16_IMM8_AVX512` — `VPSHUFLW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
