# VMOVRSW

`VMOVRSW` copies 16-bit word elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX10_MOVRS_128`, `AVX10_MOVRS_256`, `AVX10_MOVRS_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `YMM MASK1 MEM`; `ZMM MASK1 MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VMOVRSW_XMMu16_MASKmskw_MEMu16_AVX512` — `VMOVRSW`
- `VMOVRSW_YMMu16_MASKmskw_MEMu16_AVX512` — `VMOVRSW`
- `VMOVRSW_ZMMu16_MASKmskw_MEMu16_AVX512` — `VMOVRSW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
