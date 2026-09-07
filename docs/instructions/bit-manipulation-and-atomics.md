# Bit manipulation and atomics

This generated bundle contains 46 XED ICLASS reference sections. Each section preserves the instruction-specific semantic prose, availability, architectural effects, representative forms, backend notes, and pinned sources from the per-ICLASS semantic generator.

## AADD

`AADD` atomically adds a register value to a memory operand without using the LOCK prefix spelling, implementing the RAO-INT atomic-add operation. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RAO`
- XED category/categories: `APX`, `LEGACY`
- ISA set(s): `APX_F_RAO_INT`, `RAO_INT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32`; `MEM GPR64`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AADD_MEM32_GPR32` — `AADD`
- `AADD_MEM64_GPR64` — `AADD`
- `AADD_MEMi32_GPR32i32_APX` — `AADD`
- `AADD_MEMi64_GPR64i64_APX` — `AADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AAND

`AAND` atomically ANDs a register value into a memory operand, implementing the RAO-INT atomic-AND operation. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RAO`
- XED category/categories: `APX`, `LEGACY`
- ISA set(s): `APX_F_RAO_INT`, `RAO_INT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32`; `MEM GPR64`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AAND_MEM32_GPR32` — `AAND`
- `AAND_MEM64_GPR64` — `AAND`
- `AAND_MEMi32_GPR32i32_APX` — `AAND`
- `AAND_MEMi64_GPR64i64_APX` — `AAND`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ANDN

`ANDN` ANDs the complemented first source with the second. The pinned XED inventory represents it with 14 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI1`
- XED category/categories: `BMI1`
- ISA set(s): `APX_F_BMI1`, `APX_F_BMI1_N3`, `BMI1`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32 GPR32`; `GPR32 GPR32 MEM`; `GPR64 GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ANDN_GPR32d_GPR32d_GPR32d` — `ANDN`
- `ANDN_GPR32d_GPR32d_MEMd` — `ANDN`
- `ANDN_GPR32i32_GPR32i32_GPR32i32_APX` — `ANDN`
- `ANDN_GPR32i32_GPR32i32_GPR32i32_APX_N3` — `ANDN`
- `ANDN_GPR32i32_GPR32i32_MEMi32_APX` — `ANDN`
- `ANDN_GPR32i32_GPR32i32_MEMi32_APX_N3` — `ANDN`
- `ANDN_GPR64i64_GPR64i64_GPR64i64_APX` — `ANDN`
- `ANDN_GPR64i64_GPR64i64_GPR64i64_APX_N3` — `ANDN`
- `ANDN_GPR64i64_GPR64i64_MEMi64_APX` — `ANDN`
- `ANDN_GPR64i64_GPR64i64_MEMi64_APX_N3` — `ANDN`
- `ANDN_GPR64q_GPR64q_GPR64q` — `ANDN`
- `ANDN_GPR64q_GPR64q_MEMq` — `ANDN`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AOR

`AOR` atomically ORs a register value into a memory operand, implementing the RAO-INT atomic-OR operation. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RAO`
- XED category/categories: `APX`, `LEGACY`
- ISA set(s): `APX_F_RAO_INT`, `RAO_INT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32`; `MEM GPR64`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AOR_MEM32_GPR32` — `AOR`
- `AOR_MEM64_GPR64` — `AOR`
- `AOR_MEMi32_GPR32i32_APX` — `AOR`
- `AOR_MEMi64_GPR64i64_APX` — `AOR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AXOR

`AXOR` atomically XORs a register value into a memory operand, implementing the RAO-INT atomic-XOR operation. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RAO`
- XED category/categories: `APX`, `LEGACY`
- ISA set(s): `APX_F_RAO_INT`, `RAO_INT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32`; `MEM GPR64`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AXOR_MEM32_GPR32` — `AXOR`
- `AXOR_MEM64_GPR64` — `AXOR`
- `AXOR_MEMi32_GPR32i32_APX` — `AXOR`
- `AXOR_MEMi64_GPR64i64_APX` — `AXOR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BEXTR

`BEXTR` extracts a contiguous variable bit field. The pinned XED inventory represents it with 14 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI1`
- XED category/categories: `BMI1`
- ISA set(s): `APX_F_BMI1`, `APX_F_BMI1_N3`, `BMI1`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32 GPR32`; `GPR32 MEM GPR32`; `GPR64 GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BEXTR_GPR32d_GPR32d_GPR32d` — `BEXTR`
- `BEXTR_GPR32d_MEMd_GPR32d` — `BEXTR`
- `BEXTR_GPR32i32_GPR32i32_GPR32i32_APX` — `BEXTR`
- `BEXTR_GPR32i32_GPR32i32_GPR32i32_APX_N3` — `BEXTR`
- `BEXTR_GPR32i32_MEMi32_GPR32i32_APX` — `BEXTR`
- `BEXTR_GPR32i32_MEMi32_GPR32i32_APX_N3` — `BEXTR`
- `BEXTR_GPR64i64_GPR64i64_GPR64i64_APX` — `BEXTR`
- `BEXTR_GPR64i64_GPR64i64_GPR64i64_APX_N3` — `BEXTR`
- `BEXTR_GPR64i64_MEMi64_GPR64i64_APX` — `BEXTR`
- `BEXTR_GPR64i64_MEMi64_GPR64i64_APX_N3` — `BEXTR`
- `BEXTR_GPR64q_GPR64q_GPR64q` — `BEXTR`
- `BEXTR_GPR64q_MEMq_GPR64q` — `BEXTR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BEXTR_XOP

`BEXTR_XOP` extracts a variable contiguous bit field using AMD XOP's BEXTR encoding, with the start position and field length supplied by the control operand. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TBM`
- XED category/categories: `TBM`
- ISA set(s): `TBM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 MEM IMM`; `VGPR32 VGPR32 IMM`; `VGPRy MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BEXTR_XOP_GPR32d_GPR32d_IMMd` — `BEXTR_XOP`
- `BEXTR_XOP_GPR32d_MEMd_IMMd` — `BEXTR_XOP`
- `BEXTR_XOP_GPRyy_GPRyy_IMMd` — `BEXTR_XOP`
- `BEXTR_XOP_GPRyy_MEMy_IMMd` — `BEXTR_XOP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BLCFILL

`BLCFILL` computes an AMD TBM/BMI-style bit transform around the lowest set or clear bit. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TBM`
- XED category/categories: `TBM`
- ISA set(s): `TBM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 MEM`; `VGPR32 VGPR32`; `VGPRy MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BLCFILL_GPR32d_GPR32d` — `BLCFILL`
- `BLCFILL_GPR32d_MEMd` — `BLCFILL`
- `BLCFILL_GPRyy_GPRyy` — `BLCFILL`
- `BLCFILL_GPRyy_MEMy` — `BLCFILL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BLCI

`BLCI` computes an AMD TBM/BMI-style bit transform around the lowest set or clear bit. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TBM`
- XED category/categories: `TBM`
- ISA set(s): `TBM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 MEM`; `VGPR32 VGPR32`; `VGPRy MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BLCI_GPR32d_GPR32d` — `BLCI`
- `BLCI_GPR32d_MEMd` — `BLCI`
- `BLCI_GPRyy_GPRyy` — `BLCI`
- `BLCI_GPRyy_MEMy` — `BLCI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BLCIC

`BLCIC` computes an AMD TBM/BMI-style bit transform around the lowest set or clear bit. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TBM`
- XED category/categories: `TBM`
- ISA set(s): `TBM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 MEM`; `VGPR32 VGPR32`; `VGPRy MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BLCIC_GPR32d_GPR32d` — `BLCIC`
- `BLCIC_GPR32d_MEMd` — `BLCIC`
- `BLCIC_GPRyy_GPRyy` — `BLCIC`
- `BLCIC_GPRyy_MEMy` — `BLCIC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BLCMSK

`BLCMSK` computes an AMD TBM/BMI-style bit transform around the lowest set or clear bit. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TBM`
- XED category/categories: `TBM`
- ISA set(s): `TBM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 MEM`; `VGPR32 VGPR32`; `VGPRy MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BLCMSK_GPR32d_GPR32d` — `BLCMSK`
- `BLCMSK_GPR32d_MEMd` — `BLCMSK`
- `BLCMSK_GPRyy_GPRyy` — `BLCMSK`
- `BLCMSK_GPRyy_MEMy` — `BLCMSK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BLCS

`BLCS` computes an AMD TBM/BMI-style bit transform around the lowest set or clear bit. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TBM`
- XED category/categories: `TBM`
- ISA set(s): `TBM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 MEM`; `VGPR32 VGPR32`; `VGPRy MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BLCS_GPR32d_GPR32d` — `BLCS`
- `BLCS_GPR32d_MEMd` — `BLCS`
- `BLCS_GPRyy_GPRyy` — `BLCS`
- `BLCS_GPRyy_MEMy` — `BLCS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BLSFILL

`BLSFILL` computes an AMD TBM/BMI-style bit transform around the lowest set or clear bit. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TBM`
- XED category/categories: `TBM`
- ISA set(s): `TBM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 MEM`; `VGPR32 VGPR32`; `VGPRy MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BLSFILL_GPR32d_GPR32d` — `BLSFILL`
- `BLSFILL_GPR32d_MEMd` — `BLSFILL`
- `BLSFILL_GPRyy_GPRyy` — `BLSFILL`
- `BLSFILL_GPRyy_MEMy` — `BLSFILL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BLSI

`BLSI` isolates the lowest set bit. The pinned XED inventory represents it with 14 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI1`
- XED category/categories: `BMI1`
- ISA set(s): `APX_F_BMI1`, `APX_F_BMI1_N3`, `BMI1`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32`; `GPR32 MEM`; `GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BLSI_GPR32d_GPR32d` — `BLSI`
- `BLSI_GPR32d_MEMd` — `BLSI`
- `BLSI_GPR32i32_GPR32i32_APX` — `BLSI`
- `BLSI_GPR32i32_GPR32i32_APX_N3` — `BLSI`
- `BLSI_GPR32i32_MEMi32_APX` — `BLSI`
- `BLSI_GPR32i32_MEMi32_APX_N3` — `BLSI`
- `BLSI_GPR64i64_GPR64i64_APX` — `BLSI`
- `BLSI_GPR64i64_GPR64i64_APX_N3` — `BLSI`
- `BLSI_GPR64i64_MEMi64_APX` — `BLSI`
- `BLSI_GPR64i64_MEMi64_APX_N3` — `BLSI`
- `BLSI_GPR64q_GPR64q` — `BLSI`
- `BLSI_GPR64q_MEMq` — `BLSI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BLSIC

`BLSIC` computes an AMD TBM/BMI-style bit transform around the lowest set or clear bit. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TBM`
- XED category/categories: `TBM`
- ISA set(s): `TBM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 MEM`; `VGPR32 VGPR32`; `VGPRy MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BLSIC_GPR32d_GPR32d` — `BLSIC`
- `BLSIC_GPR32d_MEMd` — `BLSIC`
- `BLSIC_GPRyy_GPRyy` — `BLSIC`
- `BLSIC_GPRyy_MEMy` — `BLSIC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BLSMSK

`BLSMSK` makes a mask through the lowest set bit. The pinned XED inventory represents it with 14 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI1`
- XED category/categories: `BMI1`
- ISA set(s): `APX_F_BMI1`, `APX_F_BMI1_N3`, `BMI1`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32`; `GPR32 MEM`; `GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BLSMSK_GPR32d_GPR32d` — `BLSMSK`
- `BLSMSK_GPR32d_MEMd` — `BLSMSK`
- `BLSMSK_GPR32i32_GPR32i32_APX` — `BLSMSK`
- `BLSMSK_GPR32i32_GPR32i32_APX_N3` — `BLSMSK`
- `BLSMSK_GPR32i32_MEMi32_APX` — `BLSMSK`
- `BLSMSK_GPR32i32_MEMi32_APX_N3` — `BLSMSK`
- `BLSMSK_GPR64i64_GPR64i64_APX` — `BLSMSK`
- `BLSMSK_GPR64i64_GPR64i64_APX_N3` — `BLSMSK`
- `BLSMSK_GPR64i64_MEMi64_APX` — `BLSMSK`
- `BLSMSK_GPR64i64_MEMi64_APX_N3` — `BLSMSK`
- `BLSMSK_GPR64q_GPR64q` — `BLSMSK`
- `BLSMSK_GPR64q_MEMq` — `BLSMSK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BLSR

`BLSR` clears the lowest set bit. The pinned XED inventory represents it with 14 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI1`
- XED category/categories: `BMI1`
- ISA set(s): `APX_F_BMI1`, `APX_F_BMI1_N3`, `BMI1`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32`; `GPR32 MEM`; `GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BLSR_GPR32d_GPR32d` — `BLSR`
- `BLSR_GPR32d_MEMd` — `BLSR`
- `BLSR_GPR32i32_GPR32i32_APX` — `BLSR`
- `BLSR_GPR32i32_GPR32i32_APX_N3` — `BLSR`
- `BLSR_GPR32i32_MEMi32_APX` — `BLSR`
- `BLSR_GPR32i32_MEMi32_APX_N3` — `BLSR`
- `BLSR_GPR64i64_GPR64i64_APX` — `BLSR`
- `BLSR_GPR64i64_GPR64i64_APX_N3` — `BLSR`
- `BLSR_GPR64i64_MEMi64_APX` — `BLSR`
- `BLSR_GPR64i64_MEMi64_APX_N3` — `BLSR`
- `BLSR_GPR64q_GPR64q` — `BLSR`
- `BLSR_GPR64q_MEMq` — `BLSR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BT

`BT` copies a selected bit into carry. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BITBYTE`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv IMM`; `MEM GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BT_GPRv_GPRv` — `BT`
- `BT_GPRv_IMMb` — `BT`
- `BT_MEMv_GPRv` — `BT`
- `BT_MEMv_IMMb` — `BT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BTC

`BTC` copies a selected bit into carry and complements it. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BITBYTE`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv IMM`; `MEM GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BTC_GPRv_GPRv` — `BTC`
- `BTC_GPRv_IMMb` — `BTC`
- `BTC_MEMv_GPRv` — `BTC`
- `BTC_MEMv_IMMb` — `BTC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BTC_LOCK

`BTC_LOCK` copies a selected bit into carry and complements it; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BITBYTE`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPRv`; `MEM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BTC_LOCK_MEMv_GPRv` — `BTC_LOCK`
- `BTC_LOCK_MEMv_IMMb` — `BTC_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BTR

`BTR` copies a selected bit into carry and clears it. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BITBYTE`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv IMM`; `MEM GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BTR_GPRv_GPRv` — `BTR`
- `BTR_GPRv_IMMb` — `BTR`
- `BTR_MEMv_GPRv` — `BTR`
- `BTR_MEMv_IMMb` — `BTR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BTR_LOCK

`BTR_LOCK` copies a selected bit into carry and clears it; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BITBYTE`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPRv`; `MEM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BTR_LOCK_MEMv_GPRv` — `BTR_LOCK`
- `BTR_LOCK_MEMv_IMMb` — `BTR_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BTS

`BTS` copies a selected bit into carry and sets it. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BITBYTE`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv IMM`; `MEM GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BTS_GPRv_GPRv` — `BTS`
- `BTS_GPRv_IMMb` — `BTS`
- `BTS_MEMv_GPRv` — `BTS`
- `BTS_MEMv_IMMb` — `BTS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BTS_LOCK

`BTS_LOCK` copies a selected bit into carry and sets it; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BITBYTE`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPRv`; `MEM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BTS_LOCK_MEMv_GPRv` — `BTS_LOCK`
- `BTS_LOCK_MEMv_IMMb` — `BTS_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BZHI

`BZHI` copies source bits below a variable bit index and clears higher bits. The pinned XED inventory represents it with 14 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI2`
- XED category/categories: `BMI2`
- ISA set(s): `APX_F_BMI2`, `APX_F_BMI2_N3`, `BMI2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32 GPR32`; `GPR32 MEM GPR32`; `GPR64 GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

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

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPXCHG

`CMPXCHG` compares the accumulator with a destination and conditionally replaces the destination with a source. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SEMAPHORE`
- ISA set(s): `I486REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPRv GPRv`; `MEM GPR8`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPXCHG_GPR8_GPR8` — `CMPXCHG`
- `CMPXCHG_GPRv_GPRv` — `CMPXCHG`
- `CMPXCHG_MEMb_GPR8` — `CMPXCHG`
- `CMPXCHG_MEMv_GPRv` — `CMPXCHG`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPXCHG8B

`CMPXCHG8B` atomically compares and conditionally replaces a 64-bit memory value. The pinned XED inventory represents it with 2 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SEMAPHORE`
- ISA set(s): `PENTIUMREAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX ECX EBX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPXCHG8B_MEMq` — `CMPXCHG8B`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPXCHG8B_LOCK

`CMPXCHG8B_LOCK` atomically compares and conditionally replaces a 64-bit memory value; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 2 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SEMAPHORE`
- ISA set(s): `PENTIUMREAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX ECX EBX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPXCHG8B_LOCK_MEMq` — `CMPXCHG8B_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPXCHG_LOCK

`CMPXCHG_LOCK` compares the accumulator with a destination and conditionally replaces the destination with a source; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SEMAPHORE`
- ISA set(s): `I486REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR8`; `MEM GPRv`. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPXCHG_LOCK_MEMb_GPR8` — `CMPXCHG_LOCK`
- `CMPXCHG_LOCK_MEMv_GPRv` — `CMPXCHG_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LZCNT

`LZCNT` counts leading zero bits. The pinned XED inventory represents it with 10 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `LZCNT`
- XED category/categories: `LZCNT`
- ISA set(s): `APX_F_LZCNT`, `APX_F_LZCNT_N3`, `LZCNT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LZCNT_GPRv_GPRv` — `LZCNT`
- `LZCNT_GPRv_GPRv_APX` — `LZCNT`
- `LZCNT_GPRv_GPRv_APX_N3` — `LZCNT`
- `LZCNT_GPRv_MEMv` — `LZCNT`
- `LZCNT_GPRv_MEMv_APX` — `LZCNT`
- `LZCNT_GPRv_MEMv_APX_N3` — `LZCNT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MULX

`MULX` performs unsigned widening multiplication with separate low/high destinations without modifying arithmetic flags. The pinned XED inventory represents it with 10 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI2`
- XED category/categories: `BMI2`
- ISA set(s): `APX_F_BMI2`, `BMI2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32 GPR32`; `GPR32 GPR32 MEM`; `GPR64 GPR64 GPR64`; …. Representative implicit state: `EDX`; `RDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MULX_GPR32d_GPR32d_GPR32d` — `MULX`
- `MULX_GPR32d_GPR32d_MEMd` — `MULX`
- `MULX_GPR32i32_GPR32i32_GPR32i32_APX` — `MULX`
- `MULX_GPR32i32_GPR32i32_MEMi32_APX` — `MULX`
- `MULX_GPR64i64_GPR64i64_GPR64i64_APX` — `MULX`
- `MULX_GPR64i64_GPR64i64_MEMi64_APX` — `MULX`
- `MULX_GPR64q_GPR64q_GPR64q` — `MULX`
- `MULX_GPR64q_GPR64q_MEMq` — `MULX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PDEP

`PDEP` deposits low source bits into positions selected by a mask. The pinned XED inventory represents it with 10 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI2`
- XED category/categories: `BMI2`
- ISA set(s): `APX_F_BMI2`, `BMI2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32 GPR32`; `GPR32 GPR32 MEM`; `GPR64 GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PDEP_GPR32d_GPR32d_GPR32d` — `PDEP`
- `PDEP_GPR32d_GPR32d_MEMd` — `PDEP`
- `PDEP_GPR32i32_GPR32i32_GPR32i32_APX` — `PDEP`
- `PDEP_GPR32i32_GPR32i32_MEMi32_APX` — `PDEP`
- `PDEP_GPR64i64_GPR64i64_GPR64i64_APX` — `PDEP`
- `PDEP_GPR64i64_GPR64i64_MEMi64_APX` — `PDEP`
- `PDEP_GPR64q_GPR64q_GPR64q` — `PDEP`
- `PDEP_GPR64q_GPR64q_MEMq` — `PDEP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PEXT

`PEXT` extracts mask-selected bits and packs them into low destination bits. The pinned XED inventory represents it with 10 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI2`
- XED category/categories: `BMI2`
- ISA set(s): `APX_F_BMI2`, `BMI2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32 GPR32`; `GPR32 GPR32 MEM`; `GPR64 GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PEXT_GPR32d_GPR32d_GPR32d` — `PEXT`
- `PEXT_GPR32d_GPR32d_MEMd` — `PEXT`
- `PEXT_GPR32i32_GPR32i32_GPR32i32_APX` — `PEXT`
- `PEXT_GPR32i32_GPR32i32_MEMi32_APX` — `PEXT`
- `PEXT_GPR64i64_GPR64i64_GPR64i64_APX` — `PEXT`
- `PEXT_GPR64i64_GPR64i64_MEMi64_APX` — `PEXT`
- `PEXT_GPR64q_GPR64q_GPR64q` — `PEXT`
- `PEXT_GPR64q_GPR64q_MEMq` — `PEXT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RORX

`RORX` rotates right without modifying flags. The pinned XED inventory represents it with 10 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI2`
- XED category/categories: `BMI2`
- ISA set(s): `APX_F_BMI2`, `BMI2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32 IMM`; `GPR32 MEM IMM`; `GPR64 GPR64 IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RORX_GPR32d_GPR32d_IMMb` — `RORX`
- `RORX_GPR32d_MEMd_IMMb` — `RORX`
- `RORX_GPR32i32_GPR32i32_IMM8_APX` — `RORX`
- `RORX_GPR32i32_MEMi32_IMM8_APX` — `RORX`
- `RORX_GPR64i64_GPR64i64_IMM8_APX` — `RORX`
- `RORX_GPR64i64_MEMi64_IMM8_APX` — `RORX`
- `RORX_GPR64q_GPR64q_IMMb` — `RORX`
- `RORX_GPR64q_MEMq_IMMb` — `RORX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SARX

`SARX` arithmetically shifts right without modifying flags. The pinned XED inventory represents it with 10 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI2`
- XED category/categories: `BMI2`
- ISA set(s): `APX_F_BMI2`, `BMI2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32 GPR32`; `GPR32 MEM GPR32`; `GPR64 GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SARX_GPR32d_GPR32d_GPR32d` — `SARX`
- `SARX_GPR32d_MEMd_GPR32d` — `SARX`
- `SARX_GPR32i32_GPR32i32_GPR32i32_APX` — `SARX`
- `SARX_GPR32i32_MEMi32_GPR32i32_APX` — `SARX`
- `SARX_GPR64i64_GPR64i64_GPR64i64_APX` — `SARX`
- `SARX_GPR64i64_MEMi64_GPR64i64_APX` — `SARX`
- `SARX_GPR64q_GPR64q_GPR64q` — `SARX`
- `SARX_GPR64q_MEMq_GPR64q` — `SARX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHLX

`SHLX` shifts left without modifying flags. The pinned XED inventory represents it with 10 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI2`
- XED category/categories: `BMI2`
- ISA set(s): `APX_F_BMI2`, `BMI2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32 GPR32`; `GPR32 MEM GPR32`; `GPR64 GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHLX_GPR32d_GPR32d_GPR32d` — `SHLX`
- `SHLX_GPR32d_MEMd_GPR32d` — `SHLX`
- `SHLX_GPR32i32_GPR32i32_GPR32i32_APX` — `SHLX`
- `SHLX_GPR32i32_MEMi32_GPR32i32_APX` — `SHLX`
- `SHLX_GPR64i64_GPR64i64_GPR64i64_APX` — `SHLX`
- `SHLX_GPR64i64_MEMi64_GPR64i64_APX` — `SHLX`
- `SHLX_GPR64q_GPR64q_GPR64q` — `SHLX`
- `SHLX_GPR64q_MEMq_GPR64q` — `SHLX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHRX

`SHRX` logically shifts right without modifying flags. The pinned XED inventory represents it with 10 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI2`
- XED category/categories: `BMI2`
- ISA set(s): `APX_F_BMI2`, `BMI2`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32 GPR32`; `GPR32 MEM GPR32`; `GPR64 GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHRX_GPR32d_GPR32d_GPR32d` — `SHRX`
- `SHRX_GPR32d_MEMd_GPR32d` — `SHRX`
- `SHRX_GPR32i32_GPR32i32_GPR32i32_APX` — `SHRX`
- `SHRX_GPR32i32_MEMi32_GPR32i32_APX` — `SHRX`
- `SHRX_GPR64i64_GPR64i64_GPR64i64_APX` — `SHRX`
- `SHRX_GPR64i64_MEMi64_GPR64i64_APX` — `SHRX`
- `SHRX_GPR64q_GPR64q_GPR64q` — `SHRX`
- `SHRX_GPR64q_MEMq_GPR64q` — `SHRX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## T1MSKC

`T1MSKC` computes an AMD TBM/BMI-style bit transform around the lowest set or clear bit. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TBM`
- XED category/categories: `TBM`
- ISA set(s): `TBM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 MEM`; `VGPR32 VGPR32`; `VGPRy MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `T1MSKC_GPR32d_GPR32d` — `T1MSKC`
- `T1MSKC_GPR32d_MEMd` — `T1MSKC`
- `T1MSKC_GPRyy_GPRyy` — `T1MSKC`
- `T1MSKC_GPRyy_MEMy` — `T1MSKC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## TZCNT

`TZCNT` counts trailing zero bits. The pinned XED inventory represents it with 10 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BMI1`
- XED category/categories: `BMI1`
- ISA set(s): `APX_F_BMI1`, `APX_F_BMI1_N3`, `BMI1`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `TZCNT_GPRv_GPRv` — `TZCNT`
- `TZCNT_GPRv_GPRv_APX` — `TZCNT`
- `TZCNT_GPRv_GPRv_APX_N3` — `TZCNT`
- `TZCNT_GPRv_MEMv` — `TZCNT`
- `TZCNT_GPRv_MEMv_APX` — `TZCNT`
- `TZCNT_GPRv_MEMv_APX_N3` — `TZCNT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## TZMSK

`TZMSK` forms AMD TBM's mask from trailing zeros: it sets every bit below the source's least-significant set bit and clears that set bit and all higher bits, equivalently computing the bit pattern of (~src) AND (src - 1). The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TBM`
- XED category/categories: `TBM`
- ISA set(s): `TBM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 MEM`; `VGPR32 VGPR32`; `VGPRy MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `TZMSK_GPR32d_GPR32d` — `TZMSK`
- `TZMSK_GPR32d_MEMd` — `TZMSK`
- `TZMSK_GPRyy_GPRyy` — `TZMSK`
- `TZMSK_GPRyy_MEMy` — `TZMSK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XABORT

`XABORT` explicitly aborts the current RTM transaction and records the immediate abort code in the transactional status returned to the fallback path. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RTM`
- XED category/categories: `UNCOND_BR`
- ISA set(s): `RTM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `IMM`. Representative implicit state: `EAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XABORT_IMMb` — `XABORT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is directly relevant to control-flow lowering. Selection must preserve branch/call semantics while making relocation form, indirect-target behavior, prediction, and ABI effects explicit.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XADD

`XADD` exchanges an addend with the old destination while storing their sum. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SEMAPHORE`
- ISA set(s): `I486REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPRv GPRv`; `MEM GPR8`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XADD_GPR8_GPR8` — `XADD`
- `XADD_GPRv_GPRv` — `XADD`
- `XADD_MEMb_GPR8` — `XADD`
- `XADD_MEMv_GPRv` — `XADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XADD_LOCK

`XADD_LOCK` exchanges an addend with the old destination while storing their sum; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SEMAPHORE`
- ISA set(s): `I486REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR8`; `MEM GPRv`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XADD_LOCK_MEMb_GPR8` — `XADD_LOCK`
- `XADD_LOCK_MEMv_GPRv` — `XADD_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XBEGIN

`XBEGIN` starts a Restricted Transactional Memory region and encodes the relative fallback target to receive control if the transaction aborts. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RTM`
- XED category/categories: `COND_BR`
- ISA set(s): `RTM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `RELBR`. Representative implicit state: `rIP EAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XBEGIN_RELBRz` — `XBEGIN`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is directly relevant to control-flow lowering. Selection must preserve branch/call semantics while making relocation form, indirect-target behavior, prediction, and ABI effects explicit.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XEND

`XEND` attempts to commit the current RTM transaction, making its speculative memory updates architecturally visible atomically if commit succeeds. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RTM`
- XED category/categories: `COND_BR`
- ISA set(s): `RTM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XEND` — `XEND`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is directly relevant to control-flow lowering. Selection must preserve branch/call semantics while making relocation form, indirect-target behavior, prediction, and ABI effects explicit.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XTEST

`XTEST` sets ZF according to whether execution is currently inside a transactional region. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RTM`
- XED category/categories: `LOGICAL`
- ISA set(s): `RTM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XTEST` — `XTEST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
