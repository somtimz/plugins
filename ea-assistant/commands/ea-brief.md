---
name: ea-brief
description: Generate a synthesized one-page engagement brief emphasising the most significant decisions, risks, gaps, and open items across all artifacts
argument-hint: "[--focus decisions|risks|gaps|strategy] [--save]"
allowed-tools: [Read, Write, Glob]
---

Generate a synthesized engagement brief for the active engagement.

## Purpose

`/ea-brief` reads across all artifacts and produces a prioritised, opinionated brief — not a flat artifact list. It surfaces what matters most: strategic direction, key decisions, critical gaps, top risks, and open concerns that need attention. Output is inline in the conversation unless `--save` is passed.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

---

### Step 1 — Collect engagement data

Read the following in order:

1. **`engagement.json`** — name, type, `architectureLevel`, currentPhase, sponsor, direction (goals G-NNN, objectives OBJ-NNN, strategies STR-NNN), phase statuses, artifact list (id, status, reviewStatus, file path).

2. **All artifact files** in `artifacts/` — for each file that exists, scan for:
   - `## Executive Summary` — use verbatim if present; skip if absent
   - `## Appendix A3 — Decision Log` — extract rows where Authority = Strategic or Impact = High/Med
   - `## Appendix A4 — Stakeholder Concerns & Objections` — extract rows where Status = `Requires Attention`
   - Gap rows (`| GAP-`) — extract where Severity = Critical or High
   - Risk rows (`| RIS-`) — extract where Likelihood or Impact = Critical or High

3. **Cross-cutting registers** (if present):
   - `artifacts/cross-cutting/risk-register*.md` — all RIS-NNN rows
   - `artifacts/cross-cutting/decision-register*.md` — all Strategic decisions
   - `artifacts/cross-cutting/adr-register*.md` — ADRs with status In Progress or Completed

---

### Step 2 — Parse flags

| Flag | Behaviour |
|---|---|
| *(none)* | Balanced brief — all sections, 3–5 items each, ranked by significance |
| `--focus decisions` | Expand decisions to full detail (all Strategic + High-Impact); compress other sections to top 2 items each |
| `--focus risks` | Expand risks to full detail (all Critical + High); compress other sections to top 2 items each |
| `--focus gaps` | Expand gaps to full detail (all Critical + High); compress other sections to top 2 items each |
| `--focus strategy` | Expand strategic direction (all goals, objectives, strategies); compress other sections to top 2 items each |
| `--save` | Write the brief to `artifacts/cross-cutting/engagement-brief-{YYYY-MM-DD}.md` after displaying it |

---

### Step 3 — Produce the brief

Output the brief inline using this structure:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENGAGEMENT BRIEF  —  {Engagement Name}
{Organisation}  ·  {Engagement Type}  ·  Level: {architectureLevel}  ·  Phase: {currentPhase}
Sponsor: {sponsor}  ·  {today's date}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## Strategic Direction

{Top 2–3 goals from engagement.json direction — one line each: G-NNN: {statement}}
{Top 1–2 objectives — OBJ-NNN: {measurable target, deadline if present}}
{Top 1–2 strategies — STR-NNN: {approach}}

If direction is empty: ⚠️ No direction captured yet — run `/ea-interview` Phase A or `/ea-direction`.

---

## Key Decisions

{Top 3–5 decisions, ranked: Strategic authority first, then High-Impact Tactical; within tier by date (newest first)}

For each:
  [{Authority}] {Item} — {Value/Outcome}
  Rationale: {one-line from A3.N block, or "not captured"}
  Source: {artifact name} · {date}

⚠️ Flag any Strategic decision with no A3.N rationale block.

If no decisions: ⚠️ No governance decisions captured yet — use `a: {text}` during interviews or `/ea-adrs new`.

---

## Critical Gaps

{Top 3–5 gaps ranked: Critical first, then High}

For each:
  {GAP-NNN}: {description} — Severity: {severity}
  Source: {artifact name}

If no gap analysis exists: ⚠️ Gap analysis not yet performed for phases: {list phases in progress or complete with no gap artifact}.

---

## Top Risks

{Top 3–5 risks ranked by Likelihood × Impact; Critical/High only unless --focus risks}

For each:
  {RIS-NNN}: {title} — {Likelihood}/{Impact} | Status: {status} | Owner: {owner}
  ⚠️ flag if mitigation strategy is empty

If no risk register: ⚠️ No risks captured — run `/ea-risks generate` or add risks during interviews.

---

## Open Concerns

{All CON-NNN where Status = Requires Attention, up to 5; oldest first}

For each:
  {CON-NNN}: {concern} — Raised by: {source}
  Action: {action/owner}

If none: ✅ No unresolved stakeholder concerns recorded.

---

## Engagement Status

Phases complete:      {comma-separated list, or "none yet"}
Phases in progress:   {comma-separated list}
Phases not started:   {comma-separated list of applicable phases only}

Artifacts: {N} total  ·  {N} ✅ Approved  ·  {N} 🔄 In Review  ·  {N} 📝 Draft  ·  {N} ⚠️ Needs Revision

Next: {one sentence — current phase's most urgent next action, or the next phase to begin}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Significance ranking rules:**
- **Decisions:** Strategic authority → Tactical → Operational; within tier, High Impact before Med before Low; newest date first within same tier/impact
- **Gaps:** Critical → High; omit Med/Low unless `--focus gaps`
- **Risks:** Critical → High by combined Likelihood + Impact; omit Low unless `--focus risks`
- **Concerns:** Requires Attention only; oldest first (longest unresolved = most urgent)

**When data is sparse** (early-phase or lightly-populated engagement):
- Show what exists; for each empty section, state clearly what is missing and which command or interview would populate it
- Do not fabricate or infer content — use `⚠️ Not yet captured` and a remediation suggestion

---

### Step 4 — Save (if `--save` flag provided)

Write the brief to `artifacts/cross-cutting/engagement-brief-{YYYY-MM-DD}.md` with frontmatter:

```yaml
---
artifact: Engagement Brief
engagement: {name}
phase: {currentPhase}
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {YYYY-MM-DDTHH:MM:SSZ}
generatedBy: /ea-brief
taxonomy:
  domain: Cross-cutting
  category: Planning
  audience: Executive
  layer: Reference
  sensitivity: Internal
  tags: [cross-cutting, brief, executive, summary]
---
```

Confirm the saved path and offer: `Run /ea-publish --executive to include this brief in an executive pack.`

---

### Notes

- `/ea-brief` is **read-only** — it never modifies artifacts or `engagement.json`
- Run at the end of each phase for a stakeholder-ready progress snapshot
- Combine with `/ea-publish --executive` for a full board/sponsor pack
- If the brief reveals significant gaps in captured content, use `/ea-interview`, `/ea-risks`, or `/ea-concerns` to populate the missing sections
