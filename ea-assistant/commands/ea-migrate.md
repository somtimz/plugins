---
name: ea-migrate
description: Detect and resolve alignment gaps between an EA engagement and the current ea-assistant version — missing taxonomy, appendices, new artifacts, engagement.json schema fields, template body sections/guidance the artifact predates, section ordering, and heuristically-detected misplaced content (moved within or across documents). Body sections/reorder/content-moves are confirmed per item, snapshotted, and excluded from --auto. Always asks permission before making any change.
argument-hint: "[--report] [--auto] [--force]"
allowed-tools: [Read, Write, Bash, Glob]
---

You are executing the `/ea-migrate` command. Load the `ea-engagement-lifecycle` skill and the `ea-artifact-templates` skill for context.

## Overview

Scans the active engagement for alignment gaps between its artifacts and the current ea-assistant template standard, then offers targeted remediation with **explicit per-item confirmation before any change**.

**This command never modifies files without the user's explicit approval.**

Flags:
- `--report` — scan and report only; do not offer remediation
- `--auto` — apply all non-destructive remediations without confirmation (excludes 3g detail-file creation and the 3a structural flattens, which always require per-item confirmation)
- `--force` — run the full gap scan even when version stamps already match the current version (structural drift can persist across matching versions)

---

## Step 1 — Resolve Active Engagement

Check context for active slug; if none, scan `EA-projects/*/engagement.json`. Read `engagement.json`. Extract: `name`, `slug`, `pluginVersion`, `lastMigratedVersion`, `schemaVersion` (treat as absent for pre-versioning engagements), `artifacts[]`, `direction`, `phases`, `engagementType`, `architectureDomains`.

---

## Step 2 — Determine Version Delta

Read current plugin version from `.claude-plugin/plugin.json`.

If `pluginVersion` equals current version AND `lastMigratedVersion` equals current version **AND `--force` was not passed**, run a fast **structural integrity probe** before short-circuiting (version stamps can match while the structure is still legacy — see 3a):

- `direction` is **concept-keyed** (not domain-keyed `Business`/`Data`/`Application`/`Technology`/`Motivation`)
- `metrics` is a **flat array** (not a domain-keyed object)
- top-level `finance`, `policies`, `adoptedRAs`, `localRA`, `constraintsRepoPath` and `direction.opportunities`/`direction.gaps` are present

If the probe finds **no** structural gaps:
> "✅ This engagement is fully aligned with ea-assistant v{current_version}. No migration needed." → stop.

If the probe finds structural gaps (or `--force` was passed), continue to Step 3 — the version match does not exempt structural drift.

---

## Step 3 — Scan for Gaps

Read `skills/ea-engagement-lifecycle/references/migration-gap-catalogue.md` for the full gap check definitions, severity levels, and remediation rules for all six areas:
- 3a — engagement.json schema gaps
- 3b — expected artifacts missing
- 3c — artifact frontmatter gaps (taxonomy, templateVersion)
- 3d — phase-organized artifact structure (**detection only** — file moves are handled by `/ea-migrate --reorganize`)
- 3e — rules file and CLAUDE.md format gaps
- 3f — artifact content gaps (Appendix A3/A4/A5)
- 3i — template body section & guidance gaps (sections/guidance the current template defines but the artifact is missing) — **insertion-only, per-section confirmation, excluded from `--auto`**; skips command-generated artifacts (registers/matrices/derived)
- 3j — section ordering gaps (existing sections out of template order) — **whole-section atomic reorder, per-artifact confirmation, snapshot first, excluded from `--auto`**
- 3k — misplaced content (heuristic) — surfaces content that likely belongs in another section or another artifact and proposes a **user-confirmed** move; register-bound content is offered as formal registration, not raw paste; **snapshot first, excluded from `--auto`**

Additionally, run this engagement-specific scan:

**3g — Missing detail files on high-priority items**

Scan all artifact files for:
- Risk Register: rows with `Rating: Critical` or `Rating: High`
- Requirements Register: rows with `Priority: High`
- Appendix A3 (Decision Log): rows with `Authority: Strategic`
- Appendix A4 (Concerns): rows with `Status: Requires Attention`

For each qualifying item, check whether `EA-projects/{slug}/artifacts/details/{ID}.md` exists. If not, report:

```
GAP-M-{NNN}  [Info]  {ID} ({type}, {priority/rating}) — no detail file
             Suggested: run /ea-detail new {ID} to capture narrative, rationale, and risks
```

**Remediation for 3g:** Report-only — never bulk-create detail files. Empty stubs add navigation noise without content (detail files are opt-in per `detail-file-convention.md`). For each item the user explicitly selects, run the `/ea-detail new {ID}` flow (which extracts the table row, title, and related IDs) and immediately prompt for at least a Summary. If the user declines to provide any content, do not create the file. 3g is always excluded from `--auto`.

**3h — Cross-cutting sub-folder structure**

Scan `EA-projects/{slug}/artifacts/cross-cutting/` (flat level only — not recursing into sub-folders) for `.md` files that should live in a sub-folder. Match by filename pattern:

| Pattern | Target sub-folder |
|---|---|
| `adr-*.md`, `adr-register*.md`, `decision-register*.md`, `constraints-register*.md`, `policies-register*.md` | `governance/` |
| `risk-register*.md`, `concerns-register*.md`, `change-register*.md`, `change-request-*.md` | `operations/` |
| `zachman-diagram-*.md`, `role-catalogue.md` | `context/` |

For each misplaced file found, report:

```
GAP-M-{NNN}  [Medium]  {filename} is in cross-cutting/ root — should be in cross-cutting/{sub-folder}/
             Suggested: run /ea-migrate --reorganize to move it
```

Also check `engagement.json → artifacts[]`: if any `file` path contains `artifacts/cross-cutting/{filename}` (flat, no sub-folder), flag as needing path update.

**Remediation for 3h:** Move the files to their target sub-folders (creating the sub-folder if needed) and update `engagement.json → artifacts[]` file paths to match. Handled by `/ea-migrate --reorganize`.

Track each gap found with: gap ID (GAP-M-NNN), type, affected file, severity, proposed remediation.

---

## Step 4 — Produce the Migration Report

```
════════════════════════════════════════════════════════════
MIGRATION REPORT — {engagement name}
Plugin: v{current} | Engagement last opened: v{pluginVersion} | Last migrated: v{lastMigratedVersion}
════════════════════════════════════════════════════════════

engagement.json schema gaps      {N gaps | ✅ None}
  GAP-M-001  [Low]    pluginVersion field absent
  GAP-M-002  [Low]    lastMigratedVersion field absent

Missing artifacts                {N gaps | ✅ None}
  GAP-M-010  [Medium] Engagement Charter not present (introduced v0.9.5)

Phase structure gaps             {N gaps | ✅ None}
  GAP-M-015  [Medium] {N} artifacts at flat paths — run /ea-migrate --reorganize to move them
  GAP-M-016  [Low]    architecture-vision.md — relatedArtifacts/diagrams/links fields absent

Artifact frontmatter gaps        {N gaps | ✅ None}
  GAP-M-020  [Medium] architecture-vision.md — taxonomy: block missing
  GAP-M-022  [Low]    requirements-register.md — templateVersion field missing

Rules file / CLAUDE.md gaps      {N gaps | ✅ None}
  GAP-M-024  [Low]    .claude/rules/ea-engagement.md missing
  GAP-M-025  [Medium] CLAUDE.md — old-format; regenerate as pointer doc

Artifact content gaps            {N gaps | ✅ None}
  GAP-M-030  [Medium] architecture-vision.md — Appendix A4 missing
  GAP-M-040  [Low]    architecture-vision.md — Appendix A5 missing

Template body gaps               {N gaps | ✅ None}
  GAP-M-045  [Low]    business-architecture.md — section "Related Matrices" missing (template adds it)
  GAP-M-046  [Info]   business-scenario-BS-001.md — §3 Environment has no guidance block
  (insertion-only · per-section confirm · excluded from --auto)

Section ordering gaps            {N gaps | ✅ None}
  GAP-M-047  [Low]    business-architecture.md — Organisation Model / Business Context out of template order
  (whole-section reorder · snapshot first · per-artifact confirm · excluded from --auto)

Misplaced content (heuristic)    {N gaps | ✅ None}
  GAP-M-048  [Info]   architecture-vision.md — Risk-titled table → suggest Risk Register (/ea-risks add)
  GAP-M-049  [Info]   architecture-vision.md — "Work Packages" section → suggest Architecture Roadmap
  (heuristic suggestions · user-confirmed move · snapshot first · excluded from --auto)

Missing detail files             {N gaps | ✅ None}
  GAP-M-050  [Info]   RIS-001 (Risk, Critical) — no detail file
  GAP-M-051  [Info]   G-002 (Goal, Strategic decision) — no detail file

════════════════════════════════════════════════════════════
Total: {N} gaps — {N} Medium, {N} Low, {N} Info
════════════════════════════════════════════════════════════
```

Stop here if `--report` was specified.

---

## Step 5 — Offer Remediation

```
How would you like to proceed?

  1. Fix all — apply all non-destructive remediations (I'll confirm each before writing)
  2. Fix by type — choose a gap category to fix
  3. Fix one — select a single gap by ID
  4. Skip — close without changes
```

**Never apply any change without the user selecting an option.** If `--auto` was specified, proceed as option 1 — but still announce each change before writing. **The 3a structural flattens (domain-keyed `direction` → concept-keyed; domain-keyed `metrics` object → flat array), 3g (detail files), 3i (body sections/guidance), 3j (section reorder), and 3k (misplaced content) are always excluded from `--auto`**. The 3a structural flattens relocate **populated** direction/metrics data, so they **snapshot `engagement.json` first** and run the uniqueness/unknown-key guard from the gap catalogue, aborting without writing if either check fails. — they require interactive per-item confirmation even under `--auto`, because they touch artifact bodies rather than metadata/structure. 3j and 3k relocate **populated** content and additionally **snapshot the affected artifact(s) before applying** (see the gap catalogue's "Snapshot Before Restructure"); a content-preservation check runs after every reorder/move, restoring from the snapshot if anything would be lost or duplicated.

---

## Step 6 — Apply Remediations

For each selected gap, present the proposed change before writing:

```
GAP-M-020 — architecture-vision.md — taxonomy: block missing
──────────────────────────────────────────────────────────────
Proposed addition to frontmatter (after templateVersion field):

  taxonomy:
    domain: Cross-cutting
    category: Strategy
    ...

Apply this change? (y / n / edit)
```

For `edit`: show the proposed YAML and allow modification before applying.

**Remediation content:** All gap-specific remediation rules are in `skills/ea-engagement-lifecycle/references/migration-gap-catalogue.md`. Appendix markdown blocks are in `skills/ea-artifact-templates/references/appendix-templates.md`.

---

## Step 7 — Finalise

After all remediations are applied or skipped:

1. Update `engagement.json`: set `pluginVersion` and `lastMigratedVersion` to current version; set `schemaVersion` to the current schema version (see `engagement-schema.md` — add the field if absent); update `lastModified`
2. Append a migration audit entry to `engagement.json → migrations[]` (create the array if absent):
   ```json
   { "date": "{ISO 8601}", "fromPluginVersion": "{old}", "toPluginVersion": "{current}", "fromSchemaVersion": {old or null}, "toSchemaVersion": {current}, "gapsFound": N, "gapsFixed": N, "gapsSkipped": N }
   ```
3. For each modified artifact: update `templateVersion` to current version and `lastModified` to now
4. Report applied / skipped / remaining counts; suggest re-running if gaps remain

---

## Flag: --reorganize [--report] [--auto]

Move flat-path artifacts in the active engagement into their correct phase subfolders and update all `engagement.json` file paths to match. This flag does one thing only — file moves. It does not patch frontmatter, add appendices, or touch `engagement.json` fields other than the `file` path of each moved artifact.

**This flag never moves a file without the user's explicit approval** (unless `--auto` is given).

Additional flags:
- `--report` — list what would be moved; make no changes
- `--auto` — apply all moves without per-file confirmation (still announces each move)

### Phase Folder Mapping

| `phase:` frontmatter value | Target folder |
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

### Reorganize Steps

1. **Resolve active engagement.** Check context for active slug; if none, scan `EA-projects/*/engagement.json` and ask. Read `engagement.json` and extract `name`, `slug`, and `artifacts[]`.

2. **Find flat-path artifacts.** Identify artifacts whose `file` path in `engagement.json` matches `artifacts/{artifact-id}.md` (no phase subfolder). For each: read the artifact file, extract the `phase:` frontmatter field, look up the target folder. If `phase:` does not match any row: mark as **unmappable**.

3. **Produce the reorganization plan:**
   ```
   ════════════════════════════════════════════════════════════
   REORGANIZE — {engagement name}
   ════════════════════════════════════════════════════════════

   Artifacts to move               {N | ✅ None — already organized}
     architecture-vision.md        artifacts/ → artifacts/phase-a/
     business-architecture.md      artifacts/ → artifacts/phase-b/

   Unmappable (phase: value not recognized)
     some-artifact.md              phase: "Unknown" — set correct phase: in frontmatter, then re-run
   ════════════════════════════════════════════════════════════
   ```
   Stop here if `--report` was specified or if there are no moveable artifacts.

4. **Confirm and move.** If `--auto` is not set, ask per artifact:
   ```
   Move artifacts/architecture-vision.md → artifacts/phase-a/architecture-vision.md ? (y / n / all / quit)
   ```
   - `y` — move this file
   - `n` — skip this file
   - `all` — move all remaining without further prompts
   - `quit` — stop without making any further changes

   For each approved move:
   - Create the target phase subfolder if it does not exist
   - Move the file: `mv EA-projects/{slug}/artifacts/{artifact-id}.md EA-projects/{slug}/artifacts/{phase-folder}/{artifact-id}.md`
   - Update the `file` field in `engagement.json → artifacts[]` for this artifact to the new path

5. **Move cross-cutting sub-folder artifacts.** After phase-folder moves, scan for GAP-M-3h items (flat cross-cutting files). For each:
   - Present the move: `"Move artifacts/cross-cutting/{file} → artifacts/cross-cutting/{sub-folder}/{file}? (y/n/all/quit)"`
   - On confirm: create sub-folder if needed, move the file, update `engagement.json → artifacts[]` path.

6. **Seed cross-cutting-index.md** if it does not exist. If `artifacts/cross-cutting/cross-cutting-index.md` is missing, create it from `templates/cross-cutting/cross-cutting-index.md` with `engagement_name` substituted. Register in `engagement.json → artifacts[]`.

7. **Finalise.** Update `engagement.json` `lastModified` to now. Print a summary:
   ```
   Moved to phase folders:        {N} artifacts
   Moved to cross-cutting subs:   {N} artifacts
   Skipped:                       {N} artifacts
   Unmappable:                    {N} artifacts (set phase: frontmatter and re-run)
   ```
