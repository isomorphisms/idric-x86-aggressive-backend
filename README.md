# Idriç x86 aggressive backend

Experimental direct x86 backend work for Idriç.

The checked path now consumes the Idriç compiler's versioned mathematical
one-step artifact, selects an exact-integer scalar plan, directly encodes
x86-64, writes a direct ELF64 image, and runs the hostile `R^128` fixture
natively.  It does not parse `.idric` source and has no RefC, generated-C,
assembler, linker, libc, or dynamic-loader fallback.

`make test` runs backend-boundary, hostile-rejection, direct-ELF, and native
exact-result tests.  `make integration IDRIC_REPO=/path/to/Idric` additionally
runs the real compiler emitter on
`examples/mathematical-one-step/R128Pipeline.idric`, verifies its source digest,
executes the resulting ELF, and writes the cross-repository execution receipt.

See [the checked direct-ELF boundary](docs/first-direct-elf64.md) for what is
verified here and what remains owned by the Idriç compiler and RHS/AICI.
