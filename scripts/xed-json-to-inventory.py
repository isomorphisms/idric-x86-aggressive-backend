#!/usr/bin/env python3

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

FLAG_ACTIONS = {"mod", "tst", "u", "0", "1", "ah", "pop"}


def text(value):
    if value is None:
        return ""
    if isinstance(value, list):
        return " ".join(str(x) for x in value)
    if isinstance(value, dict):
        return json.dumps(value, sort_keys=True, separators=(",", ":"))
    return str(value)


def json_text(value):
    if value in (None, ""):
        return ""
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def markdown(value):
    return str(value).replace("|", "\\|")


def truth(value):
    return "true" if value else "false"


def normalized_modes(record):
    modes = {int(x) for x in (record.get("mode_restriction") or [])}
    return {
        "mode_16": truth(16 in modes),
        "mode_32": truth(32 in modes),
        "mode_64": truth(64 in modes),
    }


def normalized_flags(raw_flags):
    """Split XED's flag-action syntax without throwing away the raw field.

    XED actions ending in ``-tst`` read a flag. Every other action in XED's
    flag grammar writes a flag; ``-u`` additionally marks an undefined result.
    This follows pysrc/flag_gen.py in the pinned XED source.
    """
    reads = set()
    writes = set()
    undefined = set()

    for flag, action in re.findall(
        r"\b([A-Za-z0-9_]+)-(mod|tst|u|0|1|ah|pop)\b", raw_flags or ""
    ):
        action = action.lower()
        flag = flag.lower()
        if action not in FLAG_ACTIONS:
            continue
        if action == "tst":
            reads.add(flag)
        else:
            writes.add(flag)
            if action == "u":
                undefined.add(flag)

    return {
        "flags_read": " ".join(sorted(reads)),
        "flags_written": " ".join(sorted(writes)),
        "flags_undefined": " ".join(sorted(undefined)),
        "flags_raw": text(raw_flags),
    }


def vendor_scope(record):
    """Return only vendor facts XED states explicitly.

    Absence of AMDONLY/INTELONLY is *not* evidence that a form is shared.
    Architectural Intel/AMD availability and semantic differences therefore
    stay a separate review layer rather than being guessed from extension names.
    """
    attrs = {str(x).upper() for x in (record.get("attributes") or [])}
    isa_set = str(record.get("isa_set") or "").upper()

    if "AMDONLY" in attrs:
        return "amd-only", "attribute:AMDONLY"
    if "INTELONLY" in attrs:
        return "intel-only", "attribute:INTELONLY"
    if isa_set == "AMD":
        return "amd-only", "isa_set:AMD"
    if isa_set == "INTEL":
        return "intel-only", "isa_set:INTEL"
    return "unspecified", ""


def only_or_join(values):
    return "|".join(sorted({str(v) for v in values if v not in (None, "")}))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("xed_json", type=Path)
    parser.add_argument("--out-dir", type=Path, default=Path("generated"))
    parser.add_argument(
        "--summary",
        type=Path,
        default=Path("docs/x86-isa-inventory.generated.md"),
    )
    parser.add_argument("--source-revision", default="")
    parser.add_argument("--source-reference", default="")
    args = parser.parse_args()

    db = json.loads(args.xed_json.read_text())
    records = db["Instructions"]
    version = args.source_revision or db.get("Version", "unknown")
    source_reference = args.source_reference or "intelxed/xed"

    args.out_dir.mkdir(parents=True, exist_ok=True)
    args.summary.parent.mkdir(parents=True, exist_ok=True)

    iclasses = sorted({r["iclass"] for r in records if r.get("iclass")})
    iforms = sorted({r["iform"] for r in records if r.get("iform")})
    extensions = sorted({r.get("extension") or "UNKNOWN" for r in records})
    categories = sorted({r.get("category") or "UNKNOWN" for r in records})

    (args.out_dir / "xed-iclasses.txt").write_text("\n".join(iclasses) + "\n")
    (args.out_dir / "xed-iforms.txt").write_text("\n".join(iforms) + "\n")

    columns = [
        "record_index",
        "iclass",
        "iform",
        "disasm_intel",
        "category",
        "extension",
        "isa_set",
        "cpl",
        "mode_16",
        "mode_32",
        "mode_64",
        "mode_restriction",
        "eosz_list",
        "easz_list",
        "operands",
        "parsed_operands",
        "explicit_operands",
        "implicit_operands",
        "flags_read",
        "flags_written",
        "flags_undefined",
        "flags_raw",
        "encoding_space",
        "encoding_pattern",
        "attributes",
        "undocumented",
        "vendor_scope",
        "vendor_evidence",
        "source_revision",
        "source_reference",
    ]

    normalized_records = []
    with (args.out_dir / "xed-instructions.tsv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns, delimiter="\t")
        writer.writeheader()
        for index, r in enumerate(records):
            scope, evidence = vendor_scope(r)
            row = {
                "record_index": index,
                "iclass": text(r.get("iclass")),
                "iform": text(r.get("iform")),
                "disasm_intel": text(r.get("disasm_intel")),
                "category": text(r.get("category")),
                "extension": text(r.get("extension")),
                "isa_set": text(r.get("isa_set")),
                "cpl": text(r.get("cpl")),
                **normalized_modes(r),
                "mode_restriction": text(r.get("mode_restriction")),
                "eosz_list": text(r.get("eosz_list")),
                "easz_list": text(r.get("easz_list")),
                "operands": text(r.get("operand_list")),
                "parsed_operands": json_text(r.get("parsed_operands")),
                "explicit_operands": text(r.get("explicit_operands")),
                "implicit_operands": text(r.get("implicit_operands")),
                **normalized_flags(r.get("flags")),
                "encoding_space": text(r.get("encoding_space")),
                "encoding_pattern": text(r.get("pattern")),
                "attributes": text(r.get("attributes")),
                "undocumented": truth(bool(r.get("undocumented"))),
                "vendor_scope": scope,
                "vendor_evidence": evidence,
                "source_revision": version,
                "source_reference": source_reference,
            }
            writer.writerow(row)
            normalized_records.append(row)

    by_iform = defaultdict(list)
    for row in normalized_records:
        if row["iform"]:
            by_iform[row["iform"]].append(row)

    form_columns = [
        "iform",
        "iclass",
        "record_count",
        "category",
        "extension",
        "isa_set",
        "cpl",
        "mode_16",
        "mode_32",
        "mode_64",
        "vendor_scope",
        "source_revision",
        "source_reference",
    ]
    with (args.out_dir / "xed-iform-index.tsv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=form_columns, delimiter="\t")
        writer.writeheader()
        for iform in sorted(by_iform):
            rows = by_iform[iform]
            writer.writerow(
                {
                    "iform": iform,
                    "iclass": only_or_join(r["iclass"] for r in rows),
                    "record_count": len(rows),
                    "category": only_or_join(r["category"] for r in rows),
                    "extension": only_or_join(r["extension"] for r in rows),
                    "isa_set": only_or_join(r["isa_set"] for r in rows),
                    "cpl": only_or_join(r["cpl"] for r in rows),
                    "mode_16": truth(any(r["mode_16"] == "true" for r in rows)),
                    "mode_32": truth(any(r["mode_32"] == "true" for r in rows)),
                    "mode_64": truth(any(r["mode_64"] == "true" for r in rows)),
                    "vendor_scope": only_or_join(r["vendor_scope"] for r in rows),
                    "source_revision": version,
                    "source_reference": source_reference,
                }
            )

    ext_records = Counter()
    ext_iclasses = defaultdict(set)
    ext_iforms = defaultdict(set)
    cat_records = Counter()
    cat_iclasses = defaultdict(set)
    vendor_records = Counter()

    for row in normalized_records:
        ext = row["extension"] or "UNKNOWN"
        cat = row["category"] or "UNKNOWN"
        ext_records[ext] += 1
        cat_records[cat] += 1
        vendor_records[row["vendor_scope"]] += 1
        if row["iclass"]:
            ext_iclasses[ext].add(row["iclass"])
            cat_iclasses[cat].add(row["iclass"])
        if row["iform"]:
            ext_iforms[ext].add(row["iform"])

    lines = [
        "# Generated x86 ISA inventory",
        "",
        "> Generated from pinned Intel XED metadata. Do not hand-edit this file.",
        "",
        f"XED revision: `{version}`",
        f"Source: `{source_reference}`",
        "",
        f"- XED instruction records: **{len(records):,}**",
        f"- unique instruction classes (ICLASS): **{len(iclasses):,}**",
        f"- unique concrete forms (IFORM): **{len(iforms):,}**",
        f"- XED extensions: **{len(extensions):,}**",
        f"- XED categories: **{len(categories):,}**",
        "",
        "XED records and IFORMs are deliberately counted separately. `generated/xed-instructions.tsv` "
        "keeps every exported XED record; `generated/xed-iform-index.tsv` has exactly one row per "
        "unique IFORM and reports how many XED records contribute to that form. Repeated IFORMs are "
        "not silently collapsed because their mode, encoding, operand, or other metadata may differ.",
        "",
        "The complete mnemonic-class list is in `generated/xed-iclasses.txt`. ",
        "The concrete form list is in `generated/xed-iforms.txt`. ",
        "The full normalized record-level metadata is in `generated/xed-instructions.tsv`.",
        "",
        "## Vendor scope stated by XED",
        "",
        "`unspecified` means exactly that: the exported XED record did not state a vendor-only marker. "
        "It must not be read as 'shared by Intel and AMD'. Manual cross-checks remain a separate layer.",
        "",
        "| vendor scope | records |",
        "|---|---:|",
    ]

    for scope in sorted(vendor_records):
        lines.append(f"| {markdown(scope)} | {vendor_records[scope]:,} |")

    lines.extend(
        [
            "",
            "## By XED extension",
            "",
            "| extension | ICLASSes | IFORMs | records |",
            "|---|---:|---:|---:|",
        ]
    )

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
            "every listed instruction. Backend support is intentionally tracked outside the "
            "generated inventory.",
            "",
        ]
    )

    args.summary.write_text("\n".join(lines))


if __name__ == "__main__":
    main()
