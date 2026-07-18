# EA Assistant — First-Class Operating Model Artifact Plan

**Target version:** 0.9.88  
**Source material:**
- Executive distinction: Business Architecture vs Business Operating Model (the `/ce-plan` prompt)
- `skills/ea-artifact-templates/references/ea-concepts.md`
- `templates/phase-b/business-architecture.md`

**Scope:** Make the Operating Model a first-class Phase B artifact with its own template and slash command, sharpen the Business Architecture / Operating Model distinction in concepts and guidance, refactor the Business Architecture template to focus on the stable business blueprint, and keep execution-design content (organisation, processes, controls, sourcing, workforce, performance management) in the Operating Model artifact.

---

## Decisions

| Decision | Choice | Rationale |
|---|---|---|
| **Operating Model surface** | New slash command `/ea-operatingmodel` + dedicated artifact template `operating-model.md` | First-class treatment matching Architecture Vision, Business Architecture, Data Architecture, etc. Makes OM scoreable, linkable, and exportable. |
| **OM content ownership** | OM is an **authored artifact**, not a generated register | Organisation design, decision rights, controls, sourcing, and workforce are narrative/design frameworks. The structured pieces already have homes: `PROC-NNN` in `/ea-processes`, `ROLE-NNN` as EA engagement roles, `SVC-NNN` as business services. |
| **BA template refactor** | Remove §2 Organisation Model and §4 Business Processes from `business-architecture.md`; replace with summary-and-link pointers to the OM artifact and the Business Processes Register | Keeps BA focused on capabilities, value streams, services, information, rules, and measures. Avoids duplicating execution design. |
| **Role boundary** | `/ea-roles` stays EA **engagement** roles; business operating roles live in the OM artifact tables | The Role Catalogue (`ROLE-NNN`) is governance/RACI for the EA effort, not the target operating model. Clarify in command text. |
| **Process home** | `PROC-NNN` and `/ea-processes` remain the authoritative execution-flow register; OM artifact links to it | Business processes are OM elements. No new prefix or register needed. |
| **Service home** | `SVC-NNN` and `/ea-services` remain BA concepts; add optional **Delivery Model** field to note OM delivery arrangements | The service *definition* is BA; *how* it is delivered is OM. |
| **Storage model** | No new top-level `engagement.json` array for OM; store the artifact entry in `artifacts[]` like other authored Phase B artifacts | OM content is mostly free-form. Reuse existing `businessProcesses[]` for structured process data. |
| **ID scheme** | No new ID prefixes | Reuse `CAP-NNN`, `VS-NNN`, `SVC-NNN`, `BR-NNN`, `PROC-NNN`, `UC-NNN`, `ROLE-NNN`. OM artifact itself has `artifactId: operating-model`. |
| **Zachman cell** | `operating-model.md` → `Enterprise/How` (same as `business-architecture.md`) | OM answers "How does the enterprise function to deliver value?" at the enterprise level. |
| **Compliance carry-over** | OM requires T3-A3, T3-A4, T3-ADR, T3-RATIONALE, linked to BA, traced to Requirements Register | Same tier-3 obligations as other Phase B authored artifacts. |

A decision journal entry will be created at `ea-assistant/decisions/2026-07-17-operating-model-artifact.md` (supplements, does not replace, `2026-07-17-business-architecture-layer-storage.md`).

---

## Implementation Units

### Phase 0 — Concepts and storage foundation

- `skills/ea-artifact-templates/references/ea-concepts.md`
  - Sharpen the **Operating Model** definition: explicitly contrast it with **Business Architecture** (what vs. how; stable blueprint vs. execution design).
  - Add a short **Concept Home** table mapping business-layer concepts to BA / OM / Both:
    - BA: Capability Model, Value Streams, Business Services, Business Information, Business Rules, Business Measures, Use Cases
    - OM: Organisation Design, Roles & Decision Rights, Governance & Controls, Business Processes, Resources & Workforce, Sourcing, Technology/Data Enablement, Performance Management, Locations/Channels
    - Both: Requirements, Stakeholder Concerns, Gaps
- `ea-assistant/CLAUDE.md`
  - Update version pointer to 0.9.88.
  - Add `/ea-operatingmodel` to Command Reference.
  - Update Business Architecture command/template descriptions to reflect OM separation.
- `templates/seeds/engagement-json.md`
  - No new top-level array required; confirm schema supports artifact entries for `operating-model`.
- `skills/ea-engagement-lifecycle/references/engagement-schema.md`
  - Document that `operating-model` is a Phase B authored artifact in `artifacts[]`; processes remain in `businessProcesses[]`.
- `skills/ea-engagement-lifecycle/references/migration-gap-catalogue.md`
  - Add a `GAP-M` entry for legacy engagements where BA artifacts contain Organisation Model / Business Processes sections that should be split into a separate OM artifact.
- `commands/ea-migrate.md`
  - Add a Step-3k probe: if `business-architecture.md` still contains `## 2. Organisation Model` or `## 4. Business Processes`, offer to create `operating-model.md` and move those sections.

### Phase 1 — New Operating Model artifact and command

- `templates/phase-b/operating-model.md`
  - Frontmatter: `artifact: Operating Model`, `artifactId: operating-model`, `phase: B`, `zachmanCell: Enterprise/How`, audience Business/Architecture.
  - Compliance Checklist: T3-A3, T3-A4, T3-ADR, T3-RATIONALE, Linked to Business Architecture, Traces to Requirements Register.
  - Guidance block explaining the BA/OM split and the artifact's purpose.
  - Sections:
    1. Executive Summary
    2. Operating Model Context — link to `business-architecture`, `architecture-vision`, `statement-of-architecture-work`
    3. Organisation Design — structure, operating units, governance fora
    4. Roles, Decision Rights & Accountability — operating roles (not EA roles), RACI for key decisions
    5. Business Processes Execution Model — summary table linking to `business-processes-register.md` and `PROC-NNN` detail files
    6. Controls, Policies & SLAs — business controls and performance thresholds
    7. Workforce, Locations & Channels — people, skills, geography, delivery channels
    8. Sourcing & Partnership Model — make/buy/partner, vendor roles
    9. Information & Technology Enablement — how data/app/tech enable the OM (links to Phase C/D artifacts)
    10. Performance Management — KPIs, metrics, review cadence
    11. Gap Analysis — OM gaps linked to `GAP-NNN`
    12. Appendix A3 — Decision Log
    13. Appendix A4 — Stakeholder Concerns (CON-NNN)
    14. Appendix A5 — Related Architecture Decisions (ADR-NNN)
    15. Traceability Summary
- `commands/ea-operatingmodel.md`
  - Modes: `create | view | check | link | interview`
  - `create` — create `operating-model.md` from template (wraps `/ea-artifact create operating-model`) and seed links to BA/AV.
  - `view` — display OM artifact with compliance status.
  - `check` — verify OM links back to `business-architecture.md`, links forward to `business-processes-register.md`, and has no orphan processes.
  - `link` — quick-link a process, role, service, or ADR into the OM artifact's relevant table.
  - `interview` — run a short OM-specific question bank (org design, decision rights, controls, sourcing, workforce, performance management).

### Phase 2 — Business Architecture template refactor

- `templates/phase-b/business-architecture.md`
  - Update Guidance block: explicitly state BA = stable blueprint (capabilities, value streams, services, information, rules, measures); OM = execution design.
  - Remove `## 2. Organisation Model` (move content to OM on migration).
  - Keep `## 1. Business Context` but add a pointer to the OM artifact when it exists.
  - Keep `## 3. Business Capabilities` and `## 3a. Value Streams` (BA content).
  - Replace `## 4. Business Processes` with a summary-and-link section: `## 4. Business Processes (summary)` that points to the Business Processes Register and OM artifact.
  - Keep `## 4a. Use Case Catalog` as summary-and-link (use cases are BA behavior artifacts).
  - Update `## Related Matrices` if needed (process matrices stay but are sourced from OM context).
  - Ensure Compliance Checklist no longer expects Organisation Model or detailed process tables inside BA.

### Phase 3 — Command alignment and clarity

- `commands/ea-processes.md`
  - Update description to mention OM context: processes are execution-flow elements mastered in the OM.
  - In `add` mode, after capturing process, offer: "Link this process to the Operating Model? (y/n)" — if yes, add `operatingModelContext` note and update OM artifact §5.
- `commands/ea-roles.md`
  - Update description: "Role Catalogue for EA engagement roles (`ROLE-NNN`) — not business operating roles, which live in the Operating Model artifact."
- `commands/ea-services.md`
  - Add optional fields: `deliveryChannel`, `operatingModelNote`.
  - Update description: business services are BA concepts; delivery arrangements are captured in OM.
- `commands/ea-artifact.md`
  - Add to Artifact Naming map: "Operating Model" / "Operating Model Design" → `operating-model`.
  - Ensure `create` can resolve the new template.
- `commands/ea-score.md`
  - Add `operating-model` to the authored-artifact scoring list (it is not generated, so it is scored).
- `templates/cross-cutting/cross-cutting-index.md`
  - No change required; OM is a Phase B artifact, not a cross-cutting register. Optionally add a note in the Context/Operations section pointing to Phase B artifacts.

### Phase 4 — Compliance, scoring, and matrices

- `skills/ea-artifact-templates/references/compliance-check.md`
  - Add an `operating-model` artifact section with checks:
    - T3-A3 Appendix A3 present
    - T3-A4 (if applicable)
    - T3-ADR Appendix A5 present
    - T3-RATIONALE no missing strategic rationale blocks
    - Linked to `business-architecture`
    - Traces to Requirements Register
    - §5 Business Processes Execution Model links to at least one `PROC-NNN`
- `skills/ea-engagement-lifecycle/references/grill-scoring-rubric.md`
  - Add scoring guidance for `operating-model.md` sections (completeness weights, quality criteria).
- `commands/ea-grill.md` / `skills/ea-grill-skills/SKILL.md`
  - Add OM artifact to grillable artifact types.
  - Add checks: OM gaps trace to BA capabilities; processes are not duplicated between BA and OM; OM describes how, not what.
- `skills/ea-artifact-templates/references/matrix-catalogue.md`
  - Confirm `process-value-stream`, `capability-organization`, `actor-role` matrices are available; add `process-operating-model` matrix if useful (Process × OM section).

### Phase 5 — Interview and persona updates

- `commands/ea-interview.md` / `skills/ea-interviewer/SKILL.md`
  - Add a Phase B OM interview mode: questions for org design, decision rights, controls, sourcing, workforce, performance management, channels.
  - Ensure Phase B BA interview no longer asks org-chart/process-step questions; those route to OM mode.
- `skills/ea-engagement-lifecycle/references/phase-interview-questions.md`
  - Split Phase B questions into BA stream and OM stream.
- `skills/ea-engagement-lifecycle/references/persona-registry.md`
  - Add `/ea-operatingmodel` to relevant personas (business-architect, cio, chief-product-officer).

### Phase 6 — Version bump and documentation hygiene

Bump version to **0.9.88** in:
- `ea-assistant/.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json` (relative from ea-assistant/)
- `ea-assistant/docs/PRD.md` — add a v0.9.88 release section covering the BA/OM split
- `ea-assistant/commands/ea-help.md` — add `/ea-operatingmodel`; update `/ea-processes`, `/ea-roles`, `/ea-services` descriptions
- `ea-assistant/README.md` — update feature bullets and commands table
- `ea-assistant/CLAUDE.md` — update version, command count, Command Reference, and Business Architecture description

Also:
- Align every `skills/*/SKILL.md` frontmatter `version` to 0.9.88.
- Run `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/`.

---

## Verification Checklist

- [ ] Create a test engagement (`/ea-new`).
- [ ] `/ea-artifact create operating-model` → verify `artifacts/phase-b/operating-model.md` is created with correct frontmatter and compliance checklist.
- [ ] `/ea-operatingmodel check` on a fresh OM → reports expected missing links to BA and processes register.
- [ ] `/ea-artifact create business-architecture` → verify template has no `## 2. Organisation Model` and no full `## 4. Business Processes` section.
- [ ] `/ea-processes add` → verify process is stored in `engagement.json → businessProcesses[]` and register is generated.
- [ ] `/ea-operatingmodel link PROC-NNN` → verify OM artifact §5 references the process.
- [ ] `/ea-score operating-model` → verify Completeness/Quality Scorecard block is written and `engagement.json → artifacts[].scores` is updated.
- [ ] `/ea-grill operating-model` → verify OM-specific compliance checks run and flag missing BA link if absent.
- [ ] `/ea-consistency --ids` → no false positives on `operating-model` artifact or OM sections.
- [ ] `/ea-migrate --report` on a legacy engagement → detects Organisation Model / Business Processes in BA and proposes OM creation.
- [ ] `/ea-generate operating-model docx` succeeds and exports the artifact.
- [ ] Run frontmatter validation on `ea-assistant/`; parse all new JSON/markdown files.

---

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Existing engagements have BA artifacts with Organisation Model / Business Processes sections | `/ea-migrate` detects and offers to split them into a new OM artifact; snapshots preserve original content. |
| Users confuse `/ea-roles` (EA engagement roles) with business operating roles | Update command description and OM artifact guidance; keep `ROLE-NNN` strictly for EA governance roles. |
| OM overlaps with `/ea-processes` register | Define clear boundary in `ea-concepts.md`: OM artifact is the *integrating execution design*; processes register is the *structured activity catalogue*. |
| Scoring rubric missing OM weights | Add OM section weights to `grill-scoring-rubric.md` in Phase 4 before `/ea-score` is exposed. |
| Process linkage back to OM is manual | `/ea-processes add` offers an OM link; `/ea-operatingmodel check` flags orphans. |

---

## Out of Scope

- BPMN import, process simulation, or dynamic swimlane rendering.
- New ID prefixes or new cross-cutting registers for OM sub-elements.
- Changes to other plugins (`RAG-assistant`, `ITIL-assistant`).
- Major rewrite of all Phase B interview questions beyond BA/OM split.
- External system deployment or stakeholder communications.
- Auto-extraction of org charts from uploads.
