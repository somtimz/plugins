---
name: ea-gaps
description: Manage architecture gaps — list, add, promote from raw gap text, update, trace to work packages, and generate a gap register
argument-hint: "[list|add|promote|update|trace|generate] [GAP-NNN] [--domain Business|Data|Application|Technology|Capability|Process] [--severity Critical|High|Medium|Low] [--status Open|Mitigated|Closed|Accepted] [--phase A|B|C|D|E|F|G|H]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-gaps` command. Load the `ea-gaps-management` skill for detailed logic.

## Overview

Architecture gaps represent the difference between the as-is (baseline) state and the to-be (target) state in a given architecture domain. Gaps are identified in Phase B–D artifacts, consolidated in Gap Analysis (Phase E), and addressed by Work Packages in the Architecture Roadmap. This command manages formally promoted `GAP-NNN` entries.

This command complements `/ea-trace --gaps`, which aggregates raw gap prose from artifact text. Use `/ea-trace --gaps` to discover gap statements in artifacts, then `/ea-gaps promote` to formalise the most important ones with structured metadata.

**Modes:**
- `list` (default) — read `engagement.json → direction.gaps[]`, render a table grouped by Severity
- `add` — interactively capture a new gap and write it to `engagement.json`
- `promote` — formalise a raw gap statement (from `/ea-trace --gaps` output or user input) as a GAP-NNN entry
- `update` — update a single field on an existing gap (`/ea-gaps update GAP-NNN <field> <value>`)
- `trace` — show upstream artifact linkage and downstream work package coverage for each gap
- `generate` — produce a printable Gap Register artifact

**Filters:**
- `--domain` — filter by architecture domain
- `--severity` — filter by severity
- `--status` — filter by status
- `--phase` — filter by ADM phase where identified

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, artifacts, direction.gaps[].

---

## Mode: `list` (default)

1. Read `engagement.json → direction.gaps[]`.
2. Render a summary table grouped by Severity (Critical first, then High, Medium, Low):

```
Gap Register — {engagement name}
══════════════════════════════════════════
Total: {N}  |  Critical: {N}  |  High: {N}  |  Medium: {N}  |  Low: {N}
Open: {N}  |  Mitigated: {N}  |  Closed: {N}  |  Accepted: {N}

By Domain:   Business {N}  |  Data {N}  |  Application {N}  |  Technology {N}  |  Capability {N}  |  Process {N}

| ID | Statement (truncated) | Domain | Severity | Phase | Linked WPs | Status |
|---|---|---|---|---|---|---|
| GAP-001 | ... | Business | Critical | B | — | Open |
...

Unaddressed: {N} Critical/High gap(s) with no linked Work Packages
```

3. Flag Critical/High gaps with `status = Open` and empty `linkedWorkPackages`: "⚠️ {N} unaddressed Critical/High gap(s) — no linked Work Packages. Run `/ea-gaps trace` to review."

---

## Mode: `add`

Invoked as: `/ea-gaps add`

1. Determine the ID series to use: if the user's active phase is F or G, use GAP-M-NNN (migration gaps); otherwise use GAP-NNN. Read `direction.gaps[]` and increment the highest existing N in the relevant series.
2. Prompt for each field in sequence:

```
Creating new gap — GAP-{NNN}  (or GAP-M-{NNN} for Phase F/G)

1. Statement (the gap — what is missing between baseline and target):
2. Domain (Business / Data / Application / Technology / Capability / Process):
3. Severity (Critical / High / Medium / Low):
4. Baseline (current/as-is state description):
5. Target (desired/to-be state description):
6. Phase (which ADM phase this gap was identified in):
   Prelim / A / B / C-Data / C-App / D / E / F / G / H / Requirements
7. Linked Work Packages (WP-NNN IDs, comma-separated, or press Enter) [optional]:
8. Linked Artifact (artifact ID where the gap appears, or press Enter) [optional]:
```

3. Show confirmation preview:

```
New gap — GAP-NNN
Statement: {statement}
Domain: {domain}  |  Severity: {severity}  |  Phase: {phase}
Baseline: {baseline}
Target: {target}
Linked WPs: {linkedWorkPackages or "—"}  |  Linked Artifact: {linkedArtifact or "—"}

Add to engagement? (y/n)
```

4. On confirm: append to `engagement.json → direction.gaps[]` with `status: Open`. Update `lastModified`.
5. If severity is Critical and no linked WPs: warn "⚠️ This is a Critical gap with no linked Work Package. Add a WP with `/ea-gaps update GAP-NNN linkedWorkPackages WP-NNN` or accept the gap deliberately."
6. Confirm: "GAP-NNN added. Use `/ea-gaps trace GAP-NNN` to check work package linkage."

---

## Mode: `promote`

Invoked as: `/ea-gaps promote`

Promotes a raw gap statement into a formal GAP-NNN entry. Useful after running `/ea-trace --gaps` which surfaces raw gap text from artifact prose.

1. Ask: "Paste the raw gap statement to promote (or describe the gap):"
2. If the user pastes multiple gaps, ask: "I see {N} gap statements. Promote them one at a time? (y/n)" — if yes, loop through each.
3. For each gap, pre-fill the `Statement` field from the pasted text and prompt for remaining fields (same sequence as `add`, with Statement pre-filled).
4. Assign next GAP-NNN or GAP-M-NNN and write to `engagement.json → direction.gaps[]`.
5. Confirm: "GAP-NNN promoted from raw gap text. Run `/ea-gaps trace GAP-NNN` to link it to a Work Package."

---

## Mode: `update`

Invoked as: `/ea-gaps update GAP-NNN <field> <value>`

1. Locate the `GAP-NNN` entry in `engagement.json → direction.gaps[]`.
2. Valid fields for update:

| Field | Valid values |
|---|---|
| `statement` | any string |
| `domain` | Business / Data / Application / Technology / Capability / Process |
| `severity` | Critical / High / Medium / Low |
| `baseline` | any string |
| `target` | any string |
| `phase` | Prelim / A / B / C-Data / C-App / D / E / F / G / H / Requirements |
| `status` | Open / Mitigated / Closed / Accepted |
| `linkedWorkPackages` | comma-separated WP-NNN list (replaces current list) |
| `linkedArtifact` | artifact ID string |

3. Validation rules:
   - Setting `status` to `Accepted` for a Critical gap → warn: "Accepting a Critical gap without a linked Work Package means this gap is acknowledged but will not be addressed. Confirm? (y/n)"
   - Setting `status` to `Closed` → confirm that the WP(s) have been delivered; note: "Mark as Closed only when the work package(s) addressing this gap have been implemented."
   - Removing all `linkedWorkPackages` on a Mitigated gap → warn: "Removing all Work Packages will revert status to Open. Continue? (y/n)" — if yes, also set `status: Open`.
4. Show proposed change: `"GAP-NNN: {field} — '{old}' → '{new}'"`
5. Ask: `"Apply? (y/n)"`
6. On confirm: update `engagement.json`, set `lastModified: today`.
7. Confirm: `"Updated GAP-NNN: {field} set to '{new_value}'."`

---

## Mode: `trace`

Invoked as: `/ea-gaps trace [GAP-NNN]`

**Without GAP-NNN (all gaps):**
1. Read all `direction.gaps[]` entries.
2. Output a traceability matrix:

```
| ID | Statement | Domain | Severity | Phase | Linked WPs | Status | Unaddressed? |
|---|---|---|---|---|---|---|---|
```

3. Flag gaps with Severity = Critical or High, Status = Open, and no linked WPs with "⚠️ Unaddressed."

**With GAP-NNN (single gap):**
1. Load the gap entry.
2. Upstream:
   - `linkedArtifact`: name and phase of the source artifact
   - Which ADM phase the gap was identified in
   - Scan `direction` for any REQ-NNN that may have generated awareness of this gap (free-text match on statement)
3. Downstream:
   - List `linkedWorkPackages` (WP-NNN IDs)
   - For each WP-NNN, scan the Architecture Roadmap artifact for wave, priority, and delivery status
   - Flag WP-NNN IDs that appear in `linkedWorkPackages` but cannot be found in the Architecture Roadmap as "⚠️ WP not found in Architecture Roadmap"
4. Output:

```
Gap Trace — GAP-NNN
Statement: {statement}
Domain: {domain}  |  Severity: {severity}  |  Status: {status}

Upstream:
  Source Artifact: {linkedArtifact or "—"}
  Identified in Phase: {phase}

Downstream:
  WP-001  {wave}  {description}
  WP-002  {wave}  {description}
  {N linked WPs}

{⚠️ Unaddressed critical gap — no linked Work Packages | ✅ Covered by {N} Work Package(s)}
```

---

## Mode: `generate`

Invoked as: `/ea-gaps generate`

1. Read all `direction.gaps[]` entries. Separate into: GAP-NNN (architecture gaps) and GAP-M-NNN (migration gaps).
2. Write `EA-projects/{slug}/artifacts/cross-cutting/gap-register-{YYYY-MM-DD}.md`:

```markdown
---
artifact: Gap Register
artifactId: gap-register
engagement: {name}
phase: All
status: Draft
generated: {YYYY-MM-DD}
---

# Gap Register — {engagement name}

**Generated:** {YYYY-MM-DD}  |  **Total Gaps:** {N}  |  **Unaddressed:** {N}

---

## Architecture Gaps (GAP-NNN)

### GAP-NNN: {first 60 chars of statement}

| Field | Value |
|---|---|
| **ID** | GAP-NNN |
| **Statement** | {statement} |
| **Domain** | {domain} |
| **Severity** | {severity} |
| **Baseline** | {baseline} |
| **Target** | {target} |
| **Phase Identified** | {phase} |
| **Linked Work Packages** | {linkedWorkPackages or "—"} |
| **Linked Artifact** | {linkedArtifact or "—"} |
| **Status** | {status} |

---

## Migration Gaps (GAP-M-NNN)

{Same H3 structure per GAP-M-NNN, or "No migration gaps recorded." if empty}

---

## Summary

| Domain | Critical | High | Medium | Low | Total |
|---|---|---|---|---|---|
| Business | {N} | {N} | {N} | {N} | {N} |
...

> Raw gap statements in artifact prose can be promoted to formal GAP-NNN entries using `/ea-gaps promote`.
```

3. Confirm: "Gap Register written to `artifacts/cross-cutting/gap-register-{date}.md`. {N} architecture gaps, {N} migration gaps."

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No gaps found | "No gaps found. Use `/ea-gaps add` to capture gaps, or `/ea-trace --gaps` to view raw gap statements in artifact prose." |
| Phase F/G — migration gap | Assign GAP-M-NNN automatically based on active phase |
| Critical/High gap with no linked WP | Flag in `list` and `trace`; prompt to add WP or accept |
| Duplicate GAP-NNN | Keep both; note: "Duplicate ID — re-numbering applied: GAP-NNN (from {artifact})" |
| GAP-NNN not found for update/trace | "GAP-NNN not found in `direction.gaps[]`. Run `/ea-gaps list` to see all managed gaps." |
