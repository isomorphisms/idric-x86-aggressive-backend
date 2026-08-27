# x86 ISA inventory

This backend starts by enumerating the architecture before choosing instructions to emit.

## Two levels of "instruction"

x86 needs at least two useful levels of inventory:

1. **ICLASS** — the mnemonic-like instruction class: `ADD`, `JMP`, `VADDPS`, `VMRUN`, and so on.
2. **IFORM** — a concrete operand/encoding form within an ICLASS.

The distinction matters. Treating `ADD` as one instruction discards operand widths, register versus memory forms, encoding spaces, APX/EVEX distinctions, mode restrictions, and other information the backend will eventually need.

Intel XED's published generated header currently has 1,960 real ICLASS values, excluding its `INVALID` and `LAST` sentinels. The IFORM set is much larger.

## Primary machine-readable source

The inventory is generated from Intel XED release `v2026.08.23`, commit:

`0bcb6237345c5066726dcc08b3d87928df3b5b26`

XED already provides a supported metadata-export path:

```text
python mfile.py just-prep
python pysrc/xed_to_db.py --xed-dgen=obj/dgen --out=xed_db.json
```

`just-prep` gathers and normalizes the active XED instruction layers without compiling the library. `xed_to_db.py` exposes fields including ICLASS, IFORM, ISA set, extension, category, operands, flags, CPL, encoding space, opcode information, mode restrictions, and attributes.

The repository wrapper is:

```text
scripts/refresh-xed-inventory.sh
```

It pins both XED and its sibling `mbuild` dependency and then generates:

- `generated/xed-iclasses.txt` — every unique ICLASS
- `generated/xed-iforms.txt` — every unique IFORM
- `generated/xed-instructions.tsv` — row-level metadata for the concrete instruction records
- `docs/x86-isa-inventory.generated.md` — counts grouped by XED extension and category

## Architectural cross-checks

Machine-readable enumeration is not the same thing as architectural interpretation. We cross-check the generated inventory against:

- Intel 64 and IA-32 Software Developer's Manual, revision 092, especially Volume 2 A-Z.
- AMD64 Architecture Programmer's Manual, combined Volumes 1-5 revision 4.09.
- AMD64 APM Volume 3 revision 3.37 for general-purpose/system instructions.
- AMD64 APM Volume 4 revision 3.26 for 128-, 256-, and 512-bit media instructions.

Exact source pins live in `research/source-pins.json`.

## What the complete inventory includes

The inventory is intentionally broader than the first Idriç backend subset. It includes, where present in the pinned XED database:

- legacy integer and data movement
- integer arithmetic, logic, shifts, rotates, bit manipulation
- compare/test, conditional moves, branches, loops, calls, returns
- stack and string instructions
- atomic and lockable operations
- system, privileged, interrupt, syscall, protection, paging, and state-management instructions
- x87
- MMX and 3DNow!
- SSE generations
- AVX and AVX2
- FMA, BMI/BMI2, ADX and related scalar extensions
- AES, SHA, GFNI and other crypto-oriented extensions
- AVX-512 families
- AVX10
- AMX
- APX
- Intel VMX
- AMD SVM and AMD-specific extensions such as XOP/TBM where represented
- legacy, obsolete, and undocumented forms retained by XED

## Backend policy is separate

A row in this inventory means "this exists in the x86 instruction universe represented by the pinned sources." It does **not** mean Idriç should emit it.

The first executable x86-64 user-mode subset can remain tiny: data movement, LEA, integer arithmetic/logic, compare/test, branches, direct calls/returns, and the stack/ABI operations actually required by a minimal program. SIMD, Float16-oriented work, unusual dispatch machinery, and vendor-specific instructions should then be selected deliberately from the complete catalog.
