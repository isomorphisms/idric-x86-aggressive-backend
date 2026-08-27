# SYSENTER

`SYSENTER` enters a privileged operating-system service routine through model-specific fast-system-call state. The pinned XED inventory represents it with 2 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSCALL`
- ISA set(s): `SEP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EIP ESP`; `RIP RSP`.

Recorded flag behavior: `MUST [ vm-0 rf-0 if-0 ]`.

## Important forms

- `SYSENTER` — `SYSENTER`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is directly relevant to control-flow lowering. Selection must preserve branch/call semantics while making relocation form, indirect-target behavior, prediction, and ABI effects explicit.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
