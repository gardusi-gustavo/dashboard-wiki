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
    ap.add_argument("--database")
    ap.add_argument("--out", default="dist")
    args = ap.parse_args()
    root = Path(__file__).resolve().parent.parent.parent
    database = Path(args.database).resolve() if args.database else None
    out = Path(args.out).resolve()
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    docs = root / "docs"
    if docs.is_dir():
        shutil.copytree(docs, out / "docs")
    local_data = root / "src/data/playlists"
    data_dir = (database / "data/playlists") if database and (database / "data/playlists").is_dir() else local_data
    catalog_file = data_dir / "catalog.json"
    if catalog_file.exists():
        files = [catalog_file]
    else:
        files = sorted(data_dir.glob("20*.json")) if data_dir.is_dir() else []
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
    wiki_rows = ""
    if database and (database / "data/index.json").is_file():
        wiki_index = json.loads((database / "data/index.json").read_text(encoding="utf-8"))
        pages_out = out / "wiki"
        pages_out.mkdir(parents=True, exist_ok=True)
        links = []
        for entry in wiki_index.get("pages", []):
            page_file = database / "data" / entry["path"]
            if not page_file.is_file():
                continue
            page = json.loads(page_file.read_text(encoding="utf-8"))
            slug = page.get("slug") or page.get("id")
            body = html.escape(page.get("body", ""))
            (pages_out / f"{slug}.html").write_text(
                f"<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
                f"<title>{html.escape(page.get('title', slug))}</title></head><body>"
                f"<h1>{html.escape(page.get('title', slug))}</h1><pre>{body}</pre>"
                f"</body></html>", encoding="utf-8")
            links.append(f"<li><a href=\"wiki/{html.escape(slug)}.html\">{html.escape(page.get('title', slug))}</a></li>")
        wiki_rows = "<h2>Wiki database</h2><ul>" + "".join(links) + "</ul>"
        (out / "data").mkdir(parents=True, exist_ok=True)
        shutil.copy2(database / "data/index.json", out / "data/wiki.json")
    counts = "".join(f"<li>{html.escape(k)}: {len(v) if isinstance(v, list) else '?'}</li>"
                    for k, v in sorted(catalog.items()))
    (out / "index.html").write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>wiki</title>
<style>body{{font-family:system-ui,sans-serif;max-width:70rem;margin:2rem auto;padding:0 1rem}}</style>
</head><body><h1>wiki</h1>
<p>Built from the local playlists catalog and the local docs.</p>
<h2>Sections</h2><ul>{rows}</ul>
<h2>Media catalog</h2><ul>{counts}</ul>{wiki_rows}
</body></html>
""", encoding="utf-8")
    print(f"built {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
