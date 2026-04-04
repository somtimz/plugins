---
name: ea-consistency
description: Focused consistency check — cross-artifact contradictions, ID reference validation, and within-artifact section consistency. Faster and more targeted than /ea-engage-review.
argument-hint: "[artifact <id>] [--ids] [--report]"
allowed-tools: [Read, Glob, Grep, Bash]
---

You are executing the `/ea-consistency` command.

## Overview

Runs a focused consistency check on the active engagement. Unlike `/ea-engage-review`, this command does not cover governance, quality scores, or alignment — it checks only consistency and ID integrity. All modes are **read-only**: no files are modified.

**Modes:**

| Args | Mode | What it checks |
|---|---|---|
| (none) | Full | Cross-artifact contradictions, naming consistency, requirement traceability, phase alignment, ID reference validation |
| `artifact <id>` | Artifact | Within-artifact section consistency + ID refs scoped to that file |
| `--ids` | IDs only | Fast scan — ID definition registry, broken references, orphaned IDs |
| `--report` (added to any mode) | Report | Suppresses interactive menu; prints full report inline |

---

## Step 1 — Resolve Active Engagement

Check context for active slug. If none, scan `EA-projects/*/engagement.json` and ask the user to select. Load `engagement.json` and extract `name` and `slug`.

---

## Step 2 — Mode Dispatch

Parse the arguments passed to this command and route to the appropriate mode below.

---

### Full Mode (no args)

Invoke the `ea-consistency-checker` agent. Instruct it to run all steps including the ID reference validation step (step 5b). Pass the engagement slug and artifact root path.

After the agent produces its report, unless `--report` was specified, offer:

```
What would you like to do?

  1. View full ID reference report
  2. Deep-review an artifact        →  /ea-grill [artifact]
  3. Full engagement review         →  /ea-engage-review
  Enter a number or press Enter to close.
```

---

### Artifact Mode (`artifact <id>`)

**1. Locate the artifact**

Use Glob to find `EA-projects/{slug}/artifacts/**/{id}.md`. If not found, list available artifact IDs and ask the user to confirm.

**2. Within-artifact section consistency**

Read the artifact. For each top-level section heading (`## ...`), collect all ID tokens matching `(G|OBJ|DRV|STR|ISS|PRB|MET|REQ|RIS|ADR|WP|GAP|CON)-\d{3}` and the label or description text immediately associated with each token (the same table row, or the inline text surrounding it).

Build a map: `{ id → [ { section, label_text } ] }`

Flag any ID that appears in two or more sections with **differing label text**. Example:
```
⚠️  G-001 labelled inconsistently within this artifact:
    §3 Goals:              "Reduce operational costs"
    §14 Strategic Alignment: "Reduce supply chain costs"
    → Standardise the label across all sections
```

**3. ID reference validation (scoped to this artifact)**

Scan all other artifacts in `EA-projects/{slug}/artifacts/**/*.md` to build the engagement-wide ID definition registry (see step 5b in `ea-consistency-checker` for the definition rules).

Then check every ID referenced in the current artifact against the registry. Report any broken references (ID used in this artifact but not defined anywhere in the engagement).

**4. Output**

```
Consistency check: {artifact-name}
──────────────────────────────────
Within-artifact label inconsistencies: {N}
Broken ID references: {N}

[findings listed]

✅ No further issues found.
```

Unless `--report`, offer:
```
  1. Run a full engagement consistency check  →  /ea-consistency
  2. Deep-review this artifact                →  /ea-grill {id}
  3. Continue
```

---

### IDs-Only Mode (`--ids`)

Fast path — skips all entity/contradiction/traceability logic.

**1. Build ID definition registry**

Scan every `.md` file in `EA-projects/{slug}/artifacts/**/*.md`. An ID is **defined** when it appears as:
- First cell of a Markdown table row: `| G-001 | ...`
- A heading that begins with the ID token: `## G-001 — label`

Pattern: `(G|OBJ|DRV|STR|ISS|PRB|MET|REQ|RIS|ADR|WP|GAP|CON)-\d{3}`

**2. Scan for references**

Scan every artifact for any occurrence of the pattern. Occurrences that are NOT the definition source are references.

**3. Report**

```
ID Reference Scan — {engagement name}
──────────────────────────────────────
IDs defined:    {N}
IDs referenced: {N}

🔴 Broken references ({N})
| Artifact | Section | ID | Context |
|---|---|---|---|
| phase-a/architecture-vision.md | §14 Key Risks | RIS-007 | "linked to RIS-007" |

ℹ️  Orphaned IDs — defined but never referenced elsewhere ({N})
| Artifact | ID |
|---|---|
| phase-b/business-architecture.md | GAP-003 |

✅ All other IDs valid.
```

Unless `--report`, offer:
```
  1. Run full consistency check  →  /ea-consistency
  2. Continue
```
