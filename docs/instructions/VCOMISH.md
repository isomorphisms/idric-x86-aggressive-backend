# VCOMISH

`VCOMISH` compares two scalar binary16 values, writes the integer condition flags used by branches and SET/CMOV instructions, and uses ordered-comparison exception behavior for NaNs. The pinned XED inventory represents it with 3 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `FP16`
- ISA set(s): `AVX512_FP16_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: `MUST [  zf-mod pf-mod cf-mod of-0 sf-0 af-0  ]`.

## Important forms

- `VCOMISH_XMMf16_MEMf16_AVX512` — `VCOMISH`
- `VCOMISH_XMMf16_XMMf16_AVX512` — `VCOMISH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
