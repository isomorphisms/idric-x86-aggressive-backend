#!/usr/bin/env python3

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GENERATED = ROOT / "generated"

RECORD_COLUMNS = {
    "record_index",
    "iclass",
    "iform",
    "category",
    "extension",
    "isa_set",
    "cpl",
    "mode_16",
    "mode_32",
    "mode_64",
    "operands",
    "flags_read",
    "flags_written",
    "flags_raw",
    "encoding_pattern",
    "vendor_scope",
    "vendor_evidence",
    "source_revision",
    "source_reference",
}
FORM_COLUMNS = {
    "iform",
    "iclass",
    "record_count",
    "mode_16",
    "mode_32",
    "mode_64",
    "vendor_scope",
    "source_revision",
    "source_reference",
}
BOOLEAN = {"true", "false"}
VENDOR_SCOPES = {"amd-only", "intel-only", "unspecified"}


def read_lines(path):
    return {line.strip() for line in path.read_text().splitlines() if line.strip()}


def read_tsv(path):
    with path.open(newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def fail(message):
    raise SystemExit(f"inventory validation failed: {message}")


def main():
    record_path = GENERATED / "xed-instructions.tsv"
    form_path = GENERATED / "xed-iform-index.tsv"
    iclass_path = GENERATED / "xed-iclasses.txt"
    iform_path = GENERATED / "xed-iforms.txt"

    for path in (record_path, form_path, iclass_path, iform_path):
        if not path.exists():
            fail(f"missing {path.relative_to(ROOT)}")

    records = read_tsv(record_path)
    forms = read_tsv(form_path)
    iclasses = read_lines(iclass_path)
    iforms = read_lines(iform_path)

    if not records:
        fail("record table is empty")
    if not forms:
        fail("IFORM index is empty")

    missing = RECORD_COLUMNS - set(records[0])
    if missing:
        fail(f"record table missing columns: {', '.join(sorted(missing))}")
    missing = FORM_COLUMNS - set(forms[0])
    if missing:
        fail(f"IFORM index missing columns: {', '.join(sorted(missing))}")

    if "backend_status" in records[0] or "backend_status" in forms[0]:
        fail("backend support status must remain outside the complete inventory")

    record_iclasses = {row["iclass"] for row in records if row["iclass"]}
    record_iforms = {row["iform"] for row in records if row["iform"]}
    form_iforms = {row["iform"] for row in forms if row["iform"]}

    if record_iclasses != iclasses:
        fail("xed-iclasses.txt does not match the record table")
    if record_iforms != iforms:
        fail("xed-iforms.txt does not match the record table")
    if form_iforms != iforms:
        fail("IFORM index does not contain exactly the unique IFORM set")
    if len(forms) != len(iforms):
        fail("IFORM index is not one row per unique IFORM")

    record_count_sum = 0
    for row in forms:
        try:
            count = int(row["record_count"])
        except ValueError:
            fail(f"non-integer record_count for {row['iform']}")
        if count < 1:
            fail(f"zero record_count for {row['iform']}")
        record_count_sum += count

    if record_count_sum != len(records):
        fail(
            f"IFORM record_count sum {record_count_sum} does not equal record rows {len(records)}"
        )

    for row in records:
        if not row["iclass"] or not row["iform"]:
            fail(f"record {row.get('record_index', '?')} lacks ICLASS or IFORM")
        for col in ("mode_16", "mode_32", "mode_64"):
            if row[col] not in BOOLEAN:
                fail(f"record {row['record_index']} has invalid {col}={row[col]!r}")
        if row["vendor_scope"] not in VENDOR_SCOPES:
            fail(
                f"record {row['record_index']} has invalid vendor_scope={row['vendor_scope']!r}"
            )
        if row["vendor_scope"] != "unspecified" and not row["vendor_evidence"]:
            fail(f"record {row['record_index']} has vendor scope without evidence")
        if not row["source_revision"] or not row["source_reference"]:
            fail(f"record {row['record_index']} lacks source provenance")

    print(
        f"validated {len(records):,} XED records, {len(iclasses):,} ICLASSes, "
        f"and {len(iforms):,} unique IFORMs"
    )


if __name__ == "__main__":
    main()
