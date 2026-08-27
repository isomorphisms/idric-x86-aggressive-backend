# TZCNT

`TZCNT` counts trailing zero bits. The pinned XED inventory represents it with 10 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BMI1`
- XED category/categories: `BMI1`
- ISA set(s): `APX_F_BMI1`, `APX_F_BMI1_N3`, `BMI1`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: `MUST [ OF-U SF-U ZF-MOD AF-U PF-U CF-MOD ]`; `MUST [ of-u sf-u zf-mod af-u pf-u cf-mod ]`.

## Important forms

- `TZCNT_GPRv_GPRv` — `TZCNT`
- `TZCNT_GPRv_GPRv_APX` — `TZCNT`
- `TZCNT_GPRv_GPRv_APX_N3` — `TZCNT`
- `TZCNT_GPRv_MEMv` — `TZCNT`
- `TZCNT_GPRv_MEMv_APX` — `TZCNT`
- `TZCNT_GPRv_MEMv_APX_N3` — `TZCNT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
