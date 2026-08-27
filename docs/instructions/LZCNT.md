# LZCNT

`LZCNT` counts leading zero bits. The pinned XED inventory represents it with 10 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `LZCNT`
- XED category/categories: `LZCNT`
- ISA set(s): `APX_F_LZCNT`, `APX_F_LZCNT_N3`, `LZCNT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: `MUST [ CF-MOD ZF-MOD OF-U AF-U PF-U SF-U ]`; `MUST [ cf-mod zf-mod of-u af-u pf-u sf-u ]`.

## Important forms

- `LZCNT_GPRv_GPRv` — `LZCNT`
- `LZCNT_GPRv_GPRv_APX` — `LZCNT`
- `LZCNT_GPRv_GPRv_APX_N3` — `LZCNT`
- `LZCNT_GPRv_MEMv` — `LZCNT`
- `LZCNT_GPRv_MEMv_APX` — `LZCNT`
- `LZCNT_GPRv_MEMv_APX_N3` — `LZCNT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
