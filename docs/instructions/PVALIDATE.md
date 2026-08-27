# PVALIDATE

`PVALIDATE` validates or rescinds validation of an AMD SEV-SNP guest page's reverse-map-table entry and returns status through EAX and flags. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `SNP`
- XED category/categories: `SYSTEM`
- ISA set(s): `SNP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

## Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RAX ECX EDX`.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `PVALIDATE_RAX_ECX_EDX` — `PVALIDATE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
