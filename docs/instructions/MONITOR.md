# MONITOR

`MONITOR` arms hardware monitoring of a memory address for use with MWAIT. The pinned XED inventory represents it with 4 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `MONITOR`
- XED category/categories: `MISC`
- ISA set(s): `MONITOR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

## Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `AX ECX EDX`; `EAX ECX EDX`; `RAX ECX EDX`.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `MONITOR` — `MONITOR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
