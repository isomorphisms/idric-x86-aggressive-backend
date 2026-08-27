# SAR

`SAR` shifts the destination arithmetically right, replicating the sign bit. The pinned XED inventory represents it with 84 normalized encoding records and 48 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SHIFT`
- ISA set(s): `APX_F`, `APX_F_N3`, `I186`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR8`; `GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `CL`; `IMM`.

Recorded flag behavior: `IMM1 MUST [ OF-MOD SF-MOD ZF-MOD AF-U PF-MOD CF-MOD ], IMMx MUST [ OF-U SF-MOD ZF-MOD AF-U PF-MOD CF-MOD ]`; `IMM1 MUST [ of-mod sf-mod zf-mod af-u pf-mod cf-mod ], IMMx MUST [ of-u sf-mod zf-mod af-u pf-mod cf-mod ]`; `MAY [ OF-U SF-MOD ZF-MOD AF-U PF-MOD CF-MOD ]`; ….

## Important forms

- `SAR_GPR8_CL` — `SAR`
- `SAR_GPR8_IMMb` — `SAR`
- `SAR_GPR8_ONE` — `SAR`
- `SAR_GPR8i8_CL_APX` — `SAR`
- `SAR_GPR8i8_CL_APX_N3` — `SAR`
- `SAR_GPR8i8_GPR8i8_CL_APX_N3` — `SAR`
- `SAR_GPR8i8_GPR8i8_IMM8_APX_N3` — `SAR`
- `SAR_GPR8i8_GPR8i8_ONE_APX_N3` — `SAR`
- `SAR_GPR8i8_IMM8_APX` — `SAR`
- `SAR_GPR8i8_IMM8_APX_N3` — `SAR`
- `SAR_GPR8i8_MEMi8_CL_APX_N3` — `SAR`
- `SAR_GPR8i8_MEMi8_IMM8_APX_N3` — `SAR`
- … 36 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
