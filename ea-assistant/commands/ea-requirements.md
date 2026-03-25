---
name: ea-requirements
description: Manage architecture requirements, principles, policies, and standards — capture, view, sync from repo, and trace to artifacts
argument-hint: "[list|add|sync|trace|principles|policies|standards]"
allowed-tools: [Read, Write, Bash]
---

Manage architecture requirements, principles, policies, and standards for the active engagement.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

Delegate detailed requirements management to the `ea-requirements-management` skill.

---

### Mode: `list` (default)

Display all requirements from `requirements/requirements.md` with a Scope column. Prefix Corporate requirement IDs with 🔒:

```
Architecture Requirements — Acme Retail Transformation
═══════════════════════════════════════════════════════════════════
ID         Scope      Priority  Status    Title
───────────────────────────────────────────────────────────────────
🔒REQ-001  Corporate  High      Approved  Omnichannel capability
🔒REQ-002  Corporate  High      Draft     Real-time inventory sync
  REQ-003  Project    Medium    Draft     Customer data privacy (GDPR)
  REQ-004  Project    Low       Deferred  Legacy system decommission
═══════════════════════════════════════════════════════════════════
4 requirements (1 Approved, 2 Draft, 1 Deferred) | 2 Corporate 🔒, 2 Project
```

**Subcommand variants:**
- `list corporate` — show only Corporate-scoped items
- `list project` — show only Project-scoped items
- `list principles` — show only category `Principle` (see Mode: `principles`)
- `list policies` — show only category `Policy` (see Mode: `policies`)
- `list standards` — show only category `Standard` (see Mode: `standards`)
- `list corporate waived` — combine scope and status filters (any valid status value accepted)

Offer: add a requirement, sync from repo, view traceability, view principles, view policies, view standards.

---

### Mode: `principles` (alias: `list principles`)

Display only requirements with `category: "Principle"`, grouped by scope (Corporate first):

```
Architecture Principles — Acme Retail Transformation
═══════════════════════════════════════════════════════════════════
ID         Scope      Priority  Status    Statement
───────────────────────────────────────────────────────────────────
🔒REQ-005  Corporate  High      Approved  Single source of truth for all master data
  REQ-007  Project    Medium    Draft     All integrations use published APIs
═══════════════════════════════════════════════════════════════════
2 principles (1 Approved, 1 Draft) | 1 Corporate 🔒, 1 Project
```

For each principle, display its full **rationale** and **implications** fields below the table (stored in the requirement's `description` field using the sub-structure `Rationale: … / Implications: …`).

Offer: add a principle, or switch to full requirements list.

---

### Mode: `policies` (alias: `list policies`)

Display only requirements with `category: "Policy"`, grouped by scope (Corporate first):

```
Organisation Policies — Acme Retail Transformation
═══════════════════════════════════════════════════════════════════
ID         Scope      Priority  Status    Title
───────────────────────────────────────────────────────────────────
🔒REQ-008  Corporate  High      Approved  Data Retention Policy
🔒REQ-009  Corporate  High      Approved  Cloud Hosting Approval Policy
  REQ-011  Project    Medium    Draft     Vendor Onboarding Policy
═══════════════════════════════════════════════════════════════════
3 policies (2 Approved, 1 Draft) | 2 Corporate 🔒, 1 Project
```

For each policy, display its full **statement**, **owner**, **effective date**, and **enforcement** fields below the table (stored in the requirement's `description` field using `Owner: … / Effective: … / Enforcement: …`).

Offer: add a policy, or switch to full requirements list.

---

### Mode: `standards` (alias: `list standards`)

Display only requirements with `category: "Standard"`, grouped by scope (Corporate first):

```
Architecture Standards — Acme Retail Transformation
═══════════════════════════════════════════════════════════════════
ID         Scope      Priority  Status    Title
───────────────────────────────────────────────────────────────────
🔒REQ-010  Corporate  High      Approved  REST API Design Standard v2.1
🔒REQ-012  Corporate  High      Approved  ISO 27001:2022 Information Security
  REQ-013  Project    Medium    Draft     Microservices Deployment Standard
═══════════════════════════════════════════════════════════════════
3 standards (2 Approved, 1 Draft) | 2 Corporate 🔒, 1 Project
```

For each standard, display its full **statement**, **version**, **domain**, and **enforcement** fields below the table (stored in the requirement's `description` field using `Version: … / Domain: … / Enforcement: …`).

Offer: add a standard, or switch to full requirements list.

---

### Mode: `add`

1. Ask for:
   - Title (required)
   - Category: Functional / Non-Functional / Constraint / Principle / Policy / Standard
   - Priority: High / Medium / Low
   - Source: stakeholder name or document reference
   - ADM phase relevance

   **If category is `Principle`**, ask two additional fields:
   - **Rationale** — why this principle exists; what risk or problem it prevents
   - **Implications** — what the principle means for design decisions in practice
   Store in `description` as: `Rationale: {text}\n\nImplications: {text}`

   **If category is `Policy`**, ask three additional fields:
   - **Owner** — team or role responsible for the policy (e.g., CISO, CTO Office)
   - **Effective date** — when the policy came into force (YYYY-MM-DD or "TBD")
   - **Enforcement** — `Mandatory` or `Advisory`
   Store in `description` as: `Owner: {text} / Effective: {date} / Enforcement: {value}`

   **If category is `Standard`**, ask three additional fields:
   - **Version** — version or edition of the standard (e.g., "v2.1", "2022", "TBD")
   - **Domain** — `Business` / `Data` / `Application` / `Technology` / `Cross-cutting`
   - **Enforcement** — `Mandatory` or `Advisory`
   Store in `description` as: `Version: {text} / Domain: {value} / Enforcement: {value}`
2. Ask: "Is this a **Corporate** (enterprise-wide standard or policy) or **Project** (specific to this engagement) requirement?"
   - If **Corporate**: source field is mandatory. Display notice: "Corporate requirements have read-only content fields. Only status, linked artifacts, and waiver justification can be updated after adding."
   - If **Project**: ask (optional): "Does this requirement derive from an existing Corporate requirement? Enter a Corporate REQ ID or press Enter to skip." If an ID is provided, validate it exists and is Corporate-scoped — warn if not, but do not block.
3. Generate next ID (REQ-{NNN})
4. Apply Zachman classification (offer default or ask)
5. Add to `requirements.md` and `requirements-index.json` with `scope` and (if applicable) `derivedFrom` populated
6. Set status to `Draft`

**Waived status (any requirement edit):** When setting status to `Waived` on a Corporate requirement, enforce non-empty `waiverJustification`. Prompt: "A waiver justification is required for Corporate requirements. Please enter the justification." Do not write until provided.

---

### Mode: `sync`

1. Read `requirementsRepoPath` from `engagement.json`
2. If path is empty, ask user to provide it and offer to save to `.claude/ea-assistant.local.md`
3. Delegate to the `ea-requirements-management` skill for the full sync workflow
4. Handle mixed formats: `.md`, `.docx`, `.xlsx`, `.csv`
5. Present extracted requirements for user confirmation before writing
6. All imported records are automatically tagged `scope: "Corporate"`. Existing Corporate records' `status`, `linkedArtifacts`, and `waiverJustification` are never overwritten during re-sync.
7. Report sync summary: added, updated, conflicts, scope reclassifications (Project → Corporate)

---

### Mode: `trace`

1. Generate a traceability matrix grouped by scope — Corporate requirements first, Project requirements second:

```
Requirements Traceability Matrix
══════════════════════════════════════════════════════════════════
── Corporate Requirements ─────────────────────────────────────────
Req ID     | Title               | Arch Vision | Biz Arch | App Arch
🔒REQ-001  | Omnichannel cap.    | ✅          | ✅        | ⬜
🔒REQ-002  | Real-time inventory | ⬜          | ✅        | ⬜

── Project Requirements ───────────────────────────────────────────
Req ID     | Title               | Derives From | Arch Vision | Biz Arch | App Arch
REQ-003    | GDPR compliance     | —            | ✅          | ⬜        | ⬜
══════════════════════════════════════════════════════════════════
Legend: ✅ Addressed | ⚠️ Partial | ⬜ Not addressed | 🚫 Waived
⚠️  2 requirements have no artifact coverage
```

Waived Corporate requirements show 🚫 in all artifact cells (the waiver itself is the coverage action).

2. Flag requirements with no artifact linkage (Waived requirements are excluded from untraced count)
3. Offer to link a requirement to an artifact
