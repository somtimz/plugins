---
name: ea-operatingmodel
description: Create, view, check, and manage the Operating Model artifact — the execution-design counterpart to the Business Architecture
type: command
argument-hint: "[create|view|check|link|interview] [args]"
allowed-tools: [Read, Write, Bash, Glob]
---

You are executing the `/ea-operatingmodel` command. Load the `ea-artifact-templates` skill for concept definitions and template handling, and the `ea-engagement-lifecycle` skill for engagement resolution.

## Overview

The Operating Model is a first-class Phase B artifact that describes **how** the organisation will operate to deliver value: organisation design, decision rights, governance/controls, business process execution context, workforce/locations/channels, sourcing, technology/data enablement, and performance management. It is the execution-design counterpart to the **Business Architecture**, which describes *what* the organisation must be able to do (capabilities, value streams, services, etc.).

Before prompting or validating, read `skills/ea-artifact-templates/references/ea-concepts.md` → **Operating Model** for the canonical definition and the BA/OM concept-home table.

**Modes:**
- `create` (default if no mode specified and artifact does not exist) — create `artifacts/phase-b/operating-model.md` from the template, seed links to Business Architecture and Architecture Vision, and register it in `engagement.json → artifacts[]`
- `view` — display the OM artifact with its compliance status
- `check` — validate OM links: links back to BA, links forward to Business Processes Register, no orphan process references
- `link` — quick-link a mastered item into the OM artifact (process, service, ADR, metric, vendor)
- `interview` — run the OM-specific question bank to populate the artifact

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, `artifacts[]`, `businessProcesses[]`, `services[]`.

---

## Mode: `create`

1. Check if `artifacts/phase-b/operating-model.md` already exists. If yes → switch to `view` mode and tell the user.
2. Ensure Phase B status is at least `In Progress`. If not, warn: "Phase B is not yet started. Run `/ea-phase B` first? (y/n)".
3. Copy `templates/phase-b/operating-model.md` to `EA-projects/{slug}/artifacts/phase-b/operating-model.md`.
4. Pre-populate known fields from `engagement.json`: name, sponsor, organisation, date (today).
5. Set `templateVersion` in the artifact frontmatter to the current plugin version (read from `.claude-plugin/plugin.json`).
6. Add cross-reference fields in the artifact frontmatter:
   - `relatedArtifacts: ["business-architecture", "architecture-vision", "statement-of-architecture-work"]`
   - `diagrams: []`
   - `links: []`
7. Add an entry to `engagement.json → artifacts[]`:
   ```json
   {
     "artifactId": "operating-model",
     "name": "Operating Model",
     "phase": "B",
     "file": "artifacts/phase-b/operating-model.md",
     "status": "Draft",
     "reviewStatus": "Not Reviewed",
     "version": "0.1",
     "templateVersion": "{current_version}"
   }
   ```
8. Confirm creation and offer to start the OM interview (`/ea-operatingmodel interview`).

---

## Mode: `view`

1. Find the OM file using `engagement.json → artifacts[].file` (fallback: search `artifacts/phase-b/operating-model.md`).
2. Run the Compliance Check (see `skills/ea-artifact-templates/references/compliance-check.md`) for `operating-model`:
   - If all checks pass → display artifact with a `✅ Compliant` badge.
   - If failures exist → display a compliance notice above the content with options to achieve compliance or view details.
3. Display the artifact content.
4. Show review status and any open review comments from `operating-model.review.md`.
5. Offer:
   - Edit via interview (`/ea-operatingmodel interview`)
   - Deep review (`/ea-grill operating-model`)
   - Export to Word (`/ea-generate operating-model docx`)

---

## Mode: `check`

1. Load the OM artifact and parse its sections.
2. Resolve the linked Business Architecture file (`artifacts/phase-b/business-architecture.md`).
3. Load `engagement.json → businessProcesses[]`.
4. Report:

```
Operating Model Check — {engagement name}
════════════════════════════════════════════════════════════
Business Architecture linked         {✅ / ⚠️ missing back-link}
Processes Register linked            {✅ / ⚠️ no §5 table entries}
Orphan process references            {N} PROC-NNN IDs in OM not found in engagement.json
Processes without OM context         {N} active PROC-NNN entries not referenced in OM
Controls linked to POL/CST/BR        {✅ / ⚠️}
Sourcing linked to VDR (if any)    {✅ / ⚠️}
Metrics linked to MET-NNN            {✅ / ⚠️}
════════════════════════════════════════════════════════════
```

5. If orphans or missing links are found, suggest:
   - `/ea-operatingmodel link PROC-NNN` to add a process reference
   - `/ea-operatingmodel interview` to populate missing sections
   - `/ea-processes add` to create missing process entries

---

## Mode: `link <item-type> <id>`

Supported item types: `process`, `service`, `adr`, `metric`, `vendor`.

Examples:
- `/ea-operatingmodel link process PROC-001`
- `/ea-operatingmodel link service SVC-003`
- `/ea-operatingmodel link adr ADR-012`
- `/ea-operatingmodel link metric MET-005`
- `/ea-operatingmodel link vendor VDR-002`

1. Verify the ID exists in `engagement.json` or the appropriate register.
2. Insert a row reference into the relevant OM section:
   - `process` → §5 Business Processes Execution Model
   - `service` → §8 Information & Technology Enablement (or §5 if service delivery is process-centric)
   - `adr` → Appendix A5 — Related Architecture Decisions
   - `metric` → §9 Performance Management
   - `vendor` → §7 Sourcing & Partnership Model
3. Update `relatedArtifacts` or `links` frontmatter if a new artifact-level cross-reference is created.
4. Confirm the link and show the updated table.

---

## Mode: `interview`

Run a structured OM interview question bank. The interview is Phase B scoped and complements the Business Architecture interview. It does **not** ask about capabilities or value streams — those are captured via `/ea-interview` BA mode or `/ea-capabilities` / `/ea-valuestreams`.

Question areas (asked in order, skip if the section already has non-placeholder content and the user opts to keep it):

1. **Organisation Design** — operating units, governance fora, reporting changes
2. **Decision Rights** — key decisions, accountable roles, escalation paths
3. **Governance, Controls & SLAs** — controls, policies, review cadence
4. **Business Processes Execution Model** — which processes execute key value streams (links to PROC-NNN)
5. **Workforce, Locations & Channels** — skills, geography, delivery channels
6. **Sourcing & Partnership Model** — make/buy/partner rationale
7. **Information & Technology Enablement** — how data/apps/tech enable the OM
8. **Performance Management** — metrics, review cadence, ownership

Capture answers as draft text under each section. When a decision meets the ADR threshold (tech/vendor selection, high cost/risk, hard to reverse, make-vs-buy, contested, affects governance/security/compliance/principles), suggest `/ea-adrs new`.

After the interview, run `/ea-operatingmodel check` automatically and show the result.

---

## Output Format

**`create`:**
```
Operating Model artifact created — artifacts/phase-b/operating-model.md
Linked to: Business Architecture, Architecture Vision, Statement of Architecture Work
Next: /ea-operatingmodel interview
```

**`check`:** see table above.

**`link`:**
```
Linked {type} {ID} to Operating Model §{section}.
```

---

## Edge Cases

| Scenario | Handling |
|---|---|
| OM already exists | Switch to `view`; do not overwrite |
| Business Architecture does not exist | Create OM anyway; flag missing back-link in `check` |
| Phase B not started | Warn and offer `/ea-phase B` |
| Link target ID not found | Report "{ID} not found in engagement.json or registers" and stop |
| OM artifact passed to `/ea-score` | Scored as authored artifact using the OM rubric |
