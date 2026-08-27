# FIDIVR

`FIDIVR` divides values in the operand format encoded by the mnemonic (its encoded scalar or vector elements). The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `X87`
- XED category/categories: `X87_ALU`
- ISA set(s): `X87`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `ST0 X87STATUS`.

Recorded flag behavior: `MUST [ fc0-u   fc1-mod fc2-u   fc3-u   ]`.

## Important forms

- `FIDIVR_ST0_MEMmem16int` — `FIDIVR`
- `FIDIVR_ST0_MEMmem32int` — `FIDIVR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
