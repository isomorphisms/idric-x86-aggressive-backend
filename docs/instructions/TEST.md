# TEST

`TEST` computes a bitwise AND only to set logical flags and discards the result. The pinned XED inventory represents it with 14 normalized encoding records and 14 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `BASE`
- XED category/categories: `LOGICAL`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: `MUST [ of-0 sf-mod zf-mod af-u pf-mod cf-0 ]`.

## Important forms

- `TEST_AL_IMMb` — `TEST`
- `TEST_GPR8_GPR8` — `TEST`
- `TEST_GPR8_IMMb_F6r0` — `TEST`
- `TEST_GPR8_IMMb_F6r1` — `TEST`
- `TEST_GPRv_GPRv` — `TEST`
- `TEST_GPRv_IMMz_F7r0` — `TEST`
- `TEST_GPRv_IMMz_F7r1` — `TEST`
- `TEST_MEMb_GPR8` — `TEST`
- `TEST_MEMb_IMMb_F6r0` — `TEST`
- `TEST_MEMb_IMMb_F6r1` — `TEST`
- `TEST_MEMv_GPRv` — `TEST`
- `TEST_MEMv_IMMz_F7r0` — `TEST`
- … 2 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this belongs to the small x86-64 user-mode baseline worth supporting early. Flag liveness, register constraints, and exact encoding choice should be explicit.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
