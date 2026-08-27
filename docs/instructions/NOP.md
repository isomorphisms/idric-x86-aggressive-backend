# NOP

`NOP` performs no architectural data computation while consuming an instruction slot; multi-byte encodings are commonly used for alignment and patchable padding. The pinned XED inventory represents it with 58 normalized encoding records and 28 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BASE`
- XED category/categories: `NOP`, `WIDENOP`
- ISA set(s): `FAT_NOP`, `I86`, `PPRO`, `PREFETCH_NOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPRv`; `GPRv GPRv`; `GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `NOP_90` — `NOP`
- `NOP_GPRv_0F18r0` — `NOP`
- `NOP_GPRv_0F18r1` — `NOP`
- `NOP_GPRv_0F18r2` — `NOP`
- `NOP_GPRv_0F18r3` — `NOP`
- `NOP_GPRv_0F18r4` — `NOP`
- `NOP_GPRv_0F18r5` — `NOP`
- `NOP_GPRv_0F18r6` — `NOP`
- `NOP_GPRv_0F18r7` — `NOP`
- `NOP_GPRv_0F1F` — `NOP`
- `NOP_GPRv_GPRv_0F0D` — `NOP`
- `NOP_GPRv_GPRv_0F19` — `NOP`
- … 16 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
