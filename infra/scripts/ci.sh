#!/usr/bin/env bash
set -euo pipefail
ROOT="${CI_PROJECT_DIR:-$(git rev-parse --show-toplevel)}"
cd "$ROOT"
"$ROOT/infra/scripts/ci/validate-repo.sh" --root "$ROOT"
"$ROOT/infra/scripts/ci/check-size.sh" --root "$ROOT"
echo "wiki checks ok"

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/database/data/playlists"
python3 - "$tmp/database/data/playlists/2026-11-08.json" <<'PY'
import json, sys
json.dump({"schema": 1, "domain": "playlists", "date": "2026-11-08",
           "generated_at": "2026-11-08T00:00:00Z", "source": {"provider": "ci"},
           "collections": {}}, open(sys.argv[1], "w"))
PY
python3 infra/scripts/build.py --database "$tmp/database" --out "$tmp/dist"
test -s "$tmp/dist/index.html"
