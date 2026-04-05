---
name: ea-artifact
description: Create, view, or list EA artifacts for the active engagement
argument-hint: "[create|list|view] [artifact-name]"
allowed-tools: [Read, Write, Bash]
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
11. Ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-next.md` and output the recommendation.

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
