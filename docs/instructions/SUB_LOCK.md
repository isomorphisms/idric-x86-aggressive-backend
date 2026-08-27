# SUB_LOCK

`SUB_LOCK` subtracts the source from the destination and writes the difference while updating arithmetic flags; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `MEM GPR8`; `MEM GPRv`; `MEM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: `MUST [ of-mod sf-mod zf-mod af-mod pf-mod cf-mod ]`.

## Important forms

- `SUB_LOCK_MEMb_GPR8` — `SUB_LOCK`
- `SUB_LOCK_MEMb_IMMb_80r5` — `SUB_LOCK`
- `SUB_LOCK_MEMb_IMMb_82r5` — `SUB_LOCK`
- `SUB_LOCK_MEMv_GPRv` — `SUB_LOCK`
- `SUB_LOCK_MEMv_IMMb` — `SUB_LOCK`
- `SUB_LOCK_MEMv_IMMz` — `SUB_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
