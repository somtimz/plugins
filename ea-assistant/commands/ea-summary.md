---
name: ea-summary
description: Refresh or review executive summaries for EA artifacts
argument-hint: "[refresh [artifact-name] | status]"
allowed-tools: [Read, Write, Glob]
---

Refresh or review executive summaries for the active engagement's artifacts.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

---

### Mode: `refresh [artifact-name]`

Regenerate the Executive Summary for one artifact, or for a user-selected set.

1. **If an artifact name is provided:**
   - Locate the artifact file in `EA-projects/{slug}/artifacts/`.
   - Check that it has a `## Executive Summary` section. If absent, offer to add the standard section first, then continue.

2. **If no artifact name is provided:**
   - List all created artifacts that have a `## Executive Summary` section.
   - Present a numbered selection menu with multi-select support:
     ```
     Artifacts with Executive Summary sections:

       #  Artifact                        Phase   Last Modified
       ─────────────────────────────────────────────────────────
       1  Architecture Vision             A       2026-03-14
       2  Business Architecture           B       2026-03-18
       3  Requirements Register           Req     2026-03-12
     ```
     Prompt: `Enter numbers (e.g. 1,3), a range (e.g. 1-3), or "all":`.

3. **For each selected artifact:**
   - Read the full artifact content.
   - Draft a 3–5 sentence executive summary: what this artifact covers, what has been decided or described, and what is notable or still open. Avoid technical jargon.
   - Present the draft:
     > **Executive Summary for {Artifact Name}:**
     > {drafted summary}
     > Accept? (y / edit / skip)
   - On `y`: write the summary to the `## Executive Summary` section of the artifact; update `lastModified` in `engagement.json`.
   - On `edit`: show the summary in an editable prompt; apply the user's version.
   - On `skip`: leave unchanged; continue to the next artifact.

4. After all artifacts are processed, confirm:
   ```
   Executive summary refresh complete.
   ✅ Updated: {N} artifacts
   ⏭️  Skipped: {N} artifacts
   ```

---

### Mode: `status`

Show executive summary coverage across all created artifacts.

1. Read `engagement.json` and list all created artifacts.

2. For each artifact, check whether its file contains a `## Executive Summary` section and whether the placeholder `{{executive_summary}}` is still unfilled.

3. Present a coverage table:
   ```
   Executive Summary Status — {Engagement Name}

     #  Artifact                        Phase   Summary
     ─────────────────────────────────────────────────────────
     1  Architecture Vision             A       ✅ Present
     2  Business Architecture           B       ✅ Present
     3  Requirements Register           Req     ⚠️  Placeholder only
     4  Technology Architecture         D       ❌ Section absent
     5  Risk Register                   Cross   ✅ Present
   ```

   Status values:
   - ✅ Present — section exists and is filled
   - ⚠️  Placeholder only — section exists but still contains `{{executive_summary}}`
   - ❌ Section absent — no `## Executive Summary` section in the artifact

4. If any artifacts have `⚠️` or `❌` status, offer:
   `Run /ea-summary refresh to update missing or placeholder summaries.`
