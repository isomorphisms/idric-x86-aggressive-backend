# x86 instruction reference

This directory contains one generated Markdown page for each of the **1,987** XED ICLASS values in the pinned inventory.

The pages are mnemonic-level documentation. Concrete encodings remain in `../../generated/xed-instructions.tsv`; backend support is a separate decision.

Regenerate with `python3 scripts/generate-instruction-docs.py` and verify with `python3 scripts/generate-instruction-docs.py --check`.
