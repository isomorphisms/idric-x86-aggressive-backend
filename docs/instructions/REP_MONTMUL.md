# REP_MONTMUL

`REP_MONTMUL` repeats a VIA PadLock cryptographic or hashing primitive over a buffer using implicit registers for state, addresses, and count. The pinned XED inventory represents it with 2 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `VIA_PADLOCK_MONTMUL`
- XED category/categories: `VIA_PADLOCK`
- ISA set(s): `VIA_PADLOCK_MONTMUL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX ECX EDX MEM ArSI FINAL`.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `REP_MONTMUL` — `REP_MONTMUL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
