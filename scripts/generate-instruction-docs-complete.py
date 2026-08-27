#!/usr/bin/env python3
"""Complete the reviewed semantic coverage for the final three special ICLASSes."""

from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "instruction_docs_reviewed", HERE / "generate-instruction-docs-reviewed.py"
)
reviewed = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(reviewed)

previous = reviewed.base.general_semantics

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


reviewed.base.general_semantics = complete_general_semantics

if __name__ == "__main__":
    reviewed.base.main()
