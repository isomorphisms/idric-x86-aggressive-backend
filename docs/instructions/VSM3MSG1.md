# VSM3MSG1

`VSM3MSG1` performs the first SM3 message-schedule expansion transformation on packed 32-bit words. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `SM3`
- XED category/categories: `VEX`
- ISA set(s): `SM3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `VSM3MSG1_XMMu32_XMMu32_MEMu32` — `VSM3MSG1`
- `VSM3MSG1_XMMu32_XMMu32_XMMu32` — `VSM3MSG1`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
