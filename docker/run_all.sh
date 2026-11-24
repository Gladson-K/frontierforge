#!/usr/bin/env bash
set -u

cd "$(dirname "$0")/.."
status=0

for name in quantum neuro bayes photonic cellular reversible reservoir tests; do
  echo "=== building frontierforge:${name} ==="
  if docker build -f "docker/Dockerfile.${name}" -t "frontierforge:${name}" .; then
    echo "=== running frontierforge:${name} ==="
    docker run --rm "frontierforge:${name}" || status=1
  else
    status=1
  fi
done

exit "$status"
