# Cryptography, random, and hashing

This generated bundle contains 48 XED ICLASS reference sections. Each section preserves the instruction-specific semantic prose, availability, architectural effects, representative forms, backend notes, and pinned sources from the per-ICLASS semantic generator.

## AESDEC

`AESDEC` performs an AES decryption-round transformation on a 128-bit state using the supplied round key. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AES`
- XED category/categories: `AES`
- ISA set(s): `AES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESDEC_XMMdq_MEMdq` — `AESDEC`
- `AESDEC_XMMdq_XMMdq` — `AESDEC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AESDECLAST

`AESDECLAST` performs an AES decryption-round transformation on a 128-bit state using the supplied round key without inverse MixColumns in the final-round form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AES`
- XED category/categories: `AES`
- ISA set(s): `AES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESDECLAST_XMMdq_MEMdq` — `AESDECLAST`
- `AESDECLAST_XMMdq_XMMdq` — `AESDECLAST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AESENC

`AESENC` performs an AES encryption-round transformation on a 128-bit state using the supplied round key. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AES`
- XED category/categories: `AES`
- ISA set(s): `AES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESENC_XMMdq_MEMdq` — `AESENC`
- `AESENC_XMMdq_XMMdq` — `AESENC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AESENCLAST

`AESENCLAST` performs an AES encryption-round transformation on a 128-bit state using the supplied round key without MixColumns in the final-round form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AES`
- XED category/categories: `AES`
- ISA set(s): `AES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESENCLAST_XMMdq_MEMdq` — `AESENCLAST`
- `AESENCLAST_XMMdq_XMMdq` — `AESENCLAST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AESIMC

`AESIMC` applies the AES inverse MixColumns transformation to a round key. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AES`
- XED category/categories: `AES`
- ISA set(s): `AES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESIMC_XMMdq_MEMdq` — `AESIMC`
- `AESIMC_XMMdq_XMMdq` — `AESIMC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AESKEYGENASSIST

`AESKEYGENASSIST` computes S-box, rotation, and round-constant helper values used in AES key expansion. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AES`
- XED category/categories: `AES`
- ISA set(s): `AES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESKEYGENASSIST_XMMdq_MEMdq_IMMb` — `AESKEYGENASSIST`
- `AESKEYGENASSIST_XMMdq_XMMdq_IMMb` — `AESKEYGENASSIST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## GF2P8AFFINEINVQB

`GF2P8AFFINEINVQB` applies a packed GF(2^8) multiplicative inverse followed by an affine transformation. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `GFNI`
- XED category/categories: `GFNI`
- ISA set(s): `GFNI`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `GF2P8AFFINEINVQB_XMMu8_MEMu64_IMM8` — `GF2P8AFFINEINVQB`
- `GF2P8AFFINEINVQB_XMMu8_XMMu64_IMM8` — `GF2P8AFFINEINVQB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## GF2P8AFFINEQB

`GF2P8AFFINEQB` applies a packed affine transformation over GF(2^8) to bytes. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `GFNI`
- XED category/categories: `GFNI`
- ISA set(s): `GFNI`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `GF2P8AFFINEQB_XMMu8_MEMu64_IMM8` — `GF2P8AFFINEQB`
- `GF2P8AFFINEQB_XMMu8_XMMu64_IMM8` — `GF2P8AFFINEQB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## GF2P8MULB

`GF2P8MULB` multiplies packed bytes in GF(2^8) using the instruction-defined reduction polynomial. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `GFNI`
- XED category/categories: `GFNI`
- ISA set(s): `GFNI`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `GF2P8MULB_XMMu8_MEMu8` — `GF2P8MULB`
- `GF2P8MULB_XMMu8_XMMu8` — `GF2P8MULB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PCLMULQDQ

`PCLMULQDQ` performs carry-less multiplication of selected binary-polynomial operands for CRC and finite-field arithmetic. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `PCLMULQDQ`
- XED category/categories: `PCLMULQDQ`
- ISA set(s): `PCLMULQDQ`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PCLMULQDQ_XMMdq_MEMdq_IMMb` — `PCLMULQDQ`
- `PCLMULQDQ_XMMdq_XMMdq_IMMb` — `PCLMULQDQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDRAND

`RDRAND` requests a hardware-generated random value and reports success through the carry flag. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RDRAND`
- XED category/categories: `RDRAND`
- ISA set(s): `RDRAND`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDRAND_GPRv` — `RDRAND`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDSEED

`RDSEED` requests a hardware seed value intended for seeding a software pseudorandom generator and reports availability through the carry flag. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RDSEED`
- XED category/categories: `RDSEED`
- ISA set(s): `RDSEED`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDSEED_GPRv` — `RDSEED`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## REP_XCRYPTCBC

`REP_XCRYPTCBC` repeats a VIA PadLock cryptographic or hashing primitive over a buffer using implicit registers for state, addresses, and count. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VIA_PADLOCK_AES`
- XED category/categories: `VIA_PADLOCK`
- ISA set(s): `VIA_PADLOCK_AES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `MEM OrCX OrDX OrBX ArAX ArDI FINAL MEM ArSI`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `REP_XCRYPTCBC` — `REP_XCRYPTCBC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## REP_XCRYPTCFB

`REP_XCRYPTCFB` repeats a VIA PadLock cryptographic or hashing primitive over a buffer using implicit registers for state, addresses, and count. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VIA_PADLOCK_AES`
- XED category/categories: `VIA_PADLOCK`
- ISA set(s): `VIA_PADLOCK_AES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `MEM OrCX OrDX OrBX ArAX ArDI FINAL MEM ArSI`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `REP_XCRYPTCFB` — `REP_XCRYPTCFB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## REP_XCRYPTCTR

`REP_XCRYPTCTR` repeats a VIA PadLock cryptographic or hashing primitive over a buffer using implicit registers for state, addresses, and count. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VIA_PADLOCK_AES`
- XED category/categories: `VIA_PADLOCK`
- ISA set(s): `VIA_PADLOCK_AES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `MEM OrCX OrDX OrBX ArAX ArDI FINAL MEM ArSI`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `REP_XCRYPTCTR` — `REP_XCRYPTCTR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## REP_XCRYPTECB

`REP_XCRYPTECB` repeats a VIA PadLock cryptographic or hashing primitive over a buffer using implicit registers for state, addresses, and count. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VIA_PADLOCK_AES`
- XED category/categories: `VIA_PADLOCK`
- ISA set(s): `VIA_PADLOCK_AES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `MEM OrCX OrDX OrBX ArDI FINAL MEM ArSI`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `REP_XCRYPTECB` — `REP_XCRYPTECB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## REP_XCRYPTOFB

`REP_XCRYPTOFB` repeats a VIA PadLock cryptographic or hashing primitive over a buffer using implicit registers for state, addresses, and count. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VIA_PADLOCK_AES`
- XED category/categories: `VIA_PADLOCK`
- ISA set(s): `VIA_PADLOCK_AES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `MEM OrCX OrDX OrBX ArAX ArDI FINAL MEM ArSI`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `REP_XCRYPTOFB` — `REP_XCRYPTOFB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## REP_XSHA1

`REP_XSHA1` repeats a VIA PadLock cryptographic or hashing primitive over a buffer using implicit registers for state, addresses, and count. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VIA_PADLOCK_SHA`
- XED category/categories: `VIA_PADLOCK`
- ISA set(s): `VIA_PADLOCK_SHA`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `ArAX OrCX MEM ArSI FINAL MEM ArDI FINAL`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `REP_XSHA1` — `REP_XSHA1`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## REP_XSHA256

`REP_XSHA256` repeats a VIA PadLock cryptographic or hashing primitive over a buffer using implicit registers for state, addresses, and count. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VIA_PADLOCK_SHA`
- XED category/categories: `VIA_PADLOCK`
- ISA set(s): `VIA_PADLOCK_SHA`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `ArAX OrCX MEM ArSI FINAL MEM ArDI FINAL`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `REP_XSHA256` — `REP_XSHA256`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHA1MSG1

`SHA1MSG1` computes part of the SHA-1 message schedule over packed 32-bit words. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SHA`
- XED category/categories: `SHA`
- ISA set(s): `SHA`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHA1MSG1_XMMi32_MEMi32_SHA` — `SHA1MSG1`
- `SHA1MSG1_XMMi32_XMMi32_SHA` — `SHA1MSG1`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHA1MSG2

`SHA1MSG2` computes part of the SHA-1 message schedule over packed 32-bit words. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SHA`
- XED category/categories: `SHA`
- ISA set(s): `SHA`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHA1MSG2_XMMi32_MEMi32_SHA` — `SHA1MSG2`
- `SHA1MSG2_XMMi32_XMMi32_SHA` — `SHA1MSG2`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHA1NEXTE

`SHA1NEXTE` computes a SHA-1 E-state update used between grouped rounds. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SHA`
- XED category/categories: `SHA`
- ISA set(s): `SHA`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHA1NEXTE_XMMi32_MEMi32_SHA` — `SHA1NEXTE`
- `SHA1NEXTE_XMMi32_XMMi32_SHA` — `SHA1NEXTE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHA1RNDS4

`SHA1RNDS4` executes four SHA-1 compression rounds using a selected SHA-1 round function. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SHA`
- XED category/categories: `SHA`
- ISA set(s): `SHA`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHA1RNDS4_XMMi32_MEMi32_IMM8_SHA` — `SHA1RNDS4`
- `SHA1RNDS4_XMMi32_XMMi32_IMM8_SHA` — `SHA1RNDS4`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHA256MSG1

`SHA256MSG1` computes part of the SHA-256 message schedule over packed 32-bit words. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SHA`
- XED category/categories: `SHA`
- ISA set(s): `SHA`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHA256MSG1_XMMi32_MEMi32_SHA` — `SHA256MSG1`
- `SHA256MSG1_XMMi32_XMMi32_SHA` — `SHA256MSG1`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHA256MSG2

`SHA256MSG2` computes part of the SHA-256 message schedule over packed 32-bit words. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SHA`
- XED category/categories: `SHA`
- ISA set(s): `SHA`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHA256MSG2_XMMi32_MEMi32_SHA` — `SHA256MSG2`
- `SHA256MSG2_XMMi32_XMMi32_SHA` — `SHA256MSG2`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHA256RNDS2

`SHA256RNDS2` executes two SHA-256 compression rounds using packed state and message values. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SHA`
- XED category/categories: `SHA`
- ISA set(s): `SHA`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: `XMM0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHA256RNDS2_XMMi32_MEMi32_SHA` — `SHA256RNDS2`
- `SHA256RNDS2_XMMi32_XMMi32_SHA` — `SHA256RNDS2`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VAESDEC

`VAESDEC` performs an AES decryption-round transformation on packed 128-bit AES state blocks using the supplied round key. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`, `AVXAES`, `VAES`
- XED category/categories: `AES`, `VAES`
- ISA set(s): `AVX512_VAES_128`, `AVX512_VAES_256`, `AVX512_VAES_512`, `AVXAES`, `VAES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VAESDEC_XMMdq_XMMdq_MEMdq` — `VAESDEC`
- `VAESDEC_XMMdq_XMMdq_XMMdq` — `VAESDEC`
- `VAESDEC_XMMu128_XMMu128_MEMu128_AVX512` — `VAESDEC`
- `VAESDEC_XMMu128_XMMu128_XMMu128_AVX512` — `VAESDEC`
- `VAESDEC_YMMu128_YMMu128_MEMu128` — `VAESDEC`
- `VAESDEC_YMMu128_YMMu128_MEMu128_AVX512` — `VAESDEC`
- `VAESDEC_YMMu128_YMMu128_YMMu128` — `VAESDEC`
- `VAESDEC_YMMu128_YMMu128_YMMu128_AVX512` — `VAESDEC`
- `VAESDEC_ZMMu128_ZMMu128_MEMu128_AVX512` — `VAESDEC`
- `VAESDEC_ZMMu128_ZMMu128_ZMMu128_AVX512` — `VAESDEC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VAESDECLAST

`VAESDECLAST` performs an AES decryption-round transformation on packed 128-bit AES state blocks using the supplied round key without inverse MixColumns for the final-round form. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`, `AVXAES`, `VAES`
- XED category/categories: `AES`, `VAES`
- ISA set(s): `AVX512_VAES_128`, `AVX512_VAES_256`, `AVX512_VAES_512`, `AVXAES`, `VAES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VAESDECLAST_XMMdq_XMMdq_MEMdq` — `VAESDECLAST`
- `VAESDECLAST_XMMdq_XMMdq_XMMdq` — `VAESDECLAST`
- `VAESDECLAST_XMMu128_XMMu128_MEMu128_AVX512` — `VAESDECLAST`
- `VAESDECLAST_XMMu128_XMMu128_XMMu128_AVX512` — `VAESDECLAST`
- `VAESDECLAST_YMMu128_YMMu128_MEMu128` — `VAESDECLAST`
- `VAESDECLAST_YMMu128_YMMu128_MEMu128_AVX512` — `VAESDECLAST`
- `VAESDECLAST_YMMu128_YMMu128_YMMu128` — `VAESDECLAST`
- `VAESDECLAST_YMMu128_YMMu128_YMMu128_AVX512` — `VAESDECLAST`
- `VAESDECLAST_ZMMu128_ZMMu128_MEMu128_AVX512` — `VAESDECLAST`
- `VAESDECLAST_ZMMu128_ZMMu128_ZMMu128_AVX512` — `VAESDECLAST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VAESENC

`VAESENC` performs an AES encryption-round transformation on packed 128-bit AES state blocks using the supplied round key. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`, `AVXAES`, `VAES`
- XED category/categories: `AES`, `VAES`
- ISA set(s): `AVX512_VAES_128`, `AVX512_VAES_256`, `AVX512_VAES_512`, `AVXAES`, `VAES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VAESENC_XMMdq_XMMdq_MEMdq` — `VAESENC`
- `VAESENC_XMMdq_XMMdq_XMMdq` — `VAESENC`
- `VAESENC_XMMu128_XMMu128_MEMu128_AVX512` — `VAESENC`
- `VAESENC_XMMu128_XMMu128_XMMu128_AVX512` — `VAESENC`
- `VAESENC_YMMu128_YMMu128_MEMu128` — `VAESENC`
- `VAESENC_YMMu128_YMMu128_MEMu128_AVX512` — `VAESENC`
- `VAESENC_YMMu128_YMMu128_YMMu128` — `VAESENC`
- `VAESENC_YMMu128_YMMu128_YMMu128_AVX512` — `VAESENC`
- `VAESENC_ZMMu128_ZMMu128_MEMu128_AVX512` — `VAESENC`
- `VAESENC_ZMMu128_ZMMu128_ZMMu128_AVX512` — `VAESENC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VAESENCLAST

`VAESENCLAST` performs an AES encryption-round transformation on packed 128-bit AES state blocks using the supplied round key without MixColumns for the final-round form. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`, `AVXAES`, `VAES`
- XED category/categories: `AES`, `VAES`
- ISA set(s): `AVX512_VAES_128`, `AVX512_VAES_256`, `AVX512_VAES_512`, `AVXAES`, `VAES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VAESENCLAST_XMMdq_XMMdq_MEMdq` — `VAESENCLAST`
- `VAESENCLAST_XMMdq_XMMdq_XMMdq` — `VAESENCLAST`
- `VAESENCLAST_XMMu128_XMMu128_MEMu128_AVX512` — `VAESENCLAST`
- `VAESENCLAST_XMMu128_XMMu128_XMMu128_AVX512` — `VAESENCLAST`
- `VAESENCLAST_YMMu128_YMMu128_MEMu128` — `VAESENCLAST`
- `VAESENCLAST_YMMu128_YMMu128_MEMu128_AVX512` — `VAESENCLAST`
- `VAESENCLAST_YMMu128_YMMu128_YMMu128` — `VAESENCLAST`
- `VAESENCLAST_YMMu128_YMMu128_YMMu128_AVX512` — `VAESENCLAST`
- `VAESENCLAST_ZMMu128_ZMMu128_MEMu128_AVX512` — `VAESENCLAST`
- `VAESENCLAST_ZMMu128_ZMMu128_ZMMu128_AVX512` — `VAESENCLAST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VAESIMC

`VAESIMC` applies AES inverse MixColumns to an encoded round key so it can be used by the AES decryption-round instructions. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVXAES`
- XED category/categories: `AES`
- ISA set(s): `AVXAES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VAESIMC_XMMdq_MEMdq` — `VAESIMC`
- `VAESIMC_XMMdq_XMMdq` — `VAESIMC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VAESKEYGENASSIST

`VAESKEYGENASSIST` computes S-box, rotation, and round-constant helper values used during AES key-schedule expansion. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVXAES`
- XED category/categories: `AES`
- ISA set(s): `AVXAES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VAESKEYGENASSIST_XMMdq_MEMdq_IMMb` — `VAESKEYGENASSIST`
- `VAESKEYGENASSIST_XMMdq_XMMdq_IMMb` — `VAESKEYGENASSIST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VGF2P8AFFINEINVQB

`VGF2P8AFFINEINVQB` applies a packed GF(2^8) multiplicative inverse followed by an affine transformation. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`, `GFNI`
- XED category/categories: `GFNI`
- ISA set(s): `AVX512_GFNI_128`, `AVX512_GFNI_256`, `AVX512_GFNI_512`, `AVX_GFNI`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM IMM`; `XMM MASK1 XMM XMM IMM`; `XMM XMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VGF2P8AFFINEINVQB_XMMu8_MASKmskw_XMMu8_MEMu64_IMM8_AVX512` — `VGF2P8AFFINEINVQB`
- `VGF2P8AFFINEINVQB_XMMu8_MASKmskw_XMMu8_XMMu64_IMM8_AVX512` — `VGF2P8AFFINEINVQB`
- `VGF2P8AFFINEINVQB_XMMu8_XMMu8_MEMu64_IMM8` — `VGF2P8AFFINEINVQB`
- `VGF2P8AFFINEINVQB_XMMu8_XMMu8_XMMu64_IMM8` — `VGF2P8AFFINEINVQB`
- `VGF2P8AFFINEINVQB_YMMu8_MASKmskw_YMMu8_MEMu64_IMM8_AVX512` — `VGF2P8AFFINEINVQB`
- `VGF2P8AFFINEINVQB_YMMu8_MASKmskw_YMMu8_YMMu64_IMM8_AVX512` — `VGF2P8AFFINEINVQB`
- `VGF2P8AFFINEINVQB_YMMu8_YMMu8_MEMu64_IMM8` — `VGF2P8AFFINEINVQB`
- `VGF2P8AFFINEINVQB_YMMu8_YMMu8_YMMu64_IMM8` — `VGF2P8AFFINEINVQB`
- `VGF2P8AFFINEINVQB_ZMMu8_MASKmskw_ZMMu8_MEMu64_IMM8_AVX512` — `VGF2P8AFFINEINVQB`
- `VGF2P8AFFINEINVQB_ZMMu8_MASKmskw_ZMMu8_ZMMu64_IMM8_AVX512` — `VGF2P8AFFINEINVQB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VGF2P8AFFINEQB

`VGF2P8AFFINEQB` applies a packed affine transformation over GF(2^8) to bytes. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`, `GFNI`
- XED category/categories: `GFNI`
- ISA set(s): `AVX512_GFNI_128`, `AVX512_GFNI_256`, `AVX512_GFNI_512`, `AVX_GFNI`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM IMM`; `XMM MASK1 XMM XMM IMM`; `XMM XMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VGF2P8AFFINEQB_XMMu8_MASKmskw_XMMu8_MEMu64_IMM8_AVX512` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_XMMu8_MASKmskw_XMMu8_XMMu64_IMM8_AVX512` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_XMMu8_XMMu8_MEMu64_IMM8` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_XMMu8_XMMu8_XMMu64_IMM8` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_YMMu8_MASKmskw_YMMu8_MEMu64_IMM8_AVX512` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_YMMu8_MASKmskw_YMMu8_YMMu64_IMM8_AVX512` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_YMMu8_YMMu8_MEMu64_IMM8` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_YMMu8_YMMu8_YMMu64_IMM8` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_ZMMu8_MASKmskw_ZMMu8_MEMu64_IMM8_AVX512` — `VGF2P8AFFINEQB`
- `VGF2P8AFFINEQB_ZMMu8_MASKmskw_ZMMu8_ZMMu64_IMM8_AVX512` — `VGF2P8AFFINEQB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VGF2P8MULB

`VGF2P8MULB` multiplies packed bytes in GF(2^8) using the instruction-defined reduction polynomial. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`, `GFNI`
- XED category/categories: `GFNI`
- ISA set(s): `AVX512_GFNI_128`, `AVX512_GFNI_256`, `AVX512_GFNI_512`, `AVX_GFNI`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VGF2P8MULB_XMMu8_MASKmskw_XMMu8_MEMu8_AVX512` — `VGF2P8MULB`
- `VGF2P8MULB_XMMu8_MASKmskw_XMMu8_XMMu8_AVX512` — `VGF2P8MULB`
- `VGF2P8MULB_XMMu8_XMMu8_MEMu8` — `VGF2P8MULB`
- `VGF2P8MULB_XMMu8_XMMu8_XMMu8` — `VGF2P8MULB`
- `VGF2P8MULB_YMMu8_MASKmskw_YMMu8_MEMu8_AVX512` — `VGF2P8MULB`
- `VGF2P8MULB_YMMu8_MASKmskw_YMMu8_YMMu8_AVX512` — `VGF2P8MULB`
- `VGF2P8MULB_YMMu8_YMMu8_MEMu8` — `VGF2P8MULB`
- `VGF2P8MULB_YMMu8_YMMu8_YMMu8` — `VGF2P8MULB`
- `VGF2P8MULB_ZMMu8_MASKmskw_ZMMu8_MEMu8_AVX512` — `VGF2P8MULB`
- `VGF2P8MULB_ZMMu8_MASKmskw_ZMMu8_ZMMu8_AVX512` — `VGF2P8MULB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCLMULQDQ

`VPCLMULQDQ` performs carry-less multiplication of selected binary-polynomial operands for CRC and finite-field arithmetic. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`, `VPCLMULQDQ`
- XED category/categories: `AVX`, `VPCLMULQDQ`
- ISA set(s): `AVX`, `AVX512_VPCLMULQDQ_128`, `AVX512_VPCLMULQDQ_256`, `AVX512_VPCLMULQDQ_512`, `VPCLMULQDQ`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`; `YMM YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCLMULQDQ_XMMdq_XMMdq_MEMdq_IMMb` — `VPCLMULQDQ`
- `VPCLMULQDQ_XMMdq_XMMdq_XMMdq_IMMb` — `VPCLMULQDQ`
- `VPCLMULQDQ_XMMu128_XMMu64_MEMu64_IMM8_AVX512` — `VPCLMULQDQ`
- `VPCLMULQDQ_XMMu128_XMMu64_XMMu64_IMM8_AVX512` — `VPCLMULQDQ`
- `VPCLMULQDQ_YMMu128_YMMu64_MEMu64_IMM8` — `VPCLMULQDQ`
- `VPCLMULQDQ_YMMu128_YMMu64_MEMu64_IMM8_AVX512` — `VPCLMULQDQ`
- `VPCLMULQDQ_YMMu128_YMMu64_YMMu64_IMM8` — `VPCLMULQDQ`
- `VPCLMULQDQ_YMMu128_YMMu64_YMMu64_IMM8_AVX512` — `VPCLMULQDQ`
- `VPCLMULQDQ_ZMMu128_ZMMu64_MEMu64_IMM8_AVX512` — `VPCLMULQDQ`
- `VPCLMULQDQ_ZMMu128_ZMMu64_ZMMu64_IMM8_AVX512` — `VPCLMULQDQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPSHAB

`VPSHAB` performs AMD XOP packed arithmetic shifts with per-element signed counts, using count sign to choose left versus arithmetic-right direction. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM XMM`; `XMM XMM MEM`; `XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPSHAB_XMMdq_MEMdq_XMMdq` — `VPSHAB`
- `VPSHAB_XMMdq_XMMdq_MEMdq` — `VPSHAB`
- `VPSHAB_XMMdq_XMMdq_XMMdq` — `VPSHAB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPSHAD

`VPSHAD` performs AMD XOP packed arithmetic shifts with per-element signed counts, using count sign to choose left versus arithmetic-right direction. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM XMM`; `XMM XMM MEM`; `XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPSHAD_XMMdq_MEMdq_XMMdq` — `VPSHAD`
- `VPSHAD_XMMdq_XMMdq_MEMdq` — `VPSHAD`
- `VPSHAD_XMMdq_XMMdq_XMMdq` — `VPSHAD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPSHAQ

`VPSHAQ` performs AMD XOP packed arithmetic shifts with per-element signed counts, using count sign to choose left versus arithmetic-right direction. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM XMM`; `XMM XMM MEM`; `XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPSHAQ_XMMdq_MEMdq_XMMdq` — `VPSHAQ`
- `VPSHAQ_XMMdq_XMMdq_MEMdq` — `VPSHAQ`
- `VPSHAQ_XMMdq_XMMdq_XMMdq` — `VPSHAQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPSHAW

`VPSHAW` performs AMD XOP packed arithmetic shifts with per-element signed counts, using count sign to choose left versus arithmetic-right direction. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM XMM`; `XMM XMM MEM`; `XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPSHAW_XMMdq_MEMdq_XMMdq` — `VPSHAW`
- `VPSHAW_XMMdq_XMMdq_MEMdq` — `VPSHAW`
- `VPSHAW_XMMdq_XMMdq_XMMdq` — `VPSHAW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VSHA512MSG1

`VSHA512MSG1` performs the first SHA-512 message-schedule helper transformation on packed 64-bit words. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SHA512`
- XED category/categories: `SHA512`
- ISA set(s): `SHA512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `YMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VSHA512MSG1_YMMu64_XMMu64` — `VSHA512MSG1`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VSHA512MSG2

`VSHA512MSG2` performs the second SHA-512 message-schedule helper transformation on packed 64-bit words. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SHA512`
- XED category/categories: `SHA512`
- ISA set(s): `SHA512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `YMM YMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VSHA512MSG2_YMMu64_YMMu64` — `VSHA512MSG2`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VSHA512RNDS2

`VSHA512RNDS2` executes two SHA-512 compression rounds on packed state and message words. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SHA512`
- XED category/categories: `SHA512`
- ISA set(s): `SHA512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `YMM YMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VSHA512RNDS2_YMMu64_YMMu64_XMMu64` — `VSHA512RNDS2`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VSM3MSG1

`VSM3MSG1` performs the first SM3 message-schedule expansion transformation on packed 32-bit words. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SM3`
- XED category/categories: `VEX`
- ISA set(s): `SM3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VSM3MSG1_XMMu32_XMMu32_MEMu32` — `VSM3MSG1`
- `VSM3MSG1_XMMu32_XMMu32_XMMu32` — `VSM3MSG1`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VSM3MSG2

`VSM3MSG2` performs the second SM3 message-schedule expansion transformation on packed 32-bit words. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SM3`
- XED category/categories: `VEX`
- ISA set(s): `SM3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VSM3MSG2_XMMu32_XMMu32_MEMu32` — `VSM3MSG2`
- `VSM3MSG2_XMMu32_XMMu32_XMMu32` — `VSM3MSG2`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VSM3RNDS2

`VSM3RNDS2` executes two SM3 compression rounds using packed state and message words. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SM3`
- XED category/categories: `VEX`
- ISA set(s): `SM3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VSM3RNDS2_XMMu32_XMMu32_MEMu32_IMM8` — `VSM3RNDS2`
- `VSM3RNDS2_XMMu32_XMMu32_XMMu32_IMM8` — `VSM3RNDS2`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VSM4KEY4

`VSM4KEY4` computes four SM4 key-schedule words from packed 32-bit state. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`, `SM4`
- XED category/categories: `AVX512`, `VEX`
- ISA set(s): `SM4`, `SM4_128`, `SM4_256`, `SM4_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VSM4KEY4_XMMu32_XMMu32_MEMu32` — `VSM4KEY4`
- `VSM4KEY4_XMMu32_XMMu32_MEMu32_AVX512` — `VSM4KEY4`
- `VSM4KEY4_XMMu32_XMMu32_XMMu32` — `VSM4KEY4`
- `VSM4KEY4_XMMu32_XMMu32_XMMu32_AVX512` — `VSM4KEY4`
- `VSM4KEY4_YMMu32_YMMu32_MEMu32` — `VSM4KEY4`
- `VSM4KEY4_YMMu32_YMMu32_MEMu32_AVX512` — `VSM4KEY4`
- `VSM4KEY4_YMMu32_YMMu32_YMMu32` — `VSM4KEY4`
- `VSM4KEY4_YMMu32_YMMu32_YMMu32_AVX512` — `VSM4KEY4`
- `VSM4KEY4_ZMMu32_ZMMu32_MEMu32_AVX512` — `VSM4KEY4`
- `VSM4KEY4_ZMMu32_ZMMu32_ZMMu32_AVX512` — `VSM4KEY4`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VSM4RNDS4

`VSM4RNDS4` executes four SM4 cipher rounds on packed 32-bit state. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`, `SM4`
- XED category/categories: `AVX512`, `VEX`
- ISA set(s): `SM4`, `SM4_128`, `SM4_256`, `SM4_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM`; `XMM XMM XMM`; `YMM YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VSM4RNDS4_XMMu32_XMMu32_MEMu32` — `VSM4RNDS4`
- `VSM4RNDS4_XMMu32_XMMu32_MEMu32_AVX512` — `VSM4RNDS4`
- `VSM4RNDS4_XMMu32_XMMu32_XMMu32` — `VSM4RNDS4`
- `VSM4RNDS4_XMMu32_XMMu32_XMMu32_AVX512` — `VSM4RNDS4`
- `VSM4RNDS4_YMMu32_YMMu32_MEMu32` — `VSM4RNDS4`
- `VSM4RNDS4_YMMu32_YMMu32_MEMu32_AVX512` — `VSM4RNDS4`
- `VSM4RNDS4_YMMu32_YMMu32_YMMu32` — `VSM4RNDS4`
- `VSM4RNDS4_YMMu32_YMMu32_YMMu32_AVX512` — `VSM4RNDS4`
- `VSM4RNDS4_ZMMu32_ZMMu32_MEMu32_AVX512` — `VSM4RNDS4`
- `VSM4RNDS4_ZMMu32_ZMMu32_ZMMu32_AVX512` — `VSM4RNDS4`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
