# First direct ELF64 gate

`fixtures/print_x.idric` is the deliberately tiny acceptance source. The path is:

```text
.idric source
  -> frozen bootstrap recognizer
  -> validated WriteByte/Exit backend IR
  -> direct x86-64 instruction encoding
  -> direct ELF64 writer
  -> Linux process entry
```

The recognizer accepts only `main : IO (); main = putChar '<ASCII byte>'`. It is a temporary, explicit bootstrap seam, not a claim to lower general Idriç IO or general checked ANF. Replacing it with the pinned checked-compiler seam is the next compiler-integration task; the backend IR, encoder, and ELF writer do not depend on C or RefC.

The ELF header points directly at the emitted instruction stream. There is no CRT `main`, dynamic interpreter, symbol table, relocation, section, generated C, assembler, linker, libc, Idris runtime, or RefC reference. The one loadable segment is read/execute. Linux supplies the initial stack, but this program neither reads nor changes it, so entry alignment is preserved and no call-alignment question is hidden.

The entry sequence uses the Linux x86-64 syscall ABI directly: `rax` is the syscall number and `rdi`, `rsi`, `rdx` are the first three arguments. It issues `write(1, output, 1)`, then `exit(0)`. A RIP-relative `lea` addresses the byte embedded immediately after the final instruction.

Run `make test` for the exact output oracle and ELF assertions. Run `make inspect` to show the ELF headers, host disassembly, and the backend's byte-for-byte instruction listing. Branching, ordinary calls, SIMD, and optimized selection remain outside this gate.
