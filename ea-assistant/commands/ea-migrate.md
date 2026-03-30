---
name: ea-migrate
description: Detect and resolve alignment gaps between an EA engagement and the current ea-assistant version — missing taxonomy, appendices, new artifacts, and engagement.json schema fields. Always asks permission before making any change.
argument-hint: "[--report] [--auto]"
allowed-tools: [Read, Write, Glob, Bash]
---

You are executing the `/ea-migrate` command. Load the `ea-engagement-lifecycle` skill and the `ea-artifact-templates` skill for context.

## Overview

`/ea-migrate` scans the active engagement for alignment gaps between its artifacts and the current ea-assistant template standard, then offers targeted remediation with **explicit per-item confirmation before any change is made**.

**This command never modifies files without the user's explicit approval.**

Flags:
- `--report` — scan and report only; do not offer remediation
- `--auto` — apply all non-destructive remediations without confirmation (use with caution)

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Read `engagement.json`. Extract: `name`, `slug`, `pluginVersion`, `lastMigratedVersion`, `artifacts[]`, `direction`, `phases`, `engagementType`, `architectureDomains`.

---

## Step 2 — Determine Version Delta

Read the current plugin version from the ea-assistant `.claude-plugin/plugin.json` file.

```
Current plugin version : {current_version}
Engagement pluginVersion : {engagement_pluginVersion or "not set — pre-0.9.5"}
Last migrated version  : {lastMigratedVersion or "never migrated"}
```

Compute the delta: list which version bands are unprocessed (see Gap Catalogue below).

If `pluginVersion` equals the current version AND `lastMigratedVersion` equals the current version:
> "✅ This engagement is fully aligned with ea-assistant v{current_version}. No migration needed."
Stop.

---

## Step 3 — Scan for Gaps

Scan systematically across four areas. Track every gap found with: a gap ID (GAP-M-NNN), gap type, affected file, severity, and proposed remediation.

### 3a — engagement.json schema gaps

| Check | Gap if… | Severity |
|---|---|---|
| `pluginVersion` field present | Field absent | Low |
| `lastMigratedVersion` field present | Field absent | Low |
| `direction` field present | Absent (pre-0.4.0) | Medium |
| `metrics` field present | Absent (pre-0.5.0) | Low |
| `engagementType` field present | Absent (pre-0.2.0) | Low |
| `architectureDomains` field present | Absent (pre-0.2.0) | Low |
| `optOuts` field present | Absent (pre-0.8.0) | Low |

### 3b — Expected artifacts missing

Check `engagement.json → artifacts[]` and the `EA-projects/{slug}/artifacts/` directory for expected artifacts that are absent:

| Artifact | Introduced in | Severity if absent |
|---|---|---|
| Engagement Charter (`engagement-charter`) | 0.9.5 | Medium — Preliminary deliverable missing |
| Governance Framework (`governance-framework`) | 0.9.4 | Low — governance artifact missing |

For each absent artifact, flag as a gap but do not auto-create — creating artifacts requires user input.

### 3c — Artifact frontmatter gaps

For each artifact file in `EA-projects/{slug}/artifacts/` (excluding `*.review.md`, registers, and session logs):

Read the frontmatter. Check for:

| Check | Gap if… | Introduced in | Severity |
|---|---|---|---|
| `taxonomy:` block present with all 5 sub-fields | Block absent or incomplete | 0.9.4 | Medium |
| `templateVersion:` field present | Field absent | 0.9.5 | Low |
| `complianceNote` not set to `accepted-non-standard` on a standard artifact | Flag for review, not a migration gap | — | Info |

For taxonomy gaps: look up the canonical taxonomy for this artifact type from `skills/ea-artifact-templates/references/taxonomy.md`. If the artifact type is not in the canonical map, flag for manual assignment.

### 3d — CLAUDE.md format gap

Check `EA-projects/{slug}/CLAUDE.md`:

| Check | Gap if… | Introduced in | Severity |
|---|---|---|---|
| File contains `## Where to Find Content` section | Section absent — file is old-format (fat CLAUDE.md with full goal/objective/strategy tables) | 0.9.12 | Medium |

If the gap is present, the remediation is to regenerate CLAUDE.md using the current pointer-format template (from `/ea-new`). The full strategic data is not lost — it remains in `engagement.json → direction` and artifact files.

### 3e — Artifact content gaps

For each artifact, check for missing structural elements added in recent versions:

| Check | Artifact Types | Gap if… | Introduced in | Severity |
|---|---|---|---|---|
| `## Appendix A3 — Decision Log` section present | Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Roadmap, SAoW, Migration Plan | Section absent | 0.7.0 | Medium |
| `## Appendix A4 — Stakeholder Concerns & Objections` section present | Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Roadmap, SAoW, Migration Plan, Engagement Charter, Governance Framework, Implementation Governance Plan | Section absent | 0.9.3 | Medium |
| `## Appendix A5 — Related Architecture Decisions` section present | Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Architecture Roadmap, SAoW, Migration Plan, Compliance Assessment, Requirements Register, Engagement Charter, Governance Framework, Implementation Governance Plan | Section absent | 0.9.7 | Low |

---

## Step 4 — Produce the Migration Report

Present the full gap report before offering any remediation:

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

Artifact frontmatter gaps        {N gaps | ✅ None}
  GAP-M-020  [Medium] architecture-vision.md — taxonomy: block missing
  GAP-M-021  [Medium] business-architecture.md — taxonomy: block missing
  GAP-M-022  [Low]    requirements-register.md — templateVersion field missing

CLAUDE.md format gap             {N gaps | ✅ None}
  GAP-M-025  [Medium] CLAUDE.md — old-format (Strategic Intent tables present); regenerate as pointer doc

Artifact content gaps            {N gaps | ✅ None}
  GAP-M-030  [Medium] architecture-vision.md — Appendix A4 missing
  GAP-M-031  [Medium] business-architecture.md — Appendix A4 missing
  GAP-M-040  [Low]    architecture-vision.md — Appendix A5 — Related Architecture Decisions section missing
  GAP-M-041  [Low]    business-architecture.md — Appendix A5 — Related Architecture Decisions section missing

════════════════════════════════════════════════════════════
Total: {N} gaps — {N} Medium, {N} Low, {N} Info
════════════════════════════════════════════════════════════
```

If `--report` was specified, stop here.

---

## Step 5 — Offer Remediation

After the report, present:

```
How would you like to proceed?

  1. Fix all — apply all non-destructive remediations (I'll confirm each before writing)
  2. Fix by type — choose a gap category to fix (schema / missing artifacts / frontmatter / content)
  3. Fix one — select a single gap by ID to fix
  4. Skip — close without changes

  Enter a number, a gap ID (e.g. GAP-M-020), or press Enter to close.
```

**Never apply any change without the user selecting an option.**

If `--auto` was specified, skip this menu and proceed as if option 1 was selected — but still announce each change before writing.

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
    audience: Executive
    layer: Motivation
    sensitivity: Internal
    tags: [vision, drivers, goals, strategy, phase-a]

Apply this change? (y / n / edit)
```

For `edit` responses: show the proposed YAML and allow the user to modify values before applying.

### Remediation rules per gap type

**engagement.json schema gaps:**
- `pluginVersion` absent → add `"pluginVersion": "{current_version}"`
- `lastMigratedVersion` absent → add `"lastMigratedVersion": "0.0.0"` (will be set to current at migration completion)
- `direction` absent → add empty `direction` object with keys matching `architectureDomains`
- `metrics` absent → add empty `metrics` object with keys matching `architectureDomains`
- `engagementType` absent → add `"engagementType": null` (user can set via `/ea-open` → Edit Metadata)
- `architectureDomains` absent → add `"architectureDomains": ["Business","Data","Application","Technology"]`
- `optOuts` absent → add `"optOuts": []`

**Missing artifact gaps:**
- Do NOT auto-create artifacts — they require interview input
- Instead: report the gap and offer: "Would you like to create this artifact now? (`/ea-artifact create {artifact-id}`)"

**Artifact frontmatter gaps — taxonomy block:**
1. Look up the artifact's type from its `artifact:` frontmatter field
2. Find the canonical taxonomy from `skills/ea-artifact-templates/references/taxonomy.md`
3. If found: present the canonical values for confirmation, then inject the `taxonomy:` block after the `templateVersion:` field (or after `version:` if `templateVersion` is also absent)
4. If not found (non-standard artifact): present a blank taxonomy block and ask the user to fill in the values

**Artifact frontmatter gaps — templateVersion:**
- Inject `templateVersion: 0.0.0` to signal "pre-versioning origin"
- The user can update this to the actual version if known

**Artifact content gaps — Appendix A3:**
Append before the closing footer (or before Appendix A4 if that section exists):
```markdown
## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>
Record governance decisions made during the development of this artifact. Use `/ea-decisions` to generate a cross-artifact Decision Register.
</details>

| ID | Decision | State | Authority | Domain | Cost | Impact | Risk | Subject | Captured By | Owner | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |
```

**Artifact content gaps — Appendix A5:**
Append before Appendix A3 (or before the footer if neither appendix is present):
```markdown
## Appendix A5 — Related Architecture Decisions

| ADR ID | Title | Status | Summary |
|---|---|---|---|
| *(no related ADRs recorded)* | — | — | — |
```

**Artifact content gaps — Appendix A4:**
Append after Appendix A3 (or before the footer if A3 is absent):
```markdown
## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>
Record all stakeholder concerns, objections, and tough questions raised about this artifact. Use `/ea-concerns` to generate a cross-artifact Concerns Register.
</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |
```

---

## Step 7 — Finalise

After all selected remediations are applied (or skipped):

1. Update `engagement.json`:
   - Set `pluginVersion` to the current plugin version
   - Set `lastMigratedVersion` to the current plugin version
   - Update `lastModified` to now
2. For each artifact that was modified, update its `templateVersion` to the current plugin version and `lastModified` to now
3. Confirm:

```
Migration complete
──────────────────────────────────────────────────────────────
Applied  : {N} remediations
Skipped  : {N} gaps (deferred)
Remaining: {N} gaps still open

engagement.json updated — pluginVersion and lastMigratedVersion set to v{current}.

{if remaining gaps > 0}
Run /ea-migrate again to address remaining gaps.
{end}
```

---

## Handling Non-Standard Artifacts

If an artifact's `artifact:` field does not match any known template type:
- Flag it with `[Info]` severity — not a migration error
- Do not attempt to assign canonical taxonomy values
- Suggest: "This artifact does not match a known template type. Review manually or use `/ea-grill artifact` to assess its quality."

## Handling Approved Artifacts

If a gap remediation would modify an `Approved` artifact, warn before writing:
```
⚠️ {artifact name} is Approved. Applying this remediation will NOT change content sections — it only adds metadata (taxonomy/templateVersion) or appends empty appendix tables. The artifact's reviewStatus will remain Approved.
Proceed? (y/n)
```

Only structural metadata additions (frontmatter fields, empty appendix tables) are permitted on Approved artifacts. Content edits require the artifact to be reopened for revision.
