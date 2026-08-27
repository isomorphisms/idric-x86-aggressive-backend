# VPSHLD

`VPSHLD` implements the distinct architectural operation named VPSHLD in XED category XOP; the pinned Intel/AMD reference defines its exact data transformation. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `AMD`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MEM XMM`; `XMM XMM MEM`; `XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VPSHLD_XMMdq_MEMdq_XMMdq` — `VPSHLD`
- `VPSHLD_XMMdq_XMMdq_MEMdq` — `VPSHLD`
- `VPSHLD_XMMdq_XMMdq_XMMdq` — `VPSHLD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
