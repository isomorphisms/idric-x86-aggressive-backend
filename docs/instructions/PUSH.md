# PUSH

`PUSH` decrements the stack pointer and stores an operand on the current stack using the instruction's operand size. The pinned XED inventory represents it with 12 normalized encoding records and 11 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BASE`
- XED category/categories: `PUSH`
- ISA set(s): `I186`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPRv`; `IMM`; `MEM`. Representative implicit state: `CS STACKPUSH`; `DS STACKPUSH`; `ES STACKPUSH`; ….

Recorded flag behavior: not uniformly recorded.

## Important forms

- `PUSH_CS` — `PUSH`
- `PUSH_DS` — `PUSH`
- `PUSH_ES` — `PUSH`
- `PUSH_FS` — `PUSH`
- `PUSH_GPRv_50` — `PUSH`
- `PUSH_GPRv_FFr6` — `PUSH`
- `PUSH_GS` — `PUSH`
- `PUSH_IMMb` — `PUSH`
- `PUSH_IMMz` — `PUSH`
- `PUSH_MEMv` — `PUSH`
- `PUSH_SS` — `PUSH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this belongs to the small x86-64 user-mode baseline worth supporting early. Flag liveness, register constraints, and exact encoding choice should be explicit.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
