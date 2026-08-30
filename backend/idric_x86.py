#!/usr/bin/env python3
"""Checked Idriç mathematical one-step artifact to direct ELF64.

The backend never parses Idriç source.  It consumes the versioned artifact
emitted after ordinary Idriç core type checking, validates the typed boundary,
selects an exact-integer scalar plan, and writes x86-64 and ELF bytes directly.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import platform
import re
import struct
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

ELF_BASE = 0x400000
CODE_OFFSET = 0x1000
ARTIFACT_HEADER = "EDRIC_MATH_ONE_STEP\t1"
RECEIPT_HEADER = "MATH_BACKEND_EXECUTION\t1"
BACKEND_REPOSITORY = "isomorphisms/idric-x86-aggressive-backend"
I64_MIN = -(1 << 63)
I64_MAX = (1 << 63) - 1

IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_.-]*\Z")
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
DECIMAL = re.compile(r"(?:0|-[1-9][0-9]*|[1-9][0-9]*)\Z")
GIT_HEAD = re.compile(r"[0-9a-f]{40}\Z")


class ArtifactError(ValueError):
    def __init__(self, code: str, detail: str):
        super().__init__(f"{code}: {detail}")
        self.code = code
        self.detail = detail


@dataclass(frozen=True)
class Space:
    name: str
    dimension: int


@dataclass(frozen=True)
class TypedValue:
    name: str
    kind: str
    space: str
    dimension: int
    coordinates: tuple[int, ...]


@dataclass(frozen=True)
class Certificate:
    name: str
    kind: str
    provenance: str
    trace: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class Transform:
    name: str
    kind: str
    space: str
    ambient: int
    orientation: str
    parameters: tuple[tuple[str, int], ...]
    certificate: str

    def parameter(self, name: str) -> int:
        return dict(self.parameters)[name]


@dataclass(frozen=True)
class Step:
    name: str
    result: str
    kind: str
    arguments: tuple[tuple[str, str], ...]
    certificate: str

    def argument(self, name: str) -> str:
        return dict(self.arguments)[name]


@dataclass(frozen=True)
class TemporaryHint:
    name: str
    hint: str


@dataclass(frozen=True)
class CheckedArtifact:
    raw: bytes
    source_sha256: str
    compiler_repository: str
    compiler_head: str
    spaces: tuple[Space, ...]
    values: tuple[TypedValue, ...]
    certificates: tuple[Certificate, ...]
    transforms: tuple[Transform, ...]
    steps: tuple[Step, ...]
    plan_inputs: tuple[tuple[str, tuple[str, ...], str], ...]
    temporaries: tuple[TemporaryHint, ...]

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.raw).hexdigest()


@dataclass(frozen=True)
class RuntimeType:
    kind: str
    space: str | None
    dimension: int


@dataclass(frozen=True)
class PlannedStep:
    step: Step
    result_type: RuntimeType
    output_offset: int
    realization: str = "scalar_integer"

    @property
    def output_size(self) -> int:
        return 8 if self.result_type.kind == "scalar" else 8 * self.result_type.dimension


@dataclass(frozen=True)
class TemporaryDecision:
    name: str
    decision: str
    detail: str


@dataclass(frozen=True)
class ScalarPlan:
    artifact: CheckedArtifact
    steps: tuple[PlannedStep, ...]
    result_size: int
    temporary_decisions: tuple[TemporaryDecision, ...]


@dataclass(frozen=True)
class CompiledImage:
    elf: bytes
    listing: str
    plan: ScalarPlan


def _fail(code: str, detail: str) -> None:
    raise ArtifactError(code, detail)


def _identifier(value: str, where: str) -> str:
    if not IDENTIFIER.fullmatch(value):
        _fail("malformed_identifier", f"{where}: {value!r}")
    return value


def _integer(value: str, where: str) -> int:
    if not DECIMAL.fullmatch(value):
        _fail("malformed_integer", f"{where}: {value!r}")
    return int(value)


def _positive_integer(value: str, where: str) -> int:
    number = _integer(value, where)
    if number <= 0:
        _fail("invalid_dimension", f"{where}: expected positive integer")
    return number


def _fields(line: str, count: int, where: str) -> list[str]:
    fields = line.split("\t")
    if len(fields) != count:
        _fail("malformed_row", f"{where}: expected {count} tab-separated fields")
    return fields


def _key_values(fields: Sequence[str], expected: Sequence[str], where: str) -> dict[str, str]:
    if len(fields) != len(expected):
        _fail("malformed_step", f"{where}: expected keys {','.join(expected)}")
    result: dict[str, str] = {}
    for field, wanted in zip(fields, expected):
        if "=" not in field:
            _fail("malformed_step", f"{where}: expected {wanted}=<value>")
        key, value = field.split("=", 1)
        if key != wanted or not value:
            _fail("malformed_step", f"{where}: expected {wanted}=<value>, got {field!r}")
        result[key] = value
    return result


def parse_checked_artifact_bytes(raw: bytes) -> CheckedArtifact:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        _fail("artifact_not_utf8", str(error))
    if not text.endswith("\n"):
        _fail("missing_final_newline", "artifact must end with one newline")
    if "\r" in text or "\x00" in text:
        _fail("invalid_artifact_byte", "CR and NUL are forbidden")
    lines = text[:-1].split("\n")
    if any(not line for line in lines):
        _fail("blank_row", "blank rows are forbidden")
    if not lines or lines[0] != ARTIFACT_HEADER:
        _fail("wrong_artifact_header", f"expected {ARTIFACT_HEADER!r}")
    if len(lines) < 5:
        _fail("truncated_artifact", "source/core/end rows missing")
    source = _fields(lines[1], 2, "source_sha256")
    if source[0] != "source_sha256" or not SHA256.fullmatch(source[1]):
        _fail("malformed_source_digest", "source_sha256 must be lowercase SHA-256")
    compiler = _fields(lines[2], 3, "compiler_head")
    if (compiler[0] != "compiler_head" or compiler[1] != "isomorphisms/Idric"
            or not GIT_HEAD.fullmatch(compiler[2])):
        _fail("malformed_compiler_head", "compiler_head must name isomorphisms/Idric and a full lowercase head")
    core = _fields(lines[3], 2, "core_typecheck")
    if core != ["core_typecheck", "PASS"]:
        _fail("core_typecheck_not_pass", "ordinary core typecheck PASS is required")

    spaces: list[Space] = []
    values: list[TypedValue] = []
    certificates: list[Certificate] = []
    transforms: list[Transform] = []
    steps: list[Step] = []
    plan_inputs: list[tuple[str, tuple[str, ...], str]] = []
    temporaries: list[TemporaryHint] = []
    sections = {"space": 0, "value": 1, "certificate": 2, "transform": 3,
                "step": 4, "plan_input": 5, "temporary": 6, "end": 7}
    section = 0
    seen_end = False
    for row_number, line in enumerate(lines[4:], start=5):
        fields = line.split("\t")
        tag = fields[0]
        where = f"row {row_number} ({tag})"
        if tag not in sections:
            _fail("unknown_artifact_row", f"{where}: {tag!r}")
        if sections[tag] < section:
            _fail("artifact_section_order", f"{where}: section out of order")
        section = sections[tag]
        if tag == "end":
            if fields != ["end"] or row_number != len(lines):
                _fail("malformed_end", "end must be the final row")
            seen_end = True
        elif tag == "space":
            fields = _fields(line, 3, where)
            spaces.append(Space(_identifier(fields[1], where), _positive_integer(fields[2], where)))
        elif tag == "value":
            fields = _fields(line, 7, where)
            if fields[2] not in {"vector", "covector", "sphere_point"}:
                _fail("unknown_value_kind", f"{where}: {fields[2]!r}")
            if fields[5] != "exact_integer":
                _fail("unsupported_scalar", f"{where}: only exact_integer is supported")
            coordinates = tuple(_integer(item, f"{where}.coordinates") for item in fields[6].split(","))
            values.append(TypedValue(_identifier(fields[1], where), fields[2],
                                     _identifier(fields[3], where),
                                     _positive_integer(fields[4], where), coordinates))
        elif tag == "certificate":
            fields = line.split("\t")
            if len(fields) < 5:
                _fail("malformed_row", f"{where}: expected at least 5 fields")
            if fields[3] != "PASS":
                _fail("certificate_not_pass", f"{where}: certificate must be PASS")
            certificate_kinds = {"SameSpace", "OrthogonalTransform", "PreservesSquaredNorm",
                                 "SphereAmbientDimension", "OrthogonalSphereAction"}
            if fields[2] not in certificate_kinds:
                _fail("unknown_certificate_kind", f"{where}: {fields[2]!r}")
            provenances = {"unification", "normalization", "structure_law_instance", "named_theorem"}
            if fields[4] not in provenances:
                _fail("unknown_certificate_provenance", f"{where}: {fields[4]!r}")
            trace_keys = {"registry_version", "goal", "generated_by", "hypotheses", "conclusion",
                          "resolver", "candidates", "selected_theorem", "generated_term",
                          "core_typecheck", "reason", "resolved", "result", "law", "theorem"}
            trace: list[tuple[str, str]] = []
            seen_trace_keys: set[str] = set()
            for extra in fields[5:]:
                if "=" not in extra:
                    _fail("malformed_certificate_trace", f"{where}: {extra!r}")
                key, value = extra.split("=", 1)
                if key not in trace_keys or not value:
                    _fail("unknown_certificate_trace", f"{where}: {key!r}")
                if key in seen_trace_keys:
                    _fail("duplicate_certificate_trace", f"{where}: duplicate {key}")
                seen_trace_keys.add(key)
                trace.append((key, value))
            trace_map = dict(trace)
            required_trace = {"goal", "generated_by", "reason", "generated_term", "core_typecheck"}
            missing_trace = sorted(required_trace - trace_map.keys())
            if missing_trace:
                _fail("missing_certificate_trace", f"{where}: {','.join(missing_trace)}")
            if trace_map["core_typecheck"] != "PASS":
                _fail("certificate_core_typecheck", f"{where}: expected core_typecheck=PASS")
            if fields[4] == "structure_law_instance" and "law" not in trace_map:
                _fail("missing_law_provenance", where)
            if fields[4] == "named_theorem" and not ({"theorem", "selected_theorem"} & trace_map.keys()):
                _fail("missing_theorem_provenance", where)
            certificates.append(Certificate(_identifier(fields[1], where),
                                            _identifier(fields[2], where), fields[4], tuple(trace)))
        elif tag == "transform":
            fields = line.split("\t")
            if len(fields) not in {8, 10}:
                _fail("malformed_row", f"{where}: reflection has 8 fields; plane_rotation has 10")
            if fields[2] not in {"reflection", "plane_rotation"}:
                _fail("unknown_transform_kind", f"{where}: {fields[2]!r}")
            if fields[5] not in {"preserving", "reversing"}:
                _fail("unknown_orientation", f"{where}: {fields[5]!r}")
            parameter_keys = ("axis",) if fields[2] == "reflection" else ("i", "j", "turns")
            expected_count = 8 if fields[2] == "reflection" else 10
            if len(fields) != expected_count:
                _fail("malformed_transform", f"{where}: wrong field count for {fields[2]}")
            parsed_parameters = _key_values(fields[6:-1], parameter_keys, where)
            parameters = tuple((key, _integer(parsed_parameters[key], f"{where}.{key}"))
                               for key in parameter_keys)
            if fields[2] == "reflection" and parameters != (("axis", 0),):
                _fail("unsupported_transform", f"{where}: v1 reflection must use axis=0")
            if fields[2] == "plane_rotation" and parameters != (("i", 0), ("j", 1), ("turns", 1)):
                _fail("unsupported_transform", f"{where}: v1 plane rotation must be i=0,j=1,turns=1")
            cert = _key_values([fields[-1]], ["certificate"], where)["certificate"]
            transforms.append(Transform(
                _identifier(fields[1], where), fields[2], _identifier(fields[3], where),
                _positive_integer(fields[4], where), fields[5],
                parameters, _identifier(cert, where)))
        elif tag == "step":
            if len(fields) < 6:
                _fail("malformed_step", f"{where}: too few fields")
            kind = fields[3]
            expected = {
                "Contract": ("space", "covector", "vector", "certificate"),
                "Dot": ("space", "left", "right", "certificate"),
                "SquaredNorm": ("space", "vector", "certificate"),
                "Reflect": ("space", "axis", "vector", "certificate"),
                "RotatePlane": ("space", "ambient", "i", "j", "turns", "vector", "certificate"),
                "ActOnSphere": ("sphere_dimension", "ambient", "space", "transform", "point", "certificate"),
            }
            if kind not in expected:
                _fail("unknown_semantic_operation", f"{where}: {kind!r}")
            parsed = _key_values(fields[4:], expected[kind], where)
            certificate = _identifier(parsed["certificate"], where)
            arguments = tuple((key, value) for key, value in parsed.items() if key != "certificate")
            steps.append(Step(_identifier(fields[1], where), _identifier(fields[2], where),
                              kind, arguments, certificate))
        elif tag == "plan_input":
            fields = _fields(line, 4, where)
            cert = _key_values([fields[3]], ["certificate"], where)["certificate"]
            allowed = tuple(fields[2].split(","))
            universe = ("scalar_loop", "packed_vector", "gpu_vector", "special_instruction")
            if not allowed or any(choice not in universe for choice in allowed):
                _fail("unknown_plan_input", f"{where}: {fields[2]!r}")
            if tuple(sorted(set(allowed), key=universe.index)) != allowed:
                _fail("plan_input_order", f"{where}: choices must be unique and canonical")
            plan_inputs.append((_identifier(fields[1], where), allowed, _identifier(cert, where)))
        elif tag == "temporary":
            fields = _fields(line, 3, where)
            if fields[2] not in {"register_candidate", "foldable", "reusable", "spill_permitted"}:
                _fail("unknown_temporary_hint", f"{where}: {fields[2]!r}")
            temporaries.append(TemporaryHint(_identifier(fields[1], where), fields[2]))
    if not seen_end:
        _fail("missing_end", "artifact must finish with end")
    if not spaces or not values or not certificates or not steps:
        _fail("empty_required_section", "space, value, certificate, and step are required")
    _reject_duplicate_names(spaces, values, certificates, transforms, steps, temporaries)
    if [item.name for item in spaces] != sorted(item.name for item in spaces):
        _fail("space_order", "spaces must be sorted")
    if [item.name for item in values] != sorted(item.name for item in values):
        _fail("value_order", "values must be sorted")
    artifact = CheckedArtifact(raw, source[1], compiler[1], compiler[2], tuple(spaces), tuple(values),
                               tuple(certificates), tuple(transforms), tuple(steps),
                               tuple(plan_inputs), tuple(temporaries))
    _validate_checked_artifact(artifact)
    return artifact


def parse_checked_artifact(path: Path) -> CheckedArtifact:
    return parse_checked_artifact_bytes(path.read_bytes())


def _reject_duplicate_names(
    spaces: Sequence[Space], values: Sequence[TypedValue], certificates: Sequence[Certificate],
    transforms: Sequence[Transform], steps: Sequence[Step], temporaries: Sequence[TemporaryHint],
) -> None:
    groups = (("space", [x.name for x in spaces]), ("value", [x.name for x in values]),
              ("certificate", [x.name for x in certificates]),
              ("transform", [x.name for x in transforms]), ("step", [x.name for x in steps]),
              ("step result", [x.result for x in steps]),
              ("temporary", [x.name for x in temporaries]))
    for kind, names in groups:
        if len(names) != len(set(names)):
            _fail("duplicate_name", f"duplicate {kind}")
    compiler_identifiers = ([x.name for x in spaces] + [x.name for x in values]
                            + [x.name for x in certificates] + [x.name for x in transforms]
                            + [x.name for x in steps] + [x.result for x in steps])
    if len(compiler_identifiers) != len(set(compiler_identifiers)):
        _fail("duplicate_name", "compiler identifiers must be globally unique")


def _validate_checked_artifact(artifact: CheckedArtifact) -> None:
    spaces = {item.name: item for item in artifact.spaces}
    certificates = {item.name: item for item in artifact.certificates}
    for value in artifact.values:
        if value.space not in spaces:
            _fail("unknown_space", f"value {value.name}: {value.space}")
        if spaces[value.space].dimension != value.dimension:
            _fail("dimension_mismatch", f"value {value.name}: {value.dimension} vs {spaces[value.space].dimension}")
        if len(value.coordinates) != value.dimension:
            _fail("coordinate_count", f"value {value.name}: expected {value.dimension}, got {len(value.coordinates)}")
        for coordinate in value.coordinates:
            _require_i64(coordinate, f"value {value.name}")
        if value.kind == "sphere_point" and sum(x * x for x in value.coordinates) != 1:
            _fail("sphere_point_not_unit", f"value {value.name}: exact squared norm is not 1")
    for transform in artifact.transforms:
        if transform.space not in spaces or spaces[transform.space].dimension != transform.ambient:
            _fail("transform_ambient_mismatch", f"transform {transform.name}")
        if transform.certificate not in certificates:
            _fail("unknown_certificate", f"transform {transform.name}: {transform.certificate}")
        if certificates[transform.certificate].kind != "OrthogonalTransform":
            _fail("transform_certificate_kind", f"transform {transform.name}: {transform.certificate}")
        wanted = "reversing" if transform.kind == "reflection" else "preserving"
        if transform.orientation != wanted:
            _fail("orientation_error", f"transform {transform.name}: {transform.kind} must be {wanted}")
        for key, coordinate in transform.parameters:
            if key in {"axis", "i", "j"} and not 0 <= coordinate < transform.ambient:
                _fail("transform_axis_bounds", f"transform {transform.name}: {key}={coordinate}")
        if transform.kind == "plane_rotation" and transform.parameter("i") == transform.parameter("j"):
            _fail("rotation_plane_degenerate", f"transform {transform.name}")

    runtime_types: dict[str, RuntimeType] = {
        value.name: RuntimeType(value.kind, value.space, value.dimension) for value in artifact.values
    }
    transform_map = {item.name: item for item in artifact.transforms}
    for step in artifact.steps:
        if step.certificate not in certificates:
            _fail("unknown_certificate", f"step {step.name}: {step.certificate}")
        if step.result in runtime_types:
            _fail("duplicate_runtime_value", f"step result {step.result}")
        runtime_types[step.result] = _validate_step(
            step, runtime_types, spaces, transform_map, certificates)

    if [item[0] for item in artifact.plan_inputs] != [step.name for step in artifact.steps]:
        _fail("plan_input_coverage", "one plan_input in step order is required")
    for (step_name, allowed, cert), step in zip(artifact.plan_inputs, artifact.steps):
        if step_name != step.name or cert != step.certificate:
            _fail("plan_input_certificate", f"plan_input {step_name}")
        if "scalar_loop" not in allowed:
            _fail("scalar_baseline_absent", f"step {step_name} does not permit scalar_loop")
    if [item.name for item in artifact.temporaries] != [step.result for step in artifact.steps]:
        _fail("temporary_coverage", "one temporary policy in step-result order is required")


def _runtime_ref(types: Mapping[str, RuntimeType], name: str, where: str) -> RuntimeType:
    if name not in types:
        _fail("unknown_runtime_value", f"{where}: {name}")
    return types[name]


def _space_argument(step: Step, spaces: Mapping[str, Space]) -> Space:
    name = step.argument("space")
    if name not in spaces:
        _fail("unknown_space", f"step {step.name}: {name}")
    return spaces[name]


def _require_vector(value: RuntimeType, where: str, allow_sphere: bool = False) -> None:
    allowed = {"vector", "sphere_point"} if allow_sphere else {"vector"}
    if value.kind not in allowed:
        _fail("expected_vector", f"{where}: got {value.kind}; no vector/covector conversion exists")


def _validate_step(
    step: Step, types: Mapping[str, RuntimeType], spaces: Mapping[str, Space],
    transforms: Mapping[str, Transform], certificates: Mapping[str, Certificate],
) -> RuntimeType:
    if step.kind == "Contract":
        space = _space_argument(step, spaces)
        covector = _runtime_ref(types, step.argument("covector"), step.name)
        vector = _runtime_ref(types, step.argument("vector"), step.name)
        if covector.kind != "covector":
            _fail("contraction_requires_covector", f"step {step.name}: got {covector.kind}")
        _require_vector(vector, step.name)
        if covector.space != vector.space or vector.space != space.name:
            _fail("contraction_space_mismatch", f"step {step.name}: {covector.space}, {vector.space}, {space.name}")
        if covector.dimension != vector.dimension or vector.dimension != space.dimension:
            _fail("contraction_dimension_mismatch", f"step {step.name}")
        if step.certificate not in certificates or certificates[step.certificate].kind != "SameSpace":
            _fail("certificate_hypothesis_mismatch", f"step {step.name}: SameSpace required")
        return RuntimeType("scalar", None, 1)
    if step.kind in {"Dot", "SquaredNorm"}:
        space = _space_argument(step, spaces)
        names = ((step.argument("left"), step.argument("right")) if step.kind == "Dot"
                 else (step.argument("vector"), step.argument("vector")))
        left, right = (_runtime_ref(types, name, step.name) for name in names)
        _require_vector(left, step.name, allow_sphere=step.kind == "SquaredNorm")
        _require_vector(right, step.name, allow_sphere=step.kind == "SquaredNorm")
        if left.space != right.space or left.space != space.name:
            _fail("dot_space_mismatch", f"step {step.name}: {left.space}, {right.space}, {space.name}")
        if left.dimension != right.dimension or left.dimension != space.dimension:
            _fail("dot_dimension_mismatch", f"step {step.name}")
        certificate_kind = certificates[step.certificate].kind if step.certificate in certificates else None
        allowed_certificates = ({"SameSpace", "PreservesSquaredNorm"}
                                if step.kind == "SquaredNorm" else {"SameSpace"})
        if certificate_kind not in allowed_certificates:
            _fail("certificate_hypothesis_mismatch",
                  f"step {step.name}: one of {sorted(allowed_certificates)} required")
        return RuntimeType("scalar", None, 1)
    if step.kind in {"Reflect", "RotatePlane"}:
        space = _space_argument(step, spaces)
        vector = _runtime_ref(types, step.argument("vector"), step.name)
        _require_vector(vector, step.name, allow_sphere=True)
        if vector.space != space.name or vector.dimension != space.dimension:
            _fail("transform_space_mismatch", f"step {step.name}")
        if step.kind == "Reflect":
            axis = _integer(step.argument("axis"), f"step {step.name}.axis")
            matches = [item for item in transforms.values()
                       if item.kind == "reflection" and item.space == space.name
                       and item.parameter("axis") == axis]
        else:
            ambient = _positive_integer(step.argument("ambient"), f"step {step.name}.ambient")
            i = _integer(step.argument("i"), f"step {step.name}.i")
            j = _integer(step.argument("j"), f"step {step.name}.j")
            turns = _integer(step.argument("turns"), f"step {step.name}.turns")
            if ambient != space.dimension:
                _fail("transform_ambient_mismatch", f"step {step.name}")
            matches = [item for item in transforms.values()
                       if item.kind == "plane_rotation" and item.space == space.name
                       and item.parameter("i") == i and item.parameter("j") == j
                       and item.parameter("turns") == turns]
        if len(matches) != 1:
            _fail("ambiguous_transform" if len(matches) > 1 else "transform_absent",
                  f"step {step.name}: expected exactly one checked transform")
        if matches[0].certificate != step.certificate:
            _fail("transform_certificate_mismatch", f"step {step.name}: {step.certificate} vs {matches[0].certificate}")
        return RuntimeType(vector.kind, vector.space, vector.dimension)
    if step.kind == "ActOnSphere":
        sphere_dimension = _integer(step.argument("sphere_dimension"), f"step {step.name}.sphere_dimension")
        ambient = _positive_integer(step.argument("ambient"), f"step {step.name}.ambient")
        space = _space_argument(step, spaces)
        point = _runtime_ref(types, step.argument("point"), step.name)
        if point.kind != "sphere_point":
            _fail("expected_sphere_point", f"step {step.name}: got {point.kind}")
        if sphere_dimension + 1 != ambient or ambient != space.dimension:
            _fail("sphere_ambient_dimension", f"step {step.name}: S^{sphere_dimension} needs R^{sphere_dimension + 1}")
        if point.space != space.name or point.dimension != ambient:
            _fail("sphere_point_space", f"step {step.name}")
        transform_name = step.argument("transform")
        if transform_name not in transforms:
            _fail("unknown_transform", f"step {step.name}: {transform_name}")
        transform = transforms[transform_name]
        if transform.space != space.name or transform.ambient != ambient:
            _fail("sphere_transform_space", f"step {step.name}")
        if step.certificate not in certificates or certificates[step.certificate].kind != "OrthogonalSphereAction":
            _fail("certificate_hypothesis_mismatch", f"step {step.name}: OrthogonalSphereAction required")
        return RuntimeType("sphere_point", space.name, ambient)
    raise AssertionError(step.kind)


def _require_i64(value: int, where: str) -> None:
    if not I64_MIN <= value <= I64_MAX:
        _fail("integer_out_of_range", f"{where}: {value} does not fit signed 64-bit exact plan")


def make_scalar_plan(artifact: CheckedArtifact) -> ScalarPlan:
    types: dict[str, RuntimeType] = {
        value.name: RuntimeType(value.kind, value.space, value.dimension) for value in artifact.values
    }
    spaces = {item.name: item for item in artifact.spaces}
    transforms = {item.name: item for item in artifact.transforms}
    certificates = {item.name: item for item in artifact.certificates}
    offset = 0
    planned: list[PlannedStep] = []
    for step in artifact.steps:
        result_type = _validate_step(step, types, spaces, transforms, certificates)
        item = PlannedStep(step, result_type, offset)
        planned.append(item)
        offset += item.output_size
        types[step.result] = result_type
    _prove_i64_plan(artifact, planned)
    decisions: list[TemporaryDecision] = []
    for item in planned:
        if item.result_type.kind == "scalar":
            decisions.append(TemporaryDecision(f"{item.step.name}.accumulator", "register", "rax"))
            decisions.append(TemporaryDecision(f"{item.step.name}.product", "reuse", "r11 per coordinate"))
        else:
            decisions.append(TemporaryDecision(f"{item.step.name}.coordinate", "reuse", "rax per coordinate"))
    planned_by_result = {item.step.result: item for item in planned}
    for hint in artifact.temporaries:
        result = planned_by_result[hint.name]
        if result.result_type.kind == "scalar":
            decisions.append(TemporaryDecision(
                hint.name, "register", "rax until copied to its explicit observation slot; not folded"))
        else:
            decisions.append(TemporaryDecision(
                hint.name, "reuse", "rax per coordinate, streamed to its explicit observation slot"))
    decisions.extend(TemporaryDecision(
        f"certificate.{item.name}", "fold", "validated during planning and erased before machine code")
        for item in artifact.certificates)
    decisions.append(TemporaryDecision(
        "packed_realization_candidate", "eliminate", "scalar_integer selected; no packed claim"))
    decisions.append(TemporaryDecision("scalar_plan.spills", "eliminate", "no compiler temporary spills"))
    return ScalarPlan(artifact, tuple(planned), offset, tuple(decisions))


def _prove_i64_plan(artifact: CheckedArtifact, planned: Sequence[PlannedStep]) -> None:
    """Conservatively prove this fixed exact workload cannot overflow i64."""
    exact: dict[str, tuple[int, ...]] = {item.name: item.coordinates for item in artifact.values}
    transforms = {item.name: item for item in artifact.transforms}
    for item in planned:
        step = item.step
        if step.kind == "Contract":
            left, right = exact[step.argument("covector")], exact[step.argument("vector")]
            _require_i64(sum(abs(a) * abs(b) for a, b in zip(left, right)), f"step {step.name} bound")
        elif step.kind in {"Dot", "SquaredNorm"}:
            left_name = step.argument("left") if step.kind == "Dot" else step.argument("vector")
            right_name = step.argument("right") if step.kind == "Dot" else step.argument("vector")
            _require_i64(sum(abs(a) * abs(b) for a, b in zip(exact[left_name], exact[right_name])),
                         f"step {step.name} bound")
        elif step.kind == "Reflect":
            result = list(exact[step.argument("vector")])
            axis = _integer(step.argument("axis"), step.name)
            if result[axis] == I64_MIN:
                _fail("integer_negation_overflow", f"step {step.name}: coordinate {axis}")
            result[axis] = -result[axis]
            exact[step.result] = tuple(result)
        elif step.kind == "RotatePlane":
            result = list(exact[step.argument("vector")])
            i, j = _integer(step.argument("i"), step.name), _integer(step.argument("j"), step.name)
            if result[j] == I64_MIN:
                _fail("integer_negation_overflow", f"step {step.name}: coordinate {j}")
            result[i], result[j] = -result[j], result[i]
            exact[step.result] = tuple(result)
        elif step.kind == "ActOnSphere":
            result = list(exact[step.argument("point")])
            transform = transforms[step.argument("transform")]
            if transform.kind == "reflection":
                axis = transform.parameter("axis")
                if result[axis] == I64_MIN:
                    _fail("integer_negation_overflow", f"step {step.name}: coordinate {axis}")
                result[axis] = -result[axis]
            else:
                i, j = transform.parameter("i"), transform.parameter("j")
                if result[j] == I64_MIN:
                    _fail("integer_negation_overflow", f"step {step.name}: coordinate {j}")
                result[i], result[j] = -result[j], result[i]
            exact[step.result] = tuple(result)


class Assembler:
    def __init__(self) -> None:
        self.code = bytearray()
        self.labels: dict[str, int] = {}
        self.fixups: list[tuple[int, str]] = []
        self.records: list[tuple[int, int, str]] = []

    def emit(self, raw: bytes, text: str) -> None:
        start = len(self.code)
        self.code.extend(raw)
        self.records.append((start, len(self.code), text))

    def label(self, name: str) -> None:
        if name in self.labels:
            raise AssertionError(f"duplicate assembler label {name}")
        self.labels[name] = len(self.code)

    def rel32(self, prefix: bytes, label: str, text: str) -> None:
        start = len(self.code)
        self.code.extend(prefix)
        displacement_at = len(self.code)
        self.code.extend(b"\x00\x00\x00\x00")
        self.fixups.append((displacement_at, label))
        self.records.append((start, len(self.code), text))

    def finish(self) -> tuple[bytes, str]:
        for at, label in self.fixups:
            if label not in self.labels:
                raise AssertionError(f"unknown assembler label {label}")
            self.code[at:at + 4] = struct.pack("<i", self.labels[label] - (at + 4))
        lines = [f"{start:04x}  {bytes(self.code[start:end]).hex(' '):<38} {text}"
                 for start, end, text in self.records]
        return bytes(self.code), "\n".join(lines) + "\n"


def _rex(*, r: int = 0, x: int = 0, b: int = 0, w: int = 1) -> bytes:
    return bytes([0x40 | (w << 3) | (((r >> 3) & 1) << 2)
                  | (((x >> 3) & 1) << 1) | ((b >> 3) & 1)])


def _modrm(mod: int, reg: int, rm: int) -> bytes:
    return bytes([(mod << 6) | ((reg & 7) << 3) | (rm & 7)])


def _sib(scale: int, index: int, base: int) -> bytes:
    return bytes([(scale << 6) | ((index & 7) << 3) | (base & 7)])


def _mov_imm(register: int, value: int) -> bytes:
    if not 0 <= value <= I64_MAX:
        raise ValueError(f"immediate out of range: {value}")
    if value <= 0x7FFFFFFF:
        return _rex(b=register) + b"\xc7" + _modrm(3, 0, register) + struct.pack("<I", value)
    return _rex(b=register) + bytes([0xB8 + (register & 7)]) + struct.pack("<Q", value)


def _xor(register: int) -> bytes:
    return _rex(r=register, b=register) + b"\x31" + _modrm(3, register, register)


def _mov_reg(destination: int, source: int) -> bytes:
    return _rex(r=source, b=destination) + b"\x89" + _modrm(3, source, destination)


def _load_indexed(destination: int, base: int, index: int) -> bytes:
    return (_rex(r=destination, x=index, b=base) + b"\x8b" + _modrm(1, destination, 4)
            + _sib(3, index, base) + b"\x00")


def _store_indexed(base: int, index: int, source: int) -> bytes:
    return (_rex(r=source, x=index, b=base) + b"\x89" + _modrm(1, source, 4)
            + _sib(3, index, base) + b"\x00")


def _imul_indexed(destination: int, base: int, index: int) -> bytes:
    return (_rex(r=destination, x=index, b=base) + b"\x0f\xaf"
            + _modrm(1, destination, 4) + _sib(3, index, base) + b"\x00")


def _add(destination: int, source: int) -> bytes:
    return _rex(r=source, b=destination) + b"\x01" + _modrm(3, source, destination)


def _neg(register: int) -> bytes:
    return _rex(b=register) + b"\xf7" + _modrm(3, 3, register)


def _inc(register: int) -> bytes:
    return _rex(b=register) + b"\xff" + _modrm(3, 0, register)


def _cmp_imm(register: int, value: int) -> bytes:
    return _rex(b=register) + b"\x81" + _modrm(3, 7, register) + struct.pack("<i", value)


def _lea_stack(destination: int, offset: int) -> bytes:
    return (_rex(r=destination, b=4) + b"\x8d" + _modrm(2, destination, 4)
            + _sib(0, 4, 4) + struct.pack("<i", offset))


def _store_stack(offset: int, source: int) -> bytes:
    return (_rex(r=source, b=4) + b"\x89" + _modrm(2, source, 4)
            + _sib(0, 4, 4) + struct.pack("<i", offset))


def _sub_rsp(amount: int) -> bytes:
    return b"\x48\x81\xec" + struct.pack("<I", amount)


def _lea_rip(assembler: Assembler, destination: int, label: str, text: str) -> None:
    assembler.rel32(_rex(r=destination) + b"\x8d" + _modrm(0, destination, 5), label, text)


def _jump(assembler: Assembler, condition: str, label: str) -> None:
    opcodes = {"eq": b"\x0f\x84", "ne": b"\x0f\x85"}
    assembler.rel32(opcodes[condition], label, f"j{condition} {label}")


def _address_of(
    assembler: Assembler, ref: str, destination: int, source_values: Mapping[str, TypedValue],
    outputs: Mapping[str, PlannedStep],
) -> None:
    if ref in source_values:
        _lea_rip(assembler, destination, f"value.{ref}", f"lea r{destination}, [rip + value.{ref}]")
    else:
        offset = outputs[ref].output_offset
        assembler.emit(_lea_stack(destination, offset), f"lea r{destination}, [rsp + {offset}] ; {ref}")


def _emit_reduction(
    assembler: Assembler, left: str, right: str, dimension: int, output_offset: int,
    source_values: Mapping[str, TypedValue], outputs: Mapping[str, PlannedStep], label: str,
) -> None:
    _address_of(assembler, left, 12, source_values, outputs)
    _address_of(assembler, right, 13, source_values, outputs)
    assembler.emit(_xor(0), "xor rax, rax ; exact-integer accumulator")
    assembler.emit(_xor(10), "xor r10, r10 ; coordinate index")
    assembler.label(f"{label}.loop")
    assembler.emit(_load_indexed(11, 12, 10), "mov r11, [r12 + r10*8]")
    assembler.emit(_imul_indexed(11, 13, 10), "imul r11, [r13 + r10*8]")
    assembler.emit(_add(0, 11), "add rax, r11")
    assembler.emit(_inc(10), "inc r10")
    assembler.emit(_cmp_imm(10, dimension), f"cmp r10, {dimension}")
    _jump(assembler, "ne", f"{label}.loop")
    assembler.emit(_store_stack(output_offset, 0), f"mov [rsp + {output_offset}], rax ; observed scalar")


def _emit_transform(
    assembler: Assembler, source: str, dimension: int, output_offset: int,
    transform: Transform, source_values: Mapping[str, TypedValue], outputs: Mapping[str, PlannedStep],
    label: str,
) -> None:
    _address_of(assembler, source, 12, source_values, outputs)
    assembler.emit(_lea_stack(14, output_offset), f"lea r14, [rsp + {output_offset}] ; observed vector")
    assembler.emit(_xor(10), "xor r10, r10 ; coordinate index")
    assembler.label(f"{label}.loop")
    if transform.kind == "reflection":
        assembler.emit(_load_indexed(0, 12, 10), "mov rax, [r12 + r10*8]")
        assembler.emit(_cmp_imm(10, transform.parameter("axis")),
                       f"cmp r10, {transform.parameter('axis')}")
        _jump(assembler, "ne", f"{label}.store")
        assembler.emit(_neg(0), "neg rax ; reflected coordinate")
    else:
        i, j = transform.parameter("i"), transform.parameter("j")
        assembler.emit(_cmp_imm(10, i), f"cmp r10, {i}")
        _jump(assembler, "eq", f"{label}.load_j_neg")
        assembler.emit(_cmp_imm(10, j), f"cmp r10, {j}")
        _jump(assembler, "eq", f"{label}.load_i")
        assembler.emit(_load_indexed(0, 12, 10), "mov rax, [r12 + r10*8]")
        assembler.rel32(b"\xe9", f"{label}.store", f"jmp {label}.store")
        assembler.label(f"{label}.load_j_neg")
        assembler.emit(_mov_imm(9, j), f"mov r9, {j}")
        assembler.emit(_load_indexed(0, 12, 9), "mov rax, [r12 + r9*8]")
        assembler.emit(_neg(0), "neg rax ; quarter-turn first coordinate")
        assembler.rel32(b"\xe9", f"{label}.store", f"jmp {label}.store")
        assembler.label(f"{label}.load_i")
        assembler.emit(_mov_imm(9, i), f"mov r9, {i}")
        assembler.emit(_load_indexed(0, 12, 9), "mov rax, [r12 + r9*8]")
    assembler.label(f"{label}.store")
    assembler.emit(_store_indexed(14, 10, 0), "mov [r14 + r10*8], rax ; observable result, not temporary")
    assembler.emit(_inc(10), "inc r10")
    assembler.emit(_cmp_imm(10, dimension), f"cmp r10, {dimension}")
    _jump(assembler, "ne", f"{label}.loop")


def encode_scalar_plan(plan: ScalarPlan) -> CompiledImage:
    assembler = Assembler()
    stack_size = (plan.result_size + 15) & ~15
    assembler.emit(_sub_rsp(stack_size), f"sub rsp, {stack_size} ; explicit observation buffer")
    source_values = {item.name: item for item in plan.artifact.values}
    transforms = {item.name: item for item in plan.artifact.transforms}
    outputs: dict[str, PlannedStep] = {}
    for index, planned in enumerate(plan.steps):
        step = planned.step
        label = f"step{index}.{step.name}"
        assembler.label(label)
        if step.kind == "Contract":
            dimension = _ref_runtime_type(step.argument("vector"), source_values, outputs).dimension
            _emit_reduction(assembler, step.argument("covector"), step.argument("vector"), dimension,
                            planned.output_offset, source_values, outputs, label)
        elif step.kind == "Dot":
            dimension = _ref_runtime_type(step.argument("left"), source_values, outputs).dimension
            _emit_reduction(assembler, step.argument("left"), step.argument("right"), dimension,
                            planned.output_offset, source_values, outputs, label)
        elif step.kind == "SquaredNorm":
            dimension = _ref_runtime_type(step.argument("vector"), source_values, outputs).dimension
            _emit_reduction(assembler, step.argument("vector"), step.argument("vector"), dimension,
                            planned.output_offset, source_values, outputs, label)
        elif step.kind in {"Reflect", "RotatePlane"}:
            transform = _unique_step_transform(step, tuple(transforms.values()))
            _emit_transform(assembler, step.argument("vector"), planned.result_type.dimension,
                            planned.output_offset, transform, source_values, outputs, label)
        elif step.kind == "ActOnSphere":
            _emit_transform(assembler, step.argument("point"), planned.result_type.dimension,
                            planned.output_offset, transforms[step.argument("transform")],
                            source_values, outputs, label)
        else:
            raise AssertionError(step.kind)
        outputs[step.result] = planned

    assembler.emit(_mov_imm(0, 1), "mov rax, 1 ; SYS_write")
    assembler.emit(_mov_imm(7, 1), "mov rdi, 1 ; stdout")
    assembler.emit(_mov_reg(6, 4), "mov rsi, rsp ; exact binary observations")
    assembler.emit(_mov_imm(2, plan.result_size), f"mov rdx, {plan.result_size}")
    assembler.emit(b"\x0f\x05", "syscall")
    assembler.emit(_xor(7), "xor rdi, rdi ; status 0")
    assembler.emit(_mov_imm(0, 60), "mov rax, 60 ; SYS_exit")
    assembler.emit(b"\x0f\x05", "syscall")
    for value in plan.artifact.values:
        assembler.label(f"value.{value.name}")
        raw = b"".join(struct.pack("<q", coordinate) for coordinate in value.coordinates)
        assembler.emit(raw, f".quad {value.name}[{value.dimension}] ; checked {value.kind} {value.space}")
    machine, listing = assembler.finish()
    elf = write_elf(machine)
    return CompiledImage(elf, listing + _inspection_listing(plan), plan)


def _ref_runtime_type(
    ref: str, source_values: Mapping[str, TypedValue], outputs: Mapping[str, PlannedStep]
) -> RuntimeType:
    if ref in source_values:
        item = source_values[ref]
        return RuntimeType(item.kind, item.space, item.dimension)
    return outputs[ref].result_type


def _unique_step_transform(step: Step, transforms: Sequence[Transform]) -> Transform:
    if step.kind == "Reflect":
        matches = [item for item in transforms if item.kind == "reflection"
                   and item.space == step.argument("space")
                   and item.parameter("axis") == _integer(step.argument("axis"), step.name)]
    else:
        matches = [item for item in transforms if item.kind == "plane_rotation"
                   and item.space == step.argument("space")
                   and item.ambient == _integer(step.argument("ambient"), step.name)
                   and item.parameter("i") == _integer(step.argument("i"), step.name)
                   and item.parameter("j") == _integer(step.argument("j"), step.name)
                   and item.parameter("turns") == _integer(step.argument("turns"), step.name)]
    if len(matches) != 1:
        raise AssertionError("validated transform resolution changed")
    return matches[0]


def _inspection_listing(plan: ScalarPlan) -> str:
    lines = ["", "# backend plan", "plan scalar_integer ; signed i64, overflow bound checked"]
    lines.extend(f"plan {item.step.name} scalar_integer" for item in plan.steps)
    lines.append("# one-step temporaries are not presumed memory stores")
    lines.extend(f"temporary {item.name} {item.decision} {item.detail}"
                 for item in plan.temporary_decisions)
    lines.extend(("fallback RefC ABSENT", "fallback c_compiler ABSENT",
                  "fallback assembler ABSENT", "fallback linker ABSENT", "fallback libc ABSENT"))
    return "\n".join(lines) + "\n"


def write_elf(code_and_data: bytes) -> bytes:
    entry = ELF_BASE + CODE_OFFSET
    file_size = CODE_OFFSET + len(code_and_data)
    ident = b"\x7fELF\x02\x01\x01" + b"\x00" * 9
    elf_header = ident + struct.pack(
        "<HHIQQQIHHHHHH", 2, 62, 1, entry, 64, 0, 0, 64, 56, 1, 0, 0, 0
    )
    program_header = struct.pack(
        "<IIQQQQQQ", 1, 5, 0, ELF_BASE, ELF_BASE, file_size, file_size, 0x1000
    )
    headers = elf_header + program_header
    return headers + bytes(CODE_OFFSET - len(headers)) + code_and_data


def compile_artifact(
    artifact_path: Path, output_path: Path, listing_path: Path | None = None,
    source_path: Path | None = None,
) -> CompiledImage:
    artifact = parse_checked_artifact(artifact_path)
    if source_path is not None:
        digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
        if digest != artifact.source_sha256:
            _fail("source_digest_mismatch", f"artifact has {artifact.source_sha256}, source has {digest}")
    compiled = encode_scalar_plan(make_scalar_plan(artifact))
    output_path.write_bytes(compiled.elf)
    output_path.chmod(0o755)
    if listing_path is not None:
        listing_path.write_text(compiled.listing)
    return compiled


def decode_observations(plan: ScalarPlan, raw: bytes) -> tuple[tuple[str, str, str], ...]:
    if len(raw) != plan.result_size:
        _fail("native_output_size", f"expected {plan.result_size} bytes, got {len(raw)}")
    observations: list[tuple[str, str, str]] = []
    for item in plan.steps:
        count = 1 if item.result_type.kind == "scalar" else item.result_type.dimension
        values = struct.unpack_from(f"<{count}q", raw, item.output_offset)
        observations.append((item.step.result, item.result_type.kind,
                             ",".join(str(value) for value in values)))
    return tuple(observations)


def backend_head(repository_root: Path | None = None) -> str:
    root = repository_root or Path(__file__).resolve().parents[1]
    run = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, check=True,
                         capture_output=True, text=True)
    head = run.stdout.strip()
    if not GIT_HEAD.fullmatch(head):
        raise RuntimeError(f"git returned malformed head {head!r}")
    return head


def render_execution_receipt(
    compiled: CompiledImage, native_stdout: bytes, head: str,
    rejections: Iterable[tuple[str, str, str]] = (),
) -> str:
    if not GIT_HEAD.fullmatch(head):
        raise ValueError("backend head must be a full 40-character commit")
    observations = decode_observations(compiled.plan, native_stdout)
    lines = [RECEIPT_HEADER, f"artifact_sha256\t{compiled.plan.artifact.sha256}",
             f"compiler_head\t{compiled.plan.artifact.compiler_repository}\t"
             f"{compiled.plan.artifact.compiler_head}",
             f"backend_head\t{BACKEND_REPOSITORY}\t{head}",
             "target\tx86_64-linux-direct-elf"]
    lines.extend(f"plan\t{item.step.name}\t{item.realization}" for item in compiled.plan.steps)
    lines.extend(f"temporary\t{item.name}\t{item.decision}\t{item.detail}"
                 for item in compiled.plan.temporary_decisions)
    lines.extend((
        "stage\tsource_parse\tPASS\tpropagated from bound compiler artifact; emitter runs only after source parsing",
        "stage\tconstraint_generation\tPASS\tpropagated from bound compiler artifact and typed certificate traces",
        "stage\tconstraint_resolution\tPASS\tpropagated from bound compiler artifact; every referenced certificate is PASS",
        "stage\tcore_typecheck\tPASS\tpropagated from artifact core_typecheck row at the bound compiler head",
        "stage\tone_step_form\tPASS\tstrict EDRIC_MATH_ONE_STEP v1 artifact validated",
        "stage\tbackend_plan\tPASS\texact signed i64 scalar baseline; overflow bound checked",
        "stage\ttarget_codegen\tPASS\tdirect in-process x86-64 encoder and ELF writer",
        "stage\tnative_execution\tPASS\tgenerated ELF ran on hosted x86_64 Linux",
        "fallback\tRefC\tABSENT", "fallback\tc_compiler\tABSENT",
        "fallback\tassembler\tABSENT", "fallback\tlinker\tABSENT", "fallback\tlibc\tABSENT",
        f"elf_sha256\t{hashlib.sha256(compiled.elf).hexdigest()}",
    ))
    step_by_result = {item.step.result: item for item in compiled.plan.steps}
    for name, kind, coordinates in observations:
        item = step_by_result[name]
        if kind == "scalar":
            lines.append(f"observation\tscalar\t{name}\texact_integer\t{coordinates}")
        else:
            lines.append(f"observation\tvector\t{name}\t{item.result_type.space}\t"
                         f"{item.result_type.dimension}\texact_integer\t{coordinates}")
    lines.extend(f"rejection\t{case}\t{stage}\t{code}" for case, stage, code in rejections)
    lines.append("end")
    return "\n".join(lines) + "\n"


def run_native(compiled: CompiledImage, output_path: Path) -> bytes:
    if platform.system() != "Linux" or platform.machine() not in {"x86_64", "AMD64"}:
        raise RuntimeError("native_execution SKIP: requires hosted x86_64 Linux")
    run = subprocess.run([os.fspath(output_path)], check=False, capture_output=True)
    if run.returncode != 0:
        raise RuntimeError(f"generated ELF exited {run.returncode}; stderr={run.stderr!r}")
    if run.stderr:
        raise RuntimeError(f"generated ELF wrote stderr: {run.stderr!r}")
    decode_observations(compiled.plan, run.stdout)
    return run.stdout


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path, help="checked one-step artifact; never .idric source")
    parser.add_argument("-o", "--output", type=Path, required=True)
    parser.add_argument("--source", type=Path, help="used only to verify source_sha256")
    parser.add_argument("--listing", type=Path)
    parser.add_argument("--run-receipt", type=Path)
    args = parser.parse_args()
    compiled = compile_artifact(args.artifact, args.output, args.listing, args.source)
    if args.run_receipt is not None:
        stdout = run_native(compiled, args.output)
        args.run_receipt.write_text(render_execution_receipt(compiled, stdout, backend_head()))


if __name__ == "__main__":
    main()
