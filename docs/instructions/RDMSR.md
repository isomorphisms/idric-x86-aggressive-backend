# RDMSR

`RDMSR` reads a model-specific register selected by ECX and returns its 64-bit value in EDX:EAX; ordinary user-mode code cannot execute it. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BASE`, `MSR_IMM`
- XED category/categories: `SYSTEM`, `VEX`
- ISA set(s): `APX_F_MSR_IMM`, `MSR_IMM`, `PENTIUMREAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

## Architectural effects

Representative explicit operands: `GPR64 IMM`; `VGPR64 IMM`. Representative implicit state: `EAX EDX ECX MSRS`; `MSRS`.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `RDMSR` — `RDMSR`
- `RDMSR_GPR64u64_IMM32` — `RDMSR`
- `RDMSR_GPR64u64_IMM32_APX` — `RDMSR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
