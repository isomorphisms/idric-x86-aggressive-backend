# VMOVNTPS

`VMOVNTPS` moves packed single-precision floating-point elements using non-temporal memory semantics intended for streaming data. The pinned XED inventory represents it with 5 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `MEM XMM`; `MEM YMM`; `MEM ZMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VMOVNTPS_MEMdq_XMMdq` — `VMOVNTPS`
- `VMOVNTPS_MEMf32_XMMf32_AVX512` — `VMOVNTPS`
- `VMOVNTPS_MEMf32_YMMf32_AVX512` — `VMOVNTPS`
- `VMOVNTPS_MEMf32_ZMMf32_AVX512` — `VMOVNTPS`
- `VMOVNTPS_MEMqq_YMMqq` — `VMOVNTPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
