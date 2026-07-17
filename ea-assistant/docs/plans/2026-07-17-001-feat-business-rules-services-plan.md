---
title: EA Assistant — Business Rules & Business Services - Plan
type: feat
date: 2026-07-17
artifact_contract: ce-unified-plan/v1
artifact_readiness: implementation-ready
execution: code
---

# EA Assistant — Business Rules & Business Services - Plan

## Goal Capsule

**Objective:** Add first-class **Business Rule** (`BR-NNN`) and **Business Service** (`SVC-NNN` with a `Type: Business` column) support to the `ea-assistant` plugin, grounded in the York Region business-rules framework and the user-supplied Business Services guidance.

**Authority hierarchy:** User request → project `CLAUDE.md` constraints (no inline concept definitions, unified ID scheme, `engagement.json` as single source of truth, relative paths, frontmatter validation).

**Stop conditions:** The plan covers canonical concept definitions, the new `BR-NNN` ID prefix, register commands and management skills, register/detail-file templates, `engagement.json` wiring, matrix-catalogue additions, documentation/marketplace updates, version bump, and verification gates. It does **not** author rule/service content for a live client engagement.

**Execution profile:** File-level plugin changes across ~25 files. Work on a feature branch and land via PR per the project workflow.

**Tail ownership:** Implementer verifies frontmatter validation and JSON integrity before opening the PR.

---

## Product Contract

### Summary

Introduce two new first-class EA objects and their registers:

- **Business Rule (`BR-NNN`)** — declarative statements that govern business behaviour (obligation, prohibition, permission, definition, derivation, condition). Rules carry a category, structural elements (Subject, Condition, Directive, Outcome, Authority, Enforcement), lifecycle state, and traceability to policies, constraints, services, and requirements.
- **Business Service (`SVC-NNN`, `Level: Business`)** — externally visible, contract-governed business behaviour offered to consumers via the Consumer–Outcome–Interface triad, with a Service Passport (Name, Owner, Value Proposition, SLAs, Inputs/Outputs, Applicable Rules) and anti-pattern checks.

Both are persisted as top-level arrays in `engagement.json`, rendered on demand into cross-cutting registers, and wired into existing traceability, scoring, and publishing flows.

### Requirements

R1. Add a canonical **Business Rule** concept and `BR-NNN` ID prefix in `skills/ea-artifact-templates/references/ea-concepts.md` and the `ea-assistant/CLAUDE.md` ID scheme table.

R2. Extend the existing **Service** concept in `ea-concepts.md` to explicitly define *Business Service* (`Level: Business`) and keep the unified `SVC-NNN` ID for all service levels; no domain-prefixed IDs such as `BSV-NNN`.

R3. Add top-level `rules[]` and `services[]` arrays to `engagement.json` schema, the seed template, and `/ea-migrate` backfill logic.

R4. Create `/ea-rules` command with modes `list|add|update|trace|impact|generate`, following the register-protocol pattern.

R5. Create `/ea-services` command with modes `list|add|update|trace|impact|generate`, following the register-protocol pattern.

R6. Create `skills/ea-business-rules-management/SKILL.md` and `skills/ea-business-services-management/SKILL.md` defining field schemas, lifecycle states, trace chains, groupings, and register-specific checks.

R7. Create register seed templates:
  - `templates/cross-cutting/business-rules-register.md`
  - `templates/cross-cutting/business-services-register.md`

R8. Update `templates/cross-cutting/item-detail.md` guidance to cover `BR-NNN` and `SVC-NNN` detail files; detail files live at `artifacts/details/{ID}.md` as usual.

R9. Update `templates/cross-cutting/cross-cutting-index.md` to list the new registers under Governance (Rules) and Context (Services).

R10. Add two matrices to `skills/ea-artifact-templates/references/matrix-catalogue.md`:
  - `business-rule-service` — rows = `BR-NNN`, columns = `SVC-NNN`
  - `capability-service` — rows = `CAP-NNN`, columns = `SVC-NNN`

R11. Update `commands/ea-help.md`, `commands/ea-meta.md`, and `commands/ea-status.md` to surface the new registers and counts.

R12. Update `README.md`, `docs/PRD.md`, `ea-assistant/CLAUDE.md`, `.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json`; plugin and marketplace descriptions must match exactly.

R13. Bump `version` in `.claude-plugin/plugin.json` and in **all** `ea-assistant/skills/*/SKILL.md` frontmatter files to the new release version.

R14. Run the frontmatter validator (`~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/`) and confirm it passes before committing.

### Scope Boundaries

- **In scope:** Plugin infrastructure for rules and services (concepts, IDs, commands, skills, templates, schema, docs, version).
- **Out of scope:** Authoring actual business rules or services for a specific engagement; changes to the Architecture Repository shared schema; new agents; changes to Python export scripts beyond ensuring the new register files are discovered by `/ea-generate` and `/ea-publish`.

### Dependencies

- Existing register-protocol, constraints/policies commands, and motivation-register commands are the implementation pattern.
- The frontmatter validator is run via the locally installed Bun binary.

---

## Planning Contract

### Key Technical Decisions

KTD1. **Storage model:** Rules and services live as top-level siblings in `engagement.json` (`rules[]`, `services[]`), alongside `metrics[]`, `policies[]`, and `finance[]`. This makes them first-class, cross-cutting registers and lets `/ea-rules generate` and `/ea-services generate` produce stable register files from JSON, consistent with the direction-register pattern.

KTD2. **ID scheme:** New `BR-NNN` for Business Rules. Reuse `SVC-NNN` for services and add a `Level` column (`Business` / `Application` / `Technology`) rather than inventing a separate `BSV-NNN` prefix. This preserves the existing `goal-service` matrix and service catalogue conventions.

KTD3. **Register placement:**
  - `artifacts/cross-cutting/governance/business-rules-register.md` — rules are governance artefacts that operationalise policies/constraints.
  - `artifacts/cross-cutting/context/business-services-register.md` — services are business-context reference material, analogous to the Role Catalogue and Zachman Diagram.

KTD4. **Command pattern:** `/ea-rules` and `/ea-services` are thin command files that load rich skills. They follow `register-protocol.md` for `list/add/update/trace/generate` and add an `impact` mode (downstream capabilities, work packages, requirements). No Display View Sync into the Architecture Vision — rules/services are not Phase-A motivation registers; registers are refreshed via `generate`.

KTD5. **No new agents:** Existing `ea-interviewer` can suggest rules/services during Phase B interviews; the commands and skills do the management.

KTD6. **Matrices are data-only additions:** Add entries to `matrix-catalogue.md`; `/ea-matrix` consumes the catalogue automatically, so no core matrix logic changes.

### Assumptions

- The user’s extracted frameworks (`Business Rules in York Region.docx` text and the inline Business Services guidance) are authoritative for rule/service definitions; canonical plugin definitions cite them without restating the full taxonomy.
- The current plugin version is `0.9.84`; this change will ship as `0.9.85`.
- Existing engagements without `rules[]`/`services[]` are backfilled as empty arrays by `/ea-migrate` without user prompting.

### Sequencing

1. Concept + ID scheme + schema/seed/migration.
2. Skills + commands.
3. Templates + cross-cutting index + matrices.
4. Help/status/meta + README/PRD/CLAUDE/marketplace + version bump.
5. Verification and PR.

---

## Implementation Units

### U1. Canonical concepts and ID scheme

**Goal:** Define Business Rule and Business Service in the concept reference and update the ID scheme.

**Requirements:** R1, R2.

**Files:**
- `ea-assistant/skills/ea-artifact-templates/references/ea-concepts.md`
- `ea-assistant/CLAUDE.md`

**Approach:**
- Insert a `### Business Rule (BR-NNN)` section after the existing `Constraint` or `Policy` section. Define: declarative statement, structural elements, categories, lifecycle, and distinction from policy/constraint/requirement/principle. Cite the York Region framework.
- Update the existing `### Service (SVC-NNN)` section to add a `Level` column and a Business Service paragraph; cite the Business Services guidance.
- Add `BR-NNN` to the ID Scheme table in `ea-assistant/CLAUDE.md`. Clarify that `SVC-NNN` covers all service levels with a `Level` column.

**Test scenarios:**
- `rg "Business Rule" ea-concepts.md` returns the new section.
- `rg "BR-NNN" CLAUDE.md` returns the ID table entry.

**Verification:** Read the edited sections and confirm no inline definitions contradict `ea-concepts.md`.

---

### U2. `engagement.json` schema, seed template, and migration backfill

**Goal:** Persist rules and services in the engagement record and keep legacy engagements forward-compatible.

**Requirements:** R3.

**Files:**
- `ea-assistant/skills/ea-engagement-lifecycle/references/engagement-schema.md`
- `ea-assistant/templates/seeds/engagement-json.md`
- `ea-assistant/commands/ea-migrate.md` (or the migration logic it calls)

**Approach:**
- In `engagement-schema.md`, add `rules[]` and `services[]` top-level arrays with full entry schemas (see Appendix A for proposed fields).
- In `engagement-json.md`, add `"rules": []` and `"services": []` after `finance`.
- In `/ea-migrate`, add a migration step that backfills missing `rules`/`services` arrays as `[]` and records the change in `migrations[]`.

**Test scenarios:**
- A new `/ea-new` engagement contains empty `rules` and `services` arrays.
- Running `/ea-migrate` on an engagement created at v0.9.84 adds the arrays without overwriting existing data.

**Verification:** Inspect generated `engagement.json` after `/ea-new` and after `/ea-migrate`.

---

### U3. Business Rules management skill

**Goal:** Provide the rich logic for the `/ea-rules` command.

**Requirements:** R6.

**Files:**
- `ea-assistant/skills/ea-business-rules-management/SKILL.md` (new)

**Approach:**
- Frontmatter: `name`, `description`, `version: 0.9.85`.
- Declare a Register Spec:
  - Prefix `BR`, storage `engagement.json → rules[]`, register file `artifacts/cross-cutting/governance/business-rules-register.md`, seed template `templates/cross-cutting/business-rules-register.md`.
  - Fields: `statement`, `type` (Obligation / Prohibition / Permission / Definition / Derivation / Condition), `category` (Structural / Operative / Derivation / Decision / Event), `subject`, `condition`, `directive`, `outcome`, `authority`, `enforcement`, `status` (Draft / Proposed / Approved / Implemented / Retired), `sourcePolicy` (POL-NNN optional), `linkedConstraints` (CST-NNN optional), `linkedServices` (SVC-NNN optional), `linkedRequirements` (REQ-NNN optional), `owner`, `reviewCycle`, `phase`.
  - Link fields and orphan rules.
  - Groupings: by `category`, then by `status`.
  - Checks: rule statement must contain a clear Subject + Condition + Directive; Approved rules must have an Owner and Authority.
- Reuse `register-protocol.md` mechanics; do not restate them inline.

**Test scenarios:**
- `/ea-rules add` assigns `BR-001` and stores the entry in `engagement.json`.
- `/ea-rules generate` writes `business-rules-register.md` from the seed template.

**Verification:** Read the skill and confirm it delegates protocol mechanics and cites `ea-concepts.md`.

---

### U4. Business Services management skill

**Goal:** Provide the rich logic for the `/ea-services` command.

**Requirements:** R6.

**Files:**
- `ea-assistant/skills/ea-business-services-management/SKILL.md` (new)

**Approach:**
- Frontmatter: `name`, `description`, `version: 0.9.85`.
- Declare a Register Spec:
  - Prefix `SVC`, storage `engagement.json → services[]`, register file `artifacts/cross-cutting/context/business-services-register.md`, seed template `templates/cross-cutting/business-services-register.md`.
  - Fields: `name`, `level` (Business / Application / Technology), `owner`, `valueProposition`, `consumers`, `outcomes`, `interfaces` (IFC-NNN), `inputs`, `outputs`, `slas`, `applicableRules` (BR-NNN), `realisedBy` (CAP-NNN / ABB-NNN / SBB-NNN), `linkedRequirements` (REQ-NNN), `status` (Proposed / Approved / Operational / Sunsetting / Retired), `phase`.
  - Link fields and orphan checks.
  - Groupings: by `level`, then by `status`; anti-pattern flags for Shadow/God/Protocol services.
- Reuse `register-protocol.md` mechanics.

**Test scenarios:**
- `/ea-services add` assigns `SVC-001` with `Level: Business`.
- `/ea-services generate` writes `business-services-register.md`.

**Verification:** Read the skill and confirm it delegates protocol mechanics and cites `ea-concepts.md`.

---

### U5. Register commands

**Goal:** Expose `/ea-rules` and `/ea-services` slash commands.

**Requirements:** R4, R5.

**Files:**
- `ea-assistant/commands/ea-rules.md` (new)
- `ea-assistant/commands/ea-services.md` (new)

**Approach:**
- Mirror the thin-command shape of `commands/ea-drivers.md` / `commands/ea-constraints.md`:
  - Frontmatter with `name`, `description`, `argument-hint`, `allowed-tools`.
  - Step 1: resolve active engagement.
  - Mode dispatch: `list|add|update|trace|impact|generate`.
  - Load the corresponding skill for detailed logic.
- `list` renders from `engagement.json` and the register file; `add`/`update` mutate `engagement.json` and nudge `generate`; `generate` archives the prior register per the snapshot convention.

**Test scenarios:**
- `/ea-rules list` on an empty engagement shows the empty-state message.
- `/ea-services generate` creates `artifacts/cross-cutting/context/business-services-register.md` and registers it in `engagement.json → artifacts[]`.

**Verification:** Read both command files and confirm frontmatter is valid and modes are complete.

---

### U6. Register seed templates and cross-cutting index

**Goal:** Provide guidance-rich register artifacts and navigation.

**Requirements:** R7, R8, R9.

**Files:**
- `ea-assistant/templates/cross-cutting/business-rules-register.md` (new)
- `ea-assistant/templates/cross-cutting/business-services-register.md` (new)
- `ea-assistant/templates/cross-cutting/cross-cutting-index.md`
- `ea-assistant/templates/cross-cutting/item-detail.md`

**Approach:**
- Copy the structure of `constraints-register.md` / `policies-register.md`:
  - YAML frontmatter with `artifact`, `artifactId`, `taxonomy` (`category: Register`, `audience: All`/`Architecture`, `layer: Reference`/`Governance`, `tags` including `cross-cutting`, `business-rules`/`business-services`).
  - `<details>` compliance and guidance blocks.
  - Summary count table.
  - Grouped section tables with placeholder rows.
  - Appendix A3/A5.
- In `item-detail.md`, add bullet guidance for `BR-NNN` (rule elements, lifecycle, trace to services) and `SVC-NNN` (consumer-outcome-interface triad, SLAs, applicable rules).
- In `cross-cutting-index.md`, add rows for Business Rules Register under Governance and Business Services Register under Context, with the correct `generate` commands.

**Test scenarios:**
- Frontmatter validator accepts the new templates.
- `/ea-rules generate` fills the seed template and produces a valid register file.

**Verification:** Run the frontmatter validator after writing templates.

---

### U7. Matrix catalogue additions

**Goal:** Let `/ea-matrix` create rule-to-service and capability-to-service relationship matrices.

**Requirements:** R10.

**Files:**
- `ea-assistant/skills/ea-artifact-templates/references/matrix-catalogue.md`

**Approach:**
- Add `business-rule-service` entry under Cross-cutting/Phase B:
  - Axes: rows = `BR-NNN`, columns = `SVC-NNN`.
  - Markers: `A` applies · `E` enforces · `I` implemented by · `N` not applicable.
  - Seed sources: `artifacts/cross-cutting/governance/business-rules-register.md` and `artifacts/cross-cutting/context/business-services-register.md`.
  - Grill checks: every Approved rule applies to at least one service or is flagged; every Business service column with no rule is flagged.
- Add `capability-service` entry under Phase B:
  - Axes: rows = `CAP-NNN`, columns = `SVC-NNN`.
  - Markers: `R` realises · `S` supports · `C` consumes · `M` missing.
  - Seed sources: `artifacts/phase-b/business-architecture.md` and `artifacts/cross-cutting/context/business-services-register.md`.
- Update the `goal-service` seed-sources line to also include the services register.

**Verification:** Confirm the catalogue file parses and the Phase Index count reflects the new matrices.

---

### U8. Help, meta, and status surfaces

**Goal:** Make the new registers discoverable in command menus and dashboards.

**Requirements:** R11.

**Files:**
- `ea-assistant/commands/ea-help.md`
- `ea-assistant/commands/ea-meta.md`
- `ea-assistant/commands/ea-status.md`

**Approach:**
- `ea-help.md`: add two rows to the All Commands table for `/ea-rules` and `/ea-services`; update the feature/tips prose.
- `ea-meta.md`: add `rules` and `services` counts to the Direction (or a new Cross-cutting Registers) group in View Mode.
- `ea-status.md`: add `rules` and `services` counts to the portfolio/dashboard output and `--direction` view where cross-cutting registers are summarised.

**Verification:** Grep the three files for `ea-rules` and `ea-services` and confirm counts are wired.

---

### U9. Documentation, marketplace, and version bump

**Goal:** Keep all public-facing plugin metadata consistent at the new version.

**Requirements:** R12, R13.

**Files:**
- `ea-assistant/.claude-plugin/plugin.json`
- `ea-assistant/../.claude-plugin/marketplace.json`
- `ea-assistant/README.md`
- `ea-assistant/docs/PRD.md`
- `ea-assistant/CLAUDE.md`
- `ea-assistant/skills/*/SKILL.md`

**Approach:**
- Bump `version` in `plugin.json` from `0.9.84` → `0.9.85`; add “Business Rules Register (BR-NNN) and Business Services Register (SVC-NNN)” to the description.
- Copy the exact same description and version into `marketplace.json`.
- Add a new `## v0.9.85 — Business Rules & Business Services` section to `docs/PRD.md` summarising the change, files touched, and design decisions.
- Add feature bullets and command rows for `/ea-rules` and `/ea-services` in `README.md`.
- Update `CLAUDE.md` version pointer, command count, ID scheme table, and command reference.
- Bump the `version:` frontmatter field in every `ea-assistant/skills/*/SKILL.md` to `0.9.85`.

**Verification:**
- `python -m json.tool` on both JSON files passes.
- `grep -F "0.9.85" plugin.json marketplace.json` returns both.
- `grep -F "0.9.85" skills/*/SKILL.md | wc -l` matches the number of skill files.

---

### U10. Verification and PR

**Goal:** Land the change cleanly.

**Requirements:** R14.

**Files:** All touched files.

**Approach:**
- Create branch `feat/business-rules-services` from `main`.
- Run `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/` and fix any issues.
- Run `git diff --stat` to confirm no unintended files changed.
- Commit with conventional commits, e.g. `feat(ea-assistant): add business rules and business services registers (v0.9.85)`.
- Open PR via `gh pr create` with a clear summary, test plan, and the verification checklist.

**Verification:**
- Frontmatter validator passes.
- JSON parse of `plugin.json` and `marketplace.json` passes.
- PR created and checks running.

---

## Verification Contract

1. **Frontmatter validation:** Run `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/` and confirm zero errors. This is the primary quality gate for any command/skill/agent/template change.

2. **JSON integrity:** Run `python -m json.tool` on `ea-assistant/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.

3. **Concept reference integrity:** Confirm `ea-concepts.md` defines Business Rule and Business Service without inline redefinition elsewhere; confirm `BR-NNN` appears in `ea-assistant/CLAUDE.md` ID scheme table.

4. **Command and skill wiring:** Confirm `commands/ea-rules.md` and `commands/ea-services.md` load their respective skills and declare all six modes.

5. **Template wiring:** Confirm `templates/cross-cutting/business-rules-register.md` and `business-services-register.md` exist, have valid YAML frontmatter with `taxonomy`, and are referenced by the skills.

6. **Runtime smoke test (after install or in a throwaway worktree):**
  - `/ea-new test-rules-services-2026`
  - `/ea-rules add` → capture one rule, verify `BR-001` appears in `engagement.json → rules[]`.
  - `/ea-services add` → capture one business service, verify `SVC-001` with `level: Business` appears in `engagement.json → services[]`.
  - `/ea-rules generate` and `/ea-services generate` → verify register files are written, archived if regenerated, and registered in `engagement.json → artifacts[]`.
  - `/ea-help` → verify both commands appear in the table.

7. **Version consistency:** Confirm `plugin.json`, `marketplace.json`, all skill frontmatters, `docs/PRD.md`, and `CLAUDE.md` all reference `0.9.85` and that plugin/marketplace descriptions match byte-for-byte.

---

## Definition of Done

- [ ] U1 complete: `ea-concepts.md` and `ea-assistant/CLAUDE.md` updated with Business Rule and Business Service definitions plus `BR-NNN` ID.
- [ ] U2 complete: `engagement.json` schema, seed template, and `/ea-migrate` backfill include `rules[]` and `services[]`.
- [ ] U3 complete: `skills/ea-business-rules-management/SKILL.md` written and follows register-protocol.
- [ ] U4 complete: `skills/ea-business-services-management/SKILL.md` written and follows register-protocol.
- [ ] U5 complete: `commands/ea-rules.md` and `commands/ea-services.md` written with all modes.
- [ ] U6 complete: register seed templates and `cross-cutting-index.md` updated; `item-detail.md` guidance covers BR/SVC.
- [ ] U7 complete: `matrix-catalogue.md` includes `business-rule-service` and `capability-service` matrices.
- [ ] U8 complete: `ea-help.md`, `ea-meta.md`, and `ea-status.md` surface rules/services counts.
- [ ] U9 complete: README, PRD, CLAUDE, plugin.json, marketplace.json updated; version bumped to `0.9.85` everywhere; skill versions aligned.
- [ ] U10 complete: frontmatter validation passes; JSON parses; branch `feat/business-rules-services` pushed and PR opened.
- [ ] No placeholder rows remain in templates after generation; no unintended files changed; no inline concept definitions outside `ea-concepts.md`.

---

## Appendix A — Proposed `engagement.json` entry schemas

### `rules[]` entry

```json
{
  "id": "BR-001",
  "statement": "A customer must be verified before a high-value claim is approved.",
  "type": "Obligation",
  "category": "Operative",
  "subject": "Customer identity verification",
  "condition": "Claim value exceeds $10,000",
  "directive": "Must complete identity verification",
  "outcome": "Claim approval is blocked until verification is complete",
  "authority": "Fraud Control Policy POL-004",
  "enforcement": "System-enforced in claims workflow; audited monthly",
  "owner": "Head of Fraud Control",
  "status": "Approved",
  "phase": "B",
  "reviewCycle": "2027-01-15",
  "linkedPolicies": ["POL-004"],
  "linkedConstraints": ["CST-002"],
  "linkedServices": ["SVC-003"],
  "linkedRequirements": ["REQ-012"]
}
```

### `services[]` entry

```json
{
  "id": "SVC-001",
  "name": "Claims Settlement",
  "level": "Business",
  "owner": "Claims Operations Director",
  "valueProposition": "Settle eligible claims within 5 business days",
  "consumers": ["Policyholder", "Claims Agent"],
  "outcomes": ["Claim resolved", "Payment issued"],
  "inputs": ["Claim request", "Supporting documents"],
  "outputs": ["Settlement decision", "Payment confirmation"],
  "interfaces": ["IFC-001"],
  "slas": ["MET-005"],
  "applicableRules": ["BR-001", "BR-007"],
  "realisedBy": ["CAP-003", "ABB-002"],
  "linkedRequirements": ["REQ-012", "REQ-013"],
  "status": "Operational",
  "phase": "B"
}
```
