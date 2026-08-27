# VPERMIL2PS

`VPERMIL2PS` reorders packed single-precision floating-point elements according to an immediate, index vector, or fixed permutation. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM XMM MEM XMM IMM`; `XMM XMM XMM MEM IMM`; `XMM XMM XMM XMM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPERMIL2PS_XMMdq_XMMdq_MEMdq_XMMdq_IMMb` — `VPERMIL2PS`
- `VPERMIL2PS_XMMdq_XMMdq_XMMdq_MEMdq_IMMb` — `VPERMIL2PS`
- `VPERMIL2PS_XMMdq_XMMdq_XMMdq_XMMdq_IMMb` — `VPERMIL2PS`
- `VPERMIL2PS_YMMqq_YMMqq_MEMqq_YMMqq_IMMb` — `VPERMIL2PS`
- `VPERMIL2PS_YMMqq_YMMqq_YMMqq_MEMqq_IMMb` — `VPERMIL2PS`
- `VPERMIL2PS_YMMqq_YMMqq_YMMqq_YMMqq_IMMb` — `VPERMIL2PS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
