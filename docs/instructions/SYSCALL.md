# SYSCALL

`SYSCALL` enters an operating-system system-call handler through model-specific entry state, saving the user return location in registers rather than building a normal call frame. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `LONGMODE`
- XED category/categories: `SYSCALL`
- ISA set(s): `LONGMODE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RIP RCX R11`.

Recorded flag behavior: `MUST [ id-mod vip-mod vif-mod ac-mod vm-0 rf-0 nt-mod iopl-mod of-mod df-mod if-mod tf-mod sf-mod zf-mod af-mod pf-mod cf-mod ]`.

## Important forms

- `SYSCALL` — `SYSCALL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is directly relevant to control-flow lowering. Selection must preserve branch/call semantics while making relocation form, indirect-target behavior, prediction, and ABI effects explicit.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
