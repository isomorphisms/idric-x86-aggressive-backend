# PCMPESTRI64

`PCMPESTRI64` compares corresponding its encoded scalar or vector elements under the encoded predicate and produces mask or Boolean lane results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `SSE4`
- XED category/categories: `SSE`
- ISA set(s): `SSE42`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: `RAX RDX RCX`.

Recorded flag behavior: not uniformly recorded.

## Important forms

- `PCMPESTRI64_XMMdq_MEMdq_IMMb` — `PCMPESTRI64`
- `PCMPESTRI64_XMMdq_XMMdq_IMMb` — `PCMPESTRI64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
