# CMP

`CMP` subtracts conceptually to set arithmetic flags for a comparison and discards the numerical result. The pinned XED inventory represents it with 18 normalized encoding records and 18 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `CMP_AL_IMMb` — `CMP`
- `CMP_GPR8_GPR8_38` — `CMP`
- `CMP_GPR8_GPR8_3A` — `CMP`
- `CMP_GPR8_IMMb_80r7` — `CMP`
- `CMP_GPR8_IMMb_82r7` — `CMP`
- `CMP_GPR8_MEMb` — `CMP`
- `CMP_GPRv_GPRv_39` — `CMP`
- `CMP_GPRv_GPRv_3B` — `CMP`
- `CMP_GPRv_IMMb` — `CMP`
- `CMP_GPRv_IMMz` — `CMP`
- `CMP_GPRv_MEMv` — `CMP`
- `CMP_MEMb_GPR8` — `CMP`
- … 6 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this belongs to the small x86-64 user-mode baseline worth supporting early. Flag liveness, register constraints, and exact encoding choice should be explicit.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
