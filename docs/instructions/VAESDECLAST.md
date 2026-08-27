# VAESDECLAST

`VAESDECLAST` performs an AES decryption-round transformation on packed 128-bit AES state blocks using the supplied round key without inverse MixColumns for the final-round form. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`, `AVXAES`, `VAES`
- XED category/categories: `AES`, `VAES`
- ISA set(s): `AVX512_VAES_128`, `AVX512_VAES_256`, `AVX512_VAES_512`, `AVXAES`, `VAES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VAESDECLAST_XMMdq_XMMdq_MEMdq` — `VAESDECLAST`
- `VAESDECLAST_XMMdq_XMMdq_XMMdq` — `VAESDECLAST`
- `VAESDECLAST_XMMu128_XMMu128_MEMu128_AVX512` — `VAESDECLAST`
- `VAESDECLAST_XMMu128_XMMu128_XMMu128_AVX512` — `VAESDECLAST`
- `VAESDECLAST_YMMu128_YMMu128_MEMu128` — `VAESDECLAST`
- `VAESDECLAST_YMMu128_YMMu128_MEMu128_AVX512` — `VAESDECLAST`
- `VAESDECLAST_YMMu128_YMMu128_YMMu128` — `VAESDECLAST`
- `VAESDECLAST_YMMu128_YMMu128_YMMu128_AVX512` — `VAESDECLAST`
- `VAESDECLAST_ZMMu128_ZMMu128_MEMu128_AVX512` — `VAESDECLAST`
- `VAESDECLAST_ZMMu128_ZMMu128_ZMMu128_AVX512` — `VAESDECLAST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
