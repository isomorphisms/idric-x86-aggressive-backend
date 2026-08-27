# VPMOVZXWQ

`VPMOVZXWQ` copies 64-bit quadword elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX2`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX2`, `DATAXFER`
- ISA set(s): `AVX`, `AVX2`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `XMM MASK1 XMM`; `XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPMOVZXWQ_XMMdq_MEMd` — `VPMOVZXWQ`
- `VPMOVZXWQ_XMMdq_XMMd` — `VPMOVZXWQ`
- `VPMOVZXWQ_XMMi64_MASKmskw_MEMi16_AVX512` — `VPMOVZXWQ`
- `VPMOVZXWQ_XMMi64_MASKmskw_XMMi16_AVX512` — `VPMOVZXWQ`
- `VPMOVZXWQ_YMMi64_MASKmskw_MEMi16_AVX512` — `VPMOVZXWQ`
- `VPMOVZXWQ_YMMi64_MASKmskw_XMMi16_AVX512` — `VPMOVZXWQ`
- `VPMOVZXWQ_YMMqq_MEMq` — `VPMOVZXWQ`
- `VPMOVZXWQ_YMMqq_XMMq` — `VPMOVZXWQ`
- `VPMOVZXWQ_ZMMi64_MASKmskw_MEMi16_AVX512` — `VPMOVZXWQ`
- `VPMOVZXWQ_ZMMi64_MASKmskw_XMMi16_AVX512` — `VPMOVZXWQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
