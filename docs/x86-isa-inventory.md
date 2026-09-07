# x86 ISA inventory

This backend starts by enumerating the architecture before choosing instructions to emit.

## Two levels of "instruction"

x86 needs at least two useful levels of inventory:

1. **ICLASS** — the mnemonic-like instruction class: `ADD`, `JMP`, `VADDPS`, `VMRUN`, and so on.
2. **IFORM** — a concrete operand/encoding form within an ICLASS.

The distinction matters. Treating `ADD` as one instruction discards operand widths, register-versus-memory forms, encoding spaces, APX/EVEX distinctions, mode restrictions, and other information the backend will eventually need.

There is one more distinction in the XED export itself: a single IFORM can occur in more than one exported XED record. The pinned database currently has 10,994 instruction records but 9,001 unique IFORM values. Therefore this repository keeps both:

- `generated/xed-instructions.tsv` — every normalized XED record, without silently deduplicating repeated IFORMs;
- `generated/xed-iform-index.tsv` — exactly one row per unique IFORM, with a `record_count` pointing back to the record-level multiplicity.

For completeness checks, the repository uses the normalized database generated from the pinned XED release rather than a hand-written mnemonic list.

## Primary machine-readable source

The inventory is generated from Intel XED release `v2026.08.23`, commit:

`0bcb6237345c5066726dcc08b3d87928df3b5b26`

XED already provides a supported metadata-export path:

```text
python mfile.py just-prep
python pysrc/xed_to_db.py --xed-dgen=obj/dgen --out=xed_db.json
```

`just-prep` gathers and normalizes the active XED instruction layers without compiling the library. `xed_to_db.py` exposes ICLASS, IFORM, ISA set, extension, category, operands, flags, CPL, encoding space, opcode information, mode restrictions, attributes, and related metadata.

The repository wrapper is:

```text
scripts/refresh-xed-inventory.sh
```

It pins both XED and its sibling `mbuild` dependency, generates the inventory, and validates the generated invariants.

Generated outputs:

- `generated/xed-iclasses.txt` — every unique ICLASS;
- `generated/xed-iforms.txt` — every unique IFORM;
- `generated/xed-instructions.tsv` — one row per XED instruction record;
- `generated/xed-iform-index.tsv` — one row per unique IFORM;
- `docs/x86-isa-inventory.generated.md` — generated counts by vendor scope, extension, and category.

The record table has explicit `mode_16`, `mode_32`, and `mode_64` columns; split `flags_read`, `flags_written`, and `flags_undefined` columns while retaining `flags_raw`; explicit source revision/reference fields; and the original operand/encoding metadata needed to avoid prematurely collapsing concrete forms.

## Human-readable ISA family map

This table is a navigation map, not the completeness oracle. XED categories and extensions overlap, and new XED releases can add labels. The generated extension/category tables remain the mechanical check that nothing in the pinned database disappeared.

| Family | XED handles / representative labels | What belongs here |
|---|---|---|
| Base integer and data movement | `BASE`, `DATAXFER` | `MOV` forms, sign/zero extension, exchanges, immediate/register/memory movement |
| Integer arithmetic | `BASE`, `BINARY` | add/subtract, multiply/divide, increment/decrement, carry/borrow variants |
| Logical and bitwise | `LOGICAL`, `BASE` | AND/OR/XOR/NOT and related scalar logical forms |
| Shifts and rotates | `SHIFT`, `ROTATE` | logical/arithmetic shifts, rotates, rotate-through-carry |
| Compare and test | `BINARY`, `LOGICAL` | compare/test forms and flag-setting scalar comparisons |
| Conditional moves / sets | `CMOV`, `SETCC` | flag-dependent data movement and boolean materialization |
| Branches, calls, returns, loops | `COND_BR`, `UNCOND_BR`, `CALL`, `RET`, `LOOP` | direct/indirect control flow, conditional jumps, calls, returns, loop-family instructions |
| Stack operations | `PUSH`, `POP` | push/pop forms and legacy stack-manipulation instructions |
| String and I/O-string operations | `STRINGOP`, `IOSTRINGOP` | move/compare/scan/store/load strings and REP-sensitive forms |
| Address calculation | `LEA` within base data-transfer metadata | effective-address formation without a memory load |
| Atomic / locking | `SEMAPHORE`, lockable `BASE`, `CMPCCXADD`, `RAO` | locked RMW, compare/exchange, exchange-add, newer atomic families |
| Bit scan/count/manipulation | `BITBYTE`, `BMI1`, `BMI2`, `LZCNT` | scans, counts, extracts/deposits, bit tests/manipulation |
| System and privileged | `SYSTEM`, `SEGOP`, `XSAVE*`, protection/state families | control registers, descriptors, paging/TLB, processor state, privileged operations |
| Interrupts and syscall boundaries | `INTERRUPT`, `SYSCALL`, `SYSRET` | software interrupts, syscall/sysret and related transitions |
| x87 | `X87` | legacy x87 floating-point stack instructions |
| MMX / 3DNow! | `MMX`, `3DNOW`, `3DNOW_PREFETCH` | legacy packed integer / AMD 3DNow! families |
| SSE generations | `SSE`, `SSE2`, `SSE3`, `SSSE3`, `SSE4`, `SSE4a` | 128-bit SIMD and scalar FP/integer extensions |
| AVX / AVX2 | `AVX`, `AVX2`, `AVX2GATHER` | VEX-encoded vector arithmetic, logic, permutation, gather, etc. |
| FMA | `FMA`, `FMA4` | fused multiply-add families; vendor history must remain visible |
| Crypto / finite-field | `AES`, `AVXAES`, `VAES`, `PCLMULQDQ`, `VPCLMULQDQ`, `SHA`, `SHA512`, `GFNI`, `SM3`, `SM4`, `KEYLOCKER*` | cryptographic and carry-less / finite-field operations |
| AVX-512 | `AVX512EVEX`, `AVX512VEX` plus AVX-512 categories | EVEX vector widths, masks, gathers/scatters, conversions, FP16/BF16 and subfamilies |
| AVX10 | AVX10 ISA sets represented in current XED data | newer converged vector ISA generations; inspect `isa_set` as well as extension |
| AMX | `AMX_TILE`, `AMX_TILE` category | tile state, tile movement and matrix-oriented operations |
| APX | `APXEVEX`, `APXLEGACY`, `APX` category | extended GPR/encoding/control-flow capabilities and APX forms |
| Virtualization | Intel VMX/VTX metadata, AMD `SVM` | hardware virtualization instructions; Intel and AMD families are not merged |
| Intel-specific / future-feature layers | SGX, TDX, FRED, UINTR, VMX-related and other explicitly documented Intel layers | retain as inventory even when not baseline backend targets |
| AMD-specific layers | `SVM`, `SSE4a`, `XOP`, `TBM`, `FMA4`, `CLZERO`, `MONITORX`, `MCOMMIT`, `RDPRU`, `AMD_INVLPGB`, 3DNow! | retain explicit AMD-only records and semantic/availability differences |
| Other-vendor / legacy layers | VIA PadLock families and XED undocumented/legacy attributes | inventory-only unless deliberately selected later |

## Vendor semantics: preserve uncertainty too

Intel XED is the mechanical source, but it contains AMD-specific records and attributes. The generator only assigns `vendor_scope=amd-only` or `vendor_scope=intel-only` when the exported record supplies explicit evidence such as `AMDONLY`, `INTELONLY`, or an explicit vendor ISA set. Otherwise it writes `vendor_scope=unspecified`.

That wording is deliberate. **Unspecified does not mean shared by Intel and AMD.** Absence of a vendor-only marker is not enough to prove identical availability or semantics. For example, XED's AMD layer has separate `SYSCALL_AMD` and `SYSRET_AMD` records for AMD's 32-bit behavior. The raw attributes and ISA-set fields are retained so this distinction is not flattened away.

The Intel SDM / instruction-set-extension reference and AMD64 APM remain architectural cross-checks. A later manual vendor-difference overlay can add semantic and availability judgments without rewriting the XED-derived inventory or pretending that XED alone proves cross-vendor equivalence.

## Architectural cross-checks

Exact source pins live in `research/source-pins.json`. The current review set includes:

- Intel 64 and IA-32 Software Developer's Manual, revision 092, especially Volume 2 A-Z;
- Intel Architecture Instruction Set Extensions Programming Reference, revision `319433-062`;
- AMD64 Architecture Programmer's Manual, combined Volumes 1-5 revision 4.09;
- AMD64 APM Volume 3 revision 3.37 for general-purpose/system instructions;
- AMD64 APM Volume 4 revision 3.26 for 128-, 256-, and 512-bit media instructions.

## Backend policy is a separate artifact

A row in this inventory means "this exists in the x86 instruction universe represented by the pinned source." It does **not** mean Idriç emits it, prefers it, or even allows it in user mode.

The initial backend scope is documented separately in `docs/x86-64-initial-backend-subset.md`. No `backend_status` column is allowed in the generated complete-inventory tables; the validator checks that separation. Eventually support should be attached to deliberately selected concrete IFORMs rather than casually declaring an entire ICLASS implemented.
