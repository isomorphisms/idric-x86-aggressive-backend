#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pins="$repo_root/research/source-pins.json"

xed_sha="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["intel_xed"]["commit"])' "$pins")"
mbuild_sha="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["intel_mbuild"]["commit"])' "$pins")"

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

fetch_commit() {
    local url="$1"
    local sha="$2"
    local dst="$3"
    git init -q "$dst"
    git -C "$dst" remote add origin "$url"
    git -C "$dst" fetch -q --depth 1 origin "$sha"
    git -C "$dst" checkout -q --detach FETCH_HEAD
}

fetch_commit https://github.com/intelxed/xed.git "$xed_sha" "$work/xed"
fetch_commit https://github.com/intelxed/mbuild.git "$mbuild_sha" "$work/mbuild"

(
    cd "$work/xed"
    python3 mfile.py just-prep
    python3 pysrc/xed_to_db.py \
        --xed-dgen=obj/dgen \
        --out="$work/xed-db.json" \
        --compact \
        --validate
)

python3 "$repo_root/scripts/xed-json-to-inventory.py" \
    "$work/xed-db.json" \
    --out-dir "$repo_root/generated" \
    --summary "$repo_root/docs/x86-isa-inventory.generated.md"

printf 'Generated %s\n' "$repo_root/generated/xed-iclasses.txt"
printf 'Generated %s\n' "$repo_root/generated/xed-iforms.txt"
printf 'Generated %s\n' "$repo_root/generated/xed-instructions.tsv"
printf 'Generated %s\n' "$repo_root/docs/x86-isa-inventory.generated.md"
