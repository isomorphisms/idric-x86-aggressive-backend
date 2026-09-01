#!/usr/bin/env python3
import hashlib
import os
import platform
import struct
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from backend.r128_math import (
    CODE_OFFSET,
    ArtifactError,
    compile_artifact,
    decode_observations,
    make_scalar_plan,
    parse_checked_artifact_bytes,
    render_execution_receipt,
    run_native,
)

ROOT = Path(__file__).resolve().parents[1]
DIMENSION = 128
ZERO_TAIL = [0] * 124
X = [3, 4, 12, *ZERO_TAIL, 9]
Y = [5, -2, 7, *ZERO_TAIL, 11]
PHI = list(Y)
SPHERE_BASIS = [*([0] * 127), 1]
H_X = [-3, 4, 12, *ZERO_TAIL, 9]
H_Y = [-5, -2, 7, *ZERO_TAIL, 11]
G_X = [-4, 3, 12, *ZERO_TAIL, 9]
G_Y = [2, 5, 7, *ZERO_TAIL, 11]
G2_X = [-3, -4, 12, *ZERO_TAIL, 9]
G3_X = [4, -3, 12, *ZERO_TAIL, 9]
SPHERE_AFTER = list(SPHERE_BASIS)


def coordinates(values: list[int]) -> str:
    assert len(values) == DIMENSION
    return ",".join(map(str, values))


def checked_artifact_text() -> str:
    source = b"test-only backend fixture; not compiler output\n"
    lines = [
        "EDRIC_MATH_ONE_STEP\t1",
        f"source_sha256\t{hashlib.sha256(source).hexdigest()}",
        "compiler_head\tisomorphisms/Idric\t0000000000000000000000000000000000000000",
        "core_typecheck\tPASS",
        "space\tR128\t128",
        f"value\tphi\tcovector\tR128\t128\texact_integer\t{coordinates(PHI)}",
        f"value\tsphere_basis\tsphere_point\tR128\t128\texact_integer\t{coordinates(SPHERE_BASIS)}",
        f"value\tx\tvector\tR128\t128\texact_integer\t{coordinates(X)}",
        f"value\ty\tvector\tR128\t128\texact_integer\t{coordinates(Y)}",
        "certificate\tcert_same\tSameSpace\tPASS\tunification\tregistry_version=1\tgoal=SameSpaceAndDimension_R128_128\tgenerated_by=contraction_and_dot\tgenerated_term=same_space_R128_128\tcore_typecheck=PASS\treason=unified_named_space_and_dimension\tresolved=R128_128\tresult=solved",
        "certificate\tcert_h\tOrthogonalTransform\tPASS\tstructure_law_instance\tregistry_version=1\tgoal=OrthogonalTransform_H_R128_128_reversing\tgenerated_by=reflection\thypotheses=H_is_first_axis_reflection\tconclusion=H_is_orthogonal_reversing\tresolver=structure_law_instance\tgenerated_term=first_axis_reflection_orthogonal_H\tcore_typecheck=PASS\treason=registered_checked_law\tresolved=H_R128_128\tresult=solved\tlaw=first_axis_reflection_is_orthogonal",
        "certificate\tcert_g\tOrthogonalTransform\tPASS\tstructure_law_instance\tregistry_version=1\tgoal=OrthogonalTransform_G_R128_128_preserving\tgenerated_by=plane_rotation\thypotheses=G_is_exact_first_plane_quarter_turn\tconclusion=G_is_orthogonal_preserving\tresolver=structure_law_instance\tgenerated_term=first_plane_quarter_turn_orthogonal_G\tcore_typecheck=PASS\treason=registered_checked_law\tresolved=G_R128_128\tresult=solved\tlaw=first_plane_quarter_turn_is_orthogonal",
        "certificate\tcert_sphere\tOrthogonalSphereAction\tPASS\tnamed_theorem\tregistry_version=1\tgoal=OrthogonalSphereAction_G_127_128\tgenerated_by=act_on_sphere\thypotheses=G_OrthogonalTransform_R128_and_point_on_S127\tconclusion=G_point_on_S127\tresolver=named_theorem\tcandidates=orthogonal_preserves_unit_sphere\tselected_theorem=orthogonal_preserves_unit_sphere\tgenerated_term=orthogonal_preserves_unit_sphere_G_sphere_basis\tcore_typecheck=PASS\treason=unique_checked_candidate\tresolved=G_S127_R128\tresult=solved\ttheorem=orthogonal_preserves_unit_sphere",
        "certificate\tcert_sphere_norm\tPreservesSquaredNorm\tPASS\tnamed_theorem\tregistry_version=1\tgoal=PreservesSquaredNorm_G_128\tgenerated_by=sphere_squared_norm\thypotheses=G_OrthogonalTransform_R128_preserving\tconclusion=squared_norm_sphere_after_equals_squared_norm_sphere_basis\tresolver=named_theorem\tcandidates=orthogonal_preserves_squared_norm\tselected_theorem=orthogonal_preserves_squared_norm\tgenerated_term=orthogonal_preserves_squared_norm_G_sphere_basis\tcore_typecheck=PASS\treason=unique_checked_candidate\tresolved=G_R128_128\tresult=solved\ttheorem=orthogonal_preserves_squared_norm",
        "transform\tH\treflection\tR128\t128\treversing\taxis=0\tcertificate=cert_h",
        "transform\tG\tplane_rotation\tR128\t128\tpreserving\ti=0\tj=1\tturns=1\tcertificate=cert_g",
        "step\tcontract\tcontraction\tContract\tspace=R128\tcovector=phi\tvector=x\tcertificate=cert_same",
        "step\tdot_xx\tx_dot_x\tDot\tspace=R128\tleft=x\tright=x\tcertificate=cert_same",
        "step\tdot_xy\tx_dot_y\tDot\tspace=R128\tleft=x\tright=y\tcertificate=cert_same",
        "step\tnorm_x\tx_squared_norm\tSquaredNorm\tspace=R128\tvector=x\tcertificate=cert_same",
        "step\treflect_x\thx\tReflect\tspace=R128\taxis=0\tvector=x\tcertificate=cert_h",
        "step\treflect_y\thy\tReflect\tspace=R128\taxis=0\tvector=y\tcertificate=cert_h",
        "step\treflect_hx\th2x\tReflect\tspace=R128\taxis=0\tvector=hx\tcertificate=cert_h",
        "step\tdot_hx_hy\thx_dot_hy\tDot\tspace=R128\tleft=hx\tright=hy\tcertificate=cert_same",
        "step\trotate_x\tgx\tRotatePlane\tspace=R128\tambient=128\ti=0\tj=1\tturns=1\tvector=x\tcertificate=cert_g",
        "step\trotate_y\tgy\tRotatePlane\tspace=R128\tambient=128\ti=0\tj=1\tturns=1\tvector=y\tcertificate=cert_g",
        "step\trotate_gx\tg2x\tRotatePlane\tspace=R128\tambient=128\ti=0\tj=1\tturns=1\tvector=gx\tcertificate=cert_g",
        "step\trotate_g2x\tg3x\tRotatePlane\tspace=R128\tambient=128\ti=0\tj=1\tturns=1\tvector=g2x\tcertificate=cert_g",
        "step\trotate_g3x\tg4x\tRotatePlane\tspace=R128\tambient=128\ti=0\tj=1\tturns=1\tvector=g3x\tcertificate=cert_g",
        "step\tdot_gx_gy\tgx_dot_gy\tDot\tspace=R128\tleft=gx\tright=gy\tcertificate=cert_same",
        "step\tact_sphere\tsphere_after\tActOnSphere\tsphere_dimension=127\tambient=128\tspace=R128\ttransform=G\tpoint=sphere_basis\tcertificate=cert_sphere",
        "step\tsphere_norm\tsphere_squared_norm\tSquaredNorm\tspace=R128\tvector=sphere_after\tcertificate=cert_sphere_norm",
    ]
    step_names = ("contract", "dot_xx", "dot_xy", "norm_x", "reflect_x", "reflect_y",
                  "reflect_hx", "dot_hx_hy", "rotate_x", "rotate_y", "rotate_gx",
                  "rotate_g2x", "rotate_g3x", "dot_gx_gy", "act_sphere", "sphere_norm")
    step_certificates = (
        "cert_same", "cert_same", "cert_same", "cert_same", "cert_h", "cert_h", "cert_h",
        "cert_same", "cert_g", "cert_g", "cert_g", "cert_g", "cert_g", "cert_same",
        "cert_sphere", "cert_sphere_norm",
    )
    lines.extend(f"plan_input\t{name}\tscalar_loop,packed_vector,gpu_vector,special_instruction\t"
                 f"certificate={certificate}"
                 for name, certificate in zip(step_names, step_certificates))
    results = ("contraction", "x_dot_x", "x_dot_y", "x_squared_norm", "hx", "hy", "h2x",
               "hx_dot_hy", "gx", "gy", "g2x", "g3x", "g4x", "gx_dot_gy",
               "sphere_after", "sphere_squared_norm")
    lines.extend(f"temporary\t{name}\t{'foldable' if 'dot' in name or 'norm' in name or 'contract' in name else 'reusable'}"
                 for name in results)
    lines.append("end")
    return "\n".join(lines) + "\n"


def replace_once(text: str, old: str, new: str) -> bytes:
    if text.count(old) != 1:
        raise AssertionError((old, text.count(old)))
    return text.replace(old, new).encode()


class CheckedMathBackendTest(unittest.TestCase):
    def compile_and_run(self):
        artifact_text = checked_artifact_text()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            artifact = root / "r128.math-one-step"
            output = root / "r128"
            listing = root / "r128.instructions"
            artifact.write_text(artifact_text)
            compiled = compile_artifact(artifact, output, listing)
            native = run_native(compiled, output)
            yield compiled, native, output.read_bytes(), listing.read_text()

    @unittest.skipUnless(platform.system() == "Linux" and platform.machine() == "x86_64",
                         "native direct ELF acceptance requires x86_64 Linux")
    def test_exact_r128_math_runs_natively(self) -> None:
        for compiled, native, image, listing in self.compile_and_run():
            observations = {name: values for name, _kind, values in decode_observations(compiled.plan, native)}
            self.assertEqual(observations["contraction"], "190")
            self.assertEqual(observations["x_dot_x"], "250")
            self.assertEqual(observations["x_dot_y"], "190")
            self.assertEqual(observations["x_squared_norm"], "250")
            self.assertEqual(observations["hx_dot_hy"], "190")
            self.assertEqual(observations["gx_dot_gy"], "190")
            self.assertEqual(observations["sphere_squared_norm"], "1")
            self.assertEqual(observations["hx"], coordinates(H_X))
            self.assertEqual(observations["hy"], coordinates(H_Y))
            self.assertEqual(observations["h2x"], coordinates(X))
            self.assertEqual(observations["gx"], coordinates(G_X))
            self.assertEqual(observations["gy"], coordinates(G_Y))
            self.assertEqual(observations["g2x"], coordinates(G2_X))
            self.assertEqual(observations["g3x"], coordinates(G3_X))
            self.assertEqual(observations["g4x"], coordinates(X))
            self.assertEqual(observations["sphere_after"], coordinates(SPHERE_AFTER))
            self.assertEqual(observations["hx"].split(",")[-1], "9")
            self.assertEqual(image[:4], b"\x7fELF")
            self.assertEqual(struct.unpack_from("<H", image, 18)[0], 62)
            self.assertEqual(struct.unpack_from("<Q", image, 40)[0], 0)
            self.assertEqual(struct.unpack_from("<I", image, 64 + 4)[0], 5)
            for forbidden in (b"RefC", b"libc", b".interp", b".dynamic"):
                self.assertNotIn(forbidden, image)
            self.assertNotIn(struct.pack("<q", 190), image)
            self.assertNotIn(struct.pack("<q", 250), image)
            self.assertIn("exact-integer accumulator", listing)
            self.assertIn("one-step temporaries are not presumed memory stores", listing)
            self.assertIn("temporary contract.accumulator register rax", listing)
            self.assertIn("temporary contract.product reuse r11", listing)
            self.assertIn("scalar_plan.spills eliminate", listing)

    @unittest.skipUnless(platform.system() == "Linux" and platform.machine() == "x86_64",
                         "native direct ELF acceptance requires x86_64 Linux")
    def test_execution_receipt_binds_artifact_compiler_elf_and_observations(self) -> None:
        for compiled, native, _image, _listing in self.compile_and_run():
            receipt = render_execution_receipt(compiled, native, "1" * 40)
            self.assertTrue(receipt.startswith("MATH_BACKEND_EXECUTION\t1\nartifact_sha256\t"))
            self.assertIn("\ncompiler_head\tisomorphisms/Idric\t" + "0" * 40 + "\n", receipt)
            self.assertIn("\nbackend_head\tisomorphisms/idric-x86-aggressive-backend\t" + "1" * 40, receipt)
            self.assertIn("stage\tnative_execution\tPASS", receipt)
            self.assertNotIn("rhs_validation", receipt)
            stages = [line.split("\t")[1] for line in receipt.splitlines()
                      if line.startswith("stage\t")]
            self.assertEqual(stages, ["source_parse", "constraint_generation",
                                      "constraint_resolution", "core_typecheck", "one_step_form",
                                      "backend_plan", "target_codegen", "native_execution"])
            self.assertIn("fallback\tRefC\tABSENT", receipt)
            self.assertIn("observation\tscalar\tcontraction\texact_integer\t190", receipt)
            self.assertIn("observation\tvector\tg4x\tR128\t128\texact_integer\t", receipt)

    def test_compile_path_does_not_invoke_toolchain_fallbacks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            artifact = root / "fixture.math-one-step"
            artifact.write_text(checked_artifact_text())
            with patch("backend.r128_math.subprocess.run", side_effect=AssertionError("external tool invoked")):
                compile_artifact(artifact, root / "fixture")

    def assert_rejection(self, raw: bytes, code: str) -> None:
        with self.assertRaises(ArtifactError) as caught:
            parse_checked_artifact_bytes(raw)
        self.assertEqual(caught.exception.code, code)

    def assert_plan_rejection(self, raw: bytes, code: str) -> None:
        with self.assertRaises(ArtifactError) as caught:
            make_scalar_plan(parse_checked_artifact_bytes(raw))
        self.assertEqual(caught.exception.code, code)

    def single_step_artifact(self, step_name: str, result_name: str) -> str:
        lines = checked_artifact_text().splitlines()
        kept: list[str] = []
        for line in lines:
            if line.startswith("step\t") and not line.startswith(f"step\t{step_name}\t"):
                continue
            if line.startswith("plan_input\t") and not line.startswith(f"plan_input\t{step_name}\t"):
                continue
            if line.startswith("temporary\t") and not line.startswith(f"temporary\t{result_name}\t"):
                continue
            kept.append(line)
        return "\n".join(kept) + "\n"

    def test_idric_source_is_not_recognized_by_backend(self) -> None:
        self.assert_rejection(b"module R128\nmain : IO ()\nmain = pure ()\n", "wrong_artifact_header")

    def test_vector_vector_contraction_is_rejected(self) -> None:
        text = checked_artifact_text()
        self.assert_rejection(replace_once(text, "covector=phi", "covector=y"),
                              "contraction_requires_covector")

    def test_equal_rank_named_space_mismatch_is_rejected(self) -> None:
        text = checked_artifact_text()
        text = text.replace("space\tR128\t128\n", "space\tOtherR128\t128\nspace\tR128\t128\n")
        text = text.replace("value\tphi\tcovector\tR128", "value\tphi\tcovector\tOtherR128")
        self.assert_rejection(text.encode(), "contraction_space_mismatch")

    def test_dimension_mismatch_is_rejected(self) -> None:
        text = checked_artifact_text().replace(
            "value\tphi\tcovector\tR128\t128", "value\tphi\tcovector\tR128\t127", 1)
        self.assert_rejection(text.encode(), "dimension_mismatch")

    def test_absent_theorem_fails_closed(self) -> None:
        text = checked_artifact_text().replace("certificate=cert_sphere", "certificate=missing_sphere", 1)
        self.assert_rejection(text.encode(), "unknown_certificate")

    def test_ambiguous_transform_is_a_diagnostic(self) -> None:
        text = checked_artifact_text().replace(
            "transform\tH\treflection", "transform\tH2\treflection\tR128\t128\treversing\taxis=0\tcertificate=cert_h\ntransform\tH\treflection", 1)
        self.assert_rejection(text.encode(), "ambiguous_transform")

    def test_orientation_error_is_rejected(self) -> None:
        text = checked_artifact_text().replace(
            "H\treflection\tR128\t128\treversing", "H\treflection\tR128\t128\tpreserving", 1)
        self.assert_rejection(text.encode(), "orientation_error")

    def test_sphere_ambient_error_is_rejected(self) -> None:
        text = checked_artifact_text().replace("sphere_dimension=127\tambient=128", "sphere_dimension=126\tambient=128", 1)
        self.assert_rejection(text.encode(), "sphere_ambient_dimension")

    def test_unknown_operation_is_rejected(self) -> None:
        text = checked_artifact_text().replace("\tContract\tspace=R128", "\tGLSLFallback\tspace=R128", 1)
        self.assert_rejection(text.encode(), "unknown_semantic_operation")

    def test_reordered_operation_fields_are_rejected(self) -> None:
        text = checked_artifact_text().replace(
            "space=R128\tcovector=phi\tvector=x",
            "covector=phi\tspace=R128\tvector=x", 1)
        self.assert_rejection(text.encode(), "malformed_step")

    def test_plan_cannot_omit_scalar_baseline(self) -> None:
        text = checked_artifact_text().replace(
            "scalar_loop,packed_vector,gpu_vector,special_instruction",
            "packed_vector,gpu_vector,special_instruction", 1)
        self.assert_rejection(text.encode(), "scalar_baseline_absent")

    def test_core_failure_is_not_accepted(self) -> None:
        text = checked_artifact_text().replace("core_typecheck\tPASS", "core_typecheck\tFAIL", 1)
        self.assert_rejection(text.encode(), "core_typecheck_not_pass")

    def test_certificate_hypothesis_mismatch_is_rejected(self) -> None:
        text = checked_artifact_text().replace(
            "certificate\tcert_same\tSameSpace", "certificate\tcert_same\tPreservesSquaredNorm", 1)
        self.assert_rejection(text.encode(), "certificate_hypothesis_mismatch")

    def test_unknown_trace_field_is_rejected(self) -> None:
        text = checked_artifact_text().replace("\tresult=solved\n", "\tresult=solved\tfolklore=yes\n", 1)
        self.assert_rejection(text.encode(), "unknown_certificate_trace")

    def test_required_generated_term_trace_is_rejected_when_absent(self) -> None:
        text = checked_artifact_text().replace("\tgenerated_term=same_space_R128_128", "", 1)
        self.assert_rejection(text.encode(), "missing_certificate_trace")

    def test_nonunit_sphere_point_is_rejected(self) -> None:
        text = checked_artifact_text().replace(coordinates(SPHERE_BASIS), coordinates([*([0] * 127), 2]), 1)
        self.assert_rejection(text.encode(), "sphere_point_not_unit")

    def test_reflection_rejects_int64_min_negation(self) -> None:
        text = self.single_step_artifact("reflect_x", "hx")
        original = coordinates(X)
        hostile = coordinates([-(1 << 63), *X[1:]])
        text = text.replace(original, hostile, 1)
        self.assert_plan_rejection(text.encode(), "integer_negation_overflow")

    def test_quarter_turn_rejects_int64_min_negation(self) -> None:
        text = self.single_step_artifact("rotate_x", "gx")
        original = coordinates(X)
        hostile = coordinates([X[0], -(1 << 63), *X[2:]])
        text = text.replace(original, hostile, 1)
        self.assert_plan_rejection(text.encode(), "integer_negation_overflow")

    def test_source_digest_is_checked_without_parsing_source(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            artifact = root / "fixture.math-one-step"
            source = root / "fixture.idric"
            artifact.write_text(checked_artifact_text())
            source.write_text("different source\n")
            with self.assertRaises(ArtifactError) as caught:
                compile_artifact(artifact, root / "fixture", source_path=source)
            self.assertEqual(caught.exception.code, "source_digest_mismatch")


class RealCompilerHandoffTest(unittest.TestCase):
    def test_real_idric_emitter_when_explicitly_configured(self) -> None:
        compiler = os.environ.get("EDRIC_COMPILER")
        source = os.environ.get("EDRIC_R128_SOURCE")
        if not compiler or not source:
            self.skipTest("set EDRIC_COMPILER and EDRIC_R128_SOURCE for the real checked handoff")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            artifact = root / "r128.math-one-step"
            output = root / "r128"
            subprocess.run([compiler, "--emit-math-one-step", source, "-o", artifact], check=True)
            compiled = compile_artifact(artifact, output, source_path=Path(source))
            native = run_native(compiled, output)
            self.assertNotEqual(compiled.plan.artifact.compiler_head, "0" * 40)
            expected_steps = [
                ("contract", "contraction", "Contract"),
                ("dot_xx", "x_dot_x", "Dot"),
                ("dot_xy", "x_dot_y", "Dot"),
                ("norm_x", "x_squared_norm", "SquaredNorm"),
                ("reflect_x", "hx", "Reflect"),
                ("reflect_y", "hy", "Reflect"),
                ("reflect_hx", "h2x", "Reflect"),
                ("dot_hx_hy", "hx_dot_hy", "Dot"),
                ("rotate_x", "gx", "RotatePlane"),
                ("rotate_y", "gy", "RotatePlane"),
                ("rotate_gx", "g2x", "RotatePlane"),
                ("rotate_g2x", "g3x", "RotatePlane"),
                ("rotate_g3x", "g4x", "RotatePlane"),
                ("dot_gx_gy", "gx_dot_gy", "Dot"),
                ("act_sphere", "sphere_after", "ActOnSphere"),
                ("sphere_norm", "sphere_squared_norm", "SquaredNorm"),
            ]
            self.assertEqual(
                [(item.step.name, item.step.result, item.step.kind) for item in compiled.plan.steps],
                expected_steps,
            )
            observed = {name: (kind, values)
                        for name, kind, values in decode_observations(compiled.plan, native)}
            expected_observations = {
                "contraction": ("scalar", "190"),
                "x_dot_x": ("scalar", "250"),
                "x_dot_y": ("scalar", "190"),
                "x_squared_norm": ("scalar", "250"),
                "hx": ("vector", coordinates(H_X)),
                "hy": ("vector", coordinates(H_Y)),
                "h2x": ("vector", coordinates(X)),
                "hx_dot_hy": ("scalar", "190"),
                "gx": ("vector", coordinates(G_X)),
                "gy": ("vector", coordinates(G_Y)),
                "g2x": ("vector", coordinates(G2_X)),
                "g3x": ("vector", coordinates(G3_X)),
                "g4x": ("vector", coordinates(X)),
                "gx_dot_gy": ("scalar", "190"),
                "sphere_after": ("sphere_point", coordinates(SPHERE_AFTER)),
                "sphere_squared_norm": ("scalar", "1"),
            }
            self.assertEqual(observed, expected_observations)


if __name__ == "__main__":
    unittest.main()
