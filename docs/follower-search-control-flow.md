# Follower search/control-flow slice

This slice grows the x86-64 backend for the general compiler probes rather than for Wegert.

It is stacked on the first direct ELF64 gate and deliberately stays below the still-missing checked Idriç one-step-at-a-time handoff. No source recognizer is added here. The new code is target-side machinery that the checked compiler seam can eventually drive.

## Why this slice

The small search workloads shared by `bioawk`, grep-like work, parser/dispatch fixtures, and later rendering front ends all need ordinary integer control flow before unusual x86 instructions are interesting. The initial x86 subset already reserved data movement, address calculation, integer arithmetic, compare/test, conditional branches, and direct branches for exactly this kind of executable evidence.

The first native fixture specializes an exact fixed-string count over embedded bytes. It counts overlapping matches, so `AAAAA` searched for `AAA` returns three. Embedded NUL bytes and byte values above 127 remain ordinary data.

The emitted loop uses ordinary x86 strengths instead of imitating Thumb instruction-for-instruction:

- RIP-relative `LEA` for the embedded byte base;
- indexed byte loads of the form `[rsi + rcx + displacement]`;
- FLAGS from `CMP` feeding `JAE`/`JNE`;
- direct rel32 loop branches;
- a small deterministic instruction stream with named-label fixups.

This is evidence for the user's "x86 is the wider road" hypothesis only in a narrow sense: this fixture does not need Thumb-style accommodations. It is not evidence that every later x86 lowering will be simpler.

## Deliberate boundaries

- This is not general grep, FASTA parsing, file IO, argv handling, or the full `ai-ci` biology candidate protocol.
- The haystack and needle are compile-time fixture bytes so the branch/search kernel can be inspected before runtime plumbing is introduced.
- Empty-pattern semantics fail closed because that language/search rule has not been chosen here.
- The first specialized needle is limited to 128 bytes so indexed loads need only the small displacement form. A later general lowering can choose larger displacements or another search strategy when a real fixture earns it.
- The executable reports its test result through Linux process exit status, so this first oracle rejects more than 255 candidate start positions instead of silently truncating the observable count.
- No SIMD, string instructions, BMI, AVX, AVX-512, or unusual loop instruction is used merely because x86 provides one.
- No claim is made that this straight comparison loop is fast. It is the scalar semantic baseline against which Shift-Or/Shift-And, table-driven, branchless, or SIMD candidates can later be compared on the shared workloads.

## Verification

`make test` now executes generated ELF64 binaries natively and checks:

- overlapping count semantics;
- absent and too-long needles;
- embedded NUL and high-byte values;
- explicit rejection of the unsettled empty-pattern case;
- explicit rejection before process-exit-status truncation can occur;
- byte-for-byte deterministic generation;
- fail-closed unresolved branch labels;
- inspection text showing indexed loads and ordinary conditional branches.

The existing direct-ELF64 workflow runs this automatically because the test and backend paths are already in its pull-request trigger.

## Next useful seams

The next compiler-facing task remains the checked Idriç one-step-at-a-time handoff from #12 / #4 / PR #11. Once that can express integer loops and byte loads without importing Thumb-specific representation choices, this target-side slice can be driven by real Idriç instead of a backend fixture.

After that, the shared biology/search work can grow in evidence order: exact byte/string search, many-way base/token dispatch, real corpus candidate protocol, then alternative branch/table/bit-parallel/SIMD realizations where measurements justify them.
