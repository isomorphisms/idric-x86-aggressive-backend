#!/usr/bin/env python3

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


def text(value):
    if value is None:
        return ""
    if isinstance(value, list):
        return " ".join(str(x) for x in value)
    if isinstance(value, dict):
        return json.dumps(value, sort_keys=True, separators=(",", ":"))
    return str(value)


def markdown(value):
    return str(value).replace("|", "\\|")


def vendor(record):
    attrs = set(record.get("attributes") or [])
    extension = (record.get("extension") or "").upper()
    if "AMDONLY" in attrs:
        return "AMD"
    if "INTELONLY" in attrs:
        return "Intel"
    if extension in {"3DNOW", "3DNOW_PREFETCH", "XOP", "FMA4", "TBM", "SVM"}:
        return "AMD"
    return "shared-or-unspecified"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("xed_json", type=Path)
    parser.add_argument("--out-dir", type=Path, default=Path("generated"))
    parser.add_argument(
        "--summary",
        type=Path,
        default=Path("docs/x86-isa-inventory.generated.md"),
    )
    args = parser.parse_args()

    db = json.loads(args.xed_json.read_text())
    records = db["Instructions"]
    version = db.get("Version", "unknown")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    args.summary.parent.mkdir(parents=True, exist_ok=True)

    iclasses = sorted({r["iclass"] for r in records if r.get("iclass")})
    iforms = sorted({r["iform"] for r in records if r.get("iform")})
    extensions = sorted({r.get("extension") or "UNKNOWN" for r in records})
    categories = sorted({r.get("category") or "UNKNOWN" for r in records})

    (args.out_dir / "xed-iclasses.txt").write_text("\n".join(iclasses) + "\n")
    (args.out_dir / "xed-iforms.txt").write_text("\n".join(iforms) + "\n")

    columns = [
        "iclass",
        "iform",
        "disasm_intel",
        "category",
        "extension",
        "isa_set",
        "cpl",
        "mode_restriction",
        "eosz_list",
        "easz_list",
        "operand_list",
        "explicit_operands",
        "implicit_operands",
        "flags",
        "encoding_space",
        "pattern",
        "attributes",
        "undocumented",
        "vendor",
    ]

    with (args.out_dir / "xed-instructions.tsv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter="\t")
        writer.writeheader()
        for r in records:
            row = {key: text(r.get(key)) for key in columns if key != "vendor"}
            row["vendor"] = vendor(r)
            writer.writerow(row)

    ext_records = Counter()
    ext_iclasses = defaultdict(set)
    ext_iforms = defaultdict(set)
    cat_records = Counter()
    cat_iclasses = defaultdict(set)

    for r in records:
        ext = r.get("extension") or "UNKNOWN"
        cat = r.get("category") or "UNKNOWN"
        ext_records[ext] += 1
        cat_records[cat] += 1
        if r.get("iclass"):
            ext_iclasses[ext].add(r["iclass"])
            cat_iclasses[cat].add(r["iclass"])
        if r.get("iform"):
            ext_iforms[ext].add(r["iform"])

    lines = [
        "# Generated x86 ISA inventory",
        "",
        "> Generated from pinned Intel XED metadata. Do not hand-edit this file.",
        "",
        f"XED version: `{version}`",
        "",
        f"- instruction records: **{len(records):,}**",
        f"- unique instruction classes (ICLASS): **{len(iclasses):,}**",
        f"- unique instruction forms (IFORM): **{len(iforms):,}**",
        f"- XED extensions: **{len(extensions):,}**",
        f"- XED categories: **{len(categories):,}**",
        "",
        "The complete mnemonic-class list is in `generated/xed-iclasses.txt`. ",
        "The concrete form list is in `generated/xed-iforms.txt`. ",
        "The full row-level metadata is in `generated/xed-instructions.tsv`.",
        "",
        "## By XED extension",
        "",
        "| extension | ICLASSes | IFORMs | records |",
        "|---|---:|---:|---:|",
    ]

    for ext in sorted(ext_records):
        lines.append(
            f"| {markdown(ext)} | {len(ext_iclasses[ext]):,} | "
            f"{len(ext_iforms[ext]):,} | {ext_records[ext]:,} |"
        )

    lines.extend(
        [
            "",
            "## By XED category",
            "",
            "| category | ICLASSes | records |",
            "|---|---:|---:|",
        ]
    )

    for cat in sorted(cat_records):
        lines.append(
            f"| {markdown(cat)} | {len(cat_iclasses[cat]):,} | {cat_records[cat]:,} |"
        )

    lines.extend(
        [
            "",
            "## Inventory rule",
            "",
            "Inventory completeness and backend support are different questions. "
            "Nothing in these generated files implies that the Idriç backend should emit "
            "every listed instruction. Backend support should be tracked separately.",
            "",
        ]
    )

    args.summary.write_text("\n".join(lines))


if __name__ == "__main__":
    main()
