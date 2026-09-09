# Idriç x86-64 backend

This branch is the executable x86-64 compiler route:

```text
checked .idric source
  → compiler-owned one-step-at-a-time form
  → scalar backend plan
  → directly encoded x86-64
  → directly emitted ELF64
  → native Linux execution
```

The canonical `PrintX.idric` fixture writes exactly `X` and exits 0. Seven
additional fixtures exercise add, subtract, multiply, both conditional-branch
outcomes, a direct internal call, and six-argument register pressure. The
production route uses no RefC, generated C, C compiler, assembler, linker,
libc, CRT, or target-Chez fallback.

The active compiler dependency is the declared `isomorphisms/Idric` branch
recorded in [`IDRIC_COMPILER_REF`](IDRIC_COMPILER_REF), currently `Idriç`.
CI resolves that branch for every run and records the exact compiler SHA that
actually ran. Incompatibility with the current compiler fails the lane; it does
not retry the first known-green revision.

The first complete green tuple remains historical evidence: Idric PR #63 at
`dd313277fedb2b678ff0df6769ed1330a2e80523` with backend
`e11a69d4d00501531ee058fa3d880267d5fc6d2e`.

## Run the complete route

```sh
git clone https://github.com/isomorphisms/Idric.git .idric
git -C .idric checkout Idriç
.idric/_/edric bootstrap
make ci
```

`make ci` runs 44 tests with no skips, compiles all eight real `.idric`
fixtures, regenerates every artifact and executable byte-for-byte, validates
ELF64 with `file` and `readelf`, disassembles the emitted bytes with `objdump`,
runs each executable natively, and compares exact stdout and exit status.
Evidence is retained under `build/checked-x86/<fixture>/`.

## Find the implementation

- [`backend/idric_x86.py`](backend/idric_x86.py): checked artifact parsing,
  scalar proof/planning, lowering, and concrete x86-64 encoding
- [`backend/elf64.py`](backend/elf64.py): deterministic in-process ELF64 writer
- [`fixtures/PrintX.idric`](fixtures/PrintX.idric): canonical acceptance source
- [`scripts/run_checked_integration.sh`](scripts/run_checked_integration.sh):
  real compiler/ELF/native acceptance
- [`docs/checked-x86-baseline.md`](docs/checked-x86-baseline.md): exact supported
  surface, process convention, inspection evidence, and stack reconciliation

Top-level symbolic links expose the same implementation and acceptance files
without moving the preserved PR work.
