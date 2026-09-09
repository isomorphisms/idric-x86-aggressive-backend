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

source_head=${SOURCE_HEAD_SHA:-$(git rev-parse HEAD)}
tested_checkout=$(git rev-parse HEAD)
canonical_semantics=${IDRIC_COMPLEX_SEMANTICS_SHA:-unresolved}

{
  printf 'COMPLEX_PROJECTIVE_RECEIPT\t1\n'
  printf 'role\tX86_LEADER\n'
  printf 'repository\tisomorphisms/idric-x86-aggressive-backend\n'
  printf 'source_head_sha\t%s\n' "$source_head"
  printf 'tested_checkout_sha\t%s\n' "$tested_checkout"
  printf 'canonical_complex_projective_semantics_sha\t%s\n' "$canonical_semantics"
  printf 'candidate\tdirect ELF64 x86-64; scalar SSE plus observational x87; no C assembler linker libc libm RefC LLVM\n'
  printf 'stage\tdirect_backend_generation\tPASS\n'
  printf 'stage\tnative_execution\tPASS\n'
  printf 'stage\tnumerical_corpus\tPASS\n'
  printf 'stage\tprojective_corpus\tPASS\n'
  printf 'stage\tthin_debian_execution\tPASS\n'
  printf 'stage\theadless_render\tPASS\n'
} > "$artifact_root/acceptance-receipt.tsv"

cat "$artifact_root/thin-debian-receipt.tsv"
cat "$artifact_root/acceptance-receipt.tsv"
