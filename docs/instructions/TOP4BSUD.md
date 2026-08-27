# TOP4BSUD

`TOP4BSUD` computes an ACE four-way low-precision integer tile outer-product and accumulates widened products, with signedness selected by the mnemonic. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `ACE`
- XED category/categories: `AMX_TILE`
- ISA set(s): `ACE_1`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `TMM ZMM ZMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `TOP4BSUD_TMMu32_ZMMi8_ZMMu8` — `TOP4BSUD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
