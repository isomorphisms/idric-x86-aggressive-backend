# Legacy, vendor-specific, and specialized extensions

This generated bundle contains 57 XED ICLASS reference sections. Each section preserves the instruction-specific semantic prose, availability, architectural effects, representative forms, backend notes, and pinned sources from the per-ICLASS semantic generator.

## LLWPCB

`LLWPCB` loads AMD Lightweight Profiling configuration from the Lightweight Profiling Control Block addressed by its operand. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `LWP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPRy`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LLWPCB_GPRyy` — `LLWPCB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LWPINS

`LWPINS` records an AMD Lightweight Profiling instrumentation event using the LWP control state and operands. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `LWP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPRy MEM IMM`; `VGPRy VGPR32 IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LWPINS_GPRyy_GPR32d_IMMd` — `LWPINS`
- `LWPINS_GPRyy_MEMd_IMMd` — `LWPINS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LWPVAL

`LWPVAL` records an AMD Lightweight Profiling value event using the LWP control state and operands. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `LWP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPRy MEM IMM`; `VGPRy VGPR32 IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LWPVAL_GPRyy_GPR32d_IMMd` — `LWPVAL`
- `LWPVAL_GPRyy_MEMd_IMMd` — `LWPVAL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## REP_XSTORE

`REP_XSTORE` repeats a VIA PadLock cryptographic or hashing primitive over a buffer using implicit registers for state, addresses, and count. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VIA_PADLOCK_RNG`
- XED category/categories: `VIA_PADLOCK`
- ISA set(s): `VIA_PADLOCK_RNG`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `MEM OrCX OrDX OrAX ArDI FINAL`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `REP_XSTORE` — `REP_XSTORE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SLWPCB

`SLWPCB` stores or exposes the current AMD Lightweight Profiling Control Block address according to the LWP architectural interface. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `LWP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPRy`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SLWPCB_GPRyy` — `SLWPCB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFRCZPD

`VFRCZPD` extracts the fractional part of packed double-precision floating-point elements using AMD XOP FRCZ semantics. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`; `YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFRCZPD_XMMdq_MEMdq` — `VFRCZPD`
- `VFRCZPD_XMMdq_XMMdq` — `VFRCZPD`
- `VFRCZPD_YMMqq_MEMqq` — `VFRCZPD`
- `VFRCZPD_YMMqq_YMMqq` — `VFRCZPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFRCZPS

`VFRCZPS` extracts the fractional part of packed single-precision floating-point elements using AMD XOP FRCZ semantics. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`; `YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFRCZPS_XMMdq_MEMdq` — `VFRCZPS`
- `VFRCZPS_XMMdq_XMMdq` — `VFRCZPS`
- `VFRCZPS_YMMqq_MEMqq` — `VFRCZPS`
- `VFRCZPS_YMMqq_YMMqq` — `VFRCZPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFRCZSD

`VFRCZSD` extracts the fractional part of a scalar double-precision floating-point element using AMD XOP FRCZ semantics. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFRCZSD_XMMdq_MEMq` — `VFRCZSD`
- `VFRCZSD_XMMdq_XMMq` — `VFRCZSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VFRCZSS

`VFRCZSS` extracts the fractional part of a scalar single-precision floating-point element using AMD XOP FRCZ semantics. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VFRCZSS_XMMdq_MEMd` — `VFRCZSS`
- `VFRCZSS_XMMdq_XMMd` — `VFRCZSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCMOV

`VPCMOV` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCMOV_XMMdq_XMMdq_MEMdq_XMMdq` — `VPCMOV`
- `VPCMOV_XMMdq_XMMdq_XMMdq_MEMdq` — `VPCMOV`
- `VPCMOV_XMMdq_XMMdq_XMMdq_XMMdq` — `VPCMOV`
- `VPCMOV_YMMqq_YMMqq_MEMqq_YMMqq` — `VPCMOV`
- `VPCMOV_YMMqq_YMMqq_YMMqq_MEMqq` — `VPCMOV`
- `VPCMOV_YMMqq_YMMqq_YMMqq_YMMqq` — `VPCMOV`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCOMB

`VPCOMB` performs AMD XOP packed integer comparisons under the predicate encoded by the mnemonic or immediate control and writes per-lane Boolean results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCOMB_XMMdq_XMMdq_MEMdq_IMMb` — `VPCOMB`
- `VPCOMB_XMMdq_XMMdq_XMMdq_IMMb` — `VPCOMB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCOMD

`VPCOMD` performs AMD XOP packed integer comparisons under the predicate encoded by the mnemonic or immediate control and writes per-lane Boolean results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCOMD_XMMdq_XMMdq_MEMdq_IMMb` — `VPCOMD`
- `VPCOMD_XMMdq_XMMdq_XMMdq_IMMb` — `VPCOMD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCOMQ

`VPCOMQ` performs AMD XOP packed integer comparisons under the predicate encoded by the mnemonic or immediate control and writes per-lane Boolean results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCOMQ_XMMdq_XMMdq_MEMdq_IMMb` — `VPCOMQ`
- `VPCOMQ_XMMdq_XMMdq_XMMdq_IMMb` — `VPCOMQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCOMUB

`VPCOMUB` performs AMD XOP packed integer comparisons under the predicate encoded by the mnemonic or immediate control and writes per-lane Boolean results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCOMUB_XMMdq_XMMdq_MEMdq_IMMb` — `VPCOMUB`
- `VPCOMUB_XMMdq_XMMdq_XMMdq_IMMb` — `VPCOMUB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCOMUD

`VPCOMUD` performs AMD XOP packed integer comparisons under the predicate encoded by the mnemonic or immediate control and writes per-lane Boolean results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCOMUD_XMMdq_XMMdq_MEMdq_IMMb` — `VPCOMUD`
- `VPCOMUD_XMMdq_XMMdq_XMMdq_IMMb` — `VPCOMUD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCOMUQ

`VPCOMUQ` performs AMD XOP packed integer comparisons under the predicate encoded by the mnemonic or immediate control and writes per-lane Boolean results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCOMUQ_XMMdq_XMMdq_MEMdq_IMMb` — `VPCOMUQ`
- `VPCOMUQ_XMMdq_XMMdq_XMMdq_IMMb` — `VPCOMUQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCOMUW

`VPCOMUW` performs AMD XOP packed integer comparisons under the predicate encoded by the mnemonic or immediate control and writes per-lane Boolean results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCOMUW_XMMdq_XMMdq_MEMdq_IMMb` — `VPCOMUW`
- `VPCOMUW_XMMdq_XMMdq_XMMdq_IMMb` — `VPCOMUW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPCOMW

`VPCOMW` performs AMD XOP packed integer comparisons under the predicate encoded by the mnemonic or immediate control and writes per-lane Boolean results. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM IMM`; `XMM XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPCOMW_XMMdq_XMMdq_MEMdq_IMMb` — `VPCOMW`
- `VPCOMW_XMMdq_XMMdq_XMMdq_IMMb` — `VPCOMW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPERMIL2PD

`VPERMIL2PD` reorders packed double-precision floating-point elements according to an immediate, index vector, or fixed permutation. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM IMM`; `XMM XMM XMM MEM IMM`; `XMM XMM XMM XMM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPERMIL2PD_XMMdq_XMMdq_MEMdq_XMMdq_IMMb` — `VPERMIL2PD`
- `VPERMIL2PD_XMMdq_XMMdq_XMMdq_MEMdq_IMMb` — `VPERMIL2PD`
- `VPERMIL2PD_XMMdq_XMMdq_XMMdq_XMMdq_IMMb` — `VPERMIL2PD`
- `VPERMIL2PD_YMMqq_YMMqq_MEMqq_YMMqq_IMMb` — `VPERMIL2PD`
- `VPERMIL2PD_YMMqq_YMMqq_YMMqq_MEMqq_IMMb` — `VPERMIL2PD`
- `VPERMIL2PD_YMMqq_YMMqq_YMMqq_YMMqq_IMMb` — `VPERMIL2PD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPERMIL2PS

`VPERMIL2PS` reorders packed single-precision floating-point elements according to an immediate, index vector, or fixed permutation. The pinned XED inventory represents it with 8 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM IMM`; `XMM XMM XMM MEM IMM`; `XMM XMM XMM XMM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPERMIL2PS_XMMdq_XMMdq_MEMdq_XMMdq_IMMb` — `VPERMIL2PS`
- `VPERMIL2PS_XMMdq_XMMdq_XMMdq_MEMdq_IMMb` — `VPERMIL2PS`
- `VPERMIL2PS_XMMdq_XMMdq_XMMdq_XMMdq_IMMb` — `VPERMIL2PS`
- `VPERMIL2PS_YMMqq_YMMqq_MEMqq_YMMqq_IMMb` — `VPERMIL2PS`
- `VPERMIL2PS_YMMqq_YMMqq_YMMqq_MEMqq_IMMb` — `VPERMIL2PS`
- `VPERMIL2PS_YMMqq_YMMqq_YMMqq_YMMqq_IMMb` — `VPERMIL2PS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDBD

`VPHADDBD` adds corresponding 32-bit doubleword elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDBD_XMMdq_MEMdq` — `VPHADDBD`
- `VPHADDBD_XMMdq_XMMdq` — `VPHADDBD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDBQ

`VPHADDBQ` adds corresponding 64-bit quadword elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDBQ_XMMdq_MEMdq` — `VPHADDBQ`
- `VPHADDBQ_XMMdq_XMMdq` — `VPHADDBQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDBW

`VPHADDBW` adds corresponding 16-bit word elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDBW_XMMdq_MEMdq` — `VPHADDBW`
- `VPHADDBW_XMMdq_XMMdq` — `VPHADDBW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDDQ

`VPHADDDQ` adds corresponding double-quadword vector data and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDDQ_XMMdq_MEMdq` — `VPHADDDQ`
- `VPHADDDQ_XMMdq_XMMdq` — `VPHADDDQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDUBD

`VPHADDUBD` adds corresponding 32-bit doubleword elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDUBD_XMMdq_MEMdq` — `VPHADDUBD`
- `VPHADDUBD_XMMdq_XMMdq` — `VPHADDUBD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDUBQ

`VPHADDUBQ` adds corresponding 64-bit quadword elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDUBQ_XMMdq_MEMdq` — `VPHADDUBQ`
- `VPHADDUBQ_XMMdq_XMMdq` — `VPHADDUBQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDUBW

`VPHADDUBW` adds corresponding 16-bit word elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDUBW_XMMdq_MEMdq` — `VPHADDUBW`
- `VPHADDUBW_XMMdq_XMMdq` — `VPHADDUBW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDUDQ

`VPHADDUDQ` adds corresponding double-quadword vector data and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDUDQ_XMMdq_MEMdq` — `VPHADDUDQ`
- `VPHADDUDQ_XMMdq_XMMdq` — `VPHADDUDQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDUWD

`VPHADDUWD` adds corresponding 32-bit doubleword elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDUWD_XMMdq_MEMdq` — `VPHADDUWD`
- `VPHADDUWD_XMMdq_XMMdq` — `VPHADDUWD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDUWQ

`VPHADDUWQ` adds corresponding 64-bit quadword elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDUWQ_XMMdq_MEMdq` — `VPHADDUWQ`
- `VPHADDUWQ_XMMdq_XMMdq` — `VPHADDUWQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDWD

`VPHADDWD` adds corresponding 32-bit doubleword elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDWD_XMMdq_MEMdq` — `VPHADDWD`
- `VPHADDWD_XMMdq_XMMdq` — `VPHADDWD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHADDWQ

`VPHADDWQ` adds corresponding 64-bit quadword elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHADDWQ_XMMdq_MEMdq` — `VPHADDWQ`
- `VPHADDWQ_XMMdq_XMMdq` — `VPHADDWQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHSUBBW

`VPHSUBBW` subtracts corresponding 16-bit word elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHSUBBW_XMMdq_MEMdq` — `VPHSUBBW`
- `VPHSUBBW_XMMdq_XMMdq` — `VPHSUBBW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHSUBDQ

`VPHSUBDQ` subtracts corresponding double-quadword vector data and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHSUBDQ_XMMdq_MEMdq` — `VPHSUBDQ`
- `VPHSUBDQ_XMMdq_XMMdq` — `VPHSUBDQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPHSUBWD

`VPHSUBWD` subtracts corresponding 32-bit doubleword elements and writes the lane-wise result. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPHSUBWD_XMMdq_MEMdq` — `VPHSUBWD`
- `VPHSUBWD_XMMdq_XMMdq` — `VPHSUBWD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMACSDD

`VPMACSDD` performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMACSDD_XMMdq_XMMdq_MEMdq_XMMdq` — `VPMACSDD`
- `VPMACSDD_XMMdq_XMMdq_XMMdq_XMMdq` — `VPMACSDD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMACSDQH

`VPMACSDQH` performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMACSDQH_XMMdq_XMMdq_MEMdq_XMMdq` — `VPMACSDQH`
- `VPMACSDQH_XMMdq_XMMdq_XMMdq_XMMdq` — `VPMACSDQH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMACSDQL

`VPMACSDQL` performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMACSDQL_XMMdq_XMMdq_MEMdq_XMMdq` — `VPMACSDQL`
- `VPMACSDQL_XMMdq_XMMdq_XMMdq_XMMdq` — `VPMACSDQL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMACSSDD

`VPMACSSDD` performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMACSSDD_XMMdq_XMMdq_MEMdq_XMMdq` — `VPMACSSDD`
- `VPMACSSDD_XMMdq_XMMdq_XMMdq_XMMdq` — `VPMACSSDD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMACSSDQH

`VPMACSSDQH` performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMACSSDQH_XMMdq_XMMdq_MEMdq_XMMdq` — `VPMACSSDQH`
- `VPMACSSDQH_XMMdq_XMMdq_XMMdq_XMMdq` — `VPMACSSDQH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMACSSDQL

`VPMACSSDQL` performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMACSSDQL_XMMdq_XMMdq_MEMdq_XMMdq` — `VPMACSSDQL`
- `VPMACSSDQL_XMMdq_XMMdq_XMMdq_XMMdq` — `VPMACSSDQL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMACSSWD

`VPMACSSWD` performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMACSSWD_XMMdq_XMMdq_MEMdq_XMMdq` — `VPMACSSWD`
- `VPMACSSWD_XMMdq_XMMdq_XMMdq_XMMdq` — `VPMACSSWD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMACSSWW

`VPMACSSWW` performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMACSSWW_XMMdq_XMMdq_MEMdq_XMMdq` — `VPMACSSWW`
- `VPMACSSWW_XMMdq_XMMdq_XMMdq_XMMdq` — `VPMACSSWW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMACSWD

`VPMACSWD` performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMACSWD_XMMdq_XMMdq_MEMdq_XMMdq` — `VPMACSWD`
- `VPMACSWD_XMMdq_XMMdq_XMMdq_XMMdq` — `VPMACSWD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMACSWW

`VPMACSWW` performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMACSWW_XMMdq_XMMdq_MEMdq_XMMdq` — `VPMACSWW`
- `VPMACSWW_XMMdq_XMMdq_XMMdq_XMMdq` — `VPMACSWW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMADCSSWD

`VPMADCSSWD` performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMADCSSWD_XMMdq_XMMdq_MEMdq_XMMdq` — `VPMADCSSWD`
- `VPMADCSSWD_XMMdq_XMMdq_XMMdq_XMMdq` — `VPMADCSSWD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPMADCSWD

`VPMADCSWD` performs an AMD XOP packed integer multiply-accumulate operation, with the mnemonic selecting signedness, source width, accumulation width, and saturating versus wrapping behavior. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPMADCSWD_XMMdq_XMMdq_MEMdq_XMMdq` — `VPMADCSWD`
- `VPMADCSWD_XMMdq_XMMdq_XMMdq_XMMdq` — `VPMADCSWD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPPERM

`VPPERM` reorders its encoded scalar or vector elements according to an immediate, index vector, or fixed permutation. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM MEM XMM`; `XMM XMM XMM MEM`; `XMM XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPPERM_XMMdq_XMMdq_MEMdq_XMMdq` — `VPPERM`
- `VPPERM_XMMdq_XMMdq_XMMdq_MEMdq` — `VPPERM`
- `VPPERM_XMMdq_XMMdq_XMMdq_XMMdq` — `VPPERM`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPROTB

`VPROTB` performs AMD XOP packed per-element rotates using signed variable rotate counts supplied by the control operand. The pinned XED inventory represents it with 6 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM MEM XMM`; `XMM XMM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPROTB_XMMdq_MEMdq_IMMb` — `VPROTB`
- `VPROTB_XMMdq_MEMdq_XMMdq` — `VPROTB`
- `VPROTB_XMMdq_XMMdq_IMMb` — `VPROTB`
- `VPROTB_XMMdq_XMMdq_MEMdq` — `VPROTB`
- `VPROTB_XMMdq_XMMdq_XMMdq` — `VPROTB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPROTD

`VPROTD` performs AMD XOP packed per-element rotates using signed variable rotate counts supplied by the control operand. The pinned XED inventory represents it with 6 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM MEM XMM`; `XMM XMM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPROTD_XMMdq_MEMdq_IMMb` — `VPROTD`
- `VPROTD_XMMdq_MEMdq_XMMdq` — `VPROTD`
- `VPROTD_XMMdq_XMMdq_IMMb` — `VPROTD`
- `VPROTD_XMMdq_XMMdq_MEMdq` — `VPROTD`
- `VPROTD_XMMdq_XMMdq_XMMdq` — `VPROTD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPROTQ

`VPROTQ` performs AMD XOP packed per-element rotates using signed variable rotate counts supplied by the control operand. The pinned XED inventory represents it with 6 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM MEM XMM`; `XMM XMM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPROTQ_XMMdq_MEMdq_IMMb` — `VPROTQ`
- `VPROTQ_XMMdq_MEMdq_XMMdq` — `VPROTQ`
- `VPROTQ_XMMdq_XMMdq_IMMb` — `VPROTQ`
- `VPROTQ_XMMdq_XMMdq_MEMdq` — `VPROTQ`
- `VPROTQ_XMMdq_XMMdq_XMMdq` — `VPROTQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPROTW

`VPROTW` performs AMD XOP packed per-element rotates using signed variable rotate counts supplied by the control operand. The pinned XED inventory represents it with 6 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XOP`
- XED category/categories: `XOP`
- ISA set(s): `XOP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM IMM`; `XMM MEM XMM`; `XMM XMM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VPROTW_XMMdq_MEMdq_IMMb` — `VPROTW`
- `VPROTW_XMMdq_MEMdq_XMMdq` — `VPROTW`
- `VPROTW_XMMdq_XMMdq_IMMb` — `VPROTW`
- `VPROTW_XMMdq_XMMdq_MEMdq` — `VPROTW`
- `VPROTW_XMMdq_XMMdq_XMMdq` — `VPROTW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPSHLB

`VPSHLB` performs AMD XOP packed logical shifts with per-element signed counts, using count sign to choose left versus logical-right direction. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

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

- `VPSHLB_XMMdq_MEMdq_XMMdq` — `VPSHLB`
- `VPSHLB_XMMdq_XMMdq_MEMdq` — `VPSHLB`
- `VPSHLB_XMMdq_XMMdq_XMMdq` — `VPSHLB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPSHLD

`VPSHLD` performs AMD XOP packed logical shifts with per-element signed counts, using count sign to choose left versus logical-right direction. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

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

- `VPSHLD_XMMdq_MEMdq_XMMdq` — `VPSHLD`
- `VPSHLD_XMMdq_XMMdq_MEMdq` — `VPSHLD`
- `VPSHLD_XMMdq_XMMdq_XMMdq` — `VPSHLD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPSHLQ

`VPSHLQ` performs AMD XOP packed logical shifts with per-element signed counts, using count sign to choose left versus logical-right direction. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

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

- `VPSHLQ_XMMdq_MEMdq_XMMdq` — `VPSHLQ`
- `VPSHLQ_XMMdq_XMMdq_MEMdq` — `VPSHLQ`
- `VPSHLQ_XMMdq_XMMdq_XMMdq` — `VPSHLQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VPSHLW

`VPSHLW` performs AMD XOP packed logical shifts with per-element signed counts, using count sign to choose left versus logical-right direction. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

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

- `VPSHLW_XMMdq_MEMdq_XMMdq` — `VPSHLW`
- `VPSHLW_XMMdq_XMMdq_MEMdq` — `VPSHLW`
- `VPSHLW_XMMdq_XMMdq_XMMdq` — `VPSHLW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XSTORE

`XSTORE` requests random bytes from VIA PadLock's hardware random-number generator and stores them through the instruction's implicit destination/count interface. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VIA_PADLOCK_RNG`
- XED category/categories: `VIA_PADLOCK`
- ISA set(s): `VIA_PADLOCK_RNG`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `MEM OrCX OrDX OrAX ArDI FINAL`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XSTORE` — `XSTORE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
