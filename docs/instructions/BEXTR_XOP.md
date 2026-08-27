# BEXTR_XOP

`BEXTR_XOP` extracts a variable contiguous bit field using AMD XOP's BEXTR encoding, with the start position and field length supplied by the control operand. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `TBM`
- XED category/categories: `TBM`
- ISA set(s): `TBM`
- vendor classification: `AMD`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `VGPR32 MEM IMM`; `VGPR32 VGPR32 IMM`; `VGPRy MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: `MUST [ cf-0 pf-u af-u zf-mod sf-u of-0 ]`.

## Important forms

- `BEXTR_XOP_GPR32d_GPR32d_IMMd` — `BEXTR_XOP`
- `BEXTR_XOP_GPR32d_MEMd_IMMd` — `BEXTR_XOP`
- `BEXTR_XOP_GPRyy_GPRyy_IMMd` — `BEXTR_XOP`
- `BEXTR_XOP_GPRyy_MEMy_IMMd` — `BEXTR_XOP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
