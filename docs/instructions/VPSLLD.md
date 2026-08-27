# VPSLLD

`VPSLLD` shifts packed integer elements left logically, filling vacated low bits with zeros; vector-count forms obtain counts from vector operands while immediate/scalar-count forms use their encoded count source. The pinned XED inventory represents it with 18 normalized encoding records and 18 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

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

- `VPSLLD_XMMdq_XMMdq_IMMb` — `VPSLLD`
- `VPSLLD_XMMdq_XMMdq_MEMdq` — `VPSLLD`
- `VPSLLD_XMMdq_XMMdq_XMMdq` — `VPSLLD`
- `VPSLLD_XMMu32_MASKmskw_MEMu32_IMM8_AVX512` — `VPSLLD`
- `VPSLLD_XMMu32_MASKmskw_XMMu32_IMM8_AVX512` — `VPSLLD`
- `VPSLLD_XMMu32_MASKmskw_XMMu32_MEMu32_AVX512` — `VPSLLD`
- `VPSLLD_XMMu32_MASKmskw_XMMu32_XMMu32_AVX512` — `VPSLLD`
- `VPSLLD_YMMqq_YMMqq_IMMb` — `VPSLLD`
- `VPSLLD_YMMqq_YMMqq_MEMdq` — `VPSLLD`
- `VPSLLD_YMMqq_YMMqq_XMMq` — `VPSLLD`
- `VPSLLD_YMMu32_MASKmskw_MEMu32_IMM8_AVX512` — `VPSLLD`
- `VPSLLD_YMMu32_MASKmskw_YMMu32_IMM8_AVX512` — `VPSLLD`
- … 6 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
