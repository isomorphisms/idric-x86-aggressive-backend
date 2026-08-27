# VP2INTERSECTD

`VP2INTERSECTD` implements the distinct architectural operation named VP2INTERSECTD in XED category AVX512_VP2INTERSECT; the pinned Intel/AMD reference defines its exact data transformation. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512_VP2INTERSECT`
- ISA set(s): `AVX512_VP2INTERSECT_128`, `AVX512_VP2INTERSECT_256`, `AVX512_VP2INTERSECT_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `MASK XMM MEM`; `MASK XMM XMM`; `MASK YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VP2INTERSECTD_MASKmskw_XMMu32_MEMu32_AVX512` — `VP2INTERSECTD`
- `VP2INTERSECTD_MASKmskw_XMMu32_XMMu32_AVX512` — `VP2INTERSECTD`
- `VP2INTERSECTD_MASKmskw_YMMu32_MEMu32_AVX512` — `VP2INTERSECTD`
- `VP2INTERSECTD_MASKmskw_YMMu32_YMMu32_AVX512` — `VP2INTERSECTD`
- `VP2INTERSECTD_MASKmskw_ZMMu32_MEMu32_AVX512` — `VP2INTERSECTD`
- `VP2INTERSECTD_MASKmskw_ZMMu32_ZMMu32_AVX512` — `VP2INTERSECTD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
