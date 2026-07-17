# EA Assistant — Business Architecture Deck Enrichment Plan

**Target version:** 0.9.86  
**Source material:**
- `/mnt/d/dev/misc/Business-Architecture-Explained-Complete-Guide.pptx`
- `/mnt/d/dev/misc/Business-Goals-by-Stakeholder.pptx`
- `/mnt/d/dev/misc/Business-Architecture-Deliverables-In-Depth.pptx`

**Scope:** Add first-class register management for Business Processes, Use Cases, and Value Streams; add a Stakeholder Goal Classification reference/template; and enrich the existing goal, capability, requirement, business-rule, and business-service commands/templates.

---

## Decisions

| Decision | Choice | Rationale |
|---|---|---|
| **Storage model** | New top-level arrays in `engagement.json`: `valueStreams[]`, `businessProcesses[]`, `useCases[]` | Follows the established cross-cutting register pattern (`rules[]`, `services[]`, `finance[]`). These are operational/business-layer objects, not motivation-chain items, so they do not belong under `direction`. |
| **Business Process ID prefix** | `PROC-NNN` | Avoids collision with `BP-NNN` (Business Principle) and `PRB-NNN` (Problem); no domain-prefixed ID, consistent with the unified scheme. |
| **Stakeholder Goal Classification** | Reference/template + optional `stakeholder` field on `G-NNN` goals | The deck content is a classification lens, not a first-class architecture object. No new ID prefix or register command is needed. |
| **Business Architecture artifact layout** | §3a/§4/§4a become **summary-and-link** sections pointing to generated registers and detail files | Mirrors the Phase-A Vision index model (v0.9.80). Avoids fragile display-view table sync and keeps authored process-step detail in per-item detail files. |
| **Scoring** | New registers are **not** scored | They are command-generated registers, outside the six Phase-A motivation-register exception. |
| **PPTX ingestion** | Backfill the document-ingestion skill to accept `.pptx` as a separate, lower-priority unit | Closes a tooling gap exposed by the task, but the source decks have already been extracted for this plan. |

A decision journal entry will be created at `ea-assistant/decisions/2026-07-17-business-architecture-layer-storage.md`.

---

## Implementation Units

### Phase 0 — Foundation (schema, concepts, migration)

- `skills/ea-artifact-templates/references/ea-concepts.md`
  - Verify/cite Value Stream, Business Process, Use Case definitions; add a short note pointing to the source decks for quality-check guidance.
- `ea-assistant/CLAUDE.md`
  - Add `PROC-NNN` to the ID Scheme table; update command count and version pointer.
- `templates/seeds/engagement-json.md`
  - Add `valueStreams[]`, `businessProcesses[]`, `useCases[]` arrays to the seed schema.
- `skills/ea-engagement-lifecycle/references/engagement-schema.md`
  - Document the new top-level arrays and their item schemas.
- `skills/ea-engagement-lifecycle/references/migration-gap-catalogue.md`
  - Add GAP-M entries for missing arrays and a `[]` backfill rule.
- `commands/ea-migrate.md`
  - Add Step-2 probes for the new arrays.

### Phase 1 — New registers, commands, and skills

New skills (mirroring `ea-business-rules-management/SKILL.md`):
- `skills/ea-value-streams-management/SKILL.md`
- `skills/ea-business-processes-management/SKILL.md`
- `skills/ea-use-cases-management/SKILL.md`

New commands (`list|add|update|trace|generate`):
- `commands/ea-valuestreams.md`
- `commands/ea-processes.md`
- `commands/ea-usecases.md`

New register seed templates:
- `templates/cross-cutting/operations/value-streams-register.md`
- `templates/cross-cutting/operations/business-processes-register.md`
- `templates/cross-cutting/operations/use-cases-register.md`

Cross-cutting index update:
- `templates/cross-cutting/cross-cutting-index.md` — list the three new registers under Operations.

Detail-file convention:
- On `add`, offer to create `artifacts/details/{VS|PROC|UC}-NNN.md` only when the user supplies step/flow content (no bulk empty stubs).

### Phase 2 — Business Architecture template alignment

- `templates/phase-b/business-architecture.md`
  - §3a **Value Streams**: convert placeholder table to a summary table linking to the generated register and detail files.
  - §4 **Business Processes**: convert to a summary table + register links; move detailed step tables into `artifacts/details/PROC-NNN.md` on demand.
  - §4a **Use Case Catalog**: convert to summary table + register links.
  - §8a **Traceability Summary**: add `PROC-NNN` and confirm `VS-NNN`/`UC-NNN` hops.
  - §**Related Matrices**: add `process-value-stream`, `use-case-capability`, `use-case-process`.

### Phase 3 — Matrices and traceability

- `skills/ea-artifact-templates/references/matrix-catalogue.md`
  - Add `process-value-stream` (Phase B)
  - Add `use-case-capability` (Phase B)
  - Add `use-case-process` (Phase B)
- `commands/ea-trace.md`
  - Extend the motivation/execution chain: Goal → Capability → Value Stream → Process → Use Case → Requirement.
- `commands/ea-consistency.md`
  - Include `VS-NNN`, `PROC-NNN`, and `UC-NNN` in ID reference scans.
- `commands/ea-grill.md` / `skills/ea-grill-skills/SKILL.md`
  - Add orphan checks for processes/use cases/value streams in `business-architecture.md` reviews.

### Phase 4 — Enrichment of existing commands/templates

**Stakeholder Goal Classification**
- New reference: `skills/ea-engagement-lifecycle/references/stakeholder-goal-classification.md`
  - Map goal categories to Senior Management, Business Unit Manager, Staff, and Ultimate Client.
- `commands/ea-goals.md`
  - Add optional `stakeholder` field with the four values above.
- `templates/phase-a/goals-register.md`
  - Add a Stakeholder column.
- `commands/ea-interview.md` / `skills/ea-interviewer/SKILL.md`
  - Add a Phase-A prompt to classify each goal by stakeholder.

**Capabilities**
- `commands/ea-capabilities.md`
  - Add optional `differentiation` field: `Differentiating | Enabling | Commodity`.
  - Allow linking to `VS-NNN`.
- `templates/phase-b/business-architecture.md`
  - Add a **Differentiation** column to the capability table.

**Requirements**
- `commands/ea-requirements.md`
  - Add `source` field: `Driver | Goal | Objective | Use Case | Business Scenario | Process`.
  - Add `acceptanceCriteria` field.
  - Allow upstream links to `UC-NNN`, `PROC-NNN`, `VS-NNN`.

**Business Rules / Services**
- `commands/ea-rules.md`
  - Add `linkedProcesses` and `linkedUseCases` link fields.
- `commands/ea-services.md`
  - Add `linkedValueStreams` and `linkedProcesses` link fields.

### Phase 5 — PPTX ingestion backfill (optional)

- `skills/ea-document-ingestion/SKILL.md` + `skills/ea-document-ingestion/references/file-format-guide.md`
  - Add `.pptx` to supported formats.
- New helper: `scripts/extract-pptx.py` (using `python-pptx`) or extend existing scripts.
- Follow the existing three-stage ingestion pipeline: converter → `ea-document-analyst` → user-confirmed population, with `📎 Source:` attribution.

### Phase 6 — Version bump and documentation hygiene

Bump version to **0.9.86** in:
- `ea-assistant/.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `ea-assistant/docs/PRD.md` — add a v0.9.86 release section
- `ea-assistant/commands/ea-help.md` — add the three new commands; update matrix count
- `ea-assistant/README.md` — update feature bullets and commands table
- `ea-assistant/CLAUDE.md` — update version, command count, ID scheme, and matrix count

Also:
- Align every `skills/*/SKILL.md` frontmatter `version` to 0.9.86.
- Run `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/`.

---

## Verification Checklist

- [ ] Create a test engagement.
- [ ] `/ea-valuestreams add`, `/ea-processes add`, `/ea-usecases add` → verify `engagement.json` arrays.
- [ ] Run each `generate` → verify register files, `snapshots/` archive, and `artifacts[]` entry.
- [ ] `/ea-trace` → verify Goal → Capability → Value Stream → Process → Use Case → Requirement chain.
- [ ] `/ea-consistency --ids` → no false positives on new prefixes.
- [ ] `/ea-grill business-architecture` → flags orphan processes/use cases/value streams.
- [ ] `/ea-goals add` with stakeholder field → register shows the classification.
- [ ] Run frontmatter validation; parse all new JSON/markdown files.
- [ ] Export test: `/ea-generate business-architecture docx` with `--matrices` succeeds.

---

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Command-surface bloat (the improvement advisory flags near-duplicate register commands) | Keep each new command thin; reuse `register-protocol.md` mechanics and shared skill logic. |
| Display-view sync complexity | Replace BA artifact tables with summary+link sections, following the Vision-index precedent. |
| ID collisions or invented prefixes | Add only `PROC-NNN`; `VS-NNN` and `UC-NNN` already exist. No domain-prefixed IDs. |
| Legacy engagements missing new arrays | `/ea-migrate` backfills empty arrays; document in migration-gap catalogue. |
| PPTX ingestion scope creep | Keep it as a separate, lower-priority unit; do not let it block the core register work. |

---

## Out of Scope

- BPMN import, process simulation, or dynamic swimlane rendering.
- AI-assisted process discovery from arbitrary uploads.
- Cross-engagement process pattern libraries.
- External system deployment or stakeholder communications.
