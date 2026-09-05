#!/usr/bin/env python3
"""Complete reviewed semantic coverage and render normalized ISA metadata accurately."""

from __future__ import annotations

import csv
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SPEC = importlib.util.spec_from_file_location(
    "instruction_docs_reviewed", HERE / "generate-instruction-docs-reviewed.py"
)
reviewed = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(reviewed)

previous = reviewed.base.general_semantics
base_page = reviewed.base.page

LAST = {
    "EXTRQ": "extracts a bit field from the low 64 bits of an XMM register using AMD SSE4a semantics, placing the selected field in the low bits and clearing the remainder of the low quadword; the field length and starting bit come from immediates or the control XMM operand depending on the form",
    "GETSEC": "dispatches an Intel Safer Mode Extensions leaf selected by EAX, providing the architectural entry point for measured-launch and authenticated-code operations such as capability queries, SENTER, SEXIT, ENTERACCS, and EXITAC",
    "TZMSK": "forms AMD TBM's mask from trailing zeros: it sets every bit below the source's least-significant set bit and clears that set bit and all higher bits, equivalently computing the bit pattern of (~src) AND (src - 1)",
}


def complete_general_semantics(name, rows):
    desc, fallback = previous(name, rows)
    if not fallback:
        return desc, False
    if name in LAST:
        return LAST[name], False
    return desc, True


def vendor_scopes(rows):
    return sorted({row.get("vendor_scope", "").strip() or "unspecified" for row in rows})


def flag_summary(rows):
    return "; ".join(
        [
            f"read {reviewed.base.preview_values(rows, 'flags_read')}",
            f"written {reviewed.base.preview_values(rows, 'flags_written')}",
            f"undefined {reviewed.base.preview_values(rows, 'flags_undefined')}",
            f"raw XED {reviewed.base.preview_values(rows, 'flags_raw')}",
        ]
    )


def cpl_summary(rows):
    values = sorted({row.get("cpl", "").strip() for row in rows if row.get("cpl", "").strip()})
    rendered = ", ".join(f"`{value}`" for value in values) if values else "not uniformly recorded"
    return (
        f"XED CPL metadata: {rendered}; this records privilege metadata only and does not establish "
        "processor or feature availability"
    )


def reviewed_iclasses():
    table = ROOT / "research" / "vendor-differences.tsv"
    if not table.exists():
        return set()
    with table.open(newline="") as handle:
        return {
            row["iclass"].strip()
            for row in csv.DictReader(handle, delimiter="\t")
            if row.get("iclass", "").strip()
        }


REVIEWED_ICLASSES = reviewed_iclasses()


def manual_review_source(iclass):
    if iclass in REVIEWED_ICLASSES:
        return (
            "- Manual Intel/AMD review: recorded for this ICLASS in `research/vendor-differences.tsv`; "
            "that sparse row names the pinned references and the portable rule."
        )
    return (
        "- Manual Intel/AMD review: unreviewed for this ICLASS. Pinned AMD APM revisions are reference "
        "inputs, not evidence of a completed per-instruction semantic or availability cross-check."
    )


def corrected_page(iclass, rows, pins):
    text, fallback = base_page(iclass, rows, pins)
    vendor_line = f"- vendor classification: {', '.join(f'`{scope}`' for scope in vendor_scopes(rows))}"
    flags_line = f"Recorded flag behavior: {flag_summary(rows)}."
    source_line = manual_review_source(iclass)

    corrected = []
    for line in text.splitlines():
        if line.startswith("- vendor classification:"):
            corrected.append(vendor_line)
        elif line.startswith("Recorded flag behavior:"):
            corrected.append(flags_line)
        elif line.startswith("- AMD64 Architecture Programmer's Manual revisions pinned"):
            corrected.append(source_line)
        else:
            corrected.append(line)
    return "\n".join(corrected), fallback


reviewed.base.general_semantics = complete_general_semantics
reviewed.base.cpl_summary = cpl_summary
reviewed.base.page = corrected_page

if __name__ == "__main__":
    reviewed.base.main()
