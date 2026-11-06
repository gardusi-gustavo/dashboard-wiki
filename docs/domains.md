# Domains

The folder is the work's **core domain**. Tags are extra facets.

## Core rule

Classify by the protagonist's transformation, not by setting or plot goal.

1. Q4 — what does the protagonist become?
2. Q3 — what do the characters argue about most?
3. Q9 — what is the final scene about?
4. Q1 — the setting, only when the place is the subject
5. Never Q5 — the goal is a tag, not the core

`rehab` is a method, not a core, unless the program itself is the subject.
`Oldboy` is `discipline`; `revenge` is only the goal. `The Founder` is
`business`; `kitchen` is only the setting.

The full registry and the nine-question worksheet are in
[playlists/taxonomy.md](playlists/taxonomy.md).

## Structure

A work is either a file or a folder:

```text
single work      title-year.ext
multi-file work  title-year/
series           show-year/
film franchise   franchise/
```

Inside a folder, alphabetical order is watch order:

```text
series     s01e01-title.ext
franchise  01-title-year.ext
```

Kebab-case everywhere: `[a-z0-9-]`, lowercase ASCII, no punctuation.

## Scope

| Format | Meaning |
|---|---|
| `film` | one film |
| `season` | one TV season, or one film franchise of ≤10 films |
| `sample` | 3–6 episodes, or 3–5 ambient/instructional clips |
| `full` | all seasons; explicit exception only |

Defaults:

- TV series: `season` — S1 only.
- Film franchise: `season` — all films in one folder.
- Ambient/instructional: `sample`.
- Promote to `full` only while actively watching.

## Pruning

- `season`/`sample`: keep S1, or the first 3–6 episodes; delete later seasons.
- A film franchise counts as one season: keep all films (≤10).
- `full`: exempt.
- Prune before converting. Keep the source until the portable copy is verified.

## Canonical title

Use the current international English name — the name most people search for
today — even when it differs from the release title. If it was released as A
but is now commonly found as B, use B.

Decision order:

1. English Wikipedia article title (target, not redirect).
2. TMDB English title / IMDb primary title; if both agree, use it.
3. Official international distributor or streamer title.
4. Search volume only as a tie-breaker.
5. If still tied, use the shorter unambiguous form.

Slugs: lowercase ASCII kebab-case; include the year for films and series; keep
the full title; keep episode titles when known.

## Audio and subtitles

- Prefer English audio; keep the original track when it is the point.
- A foreign-original work is valid with original audio + English subtitles.
- English should be the default track when present.
- Portable subtitles: SRT, UTF-8, one language.
- Drop commentary, extra languages, and sidecars after conversion.

## Card

The card is the portable, star set. If it is on the card, it is `star`.
No health tables, no ownership fields, no per-file inventory.
