# Security, enclaves, and control-flow protection

This generated bundle contains 48 XED ICLASS reference sections. Each section preserves the instruction-specific semantic prose, availability, architectural effects, representative forms, backend notes, and pinned sources from the per-ICLASS semantic generator.

## AESDEC128KL

`AESDEC128KL` performs an AES decryption-round transformation on a 128-bit state using the supplied round key. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `KEYLOCKER`
- XED category/categories: `KEYLOCKER`
- ISA set(s): `KEYLOCKER`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESDEC128KL_XMMu8_MEMu8` — `AESDEC128KL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AESDEC256KL

`AESDEC256KL` performs an AES decryption-round transformation on a 128-bit state using the supplied round key. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `KEYLOCKER`
- XED category/categories: `KEYLOCKER`
- ISA set(s): `KEYLOCKER`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESDEC256KL_XMMu8_MEMu8` — `AESDEC256KL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AESDECWIDE128KL

`AESDECWIDE128KL` performs an AES decryption-round transformation on a 128-bit state using the supplied round key. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `KEYLOCKER_WIDE`
- XED category/categories: `KEYLOCKER_WIDE`
- ISA set(s): `KEYLOCKER_WIDE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `XMM0 XMM1 XMM2 XMM3 XMM4 XMM5 XMM6 XMM7`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESDECWIDE128KL_MEMu8` — `AESDECWIDE128KL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AESDECWIDE256KL

`AESDECWIDE256KL` performs an AES decryption-round transformation on a 128-bit state using the supplied round key. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `KEYLOCKER_WIDE`
- XED category/categories: `KEYLOCKER_WIDE`
- ISA set(s): `KEYLOCKER_WIDE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `XMM0 XMM1 XMM2 XMM3 XMM4 XMM5 XMM6 XMM7`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESDECWIDE256KL_MEMu8` — `AESDECWIDE256KL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AESENC128KL

`AESENC128KL` performs an AES encryption-round transformation on a 128-bit state using the supplied round key. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `KEYLOCKER`
- XED category/categories: `KEYLOCKER`
- ISA set(s): `KEYLOCKER`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESENC128KL_XMMu8_MEMu8` — `AESENC128KL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AESENC256KL

`AESENC256KL` performs an AES encryption-round transformation on a 128-bit state using the supplied round key. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `KEYLOCKER`
- XED category/categories: `KEYLOCKER`
- ISA set(s): `KEYLOCKER`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESENC256KL_XMMu8_MEMu8` — `AESENC256KL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AESENCWIDE128KL

`AESENCWIDE128KL` performs an AES encryption-round transformation on a 128-bit state using the supplied round key. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `KEYLOCKER_WIDE`
- XED category/categories: `KEYLOCKER_WIDE`
- ISA set(s): `KEYLOCKER_WIDE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `XMM0 XMM1 XMM2 XMM3 XMM4 XMM5 XMM6 XMM7`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESENCWIDE128KL_MEMu8` — `AESENCWIDE128KL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AESENCWIDE256KL

`AESENCWIDE256KL` performs an AES encryption-round transformation on a 128-bit state using the supplied round key. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `KEYLOCKER_WIDE`
- XED category/categories: `KEYLOCKER_WIDE`
- ISA set(s): `KEYLOCKER_WIDE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `XMM0 XMM1 XMM2 XMM3 XMM4 XMM5 XMM6 XMM7`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AESENCWIDE256KL_MEMu8` — `AESENCWIDE256KL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BNDCL

`BNDCL` checks a pointer against the lower bound in a bound register and raises the MPX bounds exception when the pointer is below that bound. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MPX`
- XED category/categories: `MPX`
- ISA set(s): `MPX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `BND AGEN`; `BND GPR32`; `BND GPR64`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BNDCL_BND_AGEN` — `BNDCL`
- `BNDCL_BND_GPR32` — `BNDCL`
- `BNDCL_BND_GPR64` — `BNDCL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BNDCN

`BNDCN` checks a pointer against the one's-complement upper bound held by an MPX bound register and raises the bounds exception when it exceeds the represented upper limit. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MPX`
- XED category/categories: `MPX`
- ISA set(s): `MPX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `BND AGEN`; `BND GPR32`; `BND GPR64`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BNDCN_BND_AGEN` — `BNDCN`
- `BNDCN_BND_GPR32` — `BNDCN`
- `BNDCN_BND_GPR64` — `BNDCN`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BNDCU

`BNDCU` checks a pointer against the upper bound represented by an MPX bound register and raises the bounds exception when it is above that bound. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MPX`
- XED category/categories: `MPX`
- ISA set(s): `MPX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `BND AGEN`; `BND GPR32`; `BND GPR64`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BNDCU_BND_AGEN` — `BNDCU`
- `BNDCU_BND_GPR32` — `BNDCU`
- `BNDCU_BND_GPR64` — `BNDCU`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BNDLDX

`BNDLDX` loads MPX bounds metadata for a pointer from the bounds-directory/bounds-table structures associated with the current address space. The pinned XED inventory represents it with 4 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MPX`
- XED category/categories: `MPX`
- ISA set(s): `MPX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `BND MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BNDLDX_BND_MEMbnd32` — `BNDLDX`
- `BNDLDX_BND_MEMbnd64` — `BNDLDX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BNDMK

`BNDMK` constructs an MPX lower/upper bound pair from an effective address and a bound-size expression and writes it to a bound register. The pinned XED inventory represents it with 2 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MPX`
- XED category/categories: `MPX`
- ISA set(s): `MPX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `BND AGEN`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BNDMK_BND_AGEN` — `BNDMK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BNDMOV

`BNDMOV` copies an MPX bound pair between bound registers and memory without performing a bounds check. The pinned XED inventory represents it with 8 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MPX`
- XED category/categories: `MPX`
- ISA set(s): `MPX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16`, `16 32 64`, `32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `BND BND`; `BND MEM`; `MEM BND`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BNDMOV_BND_BND` — `BNDMOV`
- `BNDMOV_BND_MEMdq` — `BNDMOV`
- `BNDMOV_BND_MEMq` — `BNDMOV`
- `BNDMOV_MEMdq_BND` — `BNDMOV`
- `BNDMOV_MEMq_BND` — `BNDMOV`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BNDSTX

`BNDSTX` stores MPX bounds metadata for a pointer into the bounds-table structures associated with the current address space. The pinned XED inventory represents it with 4 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MPX`
- XED category/categories: `MPX`
- ISA set(s): `MPX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM BND`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BNDSTX_MEMbnd32_BND` — `BNDSTX`
- `BNDSTX_MEMbnd64_BND` — `BNDSTX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CLRSSBSY

`CLRSSBSY` clears the busy bit in a shadow-stack restore token so that the corresponding CET shadow stack is no longer marked busy. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CLRSSBSY_MEMu64` — `CLRSSBSY`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CLUI

`CLUI` clears the user-interrupt flag so maskable user interrupts are not delivered in the current user-interrupt context. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `UINTR`
- XED category/categories: `UINTR`
- ISA set(s): `UINTR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `UIF`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CLUI` — `CLUI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPXCHG16B

`CMPXCHG16B` atomically compares and conditionally replaces a 128-bit memory value. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `LONGMODE`
- XED category/categories: `SEMAPHORE`
- ISA set(s): `CMPXCHG16B`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `RDX RAX RCX RBX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPXCHG16B_MEMdq` — `CMPXCHG16B`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPXCHG16B_LOCK

`CMPXCHG16B_LOCK` atomically compares and conditionally replaces a 128-bit memory value; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `LONGMODE`
- XED category/categories: `SEMAPHORE`
- ISA set(s): `CMPXCHG16B`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `RDX RAX RCX RBX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPXCHG16B_LOCK_MEMdq` — `CMPXCHG16B_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ENCLS

`ENCLS` dispatches a privileged Intel SGX enclave-management leaf selected in EAX, with the other implicit registers interpreted according to that leaf. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SGX`
- XED category/categories: `SGX`
- ISA set(s): `SGX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX RBX RCX RDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ENCLS` — `ENCLS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ENCLU

`ENCLU` dispatches an unprivileged Intel SGX enclave leaf selected in EAX, including enclave entry, exit, acceptance, and related operations. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SGX`
- XED category/categories: `SGX`
- ISA set(s): `SGX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX RBX RCX RDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ENCLU` — `ENCLU`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ENCLV

`ENCLV` dispatches a virtualization-oriented Intel SGX leaf selected in EAX for enclave-management operations exposed to a VMM. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SGX_ENCLV`
- XED category/categories: `SGX`
- ISA set(s): `SGX_ENCLV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX RBX RCX RDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ENCLV` — `ENCLV`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ENCODEKEY128

`ENCODEKEY128` encodes a 128-bit AES key under Intel Key Locker's internal wrapping key and writes the resulting key handle. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `KEYLOCKER`
- XED category/categories: `KEYLOCKER`
- ISA set(s): `KEYLOCKER`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32`. Representative implicit state: `XMM0 XMM1 XMM2 XMM4 XMM5 XMM6`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ENCODEKEY128_GPR32u8_GPR32u8` — `ENCODEKEY128`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ENCODEKEY256

`ENCODEKEY256` encodes a 256-bit AES key under Intel Key Locker's internal wrapping key and writes the resulting key handle. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `KEYLOCKER`
- XED category/categories: `KEYLOCKER`
- ISA set(s): `KEYLOCKER`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32`. Representative implicit state: `XMM0 XMM1 XMM2 XMM3 XMM4 XMM5 XMM6`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ENCODEKEY256_GPR32u8_GPR32u8` — `ENCODEKEY256`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ENDBR32

`ENDBR32` marks a valid 32-bit indirect branch target for Control-flow Enforcement Technology indirect-branch tracking. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ENDBR32` — `ENDBR32`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ENDBR64

`ENDBR64` marks a valid 64-bit indirect branch target for Control-flow Enforcement Technology indirect-branch tracking. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ENDBR64` — `ENDBR64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ERETS

`ERETS` returns from a FRED-delivered event while remaining in supervisor context, restoring the saved event-return state without a privilege transition. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FRED`
- XED category/categories: `FRED`
- ISA set(s): `FRED`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `STACKPOP RIP RSP`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ERETS` — `ERETS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ERETU

`ERETU` returns from a FRED-delivered event to user context, restoring the saved user return state and performing the FRED privilege transition. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `FRED`
- XED category/categories: `FRED`
- ISA set(s): `FRED`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `STACKPOP CS SS RIP RSP GSBASE IA32_KERNEL_GS_BASE`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ERETU` — `ERETU`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## GETSEC

`GETSEC` dispatches an Intel Safer Mode Extensions leaf selected by EAX, providing the architectural entry point for measured-launch and authenticated-code operations such as capability queries, SENTER, SEXIT, ENTERACCS, and EXITAC. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SMX`
- XED category/categories: `SYSTEM`
- ISA set(s): `SMX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX EBX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `GETSEC` — `GETSEC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INCSSPD

`INCSSPD` advances the shadow-stack pointer by a scaled 32-bit count without reading or writing ordinary stack memory. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32`. Representative implicit state: `SSP`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INCSSPD_GPR32u8` — `INCSSPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INCSSPQ

`INCSSPQ` advances the shadow-stack pointer by a scaled 64-bit count without reading or writing ordinary stack memory. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR64`. Representative implicit state: `SSP`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INCSSPQ_GPR64u8` — `INCSSPQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LKGS

`LKGS` loads the kernel GS-base state used by FRED-compatible operating systems without performing a full SWAPGS-style exchange. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `LKGS`
- XED category/categories: `LKGS`
- ISA set(s): `LKGS`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `GPR16`; `MEM`. Representative implicit state: `IA32_KERNEL_GS_BASE`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LKGS_GPR16u16` — `LKGS`
- `LKGS_MEMu16` — `LKGS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LOADIWKEY

`LOADIWKEY` loads the internal wrapping key used by Intel Key Locker to create and consume encoded AES key handles. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `KEYLOCKER`
- XED category/categories: `KEYLOCKER`
- ISA set(s): `KEYLOCKER`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `XMM XMM`. Representative implicit state: `EAX XMM0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LOADIWKEY_XMMu8_XMMu8` — `LOADIWKEY`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDPKRU

`RDPKRU` reads the protection-key rights register that controls access permissions for pages associated with user protection keys. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `PKU`
- XED category/categories: `PKU`
- ISA set(s): `PKU`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EDX EAX ECX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDPKRU` — `RDPKRU`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDSSPD

`RDSSPD` reads the current shadow-stack pointer into a 32-bit general-purpose destination. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32`. Representative implicit state: `SSP`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDSSPD_GPR32u32` — `RDSSPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDSSPQ

`RDSSPQ` reads the current shadow-stack pointer into a 64-bit general-purpose destination. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR64`. Representative implicit state: `SSP`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDSSPQ_GPR64u64` — `RDSSPQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RSTORSSP

`RSTORSSP` restores the CET shadow-stack pointer from a restore token in memory and updates the token state required by shadow-stack switching. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `SSP`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RSTORSSP_MEMu64` — `RSTORSSP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SAVEPREVSSP

`SAVEPREVSSP` writes a restore token for the previous CET shadow-stack pointer after a shadow-stack switch. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `SSP`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SAVEPREVSSP` — `SAVEPREVSSP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SENDUIPI

`SENDUIPI` sends a user interprocessor interrupt to the target selected through the user-interrupt target table. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `UINTR`
- XED category/categories: `UINTR`
- ISA set(s): `UINTR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR64`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SENDUIPI_GPR64u32` — `SENDUIPI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETSSBSY

`SETSSBSY` sets the busy state associated with a supervisor shadow stack so CET can track exclusive active use. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETSSBSY` — `SETSSBSY`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## STUI

`STUI` sets the user-interrupt flag so eligible user interrupts may be delivered after the architecture's defined enabling boundary. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `UINTR`
- XED category/categories: `UINTR`
- ISA set(s): `UINTR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `UIF`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `STUI` — `STUI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## TESTUI

`TESTUI` copies the current user-interrupt enable state into the zero flag so software can test whether user interrupts are enabled. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `UINTR`
- XED category/categories: `UINTR`
- ISA set(s): `UINTR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `UIF`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `TESTUI` — `TESTUI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## UIRET

`UIRET` returns from a user-interrupt handler by restoring the user-interrupt return state established on delivery. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `UINTR`
- XED category/categories: `UINTR`
- ISA set(s): `UINTR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `rIP STACKPOP`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `UIRET` — `UIRET`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## WRPKRU

`WRPKRU` writes the protection-key rights register, changing user-space access-disable and write-disable state for protection-key domains. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `PKU`
- XED category/categories: `PKU`
- ISA set(s): `PKU`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EDX EAX ECX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `WRPKRU` — `WRPKRU`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## WRSSD

`WRSSD` writes a 32-bit value to shadow-stack memory through CET's explicit shadow-stack store mechanism. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `APX_F_CET`, `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `WRSSD_MEMu32_GPR32u32` — `WRSSD`
- `WRSSD_MEMu32_GPR32u32_APX` — `WRSSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## WRSSQ

`WRSSQ` writes a 64-bit value to shadow-stack memory through CET's explicit shadow-stack store mechanism. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `APX_F_CET`, `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR64`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `WRSSQ_MEMu64_GPR64u64` — `WRSSQ`
- `WRSSQ_MEMu64_GPR64u64_APX` — `WRSSQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## WRUSSD

`WRUSSD` writes a 32-bit value to a user shadow stack from privileged software using CET's explicit user-shadow-stack store mechanism. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `APX_F_CET`, `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM GPR32`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `WRUSSD_MEMu32_GPR32u32` — `WRUSSD`
- `WRUSSD_MEMu32_GPR32u32_APX` — `WRUSSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## WRUSSQ

`WRUSSQ` writes a 64-bit value to a user shadow stack from privileged software using CET's explicit user-shadow-stack store mechanism. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CET`
- XED category/categories: `CET`
- ISA set(s): `APX_F_CET`, `CET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM GPR64`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `WRUSSQ_MEMu64_GPR64u64` — `WRUSSQ`
- `WRUSSQ_MEMu64_GPR64u64_APX` — `WRUSSQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
