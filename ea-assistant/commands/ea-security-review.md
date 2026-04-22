---
name: ea-security-review
description: Security audit for EA artifacts — checks SABSA layer coverage, ISO 27001 control domains, and NIST CSF function coverage. Full engagement audit by default; single artifact with /ea-security-review <artifact-id>; filter by framework with --framework sabsa|iso|nist.
argument-hint: "[<artifact-id>] [--framework sabsa|iso|nist]"
allowed-tools: [Read, Write, Glob, Grep, Bash]
---

You are executing the `/ea-security-review` command.

## Overview

Runs a security audit on the active engagement using the `ea-security-auditor` agent. Three security frameworks are assessed: SABSA layer coverage, ISO 27001 control domains, and NIST CSF function coverage.

**Modes:**

| Args | Scope | What is audited |
|---|---|---|
| (none) | Full engagement (Scope C) | All artifacts — full coverage assessment across all three frameworks |
| `<artifact-id>` | Single artifact (Scope A) | One artifact — gaps relative to its phase and purpose |
| `--framework sabsa\|iso\|nist` | Framework filter | Combined with either scope — report limited to the specified framework |

---

## Step 1 — Resolve Active Engagement

Check context for active engagement slug. If none, scan `EA-projects/*/engagement.json` and ask the user to select one. Load `engagement.json` and extract `name` and `slug`.

If `EA-projects/` is empty or contains no valid engagement directories, tell the user:

```
No engagements found. Run /ea-new to create your first engagement.
```

---

## Step 2 — Parse Arguments

Inspect the arguments passed to this command:

- No args → **Full mode** (Scope C)
- First positional arg (no `--` prefix) → **Artifact mode** (Scope A); treat the value as `<artifact-id>`
- `--framework sabsa` | `--framework iso` | `--framework nist` → set framework filter; combine with whichever scope applies
- Both a positional arg and `--framework` → Artifact mode with framework filter

---

## Step 3 — Load Context

### Full Mode (Scope C)

Load full engagement context using **Scope C** from `skills/ea-engagement-lifecycle/references/context-loading.md`. Announce the loaded context before proceeding.

### Artifact Mode (Scope A)

**3a. Locate the artifact**

Use Glob to find `EA-projects/{slug}/artifacts/**/{artifact-id}.md`. If not found, list available artifact IDs and ask the user to confirm.

**3b. Load artifact-scoped context**

Load context using **Scope A** from `skills/ea-engagement-lifecycle/references/context-loading.md`. Announce the loaded context before proceeding.

---

## Step 4 — Dispatch ea-security-auditor

Invoke the `ea-security-auditor` agent. Pass:

- The engagement slug and artifact root path (`EA-projects/{slug}/artifacts/`)
- The determined scope (full or single artifact) and all loaded file paths
- The framework filter, if specified (`--framework sabsa|iso|nist`); if no filter, instruct the agent to report all three frameworks

Instruct the agent to produce a **Security Audit Report** using the format defined in its system prompt.

---

## Step 5 — Offer to Save the Report

After the agent produces its report, prompt:

```
Save this report to EA-projects/{slug}/artifacts/cross-cutting/notes/security-audit-{YYYY-MM-DD}.md? (y/n)
```

Use today's date for `{YYYY-MM-DD}`. If the user confirms, write the report file. If the file already exists (e.g. multiple runs on the same day), append a suffix: `security-audit-{YYYY-MM-DD}-2.md`.

---

## Step 6 — Recommended Next Steps

After the report (and optional save), suggest:

```
Next steps:

  • /ea-security-review --framework <framework>   — Focus on a single framework (sabsa, iso, or nist)
  • /ea-grill security <artifact-id>              — Deep interactive review of a flagged artifact
  • Ask the ea-security-advisor                   — Guidance on addressing specific findings
```

Tailor the suggestions to what the report found — if only one framework showed gaps, surface that framework in the first suggestion. If specific artifacts were flagged, name one in the second suggestion.

---

## Usage Examples

```
/ea-security-review                          — Full engagement audit
/ea-security-review architecture-vision      — Single artifact
/ea-security-review --framework iso          — ISO 27001 gaps only
/ea-security-review --framework sabsa        — SABSA coverage only
```
