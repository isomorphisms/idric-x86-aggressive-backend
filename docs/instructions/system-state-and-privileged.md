# System, processor state, and privileged operations

This generated bundle contains 62 XED ICLASS reference sections. Each section preserves the instruction-specific semantic prose, availability, architectural effects, representative forms, backend notes, and pinned sources from the per-ICLASS semantic generator.

## ARPL

`ARPL` adjusts the requested privilege level field of a protected-mode segment selector so it is not more privileged than a comparison selector. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286PROTECTED`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR16 GPR16`; `MEM GPR16`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `ARPL_GPR16_GPR16` — `ARPL`
- `ARPL_MEMw_GPR16` — `ARPL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CLFLUSH

`CLFLUSH` invalidates the cache line containing a specified memory address from the coherent cache hierarchy and writes back modified data as required. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CLFSH`
- XED category/categories: `MISC`
- ISA set(s): `CLFSH`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CLFLUSH_MEMmprefetch` — `CLFLUSH`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CLFLUSHOPT

`CLFLUSHOPT` requests cache-line writeback and invalidation like CLFLUSH but with weaker ordering that permits more overlap between multiple flushes. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CLFLUSHOPT`
- XED category/categories: `CLFLUSHOPT`
- ISA set(s): `CLFLUSHOPT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CLFLUSHOPT_MEMmprefetch` — `CLFLUSHOPT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CLI

`CLI` clears the interrupt-enable flag when privilege permits, disabling maskable external interrupts on the current logical processor. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

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

- `CLI` — `CLI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CLTS

`CLTS` clears CR0.TS so x87/SIMD state can be used without triggering the device-not-available exception used by lazy context switching. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CLTS` — `CLTS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CLWB

`CLWB` writes back a modified cache line toward memory without requiring the line to be invalidated from the caches. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `CLWB`
- XED category/categories: `CLWB`
- ISA set(s): `CLWB`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CLWB_MEMmprefetch` — `CLWB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## CPUID

`CPUID` queries processor identification and feature information selected by EAX and, for some leaves, ECX, returning structured capability data in general-purpose registers. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `MISC`
- ISA set(s): `I486REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX EBX ECX EDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `CPUID` — `CPUID`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## HLT

`HLT` halts instruction execution until an enabled interrupt, reset, or another architecturally defined wake event occurs; it is privileged in normal protected execution. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I86`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `HLT` — `HLT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INVD

`INVD` invalidates processor caches without writing modified lines back to memory and is therefore a privileged, destructive cache-management operation. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I486REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INVD` — `INVD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INVLPG

`INVLPG` invalidates the translation-lookaside-buffer entry associated with a linear address for the current address-space context. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I486REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INVLPG_MEMb` — `INVLPG`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INVLPGB

`INVLPGB` invalidates processor-maintained translation or virtualization-caching state selected by its operands. The pinned XED inventory represents it with 2 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AMD_INVLPGB`
- XED category/categories: `SYSTEM`
- ISA set(s): `AMD_INVLPGB`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX EDX ECX`; `RAX EDX ECX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INVLPGB` — `INVLPGB`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## INVPCID

`INVPCID` invalidates selected translation-cache entries using a process-context identifier and an invalidation type. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `INVPCID`
- XED category/categories: `MISC`
- ISA set(s): `APX_F_INVPCID`, `INVPCID`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `GPR32 MEM`; `GPR64 MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `INVPCID_GPR32_MEMdq` — `INVPCID`
- `INVPCID_GPR64_MEMdq` — `INVPCID`
- `INVPCID_GPR64i64_MEMi128_APX` — `INVPCID`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LAR

`LAR` loads access-rights information from a visible segment descriptor into a general-purpose register when privilege and descriptor checks succeed. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286PROTECTED`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRv`; `GPRv MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LAR_GPRv_GPRv` — `LAR`
- `LAR_GPRv_MEMw` — `LAR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LGDT

`LGDT` loads the global descriptor-table register from a memory descriptor. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `GDTR`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LGDT_MEMs` — `LGDT`
- `LGDT_MEMs64` — `LGDT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LIDT

`LIDT` loads the interrupt descriptor-table register from a memory descriptor. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `IDTR`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LIDT_MEMs` — `LIDT`
- `LIDT_MEMs64` — `LIDT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LLDT

`LLDT` loads the local descriptor-table register from a segment selector. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286PROTECTED`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `GPR16`; `MEM`. Representative implicit state: `LDTR`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LLDT_GPR16` — `LLDT`
- `LLDT_MEMw` — `LLDT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LMSW

`LMSW` loads selected low control bits of CR0 from a source operand, a legacy protected-mode control operation. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `GPR16`; `MEM`. Representative implicit state: `CR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LMSW_GPR16` — `LMSW`
- `LMSW_MEMw` — `LMSW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LSL

`LSL` loads a segment or system descriptor's effective limit into a general-purpose register when descriptor and privilege checks succeed. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286PROTECTED`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv GPRz`; `GPRv MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LSL_GPRv_GPRz` — `LSL`
- `LSL_GPRv_MEMw` — `LSL`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## LTR

`LTR` loads the task register from a task-state-segment selector. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286PROTECTED`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `GPR16`; `MEM`. Representative implicit state: `TR`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `LTR_GPR16` — `LTR`
- `LTR_MEMw` — `LTR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MONITOR

`MONITOR` arms hardware monitoring of a memory address for use with MWAIT. The pinned XED inventory represents it with 4 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MONITOR`
- XED category/categories: `MISC`
- ISA set(s): `MONITOR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `AX ECX EDX`; `EAX ECX EDX`; `RAX ECX EDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MONITOR` — `MONITOR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MONITORX

`MONITORX` AMD's extended monitor instruction arms monitoring of a memory address for use with MWAITX. The pinned XED inventory represents it with 4 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MONITORX`
- XED category/categories: `MISC`
- ISA set(s): `MONITORX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `AX ECX EDX`; `EAX ECX EDX`; `RAX ECX EDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MONITORX` — `MONITORX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MWAIT

`MWAIT` enters an optimized processor wait state until an event such as a store to a monitored address or an interrupt wakes execution. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MONITOR`
- XED category/categories: `MISC`
- ISA set(s): `MONITOR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX ECX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MWAIT` — `MWAIT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## MWAITX

`MWAITX` AMD's extended wait instruction sleeps until a monitored event, interrupt, or optional timeout wakes execution. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MONITORX`
- XED category/categories: `MISC`
- ISA set(s): `MONITORX`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX ECX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `MWAITX` — `MWAITX`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PCONFIG

`PCONFIG` invokes a platform-configuration leaf selected by registers, providing a privileged architectural entry point for configuration operations such as key programming. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `PCONFIG`
- XED category/categories: `PCONFIG`
- ISA set(s): `PCONFIG`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX EBX ECX EDX`; `EAX RBX RCX RDX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PCONFIG` — `PCONFIG`
- `PCONFIG64` — `PCONFIG`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PREFETCHIT0

`PREFETCHIT0` issues a prefetch hint for the addressed cache line with the locality or exclusivity preference encoded by the mnemonic. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `ICACHE_PREFETCH`
- XED category/categories: `PREFETCH`
- ISA set(s): `ICACHE_PREFETCH`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PREFETCHIT0_MEMu8` — `PREFETCHIT0`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## PREFETCHIT1

`PREFETCHIT1` issues a prefetch hint for the addressed cache line with the locality or exclusivity preference encoded by the mnemonic. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `ICACHE_PREFETCH`
- XED category/categories: `PREFETCH`
- ISA set(s): `ICACHE_PREFETCH`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `PREFETCHIT1_MEMu8` — `PREFETCHIT1`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDMSR

`RDMSR` reads a model-specific register selected by ECX and returns its 64-bit value in EDX:EAX; ordinary user-mode code cannot execute it. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`, `MSR_IMM`
- XED category/categories: `SYSTEM`, `VEX`
- ISA set(s): `APX_F_MSR_IMM`, `MSR_IMM`, `PENTIUMREAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `GPR64 IMM`; `VGPR64 IMM`. Representative implicit state: `EAX EDX ECX MSRS`; `MSRS`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDMSR` — `RDMSR`
- `RDMSR_GPR64u64_IMM32` — `RDMSR`
- `RDMSR_GPR64u64_IMM32_APX` — `RDMSR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDMSRLIST

`RDMSRLIST` reads a hardware-defined list of model-specific registers using the MSR-list interface and stores their values in the associated list structure. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MSRLIST`
- XED category/categories: `MSRLIST`
- ISA set(s): `MSRLIST`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RSI RDI RCX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDMSRLIST` — `RDMSRLIST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDPMC

`RDPMC` reads a selected performance-monitoring counter into EDX:EAX when privilege and control settings permit it. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `RDPMC`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX EDX ECX MSRS`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDPMC` — `RDPMC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDTSC

`RDTSC` reads the processor time-stamp counter into EDX:EAX, exposing a high-resolution cycle-like counter without fully serializing surrounding execution. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `PENTIUMREAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX EDX TSC`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDTSC` — `RDTSC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## RDTSCP

`RDTSCP` reads the time-stamp counter and IA32_TSC_AUX with ordering stronger than RDTSC on its leading side, returning the counter in EDX:EAX and auxiliary value in ECX. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `RDTSCP`
- XED category/categories: `SYSTEM`
- ISA set(s): `RDTSCP`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX EDX ECX TSC TSCAUX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `RDTSCP` — `RDTSCP`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SGDT

`SGDT` stores the current global descriptor-table register to memory. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `GDTR`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SGDT_MEMs` — `SGDT`
- `SGDT_MEMs64` — `SGDT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SIDT

`SIDT` stores the current interrupt descriptor-table register to memory. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32`, `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `IDTR`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SIDT_MEMs` — `SIDT`
- `SIDT_MEMs64` — `SIDT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SLDT

`SLDT` stores the current local descriptor-table selector. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286PROTECTED`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv`; `MEM`. Representative implicit state: `LDTR`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SLDT_GPRv` — `SLDT`
- `SLDT_MEMw` — `SLDT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SMSW

`SMSW` stores the machine-status word, exposing selected low CR0 state. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv`; `MEM`. Representative implicit state: `CR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SMSW_GPRv` — `SMSW`
- `SMSW_MEMw` — `SMSW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## STI

`STI` sets the interrupt-enable flag when privilege permits, enabling maskable external interrupts after the architecture's defined delay. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

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

- `STI` — `STI`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## STR

`STR` stores the current task-register selector. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286PROTECTED`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPRv`; `MEM`. Representative implicit state: `TR`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `STR_GPRv` — `STR`
- `STR_MEMw` — `STR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## SWAPGS

`SWAPGS` exchanges the current GS base with the kernel GS base stored in a model-specific register, supporting fast per-CPU context changes around kernel entry and exit. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `LONGMODE`
- XED category/categories: `SYSTEM`
- ISA set(s): `LONGMODE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `GSBASE`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `SWAPGS` — `SWAPGS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## TLBSYNC

`TLBSYNC` waits for earlier AMD broadcast TLB invalidations initiated by INVLPGB to complete before subsequent execution depends on their global effect. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `AMD_INVLPGB`
- XED category/categories: `SYSTEM`
- ISA set(s): `AMD_INVLPGB`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `TLBSYNC` — `TLBSYNC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## URDMSR

`URDMSR` reads an operating-system-authorized user-mode MSR through the user-MSR facility without granting arbitrary RDMSR privilege. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `USER_MSR`
- XED category/categories: `APX`, `USER_MSR`
- ISA set(s): `APX_F_USER_MSR`, `USER_MSR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR64 GPR64`; `GPR64 IMM`; `VGPR64 IMM`. Representative implicit state: `MSRS`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `URDMSR_GPR64u64_GPR64u64` — `URDMSR`
- `URDMSR_GPR64u64_GPR64u64_APX` — `URDMSR`
- `URDMSR_GPR64u64_IMM32` — `URDMSR`
- `URDMSR_GPR64u64_IMM32_APX` — `URDMSR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## UWRMSR

`UWRMSR` writes an operating-system-authorized user-mode MSR through the user-MSR facility without granting arbitrary WRMSR privilege. The pinned XED inventory represents it with 4 normalized encoding records and 4 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `USER_MSR`
- XED category/categories: `APX`, `USER_MSR`
- ISA set(s): `APX_F_USER_MSR`, `USER_MSR`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR64 GPR64`; `IMM GPR64`; `IMM VGPR64`. Representative implicit state: `MSRS`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `UWRMSR_GPR64u64_GPR64u64` — `UWRMSR`
- `UWRMSR_GPR64u64_GPR64u64_APX` — `UWRMSR`
- `UWRMSR_IMM32_GPR64u64` — `UWRMSR`
- `UWRMSR_IMM32_GPR64u64_APX` — `UWRMSR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VERR

`VERR` tests whether the segment selected by its operand is readable at the current privilege level and reports the result in ZF. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286PROTECTED`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR16`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VERR_GPR16` — `VERR`
- `VERR_MEMw` — `VERR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## VERW

`VERW` tests whether the segment selected by its operand is writable at the current privilege level and reports the result in ZF. The pinned XED inventory represents it with 2 normalized encoding records and 2 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I286PROTECTED`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `GPR16`; `MEM`. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `VERW_GPR16` — `VERW`
- `VERW_MEMw` — `VERW`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## WBINVD

`WBINVD` writes back modified cache lines and invalidates the processor caches; it is a privileged whole-cache maintenance operation. The pinned XED inventory represents it with 2 normalized encoding records and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `I486REAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `WBINVD` — `WBINVD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## WBNOINVD

`WBNOINVD` writes modified cache lines back toward memory without invalidating the caches, providing a whole-cache writeback operation distinct from WBINVD. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `WBNOINVD`
- XED category/categories: `SYSTEM`
- ISA set(s): `WBNOINVD`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: not uniformly recorded.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `WBNOINVD` — `WBNOINVD`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## WRMSR

`WRMSR` writes EDX:EAX to the model-specific register selected by ECX; it is privileged and can change processor control state. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `BASE`
- XED category/categories: `SYSTEM`
- ISA set(s): `PENTIUMREAL`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `EAX EDX ECX MSRS`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `WRMSR` — `WRMSR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## WRMSRLIST

`WRMSRLIST` writes a hardware-defined list of model-specific registers using the MSR-list interface. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MSRLIST`
- XED category/categories: `MSRLIST`
- ISA set(s): `MSRLIST`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `RSI RDI RCX`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `WRMSRLIST` — `WRMSRLIST`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## WRMSRNS

`WRMSRNS` writes the model-specific register selected by ECX using the non-serializing WRMSR variant. The pinned XED inventory represents it with 3 normalized encoding records and 3 distinct IFORM/disassembly combinations. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `MSR_IMM`, `WRMSRNS`
- XED category/categories: `APX`, `VEX`, `WRMSRNS`
- ISA set(s): `APX_F_MSR_IMM`, `MSR_IMM`, `WRMSRNS`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`, `64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `IMM GPR64`; `IMM VGPR64`. Representative implicit state: `EAX EDX ECX MSRS`; `MSRS`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `WRMSRNS` — `WRMSRNS`
- `WRMSRNS_IMM32_GPR64u64` — `WRMSRNS`
- `WRMSRNS_IMM32_GPR64u64_APX` — `WRMSRNS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XGETBV

`XGETBV` reads an extended-control register selected by ECX, most commonly XCR0, to determine which processor-managed extended states are enabled. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVE`
- XED category/categories: `XSAVE`
- ISA set(s): `XSAVE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `ECX EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XGETBV` — `XGETBV`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XRSTOR

`XRSTOR` restores selected extended processor-state components from an XSAVE-format memory area. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVE`
- XED category/categories: `XSAVE`
- ISA set(s): `XSAVE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XRSTOR_MEMmxsave` — `XRSTOR`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XRSTOR64

`XRSTOR64` restores selected extended processor-state components from an XSAVE-format memory area using the standard restore semantics with the 64-bit pointer-format variant. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVE`
- XED category/categories: `XSAVE`
- ISA set(s): `XSAVE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XRSTOR64_MEMmxsave` — `XRSTOR64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XRSTORS

`XRSTORS` restores selected extended processor-state components from an XSAVE-format memory area using the supervisor-aware restore semantics. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVES`
- XED category/categories: `XSAVE`
- ISA set(s): `XSAVES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XRSTORS_MEMmxsave` — `XRSTORS`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XRSTORS64

`XRSTORS64` restores selected extended processor-state components from an XSAVE-format memory area using the supervisor-aware restore semantics with the 64-bit pointer-format variant. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVES`
- XED category/categories: `XSAVE`
- ISA set(s): `XSAVES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XRSTORS64_MEMmxsave` — `XRSTORS64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XSAVE

`XSAVE` saves the enabled subset of extended processor state to a memory area using the component layout defined by XCR0 and related control state. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVE`
- XED category/categories: `XSAVE`
- ISA set(s): `XSAVE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XSAVE_MEMmxsave` — `XSAVE`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XSAVE64

`XSAVE64` saves the enabled extended processor-state components to an XSAVE area using the standard XSAVE semantics with the 64-bit pointer-format variant. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVE`
- XED category/categories: `XSAVE`
- ISA set(s): `XSAVE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XSAVE64_MEMmxsave` — `XSAVE64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XSAVEC

`XSAVEC` saves the enabled extended processor-state components to an XSAVE area using the compacted XSAVE semantics. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVEC`
- XED category/categories: `XSAVE`
- ISA set(s): `XSAVEC`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XSAVEC_MEMmxsave` — `XSAVEC`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XSAVEC64

`XSAVEC64` saves the enabled extended processor-state components to an XSAVE area using the compacted XSAVE semantics with the 64-bit pointer-format variant. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVEC`
- XED category/categories: `XSAVE`
- ISA set(s): `XSAVEC`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XSAVEC64_MEMmxsave` — `XSAVEC64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XSAVEOPT

`XSAVEOPT` saves the enabled extended processor-state components to an XSAVE area using the optimized XSAVE semantics. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVEOPT`
- XED category/categories: `XSAVEOPT`
- ISA set(s): `XSAVEOPT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XSAVEOPT_MEMmxsave` — `XSAVEOPT`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XSAVEOPT64

`XSAVEOPT64` saves the enabled extended processor-state components to an XSAVE area using the optimized XSAVE semantics with the 64-bit pointer-format variant. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVEOPT`
- XED category/categories: `XSAVEOPT`
- ISA set(s): `XSAVEOPT`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- usable at CPL 3 subject to feature and OS enablement

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XSAVEOPT64_MEMmxsave` — `XSAVEOPT64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this instruction is documented independently of support status. A lowering should be added only when a typed IR operation or deliberate optimization maps to these semantics more clearly than a simpler baseline sequence.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XSAVES

`XSAVES` saves the enabled extended processor-state components to an XSAVE area using the supervisor-aware XSAVE semantics. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVES`
- XED category/categories: `XSAVE`
- ISA set(s): `XSAVES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XSAVES_MEMmxsave` — `XSAVES`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XSAVES64

`XSAVES64` saves the enabled extended processor-state components to an XSAVE area using the supervisor-aware XSAVE semantics with the 64-bit pointer-format variant. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVES`
- XED category/categories: `XSAVE`
- ISA set(s): `XSAVES`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: `MEM`. Representative implicit state: `EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XSAVES64_MEMmxsave` — `XSAVES64`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.

---

## XSETBV

`XSETBV` writes an extended-control register selected by ECX, changing which extended processor states are enabled; it is privileged by control-state rules. The pinned XED inventory represents it with 1 normalized encoding record and 1 distinct IFORM/disassembly combination. Those encodings are implementation choices beneath the instruction's architectural meaning; this page keeps them grouped under one mnemonic-level operation.

### Family and availability

- XED extension(s): `XSAVE`
- XED category/categories: `XSAVE`
- ISA set(s): `XSAVE`
- vendor classification: `shared-or-unspecified`
- XED mode restriction(s): `16 32 64`
- requires CPL 0; ordinary user-mode code must not emit it

### Architectural effects

Representative explicit operands: not uniformly recorded. Representative implicit state: `ECX EDX EAX XCR0`.

Recorded flag behavior: not uniformly recorded.

### Important forms

- `XSETBV` — `XSETBV`

The form list is intentionally representative rather than a copy of every encoding row. The row-level oracle remains `generated/xed-instructions.tsv`.

### Backend notes

For Idriç this is inventory/reference material first. It should not appear in ordinary user-mode lowering; any future use belongs behind an explicit runtime, kernel, hypervisor, or privileged target boundary.

### Sources

- Intel XED `v2026.08.23` / commit `0bcb6237345c5066726dcc08b3d87928df3b5b26` — machine-readable ICLASS/IFORM and encoding metadata.
- Intel 64 and IA-32 SDM revision `092` — architectural semantics.
- AMD64 Architecture Programmer's Manual revisions pinned in `research/source-pins.json` — vendor-specific availability and semantic cross-checks.
