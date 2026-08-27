# BZHI

`BZHI` copies source bits below a variable bit index and clears higher bits. The pinned XED inventory represents it with 14 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BMI2`
- XED category/categories: `BMI2`
- ISA set(s): `APX_F_BMI2`, `APX_F_BMI2_N3`, `BMI2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR32 GPR32 GPR32`; `GPR32 MEM GPR32`; `GPR64 GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `BZHI_GPR32d_GPR32d_GPR32d` — `BZHI`
- `BZHI_GPR32d_MEMd_GPR32d` — `BZHI`
- `BZHI_GPR32i32_GPR32i32_GPR32i32_APX` — `BZHI`
- `BZHI_GPR32i32_GPR32i32_GPR32i32_APX_N3` — `BZHI`
- `BZHI_GPR32i32_MEMi32_GPR32i32_APX` — `BZHI`
- `BZHI_GPR32i32_MEMi32_GPR32i32_APX_N3` — `BZHI`
- `BZHI_GPR64i64_GPR64i64_GPR64i64_APX` — `BZHI`
- `BZHI_GPR64i64_GPR64i64_GPR64i64_APX_N3` — `BZHI`
- `BZHI_GPR64i64_MEMi64_GPR64i64_APX` — `BZHI`
- `BZHI_GPR64i64_MEMi64_GPR64i64_APX_N3` — `BZHI`
- `BZHI_GPR64q_GPR64q_GPR64q` — `BZHI`
- `BZHI_GPR64q_MEMq_GPR64q` — `BZHI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
