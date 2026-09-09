#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import pathlib
import struct
import subprocess
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from backend.complex_projective import (
    build_corpus_elf,
    build_render_elf,
    exp_error_bound,
    f32,
    floating_error_bound,
)


def run_candidate(path: pathlib.Path) -> bytes:
    result = subprocess.run(
        [str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
    )
    if result.returncode != 0:
        error = result.stderr.decode(errors="replace")
        raise RuntimeError(f"candidate {path.name} exited {result.returncode}: {error}")
    return result.stdout


def exact_f32(actual: float, expected: float) -> None:
    if struct.pack("<f", actual) != struct.pack("<f", f32(expected)):
        raise AssertionError(
            f"exact Float32 mismatch: {actual!r} != {f32(expected)!r}"
        )


def close(actual: float, expected: float, tolerance: float) -> None:
    if not math.isfinite(actual) or abs(actual - expected) > tolerance:
        raise AssertionError(
            f"floating mismatch: {actual!r} vs {expected!r}, tolerance {tolerance!r}"
        )


def pair(values: tuple[float, ...], names: list[str], prefix: str) -> complex:
    return complex(
        values[names.index(prefix + ".re")],
        values[names.index(prefix + ".im")],
    )


def validate(corpus: dict, names: list[str], values: tuple[float, ...]) -> dict:
    complex_cases = corpus["complex"]
    epsilon = float(corpus["precision"]["epsilon"])

    for key in ["add", "multiply", "conjugate", "power_two", "polynomial"]:
        actual = pair(values, names, key)
        expected = complex_cases[key]["expected"]
        exact_f32(actual.real, expected[0])
        exact_f32(actual.imag, expected[1])

    exact_f32(
        values[names.index("magnitude_squared")],
        complex_cases["magnitude_squared"]["expected"],
    )

    for key in ["reciprocal", "divide", "rational"]:
        actual = pair(values, names, key)
        expected = complex(*complex_cases[key]["expected"])
        tolerance = floating_error_bound(expected, 32, epsilon)
        close(actual.real, expected.real, tolerance)
        close(actual.imag, expected.imag, tolerance)

    exponential = complex_cases["exponential"]
    actual_exp = pair(values, names, "exponential")
    expected_exp = complex(*exponential["expected_oracle"])
    degree = int(exponential["implementation"]["degree"])
    exp_bound = exp_error_bound(exponential["value"], degree, epsilon)
    if abs(actual_exp - expected_exp) > exp_bound:
        raise AssertionError(
            f"exp error {abs(actual_exp - expected_exp)} exceeds derived bound {exp_bound}"
        )

    polar = complex_cases["polar_round_trip"]
    polar_tolerance = 64 * epsilon * max(
        1.0, float(polar["expected_magnitude_oracle"])
    )
    close(
        values[names.index("polar.magnitude")],
        float(polar["expected_magnitude_oracle"]),
        polar_tolerance,
    )
    close(
        values[names.index("polar.phase_turns")],
        float(polar["expected_phase_turns"]),
        64 * epsilon,
    )
    close(
        values[names.index("polar.round_trip_re")],
        float(polar["cartesian"][0]),
        polar_tolerance,
    )
    close(
        values[names.index("polar.round_trip_im")],
        float(polar["cartesian"][1]),
        polar_tolerance,
    )

    for prefix in ["projective.real_scale", "projective.phase_scale"]:
        residual = values[names.index(prefix + ".rescaling_error_squared")]
        if abs(residual) > 64 * epsilon:
            raise AssertionError(f"{prefix} residual {residual}")

    non_equivalent = values[
        names.index("projective.non_equivalent.wedge_error_squared")
    ]
    if not math.isfinite(non_equivalent) or non_equivalent <= 1024 * epsilon:
        raise AssertionError(
            f"non-equivalent projective points collapsed: {non_equivalent}"
        )

    affine = corpus["projective"]["affine_chart_cp1"]["expected_round_trip"][0]
    exact_f32(values[names.index("affine_chart.re")], affine[0])
    exact_f32(values[names.index("affine_chart.im")], affine[1])

    return {
        "exp_bound": exp_bound,
        "non_equivalent_wedge_error_squared": non_equivalent,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--artifacts", required=True)
    parser.add_argument("--backend-sha", default=os.environ.get("GITHUB_SHA", "local"))
    parser.add_argument(
        "--idric-sha", default=os.environ.get("IDRIC_COMPLEX_SHA", "unknown")
    )
    args = parser.parse_args()

    corpus_path = pathlib.Path(args.corpus)
    artifacts = pathlib.Path(args.artifacts)
    artifacts.mkdir(parents=True, exist_ok=True)
    corpus = json.loads(corpus_path.read_text())

    corpus_elf, names = build_corpus_elf(corpus)
    render_elf, header = build_render_elf(corpus)
    corpus_executable = artifacts / "complex-corpus.elf"
    render_executable = artifacts / "complex-render.elf"
    corpus_executable.write_bytes(corpus_elf)
    render_executable.write_bytes(render_elf)
    corpus_executable.chmod(0o755)
    render_executable.chmod(0o755)

    first = run_candidate(corpus_executable)
    second = run_candidate(corpus_executable)
    if first != second:
        raise AssertionError("complex corpus candidate is not byte-deterministic")
    values = struct.unpack("<" + "f" * (len(first) // 4), first)
    if len(values) != len(names):
        raise AssertionError("candidate result layout length mismatch")
    checks = validate(corpus, names, values)
    (artifacts / "complex-corpus.bin").write_bytes(first)

    scene_first = run_candidate(render_executable)
    scene_second = run_candidate(render_executable)
    if scene_first != scene_second:
        raise AssertionError("headless render is not byte-deterministic")
    if not scene_first.startswith(header):
        raise AssertionError("render did not emit expected PPM header")
    payload = scene_first[len(header) :]
    expected_payload = int(corpus["render"]["width"]) * int(
        corpus["render"]["height"]
    ) * 3
    if len(payload) != expected_payload:
        raise AssertionError("render payload length mismatch")
    if len(set(payload)) < 64 or min(payload) == max(payload):
        raise AssertionError("render did not exercise varying complex state")
    (artifacts / "complex-projective-scene.ppm").write_bytes(scene_first)

    corpus_source = corpus_path.read_bytes()
    receipt = {
        "schema": "idric-x86-complex-projective-receipt-v1",
        "backend_repository": "isomorphisms/idric-x86-aggressive-backend",
        "backend_sha": args.backend_sha,
        "idric_repository": "isomorphisms/Idric",
        "idric_sha": args.idric_sha,
        "corpus_sha256": hashlib.sha256(corpus_source).hexdigest(),
        "precision": corpus["precision"]["name"],
        "candidate": (
            "direct ELF64 x86-64; scalar SSE + x87 observation; "
            "no C/assembler/linker/libc/libm"
        ),
        "stages": {
            "direct_elf64_generation": "PASS",
            "native_numerical_execution": "PASS",
            "projective_equivalence": "PASS",
            "bounded_complex_exponential": "PASS",
            "polar_observation_round_trip": "PASS",
            "headless_render": "PASS",
            "deterministic_regeneration": "PASS",
        },
        "complex_corpus_elf_sha256": hashlib.sha256(corpus_elf).hexdigest(),
        "complex_corpus_output_sha256": hashlib.sha256(first).hexdigest(),
        "render_elf_sha256": hashlib.sha256(render_elf).hexdigest(),
        "render_ppm_sha256": hashlib.sha256(scene_first).hexdigest(),
        "render_statistics": {
            "payload_bytes": len(payload),
            "minimum_byte": min(payload),
            "maximum_byte": max(payload),
            "distinct_byte_values": len(set(payload)),
            "mean_byte": sum(payload) / len(payload),
        },
        "derived_bounds": checks,
    }
    (artifacts / "receipt.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    )
    with (artifacts / "receipt.tsv").open("w") as output:
        output.write("COMPLEX_PROJECTIVE_X86\t1\n")
        output.write(f"backend_sha\t{args.backend_sha}\n")
        output.write(f"idric_sha\t{args.idric_sha}\n")
        output.write(f"corpus_sha256\t{receipt['corpus_sha256']}\n")
        for stage, status in receipt["stages"].items():
            output.write(f"stage\t{stage}\t{status}\n")
        output.write(f"render_ppm_sha256\t{receipt['render_ppm_sha256']}\n")
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
