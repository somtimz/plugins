---
name: ea-artifact
description: Create, view, or list EA artifacts for the active engagement
argument-hint: "[create|list|view] [artifact-name]"
allowed-tools: Read, Write, Bash
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

### Mode: `create [artifact-name]`

1. Match the artifact name to a template in `plugins/ea-assistant/templates/`
2. If ambiguous, show a numbered list of matching templates
3. Copy the template to `EA-projects/{slug}/artifacts/{artifact-id}.md`
4. Pre-populate known fields from `engagement.json` (name, sponsor, organisation, date)
5. Pre-populate any requirements linked to this phase from `requirements-index.json`
6. Add entry to `artifacts[]` in `engagement.json`
7. Confirm creation and offer to start an interview to populate it

### Mode: `view [artifact-name]`

1. Find the artifact file in `artifacts/`
2. Display the artifact content
3. Show review status and any open review comments from `{artifact}.review.md`
4. Offer: edit via interview, start review, export to Word

### Artifact Naming

Map common names to file IDs:
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
