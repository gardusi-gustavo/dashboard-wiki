# Data

The source of truth is now the local playlists catalog under
`src/data/playlists/catalog.json`. The checked-in `src/data/` tree is the
build-time fallback during the migration.

| File | Holds |
| --- | --- |
| `src/data/playlists/movies.json` | 235 film entries |
| `src/data/playlists/series.json` | 379 series entries |
| `src/data/playlists/music.json` | music blocks |
| `src/data/playlists/games.json` | game blocks |
| `src/data/playlists/audiobooks.json` | audiobook blocks |
| `src/data/playlists/podcasts.json` | podcast shows |
| `src/data/playlists/sounds.json` | sound blocks |
| `src/data/taxonomy.json` | domains, facets, core rule |
| `src/data/schema/` | JSON schema |

## Planned

The JSON source is temporary. The migration to `schema.sql` + `seed.sql` is
tracked in an issue. Until then, edit the JSON and keep it valid.

## Rules

- `core-domain` is the primary domain.
- `domains` are tags grouped by `environment`, `pursuit`, `method`, `tone`,
  `medium`.
- `mark`: `0 none`, `1 star`, `2 up`, `3 down`.
- Queue: `next`, `in-progress`, `done`; done has `completed` or `dropped`.
