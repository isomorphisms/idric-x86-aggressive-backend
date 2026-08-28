#!/usr/bin/env python3
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path

from backend.idric_x86 import CODE_OFFSET, compile_file, lower_bootstrap_source

ROOT = Path(__file__).resolve().parents[1]


class BootstrapTest(unittest.TestCase):
    def test_rejects_source_outside_frozen_form(self) -> None:
        with self.assertRaises(ValueError):
            lower_bootstrap_source('main = putStrLn "X"')

    def test_direct_elf_runs_and_has_no_dynamic_surface(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "print-x"
            listing = Path(directory) / "print-x.instructions"
            compile_file(ROOT / "fixtures/print_x.idric", output, listing)
            image = output.read_bytes()
            self.assertEqual(image[:4], b"\x7fELF")
            self.assertEqual(struct.unpack_from("<H", image, 16)[0], 2)
            self.assertEqual(struct.unpack_from("<H", image, 18)[0], 62)
            self.assertEqual(struct.unpack_from("<Q", image, 32)[0], 64)
            self.assertEqual(struct.unpack_from("<Q", image, 40)[0], 0)
            self.assertEqual(image[CODE_OFFSET:CODE_OFFSET + 2], b"\x48\xc7")
            self.assertNotIn(b"RefC", image)
            self.assertNotIn(b"libc", image)
            run = subprocess.run([output], check=False, capture_output=True)
            self.assertEqual(run.returncode, 0)
            self.assertEqual(run.stdout, b"X")
            self.assertEqual(run.stderr, b"")
            self.assertIn("syscall", listing.read_text())


if __name__ == "__main__":
    unittest.main()
