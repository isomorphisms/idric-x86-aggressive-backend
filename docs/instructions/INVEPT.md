# INVEPT

`INVEPT` invalidates processor-maintained translation or virtualization-caching state selected by its operands. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `APX_F_VMX`, `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

## Architectural effects

Representative explicit operands: `GPR32 MEM`; `GPR64 MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: `MUST [ CF-MOD ZF-MOD SF-0 OF-0 AF-0 PF-0 ]`; `MUST [ cf-mod zf-mod sf-0 of-0 af-0 pf-0 ]`.

## Important forms

- `INVEPT_GPR32_MEMdq` — `INVEPT`
- `INVEPT_GPR64_MEMdq` — `INVEPT`
- `INVEPT_GPR64i64_MEMi128_APX` — `INVEPT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
