# SYSRET_AMD

`SYSRET_AMD` implements the distinct architectural operation named SYSRET_AMD in XED category SYSRET; the pinned Intel/AMD reference defines its exact data transformation. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSRET`
- ISA set(s): `AMD`
- vendor classification: `AMD`
- XED mode restriction(s): `16 32`
- requires CPL 0; ordinary user-mode code must not emit it

## Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EIP`.

Recorded flag behavior: `MUST [ id-mod vip-mod vif-mod ac-mod rf-0 nt-mod iopl-mod of-mod df-mod if-mod tf-mod sf-mod zf-mod af-mod pf-mod cf-mod ]`.

## Important forms

- `SYSRET_AMD` — `SYSRET_AMD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
