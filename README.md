# wiki

Public wiki: media catalog, characters, theories, recipes, reference, and
household runbooks.

## Status

Public. This is the audited public subset of the former private wiki. Sensitive
pages remain in `gardusi-gustavo/private`.

## Layout

| Path | Holds |
| --- | --- |
| `docs/characters/` | per-franchise lore |
| `docs/playlists/` | media catalog, marks, taxonomy |
| `docs/analysis/` | media reads and structural notes |
| `docs/theories/` | frameworks and general theory |
| `docs/instruments/` | instrument notes |
| `docs/kitchen/recipes/` | repeatable recipes |
| `docs/home/` | generic housing, plant, and household runbooks |
| `docs/reference/` | tools, finance, health, career, and sport reference |
| `docs/tasks/` | recurring playbooks |
| `docs/system-design/` | architecture examples, AWS drills, and interview topics |
| `src/data/playlists/` | legacy media catalog mirror; database is authoritative |
| `src/data/schema/` | catalog schema |

## Rules

- Public-safe content only.
- No addresses, income, balances, health records, credentials, or life events.
- No links to private cases or `gardusi-gustavo/private`.
- See [`docs/classification.md`](docs/classification.md) for the split.

## Validation

```bash
bash infra/scripts/ci.sh
```
