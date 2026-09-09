#!/usr/bin/env bash
set -Eeuo pipefail

artifact_root=${1:?usage: run_complex_projective_thin_debian.sh ARTIFACT_DIR}
artifact_root=$(cd "$artifact_root" && pwd)

for executable in complex-corpus.elf complex-render.elf; do
  if [[ ! -x "$artifact_root/$executable" ]]; then
    echo "missing executable artifact: $artifact_root/$executable" >&2
    exit 1
  fi
done

docker run --rm \
  -v "$artifact_root:/work:ro" \
  debian:13-slim \
  /work/complex-corpus.elf > "$artifact_root/thin-debian-complex-corpus.bin"

cmp "$artifact_root/complex-corpus.bin" \
    "$artifact_root/thin-debian-complex-corpus.bin"

docker run --rm \
  -v "$artifact_root:/work:ro" \
  debian:13-slim \
  /work/complex-render.elf > "$artifact_root/thin-debian-complex-projective-scene.ppm"

cmp "$artifact_root/complex-projective-scene.ppm" \
    "$artifact_root/thin-debian-complex-projective-scene.ppm"

{
  printf 'THIN_DEBIAN_COMPLEX_PROJECTIVE\t1\n'
  printf 'image\tdebian:13-slim\n'
  printf 'stage\tnative_numerical_execution\tPASS\n'
  printf 'stage\theadless_render\tPASS\n'
  printf 'comparison\tbyte_identical_to_host_x86\tPASS\n'
} > "$artifact_root/thin-debian-receipt.tsv"

cat "$artifact_root/thin-debian-receipt.tsv"
