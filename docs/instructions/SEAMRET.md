# SEAMRET

`SEAMRET` returns from SEAM VMX-root operation to the calling legacy VMX-root environment. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `TDX`
- XED category/categories: `LEGACY`
- ISA set(s): `TDX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

## Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: `MUST [  zf-mod  cf-mod  pf-0  of-0  sf-0  af-0  ]`.

## Important forms

- `SEAMRET` — `SEAMRET`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
