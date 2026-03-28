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

Flags from `--quick` skip the detailed consistency check and show only the governance and quality summaries.

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, phases, artifacts, direction, metrics.

---

## Step 2 — Artifact Inventory

Read all `.md` files in `EA-projects/{slug}/artifacts/` (exclude `*.review.md`, `decision-register-*.md`, `risk-register-*.md`, `concerns-register-*.md`). For each:
- Extract frontmatter: artifact name, phase, status, reviewStatus, version
- Count `{{placeholder}}` tokens (unanswered fields)
- Check for T3 appendix sections: Appendix A3 (Decision Log), Appendix A4 (Concerns)

Build an inventory table for the report.

---

## Step 3 — Consistency Check (skip with `--quick`)

Invoke the `ea-consistency-checker` agent to cross-check all artifacts. Capture the output. Summarise: Critical Issues (count), Warnings (count), Traceability gaps (count).

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
For each `MET-NNN` in `engagement.json → metrics`, verify it links to a `G-NNN` or `OBJ-NNN`. Flag metrics with no linked direction item.

Summarise as: Fully aligned / Partially aligned / Gaps detected.

---

## Step 5 — Governance Scan

**5a — Open Decisions:** Scan all A3 appendices. Count rows where State = `🔄 Provisional` or `⏳ Awaiting Verification`. List by artifact.

**5b — Unresolved Concerns:** Scan all A4 appendices. Count rows where Status = `Requires Attention`. List top 3 by artifact. Flag any Category = Risk items with no matching RIS-NNN.

**5c — Open Risks:** Scan `risk-register-*.md` if present, else scan all A3/A4 rows for risk references. Count Critical + High risks with Status = Open.

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

## Consistency          {✅ No issues | ⚠️ N warnings | 🔴 N critical}
  {top 2 critical issues, if any — one line each}

## Alignment            {✅ Fully aligned | ⚠️ Partial | 🔴 Gaps detected}
  {list unlinked items — e.g. "DRV-002 has no Goal", "G-003 has no Work Package"}

## Governance
  Open decisions:         {N} ({artifact list})
  Concerns requiring attention: {N} ({top 3})
  Open critical/high risks:     {N}

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
  a) Add a Goal linked to DRV-002 — open Architecture Vision §3 for editing
  b) Mark as intentional — note in A4: "DRV-002 excluded from scope"
  c) Skip this gap
```

### Option 10 — Sync engagement

1. Re-read `engagement.json`.
2. Refresh `EA-projects/{slug}/CLAUDE.md` using the full template from `/ea-open` step 7 — this updates: Engagement Identity, Strategic Intent, Artifact Status, Phase Progress, Open Decisions.
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
