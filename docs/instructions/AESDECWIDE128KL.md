# AESDECWIDE128KL

`AESDECWIDE128KL` performs an AES decryption-round transformation on a 128-bit state using the supplied round key. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

## Family and availability

- XED extension(s): `KEYLOCKER_WIDE`
- XED category/categories: `KEYLOCKER_WIDE`
- ISA set(s): `KEYLOCKER_WIDE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

## Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `XMM0 XMM1 XMM2 XMM3 XMM4 XMM5 XMM6 XMM7`.

Recorded flag behavior: `MUST [  zf-mod of-0 sf-0 af-0 pf-0 cf-0  ]`.

## Important forms

- `AESDECWIDE128KL_MEMu8` — `AESDECWIDE128KL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

## Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

## Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
