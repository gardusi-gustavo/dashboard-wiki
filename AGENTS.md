# AGENTS.md

## Start here

- Read `README.md`.
- Read `docs/README.md` and `docs/classification.md`.
- Search open Gitea issues before starting.

## Scope

This repository is the public wiki. It contains public-safe reference and media
notes only. Sensitive records, cases, and private context stay in
`private/private`.

## Rules

- Never copy private case material or personal data into this repository.
- Keep Markdown in `docs/` and JSON in `src/`.
- Use repo-root path references in non-README Markdown.
- Update `docs/classification.md` when moving a section.

## Validation

```bash
bash infra/scripts/ci.sh
```

<!-- begin local-issues -->
## Local tasks

- The backlog is `docs/issues/`, one JSON file per task.
- Append tasks; do not rewrite task history.
- Rank: `3.x` bugs, `2.x` documentation/chores, `1.x` features/refactors.
  Higher fraction = more important.
- Filename: `<rank>-<slug>.json`; no trailing zero; one to six fractional digits.
- The file is the task. There is no author, source, platform, or status field.
- Pick the highest-ranked task.
- One work PR per repository.
- Open one native issue for the work item when the pull request starts.
- The PR references the task and the issue:
  `Task: docs/issues/<file>.json` and `Closes #N`.
- Merge deletes the task file and closes the issue. Git history keeps the record.
- On a failed PR, append an attempt to the task file, close the PR, and keep the file.
- Native issues created by the owner or external contributors remain native.
<!-- end local-issues -->
