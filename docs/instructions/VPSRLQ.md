# VPSRLQ

`VPSRLQ` shifts packed integer elements right logically, filling vacated high bits with zeros; vector-count forms permit per-element counts where the encoding provides them. The pinned XED inventory represents it with 18 normalized encoding records and 18 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX2`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX2`, `AVX512`
- ISA set(s): `AVX`, `AVX2`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 MEM IMM`; `XMM MASK1 XMM IMM`; `XMM MASK1 XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPSRLQ_XMMdq_XMMdq_IMMb` — `VPSRLQ`
- `VPSRLQ_XMMdq_XMMdq_MEMdq` — `VPSRLQ`
- `VPSRLQ_XMMdq_XMMdq_XMMdq` — `VPSRLQ`
- `VPSRLQ_XMMu64_MASKmskw_MEMu64_IMM8_AVX512` — `VPSRLQ`
- `VPSRLQ_XMMu64_MASKmskw_XMMu64_IMM8_AVX512` — `VPSRLQ`
- `VPSRLQ_XMMu64_MASKmskw_XMMu64_MEMu64_AVX512` — `VPSRLQ`
- `VPSRLQ_XMMu64_MASKmskw_XMMu64_XMMu64_AVX512` — `VPSRLQ`
- `VPSRLQ_YMMqq_YMMqq_IMMb` — `VPSRLQ`
- `VPSRLQ_YMMqq_YMMqq_MEMdq` — `VPSRLQ`
- `VPSRLQ_YMMqq_YMMqq_XMMq` — `VPSRLQ`
- `VPSRLQ_YMMu64_MASKmskw_MEMu64_IMM8_AVX512` — `VPSRLQ`
- `VPSRLQ_YMMu64_MASKmskw_YMMu64_IMM8_AVX512` — `VPSRLQ`
- … 6 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
