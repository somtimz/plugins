---
name: ea-artifact
description: Create, view, list, or manage executive summaries for EA artifacts in the active engagement
argument-hint: "[create|list|view|summary] [artifact-name]"
allowed-tools: [Read, Write, Bash, Glob]
---

Manage EA artifacts for the active engagement.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

### Mode: `list` (default when no argument given)

Display all artifacts for the active engagement:

```
Artifacts — Acme Retail Transformation
═══════════════════════════════════════════════════════
Phase      Artifact                        Status        Review
─────────────────────────────────────────────────────────────
Prelim     Architecture Principles         ✅ Approved    Approved
Req        Requirements Register           🔄 Draft       Not Reviewed
Phase A    Architecture Vision             🔄 Draft       In Review
Phase A    Statement of Architecture Work  ⬜ Not Created  —
Phase A    Stakeholder Map                 ⬜ Not Created  —
Phase B    Business Architecture           ⬜ Not Created  —
...
═══════════════════════════════════════════════════════
```

Offer: create a missing artifact, view an existing one, start an interview.

### Phase Folder Mapping

Derive the artifact's storage folder from the `phase` field in the template frontmatter:

| Template phase | Folder |
|---|---|
| Prelim or Prelim/A | `artifacts/preliminary/` |
| Requirements | `artifacts/requirements/` |
| A | `artifacts/phase-a/` |
| B | `artifacts/phase-b/` |
| C-Data | `artifacts/phase-c-data/` |
| C-App | `artifacts/phase-c-app/` |
| D | `artifacts/phase-d/` |
| E or E/F | `artifacts/phase-e/` |
| F | `artifacts/phase-f/` |
| G | `artifacts/phase-g/` |
| H | `artifacts/phase-h/` |
| All or cross-cutting | `artifacts/cross-cutting/` |
| `{{phase}}` | resolve from engagement's `currentPhase` at creation time |

### Mode: `create [artifact-name]`

1. Match the artifact name to a template in the plugin's `templates/` directory
2. If ambiguous, show a numbered list of matching templates
3. Determine the phase folder using the **Phase Folder Mapping** table above
4. Copy the template to `EA-projects/{slug}/artifacts/{phase-folder}/{artifact-id}.md`
5. Pre-populate known fields from `engagement.json` (name, sponsor, organisation, date)
6. Pre-populate any requirements linked to this phase from `requirements/requirements-index.json`
7. Set `templateVersion` in the artifact frontmatter to the current plugin version (read from `.claude-plugin/plugin.json`)
8. Resolve any `{{phase}}` placeholder in the frontmatter to the actual phase value
9. Add entry to `artifacts[]` in `engagement.json` — `file` path must be `artifacts/{phase-folder}/{artifact-id}.md`
10. Confirm creation and offer to start an interview to populate it
11. Ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-status.md` (the `--next` flag section) and output the recommendation.

### Mode: `view [artifact-name]`

1. Find the artifact file using the path recorded in `engagement.json → artifacts[].file`. If that entry is missing, search all `artifacts/*/` subfolders for `{artifact-id}.md`
2. **Run the Compliance Check** (see `skills/ea-artifact-templates/references/compliance-check.md`):
   - If all checks pass → display artifact with a `✅ Compliant` badge.
   - If failures exist → display a compliance notice above the artifact content:
     ```
     ⚠️ Compliance gaps detected ({N} issues). Options:
       1. Achieve compliance now
       2. Accept as-is (use with defaults)
       3. View compliance details
       4. Continue viewing (no action)
     ```
     If the user selects 4 or presses Enter → display the artifact as-is without changes.
3. Display the artifact content
4. Show review status and any open review comments from `{artifact}.review.md`
5. Offer:
   - Edit via interview (`/ea-interview`)
   - Start review
   - **Deep review — grill-me** (`/ea-grill {artifact-name}`) — stress-test, boardroom, pre-mortem, or design critique using the recommended skill for this artifact type
   - Export to Word
   - Achieve compliance (if non-compliant)

### Artifact Naming

Map common names to file IDs:
- "Engagement Charter" / "Charter" → `engagement-charter`
- "Architecture Vision" → `architecture-vision`
- "Business Architecture" → `business-architecture`
- "Data Architecture" / "Information Architecture" → `data-architecture`
- "Application Architecture" → `application-architecture`
- "Technology Architecture" → `technology-architecture`
- "Gap Analysis" → `gap-analysis-{phase}` (prompt for phase)
- "Roadmap" / "Architecture Roadmap" → `architecture-roadmap`
- "Stakeholder Map" → `stakeholder-map`
- "Requirements Register" → `requirements-register`
- "Migration Plan" → `migration-plan`
- "Statement of Architecture Work" → `statement-of-architecture-work`
- "Architecture Principles" → `architecture-principles`
- "Governance Framework" / "Architecture Governance Framework" → `governance-framework`
- "Implementation Governance Plan" → `implementation-governance-plan`
- "Change Request" / "Architecture Change Request" → `change-request`
- "Change Register" → generated by `/ea-changes`
- "Zachman Diagram" / "Zachman" / "Zachman Framework" → managed by `/ea-zachman`
- "ADR" / "Architecture Decision Record" → managed by `/ea-adrs new`
- "ADR Register" → generated by `/ea-adrs generate`

### Mode: `summary [refresh [artifact-name] | status]`

Refresh or review executive summaries for the active engagement's artifacts.

**Sub-mode: `refresh [artifact-name]`**

Regenerate the Executive Summary for one artifact, or for a user-selected set.

1. **If an artifact name is provided:** Locate the artifact file. Check it has a `## Executive Summary` section. If absent, offer to add the standard section first.

2. **If no artifact name is provided:** List all created artifacts that have a `## Executive Summary` section and present a numbered selection menu with multi-select support.

3. **For each selected artifact:**
   - Read the full artifact content.
   - Draft a 3–5 sentence executive summary: what this artifact covers, what has been decided or described, and what is notable or still open. Avoid technical jargon.
   - Present the draft:
     > **Executive Summary for {Artifact Name}:**
     > {drafted summary}
     > Accept? (y / edit / skip)
   - On `y`: write the summary to the `## Executive Summary` section; update `lastModified` in `engagement.json`.
   - On `edit`: show in an editable prompt; apply the user's version.
   - On `skip`: leave unchanged; continue to next artifact.

4. After all artifacts are processed, confirm:
   ```
   Executive summary refresh complete.
   ✅ Updated: {N} artifacts
   ⏭️  Skipped: {N} artifacts
   ```

**Sub-mode: `status`**

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
   ```
   Status values: ✅ Present | ⚠️ Placeholder only | ❌ Section absent

4. If any artifacts have ⚠️ or ❌ status, offer: `Run /ea-artifact summary refresh to update missing or placeholder summaries.`
