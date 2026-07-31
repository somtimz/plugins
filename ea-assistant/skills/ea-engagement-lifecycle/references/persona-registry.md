# Persona Registry

Single source of truth for **persona-based tailoring** of EA Assistant. A persona is a stakeholder role with a characteristic set of interests, a relevant command subset, a report bundle, and an entry workflow. This data drives the `--persona <role>` flag on `/ea-help` (filtered menu + workflow) and `/ea-publish` (scoped report bundle). Adding or changing a persona is a data edit here — no command logic changes.

Personas build on the existing `audience` taxonomy (`skills/ea-artifact-templates/references/taxonomy.md`: Executive / Business / Architecture / Delivery / Governance) — each persona maps to one or more audience tags, and `/ea-publish --persona` filters artifacts by those tags. Do not invent a parallel audience scheme.

## Resolution

1. Match the `--persona` argument (case-insensitive) against each persona's **Key** or any **Alias**.
2. If no match, list the available personas (Key + one-line interest) and stop.
3. A persona may also be set as the engagement default via `defaultPersona:` in `.claude/rules/ea-local-config.md`; an explicit `--persona` flag overrides it. If neither is present, commands behave as today (no persona filter).

## How commands consume this

- **`/ea-help --persona <role>`** — print the persona's Interests and Suggested Workflow, then render the command table filtered to the persona's **Commands** (instead of the full 58-command table), followed by its **Report bundle**. Always end with: "Run `/ea-help` for the full command list."
- **`/ea-publish --persona <role>`** — pre-select artifacts whose `taxonomy.audience` is in the persona's **Audience** set (plus `All`), pre-tick the **Report bundle** items, and title the output "{Persona} Pack". The user can still adjust the selection.

---

## Personas

### Enterprise Architect
- **Key:** `enterprise-architect` · **Aliases:** ea, architect, chief-architect
- **Audience:** Architecture, All
- **Interests:** Cross-domain coherence, traceability, governance, decision quality, the whole ADM
- **Commands:** `/ea-status` · `/ea-engage-review` · `/ea-lens` · `/ea-consistency` · `/ea-trace` · `/ea-grill` · `/ea-decisions` · `/ea-adrs` · `/ea-strategies` · `/ea-matrix` · `/ea-operatingmodel`
- **Report bundle:** `/ea-publish --full`; `/ea-engage-review`; `/ea-lens`
- **Entry workflow:** Full ADM — Prelim → A → B (Business Context → Business Model Canvas → Business Architecture + Operating Model) → C → D → E/F → G/H; review with `/ea-engage-review` and `/ea-lens` at phase gates

### CIO
- **Key:** `cio` · **Aliases:** chief-information-officer, it-exec
- **Audience:** Executive
- **Interests:** Strategic alignment, cost and value (TCO/payback), roadmap delivery, risk posture, decisions requiring sponsor authority
- **Commands:** `/ea-status` · `/ea-brief` · `/ea-strategies` · `/ea-finance` · `/ea-goals` · `/ea-target` · `/ea-actions` · `/ea-risks` · `/ea-decisions` · `/ea-operatingmodel`
- **Report bundle:** `/ea-publish --executive`; `/ea-finance generate` (cost roll-up); `/ea-brief --focus strategy`; Business Case; Operating Model
- **Entry workflow:** Architecture Vision + Business Context → Strategy Map (`/ea-strategies trace`) → Business Model Canvas → Operating Model → Roadmap budget (`/ea-finance`) → Decisions/Risks

### CISO
- **Key:** `ciso` · **Aliases:** security, chief-information-security-officer, security-officer
- **Audience:** Governance
- **Interests:** Security posture, compliance coverage (SABSA/ISO 27001/NIST CSF), risk, policy and constraint enforcement
- **Commands:** `/ea-security-review` · `/ea-risks` · `/ea-constraints` · `/ea-policies` · `/ea-adrs` · `/ea-concerns` · `/ea-standards`
- **Report bundle:** `/ea-security-review`; Risk Register (`/ea-risks`); Policies & Constraints registers
- **Entry workflow:** `/ea-security-review` across phases → triage findings to Risks/Constraints/Policies → track security ADRs

### Chief Product Officer
- **Key:** `chief-product-officer` · **Aliases:** cpo-product, product, cpo
- **Audience:** Business, Executive
- **Interests:** Product value streams, business capabilities, customer outcomes, benefits realisation
- **Commands:** `/ea-goals` · `/ea-objectives` · `/ea-strategies` · `/ea-scenarios` · `/ea-stories` · `/ea-matrix` · `/ea-finance` · `/ea-operatingmodel`
- **Report bundle:** Business Architecture; Operating Model; Capability/Value-Stream matrices (`/ea-matrix`); Objectives & benefits (`/ea-objectives`, benefit metrics); `/ea-brief --focus strategy`
- **Entry workflow:** Business Context → Business Model Canvas → Phase B capabilities/value streams → Operating Model (channels, delivery) → Objectives/Metrics → benefits realisation (`/ea-finance` + benefit metrics)

> **CPO note:** `cpo` is ambiguous. This registry treats `chief-product-officer` and `chief-privacy-officer` as **two distinct personas**. The bare alias `cpo` resolves to Chief Product Officer; use `chief-privacy-officer` / `privacy` for the privacy role.

### Chief Privacy Officer
- **Key:** `chief-privacy-officer` · **Aliases:** privacy, dpo, data-protection-officer
- **Audience:** Governance
- **Interests:** Data privacy, regulatory compliance (GDPR and equivalents), data governance, consent and lawful basis, data residency
- **Commands:** `/ea-security-review` · `/ea-policies` · `/ea-constraints` · `/ea-standards` · `/ea-risks` · `/ea-principles`
- **Report bundle:** `/ea-security-review` (privacy lens); Data Architecture; Policies & Constraints; Standards Information Base (`/ea-standards`)
- **Entry workflow:** Data Architecture (Phase C-Data) → privacy policies/constraints → compliance standards → residual risks

### Business Architect
- **Key:** `business-architect` · **Aliases:** ba
- **Audience:** Business
- **Interests:** Business capabilities, value streams, processes, business drivers and goals, operating model
- **Commands:** `/ea-drivers` · `/ea-goals` · `/ea-objectives` · `/ea-strategies` · `/ea-scenarios` · `/ea-matrix` · `/ea-gaps` · `/ea-operatingmodel`
- **Report bundle:** Business Architecture; Operating Model; Business Model Canvas; Capability/Value-Stream matrices (`/ea-matrix`); business Gap Analysis
- **Entry workflow:** Phase B — Business Context → Business Model Canvas → drivers/goals → capabilities & value streams → operating model → business gaps → strategies that close them

### Data Architect
- **Key:** `data-architect` · **Aliases:** da
- **Audience:** Architecture
- **Interests:** Data domains, data principles, data quality, data gaps, data governance and lineage
- **Commands:** `/ea-principles` · `/ea-gaps` · `/ea-matrix` · `/ea-standards` · `/ea-constraints` · `/ea-trace`
- **Report bundle:** Data Architecture; Data Principles (`/ea-principles`); data Gap Analysis; App/Data CRUD matrix (`/ea-matrix`)
- **Entry workflow:** Phase C-Data — data architecture → data principles & standards → data gaps → CRUD/coverage matrices

---

## Extending

Add a new persona as a `### {Name}` block with the same fields (Key, Aliases, Audience, Interests, Commands, Report bundle, Entry workflow). Keep **Audience** values within the taxonomy's five tags so `/ea-publish --persona` filtering keeps working. No command edits are required — `/ea-help` and `/ea-publish` read this file at runtime.
