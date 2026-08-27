# Generated x86 ISA data

These files are generated from the exact Intel XED revision pinned in `research/source-pins.json`.

- `xed-iclasses.txt` — one unique XED ICLASS per line
- `xed-iforms.txt` — one unique concrete XED IFORM per line
- `xed-instructions.tsv` — one row per normalized XED instruction record, retaining encoding and semantic metadata useful to the backend

Regenerate with:

```text
bash scripts/refresh-xed-inventory.sh
```

Do not hand-edit the generated inventory files.
