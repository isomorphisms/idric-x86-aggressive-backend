#!/usr/bin/env python3
"""Run the unit suite and optionally make every skip a failure."""

from __future__ import annotations

import argparse
import sys
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fail-on-skip", action="store_true")
    arguments = parser.parse_args()
    suite = unittest.defaultTestLoader.discover(str(REPOSITORY_ROOT / "tests"))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if arguments.fail_on_skip and result.skipped:
        for test, reason in result.skipped:
            print(f"unexpected SKIP: {test}: {reason}", file=sys.stderr)
        raise SystemExit(1)
    raise SystemExit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
