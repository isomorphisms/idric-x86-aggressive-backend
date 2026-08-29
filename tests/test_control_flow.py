import subprocess
import tempfile
import unittest
from pathlib import Path

from backend.x86_control import CodeBuilder, fixed_string_count_code, fixed_string_count_elf


class ControlFlowTest(unittest.TestCase):
    def run_counter(self, haystack: bytes, needle: bytes) -> tuple[int, str, bytes]:
        image, listing = fixed_string_count_elf(haystack, needle)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "count"
            path.write_bytes(image)
            path.chmod(0o755)
            run = subprocess.run([path], check=False, capture_output=True)
        self.assertEqual(run.stdout, b"")
        self.assertEqual(run.stderr, b"")
        return run.returncode, listing, image

    def test_overlapping_fixed_string_count(self) -> None:
        status, listing, _ = self.run_counter(b"AAAAA", b"AAA")
        self.assertEqual(status, 3)
        self.assertIn("movzx ebx, byte [rsi + rcx + 2]", listing)
        self.assertIn("jne next", listing)
        self.assertIn("jae done", listing)

    def test_absent_and_too_long_needles(self) -> None:
        self.assertEqual(self.run_counter(b"ACGTACGT", b"TT")[0], 0)
        self.assertEqual(self.run_counter(b"ACG", b"ACGT")[0], 0)

    def test_embedded_nul_is_data(self) -> None:
        self.assertEqual(self.run_counter(b"A\x00A\x00A", b"\x00A")[0], 2)

    def test_empty_pattern_is_explicitly_unsettled(self) -> None:
        with self.assertRaisesRegex(ValueError, "empty-pattern semantics"):
            fixed_string_count_code(b"abc", b"")

    def test_exit_status_oracle_does_not_silently_truncate(self) -> None:
        with self.assertRaisesRegex(ValueError, "process exit status"):
            fixed_string_count_code(b"A" * 258, b"AAA")

    def test_high_byte_values_compare_as_unsigned_data(self) -> None:
        self.assertEqual(
            self.run_counter(bytes([0xFF, 0x80, 0xFF]), bytes([0xFF]))[0],
            2,
        )

    def test_output_is_deterministic(self) -> None:
        first = fixed_string_count_elf(b"ACGTACGT", b"ACGT")
        second = fixed_string_count_elf(b"ACGTACGT", b"ACGT")
        self.assertEqual(first, second)

    def test_unresolved_label_fails_closed(self) -> None:
        builder = CodeBuilder()
        builder.jump("missing")
        with self.assertRaisesRegex(ValueError, "undefined label"):
            builder.finish()


if __name__ == "__main__":
    unittest.main()
