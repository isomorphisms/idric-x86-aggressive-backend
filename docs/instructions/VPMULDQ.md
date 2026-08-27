# VPMULDQ

`VPMULDQ` multiplies corresponding double-quadword vector data and writes the lane-wise result. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX`, `AVX2`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX2`, `AVX512`
- ISA set(s): `AVX`, `AVX2`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPMULDQ_XMMdq_XMMdq_MEMdq` — `VPMULDQ`
- `VPMULDQ_XMMdq_XMMdq_XMMdq` — `VPMULDQ`
- `VPMULDQ_XMMi64_MASKmskw_XMMi64_MEMi64_AVX512` — `VPMULDQ`
- `VPMULDQ_XMMi64_MASKmskw_XMMi64_XMMi64_AVX512` — `VPMULDQ`
- `VPMULDQ_YMMi64_MASKmskw_YMMi64_MEMi64_AVX512` — `VPMULDQ`
- `VPMULDQ_YMMi64_MASKmskw_YMMi64_YMMi64_AVX512` — `VPMULDQ`
- `VPMULDQ_YMMqq_YMMqq_MEMqq` — `VPMULDQ`
- `VPMULDQ_YMMqq_YMMqq_YMMqq` — `VPMULDQ`
- `VPMULDQ_ZMMi64_MASKmskw_ZMMi64_MEMi64_AVX512` — `VPMULDQ`
- `VPMULDQ_ZMMi64_MASKmskw_ZMMi64_ZMMi64_AVX512` — `VPMULDQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
