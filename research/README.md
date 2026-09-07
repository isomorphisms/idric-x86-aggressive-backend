# x86 ISA research inputs

`source-pins.json` records the exact machine-readable and architectural references used for the ISA inventory.

The generated instruction inventory is intentionally reproducible: changing a source revision is an explicit repository change, not an unnoticed consequence of running against whatever XED happens to be current that day.

`vendor-differences.tsv` is the separate manual Intel/AMD evidence layer. `vendor-differences.md` defines its evidence boundary: absence from that table means unreviewed, never implicitly shared.
