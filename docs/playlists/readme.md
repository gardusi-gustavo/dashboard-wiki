# 🎬 Playlists

> **Visibility:** private until the review closes.

**Eyes + ears — what you watch and listen to.** This is the catalog view.

Local files, disk availability, and card inventory are out of scope.
Status means watch progress only: 🟢 watched · 🟡 in progress · 🔴 not started.

The movies/series views are **generated** from the JSON source of truth in
`../../src/data/playlists`; the rest are hand-maintained data tables.

## 🗂️ Contents

- `entertainment/` — films, series, and music. See [🍿 Entertainment](entertainment/readme.md).
- `games/` — video and board games. See [🎮 Games](games/readme.md).
- `books/` — audiobooks, finished and queued.
- topic folders — `news/` · `finance/` · `tech/` · `learning/` · `culture/` · `sports/` · `health/`, podcasts filed by what they're about.
- `sounds/` — background soundscapes and noise.
- `taxonomy.md` — the nine questions, facet definitions, and core rule.
- `templates/` — work card and batch worksheet.

## 🧱 Shared rules

Every content file starts with its `# <H1>` and then its data tables. Tables are wrapped in begin/end-table comment markers (one per line, nothing else). The **Status** marker is 🟢 watched · 🟡 in progress · 🔴 not started.

## 🍿 Entertainment

Films and series live under `entertainment/`, by domain (plus `animation/west` and `animation/east`); music is `entertainment/music/`. Each domain view uses the four-table template — **🧭 Index → ⏳ In progress → 🔴 Not started → 📚 Catalog** — and is generated from `../../src/data/playlists`; edit the JSON, not the view, then regenerate the views. See [entertainment/readme.md](entertainment/readme.md).

Every work has one `core-domain` and a set of `domains` grouped by facet. The core is the ultimate subject; environment, pursuit, method, and tone are tags. Read [taxonomy.md](taxonomy.md) before tagging.

## 🎧 Audiobooks

`books/finished.md` and `books/queue.md`. Finished book rows:

<!-- begin table -->
| Book | Author | Length | Finished | Rating | Notes |
| --- | --- | --- | --- | --- | --- |
<!-- end table -->

The queue file has an `In progress` section and a `Waiting` section:

<!-- begin table -->
| Book | Author | Started | Last position | % Remaining | Time left |
| --- | --- | --- | --- | --- | --- |
<!-- end table -->

## 🎵 Music

`entertainment/music/` — **audio-only**, organized by folders; each file holds one `## 📝 Suggestions` table:

<!-- begin table -->
| Song | Original | Type | Performer | Artist | Featuring | Context | Media | Album | Duration | Link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
<!-- end table -->

Folders: `standard/` · `remix/` · `instrumental/` · `soundtrack/` · `live/` · `cover/`. A song goes to the folder matching its form; the live-vs-cover rule decides `live/` (an original member performs) vs `cover/`.

## 🎙️ Topics

Podcasts are filed by topic — `news/` · `finance/` · `tech/` · `learning/` · `culture/` · `sports/` · `health/` — generated from `../../src/data/playlists/podcasts.json` (edit the JSON, then run `npm run playlists`). Each topic readme holds a `| Podcast | Subs | Avg | Find on |` table.

## 🔊 Sounds

Background soundscapes and noise for patience / focus. One row per video:

<!-- begin table -->
| Title | Duration | Channel | Link |
| --- | --- | --- | --- |
<!-- end table -->

- `natural.md` — natural sources (water, weather, forest) — you can see the source
- `tools.md` — machine-made noise (fan, appliances) — you can't see the source
- `colors.md` — generated noise colors (white, pink, brown)