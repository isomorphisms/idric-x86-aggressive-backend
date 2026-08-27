# POP

`POP` loads a value from the current stack and increments the stack pointer, moving stack data into a register, memory location, or selected segment register. The pinned XED inventory represents it with 9 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BASE`
- XED category/categories: `POP`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPRv`; `MEM`. Representative implicit state: `DS STACKPOP`; `ES STACKPOP`; `FS STACKPOP`; ….

Recorded flag behavior: not uniformly recorded.

## Important forms

- `POP_DS` — `POP`
- `POP_ES` — `POP`
- `POP_FS` — `POP`
- `POP_GPRv_58` — `POP`
- `POP_GPRv_8F` — `POP`
- `POP_GS` — `POP`
- `POP_MEMv` — `POP`
- `POP_SS` — `POP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this belongs to the small x86-64 user-mode baseline worth supporting early. Flag liveness, register constraints, and exact encoding choice should be explicit.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
