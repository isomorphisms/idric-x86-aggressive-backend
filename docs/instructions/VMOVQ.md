# VMOVQ

`VMOVQ` copies 64-bit quadword elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 16 normalized encoding records and 13 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128N`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR64 XMM`; `MEM XMM`; `VGPR64 XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VMOVQ_GPR64q_XMMq` — `VMOVQ`
- `VMOVQ_GPR64u64_XMMu64_AVX512` — `VMOVQ`
- `VMOVQ_MEMq_XMMq_7E` — `VMOVQ`
- `VMOVQ_MEMq_XMMq_D6` — `VMOVQ`
- `VMOVQ_MEMu64_XMMu64_AVX512` — `VMOVQ`
- `VMOVQ_XMMdq_GPR64q` — `VMOVQ`
- `VMOVQ_XMMdq_MEMq_6E` — `VMOVQ`
- `VMOVQ_XMMdq_MEMq_7E` — `VMOVQ`
- `VMOVQ_XMMdq_XMMq_7E` — `VMOVQ`
- `VMOVQ_XMMdq_XMMq_D6` — `VMOVQ`
- `VMOVQ_XMMu64_GPR64u64_AVX512` — `VMOVQ`
- `VMOVQ_XMMu64_MEMu64_AVX512` — `VMOVQ`
- … 1 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
