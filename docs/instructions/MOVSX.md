# MOVSX

`MOVSX` copies a smaller signed integer and sign-extends it. The pinned XED inventory represents it with 7 normalized encoding records and 7 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DATAXFER`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR16 MEM`; `GPR32 MEM`; `GPR64 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `MOVSX_GPR16_MEMw` — `MOVSX`
- `MOVSX_GPR32_MEMw` — `MOVSX`
- `MOVSX_GPR64_MEMw` — `MOVSX`
- `MOVSX_GPRv_GPR16` — `MOVSX`
- `MOVSX_GPRv_GPR8` — `MOVSX`
- `MOVSX_GPRv_MEMb` — `MOVSX`
- `MOVSX_GPRv_MEMw` — `MOVSX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
