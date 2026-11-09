#!/usr/bin/env python3
"""Build the wiki portal and copy the database media catalog at build time."""
from __future__ import annotations

import argparse
import html
import json
import shutil
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--database", required=True)
    ap.add_argument("--out", default="dist")
    args = ap.parse_args()
    root = Path(__file__).resolve().parent.parent.parent
    database = Path(args.database).resolve()
    out = Path(args.out).resolve()
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    docs = root / "docs"
    if docs.is_dir():
        shutil.copytree(docs, out / "docs")
    data_dir = database / "data/playlists"
    files = sorted(data_dir.glob("*.json")) if data_dir.is_dir() else []
    catalog = {}
    if files:
        dataset = json.loads(files[-1].read_text(encoding="utf-8"))
        catalog = dataset.get("collections") or {}
        (out / "data").mkdir(parents=True, exist_ok=True)
        shutil.copy2(files[-1], out / "data" / "playlists.json")
    rows = "".join(
        f"<li><a href=\"docs/{html.escape(p.name)}/\">{html.escape(p.stem.title())}</a></li>"
        for p in sorted(docs.iterdir()) if p.is_dir()
    ) if docs.is_dir() else ""
    counts = "".join(f"<li>{html.escape(k)}: {len(v) if isinstance(v, list) else '?'}</li>"
                    for k, v in sorted(catalog.items()))
    (out / "index.html").write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>wiki</title>
<style>body{{font-family:system-ui,sans-serif;max-width:70rem;margin:2rem auto;padding:0 1rem}}</style>
</head><body><h1>wiki</h1>
<p>Built from <code>gardusi-gustavo/database</code> and the local docs.</p>
<h2>Sections</h2><ul>{rows}</ul>
<h2>Media catalog</h2><ul>{counts}</ul>
</body></html>
""", encoding="utf-8")
    print(f"built {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
