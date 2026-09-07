# x86 instruction reference

The pinned XED inventory currently contains **1,987 ICLASS values**.  The semantic generator still audits each ICLASS individually, but the checked-in reference is bundled by broad architectural family so it is practical to browse.

A section existing here means the instruction is documented, not that the Idriç backend supports or emits it.

| Bundle | ICLASS sections |
| --- | ---: |
| [Core integer and data movement](core-integer-and-data-movement.md) | 210 |
| [Control flow, stack, and strings](control-flow-stack-and-strings.md) | 123 |
| [Bit manipulation and atomics](bit-manipulation-and-atomics.md) | 46 |
| [x87, MMX, and SSE SIMD](x87-mmx-and-simd.md) | 392 |
| [AVX, FMA, and modern vector](avx-fma-and-modern-vector.md) | 89 |
| [AVX-512 and AVX10](avx512-and-avx10.md) | 770 |
| [Cryptography, random, and hashing](crypto-random-and-hashing.md) | 48 |
| [Matrix, tile, and AI extensions](matrix-tile-and-ai.md) | 44 |
| [System, processor state, and privileged operations](system-state-and-privileged.md) | 62 |
| [Virtualization and confidential computing](virtualization-and-confidential-computing.md) | 98 |
| [Security, enclaves, and control-flow protection](security-enclaves-and-control-flow-protection.md) | 48 |
| [Legacy, vendor-specific, and specialized extensions](legacy-vendor-and-specialized.md) | 57 |

**Total: 1,987 ICLASS sections.**

`scripts/bundle-instruction-docs.py --check` verifies that every name in `generated/xed-iclasses.txt` appears exactly once as an instruction section and that no per-ICLASS Markdown files remain checked in.
