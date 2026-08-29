# Generated x86 ISA data

These files are generated from the exact Intel XED revision pinned in `research/source-pins.json`.

- `xed-iclasses.txt` — one unique XED ICLASS per line;
- `xed-iforms.txt` — one unique concrete XED IFORM per line;
- `xed-instructions.tsv` — one row per normalized XED instruction record, preserving repeated IFORM records rather than silently collapsing them;
- `xed-iform-index.tsv` — exactly one row per unique IFORM, including the number of XED records belonging to that form.

The record table carries explicit 16/32/64-bit mode columns, split flag read/write/undefined fields plus raw XED flag text, operands, encoding pattern, privilege level, extension/ISA metadata, explicit vendor evidence where XED supplies it, and source provenance.

Regenerate and validate with:

```text
bash scripts/refresh-xed-inventory.sh
```

Do not hand-edit the generated inventory files. Backend implementation status belongs outside this directory.
