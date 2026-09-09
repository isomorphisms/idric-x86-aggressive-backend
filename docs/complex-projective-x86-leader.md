# x86-64 complex/projective leading implementation

For complex and projective arithmetic only, this branch is the current executable implementation leader. That exception does not change the general backend hierarchy: Thumb-2 remains the human-in-the-loop leader for general backend work.

## Candidate path

The candidate is direct x86-64 ELF64 machine code. Python constructs instruction bytes and ELF headers, then runs the produced file. Candidate arithmetic does not pass through C, an assembler, a linker, libc, libm, RefC, LLVM, or another compiler backend.

The baseline representation uses two scalar Float32 machine components for an ordinary complex value. This is an x86 lowering decision, not the source-language definition of the mathematical complex numbers. Projective values are represented by homogeneous complex coordinates; there is no runtime quotient object and no normalization after every operation.

The required CPU instructions are baseline x86-64 scalar SSE operations. x87 `FPATAN`, `FSIN`, and `FCOS` are used only for the observational polar/phase round trip. Magnitude, phase, and conjugation do not feed back into the holomorphic `q -> exp(q)` evolution used by the render fixture.

## Executable corpus

The shared corpus is owned by the canonical Idriç branch at:

```text
_/fixtures/complex-projective/float32.json
```

The x86 executable covers:

- complex construction by machine coordinates;
- addition, subtraction as part of rational/divisor evaluation, negation through conjugation's sign operation, multiplication, reciprocal, and division;
- integer power two;
- conjugation and squared magnitude;
- polynomial and rational evaluation;
- bounded complex exponential;
- Cartesian/polar observation and round trip;
- homogeneous rescaling by a nonzero real scale and by a nontrivial phase scale;
- projective non-equivalence through invariant wedge residuals;
- affine-to-projective/first-chart round trip.

Projective comparison never compares homogeneous components directly. Equivalent fixtures check the common-scale relation. The deliberately non-equivalent fixture accumulates the invariant residuals `zi*wj - zj*wi`.

## Bounded exponential

The current baseline complex exponential uses the degree-7 Taylor polynomial in complex arithmetic. It is accepted only when the input magnitude is at most `0.5`. The generator rejects a corpus or render whose `q(z)` leaves that domain.

The acceptance threshold is not fitted to the observed result. It is the analytic remainder

```text
exp(|q|) |q|^8 / 8!
```

plus a binary32 rounding allowance derived from machine epsilon and a conservative operation count.

This is intentionally understandable baseline code. A later range-reduced or SIMD implementation may replace it only while remaining under the same corpus and error contract.

## Headless render

`complex-render.elf` directly computes a deterministic 32x32 binary PPM scene from

```text
f(z) = R(z) exp(q(z))
```

with an explicit zero and pole in `R` and a nonconstant entire quadratic polynomial `q`. The image is produced without a desktop environment. The render code contains no lasso, overlapping-disc, path, Riemann-surface, or lacunary state.

The x86 lane requires exact byte determinism against itself. Other backends are not required to match its pixels bit-for-bit when their declared floating precision or transcendental implementation differs; they must instead satisfy the shared arithmetic/projective corpus and render-level structural checks appropriate to their precision.

## Receipts

`scripts/run_complex_projective_acceptance.py` records the exact backend SHA, canonical Idriç SHA, corpus hash, generated ELF hashes, numerical-output hash, render hash, derived exponential error bound, projective non-equivalence residual, and render statistics.

The GitHub Actions lane also executes both generated files in an unmodified `debian:13-slim` container. The thin-Debian receipt requires its numerical output and PPM to be byte-identical to the host x86-64 run.
