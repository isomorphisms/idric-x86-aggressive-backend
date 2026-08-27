# VPDPBUSD

`VPDPBUSD` forms products of selected source elements and accumulates grouped dot-product sums. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `AVX512EVEX`, `AVX_VNNI`
- XED category/categories: `AVX512`, `VEX`
- ISA set(s): `AVX512_VNNI_128`, `AVX512_VNNI_256`, `AVX512_VNNI_512`, `AVX_VNNI`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPDPBUSD_XMMi32_MASKmskw_XMMu8_MEMu32_AVX512` — `VPDPBUSD`
- `VPDPBUSD_XMMi32_MASKmskw_XMMu8_XMMu32_AVX512` — `VPDPBUSD`
- `VPDPBUSD_XMMi32_XMMu32_MEMu32` — `VPDPBUSD`
- `VPDPBUSD_XMMi32_XMMu32_XMMu32` — `VPDPBUSD`
- `VPDPBUSD_YMMi32_MASKmskw_YMMu8_MEMu32_AVX512` — `VPDPBUSD`
- `VPDPBUSD_YMMi32_MASKmskw_YMMu8_YMMu32_AVX512` — `VPDPBUSD`
- `VPDPBUSD_YMMi32_YMMu32_MEMu32` — `VPDPBUSD`
- `VPDPBUSD_YMMi32_YMMu32_YMMu32` — `VPDPBUSD`
- `VPDPBUSD_ZMMi32_MASKmskw_ZMMu8_MEMu32_AVX512` — `VPDPBUSD`
- `VPDPBUSD_ZMMi32_MASKmskw_ZMMu8_ZMMu32_AVX512` — `VPDPBUSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
