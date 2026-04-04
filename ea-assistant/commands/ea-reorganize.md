---
name: ea-reorganize
description: Move flat-path artifacts in an EA engagement into their correct phase subfolders (preliminary/, phase-a/, phase-b/, etc.) and update all engagement.json file paths to match.
argument-hint: "[--report] [--auto]"
allowed-tools: [Read, Write, Glob, Bash]
---

You are executing the `/ea-reorganize` command.

## Overview

Scans the active engagement for artifacts stored at flat paths (`artifacts/{artifact-id}.md`) and moves them into the correct phase subfolder (`artifacts/{phase-folder}/{artifact-id}.md`), updating `engagement.json` to match.

This command does **one thing only** — file moves. It does not patch frontmatter, add appendices, or touch `engagement.json` fields other than the `file` path of each moved artifact.

**This command never moves a file without the user's explicit approval.**

Flags:
- `--report` — list what would be moved; make no changes
- `--auto` — apply all moves without per-file confirmation (still announces each move)

---

## Phase Folder Mapping

| `phase:` frontmatter value (canonical + aliases) | Target folder |
|---|---|
| `Preliminary`, `Prelim`, `prelim` | `preliminary/` |
| `Requirements`, `requirements` | `requirements/` |
| `A`, `Phase A`, `Architecture Vision` | `phase-a/` |
| `B`, `Phase B`, `Business Architecture` | `phase-b/` |
| `C-Data`, `Phase C Data`, `C Data`, `Data Architecture` | `phase-c-data/` |
| `C-App`, `Phase C App`, `C App`, `Application Architecture` | `phase-c-app/` |
| `D`, `Phase D`, `Technology Architecture` | `phase-d/` |
| `E`, `Phase E`, `B-D` | `phase-e/` |
| `F`, `Phase F` | `phase-f/` |
| `G`, `Phase G` | `phase-g/` |
| `H`, `Phase H` | `phase-h/` |
| `Cross-cutting`, `cross-cutting`, `Cross Cutting` | `cross-cutting/` |

---

## Step 1 — Resolve Active Engagement

Check context for active slug; if none, scan `EA-projects/*/engagement.json` and ask the user to confirm which engagement to reorganize. Read `engagement.json` and extract `name`, `slug`, and `artifacts[]`.

---

## Step 2 — Find Flat-Path Artifacts

Identify artifacts whose `file` path in `engagement.json` is directly under `artifacts/` with no phase subfolder — i.e. the path matches `artifacts/{artifact-id}.md` rather than `artifacts/{phase-folder}/{artifact-id}.md`.

For each flat-path artifact:
1. Read the artifact file and extract the `phase:` frontmatter field
2. Look up the target folder in the Phase Folder Mapping above
3. If the `phase:` value does not match any row: mark as **unmappable** — skip and flag for manual review

---

## Step 3 — Produce the Reorganization Plan

```
════════════════════════════════════════════════════════════
REORGANIZE — {engagement name}
════════════════════════════════════════════════════════════

Artifacts to move               {N | ✅ None — already organized}

  architecture-vision.md        artifacts/ → artifacts/phase-a/
  business-architecture.md      artifacts/ → artifacts/phase-b/
  requirements-register.md      artifacts/ → artifacts/requirements/

Unmappable (phase: value not recognized)
  some-artifact.md              phase: "Unknown" — set correct phase: in frontmatter, then re-run

════════════════════════════════════════════════════════════
```

Stop here if `--report` was specified or if there are no moveable artifacts.

---

## Step 4 — Confirm and Move

If `--auto` is **not** set, ask per artifact:

```
Move artifacts/architecture-vision.md → artifacts/phase-a/architecture-vision.md ? (y / n / all / quit)
```

- `y` — move this file
- `n` — skip this file
- `all` — move all remaining without further prompts
- `quit` — stop without making any further changes

For each approved move:
1. Create the target phase subfolder if it does not exist: `mkdir -p EA-projects/{slug}/artifacts/{phase-folder}/`
2. Move the file: `mv EA-projects/{slug}/artifacts/{artifact-id}.md EA-projects/{slug}/artifacts/{phase-folder}/{artifact-id}.md`
3. Update the `file` field in `engagement.json → artifacts[]` for this artifact to the new path

---

## Step 5 — Finalise

After all moves are applied or skipped:

1. Update `engagement.json`: set `lastModified` to now
2. Print a summary:

```
Moved:   {N} artifacts
Skipped: {N} artifacts
Unmappable: {N} artifacts (set phase: frontmatter and re-run)

Run /ea-migrate to check for other alignment gaps.
```
