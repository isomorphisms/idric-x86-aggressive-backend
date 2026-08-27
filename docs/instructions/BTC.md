# BTC

`BTC` copies a selected bit into carry and complements it. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BITBYTE`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv IMM`; `MEM GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: `MUST [ of-u sf-u af-u pf-u cf-mod ]`.

## Important forms

- `BTC_GPRv_GPRv` — `BTC`
- `BTC_GPRv_IMMb` — `BTC`
- `BTC_MEMv_GPRv` — `BTC`
- `BTC_MEMv_IMMb` — `BTC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
