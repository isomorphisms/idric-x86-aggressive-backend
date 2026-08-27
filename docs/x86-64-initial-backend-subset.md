# Initial x86-64 backend subset

This file is deliberately separate from the complete ISA inventory.

**Current status: design scope only. No instruction or IFORM listed here is claimed implemented by this document.**

The first executable Idriç x86-64 path should be small enough to inspect in disassembly and reason about against the ABI. Candidate semantic operations are:

- data movement required for arguments, results, locals, and constants;
- `LEA` for address calculation where appropriate;
- integer add/subtract and the minimal logical operations needed by early examples;
- compare/test and a deliberately small set of conditional branches;
- unconditional direct branch;
- direct call and return;
- stack-pointer/frame operations only where the selected ABI actually requires them;
- explicit runtime/syscall boundary code kept separate from ordinary instruction selection.

The first lowering pass should choose **specific IFORMs** from `generated/xed-iform-index.tsv` and then inspect their record-level constraints in `generated/xed-instructions.tsv`. It should not mark every form under `MOV`, `ADD`, `JMP`, or another ICLASS as supported just because one encoding works.

Not in the initial subset unless an executable example creates a concrete reason to add them:

- x87, MMX, 3DNow!;
- SSE/AVX/AVX-512/AVX10/AMX/APX as broad families;
- privileged/system/virtualization instructions;
- vendor-specific instructions;
- unusual loop/string/dispatch machinery;
- SIMD and Float16-oriented work, which should be selected later from the complete catalog on purpose.

This separation is the rule: **inventory completeness is architectural knowledge; backend support is an implementation decision.**
