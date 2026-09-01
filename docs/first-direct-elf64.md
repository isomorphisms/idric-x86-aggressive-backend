# Preserved PR #18 checked mathematical direct ELF64 path

This document describes the preserved domain-specific R128 regression now in
`backend/r128_math.py`. It is not the canonical compiler-owned scalar handoff.
See `checked-x86-baseline.md` for the real `.idric` route.

The claimed compiler path is now:

```text
R128Pipeline.idric
  -> ordinary Idriç parse, elaboration, and core type check
  -> EDRIC_MATH_ONE_STEP v1 artifact
  -> strict x86 artifact validation
  -> exact signed-i64 scalar plan
  -> direct x86-64 instruction encoding
  -> direct ELF64 writer
  -> native hosted x86-64 execution
  -> exact binary observations for independent RHS/AICI validation
```

The Idriç compiler owns the first three arrows.  This repository starts at the
checked artifact.  `backend/r128_math.py` does not accept Idriç source syntax,
infer mathematics from names, or rediscover a source fixture.  Passing an
`.idric` file to it fails at `wrong_artifact_header`.  The optional `--source`
argument reads source bytes only to verify the artifact's SHA-256 digest.

## Checked handoff

The strict, tab-separated `EDRIC_MATH_ONE_STEP` v1 protocol records:

- the exact source SHA-256 and full `isomorphisms/Idric` head;
- ordinary core type checking as `PASS`;
- sorted named spaces and typed exact-integer vectors, covectors, and sphere
  points;
- checked certificates with typed claim kind, provenance, and whitelisted trace
  fields;
- typed orthogonal transforms, including orientation and exact generator
  parameters;
- ordered `Contract`, `Dot`, `SquaredNorm`, `Reflect`, `RotatePlane`, and
  `ActOnSphere` steps;
- allowed target realizations and one-step temporary policies.

The consumer rejects unknown rows and operations, reordered keys, missing or
failed certificates, forward/unknown values, vector/covector substitution,
equal-rank but differently named spaces, dimension disagreement, incorrect
orientation, incorrect sphere ambient dimension, ambiguous transforms, and a
plan that omits the scalar baseline.  The backend does not contain a second
theorem solver.  It validates and retains compiler certificates while ordinary
Idriç core checking remains the logical authority.

## Native workload

The exact fixture uses 128 coordinates, including a nonzero coordinate 128:

```text
x   = (3, 4, 12, 0, ..., 0, 9)
y   = (5, -2, 7, 0, ..., 0, 11)
phi = (5, -2, 7, 0, ..., 0, 11) as a covector
```

The direct executable computes and exposes the canonical 16-result workload:

| One-step operation | Result | Exact observation |
| --- | --- | --- |
| `contract` | `contraction` | `190` |
| `dot_xx` | `x_dot_x` | `250` |
| `dot_xy` | `x_dot_y` | `190` |
| `norm_x` | `x_squared_norm` | `250` |
| `reflect_x` | `hx` | `(-3,4,12,0,...,0,9)` |
| `reflect_y` | `hy` | `(-5,-2,7,0,...,0,11)` |
| `reflect_hx` | `h2x` | `x` |
| `dot_hx_hy` | `hx_dot_hy` | `190` |
| `rotate_x` | `gx` | `(-4,3,12,0,...,0,9)` |
| `rotate_y` | `gy` | `(2,5,7,0,...,0,11)` |
| `rotate_gx` | `g2x` | `(-3,-4,12,0,...,0,9)` |
| `rotate_g2x` | `g3x` | `(4,-3,12,0,...,0,9)` |
| `rotate_g3x` | `g4x` | `x` |
| `dot_gx_gy` | `gx_dot_gy` | `190` |
| `act_sphere` | `sphere_after` | `e_128` in `S^127` |
| `sphere_norm` | `sphere_squared_norm` | `1` |

The process writes a fixed-layout binary result buffer.  It does not contain
the expected values.  The test and later RHS consumer independently decode and
check `190`, `250`, the exact transformed vectors, involution, fourth power,
dot preservation, the far coordinate, and the sphere point.

## Scalar plan and temporaries

Version 1 intentionally chooses `scalar_integer`.  Coordinates are signed
64-bit integers only after a conservative compile-time bound proves every
reduction fits; otherwise planning fails rather than silently changing exact
`Integer` meaning.  No floating point or unexplained double widening is used.
SSE2 and AVX2 are not claimed yet.

Reduction accumulators remain in `rax`; the coordinate product reuses `r11`.
Transform coordinates reuse `rax`.  Checked certificate data folds away.  The
listing distinguishes register, fold, reuse, spill, and eliminate decisions.
Semantic results occupy explicit stack receipt slots because they are observed;
those slots are not evidence that every source or one-step name became a memory
store.  The current scalar plan reports zero compiler-temporary spills.

## ELF and fallback boundary

The ELF header points directly at the emitted instruction stream.  The image
has one read/execute `PT_LOAD` and no section table, interpreter, dynamic
segment, CRT entry, symbol table, relocation, generated C, assembler input,
linker input, libc, Idris runtime, or RefC reference.  Linux supplies the stack;
the program uses it for its explicit observation buffer and issues only direct
`write` and `exit` syscalls.

The compiler/backend execution receipt is `MATH_BACKEND_EXECUTION` v1.  It binds
the artifact digest, compiler head, backend head, target, selected plans,
temporary decisions, direct-codegen/native stages, absent fallbacks, ELF digest,
and exact observations.  Its `source_parse`, `constraint_generation`,
`constraint_resolution`, and `core_typecheck` stages are explicitly propagated
from the digest/head-bound compiler artifact rather than re-proved by the x86
backend.  It deliberately does not declare `rhs_validation`;
RHS owns that independent stage.

## Running it

`make test` runs the backend using an in-memory artifact explicitly labeled as
a test double.  That proves artifact validation, planning, direct encoding, ELF
execution, and the exact backend observations; it is not evidence that a real
front end emitted the artifact.

Run this additional handoff against the pinned checked-out Idriç compiler with:

```sh
make ci-unit IDRIC_REPO=/path/to/Idric
```

That configured test invokes exactly
`edric --emit-math-one-step SOURCE -o ARTIFACT`, verifies the artifact against
the same source bytes, and only then compiles and runs it. Hosted CI configures
this regression explicitly and fails on any skip. A raw local unit-test
discovery without those paths may still label this additional regression
`SKIP`; it never substitutes the test double into a claimed front-end path.
