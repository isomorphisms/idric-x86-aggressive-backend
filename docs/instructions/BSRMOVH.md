# BSRMOVH

`BSRMOVH` moves the high half of the ACE block-scale register between the block-scale state and a vector source or destination as defined by its form. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `ACE`
- XED category/categories: `AMX_TILE`
- ISA set(s): `ACE_1`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `MEM`; `ZMM`. Representative implicit state: `BSR0`.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `BSRMOVH_BSR0_MEMu64` — `BSRMOVH`
- `BSRMOVH_BSR0_ZMMu64` — `BSRMOVH`
- `BSRMOVH_MEMu64_BSR0` — `BSRMOVH`
- `BSRMOVH_ZMMu64_BSR0` — `BSRMOVH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
