# MOVD

`MOVD` copies 32-bit doubleword elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 16 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `MMX`, `SSE2`
- XED category/categories: `DATAXFER`
- ISA set(s): `PENTIUMMMX`, `SSE2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR32 MMX`; `GPR32 XMM`; `MEM MMX`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `MOVD_GPR32_MMXd` — `MOVD`
- `MOVD_GPR32_XMMd` — `MOVD`
- `MOVD_MEMd_MMXd` — `MOVD`
- `MOVD_MEMd_XMMd` — `MOVD`
- `MOVD_MMXq_GPR32` — `MOVD`
- `MOVD_MMXq_MEMd` — `MOVD`
- `MOVD_XMMdq_GPR32` — `MOVD`
- `MOVD_XMMdq_MEMd` — `MOVD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
