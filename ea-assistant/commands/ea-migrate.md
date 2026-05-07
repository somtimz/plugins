---
name: ea-migrate
description: Detect and resolve alignment gaps between an EA engagement and the current ea-assistant version — missing taxonomy, appendices, new artifacts, and engagement.json schema fields. Always asks permission before making any change.
argument-hint: "[--report] [--auto]"
allowed-tools: [Read, Write, Glob, Bash]
---

You are executing the `/ea-migrate` command. Load the `ea-engagement-lifecycle` skill and the `ea-artifact-templates` skill for context.

## Overview

Scans the active engagement for alignment gaps between its artifacts and the current ea-assistant template standard, then offers targeted remediation with **explicit per-item confirmation before any change**.

**This command never modifies files without the user's explicit approval.**

Flags:
- `--report` — scan and report only; do not offer remediation
- `--auto` — apply all non-destructive remediations without confirmation

---

## Step 1 — Resolve Active Engagement

Check context for active slug; if none, scan `EA-projects/*/engagement.json`. Read `engagement.json`. Extract: `name`, `slug`, `pluginVersion`, `lastMigratedVersion`, `artifacts[]`, `direction`, `phases`, `engagementType`, `architectureDomains`.

---

## Step 2 — Determine Version Delta

Read current plugin version from `.claude-plugin/plugin.json`.

If `pluginVersion` equals current version AND `lastMigratedVersion` equals current version:
> "✅ This engagement is fully aligned with ea-assistant v{current_version}. No migration needed." → stop.

---

## Step 3 — Scan for Gaps

Read `skills/ea-engagement-lifecycle/references/migration-gap-catalogue.md` for the full gap check definitions, severity levels, and remediation rules for all six areas:
- 3a — engagement.json schema gaps
- 3b — expected artifacts missing
- 3c — artifact frontmatter gaps (taxonomy, templateVersion)
- 3d — phase-organized artifact structure (**detection only** — file moves are handled by `/ea-reorganize`)
- 3e — rules file and CLAUDE.md format gaps
- 3f — artifact content gaps (Appendix A3/A4/A5)

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

**Remediation for 3g:** Create stub detail files (frontmatter + empty section headers only, no content) for selected items. Stubs use `templates/item-detail.md` with placeholders replaced from source table data. The user can then populate them at any time with `/ea-detail view {ID}`.

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
  GAP-M-015  [Medium] {N} artifacts at flat paths — run /ea-reorganize to move them
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

**Never apply any change without the user selecting an option.** If `--auto` was specified, proceed as option 1 — but still announce each change before writing.

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

1. Update `engagement.json`: set `pluginVersion` and `lastMigratedVersion` to current version; update `lastModified`
2. For each modified artifact: update `templateVersion` to current version and `lastModified` to now
3. Report applied / skipped / remaining counts; suggest re-running if gaps remain
