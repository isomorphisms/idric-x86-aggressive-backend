#!/usr/bin/env python3

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TABLE = ROOT / "research" / "vendor-differences.tsv"
PINS = ROOT / "research" / "source-pins.json"
ICLASSES = ROOT / "generated" / "xed-iclasses.txt"

COLUMNS = [
    "iclass",
    "review_scope",
    "difference_kind",
    "intel_pin",
    "intel_reference",
    "intel_fact",
    "amd_pin",
    "amd_reference",
    "amd_fact",
    "portable_rule",
]


def fail(message):
    raise SystemExit(f"vendor-difference validation failed: {message}")


def main():
    with TABLE.open(newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        if reader.fieldnames != COLUMNS:
            fail(f"unexpected columns: {reader.fieldnames!r}")
        rows = list(reader)

    if not rows:
        fail("manual evidence table is empty")

    pins = json.loads(PINS.read_text())
    iclasses = {line.strip() for line in ICLASSES.read_text().splitlines() if line.strip()}
    seen = set()

    for index, row in enumerate(rows, start=2):
        missing = [column for column in COLUMNS if not row[column].strip()]
        if missing:
            fail(f"row {index} has empty fields: {', '.join(missing)}")
        if row["iclass"] not in iclasses:
            fail(f"row {index} names unknown ICLASS {row['iclass']!r}")
        for column in ("intel_pin", "amd_pin"):
            if row[column] not in pins:
                fail(f"row {index} names missing source pin {row[column]!r}")
        key = (row["iclass"], row["review_scope"], row["difference_kind"])
        if key in seen:
            fail(f"duplicate reviewed scope at row {index}: {key!r}")
        seen.add(key)

    print(f"validated {len(rows)} manual Intel/AMD difference rows")


if __name__ == "__main__":
    main()
