# Virtualization and confidential computing

This generated bundle contains 98 XED ICLASS reference sections. Each section preserves the instruction-specific semantic prose, availability, architectural effects, representative forms, backend notes, and pinned sources from the per-ICLASS semantic generator.

## CLGI

`CLGI` clears AMD SVM's global-interrupt flag, blocking interrupt delivery governed by that virtualization state until it is set again. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SVM`
- XED category/categories: `SYSTEM`
- ISA set(s): `SVM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CLGI` — `CLGI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INVEPT

`INVEPT` invalidates processor-maintained translation or virtualization-caching state selected by its operands. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `APX_F_VMX`, `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `GPR32 MEM`; `GPR64 MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INVEPT_GPR32_MEMdq` — `INVEPT`
- `INVEPT_GPR64_MEMdq` — `INVEPT`
- `INVEPT_GPR64i64_MEMi128_APX` — `INVEPT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INVLPGA

`INVLPGA` invalidates processor-maintained translation or virtualization-caching state selected by its operands. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SVM`
- XED category/categories: `SYSTEM`
- ISA set(s): `SVM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `ArAX ECX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INVLPGA_ArAX_ECX` — `INVLPGA`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INVVPID

`INVVPID` invalidates processor-maintained translation or virtualization-caching state selected by its operands. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `APX_F_VMX`, `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `GPR32 MEM`; `GPR64 MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INVVPID_GPR32_MEMdq` — `INVVPID`
- `INVVPID_GPR64_MEMdq` — `INVVPID`
- `INVVPID_GPR64i64_MEMi128_APX` — `INVVPID`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PSMASH

`PSMASH` splits an AMD SEV-SNP 2 MiB reverse-map-table entry into the corresponding set of 4 KiB entries. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SNP`
- XED category/categories: `SYSTEM`
- ISA set(s): `SNP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PSMASH_RAX` — `PSMASH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PVALIDATE

`PVALIDATE` validates or rescinds validation of an AMD SEV-SNP guest page's reverse-map-table entry and returns status through EAX and flags. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SNP`
- XED category/categories: `SYSTEM`
- ISA set(s): `SNP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RAX ECX EDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PVALIDATE_RAX_ECX_EDX` — `PVALIDATE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RMPADJUST

`RMPADJUST` changes AMD SEV-SNP reverse-map-table permissions for a guest page, including VMPL-targeted permissions selected by register state. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SNP`
- XED category/categories: `SYSTEM`
- ISA set(s): `SNP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RAX RCX RDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RMPADJUST_RAX_RCX_RDX` — `RMPADJUST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RMPUPDATE

`RMPUPDATE` writes a new AMD SEV-SNP reverse-map-table entry for the selected system physical page using state supplied by privileged software. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SNP`
- XED category/categories: `SYSTEM`
- ISA set(s): `SNP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RAX RCX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RMPUPDATE_RAX_RCX` — `RMPUPDATE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SEAMCALL

`SEAMCALL` transfers from legacy VMX-root operation into SEAM VMX-root operation to invoke a SEAM-module service. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TDX`
- XED category/categories: `LEGACY`
- ISA set(s): `TDX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SEAMCALL` — `SEAMCALL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SEAMOPS

`SEAMOPS` invokes a SEAM-specific operation while software is executing in SEAM root operation. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TDX`
- XED category/categories: `LEGACY`
- ISA set(s): `TDX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SEAMOPS` — `SEAMOPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SEAMRET

`SEAMRET` returns from SEAM VMX-root operation to the calling legacy VMX-root environment. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TDX`
- XED category/categories: `LEGACY`
- ISA set(s): `TDX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SEAMRET` — `SEAMRET`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SKINIT

`SKINIT` enters AMD Secure Startup by measuring and launching the secure loader identified by the instruction's implicit state. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SVM`
- XED category/categories: `SYSTEM`
- ISA set(s): `SVM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SKINIT_EAX` — `SKINIT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## STGI

`STGI` sets AMD SVM's global-interrupt flag, permitting interrupt delivery governed by that virtualization state. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SVM`
- XED category/categories: `SYSTEM`
- ISA set(s): `SVM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `STGI` — `STGI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## TDCALL

`TDCALL` causes a Trust Domain guest to exit to the SEAM module so it can request a TDX service. The pinned XED inventory represents it with 2 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `TDX`
- XED category/categories: `LEGACY`
- ISA set(s): `TDX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `ECX`; `RCX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `TDCALL` — `TDCALL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMASKMOVDQU

`VMASKMOVDQU` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM`. Representative implicit state: `MEM ArDI`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMASKMOVDQU_XMMxub_XMMxub` — `VMASKMOVDQU`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMASKMOVPD

`VMASKMOVPD` copies packed double-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM XMM`; `MEM YMM YMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMASKMOVPD_MEMdq_XMMdq_XMMdq` — `VMASKMOVPD`
- `VMASKMOVPD_MEMqq_YMMqq_YMMqq` — `VMASKMOVPD`
- `VMASKMOVPD_XMMdq_XMMdq_MEMdq` — `VMASKMOVPD`
- `VMASKMOVPD_YMMqq_YMMqq_MEMqq` — `VMASKMOVPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMASKMOVPS

`VMASKMOVPS` copies packed single-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `AVX`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM XMM`; `MEM YMM YMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMASKMOVPS_MEMdq_XMMdq_XMMdq` — `VMASKMOVPS`
- `VMASKMOVPS_MEMqq_YMMqq_YMMqq` — `VMASKMOVPS`
- `VMASKMOVPS_XMMdq_XMMdq_MEMdq` — `VMASKMOVPS`
- `VMASKMOVPS_YMMqq_YMMqq_MEMqq` — `VMASKMOVPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMAXBF16

`VMAXBF16` selects maxima of corresponding bfloat16 elements and writes the lane-wise result. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX10_2_BF16_128`, `AVX10_2_BF16_256`, `AVX10_2_BF16_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `YMM MASK1 YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMAXBF16_XMMbf16_MASKmskw_XMMbf16_MEMbf16_AVX512` — `VMAXBF16`
- `VMAXBF16_XMMbf16_MASKmskw_XMMbf16_XMMbf16_AVX512` — `VMAXBF16`
- `VMAXBF16_YMMbf16_MASKmskw_YMMbf16_MEMbf16_AVX512` — `VMAXBF16`
- `VMAXBF16_YMMbf16_MASKmskw_YMMbf16_YMMbf16_AVX512` — `VMAXBF16`
- `VMAXBF16_ZMMbf16_MASKmskw_ZMMbf16_MEMbf16_AVX512` — `VMAXBF16`
- `VMAXBF16_ZMMbf16_MASKmskw_ZMMbf16_ZMMbf16_AVX512` — `VMAXBF16`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMAXPD

`VMAXPD` selects maxima of corresponding packed double-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 11 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMAXPD_XMMdq_XMMdq_MEMdq` — `VMAXPD`
- `VMAXPD_XMMdq_XMMdq_XMMdq` — `VMAXPD`
- `VMAXPD_XMMf64_MASKmskw_XMMf64_MEMf64_AVX512` — `VMAXPD`
- `VMAXPD_XMMf64_MASKmskw_XMMf64_XMMf64_AVX512` — `VMAXPD`
- `VMAXPD_YMMf64_MASKmskw_YMMf64_MEMf64_AVX512` — `VMAXPD`
- `VMAXPD_YMMf64_MASKmskw_YMMf64_YMMf64_AVX512` — `VMAXPD`
- `VMAXPD_YMMqq_YMMqq_MEMqq` — `VMAXPD`
- `VMAXPD_YMMqq_YMMqq_YMMqq` — `VMAXPD`
- `VMAXPD_ZMMf64_MASKmskw_ZMMf64_MEMf64_AVX512` — `VMAXPD`
- `VMAXPD_ZMMf64_MASKmskw_ZMMf64_ZMMf64_AVX512` — `VMAXPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMAXPH

`VMAXPH` selects maxima of corresponding packed IEEE binary16 floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 7 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `FP16`
- ISA set(s): `AVX512_FP16_128`, `AVX512_FP16_256`, `AVX512_FP16_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `YMM MASK1 YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMAXPH_XMMf16_MASKmskw_XMMf16_MEMf16_AVX512` — `VMAXPH`
- `VMAXPH_XMMf16_MASKmskw_XMMf16_XMMf16_AVX512` — `VMAXPH`
- `VMAXPH_YMMf16_MASKmskw_YMMf16_MEMf16_AVX512` — `VMAXPH`
- `VMAXPH_YMMf16_MASKmskw_YMMf16_YMMf16_AVX512` — `VMAXPH`
- `VMAXPH_ZMMf16_MASKmskw_ZMMf16_MEMf16_AVX512` — `VMAXPH`
- `VMAXPH_ZMMf16_MASKmskw_ZMMf16_ZMMf16_AVX512` — `VMAXPH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMAXPS

`VMAXPS` selects maxima of corresponding packed single-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 11 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMAXPS_XMMdq_XMMdq_MEMdq` — `VMAXPS`
- `VMAXPS_XMMdq_XMMdq_XMMdq` — `VMAXPS`
- `VMAXPS_XMMf32_MASKmskw_XMMf32_MEMf32_AVX512` — `VMAXPS`
- `VMAXPS_XMMf32_MASKmskw_XMMf32_XMMf32_AVX512` — `VMAXPS`
- `VMAXPS_YMMf32_MASKmskw_YMMf32_MEMf32_AVX512` — `VMAXPS`
- `VMAXPS_YMMf32_MASKmskw_YMMf32_YMMf32_AVX512` — `VMAXPS`
- `VMAXPS_YMMqq_YMMqq_MEMqq` — `VMAXPS`
- `VMAXPS_YMMqq_YMMqq_YMMqq` — `VMAXPS`
- `VMAXPS_ZMMf32_MASKmskw_ZMMf32_MEMf32_AVX512` — `VMAXPS`
- `VMAXPS_ZMMf32_MASKmskw_ZMMf32_ZMMf32_AVX512` — `VMAXPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMAXSD

`VMAXSD` selects maxima of corresponding a scalar double-precision floating-point element and writes the lane-wise result. The pinned XED inventory represents it with 5 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMAXSD_XMMdq_XMMdq_MEMq` — `VMAXSD`
- `VMAXSD_XMMdq_XMMdq_XMMq` — `VMAXSD`
- `VMAXSD_XMMf64_MASKmskw_XMMf64_MEMf64_AVX512` — `VMAXSD`
- `VMAXSD_XMMf64_MASKmskw_XMMf64_XMMf64_AVX512` — `VMAXSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMAXSH

`VMAXSH` selects maxima of corresponding a scalar IEEE binary16 floating-point element and writes the lane-wise result. The pinned XED inventory represents it with 3 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `FP16`
- ISA set(s): `AVX512_FP16_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMAXSH_XMMf16_MASKmskw_XMMf16_MEMf16_AVX512` — `VMAXSH`
- `VMAXSH_XMMf16_MASKmskw_XMMf16_XMMf16_AVX512` — `VMAXSH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMAXSS

`VMAXSS` selects maxima of corresponding a scalar single-precision floating-point element and writes the lane-wise result. The pinned XED inventory represents it with 5 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMAXSS_XMMdq_XMMdq_MEMd` — `VMAXSS`
- `VMAXSS_XMMdq_XMMdq_XMMd` — `VMAXSS`
- `VMAXSS_XMMf32_MASKmskw_XMMf32_MEMf32_AVX512` — `VMAXSS`
- `VMAXSS_XMMf32_MASKmskw_XMMf32_XMMf32_AVX512` — `VMAXSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMCALL

`VMCALL` transfers from guest context to a hypervisor-defined service through the architecture's virtualization call mechanism. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMCALL` — `VMCALL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMCLEAR

`VMCLEAR` marks the referenced VMCS inactive and ensures its current implementation state is written to the VMCS region in memory. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMCLEAR_MEMq` — `VMCLEAR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMFUNC

`VMFUNC` invokes a VM function selected by EAX while executing in VMX non-root operation, subject to VMCS enablement of that function. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VMFUNC`
- XED category/categories: `VTX`
- ISA set(s): `VMFUNC`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMFUNC` — `VMFUNC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINBF16

`VMINBF16` selects minima of corresponding bfloat16 elements and writes the lane-wise result. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX10_2_BF16_128`, `AVX10_2_BF16_256`, `AVX10_2_BF16_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `YMM MASK1 YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINBF16_XMMbf16_MASKmskw_XMMbf16_MEMbf16_AVX512` — `VMINBF16`
- `VMINBF16_XMMbf16_MASKmskw_XMMbf16_XMMbf16_AVX512` — `VMINBF16`
- `VMINBF16_YMMbf16_MASKmskw_YMMbf16_MEMbf16_AVX512` — `VMINBF16`
- `VMINBF16_YMMbf16_MASKmskw_YMMbf16_YMMbf16_AVX512` — `VMINBF16`
- `VMINBF16_ZMMbf16_MASKmskw_ZMMbf16_MEMbf16_AVX512` — `VMINBF16`
- `VMINBF16_ZMMbf16_MASKmskw_ZMMbf16_ZMMbf16_AVX512` — `VMINBF16`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINMAXBF16

`VMINMAXBF16` selects maxima of corresponding bfloat16 elements and writes the lane-wise result. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX512_MINMAX_128`, `AVX512_MINMAX_256`, `AVX512_MINMAX_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM IMM`; `XMM MASK1 XMM XMM IMM`; `YMM MASK1 YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINMAXBF16_XMMbf16_MASKmskw_XMMbf16_MEMbf16_IMM8_AVX512` — `VMINMAXBF16`
- `VMINMAXBF16_XMMbf16_MASKmskw_XMMbf16_XMMbf16_IMM8_AVX512` — `VMINMAXBF16`
- `VMINMAXBF16_YMMbf16_MASKmskw_YMMbf16_MEMbf16_IMM8_AVX512` — `VMINMAXBF16`
- `VMINMAXBF16_YMMbf16_MASKmskw_YMMbf16_YMMbf16_IMM8_AVX512` — `VMINMAXBF16`
- `VMINMAXBF16_ZMMbf16_MASKmskw_ZMMbf16_MEMbf16_IMM8_AVX512` — `VMINMAXBF16`
- `VMINMAXBF16_ZMMbf16_MASKmskw_ZMMbf16_ZMMbf16_IMM8_AVX512` — `VMINMAXBF16`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINMAXPD

`VMINMAXPD` selects maxima of corresponding packed double-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 7 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX512_MINMAX_128`, `AVX512_MINMAX_256`, `AVX512_MINMAX_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM IMM`; `XMM MASK1 XMM XMM IMM`; `YMM MASK1 YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINMAXPD_XMMf64_MASKmskw_XMMf64_MEMf64_IMM8_AVX512` — `VMINMAXPD`
- `VMINMAXPD_XMMf64_MASKmskw_XMMf64_XMMf64_IMM8_AVX512` — `VMINMAXPD`
- `VMINMAXPD_YMMf64_MASKmskw_YMMf64_MEMf64_IMM8_AVX512` — `VMINMAXPD`
- `VMINMAXPD_YMMf64_MASKmskw_YMMf64_YMMf64_IMM8_AVX512` — `VMINMAXPD`
- `VMINMAXPD_ZMMf64_MASKmskw_ZMMf64_MEMf64_IMM8_AVX512` — `VMINMAXPD`
- `VMINMAXPD_ZMMf64_MASKmskw_ZMMf64_ZMMf64_IMM8_AVX512` — `VMINMAXPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINMAXPH

`VMINMAXPH` selects maxima of corresponding packed IEEE binary16 floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 7 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX512_MINMAX_128`, `AVX512_MINMAX_256`, `AVX512_MINMAX_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM IMM`; `XMM MASK1 XMM XMM IMM`; `YMM MASK1 YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINMAXPH_XMMf16_MASKmskw_XMMf16_MEMf16_IMM8_AVX512` — `VMINMAXPH`
- `VMINMAXPH_XMMf16_MASKmskw_XMMf16_XMMf16_IMM8_AVX512` — `VMINMAXPH`
- `VMINMAXPH_YMMf16_MASKmskw_YMMf16_MEMf16_IMM8_AVX512` — `VMINMAXPH`
- `VMINMAXPH_YMMf16_MASKmskw_YMMf16_YMMf16_IMM8_AVX512` — `VMINMAXPH`
- `VMINMAXPH_ZMMf16_MASKmskw_ZMMf16_MEMf16_IMM8_AVX512` — `VMINMAXPH`
- `VMINMAXPH_ZMMf16_MASKmskw_ZMMf16_ZMMf16_IMM8_AVX512` — `VMINMAXPH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINMAXPS

`VMINMAXPS` selects maxima of corresponding packed single-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 7 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX512_MINMAX_128`, `AVX512_MINMAX_256`, `AVX512_MINMAX_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM IMM`; `XMM MASK1 XMM XMM IMM`; `YMM MASK1 YMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINMAXPS_XMMf32_MASKmskw_XMMf32_MEMf32_IMM8_AVX512` — `VMINMAXPS`
- `VMINMAXPS_XMMf32_MASKmskw_XMMf32_XMMf32_IMM8_AVX512` — `VMINMAXPS`
- `VMINMAXPS_YMMf32_MASKmskw_YMMf32_MEMf32_IMM8_AVX512` — `VMINMAXPS`
- `VMINMAXPS_YMMf32_MASKmskw_YMMf32_YMMf32_IMM8_AVX512` — `VMINMAXPS`
- `VMINMAXPS_ZMMf32_MASKmskw_ZMMf32_MEMf32_IMM8_AVX512` — `VMINMAXPS`
- `VMINMAXPS_ZMMf32_MASKmskw_ZMMf32_ZMMf32_IMM8_AVX512` — `VMINMAXPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINMAXSD

`VMINMAXSD` selects maxima of corresponding a scalar double-precision floating-point element and writes the lane-wise result. The pinned XED inventory represents it with 3 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX512_MINMAX_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM IMM`; `XMM MASK1 XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINMAXSD_XMMf64_MASKmskw_XMMf64_MEMf64_IMM8_AVX512` — `VMINMAXSD`
- `VMINMAXSD_XMMf64_MASKmskw_XMMf64_XMMf64_IMM8_AVX512` — `VMINMAXSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINMAXSH

`VMINMAXSH` selects maxima of corresponding a scalar IEEE binary16 floating-point element and writes the lane-wise result. The pinned XED inventory represents it with 3 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX512_MINMAX_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM IMM`; `XMM MASK1 XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINMAXSH_XMMf16_MASKmskw_XMMf16_MEMf16_IMM8_AVX512` — `VMINMAXSH`
- `VMINMAXSH_XMMf16_MASKmskw_XMMf16_XMMf16_IMM8_AVX512` — `VMINMAXSH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINMAXSS

`VMINMAXSS` selects maxima of corresponding a scalar single-precision floating-point element and writes the lane-wise result. The pinned XED inventory represents it with 3 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX512_MINMAX_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM IMM`; `XMM MASK1 XMM XMM IMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINMAXSS_XMMf32_MASKmskw_XMMf32_MEMf32_IMM8_AVX512` — `VMINMAXSS`
- `VMINMAXSS_XMMf32_MASKmskw_XMMf32_XMMf32_IMM8_AVX512` — `VMINMAXSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINPD

`VMINPD` selects minima of corresponding packed double-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 11 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINPD_XMMdq_XMMdq_MEMdq` — `VMINPD`
- `VMINPD_XMMdq_XMMdq_XMMdq` — `VMINPD`
- `VMINPD_XMMf64_MASKmskw_XMMf64_MEMf64_AVX512` — `VMINPD`
- `VMINPD_XMMf64_MASKmskw_XMMf64_XMMf64_AVX512` — `VMINPD`
- `VMINPD_YMMf64_MASKmskw_YMMf64_MEMf64_AVX512` — `VMINPD`
- `VMINPD_YMMf64_MASKmskw_YMMf64_YMMf64_AVX512` — `VMINPD`
- `VMINPD_YMMqq_YMMqq_MEMqq` — `VMINPD`
- `VMINPD_YMMqq_YMMqq_YMMqq` — `VMINPD`
- `VMINPD_ZMMf64_MASKmskw_ZMMf64_MEMf64_AVX512` — `VMINPD`
- `VMINPD_ZMMf64_MASKmskw_ZMMf64_ZMMf64_AVX512` — `VMINPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINPH

`VMINPH` selects minima of corresponding packed IEEE binary16 floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 7 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `FP16`
- ISA set(s): `AVX512_FP16_128`, `AVX512_FP16_256`, `AVX512_FP16_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `YMM MASK1 YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINPH_XMMf16_MASKmskw_XMMf16_MEMf16_AVX512` — `VMINPH`
- `VMINPH_XMMf16_MASKmskw_XMMf16_XMMf16_AVX512` — `VMINPH`
- `VMINPH_YMMf16_MASKmskw_YMMf16_MEMf16_AVX512` — `VMINPH`
- `VMINPH_YMMf16_MASKmskw_YMMf16_YMMf16_AVX512` — `VMINPH`
- `VMINPH_ZMMf16_MASKmskw_ZMMf16_MEMf16_AVX512` — `VMINPH`
- `VMINPH_ZMMf16_MASKmskw_ZMMf16_ZMMf16_AVX512` — `VMINPH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINPS

`VMINPS` selects minima of corresponding packed single-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 11 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINPS_XMMdq_XMMdq_MEMdq` — `VMINPS`
- `VMINPS_XMMdq_XMMdq_XMMdq` — `VMINPS`
- `VMINPS_XMMf32_MASKmskw_XMMf32_MEMf32_AVX512` — `VMINPS`
- `VMINPS_XMMf32_MASKmskw_XMMf32_XMMf32_AVX512` — `VMINPS`
- `VMINPS_YMMf32_MASKmskw_YMMf32_MEMf32_AVX512` — `VMINPS`
- `VMINPS_YMMf32_MASKmskw_YMMf32_YMMf32_AVX512` — `VMINPS`
- `VMINPS_YMMqq_YMMqq_MEMqq` — `VMINPS`
- `VMINPS_YMMqq_YMMqq_YMMqq` — `VMINPS`
- `VMINPS_ZMMf32_MASKmskw_ZMMf32_MEMf32_AVX512` — `VMINPS`
- `VMINPS_ZMMf32_MASKmskw_ZMMf32_ZMMf32_AVX512` — `VMINPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINSD

`VMINSD` selects minima of corresponding a scalar double-precision floating-point element and writes the lane-wise result. The pinned XED inventory represents it with 5 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINSD_XMMdq_XMMdq_MEMq` — `VMINSD`
- `VMINSD_XMMdq_XMMdq_XMMq` — `VMINSD`
- `VMINSD_XMMf64_MASKmskw_XMMf64_MEMf64_AVX512` — `VMINSD`
- `VMINSD_XMMf64_MASKmskw_XMMf64_XMMf64_AVX512` — `VMINSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINSH

`VMINSH` selects minima of corresponding a scalar IEEE binary16 floating-point element and writes the lane-wise result. The pinned XED inventory represents it with 3 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `FP16`
- ISA set(s): `AVX512_FP16_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINSH_XMMf16_MASKmskw_XMMf16_MEMf16_AVX512` — `VMINSH`
- `VMINSH_XMMf16_MASKmskw_XMMf16_XMMf16_AVX512` — `VMINSH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMINSS

`VMINSS` selects minima of corresponding a scalar single-precision floating-point element and writes the lane-wise result. The pinned XED inventory represents it with 5 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMINSS_XMMdq_XMMdq_MEMd` — `VMINSS`
- `VMINSS_XMMdq_XMMdq_XMMd` — `VMINSS`
- `VMINSS_XMMf32_MASKmskw_XMMf32_MEMf32_AVX512` — `VMINSS`
- `VMINSS_XMMf32_MASKmskw_XMMf32_XMMf32_AVX512` — `VMINSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMLAUNCH

`VMLAUNCH` enters a guest from a not-yet-launched VM control structure. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMLAUNCH` — `VMLAUNCH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMLOAD

`VMLOAD` loads virtualization control or guest-state information. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SVM`
- XED category/categories: `SYSTEM`
- ISA set(s): `SVM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `ArAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMLOAD_ArAX` — `VMLOAD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMMCALL

`VMMCALL` transfers from guest context to a hypervisor-defined service through the architecture's virtualization call mechanism. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SVM`
- XED category/categories: `SYSTEM`
- ISA set(s): `SVM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMMCALL` — `VMMCALL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVAPD

`VMOVAPD` copies packed double-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 20 normalized encoding records and 17 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVAPD_MEMdq_XMMdq` — `VMOVAPD`
- `VMOVAPD_MEMf64_MASKmskw_XMMf64_AVX512` — `VMOVAPD`
- `VMOVAPD_MEMf64_MASKmskw_YMMf64_AVX512` — `VMOVAPD`
- `VMOVAPD_MEMf64_MASKmskw_ZMMf64_AVX512` — `VMOVAPD`
- `VMOVAPD_MEMqq_YMMqq` — `VMOVAPD`
- `VMOVAPD_XMMdq_MEMdq` — `VMOVAPD`
- `VMOVAPD_XMMdq_XMMdq_28` — `VMOVAPD`
- `VMOVAPD_XMMdq_XMMdq_29` — `VMOVAPD`
- `VMOVAPD_XMMf64_MASKmskw_MEMf64_AVX512` — `VMOVAPD`
- `VMOVAPD_XMMf64_MASKmskw_XMMf64_AVX512` — `VMOVAPD`
- `VMOVAPD_YMMf64_MASKmskw_MEMf64_AVX512` — `VMOVAPD`
- `VMOVAPD_YMMf64_MASKmskw_YMMf64_AVX512` — `VMOVAPD`
- … 5 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVAPS

`VMOVAPS` copies packed single-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 20 normalized encoding records and 17 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVAPS_MEMdq_XMMdq` — `VMOVAPS`
- `VMOVAPS_MEMf32_MASKmskw_XMMf32_AVX512` — `VMOVAPS`
- `VMOVAPS_MEMf32_MASKmskw_YMMf32_AVX512` — `VMOVAPS`
- `VMOVAPS_MEMf32_MASKmskw_ZMMf32_AVX512` — `VMOVAPS`
- `VMOVAPS_MEMqq_YMMqq` — `VMOVAPS`
- `VMOVAPS_XMMdq_MEMdq` — `VMOVAPS`
- `VMOVAPS_XMMdq_XMMdq_28` — `VMOVAPS`
- `VMOVAPS_XMMdq_XMMdq_29` — `VMOVAPS`
- `VMOVAPS_XMMf32_MASKmskw_MEMf32_AVX512` — `VMOVAPS`
- `VMOVAPS_XMMf32_MASKmskw_XMMf32_AVX512` — `VMOVAPS`
- `VMOVAPS_YMMf32_MASKmskw_MEMf32_AVX512` — `VMOVAPS`
- `VMOVAPS_YMMf32_MASKmskw_YMMf32_AVX512` — `VMOVAPS`
- … 5 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVD

`VMOVD` copies 32-bit doubleword elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 20 normalized encoding records and 11 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128N`, `AVX512_MOVZXC_128`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 XMM`; `MEM XMM`; `VGPR32 XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVD_GPR32d_XMMd` — `VMOVD`
- `VMOVD_GPR32u32_XMMu32_AVX512` — `VMOVD`
- `VMOVD_MEMd_XMMd` — `VMOVD`
- `VMOVD_MEMu32_XMMu32_AVX512` — `VMOVD`
- `VMOVD_MEMu32_XMMu32_AVX512_MOVZXC` — `VMOVD`
- `VMOVD_XMMdq_GPR32d` — `VMOVD`
- `VMOVD_XMMdq_MEMd` — `VMOVD`
- `VMOVD_XMMu32_GPR32u32_AVX512` — `VMOVD`
- `VMOVD_XMMu32_MEMu32_AVX512` — `VMOVD`
- `VMOVD_XMMu32_MEMu32_AVX512_MOVZXC` — `VMOVD`
- `VMOVD_XMMu32_XMMu32_AVX512_MOVZXC` — `VMOVD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVDDUP

`VMOVDDUP` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `XMM MASK1 XMM`; `XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVDDUP_XMMdq_MEMq` — `VMOVDDUP`
- `VMOVDDUP_XMMdq_XMMq` — `VMOVDDUP`
- `VMOVDDUP_XMMf64_MASKmskw_MEMf64_AVX512` — `VMOVDDUP`
- `VMOVDDUP_XMMf64_MASKmskw_XMMf64_AVX512` — `VMOVDDUP`
- `VMOVDDUP_YMMf64_MASKmskw_MEMf64_AVX512` — `VMOVDDUP`
- `VMOVDDUP_YMMf64_MASKmskw_YMMf64_AVX512` — `VMOVDDUP`
- `VMOVDDUP_YMMqq_MEMqq` — `VMOVDDUP`
- `VMOVDDUP_YMMqq_YMMqq` — `VMOVDDUP`
- `VMOVDDUP_ZMMf64_MASKmskw_MEMf64_AVX512` — `VMOVDDUP`
- `VMOVDDUP_ZMMf64_MASKmskw_ZMMf64_AVX512` — `VMOVDDUP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVDQA

`VMOVDQA` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 8 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM`; `MEM YMM`; `XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVDQA_MEMdq_XMMdq` — `VMOVDQA`
- `VMOVDQA_MEMqq_YMMqq` — `VMOVDQA`
- `VMOVDQA_XMMdq_MEMdq` — `VMOVDQA`
- `VMOVDQA_XMMdq_XMMdq_6F` — `VMOVDQA`
- `VMOVDQA_XMMdq_XMMdq_7F` — `VMOVDQA`
- `VMOVDQA_YMMqq_MEMqq` — `VMOVDQA`
- `VMOVDQA_YMMqq_YMMqq_6F` — `VMOVDQA`
- `VMOVDQA_YMMqq_YMMqq_7F` — `VMOVDQA`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVDQA32

`VMOVDQA32` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 12 normalized encoding records and 9 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVDQA32_MEMu32_MASKmskw_XMMu32_AVX512` — `VMOVDQA32`
- `VMOVDQA32_MEMu32_MASKmskw_YMMu32_AVX512` — `VMOVDQA32`
- `VMOVDQA32_MEMu32_MASKmskw_ZMMu32_AVX512` — `VMOVDQA32`
- `VMOVDQA32_XMMu32_MASKmskw_MEMu32_AVX512` — `VMOVDQA32`
- `VMOVDQA32_XMMu32_MASKmskw_XMMu32_AVX512` — `VMOVDQA32`
- `VMOVDQA32_YMMu32_MASKmskw_MEMu32_AVX512` — `VMOVDQA32`
- `VMOVDQA32_YMMu32_MASKmskw_YMMu32_AVX512` — `VMOVDQA32`
- `VMOVDQA32_ZMMu32_MASKmskw_MEMu32_AVX512` — `VMOVDQA32`
- `VMOVDQA32_ZMMu32_MASKmskw_ZMMu32_AVX512` — `VMOVDQA32`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVDQA64

`VMOVDQA64` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 12 normalized encoding records and 9 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVDQA64_MEMu64_MASKmskw_XMMu64_AVX512` — `VMOVDQA64`
- `VMOVDQA64_MEMu64_MASKmskw_YMMu64_AVX512` — `VMOVDQA64`
- `VMOVDQA64_MEMu64_MASKmskw_ZMMu64_AVX512` — `VMOVDQA64`
- `VMOVDQA64_XMMu64_MASKmskw_MEMu64_AVX512` — `VMOVDQA64`
- `VMOVDQA64_XMMu64_MASKmskw_XMMu64_AVX512` — `VMOVDQA64`
- `VMOVDQA64_YMMu64_MASKmskw_MEMu64_AVX512` — `VMOVDQA64`
- `VMOVDQA64_YMMu64_MASKmskw_YMMu64_AVX512` — `VMOVDQA64`
- `VMOVDQA64_ZMMu64_MASKmskw_MEMu64_AVX512` — `VMOVDQA64`
- `VMOVDQA64_ZMMu64_MASKmskw_ZMMu64_AVX512` — `VMOVDQA64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVDQU

`VMOVDQU` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 8 normalized encoding records and 8 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM`; `MEM YMM`; `XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVDQU_MEMdq_XMMdq` — `VMOVDQU`
- `VMOVDQU_MEMqq_YMMqq` — `VMOVDQU`
- `VMOVDQU_XMMdq_MEMdq` — `VMOVDQU`
- `VMOVDQU_XMMdq_XMMdq_6F` — `VMOVDQU`
- `VMOVDQU_XMMdq_XMMdq_7F` — `VMOVDQU`
- `VMOVDQU_YMMqq_MEMqq` — `VMOVDQU`
- `VMOVDQU_YMMqq_YMMqq_6F` — `VMOVDQU`
- `VMOVDQU_YMMqq_YMMqq_7F` — `VMOVDQU`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVDQU16

`VMOVDQU16` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 12 normalized encoding records and 9 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX512BW_128`, `AVX512BW_256`, `AVX512BW_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVDQU16_MEMu16_MASKmskw_XMMu16_AVX512` — `VMOVDQU16`
- `VMOVDQU16_MEMu16_MASKmskw_YMMu16_AVX512` — `VMOVDQU16`
- `VMOVDQU16_MEMu16_MASKmskw_ZMMu16_AVX512` — `VMOVDQU16`
- `VMOVDQU16_XMMu16_MASKmskw_MEMu16_AVX512` — `VMOVDQU16`
- `VMOVDQU16_XMMu16_MASKmskw_XMMu16_AVX512` — `VMOVDQU16`
- `VMOVDQU16_YMMu16_MASKmskw_MEMu16_AVX512` — `VMOVDQU16`
- `VMOVDQU16_YMMu16_MASKmskw_YMMu16_AVX512` — `VMOVDQU16`
- `VMOVDQU16_ZMMu16_MASKmskw_MEMu16_AVX512` — `VMOVDQU16`
- `VMOVDQU16_ZMMu16_MASKmskw_ZMMu16_AVX512` — `VMOVDQU16`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVDQU32

`VMOVDQU32` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 12 normalized encoding records and 9 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVDQU32_MEMu32_MASKmskw_XMMu32_AVX512` — `VMOVDQU32`
- `VMOVDQU32_MEMu32_MASKmskw_YMMu32_AVX512` — `VMOVDQU32`
- `VMOVDQU32_MEMu32_MASKmskw_ZMMu32_AVX512` — `VMOVDQU32`
- `VMOVDQU32_XMMu32_MASKmskw_MEMu32_AVX512` — `VMOVDQU32`
- `VMOVDQU32_XMMu32_MASKmskw_XMMu32_AVX512` — `VMOVDQU32`
- `VMOVDQU32_YMMu32_MASKmskw_MEMu32_AVX512` — `VMOVDQU32`
- `VMOVDQU32_YMMu32_MASKmskw_YMMu32_AVX512` — `VMOVDQU32`
- `VMOVDQU32_ZMMu32_MASKmskw_MEMu32_AVX512` — `VMOVDQU32`
- `VMOVDQU32_ZMMu32_MASKmskw_ZMMu32_AVX512` — `VMOVDQU32`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVDQU64

`VMOVDQU64` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 12 normalized encoding records and 9 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVDQU64_MEMu64_MASKmskw_XMMu64_AVX512` — `VMOVDQU64`
- `VMOVDQU64_MEMu64_MASKmskw_YMMu64_AVX512` — `VMOVDQU64`
- `VMOVDQU64_MEMu64_MASKmskw_ZMMu64_AVX512` — `VMOVDQU64`
- `VMOVDQU64_XMMu64_MASKmskw_MEMu64_AVX512` — `VMOVDQU64`
- `VMOVDQU64_XMMu64_MASKmskw_XMMu64_AVX512` — `VMOVDQU64`
- `VMOVDQU64_YMMu64_MASKmskw_MEMu64_AVX512` — `VMOVDQU64`
- `VMOVDQU64_YMMu64_MASKmskw_YMMu64_AVX512` — `VMOVDQU64`
- `VMOVDQU64_ZMMu64_MASKmskw_MEMu64_AVX512` — `VMOVDQU64`
- `VMOVDQU64_ZMMu64_MASKmskw_ZMMu64_AVX512` — `VMOVDQU64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVDQU8

`VMOVDQU8` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 12 normalized encoding records and 9 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX512BW_128`, `AVX512BW_256`, `AVX512BW_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVDQU8_MEMu8_MASKmskw_XMMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_MEMu8_MASKmskw_YMMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_MEMu8_MASKmskw_ZMMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_XMMu8_MASKmskw_MEMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_XMMu8_MASKmskw_XMMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_YMMu8_MASKmskw_MEMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_YMMu8_MASKmskw_YMMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_ZMMu8_MASKmskw_MEMu8_AVX512` — `VMOVDQU8`
- `VMOVDQU8_ZMMu8_MASKmskw_ZMMu8_AVX512` — `VMOVDQU8`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVHLPS

`VMOVHLPS` copies packed single-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128N`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVHLPS_XMMdq_XMMdq_XMMdq` — `VMOVHLPS`
- `VMOVHLPS_XMMf32_XMMf32_XMMf32_AVX512` — `VMOVHLPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVHPD

`VMOVHPD` copies packed double-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128N`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM`; `XMM XMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVHPD_MEMf64_XMMf64_AVX512` — `VMOVHPD`
- `VMOVHPD_MEMq_XMMdq` — `VMOVHPD`
- `VMOVHPD_XMMdq_XMMq_MEMq` — `VMOVHPD`
- `VMOVHPD_XMMf64_XMMf64_MEMf64_AVX512` — `VMOVHPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVHPS

`VMOVHPS` copies packed single-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128N`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM`; `XMM XMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVHPS_MEMf32_XMMf32_AVX512` — `VMOVHPS`
- `VMOVHPS_MEMq_XMMdq` — `VMOVHPS`
- `VMOVHPS_XMMdq_XMMq_MEMq` — `VMOVHPS`
- `VMOVHPS_XMMf32_XMMf32_MEMf32_AVX512` — `VMOVHPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVLHPS

`VMOVLHPS` copies packed single-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128N`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVLHPS_XMMdq_XMMq_XMMq` — `VMOVLHPS`
- `VMOVLHPS_XMMf32_XMMf32_XMMf32_AVX512` — `VMOVLHPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVLPD

`VMOVLPD` copies packed double-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128N`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM`; `XMM XMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVLPD_MEMf64_XMMf64_AVX512` — `VMOVLPD`
- `VMOVLPD_MEMq_XMMq` — `VMOVLPD`
- `VMOVLPD_XMMdq_XMMdq_MEMq` — `VMOVLPD`
- `VMOVLPD_XMMf64_XMMf64_MEMf64_AVX512` — `VMOVLPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVLPS

`VMOVLPS` copies packed single-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128N`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM`; `XMM XMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVLPS_MEMf32_XMMf32_AVX512` — `VMOVLPS`
- `VMOVLPS_MEMq_XMMq` — `VMOVLPS`
- `VMOVLPS_XMMdq_XMMdq_MEMq` — `VMOVLPS`
- `VMOVLPS_XMMf32_XMMf32_MEMf32_AVX512` — `VMOVLPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVMSKPD

`VMOVMSKPD` extracts vector sign bits and packs them into an integer mask. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 XMM`; `VGPR32 YMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVMSKPD_GPR32d_XMMdq` — `VMOVMSKPD`
- `VMOVMSKPD_GPR32d_YMMqq` — `VMOVMSKPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVMSKPS

`VMOVMSKPS` extracts vector sign bits and packs them into an integer mask. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `VGPR32 XMM`; `VGPR32 YMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVMSKPS_GPR32d_XMMdq` — `VMOVMSKPS`
- `VMOVMSKPS_GPR32d_YMMqq` — `VMOVMSKPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this can be considered by a feature-aware optimization pass when its vector, arithmetic, or bit-level semantics match the typed IR. Presence in the complete inventory does not imply universal availability.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVNTDQ

`VMOVNTDQ` moves double-quadword vector data using non-temporal memory semantics intended for streaming data. The pinned XED inventory represents it with 5 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM`; `MEM YMM`; `MEM ZMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVNTDQ_MEMdq_XMMdq` — `VMOVNTDQ`
- `VMOVNTDQ_MEMqq_YMMqq` — `VMOVNTDQ`
- `VMOVNTDQ_MEMu32_XMMu32_AVX512` — `VMOVNTDQ`
- `VMOVNTDQ_MEMu32_YMMu32_AVX512` — `VMOVNTDQ`
- `VMOVNTDQ_MEMu32_ZMMu32_AVX512` — `VMOVNTDQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVNTDQA

`VMOVNTDQA` moves its encoded scalar or vector elements using non-temporal memory semantics intended for streaming data. The pinned XED inventory represents it with 5 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX2`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MEM`; `YMM MEM`; `ZMM MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVNTDQA_XMMdq_MEMdq` — `VMOVNTDQA`
- `VMOVNTDQA_XMMu32_MEMu32_AVX512` — `VMOVNTDQA`
- `VMOVNTDQA_YMMqq_MEMqq` — `VMOVNTDQA`
- `VMOVNTDQA_YMMu32_MEMu32_AVX512` — `VMOVNTDQA`
- `VMOVNTDQA_ZMMu32_MEMu32_AVX512` — `VMOVNTDQA`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVNTPD

`VMOVNTPD` moves packed double-precision floating-point elements using non-temporal memory semantics intended for streaming data. The pinned XED inventory represents it with 5 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM`; `MEM YMM`; `MEM ZMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVNTPD_MEMdq_XMMdq` — `VMOVNTPD`
- `VMOVNTPD_MEMf64_XMMf64_AVX512` — `VMOVNTPD`
- `VMOVNTPD_MEMf64_YMMf64_AVX512` — `VMOVNTPD`
- `VMOVNTPD_MEMf64_ZMMf64_AVX512` — `VMOVNTPD`
- `VMOVNTPD_MEMqq_YMMqq` — `VMOVNTPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVNTPS

`VMOVNTPS` moves packed single-precision floating-point elements using non-temporal memory semantics intended for streaming data. The pinned XED inventory represents it with 5 normalized encoding records and 5 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM XMM`; `MEM YMM`; `MEM ZMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVNTPS_MEMdq_XMMdq` — `VMOVNTPS`
- `VMOVNTPS_MEMf32_XMMf32_AVX512` — `VMOVNTPS`
- `VMOVNTPS_MEMf32_YMMf32_AVX512` — `VMOVNTPS`
- `VMOVNTPS_MEMf32_ZMMf32_AVX512` — `VMOVNTPS`
- `VMOVNTPS_MEMqq_YMMqq` — `VMOVNTPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVQ

`VMOVQ` copies 64-bit quadword elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 16 normalized encoding records and 13 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128N`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR64 XMM`; `MEM XMM`; `VGPR64 XMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVQ_GPR64q_XMMq` — `VMOVQ`
- `VMOVQ_GPR64u64_XMMu64_AVX512` — `VMOVQ`
- `VMOVQ_MEMq_XMMq_7E` — `VMOVQ`
- `VMOVQ_MEMq_XMMq_D6` — `VMOVQ`
- `VMOVQ_MEMu64_XMMu64_AVX512` — `VMOVQ`
- `VMOVQ_XMMdq_GPR64q` — `VMOVQ`
- `VMOVQ_XMMdq_MEMq_6E` — `VMOVQ`
- `VMOVQ_XMMdq_MEMq_7E` — `VMOVQ`
- `VMOVQ_XMMdq_XMMq_7E` — `VMOVQ`
- `VMOVQ_XMMdq_XMMq_D6` — `VMOVQ`
- `VMOVQ_XMMu64_GPR64u64_AVX512` — `VMOVQ`
- `VMOVQ_XMMu64_MEMu64_AVX512` — `VMOVQ`
- … 1 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVRSB

`VMOVRSB` copies byte elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX10_MOVRS_128`, `AVX10_MOVRS_256`, `AVX10_MOVRS_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `YMM MASK1 MEM`; `ZMM MASK1 MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVRSB_XMMu8_MASKmskw_MEMu8_AVX512` — `VMOVRSB`
- `VMOVRSB_YMMu8_MASKmskw_MEMu8_AVX512` — `VMOVRSB`
- `VMOVRSB_ZMMu8_MASKmskw_MEMu8_AVX512` — `VMOVRSB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVRSD

`VMOVRSD` copies a scalar double-precision floating-point element between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX10_MOVRS_128`, `AVX10_MOVRS_256`, `AVX10_MOVRS_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `YMM MASK1 MEM`; `ZMM MASK1 MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVRSD_XMMu32_MASKmskw_MEMu32_AVX512` — `VMOVRSD`
- `VMOVRSD_YMMu32_MASKmskw_MEMu32_AVX512` — `VMOVRSD`
- `VMOVRSD_ZMMu32_MASKmskw_MEMu32_AVX512` — `VMOVRSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVRSQ

`VMOVRSQ` copies 64-bit quadword elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX10_MOVRS_128`, `AVX10_MOVRS_256`, `AVX10_MOVRS_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `YMM MASK1 MEM`; `ZMM MASK1 MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVRSQ_XMMu64_MASKmskw_MEMu64_AVX512` — `VMOVRSQ`
- `VMOVRSQ_YMMu64_MASKmskw_MEMu64_AVX512` — `VMOVRSQ`
- `VMOVRSQ_ZMMu64_MASKmskw_MEMu64_AVX512` — `VMOVRSQ`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVRSW

`VMOVRSW` copies 16-bit word elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX10_MOVRS_128`, `AVX10_MOVRS_256`, `AVX10_MOVRS_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `YMM MASK1 MEM`; `ZMM MASK1 MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVRSW_XMMu16_MASKmskw_MEMu16_AVX512` — `VMOVRSW`
- `VMOVRSW_YMMu16_MASKmskw_MEMu16_AVX512` — `VMOVRSW`
- `VMOVRSW_ZMMu16_MASKmskw_MEMu16_AVX512` — `VMOVRSW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVSD

`VMOVSD` copies a scalar double-precision floating-point element between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 8 normalized encoding records and 7 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM XMM`; `XMM MASK1 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVSD_MEMf64_MASKmskw_XMMf64_AVX512` — `VMOVSD`
- `VMOVSD_MEMq_XMMq` — `VMOVSD`
- `VMOVSD_XMMdq_MEMq` — `VMOVSD`
- `VMOVSD_XMMdq_XMMdq_XMMq_10` — `VMOVSD`
- `VMOVSD_XMMdq_XMMdq_XMMq_11` — `VMOVSD`
- `VMOVSD_XMMf64_MASKmskw_MEMf64_AVX512` — `VMOVSD`
- `VMOVSD_XMMf64_MASKmskw_XMMf64_XMMf64_AVX512` — `VMOVSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVSH

`VMOVSH` copies a scalar IEEE binary16 floating-point element between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 4 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX512_FP16_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `XMM MASK1 MEM`; `XMM MASK1 XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVSH_MEMf16_MASKmskw_XMMf16_AVX512` — `VMOVSH`
- `VMOVSH_XMMf16_MASKmskw_MEMf16_AVX512` — `VMOVSH`
- `VMOVSH_XMMf16_MASKmskw_XMMf16_XMMf16_AVX512` — `VMOVSH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVSHDUP

`VMOVSHDUP` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `XMM MASK1 XMM`; `XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVSHDUP_XMMdq_MEMdq` — `VMOVSHDUP`
- `VMOVSHDUP_XMMdq_XMMdq` — `VMOVSHDUP`
- `VMOVSHDUP_XMMf32_MASKmskw_MEMf32_AVX512` — `VMOVSHDUP`
- `VMOVSHDUP_XMMf32_MASKmskw_XMMf32_AVX512` — `VMOVSHDUP`
- `VMOVSHDUP_YMMf32_MASKmskw_MEMf32_AVX512` — `VMOVSHDUP`
- `VMOVSHDUP_YMMf32_MASKmskw_YMMf32_AVX512` — `VMOVSHDUP`
- `VMOVSHDUP_YMMqq_MEMqq` — `VMOVSHDUP`
- `VMOVSHDUP_YMMqq_YMMqq` — `VMOVSHDUP`
- `VMOVSHDUP_ZMMf32_MASKmskw_MEMf32_AVX512` — `VMOVSHDUP`
- `VMOVSHDUP_ZMMf32_MASKmskw_ZMMf32_AVX512` — `VMOVSHDUP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVSLDUP

`VMOVSLDUP` copies its encoded scalar or vector elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 MEM`; `XMM MASK1 XMM`; `XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVSLDUP_XMMdq_MEMdq` — `VMOVSLDUP`
- `VMOVSLDUP_XMMdq_XMMdq` — `VMOVSLDUP`
- `VMOVSLDUP_XMMf32_MASKmskw_MEMf32_AVX512` — `VMOVSLDUP`
- `VMOVSLDUP_XMMf32_MASKmskw_XMMf32_AVX512` — `VMOVSLDUP`
- `VMOVSLDUP_YMMf32_MASKmskw_MEMf32_AVX512` — `VMOVSLDUP`
- `VMOVSLDUP_YMMf32_MASKmskw_YMMf32_AVX512` — `VMOVSLDUP`
- `VMOVSLDUP_YMMqq_MEMqq` — `VMOVSLDUP`
- `VMOVSLDUP_YMMqq_YMMqq` — `VMOVSLDUP`
- `VMOVSLDUP_ZMMf32_MASKmskw_MEMf32_AVX512` — `VMOVSLDUP`
- `VMOVSLDUP_ZMMf32_MASKmskw_ZMMf32_AVX512` — `VMOVSLDUP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVSS

`VMOVSS` copies a scalar single-precision floating-point element between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 8 normalized encoding records and 7 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM XMM`; `XMM MASK1 MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVSS_MEMd_XMMd` — `VMOVSS`
- `VMOVSS_MEMf32_MASKmskw_XMMf32_AVX512` — `VMOVSS`
- `VMOVSS_XMMdq_MEMd` — `VMOVSS`
- `VMOVSS_XMMdq_XMMdq_XMMd_10` — `VMOVSS`
- `VMOVSS_XMMdq_XMMdq_XMMd_11` — `VMOVSS`
- `VMOVSS_XMMf32_MASKmskw_MEMf32_AVX512` — `VMOVSS`
- `VMOVSS_XMMf32_MASKmskw_XMMf32_XMMf32_AVX512` — `VMOVSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVUPD

`VMOVUPD` copies packed double-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 20 normalized encoding records and 17 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVUPD_MEMdq_XMMdq` — `VMOVUPD`
- `VMOVUPD_MEMf64_MASKmskw_XMMf64_AVX512` — `VMOVUPD`
- `VMOVUPD_MEMf64_MASKmskw_YMMf64_AVX512` — `VMOVUPD`
- `VMOVUPD_MEMf64_MASKmskw_ZMMf64_AVX512` — `VMOVUPD`
- `VMOVUPD_MEMqq_YMMqq` — `VMOVUPD`
- `VMOVUPD_XMMdq_MEMdq` — `VMOVUPD`
- `VMOVUPD_XMMdq_XMMdq_10` — `VMOVUPD`
- `VMOVUPD_XMMdq_XMMdq_11` — `VMOVUPD`
- `VMOVUPD_XMMf64_MASKmskw_MEMf64_AVX512` — `VMOVUPD`
- `VMOVUPD_XMMf64_MASKmskw_XMMf64_AVX512` — `VMOVUPD`
- `VMOVUPD_YMMf64_MASKmskw_MEMf64_AVX512` — `VMOVUPD`
- `VMOVUPD_YMMf64_MASKmskw_YMMf64_AVX512` — `VMOVUPD`
- … 5 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVUPS

`VMOVUPS` copies packed single-precision floating-point elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 20 normalized encoding records and 17 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM MASK1 XMM`; `MEM MASK1 YMM`; `MEM MASK1 ZMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVUPS_MEMdq_XMMdq` — `VMOVUPS`
- `VMOVUPS_MEMf32_MASKmskw_XMMf32_AVX512` — `VMOVUPS`
- `VMOVUPS_MEMf32_MASKmskw_YMMf32_AVX512` — `VMOVUPS`
- `VMOVUPS_MEMf32_MASKmskw_ZMMf32_AVX512` — `VMOVUPS`
- `VMOVUPS_MEMqq_YMMqq` — `VMOVUPS`
- `VMOVUPS_XMMdq_MEMdq` — `VMOVUPS`
- `VMOVUPS_XMMdq_XMMdq_10` — `VMOVUPS`
- `VMOVUPS_XMMdq_XMMdq_11` — `VMOVUPS`
- `VMOVUPS_XMMf32_MASKmskw_MEMf32_AVX512` — `VMOVUPS`
- `VMOVUPS_XMMf32_MASKmskw_XMMf32_AVX512` — `VMOVUPS`
- `VMOVUPS_YMMf32_MASKmskw_MEMf32_AVX512` — `VMOVUPS`
- `VMOVUPS_YMMf32_MASKmskw_YMMf32_AVX512` — `VMOVUPS`
- … 5 additional concrete forms in `generated/xed-instructions.tsv`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMOVW

`VMOVW` copies 16-bit word elements between the register and memory forms allowed by its alignment and masking rules. The pinned XED inventory represents it with 8 normalized encoding records and 7 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `DATAXFER`
- ISA set(s): `AVX512_FP16_128N`, `AVX512_MOVZXC_128`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR32 XMM`; `MEM XMM`; `XMM GPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMOVW_GPR32f16_XMMf16_AVX512` — `VMOVW`
- `VMOVW_MEMf16_XMMf16_AVX512` — `VMOVW`
- `VMOVW_MEMu16_XMMu16_AVX512_MOVZXC` — `VMOVW`
- `VMOVW_XMMf16_GPR32f16_AVX512` — `VMOVW`
- `VMOVW_XMMf16_MEMf16_AVX512` — `VMOVW`
- `VMOVW_XMMu16_MEMu16_AVX512_MOVZXC` — `VMOVW`
- `VMOVW_XMMu16_XMMu16_AVX512_MOVZXC` — `VMOVW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMPSADBW

`VMPSADBW` computes grouped sums of absolute differences between source elements. The pinned XED inventory represents it with 10 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX2`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX2`, `AVX512`
- ISA set(s): `AVX`, `AVX2`, `AVX512_MEDIAX_128`, `AVX512_MEDIAX_256`, `AVX512_MEDIAX_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM IMM`; `XMM MASK1 XMM XMM IMM`; `XMM XMM MEM IMM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMPSADBW_XMMdq_XMMdq_MEMdq_IMMb` — `VMPSADBW`
- `VMPSADBW_XMMdq_XMMdq_XMMdq_IMMb` — `VMPSADBW`
- `VMPSADBW_XMMu16_MASKmskw_XMMu8_MEMu8_IMM8_AVX512` — `VMPSADBW`
- `VMPSADBW_XMMu16_MASKmskw_XMMu8_XMMu8_IMM8_AVX512` — `VMPSADBW`
- `VMPSADBW_YMMqq_YMMqq_MEMqq_IMMb` — `VMPSADBW`
- `VMPSADBW_YMMqq_YMMqq_YMMqq_IMMb` — `VMPSADBW`
- `VMPSADBW_YMMu16_MASKmskw_YMMu8_MEMu8_IMM8_AVX512` — `VMPSADBW`
- `VMPSADBW_YMMu16_MASKmskw_YMMu8_YMMu8_IMM8_AVX512` — `VMPSADBW`
- `VMPSADBW_ZMMu16_MASKmskw_ZMMu8_MEMu8_IMM8_AVX512` — `VMPSADBW`
- `VMPSADBW_ZMMu16_MASKmskw_ZMMu8_ZMMu8_IMM8_AVX512` — `VMPSADBW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMPTRLD

`VMPTRLD` loads the physical address of a VMCS region as the current VMCS pointer after validating the region. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMPTRLD_MEMq` — `VMPTRLD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMPTRST

`VMPTRST` stores the current VMCS pointer's physical address to memory. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMPTRST_MEMq` — `VMPTRST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMREAD

`VMREAD` reads a field from the current virtual-machine control structure. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `GPR32 GPR32`; `GPR64 GPR64`; `MEM GPR32`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMREAD_GPR32_GPR32` — `VMREAD`
- `VMREAD_GPR64_GPR64` — `VMREAD`
- `VMREAD_MEMd_GPR32` — `VMREAD`
- `VMREAD_MEMq_GPR64` — `VMREAD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMRESUME

`VMRESUME` re-enters a previously launched virtual machine. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMRESUME` — `VMRESUME`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMRUN

`VMRUN` enters an AMD SVM guest using the virtual-machine control block whose physical address is supplied in the implicit register. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SVM`
- XED category/categories: `SYSTEM`
- ISA set(s): `SVM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `ArAX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMRUN_ArAX` — `VMRUN`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMSAVE

`VMSAVE` saves virtualization guest or host state. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `SVM`
- XED category/categories: `SYSTEM`
- ISA set(s): `SVM`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMSAVE` — `VMSAVE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMULBF16

`VMULBF16` multiplies corresponding bfloat16 elements and writes the lane-wise result. The pinned XED inventory represents it with 6 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `AVX512`
- ISA set(s): `AVX10_2_BF16_128`, `AVX10_2_BF16_256`, `AVX10_2_BF16_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `YMM MASK1 YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMULBF16_XMMbf16_MASKmskw_XMMbf16_MEMbf16_AVX512` — `VMULBF16`
- `VMULBF16_XMMbf16_MASKmskw_XMMbf16_XMMbf16_AVX512` — `VMULBF16`
- `VMULBF16_YMMbf16_MASKmskw_YMMbf16_MEMbf16_AVX512` — `VMULBF16`
- `VMULBF16_YMMbf16_MASKmskw_YMMbf16_YMMbf16_AVX512` — `VMULBF16`
- `VMULBF16_ZMMbf16_MASKmskw_ZMMbf16_MEMbf16_AVX512` — `VMULBF16`
- `VMULBF16_ZMMbf16_MASKmskw_ZMMbf16_ZMMbf16_AVX512` — `VMULBF16`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMULPD

`VMULPD` multiplies corresponding packed double-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 11 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMULPD_XMMdq_XMMdq_MEMdq` — `VMULPD`
- `VMULPD_XMMdq_XMMdq_XMMdq` — `VMULPD`
- `VMULPD_XMMf64_MASKmskw_XMMf64_MEMf64_AVX512` — `VMULPD`
- `VMULPD_XMMf64_MASKmskw_XMMf64_XMMf64_AVX512` — `VMULPD`
- `VMULPD_YMMf64_MASKmskw_YMMf64_MEMf64_AVX512` — `VMULPD`
- `VMULPD_YMMf64_MASKmskw_YMMf64_YMMf64_AVX512` — `VMULPD`
- `VMULPD_YMMqq_YMMqq_MEMqq` — `VMULPD`
- `VMULPD_YMMqq_YMMqq_YMMqq` — `VMULPD`
- `VMULPD_ZMMf64_MASKmskw_ZMMf64_MEMf64_AVX512` — `VMULPD`
- `VMULPD_ZMMf64_MASKmskw_ZMMf64_ZMMf64_AVX512` — `VMULPD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMULPH

`VMULPH` multiplies corresponding packed IEEE binary16 floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 7 normalized encoding records and 6 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `FP16`
- ISA set(s): `AVX512_FP16_128`, `AVX512_FP16_256`, `AVX512_FP16_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `YMM MASK1 YMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMULPH_XMMf16_MASKmskw_XMMf16_MEMf16_AVX512` — `VMULPH`
- `VMULPH_XMMf16_MASKmskw_XMMf16_XMMf16_AVX512` — `VMULPH`
- `VMULPH_YMMf16_MASKmskw_YMMf16_MEMf16_AVX512` — `VMULPH`
- `VMULPH_YMMf16_MASKmskw_YMMf16_YMMf16_AVX512` — `VMULPH`
- `VMULPH_ZMMf16_MASKmskw_ZMMf16_MEMf16_AVX512` — `VMULPH`
- `VMULPH_ZMMf16_MASKmskw_ZMMf16_ZMMf16_AVX512` — `VMULPH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMULPS

`VMULPS` multiplies corresponding packed single-precision floating-point elements and writes the lane-wise result. The pinned XED inventory represents it with 11 normalized encoding records and 10 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_128`, `AVX512F_256`, `AVX512F_512`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMULPS_XMMdq_XMMdq_MEMdq` — `VMULPS`
- `VMULPS_XMMdq_XMMdq_XMMdq` — `VMULPS`
- `VMULPS_XMMf32_MASKmskw_XMMf32_MEMf32_AVX512` — `VMULPS`
- `VMULPS_XMMf32_MASKmskw_XMMf32_XMMf32_AVX512` — `VMULPS`
- `VMULPS_YMMf32_MASKmskw_YMMf32_MEMf32_AVX512` — `VMULPS`
- `VMULPS_YMMf32_MASKmskw_YMMf32_YMMf32_AVX512` — `VMULPS`
- `VMULPS_YMMqq_YMMqq_MEMqq` — `VMULPS`
- `VMULPS_YMMqq_YMMqq_YMMqq` — `VMULPS`
- `VMULPS_ZMMf32_MASKmskw_ZMMf32_MEMf32_AVX512` — `VMULPS`
- `VMULPS_ZMMf32_MASKmskw_ZMMf32_ZMMf32_AVX512` — `VMULPS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMULSD

`VMULSD` multiplies corresponding a scalar double-precision floating-point element and writes the lane-wise result. The pinned XED inventory represents it with 5 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMULSD_XMMdq_XMMdq_MEMq` — `VMULSD`
- `VMULSD_XMMdq_XMMdq_XMMq` — `VMULSD`
- `VMULSD_XMMf64_MASKmskw_XMMf64_MEMf64_AVX512` — `VMULSD`
- `VMULSD_XMMf64_MASKmskw_XMMf64_XMMf64_AVX512` — `VMULSD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMULSH

`VMULSH` multiplies corresponding a scalar IEEE binary16 floating-point element and writes the lane-wise result. The pinned XED inventory represents it with 3 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX512EVEX`
- XED category/categories: `FP16`
- ISA set(s): `AVX512_FP16_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMULSH_XMMf16_MASKmskw_XMMf16_MEMf16_AVX512` — `VMULSH`
- `VMULSH_XMMf16_MASKmskw_XMMf16_XMMf16_AVX512` — `VMULSH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMULSS

`VMULSS` multiplies corresponding a scalar single-precision floating-point element and writes the lane-wise result. The pinned XED inventory represents it with 5 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AVX`, `AVX512EVEX`
- XED category/categories: `AVX`, `AVX512`
- ISA set(s): `AVX`, `AVX512F_SCALAR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `XMM MASK1 XMM MEM`; `XMM MASK1 XMM XMM`; `XMM XMM MEM`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMULSS_XMMdq_XMMdq_MEMd` — `VMULSS`
- `VMULSS_XMMdq_XMMdq_XMMd` — `VMULSS`
- `VMULSS_XMMf32_MASKmskw_XMMf32_MEMf32_AVX512` — `VMULSS`
- `VMULSS_XMMf32_MASKmskw_XMMf32_XMMf32_AVX512` — `VMULSS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is an optimization-target candidate rather than baseline code generation. Selection should require feature-aware target information and an exact semantic oracle.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMWRITE

`VMWRITE` writes a field in the current virtual-machine control structure. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `GPR32 GPR32`; `GPR32 MEM`; `GPR64 GPR64`; …. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMWRITE_GPR32_GPR32` — `VMWRITE`
- `VMWRITE_GPR32_MEMd` — `VMWRITE`
- `VMWRITE_GPR64_GPR64` — `VMWRITE`
- `VMWRITE_GPR64_MEMq` — `VMWRITE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMXOFF

`VMXOFF` leaves Intel VMX operation on the current logical processor. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMXOFF` — `VMXOFF`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VMXON

`VMXON` enters Intel VMX operation using the VMXON region identified by the operand after validating VMX control requirements. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `VTX`
- XED category/categories: `VTX`
- ISA set(s): `VTX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VMXON_MEMq` — `VMXON`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
