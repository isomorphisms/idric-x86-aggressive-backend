# JMP

`JMP` unconditionally transfers control to the encoded direct, indirect, absolute, or far target without saving a normal return address. The pinned XED inventory represents it with 6 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BASE`
- XED category/categories: `UNCOND_BR`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPRv`; `MEM`; `RELBR`. Representative implicit state: `EIP`; `RIP`; `rIP`.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `JMP_GPRv` — `JMP`
- `JMP_MEMv` — `JMP`
- `JMP_RELBRb` — `JMP`
- `JMP_RELBRd` — `JMP`
- `JMP_RELBRz` — `JMP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is directly relevant to control-flow lowering. Selection must preserve branch/call semantics while making relocation form, indirect-target behavior, prediction, and ABI effects explicit.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
