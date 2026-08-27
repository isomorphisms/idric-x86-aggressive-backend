# URDMSR

`URDMSR` reads an operating-system-authorized user-mode MSR through the user-MSR facility without granting arbitrary RDMSR privilege. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `USER_MSR`
- XED category/categories: `APX`, `USER_MSR`
- ISA set(s): `APX_F_USER_MSR`, `USER_MSR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR64 GPR64`; `GPR64 IMM`; `VGPR64 IMM`. Representative implicit state: `MSRS`.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `URDMSR_GPR64u64_GPR64u64` — `URDMSR`
- `URDMSR_GPR64u64_GPR64u64_APX` — `URDMSR`
- `URDMSR_GPR64u64_IMM32` — `URDMSR`
- `URDMSR_GPR64u64_IMM32_APX` — `URDMSR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
