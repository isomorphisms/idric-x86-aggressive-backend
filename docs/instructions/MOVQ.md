# MOVQ

`MOVQ` copies 64-bit quadword elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 16 normalized encoding records and 16 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `MMX`, `SSE2`
- XED category/categories: `DATAXFER`
- ISA set(s): `PENTIUMMMX`, `SSE2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR64 MMX`; `GPR64 XMM`; `MEM MMX`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `MOVQ_GPR64_MMXq` — `MOVQ`
- `MOVQ_GPR64_XMMq` — `MOVQ`
- `MOVQ_MEMq_MMXq_0F7E` — `MOVQ`
- `MOVQ_MEMq_MMXq_0F7F` — `MOVQ`
- `MOVQ_MEMq_XMMq_0F7E` — `MOVQ`
- `MOVQ_MEMq_XMMq_0FD6` — `MOVQ`
- `MOVQ_MMXq_GPR64` — `MOVQ`
- `MOVQ_MMXq_MEMq_0F6E` — `MOVQ`
- `MOVQ_MMXq_MEMq_0F6F` — `MOVQ`
- `MOVQ_MMXq_MMXq_0F6F` — `MOVQ`
- `MOVQ_MMXq_MMXq_0F7F` — `MOVQ`
- `MOVQ_XMMdq_GPR64` — `MOVQ`
- … 4 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
