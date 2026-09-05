# Manual Intel/AMD difference overlay

`vendor-differences.tsv` records only vendor differences that were manually checked against the references pinned in `source-pins.json`.

This file is a separate evidence layer from the generated Intel XED inventory. It does not rewrite XED metadata and it does not treat missing manual review as evidence of shared semantics or availability.

Rules:

- `vendor_scope=unspecified` in the generated inventory remains `unspecified` until a manual source establishes something stronger.
- Absence from `vendor-differences.tsv` means **unreviewed**, not shared.
- Each row must identify the affected instruction/form scope, the kind of difference, both pinned references, the vendor facts, and the narrow portable rule a backend may rely on.
- Intel/AMD differences that do not affect an emitted backend form remain research evidence; they do not expand backend support.
- OS ABI facts are separate from ISA facts. In particular, the Linux x86-64 syscall convention does not establish portable SYSCALL semantics in other modes.

The first reviewed rows deliberately cover two different failure modes that XED metadata alone cannot settle:

1. `BSF` / `BSR`: the pinned manuals agree on ZF and zero-source destination preservation for current implementations, but differ on the remaining arithmetic flags; Intel rev. 092 also carries explicit older-processor caveats.
2. `SYSCALL` / `SYSRET`: Intel rev. 092 and AMD's pinned APM describe different mode availability and target/return machinery outside the common 64-bit case.

Do not bulk-fill this table from extension names, CPUID folklore, third-party opcode tables, or absence of an XED vendor marker.
