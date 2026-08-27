# VPINSRQ

`VPINSRQ` inserts a scalar 64-bit quadword from a register or memory source into the packed destination lane selected by the immediate index. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512DQ_128N`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM XMM GPR64 IMM`; `XMM XMM MEM IMM`; `XMM XMM VGPR64 IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPINSRQ_XMMdq_XMMdq_GPR64q_IMMb` — `VPINSRQ`
- `VPINSRQ_XMMdq_XMMdq_MEMq_IMMb` — `VPINSRQ`
- `VPINSRQ_XMMu64_XMMu64_GPR64u64_IMM8_AVX512` — `VPINSRQ`
- `VPINSRQ_XMMu64_XMMu64_MEMu64_IMM8_AVX512` — `VPINSRQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
