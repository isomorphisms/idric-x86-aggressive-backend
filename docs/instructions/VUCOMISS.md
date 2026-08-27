# VUCOMISS

`VUCOMISS` implements the distinct architectural operation named VUCOMISS in XED category AVX, AVX512; the pinned Intel/AMD reference defines its exact data transformation. The pinned XED inventory represents it with 5 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: `MUST [ cf-mod zf-mod  pf-mod of-0 af-0 sf-0 ]`; `MUST [ zf-mod pf-mod cf-mod of-0 af-0 sf-0 ]`.

## Important forms

- `VUCOMISS_XMMdq_MEMd` — `VUCOMISS`
- `VUCOMISS_XMMdq_XMMd` — `VUCOMISS`
- `VUCOMISS_XMMf32_MEMf32_AVX512` — `VUCOMISS`
- `VUCOMISS_XMMf32_XMMf32_AVX512` — `VUCOMISS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
