# VMOVW

`VMOVW` copies 16-bit word elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 8 normalized encoding records and 7 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX512_FP16_128N`, `AVX512_MOVZXC_128`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR32 XMM`; `MEM XMM`; `XMM GPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VMOVW_GPR32f16_XMMf16_AVX512` — `VMOVW`
- `VMOVW_MEMf16_XMMf16_AVX512` — `VMOVW`
- `VMOVW_MEMu16_XMMu16_AVX512_MOVZXC` — `VMOVW`
- `VMOVW_XMMf16_GPR32f16_AVX512` — `VMOVW`
- `VMOVW_XMMf16_MEMf16_AVX512` — `VMOVW`
- `VMOVW_XMMu16_MEMu16_AVX512_MOVZXC` — `VMOVW`
- `VMOVW_XMMu16_XMMu16_AVX512_MOVZXC` — `VMOVW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
