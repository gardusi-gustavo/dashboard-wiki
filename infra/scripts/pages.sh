#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
OUT_DIR="${OUT_DIR:-$ROOT/dist}"
args=(--out "$OUT_DIR")
if [[ -d _database/data ]]; then
  args+=(--database _database)
fi
python3 infra/scripts/build.py "${args[@]}"
