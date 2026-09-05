#!/usr/bin/env python3
"""Regression checks for normalized metadata rendered into instruction pages."""

from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "instruction_docs_complete", HERE / "generate-instruction-docs-complete.py"
)
complete = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(complete)

PINS = {
    "intel_xed": {"release": "test", "commit": "test"},
    "intel_sdm": {"revision": "test"},
}


def row(**overrides):
    value = {
        "extension": "BASE",
        "category": "BINARY",
        "vendor_scope": "amd-only",
        "isa_set": "AMD",
        "iform": "TEST_IFORM",
        "disasm_intel": "test",
        "mode_restriction": "",
        "cpl": "3",
        "explicit_operands": "REG0 REG1",
        "implicit_operands": "RFLAGS",
        "flags_read": "ZF",
        "flags_written": "ZF",
        "flags_undefined": "CF OF",
        "flags_raw": "MUST [ z-mod ] MAY [ c-u o-u ]",
    }
    value.update(overrides)
    return value


def require(condition, message):
    if not condition:
        raise SystemExit(f"instruction-doc rendering validation failed: {message}")


def main():
    reviewed_text, _ = complete.reviewed.base.page("BSF", [row()], PINS)
    unreviewed_text, _ = complete.reviewed.base.page(
        "ADD", [row(vendor_scope="intel-only", isa_set="I86")], PINS
    )

    require("vendor classification: `amd-only`" in reviewed_text, "vendor_scope was not rendered")
    require("shared-or-unspecified" not in reviewed_text, "legacy vendor fallback returned")

    require("Recorded flag behavior: read `ZF`" in reviewed_text, "flags_read was not rendered")
    require("written `ZF`" in reviewed_text, "flags_written was not rendered")
    require("undefined `CF OF`" in reviewed_text, "flags_undefined was not rendered")
    require("raw XED `MUST [ z-mod ] MAY [ c-u o-u ]`" in reviewed_text, "flags_raw was not rendered")

    require("XED CPL metadata: `3`" in reviewed_text, "CPL metadata disappeared")
    require(
        "does not establish processor or feature availability" in reviewed_text,
        "CPL metadata is still being used as availability evidence",
    )
    require("usable at CPL 3" not in reviewed_text, "legacy CPL availability wording returned")

    require(
        "Manual Intel/AMD review: recorded for this ICLASS" in reviewed_text,
        "reviewed overlay row was not reflected",
    )
    require(
        "Manual Intel/AMD review: unreviewed for this ICLASS" in unreviewed_text,
        "unreviewed ICLASS was not marked unreviewed",
    )
    require(
        "vendor-specific availability and semantic cross-checks" not in unreviewed_text,
        "unreviewed AMD cross-check overclaim returned",
    )

    print("validated normalized instruction-document rendering")


if __name__ == "__main__":
    main()
