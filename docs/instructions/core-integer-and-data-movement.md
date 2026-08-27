# Core integer and data movement

This generated bundle contains 210 XED ICLASS reference sections. Each section preserves the instruction-specific semantic prose, availability, architectural effects, representative forms, backend notes, and pinned sources from the per-ICLASS semantic generator.

## AAA

`AAA` adjusts the low byte of AX after adding two unpacked BCD digits, correcting AL and AH and updating the arithmetic status used by legacy decimal code. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DECIMAL`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `AL AH`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AAA` — `AAA`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AAD

`AAD` adjusts two unpacked BCD digits in AH:AL before division, combining them into a binary value in AL. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DECIMAL`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `IMM`. Representative implicit state: `AL AH`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AAD_IMMb` — `AAD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AAM

`AAM` adjusts the binary result of an 8-bit multiply into two unpacked BCD digits in AH and AL. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DECIMAL`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `IMM`. Representative implicit state: `AL AH`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AAM_IMMb` — `AAM`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AAS

`AAS` adjusts the low byte of AX after subtracting unpacked BCD digits, correcting AL and AH for legacy decimal arithmetic. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DECIMAL`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `AL AH`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AAS` — `AAS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ADC

`ADC` adds the source and incoming carry flag to the destination, enabling multiword addition. The pinned XED inventory represents it with 62 normalized encoding records and 42 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ADC_AL_IMMb` — `ADC`
- `ADC_GPR8_GPR8_10` — `ADC`
- `ADC_GPR8_GPR8_12` — `ADC`
- `ADC_GPR8_IMMb_80r2` — `ADC`
- `ADC_GPR8_IMMb_82r2` — `ADC`
- `ADC_GPR8_MEMb` — `ADC`
- `ADC_GPR8i8_GPR8i8_APX` — `ADC`
- `ADC_GPR8i8_GPR8i8_GPR8i8_APX_N3` — `ADC`
- `ADC_GPR8i8_GPR8i8_IMM8_APX_N3` — `ADC`
- `ADC_GPR8i8_GPR8i8_MEMi8_APX_N3` — `ADC`
- `ADC_GPR8i8_IMM8_APX` — `ADC`
- `ADC_GPR8i8_MEMi8_APX` — `ADC`
- … 30 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ADCX

`ADCX` adds unsigned operands using the carry flag as a carry chain while leaving overflow available for a second chain. The pinned XED inventory represents it with 12 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `ADOX_ADCX`
- XED category/categories: `ADOX_ADCX`, `APX`
- ISA set(s): `ADOX_ADCX`, `APX_F_ADX`, `APX_F_ADX_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32`; `GPR32 GPR32 GPR32`; `GPR32 GPR32 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ADCX_GPR32d_GPR32d` — `ADCX`
- `ADCX_GPR32d_MEMd` — `ADCX`
- `ADCX_GPR32i32_GPR32i32_APX` — `ADCX`
- `ADCX_GPR32i32_GPR32i32_GPR32i32_APX_N3` — `ADCX`
- `ADCX_GPR32i32_GPR32i32_MEMi32_APX_N3` — `ADCX`
- `ADCX_GPR32i32_MEMi32_APX` — `ADCX`
- `ADCX_GPR64i64_GPR64i64_APX` — `ADCX`
- `ADCX_GPR64i64_GPR64i64_GPR64i64_APX_N3` — `ADCX`
- `ADCX_GPR64i64_GPR64i64_MEMi64_APX_N3` — `ADCX`
- `ADCX_GPR64i64_MEMi64_APX` — `ADCX`
- `ADCX_GPR64q_GPR64q` — `ADCX`
- `ADCX_GPR64q_MEMq` — `ADCX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ADC_LOCK

`ADC_LOCK` adds the source and incoming carry flag to the destination, enabling multiword addition; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR8`; `MEM GPRv`; `MEM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ADC_LOCK_MEMb_GPR8` — `ADC_LOCK`
- `ADC_LOCK_MEMb_IMMb_80r2` — `ADC_LOCK`
- `ADC_LOCK_MEMb_IMMb_82r2` — `ADC_LOCK`
- `ADC_LOCK_MEMv_GPRv` — `ADC_LOCK`
- `ADC_LOCK_MEMv_IMMb` — `ADC_LOCK`
- `ADC_LOCK_MEMv_IMMz` — `ADC_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ADD

`ADD` adds the source to the destination and writes the sum while updating arithmetic flags. The pinned XED inventory represents it with 106 normalized encoding records and 54 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ADD_AL_IMMb` — `ADD`
- `ADD_GPR8_GPR8_00` — `ADD`
- `ADD_GPR8_GPR8_02` — `ADD`
- `ADD_GPR8_IMMb_80r0` — `ADD`
- `ADD_GPR8_IMMb_82r0` — `ADD`
- `ADD_GPR8_MEMb` — `ADD`
- `ADD_GPR8i8_GPR8i8_APX` — `ADD`
- `ADD_GPR8i8_GPR8i8_APX_N3` — `ADD`
- `ADD_GPR8i8_GPR8i8_GPR8i8_APX_N3` — `ADD`
- `ADD_GPR8i8_GPR8i8_IMM8_APX_N3` — `ADD`
- `ADD_GPR8i8_GPR8i8_MEMi8_APX_N3` — `ADD`
- `ADD_GPR8i8_IMM8_APX` — `ADD`
- … 42 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ADD_LOCK

`ADD_LOCK` adds the source to the destination and writes the sum while updating arithmetic flags; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR8`; `MEM GPRv`; `MEM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ADD_LOCK_MEMb_GPR8` — `ADD_LOCK`
- `ADD_LOCK_MEMb_IMMb_80r0` — `ADD_LOCK`
- `ADD_LOCK_MEMb_IMMb_82r0` — `ADD_LOCK`
- `ADD_LOCK_MEMv_GPRv` — `ADD_LOCK`
- `ADD_LOCK_MEMv_IMMb` — `ADD_LOCK`
- `ADD_LOCK_MEMv_IMMz` — `ADD_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ADOX

`ADOX` adds unsigned operands using the overflow flag as a carry chain. The pinned XED inventory represents it with 12 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `ADOX_ADCX`
- XED category/categories: `ADOX_ADCX`, `APX`
- ISA set(s): `ADOX_ADCX`, `APX_F_ADX`, `APX_F_ADX_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32`; `GPR32 GPR32 GPR32`; `GPR32 GPR32 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ADOX_GPR32d_GPR32d` — `ADOX`
- `ADOX_GPR32d_MEMd` — `ADOX`
- `ADOX_GPR32i32_GPR32i32_APX` — `ADOX`
- `ADOX_GPR32i32_GPR32i32_GPR32i32_APX_N3` — `ADOX`
- `ADOX_GPR32i32_GPR32i32_MEMi32_APX_N3` — `ADOX`
- `ADOX_GPR32i32_MEMi32_APX` — `ADOX`
- `ADOX_GPR64i64_GPR64i64_APX` — `ADOX`
- `ADOX_GPR64i64_GPR64i64_GPR64i64_APX_N3` — `ADOX`
- `ADOX_GPR64i64_GPR64i64_MEMi64_APX_N3` — `ADOX`
- `ADOX_GPR64i64_MEMi64_APX` — `ADOX`
- `ADOX_GPR64q_GPR64q` — `ADOX`
- `ADOX_GPR64q_MEMq` — `ADOX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AND

`AND` computes bitwise AND. The pinned XED inventory represents it with 106 normalized encoding records and 54 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `LOGICAL`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AND_AL_IMMb` — `AND`
- `AND_GPR8_GPR8_20` — `AND`
- `AND_GPR8_GPR8_22` — `AND`
- `AND_GPR8_IMMb_80r4` — `AND`
- `AND_GPR8_IMMb_82r4` — `AND`
- `AND_GPR8_MEMb` — `AND`
- `AND_GPR8i8_GPR8i8_APX` — `AND`
- `AND_GPR8i8_GPR8i8_APX_N3` — `AND`
- `AND_GPR8i8_GPR8i8_GPR8i8_APX_N3` — `AND`
- `AND_GPR8i8_GPR8i8_IMM8_APX_N3` — `AND`
- `AND_GPR8i8_GPR8i8_MEMi8_APX_N3` — `AND`
- `AND_GPR8i8_IMM8_APX` — `AND`
- … 42 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## AND_LOCK

`AND_LOCK` computes bitwise AND; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `LOGICAL`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR8`; `MEM GPRv`; `MEM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `AND_LOCK_MEMb_GPR8` — `AND_LOCK`
- `AND_LOCK_MEMb_IMMb_80r4` — `AND_LOCK`
- `AND_LOCK_MEMb_IMMb_82r4` — `AND_LOCK`
- `AND_LOCK_MEMv_GPRv` — `AND_LOCK`
- `AND_LOCK_MEMv_IMMb` — `AND_LOCK`
- `AND_LOCK_MEMv_IMMz` — `AND_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BOUND

`BOUND` checks a signed array index against lower and upper bounds stored in memory and raises a bounds exception when it lies outside them. The pinned XED inventory represents it with 4 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `INTERRUPT`
- ISA set(s): `I186`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16`, `32`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR16 MEM`; `GPR32 MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BOUND_GPR16_MEMa16` — `BOUND`
- `BOUND_GPR32_MEMa32` — `BOUND`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BSF

`BSF` finds the least-significant set bit index. The pinned XED inventory represents it with 4 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BITBYTE`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BSF_GPRv_GPRv` — `BSF`
- `BSF_GPRv_MEMv` — `BSF`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## BSWAP

`BSWAP` reverses the byte order within a general-purpose register. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DATAXFER`
- ISA set(s): `I486REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `BSWAP_GPRv` — `BSWAP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CBW

`CBW` sign-extends AL into AX. The pinned XED inventory represents it with 3 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `CONVERT`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16`, `32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `AX AL`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CBW` — `CBW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPB

`CCMPB` performs the architecture's conditional compare operation when the condition-code state denotes below (carry set); otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPB_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPB`
- `CCMPB_GPR8i8_IMM8_DFV_APX_N3` — `CCMPB`
- `CCMPB_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPB`
- `CCMPB_GPRv_GPRv_DFV_APX_N3` — `CCMPB`
- `CCMPB_GPRv_IMM8_DFV_APX_N3` — `CCMPB`
- `CCMPB_GPRv_IMMz_DFV_APX_N3` — `CCMPB`
- `CCMPB_GPRv_MEMv_DFV_APX_N3` — `CCMPB`
- `CCMPB_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPB`
- `CCMPB_MEMi8_IMM8_DFV_APX_N3` — `CCMPB`
- `CCMPB_MEMv_GPRv_DFV_APX_N3` — `CCMPB`
- `CCMPB_MEMv_IMM8_DFV_APX_N3` — `CCMPB`
- `CCMPB_MEMv_IMMz_DFV_APX_N3` — `CCMPB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPBE

`CCMPBE` performs the architecture's conditional compare operation when the condition-code state denotes below or equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPBE_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPBE`
- `CCMPBE_GPR8i8_IMM8_DFV_APX_N3` — `CCMPBE`
- `CCMPBE_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPBE`
- `CCMPBE_GPRv_GPRv_DFV_APX_N3` — `CCMPBE`
- `CCMPBE_GPRv_IMM8_DFV_APX_N3` — `CCMPBE`
- `CCMPBE_GPRv_IMMz_DFV_APX_N3` — `CCMPBE`
- `CCMPBE_GPRv_MEMv_DFV_APX_N3` — `CCMPBE`
- `CCMPBE_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPBE`
- `CCMPBE_MEMi8_IMM8_DFV_APX_N3` — `CCMPBE`
- `CCMPBE_MEMv_GPRv_DFV_APX_N3` — `CCMPBE`
- `CCMPBE_MEMv_IMM8_DFV_APX_N3` — `CCMPBE`
- `CCMPBE_MEMv_IMMz_DFV_APX_N3` — `CCMPBE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPF

`CCMPF` performs the architecture's conditional compare operation when the condition-code state denotes false; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPF_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPF`
- `CCMPF_GPR8i8_IMM8_DFV_APX_N3` — `CCMPF`
- `CCMPF_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPF`
- `CCMPF_GPRv_GPRv_DFV_APX_N3` — `CCMPF`
- `CCMPF_GPRv_IMM8_DFV_APX_N3` — `CCMPF`
- `CCMPF_GPRv_IMMz_DFV_APX_N3` — `CCMPF`
- `CCMPF_GPRv_MEMv_DFV_APX_N3` — `CCMPF`
- `CCMPF_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPF`
- `CCMPF_MEMi8_IMM8_DFV_APX_N3` — `CCMPF`
- `CCMPF_MEMv_GPRv_DFV_APX_N3` — `CCMPF`
- `CCMPF_MEMv_IMM8_DFV_APX_N3` — `CCMPF`
- `CCMPF_MEMv_IMMz_DFV_APX_N3` — `CCMPF`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPL

`CCMPL` performs the architecture's conditional compare operation when the condition-code state denotes less in signed comparison; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPL_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPL`
- `CCMPL_GPR8i8_IMM8_DFV_APX_N3` — `CCMPL`
- `CCMPL_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPL`
- `CCMPL_GPRv_GPRv_DFV_APX_N3` — `CCMPL`
- `CCMPL_GPRv_IMM8_DFV_APX_N3` — `CCMPL`
- `CCMPL_GPRv_IMMz_DFV_APX_N3` — `CCMPL`
- `CCMPL_GPRv_MEMv_DFV_APX_N3` — `CCMPL`
- `CCMPL_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPL`
- `CCMPL_MEMi8_IMM8_DFV_APX_N3` — `CCMPL`
- `CCMPL_MEMv_GPRv_DFV_APX_N3` — `CCMPL`
- `CCMPL_MEMv_IMM8_DFV_APX_N3` — `CCMPL`
- `CCMPL_MEMv_IMMz_DFV_APX_N3` — `CCMPL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPLE

`CCMPLE` performs the architecture's conditional compare operation when the condition-code state denotes less or equal in signed comparison; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPLE_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPLE`
- `CCMPLE_GPR8i8_IMM8_DFV_APX_N3` — `CCMPLE`
- `CCMPLE_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPLE`
- `CCMPLE_GPRv_GPRv_DFV_APX_N3` — `CCMPLE`
- `CCMPLE_GPRv_IMM8_DFV_APX_N3` — `CCMPLE`
- `CCMPLE_GPRv_IMMz_DFV_APX_N3` — `CCMPLE`
- `CCMPLE_GPRv_MEMv_DFV_APX_N3` — `CCMPLE`
- `CCMPLE_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPLE`
- `CCMPLE_MEMi8_IMM8_DFV_APX_N3` — `CCMPLE`
- `CCMPLE_MEMv_GPRv_DFV_APX_N3` — `CCMPLE`
- `CCMPLE_MEMv_IMM8_DFV_APX_N3` — `CCMPLE`
- `CCMPLE_MEMv_IMMz_DFV_APX_N3` — `CCMPLE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPNB

`CCMPNB` performs the architecture's conditional compare operation when the condition-code state denotes not below / unsigned above-or-equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPNB_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPNB`
- `CCMPNB_GPR8i8_IMM8_DFV_APX_N3` — `CCMPNB`
- `CCMPNB_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPNB`
- `CCMPNB_GPRv_GPRv_DFV_APX_N3` — `CCMPNB`
- `CCMPNB_GPRv_IMM8_DFV_APX_N3` — `CCMPNB`
- `CCMPNB_GPRv_IMMz_DFV_APX_N3` — `CCMPNB`
- `CCMPNB_GPRv_MEMv_DFV_APX_N3` — `CCMPNB`
- `CCMPNB_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPNB`
- `CCMPNB_MEMi8_IMM8_DFV_APX_N3` — `CCMPNB`
- `CCMPNB_MEMv_GPRv_DFV_APX_N3` — `CCMPNB`
- `CCMPNB_MEMv_IMM8_DFV_APX_N3` — `CCMPNB`
- `CCMPNB_MEMv_IMMz_DFV_APX_N3` — `CCMPNB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPNBE

`CCMPNBE` performs the architecture's conditional compare operation when the condition-code state denotes unsigned above; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPNBE_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPNBE`
- `CCMPNBE_GPR8i8_IMM8_DFV_APX_N3` — `CCMPNBE`
- `CCMPNBE_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPNBE`
- `CCMPNBE_GPRv_GPRv_DFV_APX_N3` — `CCMPNBE`
- `CCMPNBE_GPRv_IMM8_DFV_APX_N3` — `CCMPNBE`
- `CCMPNBE_GPRv_IMMz_DFV_APX_N3` — `CCMPNBE`
- `CCMPNBE_GPRv_MEMv_DFV_APX_N3` — `CCMPNBE`
- `CCMPNBE_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPNBE`
- `CCMPNBE_MEMi8_IMM8_DFV_APX_N3` — `CCMPNBE`
- `CCMPNBE_MEMv_GPRv_DFV_APX_N3` — `CCMPNBE`
- `CCMPNBE_MEMv_IMM8_DFV_APX_N3` — `CCMPNBE`
- `CCMPNBE_MEMv_IMMz_DFV_APX_N3` — `CCMPNBE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPNL

`CCMPNL` performs the architecture's conditional compare operation when the condition-code state denotes signed greater-or-equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPNL_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPNL`
- `CCMPNL_GPR8i8_IMM8_DFV_APX_N3` — `CCMPNL`
- `CCMPNL_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPNL`
- `CCMPNL_GPRv_GPRv_DFV_APX_N3` — `CCMPNL`
- `CCMPNL_GPRv_IMM8_DFV_APX_N3` — `CCMPNL`
- `CCMPNL_GPRv_IMMz_DFV_APX_N3` — `CCMPNL`
- `CCMPNL_GPRv_MEMv_DFV_APX_N3` — `CCMPNL`
- `CCMPNL_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPNL`
- `CCMPNL_MEMi8_IMM8_DFV_APX_N3` — `CCMPNL`
- `CCMPNL_MEMv_GPRv_DFV_APX_N3` — `CCMPNL`
- `CCMPNL_MEMv_IMM8_DFV_APX_N3` — `CCMPNL`
- `CCMPNL_MEMv_IMMz_DFV_APX_N3` — `CCMPNL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPNLE

`CCMPNLE` performs the architecture's conditional compare operation when the condition-code state denotes signed greater; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPNLE_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPNLE`
- `CCMPNLE_GPR8i8_IMM8_DFV_APX_N3` — `CCMPNLE`
- `CCMPNLE_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPNLE`
- `CCMPNLE_GPRv_GPRv_DFV_APX_N3` — `CCMPNLE`
- `CCMPNLE_GPRv_IMM8_DFV_APX_N3` — `CCMPNLE`
- `CCMPNLE_GPRv_IMMz_DFV_APX_N3` — `CCMPNLE`
- `CCMPNLE_GPRv_MEMv_DFV_APX_N3` — `CCMPNLE`
- `CCMPNLE_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPNLE`
- `CCMPNLE_MEMi8_IMM8_DFV_APX_N3` — `CCMPNLE`
- `CCMPNLE_MEMv_GPRv_DFV_APX_N3` — `CCMPNLE`
- `CCMPNLE_MEMv_IMM8_DFV_APX_N3` — `CCMPNLE`
- `CCMPNLE_MEMv_IMMz_DFV_APX_N3` — `CCMPNLE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPNO

`CCMPNO` performs the architecture's conditional compare operation when the condition-code state denotes no signed overflow; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPNO_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPNO`
- `CCMPNO_GPR8i8_IMM8_DFV_APX_N3` — `CCMPNO`
- `CCMPNO_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPNO`
- `CCMPNO_GPRv_GPRv_DFV_APX_N3` — `CCMPNO`
- `CCMPNO_GPRv_IMM8_DFV_APX_N3` — `CCMPNO`
- `CCMPNO_GPRv_IMMz_DFV_APX_N3` — `CCMPNO`
- `CCMPNO_GPRv_MEMv_DFV_APX_N3` — `CCMPNO`
- `CCMPNO_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPNO`
- `CCMPNO_MEMi8_IMM8_DFV_APX_N3` — `CCMPNO`
- `CCMPNO_MEMv_GPRv_DFV_APX_N3` — `CCMPNO`
- `CCMPNO_MEMv_IMM8_DFV_APX_N3` — `CCMPNO`
- `CCMPNO_MEMv_IMMz_DFV_APX_N3` — `CCMPNO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPNS

`CCMPNS` performs the architecture's conditional compare operation when the condition-code state denotes non-negative; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPNS_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPNS`
- `CCMPNS_GPR8i8_IMM8_DFV_APX_N3` — `CCMPNS`
- `CCMPNS_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPNS`
- `CCMPNS_GPRv_GPRv_DFV_APX_N3` — `CCMPNS`
- `CCMPNS_GPRv_IMM8_DFV_APX_N3` — `CCMPNS`
- `CCMPNS_GPRv_IMMz_DFV_APX_N3` — `CCMPNS`
- `CCMPNS_GPRv_MEMv_DFV_APX_N3` — `CCMPNS`
- `CCMPNS_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPNS`
- `CCMPNS_MEMi8_IMM8_DFV_APX_N3` — `CCMPNS`
- `CCMPNS_MEMv_GPRv_DFV_APX_N3` — `CCMPNS`
- `CCMPNS_MEMv_IMM8_DFV_APX_N3` — `CCMPNS`
- `CCMPNS_MEMv_IMMz_DFV_APX_N3` — `CCMPNS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPNZ

`CCMPNZ` performs the architecture's conditional compare operation when the condition-code state denotes nonzero; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPNZ_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPNZ`
- `CCMPNZ_GPR8i8_IMM8_DFV_APX_N3` — `CCMPNZ`
- `CCMPNZ_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPNZ`
- `CCMPNZ_GPRv_GPRv_DFV_APX_N3` — `CCMPNZ`
- `CCMPNZ_GPRv_IMM8_DFV_APX_N3` — `CCMPNZ`
- `CCMPNZ_GPRv_IMMz_DFV_APX_N3` — `CCMPNZ`
- `CCMPNZ_GPRv_MEMv_DFV_APX_N3` — `CCMPNZ`
- `CCMPNZ_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPNZ`
- `CCMPNZ_MEMi8_IMM8_DFV_APX_N3` — `CCMPNZ`
- `CCMPNZ_MEMv_GPRv_DFV_APX_N3` — `CCMPNZ`
- `CCMPNZ_MEMv_IMM8_DFV_APX_N3` — `CCMPNZ`
- `CCMPNZ_MEMv_IMMz_DFV_APX_N3` — `CCMPNZ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPO

`CCMPO` performs the architecture's conditional compare operation when the condition-code state denotes signed overflow; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPO_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPO`
- `CCMPO_GPR8i8_IMM8_DFV_APX_N3` — `CCMPO`
- `CCMPO_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPO`
- `CCMPO_GPRv_GPRv_DFV_APX_N3` — `CCMPO`
- `CCMPO_GPRv_IMM8_DFV_APX_N3` — `CCMPO`
- `CCMPO_GPRv_IMMz_DFV_APX_N3` — `CCMPO`
- `CCMPO_GPRv_MEMv_DFV_APX_N3` — `CCMPO`
- `CCMPO_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPO`
- `CCMPO_MEMi8_IMM8_DFV_APX_N3` — `CCMPO`
- `CCMPO_MEMv_GPRv_DFV_APX_N3` — `CCMPO`
- `CCMPO_MEMv_IMM8_DFV_APX_N3` — `CCMPO`
- `CCMPO_MEMv_IMMz_DFV_APX_N3` — `CCMPO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPS

`CCMPS` performs the architecture's conditional compare operation when the condition-code state denotes negative; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPS_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPS`
- `CCMPS_GPR8i8_IMM8_DFV_APX_N3` — `CCMPS`
- `CCMPS_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPS`
- `CCMPS_GPRv_GPRv_DFV_APX_N3` — `CCMPS`
- `CCMPS_GPRv_IMM8_DFV_APX_N3` — `CCMPS`
- `CCMPS_GPRv_IMMz_DFV_APX_N3` — `CCMPS`
- `CCMPS_GPRv_MEMv_DFV_APX_N3` — `CCMPS`
- `CCMPS_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPS`
- `CCMPS_MEMi8_IMM8_DFV_APX_N3` — `CCMPS`
- `CCMPS_MEMv_GPRv_DFV_APX_N3` — `CCMPS`
- `CCMPS_MEMv_IMM8_DFV_APX_N3` — `CCMPS`
- `CCMPS_MEMv_IMMz_DFV_APX_N3` — `CCMPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPT

`CCMPT` performs the architecture's conditional compare operation when the condition-code state denotes true; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPT_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPT`
- `CCMPT_GPR8i8_IMM8_DFV_APX_N3` — `CCMPT`
- `CCMPT_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPT`
- `CCMPT_GPRv_GPRv_DFV_APX_N3` — `CCMPT`
- `CCMPT_GPRv_IMM8_DFV_APX_N3` — `CCMPT`
- `CCMPT_GPRv_IMMz_DFV_APX_N3` — `CCMPT`
- `CCMPT_GPRv_MEMv_DFV_APX_N3` — `CCMPT`
- `CCMPT_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPT`
- `CCMPT_MEMi8_IMM8_DFV_APX_N3` — `CCMPT`
- `CCMPT_MEMv_GPRv_DFV_APX_N3` — `CCMPT`
- `CCMPT_MEMv_IMM8_DFV_APX_N3` — `CCMPT`
- `CCMPT_MEMv_IMMz_DFV_APX_N3` — `CCMPT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CCMPZ

`CCMPZ` performs the architecture's conditional compare operation when the condition-code state denotes zero / equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 22 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CCMPZ_GPR8i8_GPR8i8_DFV_APX_N3` — `CCMPZ`
- `CCMPZ_GPR8i8_IMM8_DFV_APX_N3` — `CCMPZ`
- `CCMPZ_GPR8i8_MEMi8_DFV_APX_N3` — `CCMPZ`
- `CCMPZ_GPRv_GPRv_DFV_APX_N3` — `CCMPZ`
- `CCMPZ_GPRv_IMM8_DFV_APX_N3` — `CCMPZ`
- `CCMPZ_GPRv_IMMz_DFV_APX_N3` — `CCMPZ`
- `CCMPZ_GPRv_MEMv_DFV_APX_N3` — `CCMPZ`
- `CCMPZ_MEMi8_GPR8i8_DFV_APX_N3` — `CCMPZ`
- `CCMPZ_MEMi8_IMM8_DFV_APX_N3` — `CCMPZ`
- `CCMPZ_MEMv_GPRv_DFV_APX_N3` — `CCMPZ`
- `CCMPZ_MEMv_IMM8_DFV_APX_N3` — `CCMPZ`
- `CCMPZ_MEMv_IMMz_DFV_APX_N3` — `CCMPZ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CDQ

`CDQ` sign-extends EAX into EDX:EAX. The pinned XED inventory represents it with 3 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `CONVERT`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16`, `32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EDX EAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CDQ` — `CDQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CDQE

`CDQE` sign-extends EAX into RAX. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `LONGMODE`
- XED category/categories: `CONVERT`
- ISA set(s): `LONGMODE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RAX EAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CDQE` — `CDQE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVB

`CFCMOVB` conditionally moves an x87 value when the condition-code state denotes below (carry set); otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVB_GPRv_GPRv_APX_N3` — `CFCMOVB`
- `CFCMOVB_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVB`
- `CFCMOVB_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVB`
- `CFCMOVB_GPRv_MEMv_APX_N3` — `CFCMOVB`
- `CFCMOVB_MEMv_GPRv_APX_N3` — `CFCMOVB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVBE

`CFCMOVBE` conditionally moves an x87 value when the condition-code state denotes below or equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVBE_GPRv_GPRv_APX_N3` — `CFCMOVBE`
- `CFCMOVBE_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVBE`
- `CFCMOVBE_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVBE`
- `CFCMOVBE_GPRv_MEMv_APX_N3` — `CFCMOVBE`
- `CFCMOVBE_MEMv_GPRv_APX_N3` — `CFCMOVBE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVL

`CFCMOVL` conditionally moves an x87 value when the condition-code state denotes less in signed comparison; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVL_GPRv_GPRv_APX_N3` — `CFCMOVL`
- `CFCMOVL_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVL`
- `CFCMOVL_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVL`
- `CFCMOVL_GPRv_MEMv_APX_N3` — `CFCMOVL`
- `CFCMOVL_MEMv_GPRv_APX_N3` — `CFCMOVL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVLE

`CFCMOVLE` conditionally moves an x87 value when the condition-code state denotes less or equal in signed comparison; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVLE_GPRv_GPRv_APX_N3` — `CFCMOVLE`
- `CFCMOVLE_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVLE`
- `CFCMOVLE_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVLE`
- `CFCMOVLE_GPRv_MEMv_APX_N3` — `CFCMOVLE`
- `CFCMOVLE_MEMv_GPRv_APX_N3` — `CFCMOVLE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVNB

`CFCMOVNB` conditionally moves an x87 value when the condition-code state denotes not below / unsigned above-or-equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVNB_GPRv_GPRv_APX_N3` — `CFCMOVNB`
- `CFCMOVNB_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVNB`
- `CFCMOVNB_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVNB`
- `CFCMOVNB_GPRv_MEMv_APX_N3` — `CFCMOVNB`
- `CFCMOVNB_MEMv_GPRv_APX_N3` — `CFCMOVNB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVNBE

`CFCMOVNBE` conditionally moves an x87 value when the condition-code state denotes unsigned above; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVNBE_GPRv_GPRv_APX_N3` — `CFCMOVNBE`
- `CFCMOVNBE_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVNBE`
- `CFCMOVNBE_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVNBE`
- `CFCMOVNBE_GPRv_MEMv_APX_N3` — `CFCMOVNBE`
- `CFCMOVNBE_MEMv_GPRv_APX_N3` — `CFCMOVNBE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVNL

`CFCMOVNL` conditionally moves an x87 value when the condition-code state denotes signed greater-or-equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVNL_GPRv_GPRv_APX_N3` — `CFCMOVNL`
- `CFCMOVNL_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVNL`
- `CFCMOVNL_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVNL`
- `CFCMOVNL_GPRv_MEMv_APX_N3` — `CFCMOVNL`
- `CFCMOVNL_MEMv_GPRv_APX_N3` — `CFCMOVNL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVNLE

`CFCMOVNLE` conditionally moves an x87 value when the condition-code state denotes signed greater; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVNLE_GPRv_GPRv_APX_N3` — `CFCMOVNLE`
- `CFCMOVNLE_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVNLE`
- `CFCMOVNLE_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVNLE`
- `CFCMOVNLE_GPRv_MEMv_APX_N3` — `CFCMOVNLE`
- `CFCMOVNLE_MEMv_GPRv_APX_N3` — `CFCMOVNLE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVNO

`CFCMOVNO` conditionally moves an x87 value when the condition-code state denotes no signed overflow; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVNO_GPRv_GPRv_APX_N3` — `CFCMOVNO`
- `CFCMOVNO_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVNO`
- `CFCMOVNO_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVNO`
- `CFCMOVNO_GPRv_MEMv_APX_N3` — `CFCMOVNO`
- `CFCMOVNO_MEMv_GPRv_APX_N3` — `CFCMOVNO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVNP

`CFCMOVNP` conditionally moves an x87 value when the condition-code state denotes not parity; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVNP_GPRv_GPRv_APX_N3` — `CFCMOVNP`
- `CFCMOVNP_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVNP`
- `CFCMOVNP_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVNP`
- `CFCMOVNP_GPRv_MEMv_APX_N3` — `CFCMOVNP`
- `CFCMOVNP_MEMv_GPRv_APX_N3` — `CFCMOVNP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVNS

`CFCMOVNS` conditionally moves an x87 value when the condition-code state denotes non-negative; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVNS_GPRv_GPRv_APX_N3` — `CFCMOVNS`
- `CFCMOVNS_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVNS`
- `CFCMOVNS_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVNS`
- `CFCMOVNS_GPRv_MEMv_APX_N3` — `CFCMOVNS`
- `CFCMOVNS_MEMv_GPRv_APX_N3` — `CFCMOVNS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVNZ

`CFCMOVNZ` conditionally moves an x87 value when the condition-code state denotes nonzero; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVNZ_GPRv_GPRv_APX_N3` — `CFCMOVNZ`
- `CFCMOVNZ_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVNZ`
- `CFCMOVNZ_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVNZ`
- `CFCMOVNZ_GPRv_MEMv_APX_N3` — `CFCMOVNZ`
- `CFCMOVNZ_MEMv_GPRv_APX_N3` — `CFCMOVNZ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVO

`CFCMOVO` conditionally moves an x87 value when the condition-code state denotes signed overflow; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVO_GPRv_GPRv_APX_N3` — `CFCMOVO`
- `CFCMOVO_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVO`
- `CFCMOVO_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVO`
- `CFCMOVO_GPRv_MEMv_APX_N3` — `CFCMOVO`
- `CFCMOVO_MEMv_GPRv_APX_N3` — `CFCMOVO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVP

`CFCMOVP` conditionally moves an x87 value when the condition-code state denotes parity; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVP_GPRv_GPRv_APX_N3` — `CFCMOVP`
- `CFCMOVP_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVP`
- `CFCMOVP_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVP`
- `CFCMOVP_GPRv_MEMv_APX_N3` — `CFCMOVP`
- `CFCMOVP_MEMv_GPRv_APX_N3` — `CFCMOVP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVS

`CFCMOVS` conditionally moves an x87 value when the condition-code state denotes negative; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVS_GPRv_GPRv_APX_N3` — `CFCMOVS`
- `CFCMOVS_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVS`
- `CFCMOVS_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVS`
- `CFCMOVS_GPRv_MEMv_APX_N3` — `CFCMOVS`
- `CFCMOVS_MEMv_GPRv_APX_N3` — `CFCMOVS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CFCMOVZ

`CFCMOVZ` conditionally moves an x87 value when the condition-code state denotes zero / equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 12 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CFCMOVZ_GPRv_GPRv_APX_N3` — `CFCMOVZ`
- `CFCMOVZ_GPRv_GPRv_GPRv_APX_N3` — `CFCMOVZ`
- `CFCMOVZ_GPRv_GPRv_MEMv_APX_N3` — `CFCMOVZ`
- `CFCMOVZ_GPRv_MEMv_APX_N3` — `CFCMOVZ`
- `CFCMOVZ_MEMv_GPRv_APX_N3` — `CFCMOVZ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CLAC

`CLAC` clears the SMAP access-control flag so supervisor-mode explicit accesses to user pages are blocked again. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SMAP`
- XED category/categories: `SMAP`
- ISA set(s): `SMAP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CLAC` — `CLAC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CLC

`CLC` clears the carry flag. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `FLAGOP`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CLC` — `CLC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CLD

`CLD` clears the direction flag so string instructions advance their implicit index registers. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `FLAGOP`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CLD` — `CLD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CLDEMOTE

`CLDEMOTE` hints that the cache line containing an address should be demoted from a nearer cache level to reduce pressure while retaining it in the hierarchy. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CLDEMOTE`
- XED category/categories: `CLDEMOTE`
- ISA set(s): `CLDEMOTE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CLDEMOTE_MEMu8` — `CLDEMOTE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CLZERO

`CLZERO` zeros the cache line containing the addressed byte using AMD's cache-line-zero operation. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CLZERO`
- XED category/categories: `CLZERO`
- ISA set(s): `CLZERO`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `ArAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CLZERO` — `CLZERO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMC

`CMC` complements the carry flag. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `FLAGOP`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMC` — `CMC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVB

`CMOVB` copies the source operand to the destination only when the condition-code state denotes below (carry set); otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVB_GPRv_GPRv` — `CMOVB`
- `CMOVB_GPRv_GPRv_GPRv_APX_N3` — `CMOVB`
- `CMOVB_GPRv_GPRv_MEMv_APX_N3` — `CMOVB`
- `CMOVB_GPRv_MEMv` — `CMOVB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVBE

`CMOVBE` copies the source operand to the destination only when the condition-code state denotes below or equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVBE_GPRv_GPRv` — `CMOVBE`
- `CMOVBE_GPRv_GPRv_GPRv_APX_N3` — `CMOVBE`
- `CMOVBE_GPRv_GPRv_MEMv_APX_N3` — `CMOVBE`
- `CMOVBE_GPRv_MEMv` — `CMOVBE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVL

`CMOVL` copies the source operand to the destination only when the condition-code state denotes less in signed comparison; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVL_GPRv_GPRv` — `CMOVL`
- `CMOVL_GPRv_GPRv_GPRv_APX_N3` — `CMOVL`
- `CMOVL_GPRv_GPRv_MEMv_APX_N3` — `CMOVL`
- `CMOVL_GPRv_MEMv` — `CMOVL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVLE

`CMOVLE` copies the source operand to the destination only when the condition-code state denotes less or equal in signed comparison; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVLE_GPRv_GPRv` — `CMOVLE`
- `CMOVLE_GPRv_GPRv_GPRv_APX_N3` — `CMOVLE`
- `CMOVLE_GPRv_GPRv_MEMv_APX_N3` — `CMOVLE`
- `CMOVLE_GPRv_MEMv` — `CMOVLE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVNB

`CMOVNB` copies the source operand to the destination only when the condition-code state denotes not below / unsigned above-or-equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVNB_GPRv_GPRv` — `CMOVNB`
- `CMOVNB_GPRv_GPRv_GPRv_APX_N3` — `CMOVNB`
- `CMOVNB_GPRv_GPRv_MEMv_APX_N3` — `CMOVNB`
- `CMOVNB_GPRv_MEMv` — `CMOVNB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVNBE

`CMOVNBE` copies the source operand to the destination only when the condition-code state denotes unsigned above; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVNBE_GPRv_GPRv` — `CMOVNBE`
- `CMOVNBE_GPRv_GPRv_GPRv_APX_N3` — `CMOVNBE`
- `CMOVNBE_GPRv_GPRv_MEMv_APX_N3` — `CMOVNBE`
- `CMOVNBE_GPRv_MEMv` — `CMOVNBE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVNL

`CMOVNL` copies the source operand to the destination only when the condition-code state denotes signed greater-or-equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVNL_GPRv_GPRv` — `CMOVNL`
- `CMOVNL_GPRv_GPRv_GPRv_APX_N3` — `CMOVNL`
- `CMOVNL_GPRv_GPRv_MEMv_APX_N3` — `CMOVNL`
- `CMOVNL_GPRv_MEMv` — `CMOVNL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVNLE

`CMOVNLE` copies the source operand to the destination only when the condition-code state denotes signed greater; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVNLE_GPRv_GPRv` — `CMOVNLE`
- `CMOVNLE_GPRv_GPRv_GPRv_APX_N3` — `CMOVNLE`
- `CMOVNLE_GPRv_GPRv_MEMv_APX_N3` — `CMOVNLE`
- `CMOVNLE_GPRv_MEMv` — `CMOVNLE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVNO

`CMOVNO` copies the source operand to the destination only when the condition-code state denotes no signed overflow; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVNO_GPRv_GPRv` — `CMOVNO`
- `CMOVNO_GPRv_GPRv_GPRv_APX_N3` — `CMOVNO`
- `CMOVNO_GPRv_GPRv_MEMv_APX_N3` — `CMOVNO`
- `CMOVNO_GPRv_MEMv` — `CMOVNO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVNP

`CMOVNP` copies the source operand to the destination only when the condition-code state denotes not parity; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVNP_GPRv_GPRv` — `CMOVNP`
- `CMOVNP_GPRv_GPRv_GPRv_APX_N3` — `CMOVNP`
- `CMOVNP_GPRv_GPRv_MEMv_APX_N3` — `CMOVNP`
- `CMOVNP_GPRv_MEMv` — `CMOVNP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVNS

`CMOVNS` copies the source operand to the destination only when the condition-code state denotes non-negative; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVNS_GPRv_GPRv` — `CMOVNS`
- `CMOVNS_GPRv_GPRv_GPRv_APX_N3` — `CMOVNS`
- `CMOVNS_GPRv_GPRv_MEMv_APX_N3` — `CMOVNS`
- `CMOVNS_GPRv_MEMv` — `CMOVNS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVNZ

`CMOVNZ` copies the source operand to the destination only when the condition-code state denotes nonzero; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVNZ_GPRv_GPRv` — `CMOVNZ`
- `CMOVNZ_GPRv_GPRv_GPRv_APX_N3` — `CMOVNZ`
- `CMOVNZ_GPRv_GPRv_MEMv_APX_N3` — `CMOVNZ`
- `CMOVNZ_GPRv_MEMv` — `CMOVNZ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVO

`CMOVO` copies the source operand to the destination only when the condition-code state denotes signed overflow; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVO_GPRv_GPRv` — `CMOVO`
- `CMOVO_GPRv_GPRv_GPRv_APX_N3` — `CMOVO`
- `CMOVO_GPRv_GPRv_MEMv_APX_N3` — `CMOVO`
- `CMOVO_GPRv_MEMv` — `CMOVO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVP

`CMOVP` copies the source operand to the destination only when the condition-code state denotes parity; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVP_GPRv_GPRv` — `CMOVP`
- `CMOVP_GPRv_GPRv_GPRv_APX_N3` — `CMOVP`
- `CMOVP_GPRv_GPRv_MEMv_APX_N3` — `CMOVP`
- `CMOVP_GPRv_MEMv` — `CMOVP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVS

`CMOVS` copies the source operand to the destination only when the condition-code state denotes negative; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVS_GPRv_GPRv` — `CMOVS`
- `CMOVS_GPRv_GPRv_GPRv_APX_N3` — `CMOVS`
- `CMOVS_GPRv_GPRv_MEMv_APX_N3` — `CMOVS`
- `CMOVS_GPRv_MEMv` — `CMOVS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMOVZ

`CMOVZ` copies the source operand to the destination only when the condition-code state denotes zero / equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `APX`, `CMOV`
- ISA set(s): `APX_F_N3`, `CMOV`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMOVZ_GPRv_GPRv` — `CMOVZ`
- `CMOVZ_GPRv_GPRv_GPRv_APX_N3` — `CMOVZ`
- `CMOVZ_GPRv_GPRv_MEMv_APX_N3` — `CMOVZ`
- `CMOVZ_GPRv_MEMv` — `CMOVZ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMP

`CMP` subtracts conceptually to set arithmetic flags for a comparison and discards the numerical result. The pinned XED inventory represents it with 18 normalized encoding records and 18 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMP_AL_IMMb` — `CMP`
- `CMP_GPR8_GPR8_38` — `CMP`
- `CMP_GPR8_GPR8_3A` — `CMP`
- `CMP_GPR8_IMMb_80r7` — `CMP`
- `CMP_GPR8_IMMb_82r7` — `CMP`
- `CMP_GPR8_MEMb` — `CMP`
- `CMP_GPRv_GPRv_39` — `CMP`
- `CMP_GPRv_GPRv_3B` — `CMP`
- `CMP_GPRv_IMMb` — `CMP`
- `CMP_GPRv_IMMz` — `CMP`
- `CMP_GPRv_MEMv` — `CMP`
- `CMP_MEMb_GPR8` — `CMP`
- … 6 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this belongs to the small x86-64 user-mode baseline worth supporting early. Flag liveness, register constraints, and exact encoding choice should be explicit.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPBEXADD

`CMPBEXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is unsigned below-or-equal. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPBEXADD_MEMu32_GPR32u32_GPR32u32` — `CMPBEXADD`
- `CMPBEXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPBEXADD`
- `CMPBEXADD_MEMu64_GPR64u64_GPR64u64` — `CMPBEXADD`
- `CMPBEXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPBEXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPBXADD

`CMPBXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is unsigned below. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPBXADD_MEMu32_GPR32u32_GPR32u32` — `CMPBXADD`
- `CMPBXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPBXADD`
- `CMPBXADD_MEMu64_GPR64u64_GPR64u64` — `CMPBXADD`
- `CMPBXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPBXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPLEXADD

`CMPLEXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is signed less-or-equal. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPLEXADD_MEMu32_GPR32u32_GPR32u32` — `CMPLEXADD`
- `CMPLEXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPLEXADD`
- `CMPLEXADD_MEMu64_GPR64u64_GPR64u64` — `CMPLEXADD`
- `CMPLEXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPLEXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPLXADD

`CMPLXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is signed less-than. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPLXADD_MEMu32_GPR32u32_GPR32u32` — `CMPLXADD`
- `CMPLXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPLXADD`
- `CMPLXADD_MEMu64_GPR64u64_GPR64u64` — `CMPLXADD`
- `CMPLXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPLXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPNBEXADD

`CMPNBEXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is unsigned above. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPNBEXADD_MEMu32_GPR32u32_GPR32u32` — `CMPNBEXADD`
- `CMPNBEXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPNBEXADD`
- `CMPNBEXADD_MEMu64_GPR64u64_GPR64u64` — `CMPNBEXADD`
- `CMPNBEXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPNBEXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPNBXADD

`CMPNBXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is unsigned above-or-equal. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPNBXADD_MEMu32_GPR32u32_GPR32u32` — `CMPNBXADD`
- `CMPNBXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPNBXADD`
- `CMPNBXADD_MEMu64_GPR64u64_GPR64u64` — `CMPNBXADD`
- `CMPNBXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPNBXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPNLEXADD

`CMPNLEXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is signed greater-than. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPNLEXADD_MEMu32_GPR32u32_GPR32u32` — `CMPNLEXADD`
- `CMPNLEXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPNLEXADD`
- `CMPNLEXADD_MEMu64_GPR64u64_GPR64u64` — `CMPNLEXADD`
- `CMPNLEXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPNLEXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPNLXADD

`CMPNLXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is signed greater-or-equal. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPNLXADD_MEMu32_GPR32u32_GPR32u32` — `CMPNLXADD`
- `CMPNLXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPNLXADD`
- `CMPNLXADD_MEMu64_GPR64u64_GPR64u64` — `CMPNLXADD`
- `CMPNLXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPNLXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPNOXADD

`CMPNOXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is no overflow. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPNOXADD_MEMu32_GPR32u32_GPR32u32` — `CMPNOXADD`
- `CMPNOXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPNOXADD`
- `CMPNOXADD_MEMu64_GPR64u64_GPR64u64` — `CMPNOXADD`
- `CMPNOXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPNOXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPNPXADD

`CMPNPXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is no parity. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPNPXADD_MEMu32_GPR32u32_GPR32u32` — `CMPNPXADD`
- `CMPNPXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPNPXADD`
- `CMPNPXADD_MEMu64_GPR64u64_GPR64u64` — `CMPNPXADD`
- `CMPNPXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPNPXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPNSXADD

`CMPNSXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is non-negative. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPNSXADD_MEMu32_GPR32u32_GPR32u32` — `CMPNSXADD`
- `CMPNSXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPNSXADD`
- `CMPNSXADD_MEMu64_GPR64u64_GPR64u64` — `CMPNSXADD`
- `CMPNSXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPNSXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPNZXADD

`CMPNZXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is nonzero. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPNZXADD_MEMu32_GPR32u32_GPR32u32` — `CMPNZXADD`
- `CMPNZXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPNZXADD`
- `CMPNZXADD_MEMu64_GPR64u64_GPR64u64` — `CMPNZXADD`
- `CMPNZXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPNZXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPOXADD

`CMPOXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is overflow. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPOXADD_MEMu32_GPR32u32_GPR32u32` — `CMPOXADD`
- `CMPOXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPOXADD`
- `CMPOXADD_MEMu64_GPR64u64_GPR64u64` — `CMPOXADD`
- `CMPOXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPOXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPPXADD

`CMPPXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is parity. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPPXADD_MEMu32_GPR32u32_GPR32u32` — `CMPPXADD`
- `CMPPXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPPXADD`
- `CMPPXADD_MEMu64_GPR64u64_GPR64u64` — `CMPPXADD`
- `CMPPXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPPXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CMPZXADD

`CMPZXADD` performs the APX CMPccXADD atomic compare-and-conditional-add primitive: it compares the memory value with the comparison operand and adds the update operand to memory when the resulting condition is zero/equal. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `CMPCCXADD`
- XED category/categories: `APX`, `VEX`
- ISA set(s): `APX_F_CMPCCXADD`, `CMPCCXADD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32 GPR32`; `MEM GPR64 GPR64`; `MEM VGPR32 VGPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CMPZXADD_MEMu32_GPR32u32_GPR32u32` — `CMPZXADD`
- `CMPZXADD_MEMu32_GPR32u32_GPR32u32_APX` — `CMPZXADD`
- `CMPZXADD_MEMu64_GPR64u64_GPR64u64` — `CMPZXADD`
- `CMPZXADD_MEMu64_GPR64u64_GPR64u64_APX` — `CMPZXADD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CQO

`CQO` sign-extends RAX into RDX:RAX. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `LONGMODE`
- XED category/categories: `CONVERT`
- ISA set(s): `LONGMODE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RDX RAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CQO` — `CQO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTB

`CTESTB` performs the architecture's conditional test operation when the condition-code state denotes below (carry set); otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTB_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTB`
- `CTESTB_GPR8i8_IMM8_DFV_APX_N3` — `CTESTB`
- `CTESTB_GPRv_GPRv_DFV_APX_N3` — `CTESTB`
- `CTESTB_GPRv_IMMz_DFV_APX_N3` — `CTESTB`
- `CTESTB_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTB`
- `CTESTB_MEMi8_IMM8_DFV_APX_N3` — `CTESTB`
- `CTESTB_MEMv_GPRv_DFV_APX_N3` — `CTESTB`
- `CTESTB_MEMv_IMMz_DFV_APX_N3` — `CTESTB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTBE

`CTESTBE` performs the architecture's conditional test operation when the condition-code state denotes below or equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTBE_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTBE`
- `CTESTBE_GPR8i8_IMM8_DFV_APX_N3` — `CTESTBE`
- `CTESTBE_GPRv_GPRv_DFV_APX_N3` — `CTESTBE`
- `CTESTBE_GPRv_IMMz_DFV_APX_N3` — `CTESTBE`
- `CTESTBE_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTBE`
- `CTESTBE_MEMi8_IMM8_DFV_APX_N3` — `CTESTBE`
- `CTESTBE_MEMv_GPRv_DFV_APX_N3` — `CTESTBE`
- `CTESTBE_MEMv_IMMz_DFV_APX_N3` — `CTESTBE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTF

`CTESTF` performs the architecture's conditional test operation when the condition-code state denotes false; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTF_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTF`
- `CTESTF_GPR8i8_IMM8_DFV_APX_N3` — `CTESTF`
- `CTESTF_GPRv_GPRv_DFV_APX_N3` — `CTESTF`
- `CTESTF_GPRv_IMMz_DFV_APX_N3` — `CTESTF`
- `CTESTF_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTF`
- `CTESTF_MEMi8_IMM8_DFV_APX_N3` — `CTESTF`
- `CTESTF_MEMv_GPRv_DFV_APX_N3` — `CTESTF`
- `CTESTF_MEMv_IMMz_DFV_APX_N3` — `CTESTF`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTL

`CTESTL` performs the architecture's conditional test operation when the condition-code state denotes less in signed comparison; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTL_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTL`
- `CTESTL_GPR8i8_IMM8_DFV_APX_N3` — `CTESTL`
- `CTESTL_GPRv_GPRv_DFV_APX_N3` — `CTESTL`
- `CTESTL_GPRv_IMMz_DFV_APX_N3` — `CTESTL`
- `CTESTL_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTL`
- `CTESTL_MEMi8_IMM8_DFV_APX_N3` — `CTESTL`
- `CTESTL_MEMv_GPRv_DFV_APX_N3` — `CTESTL`
- `CTESTL_MEMv_IMMz_DFV_APX_N3` — `CTESTL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTLE

`CTESTLE` performs the architecture's conditional test operation when the condition-code state denotes less or equal in signed comparison; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTLE_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTLE`
- `CTESTLE_GPR8i8_IMM8_DFV_APX_N3` — `CTESTLE`
- `CTESTLE_GPRv_GPRv_DFV_APX_N3` — `CTESTLE`
- `CTESTLE_GPRv_IMMz_DFV_APX_N3` — `CTESTLE`
- `CTESTLE_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTLE`
- `CTESTLE_MEMi8_IMM8_DFV_APX_N3` — `CTESTLE`
- `CTESTLE_MEMv_GPRv_DFV_APX_N3` — `CTESTLE`
- `CTESTLE_MEMv_IMMz_DFV_APX_N3` — `CTESTLE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTNB

`CTESTNB` performs the architecture's conditional test operation when the condition-code state denotes not below / unsigned above-or-equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTNB_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTNB`
- `CTESTNB_GPR8i8_IMM8_DFV_APX_N3` — `CTESTNB`
- `CTESTNB_GPRv_GPRv_DFV_APX_N3` — `CTESTNB`
- `CTESTNB_GPRv_IMMz_DFV_APX_N3` — `CTESTNB`
- `CTESTNB_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTNB`
- `CTESTNB_MEMi8_IMM8_DFV_APX_N3` — `CTESTNB`
- `CTESTNB_MEMv_GPRv_DFV_APX_N3` — `CTESTNB`
- `CTESTNB_MEMv_IMMz_DFV_APX_N3` — `CTESTNB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTNBE

`CTESTNBE` performs the architecture's conditional test operation when the condition-code state denotes unsigned above; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTNBE_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTNBE`
- `CTESTNBE_GPR8i8_IMM8_DFV_APX_N3` — `CTESTNBE`
- `CTESTNBE_GPRv_GPRv_DFV_APX_N3` — `CTESTNBE`
- `CTESTNBE_GPRv_IMMz_DFV_APX_N3` — `CTESTNBE`
- `CTESTNBE_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTNBE`
- `CTESTNBE_MEMi8_IMM8_DFV_APX_N3` — `CTESTNBE`
- `CTESTNBE_MEMv_GPRv_DFV_APX_N3` — `CTESTNBE`
- `CTESTNBE_MEMv_IMMz_DFV_APX_N3` — `CTESTNBE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTNL

`CTESTNL` performs the architecture's conditional test operation when the condition-code state denotes signed greater-or-equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTNL_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTNL`
- `CTESTNL_GPR8i8_IMM8_DFV_APX_N3` — `CTESTNL`
- `CTESTNL_GPRv_GPRv_DFV_APX_N3` — `CTESTNL`
- `CTESTNL_GPRv_IMMz_DFV_APX_N3` — `CTESTNL`
- `CTESTNL_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTNL`
- `CTESTNL_MEMi8_IMM8_DFV_APX_N3` — `CTESTNL`
- `CTESTNL_MEMv_GPRv_DFV_APX_N3` — `CTESTNL`
- `CTESTNL_MEMv_IMMz_DFV_APX_N3` — `CTESTNL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTNLE

`CTESTNLE` performs the architecture's conditional test operation when the condition-code state denotes signed greater; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTNLE_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTNLE`
- `CTESTNLE_GPR8i8_IMM8_DFV_APX_N3` — `CTESTNLE`
- `CTESTNLE_GPRv_GPRv_DFV_APX_N3` — `CTESTNLE`
- `CTESTNLE_GPRv_IMMz_DFV_APX_N3` — `CTESTNLE`
- `CTESTNLE_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTNLE`
- `CTESTNLE_MEMi8_IMM8_DFV_APX_N3` — `CTESTNLE`
- `CTESTNLE_MEMv_GPRv_DFV_APX_N3` — `CTESTNLE`
- `CTESTNLE_MEMv_IMMz_DFV_APX_N3` — `CTESTNLE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTNO

`CTESTNO` performs the architecture's conditional test operation when the condition-code state denotes no signed overflow; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTNO_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTNO`
- `CTESTNO_GPR8i8_IMM8_DFV_APX_N3` — `CTESTNO`
- `CTESTNO_GPRv_GPRv_DFV_APX_N3` — `CTESTNO`
- `CTESTNO_GPRv_IMMz_DFV_APX_N3` — `CTESTNO`
- `CTESTNO_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTNO`
- `CTESTNO_MEMi8_IMM8_DFV_APX_N3` — `CTESTNO`
- `CTESTNO_MEMv_GPRv_DFV_APX_N3` — `CTESTNO`
- `CTESTNO_MEMv_IMMz_DFV_APX_N3` — `CTESTNO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTNS

`CTESTNS` performs the architecture's conditional test operation when the condition-code state denotes non-negative; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTNS_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTNS`
- `CTESTNS_GPR8i8_IMM8_DFV_APX_N3` — `CTESTNS`
- `CTESTNS_GPRv_GPRv_DFV_APX_N3` — `CTESTNS`
- `CTESTNS_GPRv_IMMz_DFV_APX_N3` — `CTESTNS`
- `CTESTNS_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTNS`
- `CTESTNS_MEMi8_IMM8_DFV_APX_N3` — `CTESTNS`
- `CTESTNS_MEMv_GPRv_DFV_APX_N3` — `CTESTNS`
- `CTESTNS_MEMv_IMMz_DFV_APX_N3` — `CTESTNS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTNZ

`CTESTNZ` performs the architecture's conditional test operation when the condition-code state denotes nonzero; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTNZ_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTNZ`
- `CTESTNZ_GPR8i8_IMM8_DFV_APX_N3` — `CTESTNZ`
- `CTESTNZ_GPRv_GPRv_DFV_APX_N3` — `CTESTNZ`
- `CTESTNZ_GPRv_IMMz_DFV_APX_N3` — `CTESTNZ`
- `CTESTNZ_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTNZ`
- `CTESTNZ_MEMi8_IMM8_DFV_APX_N3` — `CTESTNZ`
- `CTESTNZ_MEMv_GPRv_DFV_APX_N3` — `CTESTNZ`
- `CTESTNZ_MEMv_IMMz_DFV_APX_N3` — `CTESTNZ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTO

`CTESTO` performs the architecture's conditional test operation when the condition-code state denotes signed overflow; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTO_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTO`
- `CTESTO_GPR8i8_IMM8_DFV_APX_N3` — `CTESTO`
- `CTESTO_GPRv_GPRv_DFV_APX_N3` — `CTESTO`
- `CTESTO_GPRv_IMMz_DFV_APX_N3` — `CTESTO`
- `CTESTO_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTO`
- `CTESTO_MEMi8_IMM8_DFV_APX_N3` — `CTESTO`
- `CTESTO_MEMv_GPRv_DFV_APX_N3` — `CTESTO`
- `CTESTO_MEMv_IMMz_DFV_APX_N3` — `CTESTO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTS

`CTESTS` performs the architecture's conditional test operation when the condition-code state denotes negative; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTS_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTS`
- `CTESTS_GPR8i8_IMM8_DFV_APX_N3` — `CTESTS`
- `CTESTS_GPRv_GPRv_DFV_APX_N3` — `CTESTS`
- `CTESTS_GPRv_IMMz_DFV_APX_N3` — `CTESTS`
- `CTESTS_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTS`
- `CTESTS_MEMi8_IMM8_DFV_APX_N3` — `CTESTS`
- `CTESTS_MEMv_GPRv_DFV_APX_N3` — `CTESTS`
- `CTESTS_MEMv_IMMz_DFV_APX_N3` — `CTESTS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTT

`CTESTT` performs the architecture's conditional test operation when the condition-code state denotes true; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTT_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTT`
- `CTESTT_GPR8i8_IMM8_DFV_APX_N3` — `CTESTT`
- `CTESTT_GPRv_GPRv_DFV_APX_N3` — `CTESTT`
- `CTESTT_GPRv_IMMz_DFV_APX_N3` — `CTESTT`
- `CTESTT_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTT`
- `CTESTT_MEMi8_IMM8_DFV_APX_N3` — `CTESTT`
- `CTESTT_MEMv_GPRv_DFV_APX_N3` — `CTESTT`
- `CTESTT_MEMv_IMMz_DFV_APX_N3` — `CTESTT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CTESTZ

`CTESTZ` performs the architecture's conditional test operation when the condition-code state denotes zero / equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 18 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`
- XED category/categories: `APX`
- ISA set(s): `APX_F_N3`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CTESTZ_GPR8i8_GPR8i8_DFV_APX_N3` — `CTESTZ`
- `CTESTZ_GPR8i8_IMM8_DFV_APX_N3` — `CTESTZ`
- `CTESTZ_GPRv_GPRv_DFV_APX_N3` — `CTESTZ`
- `CTESTZ_GPRv_IMMz_DFV_APX_N3` — `CTESTZ`
- `CTESTZ_MEMi8_GPR8i8_DFV_APX_N3` — `CTESTZ`
- `CTESTZ_MEMi8_IMM8_DFV_APX_N3` — `CTESTZ`
- `CTESTZ_MEMv_GPRv_DFV_APX_N3` — `CTESTZ`
- `CTESTZ_MEMv_IMMz_DFV_APX_N3` — `CTESTZ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CWD

`CWD` sign-extends AX into DX:AX. The pinned XED inventory represents it with 3 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `CONVERT`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16`, `32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `DX AX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CWD` — `CWD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CWDE

`CWDE` sign-extends AX into EAX. The pinned XED inventory represents it with 3 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `CONVERT`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16`, `32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX AX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CWDE` — `CWDE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## DAA

`DAA` adjusts AL after addition so the low and high nibbles represent a valid packed-BCD result, updating legacy arithmetic flags. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DECIMAL`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `AL`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `DAA` — `DAA`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## DAS

`DAS` adjusts AL after subtraction so the low and high nibbles represent a valid packed-BCD result, updating legacy arithmetic flags. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DECIMAL`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `AL`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `DAS` — `DAS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## DEC

`DEC` decrements its destination by one while preserving carry. The pinned XED inventory represents it with 29 normalized encoding records and 17 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPR8 GPR8`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `DEC_GPR8` — `DEC`
- `DEC_GPR8i8_APX` — `DEC`
- `DEC_GPR8i8_APX_N3` — `DEC`
- `DEC_GPR8i8_GPR8i8_APX_N3` — `DEC`
- `DEC_GPR8i8_MEMi8_APX_N3` — `DEC`
- `DEC_GPRv_48` — `DEC`
- `DEC_GPRv_APX` — `DEC`
- `DEC_GPRv_APX_N3` — `DEC`
- `DEC_GPRv_FFr1` — `DEC`
- `DEC_GPRv_GPRv_APX_N3` — `DEC`
- `DEC_GPRv_MEMv_APX_N3` — `DEC`
- `DEC_MEMb` — `DEC`
- … 5 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## DEC_LOCK

`DEC_LOCK` decrements its destination by one while preserving carry; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `DEC_LOCK_MEMb` — `DEC_LOCK`
- `DEC_LOCK_MEMv` — `DEC_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## DIV

`DIV` performs unsigned division of the implicit double-width dividend, producing quotient and remainder. The pinned XED inventory represents it with 16 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPRv`; `MEM`. Representative implicit state: `AX`; `OrAX OrDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `DIV_GPR8` — `DIV`
- `DIV_GPR8i8_APX` — `DIV`
- `DIV_GPR8i8_APX_N3` — `DIV`
- `DIV_GPRv` — `DIV`
- `DIV_GPRv_APX` — `DIV`
- `DIV_GPRv_APX_N3` — `DIV`
- `DIV_MEMb` — `DIV`
- `DIV_MEMi8_APX` — `DIV`
- `DIV_MEMi8_APX_N3` — `DIV`
- `DIV_MEMv` — `DIV`
- `DIV_MEMv_APX` — `DIV`
- `DIV_MEMv_APX_N3` — `DIV`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ENQCMD

`ENQCMD` submits a 64-byte command descriptor to a device portal and reports acceptance or retry status. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `ENQCMD`
- XED category/categories: `APX`, `ENQCMD`
- ISA set(s): `APX_F_ENQCMD`, `ENQCMD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `A_GPR MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ENQCMD_GPRa_MEMu32` — `ENQCMD`
- `ENQCMD_GPRav_MEMu32_APX` — `ENQCMD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ENQCMDS

`ENQCMDS` submits a 64-byte command descriptor to a device portal and reports acceptance or retry status. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `ENQCMD`
- XED category/categories: `APX`, `ENQCMD`
- ISA set(s): `APX_F_ENQCMD`, `ENQCMD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `A_GPR MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ENQCMDS_GPRa_MEMu32` — `ENQCMDS`
- `ENQCMDS_GPRav_MEMu32_APX` — `ENQCMDS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## HRESET

`HRESET` resets processor history components selected by a bitmap in EAX, giving privileged software an architectural way to discard selected hardware-history state. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `HRESET`
- XED category/categories: `HRESET`
- ISA set(s): `HRESET`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `IMM`. Representative implicit state: `EAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `HRESET_IMM8` — `HRESET`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## IBHF

`IBHF` forms an indirect-branch-history fence, preventing older branch history from influencing selected later indirect-branch predictions when the processor's BHI controls enable that behavior. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `IBHF`
- XED category/categories: `LEGACY`
- ISA set(s): `IBHF`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `IBHF` — `IBHF`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## IDIV

`IDIV` performs signed division of the implicit double-width dividend, producing quotient and remainder. The pinned XED inventory represents it with 16 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPRv`; `MEM`. Representative implicit state: `AX`; `OrAX OrDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `IDIV_GPR8` — `IDIV`
- `IDIV_GPR8i8_APX` — `IDIV`
- `IDIV_GPR8i8_APX_N3` — `IDIV`
- `IDIV_GPRv` — `IDIV`
- `IDIV_GPRv_APX` — `IDIV`
- `IDIV_GPRv_APX_N3` — `IDIV`
- `IDIV_MEMb` — `IDIV`
- `IDIV_MEMi8_APX` — `IDIV`
- `IDIV_MEMi8_APX_N3` — `IDIV`
- `IDIV_MEMv` — `IDIV`
- `IDIV_MEMv_APX` — `IDIV`
- `IDIV_MEMv_APX_N3` — `IDIV`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## IMUL

`IMUL` performs signed integer multiplication in widening or truncated explicit-destination forms. The pinned XED inventory represents it with 70 normalized encoding records and 36 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I186`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPRv`; `GPRv GPRv`; …. Representative implicit state: `AL AX`; `OrAX OrDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `IMUL_GPR8` — `IMUL`
- `IMUL_GPR8i8_APX` — `IMUL`
- `IMUL_GPR8i8_APX_N3` — `IMUL`
- `IMUL_GPRv` — `IMUL`
- `IMUL_GPRv_APX` — `IMUL`
- `IMUL_GPRv_APX_N3` — `IMUL`
- `IMUL_GPRv_GPRv` — `IMUL`
- `IMUL_GPRv_GPRv_APX` — `IMUL`
- `IMUL_GPRv_GPRv_APX_N3` — `IMUL`
- `IMUL_GPRv_GPRv_GPRv_APX_N3` — `IMUL`
- `IMUL_GPRv_GPRv_IMM8_APX` — `IMUL`
- `IMUL_GPRv_GPRv_IMM8_APX_N3` — `IMUL`
- … 24 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## IN

`IN` reads a byte, word, or doubleword from an I/O port into the accumulator using x86's separate port-I/O address space. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `IO`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `IMM`. Representative implicit state: `AL`; `AL DX`; `OeAX`; ….

Recorded flag behavior: not uniformly recorded.

### Important forms

- `IN_AL_DX` — `IN`
- `IN_AL_IMMb` — `IN`
- `IN_OeAX_DX` — `IN`
- `IN_OeAX_IMMb` — `IN`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INC

`INC` increments its destination by one while preserving carry. The pinned XED inventory represents it with 29 normalized encoding records and 17 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPR8 GPR8`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INC_GPR8` — `INC`
- `INC_GPR8i8_APX` — `INC`
- `INC_GPR8i8_APX_N3` — `INC`
- `INC_GPR8i8_GPR8i8_APX_N3` — `INC`
- `INC_GPR8i8_MEMi8_APX_N3` — `INC`
- `INC_GPRv_40` — `INC`
- `INC_GPRv_APX` — `INC`
- `INC_GPRv_APX_N3` — `INC`
- `INC_GPRv_FFr0` — `INC`
- `INC_GPRv_GPRv_APX_N3` — `INC`
- `INC_GPRv_MEMv_APX_N3` — `INC`
- `INC_MEMb` — `INC`
- … 5 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INC_LOCK

`INC_LOCK` increments its destination by one while preserving carry; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INC_LOCK_MEMb` — `INC_LOCK`
- `INC_LOCK_MEMv` — `INC_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INT

`INT` invokes an interrupt or exception handler through an interrupt vector encoded in the instruction, saving control state according to the current mode. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `INTERRUPT`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `IMM`. Representative implicit state: `rIP`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INT_IMMb` — `INT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INT1

`INT1` raises the debug exception through the one-byte ICEBP encoding, historically used by debuggers and in-system emulators. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `INTERRUPT`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `rIP`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INT1` — `INT1`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INT3

`INT3` raises the breakpoint exception using the dedicated one-byte breakpoint encoding. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `INTERRUPT`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `rIP`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INT3` — `INT3`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INTO

`INTO` raises the overflow exception when the overflow flag is set; this legacy instruction is not available in 64-bit mode. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `INTERRUPT`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EIP`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INTO` — `INTO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LAHF

`LAHF` copies selected arithmetic status flags into AH, providing a compact way to materialize condition-code state in a general-purpose register. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `FLAGOP`
- ISA set(s): `LAHF`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `AH`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LAHF` — `LAHF`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LDS

`LDS` loads an offset and an accompanying selector from memory, placing the selector in DS and the offset in a general-purpose register. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SEGOP`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRz MEM`. Representative implicit state: `DS`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LDS_GPRz_MEMp` — `LDS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LEA

`LEA` computes the arithmetic address expression encoded by a memory-style operand and writes that numerical address to a general-purpose register without reading memory. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `MISC`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv AGEN`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LEA_GPRv_AGEN` — `LEA`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this belongs to the small x86-64 user-mode baseline worth supporting early. Flag liveness, register constraints, and exact encoding choice should be explicit.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LES

`LES` loads an offset and an accompanying selector from memory, placing the selector in ES and the offset in a general-purpose register. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SEGOP`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRz MEM`. Representative implicit state: `ES`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LES_GPRz_MEMp` — `LES`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LFS

`LFS` loads an offset and an accompanying selector from memory, placing the selector in FS and the offset in a general-purpose register. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SEGOP`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv MEM`. Representative implicit state: `FS`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LFS_GPRv_MEMp2` — `LFS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LGS

`LGS` loads an offset and an accompanying selector from memory, placing the selector in GS and the offset in a general-purpose register. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SEGOP`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv MEM`. Representative implicit state: `GS`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LGS_GPRv_MEMp2` — `LGS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LSS

`LSS` loads an offset and an accompanying selector from memory, placing the selector in SS and the offset in a general-purpose register with the instruction's stack-segment ordering semantics. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SEGOP`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv MEM`. Representative implicit state: `SS`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LSS_GPRv_MEMp2` — `LSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MCOMMIT

`MCOMMIT` orders AMD persistent-memory writes so prior stores covered by the instruction's persistence rules are committed toward the persistence domain before later dependent software proceeds. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MCOMMIT`
- XED category/categories: `MISC`
- ISA set(s): `MCOMMIT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MCOMMIT` — `MCOMMIT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MOV

`MOV` copies a value from source to destination without arithmetic. The pinned XED inventory represents it with 22 normalized encoding records and 22 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DATAXFER`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPR8 MEM`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MOV_AL_MEMb` — `MOV`
- `MOV_GPR8_GPR8_88` — `MOV`
- `MOV_GPR8_GPR8_8A` — `MOV`
- `MOV_GPR8_IMMb_B0` — `MOV`
- `MOV_GPR8_IMMb_C6r0` — `MOV`
- `MOV_GPR8_MEMb` — `MOV`
- `MOV_GPRv_GPRv_89` — `MOV`
- `MOV_GPRv_GPRv_8B` — `MOV`
- `MOV_GPRv_IMMv` — `MOV`
- `MOV_GPRv_IMMz` — `MOV`
- `MOV_GPRv_MEMv` — `MOV`
- `MOV_GPRv_SEG` — `MOV`
- … 10 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this belongs to the small x86-64 user-mode baseline worth supporting early. Flag liveness, register constraints, and exact encoding choice should be explicit.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MOVBE

`MOVBE` loads or stores an integer while reversing byte order. The pinned XED inventory represents it with 10 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MOVBE`
- XED category/categories: `DATAXFER`
- ISA set(s): `APX_F_MOVBE`, `MOVBE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv MEM`; `MEM GPRv`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MOVBE_GPRv_GPRv_APX` — `MOVBE`
- `MOVBE_GPRv_MEMv` — `MOVBE`
- `MOVBE_GPRv_MEMv_APX` — `MOVBE`
- `MOVBE_MEMv_GPRv` — `MOVBE`
- `MOVBE_MEMv_GPRv_APX` — `MOVBE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MOVDIR64B

`MOVDIR64B` performs a 64-byte direct store using the architecture's direct-write semantics. The pinned XED inventory represents it with 3 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MOVDIR`
- XED category/categories: `MOVDIR`
- ISA set(s): `APX_F_MOVDIR64B`, `MOVDIR64B`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `A_GPR MEM`. Representative implicit state: `MEM A_GPR`; `MEM A_GPR ES`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MOVDIR64B_GPRa_MEM` — `MOVDIR64B`
- `MOVDIR64B_GPRav_MEMu32_APX` — `MOVDIR64B`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MOVDIRI

`MOVDIRI` performs a direct store from a general-purpose register to memory. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MOVDIR`
- XED category/categories: `MOVDIR`
- ISA set(s): `APX_F_MOVDIRI`, `MOVDIRI`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR32`; `MEM GPR64`; `MEM GPRy`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MOVDIRI_MEMu32_GPR32u32` — `MOVDIRI`
- `MOVDIRI_MEMu64_GPR64u64` — `MOVDIRI`
- `MOVDIRI_MEMyu_GPRyu_APX` — `MOVDIRI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MOVRS

`MOVRS` loads data with the MOVRS read-shared semantic hint, allowing coherent shared-data reads to avoid unnecessarily requesting exclusive ownership. The pinned XED inventory represents it with 5 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MOVRS`
- XED category/categories: `APX`, `LEGACY`
- ISA set(s): `APX_F_MOVRS`, `MOVRS`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 MEM`; `GPRv MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MOVRS_GPR8i8_MEMi8` — `MOVRS`
- `MOVRS_GPR8i8_MEMi8_APX` — `MOVRS`
- `MOVRS_GPRv_MEMv` — `MOVRS`
- `MOVRS_GPRv_MEMv_APX` — `MOVRS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MOVZX

`MOVZX` copies a smaller integer and zero-extends it. The pinned XED inventory represents it with 7 normalized encoding records and 7 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DATAXFER`
- ISA set(s): `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR16 MEM`; `GPR32 MEM`; `GPR64 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MOVZX_GPR16_MEMw` — `MOVZX`
- `MOVZX_GPR32_MEMw` — `MOVZX`
- `MOVZX_GPR64_MEMw` — `MOVZX`
- `MOVZX_GPRv_GPR16` — `MOVZX`
- `MOVZX_GPRv_GPR8` — `MOVZX`
- `MOVZX_GPRv_MEMb` — `MOVZX`
- `MOVZX_GPRv_MEMw` — `MOVZX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MOV_CR

`MOV_CR` moves a value between a general-purpose register and a control register, exposing privileged processor control state. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DATAXFER`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `CR GPR32`; `CR GPR64`; `GPR32 CR`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MOV_CR_CR_GPR32` — `MOV_CR`
- `MOV_CR_CR_GPR64` — `MOV_CR`
- `MOV_CR_GPR32_CR` — `MOV_CR`
- `MOV_CR_GPR64_CR` — `MOV_CR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MOV_DR

`MOV_DR` moves a value between a general-purpose register and a debug register. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DATAXFER`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `DR GPR32`; `DR GPR64`; `GPR32 DR`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MOV_DR_DR_GPR32` — `MOV_DR`
- `MOV_DR_DR_GPR64` — `MOV_DR`
- `MOV_DR_GPR32_DR` — `MOV_DR`
- `MOV_DR_GPR64_DR` — `MOV_DR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MUL

`MUL` performs unsigned widening multiplication using the accumulator implicitly. The pinned XED inventory represents it with 16 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPRv`; `MEM`. Representative implicit state: `AL AX`; `OrAX OrDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MUL_GPR8` — `MUL`
- `MUL_GPR8i8_APX` — `MUL`
- `MUL_GPR8i8_APX_N3` — `MUL`
- `MUL_GPRv` — `MUL`
- `MUL_GPRv_APX` — `MUL`
- `MUL_GPRv_APX_N3` — `MUL`
- `MUL_MEMb` — `MUL`
- `MUL_MEMi8_APX` — `MUL`
- `MUL_MEMi8_APX_N3` — `MUL`
- `MUL_MEMv` — `MUL`
- `MUL_MEMv_APX` — `MUL`
- `MUL_MEMv_APX_N3` — `MUL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## NEG

`NEG` forms the two's-complement negation of its operand. The pinned XED inventory represents it with 28 normalized encoding records and 16 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPR8 GPR8`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `NEG_GPR8` — `NEG`
- `NEG_GPR8i8_APX` — `NEG`
- `NEG_GPR8i8_APX_N3` — `NEG`
- `NEG_GPR8i8_GPR8i8_APX_N3` — `NEG`
- `NEG_GPR8i8_MEMi8_APX_N3` — `NEG`
- `NEG_GPRv` — `NEG`
- `NEG_GPRv_APX` — `NEG`
- `NEG_GPRv_APX_N3` — `NEG`
- `NEG_GPRv_GPRv_APX_N3` — `NEG`
- `NEG_GPRv_MEMv_APX_N3` — `NEG`
- `NEG_MEMb` — `NEG`
- `NEG_MEMi8_APX` — `NEG`
- … 4 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## NEG_LOCK

`NEG_LOCK` forms the two's-complement negation of its operand; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `NEG_LOCK_MEMb` — `NEG_LOCK`
- `NEG_LOCK_MEMv` — `NEG_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## NOP

`NOP` performs no architectural data computation while consuming an instruction slot; multi-byte encodings are commonly used for alignment and patchable padding. The pinned XED inventory represents it with 58 normalized encoding records and 28 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `NOP`, `WIDENOP`
- ISA set(s): `FAT_NOP`, `I86`, `PPRO`, `PREFETCH_NOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv`; `GPRv GPRv`; `GPRv MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `NOP_90` — `NOP`
- `NOP_GPRv_0F18r0` — `NOP`
- `NOP_GPRv_0F18r1` — `NOP`
- `NOP_GPRv_0F18r2` — `NOP`
- `NOP_GPRv_0F18r3` — `NOP`
- `NOP_GPRv_0F18r4` — `NOP`
- `NOP_GPRv_0F18r5` — `NOP`
- `NOP_GPRv_0F18r6` — `NOP`
- `NOP_GPRv_0F18r7` — `NOP`
- `NOP_GPRv_0F1F` — `NOP`
- `NOP_GPRv_GPRv_0F0D` — `NOP`
- `NOP_GPRv_GPRv_0F19` — `NOP`
- … 16 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## NOT

`NOT` inverts every destination bit without changing arithmetic flags. The pinned XED inventory represents it with 16 normalized encoding records and 12 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `LOGICAL`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPR8 GPR8`; `GPR8 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `NOT_GPR8` — `NOT`
- `NOT_GPR8i8_APX` — `NOT`
- `NOT_GPR8i8_GPR8i8_APX_N3` — `NOT`
- `NOT_GPR8i8_MEMi8_APX_N3` — `NOT`
- `NOT_GPRv` — `NOT`
- `NOT_GPRv_APX` — `NOT`
- `NOT_GPRv_GPRv_APX_N3` — `NOT`
- `NOT_GPRv_MEMv_APX_N3` — `NOT`
- `NOT_MEMb` — `NOT`
- `NOT_MEMi8_APX` — `NOT`
- `NOT_MEMv` — `NOT`
- `NOT_MEMv_APX` — `NOT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## NOT_LOCK

`NOT_LOCK` inverts every destination bit without changing arithmetic flags; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `LOGICAL`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `NOT_LOCK_MEMb` — `NOT_LOCK`
- `NOT_LOCK_MEMv` — `NOT_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## OR

`OR` computes bitwise inclusive OR. The pinned XED inventory represents it with 106 normalized encoding records and 54 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `LOGICAL`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `OR_AL_IMMb` — `OR`
- `OR_GPR8_GPR8_08` — `OR`
- `OR_GPR8_GPR8_0A` — `OR`
- `OR_GPR8_IMMb_80r1` — `OR`
- `OR_GPR8_IMMb_82r1` — `OR`
- `OR_GPR8_MEMb` — `OR`
- `OR_GPR8i8_GPR8i8_APX` — `OR`
- `OR_GPR8i8_GPR8i8_APX_N3` — `OR`
- `OR_GPR8i8_GPR8i8_GPR8i8_APX_N3` — `OR`
- `OR_GPR8i8_GPR8i8_IMM8_APX_N3` — `OR`
- `OR_GPR8i8_GPR8i8_MEMi8_APX_N3` — `OR`
- `OR_GPR8i8_IMM8_APX` — `OR`
- … 42 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## OR_LOCK

`OR_LOCK` computes bitwise inclusive OR; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `LOGICAL`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR8`; `MEM GPRv`; `MEM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `OR_LOCK_MEMb_GPR8` — `OR_LOCK`
- `OR_LOCK_MEMb_IMMb_80r1` — `OR_LOCK`
- `OR_LOCK_MEMb_IMMb_82r1` — `OR_LOCK`
- `OR_LOCK_MEMv_GPRv` — `OR_LOCK`
- `OR_LOCK_MEMv_IMMb` — `OR_LOCK`
- `OR_LOCK_MEMv_IMMz` — `OR_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## OUT

`OUT` writes the accumulator to an I/O port using x86's separate port-I/O address space. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `IO`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `IMM`. Representative implicit state: `AL`; `DX AL`; `DX OeAX`; ….

Recorded flag behavior: not uniformly recorded.

### Important forms

- `OUT_DX_AL` — `OUT`
- `OUT_DX_OeAX` — `OUT`
- `OUT_IMMb_AL` — `OUT`
- `OUT_IMMb_OeAX` — `OUT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PAUSE

`PAUSE` provides a processor hint inside spin-wait loops so the core can treat repeated polling more efficiently than an ordinary empty loop. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `PAUSE`
- XED category/categories: `MISC`
- ISA set(s): `PAUSE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PAUSE` — `PAUSE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PBNDKB

`PBNDKB` binds a platform key to a binary large object using the platform's key-binding mechanism and returns the architecture-defined result state. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `PBNDKB`
- XED category/categories: `PBNDKB`
- ISA set(s): `PBNDKB`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RAX RBX RCX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PBNDKB` — `PBNDKB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PREFETCHRST2

`PREFETCHRST2` issues a prefetch hint for the addressed cache line with the locality or exclusivity preference encoded by the mnemonic. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MOVRS`
- XED category/categories: `PREFETCH`
- ISA set(s): `MOVRS`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PREFETCHRST2_MEMu8` — `PREFETCHRST2`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PREFETCHWT1

`PREFETCHWT1` hints that a memory line will soon be written while expressing a weaker temporal-locality preference. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `PREFETCHWT1`
- XED category/categories: `PREFETCHWT1`
- ISA set(s): `PREFETCHWT1`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PREFETCHWT1_MEMu8` — `PREFETCHWT1`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PTWRITE

`PTWRITE` writes a software-supplied payload into Intel Processor Trace when PTWRITE tracing is enabled, allowing software events to appear in the trace stream. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `PTWRITE`
- XED category/categories: `PTWRITE`
- ISA set(s): `PTWRITE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRy`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PTWRITE_GPRy` — `PTWRITE`
- `PTWRITE_MEMy` — `PTWRITE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RCL

`RCL` rotates destination bits, optionally through carry, by the requested count. The pinned XED inventory represents it with 48 normalized encoding records and 36 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `ROTATE`
- ISA set(s): `APX_F`, `APX_F_N3`, `I186`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `CL`; `IMM`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RCL_GPR8_CL` — `RCL`
- `RCL_GPR8_IMMb` — `RCL`
- `RCL_GPR8_ONE` — `RCL`
- `RCL_GPR8i8_CL_APX` — `RCL`
- `RCL_GPR8i8_GPR8i8_CL_APX_N3` — `RCL`
- `RCL_GPR8i8_GPR8i8_IMM8_APX_N3` — `RCL`
- `RCL_GPR8i8_GPR8i8_ONE_APX_N3` — `RCL`
- `RCL_GPR8i8_IMM8_APX` — `RCL`
- `RCL_GPR8i8_MEMi8_CL_APX_N3` — `RCL`
- `RCL_GPR8i8_MEMi8_IMM8_APX_N3` — `RCL`
- `RCL_GPR8i8_MEMi8_ONE_APX_N3` — `RCL`
- `RCL_GPR8i8_ONE_APX` — `RCL`
- … 24 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RCR

`RCR` rotates destination bits, optionally through carry, by the requested count. The pinned XED inventory represents it with 48 normalized encoding records and 36 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `ROTATE`
- ISA set(s): `APX_F`, `APX_F_N3`, `I186`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `CL`; `IMM`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RCR_GPR8_CL` — `RCR`
- `RCR_GPR8_IMMb` — `RCR`
- `RCR_GPR8_ONE` — `RCR`
- `RCR_GPR8i8_CL_APX` — `RCR`
- `RCR_GPR8i8_GPR8i8_CL_APX_N3` — `RCR`
- `RCR_GPR8i8_GPR8i8_IMM8_APX_N3` — `RCR`
- `RCR_GPR8i8_GPR8i8_ONE_APX_N3` — `RCR`
- `RCR_GPR8i8_IMM8_APX` — `RCR`
- `RCR_GPR8i8_MEMi8_CL_APX_N3` — `RCR`
- `RCR_GPR8i8_MEMi8_IMM8_APX_N3` — `RCR`
- `RCR_GPR8i8_MEMi8_ONE_APX_N3` — `RCR`
- `RCR_GPR8i8_ONE_APX` — `RCR`
- … 24 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDFSBASE

`RDFSBASE` reads the current FS segment base address into a general-purpose register when FSGSBASE is enabled. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RDWRFSGS`
- XED category/categories: `RDWRFSGS`
- ISA set(s): `RDWRFSGS`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRy`. Representative implicit state: `FSBASE`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDFSBASE_GPRy` — `RDFSBASE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDGSBASE

`RDGSBASE` reads the current GS segment base address into a general-purpose register when FSGSBASE is enabled. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RDWRFSGS`
- XED category/categories: `RDWRFSGS`
- ISA set(s): `RDWRFSGS`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRy`. Representative implicit state: `GSBASE`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDGSBASE_GPRy` — `RDGSBASE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDPID

`RDPID` reads the processor identifier stored in IA32_TSC_AUX into a general-purpose register without reading the timestamp counter. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RDPID`
- XED category/categories: `RDPID`
- ISA set(s): `RDPID`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32`; `GPR64`. Representative implicit state: `TSCAUX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDPID_GPR32u32` — `RDPID`
- `RDPID_GPR64u64` — `RDPID`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDPRU

`RDPRU` reads an AMD processor register selected by ECX into EDX:EAX when the selected register is permitted to software at the current privilege level. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RDPRU`
- XED category/categories: `RDPRU`
- ISA set(s): `RDPRU`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EDX EAX ECX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDPRU` — `RDPRU`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ROL

`ROL` rotates destination bits, optionally through carry, by the requested count. The pinned XED inventory represents it with 84 normalized encoding records and 48 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `ROTATE`
- ISA set(s): `APX_F`, `APX_F_N3`, `I186`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `CL`; `IMM`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ROL_GPR8_CL` — `ROL`
- `ROL_GPR8_IMMb` — `ROL`
- `ROL_GPR8_ONE` — `ROL`
- `ROL_GPR8i8_CL_APX` — `ROL`
- `ROL_GPR8i8_CL_APX_N3` — `ROL`
- `ROL_GPR8i8_GPR8i8_CL_APX_N3` — `ROL`
- `ROL_GPR8i8_GPR8i8_IMM8_APX_N3` — `ROL`
- `ROL_GPR8i8_GPR8i8_ONE_APX_N3` — `ROL`
- `ROL_GPR8i8_IMM8_APX` — `ROL`
- `ROL_GPR8i8_IMM8_APX_N3` — `ROL`
- `ROL_GPR8i8_MEMi8_CL_APX_N3` — `ROL`
- `ROL_GPR8i8_MEMi8_IMM8_APX_N3` — `ROL`
- … 36 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## ROR

`ROR` rotates destination bits, optionally through carry, by the requested count. The pinned XED inventory represents it with 84 normalized encoding records and 48 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `ROTATE`
- ISA set(s): `APX_F`, `APX_F_N3`, `I186`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `CL`; `IMM`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ROR_GPR8_CL` — `ROR`
- `ROR_GPR8_IMMb` — `ROR`
- `ROR_GPR8_ONE` — `ROR`
- `ROR_GPR8i8_CL_APX` — `ROR`
- `ROR_GPR8i8_CL_APX_N3` — `ROR`
- `ROR_GPR8i8_GPR8i8_CL_APX_N3` — `ROR`
- `ROR_GPR8i8_GPR8i8_IMM8_APX_N3` — `ROR`
- `ROR_GPR8i8_GPR8i8_ONE_APX_N3` — `ROR`
- `ROR_GPR8i8_IMM8_APX` — `ROR`
- `ROR_GPR8i8_IMM8_APX_N3` — `ROR`
- `ROR_GPR8i8_MEMi8_CL_APX_N3` — `ROR`
- `ROR_GPR8i8_MEMi8_IMM8_APX_N3` — `ROR`
- … 36 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SAHF

`SAHF` copies selected bits of AH into arithmetic status flags, restoring a subset of condition-code state. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `FLAGOP`
- ISA set(s): `LAHF`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `AH`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SAHF` — `SAHF`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SALC

`SALC` sets AL to all ones when carry is set and to zero when carry is clear; it is a historical undocumented instruction on processors that implement it. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `FLAGOP`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `AL`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SALC` — `SALC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SAR

`SAR` shifts the destination arithmetically right, replicating the sign bit. The pinned XED inventory represents it with 84 normalized encoding records and 48 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SHIFT`
- ISA set(s): `APX_F`, `APX_F_N3`, `I186`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `CL`; `IMM`.

Recorded flag behavior: not uniformly recorded.

### Important forms

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

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SBB

`SBB` subtracts the source and incoming borrow from the destination. The pinned XED inventory represents it with 62 normalized encoding records and 42 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SBB_AL_IMMb` — `SBB`
- `SBB_GPR8_GPR8_18` — `SBB`
- `SBB_GPR8_GPR8_1A` — `SBB`
- `SBB_GPR8_IMMb_80r3` — `SBB`
- `SBB_GPR8_IMMb_82r3` — `SBB`
- `SBB_GPR8_MEMb` — `SBB`
- `SBB_GPR8i8_GPR8i8_APX` — `SBB`
- `SBB_GPR8i8_GPR8i8_GPR8i8_APX_N3` — `SBB`
- `SBB_GPR8i8_GPR8i8_IMM8_APX_N3` — `SBB`
- `SBB_GPR8i8_GPR8i8_MEMi8_APX_N3` — `SBB`
- `SBB_GPR8i8_IMM8_APX` — `SBB`
- `SBB_GPR8i8_MEMi8_APX` — `SBB`
- … 30 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SBB_LOCK

`SBB_LOCK` subtracts the source and incoming borrow from the destination; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR8`; `MEM GPRv`; `MEM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SBB_LOCK_MEMb_GPR8` — `SBB_LOCK`
- `SBB_LOCK_MEMb_IMMb_80r3` — `SBB_LOCK`
- `SBB_LOCK_MEMb_IMMb_82r3` — `SBB_LOCK`
- `SBB_LOCK_MEMv_GPRv` — `SBB_LOCK`
- `SBB_LOCK_MEMv_IMMb` — `SBB_LOCK`
- `SBB_LOCK_MEMv_IMMz` — `SBB_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SERIALIZE

`SERIALIZE` acts as a fully serializing instruction for instruction execution, forcing prior architectural effects to complete before later instructions execute. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SERIALIZE`
- XED category/categories: `SERIALIZE`
- ISA set(s): `SERIALIZE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SERIALIZE` — `SERIALIZE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETB

`SETB` writes a one-byte Boolean value that is 1 when the condition-code state denotes below (carry set); otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETB_GPR8` — `SETB`
- `SETB_GPR8i8_APX_N3` — `SETB`
- `SETB_GPR8i8_APX_N3_ZU` — `SETB`
- `SETB_MEMb` — `SETB`
- `SETB_MEMi8_APX_N3` — `SETB`
- `SETB_MEMi8_APX_N3_ZU` — `SETB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETBE

`SETBE` writes a one-byte Boolean value that is 1 when the condition-code state denotes below or equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETBE_GPR8` — `SETBE`
- `SETBE_GPR8i8_APX_N3` — `SETBE`
- `SETBE_GPR8i8_APX_N3_ZU` — `SETBE`
- `SETBE_MEMb` — `SETBE`
- `SETBE_MEMi8_APX_N3` — `SETBE`
- `SETBE_MEMi8_APX_N3_ZU` — `SETBE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETL

`SETL` writes a one-byte Boolean value that is 1 when the condition-code state denotes less in signed comparison; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETL_GPR8` — `SETL`
- `SETL_GPR8i8_APX_N3` — `SETL`
- `SETL_GPR8i8_APX_N3_ZU` — `SETL`
- `SETL_MEMb` — `SETL`
- `SETL_MEMi8_APX_N3` — `SETL`
- `SETL_MEMi8_APX_N3_ZU` — `SETL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETLE

`SETLE` writes a one-byte Boolean value that is 1 when the condition-code state denotes less or equal in signed comparison; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETLE_GPR8` — `SETLE`
- `SETLE_GPR8i8_APX_N3` — `SETLE`
- `SETLE_GPR8i8_APX_N3_ZU` — `SETLE`
- `SETLE_MEMb` — `SETLE`
- `SETLE_MEMi8_APX_N3` — `SETLE`
- `SETLE_MEMi8_APX_N3_ZU` — `SETLE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETNB

`SETNB` writes a one-byte Boolean value that is 1 when the condition-code state denotes not below / unsigned above-or-equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETNB_GPR8` — `SETNB`
- `SETNB_GPR8i8_APX_N3` — `SETNB`
- `SETNB_GPR8i8_APX_N3_ZU` — `SETNB`
- `SETNB_MEMb` — `SETNB`
- `SETNB_MEMi8_APX_N3` — `SETNB`
- `SETNB_MEMi8_APX_N3_ZU` — `SETNB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETNBE

`SETNBE` writes a one-byte Boolean value that is 1 when the condition-code state denotes unsigned above; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETNBE_GPR8` — `SETNBE`
- `SETNBE_GPR8i8_APX_N3` — `SETNBE`
- `SETNBE_GPR8i8_APX_N3_ZU` — `SETNBE`
- `SETNBE_MEMb` — `SETNBE`
- `SETNBE_MEMi8_APX_N3` — `SETNBE`
- `SETNBE_MEMi8_APX_N3_ZU` — `SETNBE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETNL

`SETNL` writes a one-byte Boolean value that is 1 when the condition-code state denotes signed greater-or-equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETNL_GPR8` — `SETNL`
- `SETNL_GPR8i8_APX_N3` — `SETNL`
- `SETNL_GPR8i8_APX_N3_ZU` — `SETNL`
- `SETNL_MEMb` — `SETNL`
- `SETNL_MEMi8_APX_N3` — `SETNL`
- `SETNL_MEMi8_APX_N3_ZU` — `SETNL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETNLE

`SETNLE` writes a one-byte Boolean value that is 1 when the condition-code state denotes signed greater; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETNLE_GPR8` — `SETNLE`
- `SETNLE_GPR8i8_APX_N3` — `SETNLE`
- `SETNLE_GPR8i8_APX_N3_ZU` — `SETNLE`
- `SETNLE_MEMb` — `SETNLE`
- `SETNLE_MEMi8_APX_N3` — `SETNLE`
- `SETNLE_MEMi8_APX_N3_ZU` — `SETNLE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETNO

`SETNO` writes a one-byte Boolean value that is 1 when the condition-code state denotes no signed overflow; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETNO_GPR8` — `SETNO`
- `SETNO_GPR8i8_APX_N3` — `SETNO`
- `SETNO_GPR8i8_APX_N3_ZU` — `SETNO`
- `SETNO_MEMb` — `SETNO`
- `SETNO_MEMi8_APX_N3` — `SETNO`
- `SETNO_MEMi8_APX_N3_ZU` — `SETNO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETNP

`SETNP` writes a one-byte Boolean value that is 1 when the condition-code state denotes not parity; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETNP_GPR8` — `SETNP`
- `SETNP_GPR8i8_APX_N3` — `SETNP`
- `SETNP_GPR8i8_APX_N3_ZU` — `SETNP`
- `SETNP_MEMb` — `SETNP`
- `SETNP_MEMi8_APX_N3` — `SETNP`
- `SETNP_MEMi8_APX_N3_ZU` — `SETNP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETNS

`SETNS` writes a one-byte Boolean value that is 1 when the condition-code state denotes non-negative; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETNS_GPR8` — `SETNS`
- `SETNS_GPR8i8_APX_N3` — `SETNS`
- `SETNS_GPR8i8_APX_N3_ZU` — `SETNS`
- `SETNS_MEMb` — `SETNS`
- `SETNS_MEMi8_APX_N3` — `SETNS`
- `SETNS_MEMi8_APX_N3_ZU` — `SETNS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETNZ

`SETNZ` writes a one-byte Boolean value that is 1 when the condition-code state denotes nonzero; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETNZ_GPR8` — `SETNZ`
- `SETNZ_GPR8i8_APX_N3` — `SETNZ`
- `SETNZ_GPR8i8_APX_N3_ZU` — `SETNZ`
- `SETNZ_MEMb` — `SETNZ`
- `SETNZ_MEMi8_APX_N3` — `SETNZ`
- `SETNZ_MEMi8_APX_N3_ZU` — `SETNZ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETO

`SETO` writes a one-byte Boolean value that is 1 when the condition-code state denotes signed overflow; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETO_GPR8` — `SETO`
- `SETO_GPR8i8_APX_N3` — `SETO`
- `SETO_GPR8i8_APX_N3_ZU` — `SETO`
- `SETO_MEMb` — `SETO`
- `SETO_MEMi8_APX_N3` — `SETO`
- `SETO_MEMi8_APX_N3_ZU` — `SETO`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETP

`SETP` writes a one-byte Boolean value that is 1 when the condition-code state denotes parity; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETP_GPR8` — `SETP`
- `SETP_GPR8i8_APX_N3` — `SETP`
- `SETP_GPR8i8_APX_N3_ZU` — `SETP`
- `SETP_MEMb` — `SETP`
- `SETP_MEMi8_APX_N3` — `SETP`
- `SETP_MEMi8_APX_N3_ZU` — `SETP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETS

`SETS` writes a one-byte Boolean value that is 1 when the condition-code state denotes negative; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETS_GPR8` — `SETS`
- `SETS_GPR8i8_APX_N3` — `SETS`
- `SETS_GPR8i8_APX_N3_ZU` — `SETS`
- `SETS_MEMb` — `SETS`
- `SETS_MEMi8_APX_N3` — `SETS`
- `SETS_MEMi8_APX_N3_ZU` — `SETS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SETZ

`SETZ` writes a one-byte Boolean value that is 1 when the condition-code state denotes zero / equal; otherwise it follows the instruction family's defined non-taken behavior. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SETCC`
- ISA set(s): `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SETZ_GPR8` — `SETZ`
- `SETZ_GPR8i8_APX_N3` — `SETZ`
- `SETZ_GPR8i8_APX_N3_ZU` — `SETZ`
- `SETZ_MEMb` — `SETZ`
- `SETZ_MEMi8_APX_N3` — `SETZ`
- `SETZ_MEMi8_APX_N3_ZU` — `SETZ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHL

`SHL` shifts the destination left, filling low bits with zero and updating shift-related flags. The pinned XED inventory represents it with 168 normalized encoding records and 60 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SHIFT`
- ISA set(s): `APX_F`, `APX_F_N3`, `I186`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `CL`; `IMM`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHL_GPR8_CL_D2r4` — `SHL`
- `SHL_GPR8_CL_D2r6` — `SHL`
- `SHL_GPR8_IMMb_C0r4` — `SHL`
- `SHL_GPR8_IMMb_C0r6` — `SHL`
- `SHL_GPR8_ONE_D0r4` — `SHL`
- `SHL_GPR8_ONE_D0r6` — `SHL`
- `SHL_GPR8i8_CL_APX` — `SHL`
- `SHL_GPR8i8_CL_APX_N3` — `SHL`
- `SHL_GPR8i8_GPR8i8_CL_APX_N3` — `SHL`
- `SHL_GPR8i8_GPR8i8_IMM8_APX_N3` — `SHL`
- `SHL_GPR8i8_GPR8i8_ONE_APX_N3` — `SHL`
- `SHL_GPR8i8_IMM8_APX` — `SHL`
- … 48 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHLD

`SHLD` performs a double-width logical shift, pulling replacement bits from a second source. The pinned XED inventory represents it with 36 normalized encoding records and 16 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SHIFT`
- ISA set(s): `APX_F`, `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv GPRv IMM`; …. Representative implicit state: `CL`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHLD_GPRv_GPRv_CL` — `SHLD`
- `SHLD_GPRv_GPRv_CL_APX` — `SHLD`
- `SHLD_GPRv_GPRv_CL_APX_N3` — `SHLD`
- `SHLD_GPRv_GPRv_GPRv_CL_APX_N3` — `SHLD`
- `SHLD_GPRv_GPRv_GPRv_IMM8_APX_N3` — `SHLD`
- `SHLD_GPRv_GPRv_IMM8_APX` — `SHLD`
- `SHLD_GPRv_GPRv_IMM8_APX_N3` — `SHLD`
- `SHLD_GPRv_GPRv_IMMb` — `SHLD`
- `SHLD_GPRv_MEMv_GPRv_CL_APX_N3` — `SHLD`
- `SHLD_GPRv_MEMv_GPRv_IMM8_APX_N3` — `SHLD`
- `SHLD_MEMv_GPRv_CL` — `SHLD`
- `SHLD_MEMv_GPRv_CL_APX` — `SHLD`
- … 4 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHR

`SHR` shifts the destination logically right, filling high bits with zero. The pinned XED inventory represents it with 84 normalized encoding records and 48 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SHIFT`
- ISA set(s): `APX_F`, `APX_F_N3`, `I186`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8`; `GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `CL`; `IMM`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHR_GPR8_CL` — `SHR`
- `SHR_GPR8_IMMb` — `SHR`
- `SHR_GPR8_ONE` — `SHR`
- `SHR_GPR8i8_CL_APX` — `SHR`
- `SHR_GPR8i8_CL_APX_N3` — `SHR`
- `SHR_GPR8i8_GPR8i8_CL_APX_N3` — `SHR`
- `SHR_GPR8i8_GPR8i8_IMM8_APX_N3` — `SHR`
- `SHR_GPR8i8_GPR8i8_ONE_APX_N3` — `SHR`
- `SHR_GPR8i8_IMM8_APX` — `SHR`
- `SHR_GPR8i8_IMM8_APX_N3` — `SHR`
- `SHR_GPR8i8_MEMi8_CL_APX_N3` — `SHR`
- `SHR_GPR8i8_MEMi8_IMM8_APX_N3` — `SHR`
- … 36 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SHRD

`SHRD` performs a double-width logical shift, pulling replacement bits from a second source. The pinned XED inventory represents it with 36 normalized encoding records and 16 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `SHIFT`
- ISA set(s): `APX_F`, `APX_F_N3`, `I386`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv GPRv GPRv`; `GPRv GPRv GPRv IMM`; …. Representative implicit state: `CL`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SHRD_GPRv_GPRv_CL` — `SHRD`
- `SHRD_GPRv_GPRv_CL_APX` — `SHRD`
- `SHRD_GPRv_GPRv_CL_APX_N3` — `SHRD`
- `SHRD_GPRv_GPRv_GPRv_CL_APX_N3` — `SHRD`
- `SHRD_GPRv_GPRv_GPRv_IMM8_APX_N3` — `SHRD`
- `SHRD_GPRv_GPRv_IMM8_APX` — `SHRD`
- `SHRD_GPRv_GPRv_IMM8_APX_N3` — `SHRD`
- `SHRD_GPRv_GPRv_IMMb` — `SHRD`
- `SHRD_GPRv_MEMv_GPRv_CL_APX_N3` — `SHRD`
- `SHRD_GPRv_MEMv_GPRv_IMM8_APX_N3` — `SHRD`
- `SHRD_MEMv_GPRv_CL` — `SHRD`
- `SHRD_MEMv_GPRv_CL_APX` — `SHRD`
- … 4 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## STAC

`STAC` sets the SMAP access-control flag so supervisor code can temporarily access user pages. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SMAP`
- XED category/categories: `SMAP`
- ISA set(s): `SMAP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `STAC` — `STAC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## STC

`STC` sets the carry flag. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `FLAGOP`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `STC` — `STC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## STD

`STD` sets the direction flag so string instructions decrement their implicit index registers. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `FLAGOP`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `STD` — `STD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SUB

`SUB` subtracts the source from the destination and writes the difference while updating arithmetic flags. The pinned XED inventory represents it with 106 normalized encoding records and 54 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SUB_AL_IMMb` — `SUB`
- `SUB_GPR8_GPR8_28` — `SUB`
- `SUB_GPR8_GPR8_2A` — `SUB`
- `SUB_GPR8_IMMb_80r5` — `SUB`
- `SUB_GPR8_IMMb_82r5` — `SUB`
- `SUB_GPR8_MEMb` — `SUB`
- `SUB_GPR8i8_GPR8i8_APX` — `SUB`
- `SUB_GPR8i8_GPR8i8_APX_N3` — `SUB`
- `SUB_GPR8i8_GPR8i8_GPR8i8_APX_N3` — `SUB`
- `SUB_GPR8i8_GPR8i8_IMM8_APX_N3` — `SUB`
- `SUB_GPR8i8_GPR8i8_MEMi8_APX_N3` — `SUB`
- `SUB_GPR8i8_IMM8_APX` — `SUB`
- … 42 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SUB_LOCK

`SUB_LOCK` subtracts the source from the destination and writes the difference while updating arithmetic flags; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `BINARY`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR8`; `MEM GPRv`; `MEM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SUB_LOCK_MEMb_GPR8` — `SUB_LOCK`
- `SUB_LOCK_MEMb_IMMb_80r5` — `SUB_LOCK`
- `SUB_LOCK_MEMb_IMMb_82r5` — `SUB_LOCK`
- `SUB_LOCK_MEMv_GPRv` — `SUB_LOCK`
- `SUB_LOCK_MEMv_IMMb` — `SUB_LOCK`
- `SUB_LOCK_MEMv_IMMz` — `SUB_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## TEST

`TEST` computes a bitwise AND only to set logical flags and discards the result. The pinned XED inventory represents it with 14 normalized encoding records and 14 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `LOGICAL`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 IMM`; `GPRv GPRv`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

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

### Backend notes

For Idriç this belongs to the small x86-64 user-mode baseline worth supporting early. Flag liveness, register constraints, and exact encoding choice should be explicit.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## TPAUSE

`TPAUSE` enters a timed pause state until the timestamp counter reaches a requested deadline or another wake condition occurs. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `WAITPKG`
- XED category/categories: `WAITPKG`
- ISA set(s): `WAITPKG`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32`. Representative implicit state: `EDX EAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `TPAUSE_GPR32u32` — `TPAUSE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## UD0

`UD0` unconditionally raises the invalid-opcode exception using an encoding reserved for that purpose. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `MISC`
- ISA set(s): `PPRO_UD0_LONG`, `PPRO_UD0_SHORT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32`; `GPR32 MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `UD0` — `UD0`
- `UD0_GPR32_GPR32` — `UD0`
- `UD0_GPR32_MEMd` — `UD0`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## UD1

`UD1` unconditionally raises the invalid-opcode exception using a ModRM-bearing reserved encoding. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `MISC`
- ISA set(s): `PPRO`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 GPR32`; `GPR32 MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `UD1_GPR32_GPR32` — `UD1`
- `UD1_GPR32_MEMd` — `UD1`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## UD2

`UD2` unconditionally raises the invalid-opcode exception and is the conventional x86 trap instruction used for deliberately unreachable code. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `MISC`
- ISA set(s): `PPRO`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `UD2` — `UD2`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## UDB

`UDB` is the permanently undefined one-byte instruction in 64-bit mode and therefore raises the invalid-opcode exception there. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `MISC`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `UDB` — `UDB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## UMONITOR

`UMONITOR` arms user-mode monitoring of a linear address so UMWAIT can enter an optimized wait state until the monitored location or another event changes execution conditions. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `WAITPKG`
- XED category/categories: `WAITPKG`
- ISA set(s): `WAITPKG`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `A_GPR`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `UMONITOR_GPRa` — `UMONITOR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## UMWAIT

`UMWAIT` enters a user-mode optimized wait state until a monitored-store event, timeout, or other wake condition occurs. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `WAITPKG`
- XED category/categories: `WAITPKG`
- ISA set(s): `WAITPKG`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32`. Representative implicit state: `EDX EAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `UMWAIT_GPR32` — `UMWAIT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## WRFSBASE

`WRFSBASE` writes a general-purpose register value as the FS segment base when FSGSBASE is enabled. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RDWRFSGS`
- XED category/categories: `RDWRFSGS`
- ISA set(s): `RDWRFSGS`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRy`. Representative implicit state: `FSBASE`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `WRFSBASE_GPRy` — `WRFSBASE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## WRGSBASE

`WRGSBASE` writes a general-purpose register value as the GS segment base when FSGSBASE is enabled. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RDWRFSGS`
- XED category/categories: `RDWRFSGS`
- ISA set(s): `RDWRFSGS`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRy`. Representative implicit state: `GSBASE`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `WRGSBASE_GPRy` — `WRGSBASE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XCHG

`XCHG` exchanges two operands; a memory form has implicit atomic exchange semantics. The pinned XED inventory represents it with 9 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `DATAXFER`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPRv`; `GPRv GPRv`; …. Representative implicit state: `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XCHG_GPR8_GPR8` — `XCHG`
- `XCHG_GPRv_GPRv` — `XCHG`
- `XCHG_GPRv_OrAX` — `XCHG`
- `XCHG_MEMb_GPR8` — `XCHG`
- `XCHG_MEMv_GPRv` — `XCHG`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XLAT

`XLAT` uses the unsigned byte in AL as an index from the implicit table base register, loads that table byte, and replaces AL with the result. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `MISC`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `MEM ArBX AL AL`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XLAT` — `XLAT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XOR

`XOR` computes bitwise exclusive OR. The pinned XED inventory represents it with 106 normalized encoding records and 54 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `APXEVEX`, `BASE`
- XED category/categories: `LOGICAL`
- ISA set(s): `APX_F`, `APX_F_N3`, `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR8 GPR8`; `GPR8 GPR8 GPR8`; `GPR8 GPR8 IMM`; …. Representative implicit state: `AL`; `OrAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XOR_AL_IMMb` — `XOR`
- `XOR_GPR8_GPR8_30` — `XOR`
- `XOR_GPR8_GPR8_32` — `XOR`
- `XOR_GPR8_IMMb_80r6` — `XOR`
- `XOR_GPR8_IMMb_82r6` — `XOR`
- `XOR_GPR8_MEMb` — `XOR`
- `XOR_GPR8i8_GPR8i8_APX` — `XOR`
- `XOR_GPR8i8_GPR8i8_APX_N3` — `XOR`
- `XOR_GPR8i8_GPR8i8_GPR8i8_APX_N3` — `XOR`
- `XOR_GPR8i8_GPR8i8_IMM8_APX_N3` — `XOR`
- `XOR_GPR8i8_GPR8i8_MEMi8_APX_N3` — `XOR`
- `XOR_GPR8i8_IMM8_APX` — `XOR`
- … 42 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XOR_LOCK

`XOR_LOCK` computes bitwise exclusive OR; this XED ICLASS is the LOCK-prefixed atomic read-modify-write form. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `LOGICAL`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM GPR8`; `MEM GPRv`; `MEM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XOR_LOCK_MEMb_GPR8` — `XOR_LOCK`
- `XOR_LOCK_MEMb_IMMb_80r6` — `XOR_LOCK`
- `XOR_LOCK_MEMb_IMMb_82r6` — `XOR_LOCK`
- `XOR_LOCK_MEMv_GPRv` — `XOR_LOCK`
- `XOR_LOCK_MEMv_IMMb` — `XOR_LOCK`
- `XOR_LOCK_MEMv_IMMz` — `XOR_LOCK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XRESLDTRK

`XRESLDTRK` resumes transactional load-address tracking after a matching suspend operation in the TSX load-address-tracking facility. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TSX_LDTRK`
- XED category/categories: `TSX_LDTRK`
- ISA set(s): `TSX_LDTRK`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XRESLDTRK` — `XRESLDTRK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XSUSLDTRK

`XSUSLDTRK` suspends transactional load-address tracking while leaving the surrounding RTM transaction active. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TSX_LDTRK`
- XED category/categories: `TSX_LDTRK`
- ISA set(s): `TSX_LDTRK`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XSUSLDTRK` — `XSUSLDTRK`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
