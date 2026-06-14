---
name: ea-engage-review
description: Comprehensive review, alignment check, and synchronization of an entire EA engagement — cross-artifact consistency, motivation chain traceability, open decisions/risks/concerns, and grill-me on key artifacts
argument-hint: "[--quick] [--grill <artifact-name>] [--sync]"
allowed-tools: [Read, Write, Glob, Grep, Bash]
---

You are executing the `/ea-engage-review` command. Load the `ea-engagement-lifecycle` skill and the `ea-artifact-templates` skill for context.

## Overview

This command performs a full-scope review of the active engagement across four dimensions:

| Dimension | What it checks | Agent / Command |
|---|---|---|
| **Consistency** | Cross-artifact contradictions, naming gaps, traceability holes | `ea-consistency-checker` |
| **Alignment** | Motivation chain coverage (DRV → G → OBJ → STR → WP), completeness per phase | Read + analysis |
| **Governance** | Open decisions, unresolved concerns, open/critical risks | Inline scan of A3/A4/risk tables |
| **Quality** | Artifact completeness %, review status, compliance state | Inline scan |

The Consistency dimension is owned by `/ea-consistency` — this command composes it; consistency logic is never restated here. `--quick` skips the consistency dimension and shows only the governance and quality summaries; the report must then mark Consistency as `⏭ Skipped (--quick) — run /ea-consistency for the focused check` rather than omitting it silently.

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, phases, artifacts, direction, metrics.

---

## Step 2 — Artifact Inventory

Read all `.md` files in `EA-projects/{slug}/artifacts/` (exclude `*.review.md`, `decision-register*.md`, `risk-register*.md`, `concerns-register*.md`, `adr-register*.md`, `change-register*.md`). For each:
- Extract frontmatter: artifact name, phase, status, reviewStatus, version
- Count `{{placeholder}}` tokens (unanswered fields)
- Check for T3 appendix sections: Appendix A3 (Decision Log), Appendix A4 (Concerns)

Build an inventory table for the report.

---

## Step 3 — Consistency Check (skip with `--quick`)

Run the `/ea-consistency` full-mode flow (which loads Scope C context and invokes the `ea-consistency-checker` agent — see `commands/ea-consistency.md`; do not restate its logic). Capture the output. Summarise: Critical Issues (count), Warnings (count), Traceability gaps (count).

---

## Step 4 — Alignment Check

Verify the motivation chain from `engagement.json → direction` through to the artifact content:

**4a — Driver → Goal coverage:**
For each `DRV-NNN` in `direction`, check that at least one `G-NNN` in the Architecture Vision cites it as a linked driver. Flag drivers with no linked goal.

**4b — Goal → Objective coverage:**
For each `G-NNN` in `direction`, check that at least one `OBJ-NNN` specifies a measure and links back to that goal. Flag goals with no linked objective.

**4c — Goal/Objective → Strategy coverage:**
For each `G-NNN` / `OBJ-NNN`, check that at least one `STR-NNN` supports it. Flag goals/objectives with no executing strategy.

**4d — Strategy → Work Package coverage (Phase E/F):**
If the Architecture Roadmap exists, check each `STR-NNN` and `G-NNN` is referenced in at least one `WP-NNN` entry. Flag goals/strategies not covered by any work package.

**4e — Metric → Objective linkage:**
For each `MET-NNN` in `engagement.json → metrics`, verify it links to a `G-NNN` or `OBJ-NNN` — except `benefit`-type metrics, which link to a `FIN-NNN` Cost Entry. Flag metrics with no linked direction or cost item.

**4f — ABB coverage (Phase C/D):**
Scan `phase-c*/**/*.md` and `phase-d*/**/*.md` for `ABB-\d{3}` tokens. For each ABB-NNN:
- Check that it is implemented by at least one `SBB-NNN` (scan same files for `SBB-\d{3}` in the ABB's `Implemented by` column)
- Check that it satisfies at least one `REQ-NNN` (scan `Satisfies` column)
Flag orphan ABBs (no REQ, no SBB).

**4g — SBB coverage (Phase D):**
Scan `phase-d*/**/*.md` for `SBB-\d{3}` tokens. For each SBB-NNN:
- Check that it implements at least one `ABB-NNN` (scan `Implements` column)
Flag vendor-first SBBs (no ABB) as anti-pattern.

**4h — Story coverage (Phase E):**
Scan `requirements/*.md` and `phase-e*/**/*.md` for `STY-\d{3}` tokens. For each STY-NNN:
- Check that it links to at least one `REQ-NNN` (scan `Satisfies` field)
- Check that it implements at least one `SBB-NNN` (scan `Implements` field)
Flag orphan stories (no REQ, no SBB).

**4i — Gap coverage:**
Scan `engagement.json → direction.gaps[]`. Count entries where `severity` is `Critical` or `High`, `status` is `Open`, and `linkedWorkPackages` is empty or `[]`. If count ≥ 1, add to the Alignment summary: `⚠️ {N} Critical/High gap(s) open with no linked Work Packages — run /ea-gaps trace`. If no `direction.gaps[]` array exists, skip silently.

Summarise as: Fully aligned / Partially aligned / Gaps detected.

---

## Step 5 — Governance Scan

**5a — Open Decisions:** Scan all A3 appendices. Count rows where State = `🔄 Provisional` or `⏳ Awaiting Verification`. List by artifact. Flag A3 rows with no ADR-NNN reference where 2+ ADR threshold indicators apply (see `ea-adrs.md` threshold criteria) — these may warrant an ADR.

**5b — Unresolved Concerns:** Scan all A4 appendices. Count rows where Status = `Requires Attention`. List top 3 by artifact. Flag any Category = Risk items with no matching RIS-NNN.

**5c — Open Risks:** Scan `risk-register*.md` if present, else scan all A3/A4 rows for risk references. Count Critical + High risks with Status = Open.

**5d — ADR Status:** Scan all `adr-*.md` files in `EA-projects/{slug}/artifacts/`. Count by status. Flag any Candidate ADRs older than 14 days (stale — no options analysis started). Flag any In Progress ADRs older than 30 days (overdue for decision).

---

## Step 6 — Quality Scan

For each artifact, compute:
- `% Complete` = (total fields − unanswered fields) / total fields × 100
- `Review health` = reviewStatus value

Classify:
- ✅ Healthy: ≥ 80% complete AND reviewStatus ≠ Not Reviewed
- ⚠️ Needs attention: 50–79% complete OR still Not Reviewed
- 🔴 Incomplete: < 50% complete

---

## Step 7 — Produce the Engagement Review Report

Output the report in this format:

```
════════════════════════════════════════════════════════════════
ENGAGEMENT REVIEW — {engagement name}
Generated: {YYYY-MM-DD}  |  Phase: {currentPhase}  |  Artifacts: {N}
════════════════════════════════════════════════════════════════

## Consistency          {✅ No issues | ⚠️ N warnings | 🔴 N critical | ⏭ Skipped (--quick) — run /ea-consistency}
  {top 2 critical issues, if any — one line each}

## Alignment            {✅ Fully aligned | ⚠️ Partial | 🔴 Gaps detected}
  {list unlinked items — e.g. "DRV-002 has no Goal", "G-003 has no Work Package"}

## Building Blocks      {✅ Complete | ⚠️ Partial | 🔴 Gaps detected}
  {N} ABBs, {N} SBBs, {N} Stories
  {list orphans — e.g. "ABB-001 has no SBB", "SBB-002 has no ABB", "STY-003 has no REQ"}

## Governance
  Open decisions:         {N} ({artifact list})
  Concerns requiring attention: {N} ({top 3})
  Open critical/high risks:     {N}
  ADRs open (Candidate):  {N}{; stale: {N} if any older than 14 days}
  ADRs in progress:       {N}{; overdue: {N} if any older than 30 days}
  A3 rows needing ADR:    {N} decisions may warrant an ADR (threshold indicators matched)

## Artifact Quality
  {artifact name}   {% complete}   {reviewStatus}   {✅/⚠️/🔴}
  {artifact name}   ...

════════════════════════════════════════════════════════════════
OVERALL: {✅ Ready for review | ⚠️ Needs attention | 🔴 Significant gaps}
════════════════════════════════════════════════════════════════
```

---

## Step 8 — Next Actions Menu

After the report, present:

```
What would you like to do?

Review options:
  1. Deep-review an artifact (grill-me)           — select an artifact to grill
  2. Review all phase {currentPhase} artifacts     — grill each artifact in current phase
  3. View open decisions                           — /ea-decisions
  4. View concerns requiring attention             — /ea-concerns --status attention
  5. View open risks                               — /ea-risks --status open

Fix options:
  6. Fix alignment gaps                            — open affected artifacts for editing
  7. Generate Decision Register                    — /ea-decisions generate
  8. Generate Risk Register                        — /ea-risks generate
  9. Generate Concerns Register                    — /ea-concerns generate
 11. Generate ADR Register                         — /ea-adrs generate
 12. Create a new ADR                              — /ea-adrs new
 13. Review unaddressed gaps                       — /ea-gaps trace

Synchronize:
 10. Sync engagement                               — refresh CLAUDE.md, update lastModified, validate all frontmatter

  Enter a number or press Enter to close.
```

### Option 1 — Deep-review an artifact

List all artifacts in the engagement numbered. After the user selects one, invoke `/ea-grill {artifact-name}` with the recommended skill for that artifact type (see ea-grill.md skill mapping table).

### Option 2 — Review all phase artifacts

For each artifact in the current phase (from `engagement.json → phases → {currentPhase} → artifacts`):
1. Announce: "Grilling {artifact name} using {skill}..."
2. Run `/ea-grill {artifact-name}` with the recommended skill.
3. After each grill, offer: "Populate A4 concerns? (y/n) — then continue to next artifact."
After all artifacts in the phase: "Phase review complete. {N} artifacts grilled, {N} concerns added to A4 appendices."

### Option 6 — Fix alignment gaps

For each flagged alignment gap:
```
Gap: {DRV-002 has no linked Goal}
Options:
  a) Add a Goal linked to DRV-002 — run `/ea-goals add` (writes engagement.json; refresh the Goals Register with `/ea-goals generate`)
  b) Mark as intentional — note in A4: "DRV-002 excluded from scope"
  c) Skip this gap
```

### Option 10 — Sync engagement

1. Re-read `engagement.json`.
2. Refresh `EA-projects/{slug}/CLAUDE.md` using the seed template at `templates/seeds/engagement-claude-md.md` — populate stable identity fields (organisation, slug, type, sponsor, started date), engagement context (vision, mission, scope), and static pointer tables only. Do **not** include current phase, status, artifact counts, or any other transitory state — these belong in `/ea-open` output, not CLAUDE.md.
3. Update `engagement.json → lastModified` to now.
4. Run Tier 1 compliance check on all artifacts — report any T1 failures.
5. Confirm: "Sync complete — CLAUDE.md refreshed, {N} T1 failures noted (run /ea-review to fix)."

---

## Handling `--grill <artifact-name>`

When invoked as `/ea-engage-review --grill architecture-vision`:
- Skip Steps 2–7.
- Go directly to Option 1 behaviour for the named artifact.

## Handling `--sync`

When invoked as `/ea-engage-review --sync`:
- Skip Steps 2–7.
- Execute Option 10 (Sync engagement) directly and confirm.
