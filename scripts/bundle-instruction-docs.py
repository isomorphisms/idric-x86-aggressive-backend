#!/usr/bin/env python3
"""Bundle generated per-ICLASS pages into a small family reference.

The semantic generators deliberately work one ICLASS at a time because that makes
coverage and fallback auditing simple.  The checked-in documentation does not
need to mirror that implementation detail.  This script preserves each page's
full prose while collecting the pages into a small, deterministic set of family
files.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC_DIR = ROOT / "docs" / "instructions"
ICLASS_FILE = ROOT / "generated" / "xed-iclasses.txt"

BUNDLES = {
    "core-integer-and-data-movement.md": "Core integer and data movement",
    "control-flow-stack-and-strings.md": "Control flow, stack, and strings",
    "bit-manipulation-and-atomics.md": "Bit manipulation and atomics",
    "x87-mmx-and-simd.md": "x87, MMX, and SSE SIMD",
    "avx-fma-and-modern-vector.md": "AVX, FMA, and modern vector",
    "avx512-and-avx10.md": "AVX-512 and AVX10",
    "crypto-random-and-hashing.md": "Cryptography, random, and hashing",
    "matrix-tile-and-ai.md": "Matrix, tile, and AI extensions",
    "system-state-and-privileged.md": "System, processor state, and privileged operations",
    "virtualization-and-confidential-computing.md": "Virtualization and confidential computing",
    "security-enclaves-and-control-flow-protection.md": "Security, enclaves, and control-flow protection",
    "legacy-vendor-and-specialized.md": "Legacy, vendor-specific, and specialized extensions",
}


def read_iclasses() -> list[str]:
    names = [line.strip() for line in ICLASS_FILE.read_text().splitlines() if line.strip()]
    if len(names) != len(set(names)):
        raise SystemExit("generated/xed-iclasses.txt contains duplicate ICLASS names")
    return names


def metadata(page: str) -> dict[str, str]:
    labels = {
        "extension": "XED extension(s)",
        "category": "XED category/categories",
        "isa": "ISA set(s)",
        "vendor": "vendor classification",
    }
    result: dict[str, str] = {}
    for key, label in labels.items():
        match = re.search(rf"^- {re.escape(label)}: (.+)$", page, flags=re.MULTILINE | re.IGNORECASE)
        result[key] = match.group(1).upper() if match else ""
    return result


def has(text: str, *needles: str) -> bool:
    return any(needle in text for needle in needles)


def classify(iclass: str, page: str) -> str:
    meta = metadata(page)
    extension = meta["extension"]
    category = meta["category"]
    isa = meta["isa"]
    vendor = meta["vendor"]
    name = iclass.upper()
    feature = " ".join((extension, category, isa))

    # Put the most architectural/specialized families first so a token such as
    # AVX512 inside a TDX or AMX ISA-set name cannot steal the instruction.
    if has(feature, "AMX", "ACE_", "ACE `", "TILE", "TMUL") or name.startswith(("TILE", "TCMM", "TDP", "TMM", "BSR")):
        return "matrix-tile-and-ai.md"

    if has(feature, "VMX", "SVM", "TDX", "SEAM", "SEV", "SNP", "RMP") or name.startswith(
        ("VM", "INVEPT", "INVVPID", "RMP", "PVALIDATE", "SEAM", "TD")
    ):
        return "virtualization-and-confidential-computing.md"

    if has(feature, "SGX", "CET", "FRED", "SMX", "KEYLOCKER", "UINTR", "PKU", "PKS", "MPX") or name.startswith(
        ("ENCL", "ENCLS", "ENCLU", "GETSEC", "ERET", "LKGS", "WRSS", "WRUSS", "UIRET", "SENDUIPI")
    ):
        return "security-enclaves-and-control-flow-protection.md"

    if has(feature, "AES", "SHA", "SM3", "SM4", "GFNI", "PCLMUL", "VAES", "VPCLMUL", "RDRAND", "RDSEED") or name.startswith(
        ("AES", "VAES", "SHA", "VPSHA", "SM3", "VSM3", "SM4", "VSM4", "GF2P8", "PCLMUL", "VPCLMUL", "RDRAND", "RDSEED")
    ):
        return "crypto-random-and-hashing.md"

    if has(feature, "AVX512", "AVX10"):
        return "avx512-and-avx10.md"

    if has(feature, "AVX", "FMA", "F16C"):
        return "avx-fma-and-modern-vector.md"

    if has(feature, "SSE", "MMX", "X87", "3DNOW"):
        return "x87-mmx-and-simd.md"

    if has(feature, "BMI", "TBM", "LZCNT", "POPCNT", "RAO", "RTM", "HLE") or name.startswith(
        (
            "ANDN", "BEXTR", "BLS", "BZH", "CMPXCHG", "MULX", "PDEP", "PEXT", "RORX",
            "SARX", "SHLX", "SHRX", "TZCNT", "LZCNT", "POPCNT", "XADD", "BT", "BTS", "BTR", "BTC",
        )
    ):
        return "bit-manipulation-and-atomics.md"

    control_categories = (
        "CALL", "COND_BR", "UNCOND_BR", "RET", "PUSH", "POP", "STRINGOP", "IOSTRINGOP",
    )
    control_names = (
        "CALL", "J", "LOOP", "RET", "PUSH", "POP", "ENTER", "LEAVE", "MOVS", "CMPS", "SCAS",
        "STOS", "LODS", "INS", "OUTS", "IRET",
    )
    if has(category, *control_categories) or name.startswith(control_names):
        return "control-flow-stack-and-strings.md"

    system_tokens = (
        "SYSTEM", "MSR", "XSAVE", "XRSTOR", "XSTATE", "SYSCALL", "SYSRET", "INVPCID", "INVLPG",
        "CACHE", "CLFLUSH", "CLWB", "WBINVD", "MONITOR", "MWAIT", "APIC", "PCONFIG",
    )
    system_names = (
        "CPUID", "RDTSC", "RDTSCP", "RDMSR", "WRMSR", "XGETBV", "XSETBV", "XSAVE", "XRSTOR",
        "INVL", "INVPCID", "LGDT", "LIDT", "SGDT", "SIDT", "LLDT", "SLDT", "LTR", "STR",
        "HLT", "CLI", "STI", "WBINVD", "INVD", "CLFLUSH", "CLWB", "MONITOR", "MWAIT", "SYSCALL", "SYSRET",
    )
    if has(feature, *system_tokens) or name.startswith(system_names):
        return "system-state-and-privileged.md"

    # Only use the explicit vendor-classification field here.  Every page cites
    # both Intel and AMD manuals in Sources, so searching the whole page for AMD
    # would incorrectly sweep ordinary shared instructions into this bucket.
    if vendor and vendor != "`SHARED-OR-UNSPECIFIED`" or has(feature, "XOP", "SSE4A", "CYRIX", "VIA", "PADLOCK"):
        return "legacy-vendor-and-specialized.md"

    return "core-integer-and-data-movement.md"


def demote_headings(page: str) -> str:
    return re.sub(r"^(#{1,5})(?= )", lambda m: "#" + m.group(1), page, flags=re.MULTILINE).strip()


def render_bundle(title: str, names: list[str], pages: dict[str, str]) -> str:
    intro = (
        f"# {title}\n\n"
        f"This generated bundle contains {len(names)} XED ICLASS reference sections. "
        "Each section preserves the instruction-specific semantic prose, availability, architectural effects, "
        "representative forms, backend notes, and pinned sources from the per-ICLASS semantic generator.\n\n"
    )
    body = "\n\n---\n\n".join(demote_headings(pages[name]) for name in names)
    return intro + body + "\n"


def write_bundles(iclasses: list[str]) -> None:
    pages: dict[str, str] = {}
    missing: list[str] = []
    for name in iclasses:
        path = DOC_DIR / f"{name}.md"
        if not path.exists():
            missing.append(name)
        else:
            pages[name] = path.read_text()
    if missing:
        raise SystemExit(f"missing {len(missing)} generated per-ICLASS pages; first: {missing[:10]}")

    grouped: dict[str, list[str]] = defaultdict(list)
    for name in iclasses:
        grouped[classify(name, pages[name])].append(name)

    assigned = [name for bundle in BUNDLES for name in grouped[bundle]]
    counts = Counter(assigned)
    duplicates = sorted(name for name, count in counts.items() if count != 1)
    if set(assigned) != set(iclasses) or duplicates:
        raise SystemExit("bundle assignment is not an exact one-to-one cover of the ICLASS oracle")

    DOC_DIR.mkdir(parents=True, exist_ok=True)
    for path in DOC_DIR.glob("*.md"):
        path.unlink()

    readme_lines = [
        "# x86 instruction reference",
        "",
        "The pinned XED inventory currently contains " + f"**{len(iclasses):,} ICLASS values**.  The semantic generator still audits each ICLASS individually, but the checked-in reference is bundled by broad architectural family so it is practical to browse.",
        "",
        "A section existing here means the instruction is documented, not that the Idriç backend supports or emits it.",
        "",
        "| Bundle | ICLASS sections |",
        "| --- | ---: |",
    ]

    for filename, title in BUNDLES.items():
        names = sorted(grouped[filename])
        (DOC_DIR / filename).write_text(render_bundle(title, names, pages))
        readme_lines.append(f"| [{title}]({filename}) | {len(names):,} |")

    readme_lines += [
        "",
        f"**Total: {len(iclasses):,} ICLASS sections.**",
        "",
        "`scripts/bundle-instruction-docs.py --check` verifies that every name in `generated/xed-iclasses.txt` appears exactly once as an instruction section and that no per-ICLASS Markdown files remain checked in.",
        "",
    ]
    (DOC_DIR / "README.md").write_text("\n".join(readme_lines))

    print(f"bundled {len(iclasses)} instruction sections into {len(BUNDLES)} family files")
    for filename, title in BUNDLES.items():
        print(f"  {filename}: {len(grouped[filename])}")


def check_bundles(iclasses: list[str]) -> None:
    expected_files = set(BUNDLES) | {"README.md"}
    actual_files = {path.name for path in DOC_DIR.glob("*.md")}
    unexpected = sorted(actual_files - expected_files)
    missing_files = sorted(expected_files - actual_files)
    if unexpected or missing_files:
        raise SystemExit(f"bundle file set mismatch; unexpected={unexpected[:10]} missing={missing_files}")

    seen: list[str] = []
    for filename in BUNDLES:
        text = (DOC_DIR / filename).read_text()
        seen.extend(re.findall(r"^## ([A-Z0-9_]+)$", text, flags=re.MULTILINE))

    counts = Counter(seen)
    duplicate = sorted(name for name, count in counts.items() if count != 1)
    missing = sorted(set(iclasses) - set(seen))
    extra = sorted(set(seen) - set(iclasses))
    if duplicate or missing or extra or len(seen) != len(iclasses):
        raise SystemExit(
            "bundle coverage mismatch: "
            f"sections={len(seen)} expected={len(iclasses)} duplicate={duplicate[:10]} "
            f"missing={missing[:10]} extra={extra[:10]}"
        )

    print(f"checked {len(seen)} instruction sections across {len(BUNDLES)} family files; exact coverage")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify the canonical bundled layout and exact ICLASS coverage")
    args = parser.parse_args()

    iclasses = read_iclasses()
    if args.check:
        check_bundles(iclasses)
    else:
        write_bundles(iclasses)


if __name__ == "__main__":
    main()
