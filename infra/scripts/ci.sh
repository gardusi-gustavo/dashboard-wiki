#!/usr/bin/env bash
set -euo pipefail
ROOT="${CI_PROJECT_DIR:-$(git rev-parse --show-toplevel)}"
cd "$ROOT"
"$ROOT/infra/scripts/ci/validate-repo.sh" --root "$ROOT"
"$ROOT/infra/scripts/ci/check-size.sh" --root "$ROOT"
echo "wiki checks ok"

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
python3 infra/scripts/build.py --out "$tmp/dist"
test -s "$tmp/dist/index.html"
test -s "$tmp/dist/data/playlists.json"
