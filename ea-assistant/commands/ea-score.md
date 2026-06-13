---
name: ea-score
description: Score artifacts on Completeness and Quality (0–100 with bands), per section and overall, using the grill scoring rubric. Writes an author-only Scorecard block into each artifact; --all scores the whole engagement; --status shows the last scores without rescoring.
argument-hint: "[artifact-id | --all | --status] [--no-write]"
allowed-tools: [Read, Write, Bash, Glob]
---

You are executing the `/ea-score` command. Load the `ea-grill-skills` skill (the scoring engine) and read `skills/ea-engagement-lifecycle/references/grill-scoring-rubric.md` (the rubric — scale, bands, the two scores, the four Quality sub-dimensions including readability, the roll-up, and the Scorecard block format). For concept definitions used by the Quality "definition-correctness" check, the rubric points to `ea-concepts.md`; do not restate definitions here.

`/ea-score` is the **scoring pass** — it produces the two scores per section and overall and writes them into each artifact's Scorecard block. It is lighter than `/ea-grill` (which runs the full adversarial review); both use the same rubric, and `/ea-grill` also refreshes the Scorecard when it runs.

## Step 1 — Resolve Active Engagement

1. Check conversation context for an active engagement slug. If none, scan `EA-projects/*/engagement.json` (excluding `.archive/`) and ask the user to select one.
2. Load `engagement.json` — name, slug, `artifacts[]`.

## Step 2 — Parse Arguments

| Mode | Invocation | Effect |
|---|---|---|
| Single | `/ea-score {artifact-id}` | Score one artifact; write its Scorecard block |
| All | `/ea-score --all` | Score every authored artifact; write each Scorecard; show the engagement roll-up |
| Status | `/ea-score --status` | Read existing scores (Scorecard blocks / `engagement.json`), show the roll-up — **no rescoring, no writes** |

`--no-write` (single/all): compute and show scores but do not modify any artifact (preview).

## Scope (which artifacts are scored)

Score **authored** artifacts. **Skip command-generated artifacts** (their bodies are owned by a generating command, so a "quality" score is not meaningful): any artifact with a `generated:` frontmatter field, or whose `artifactId` matches `*-register`, `*-matrix`, `decision-register`, `cost-model-register`, `traceability-matrix`, `zachman-diagram`, `role-catalogue`, `consolidated-report`, or `cross-cutting-index`. List skipped artifacts under the roll-up as `— (generated; not scored)`. This mirrors the `/ea-migrate` 3i/3j/3k scope.

## Step 3 — Score an Artifact (single, and per artifact under `--all`)

1. Load the artifact file. Extract its `## ` body sections (exclude the author-only `## Compliance Checklist`, the `📊 Scorecard` block itself, and `## Artifact Working Notes`).
2. Extract each section's `<details>📋 Guidance</details>` block (the scoring standard). If a section has none, score against TOGAF best practice for the artifact type and note it.
3. For each section, apply the rubric:
   - **Completeness 0–100** from the section's populated/placeholder state (rubric mapping).
   - **Quality 0–100** from the four sub-dimensions (definition-correctness, guidance adherence, evidence & rigour, readability) — or `—` if the section is empty.
   - Record a short Note (the worst readability/quality issue, or `—`).
4. Compute the **overall** Completeness (required-section-weighted mean) and Quality (mean over non-empty sections) per the rubric.
5. Unless `--no-write` or `--status`: **write/refresh the Scorecard block** in the artifact (replace any existing `📊 Scorecard` block in place; place a new one after the Compliance Checklist block, or after the H1 if absent). Set the Scorecard's `last scored` date to today.
6. Update `engagement.json → artifacts[]` for this artifact: set `scores: { completeness: {N}, quality: {N}, scoredAt: "{today}" }`. Do not change `status` or `reviewStatus`.
7. **Approved artifacts:** scoring is read-only by default — show the scores but prompt before writing the block: "{name} is Approved. Write the Scorecard block? (reviewStatus stays Approved.) (y/n)".

## Step 4 — Output

**Single:**
```
Score — {Artifact Name}
  Completeness  {N}/100 ({band})
  Quality       {N}/100 ({band})
  Weakest section: {section} (Completeness {N} / Quality {N}) — {note}
Scorecard written to the artifact ({M} sections scored).
```

**`--all` / `--status` (engagement roll-up):**
```
Scorecard — {Engagement Name}   (scored {date})
══════════════════════════════════════════════════════════════
Artifact                        Phase   Completeness    Quality
──────────────────────────────────────────────────────────────
Architecture Vision             A       78 (Substantial) 66 (Partial)
Business Architecture           B       64 (Partial)     71 (Partial)
Risk Register                   All     — (generated; not scored)
──────────────────────────────────────────────────────────────
Engagement mean (authored)      {N} Completeness · {N} Quality
Lowest: {artifact} ({score})    |    Below 50: {list or None}
```

Sort by phase then artifact. After `--all`, suggest: "Run `/ea-grill {artifact}` for a deep review of the lowest-scoring artifact, or `/ea-score {artifact}` after revising to track improvement."

## Edge Cases

| Scenario | Handling |
|---|---|
| Artifact has no guidance blocks (legacy) | Score against TOGAF best practice; note `*(no guidance blocks — scored against best practice)*`; suggest `/ea-migrate` (scan 3i) to backfill guidance |
| Artifact is all placeholders | Completeness ~0–20 (Stub), Quality `—`; flag "not yet populated — run `/ea-interview`" |
| Existing Scorecard block present | Replace it in place (match on `📊 Scorecard`); never append a duplicate |
| `--status` but no scores recorded | "No scores yet — run `/ea-score --all` first." |
| Generated artifact passed by id | "{id} is command-generated — its body is owned by {command}; not scored. Run that command to refresh it." |
