---
name: ea-requirements
description: Manage architecture requirements — capture, view, sync from repo, and trace to artifacts
argument-hint: "[list|add|sync|trace]"
allowed-tools: [Read, Write, Bash]
---

Manage architecture requirements for the active engagement.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

Delegate detailed requirements management to the `ea-requirements-management` skill.

---

### Mode: `list` (default)

Display all requirements from `requirements/requirements.md` with a Scope column. Prefix Enterprise requirement IDs with 🔒:

```
Architecture Requirements — Acme Retail Transformation
═══════════════════════════════════════════════════════════════════
ID         Scope       Priority  Status    Title
───────────────────────────────────────────────────────────────────
🔒REQ-001  Enterprise  High      Approved  Omnichannel capability
🔒REQ-002  Enterprise  High      Draft     Real-time inventory sync
  REQ-003  Program     Medium    Draft     Customer data privacy (GDPR)
  REQ-004  Program     Low       Deferred  Legacy system decommission
═══════════════════════════════════════════════════════════════════
4 requirements (1 Approved, 2 Draft, 1 Deferred) | 2 Enterprise 🔒, 2 Program
```

**Subcommand variants:**
- `list enterprise` — show only Enterprise-scoped requirements
- `list program` — show only Program-scoped requirements
- `list enterprise waived` — combine scope and status filters (any valid status value accepted)

Offer: add a requirement, sync from repo, view traceability.

---

### Mode: `add`

1. Ask for:
   - Requirement statement (required)
   - Category: Functional / Non-Functional / Principle
     - **Deprecated:** `Constraint` category is deprecated for new capture. Use `/ea-constraints add` to create standalone constraints with `CST-NNN` IDs. Legacy `category: Constraint` rows remain valid for backward compatibility.
   - Priority: High / Medium / Low
   - Source: stakeholder name or document reference
   - ADM phase relevance
2. **If Category = Non-Functional**, ask additional NFR fields:
   - "NFR Sub-Type? (Performance / Reliability / Availability / Usability / Security / Maintainability / Portability / Compatibility / Recoverability)"
   - "Measurable Target? Enter the quantifiable threshold (e.g. 99.9% availability, RTO 4h, <200ms p95 response time). Press Enter to skip."
     - If skipped: mark `⚠️ Not answered` and warn: "NFRs without measurable targets cannot be verified during implementation — consider adding one before setting status to Approved."
   - Populate `nfrSubType` and `measurableTarget` in `requirements-index.json`
3. Ask: "Is this an **Enterprise** (organisation-wide standard or policy) or **Program** (specific to this engagement) requirement?"
   - If **Enterprise**: source field is mandatory. Display notice: "Enterprise requirements have read-only content fields. Only status, linked artifacts, and waiver justification can be updated after adding."
   - If **Program**: ask (optional): "Does this requirement derive from an existing Enterprise requirement? Enter an Enterprise REQ ID or press Enter to skip." If an ID is provided, validate it exists and is Enterprise-scoped — warn if not, but do not block.
4. Generate next ID (REQ-{NNN})
5. Apply Zachman classification (offer default or ask)
6. Add to `requirements.md` and `requirements-index.json` with `scope` and (if applicable) `derivedFrom` populated
7. Set status to `Draft`

**Waived status (any requirement edit):** When setting status to `Waived` on an Enterprise requirement, enforce non-empty `waiverJustification`. Prompt: "A waiver justification is required for Enterprise requirements. Please enter the justification." Do not write until provided.

---

### Mode: `sync`

1. Read `requirementsRepoPath` from `engagement.json`
2. If path is empty, ask user to provide it and offer to save to `.claude/ea-assistant.local.md`
3. Delegate to the `ea-requirements-management` skill for the full sync workflow
4. Handle mixed formats: `.md`, `.docx`, `.xlsx`, `.csv`
5. Present extracted requirements for user confirmation before writing
6. All imported records are automatically tagged `scope: "Enterprise"`. Existing Enterprise records' `status`, `linkedArtifacts`, and `waiverJustification` are never overwritten during re-sync.
7. Report sync summary: added, updated, conflicts, scope reclassifications (Program → Enterprise)

---

### Mode: `trace`

1. Generate a traceability matrix grouped by scope — Enterprise requirements first, Program requirements second:

```
Requirements Traceability Matrix
══════════════════════════════════════════════════════════════════
── Enterprise Requirements ────────────────────────────────────────
Req ID     | Title               | Arch Vision | Biz Arch | App Arch
🔒REQ-001  | Omnichannel cap.    | ✅          | ✅        | ⬜
🔒REQ-002  | Real-time inventory | ⬜          | ✅        | ⬜

── Program Requirements ───────────────────────────────────────────
Req ID     | Title               | Derives From | Arch Vision | Biz Arch | App Arch
REQ-003    | GDPR compliance     | —            | ✅          | ⬜        | ⬜
══════════════════════════════════════════════════════════════════
Legend: ✅ Addressed | ⚠️ Partial | ⬜ Not addressed | 🚫 Waived
⚠️  2 requirements have no artifact coverage
```

Waived Enterprise requirements show 🚫 in all artifact cells (the waiver itself is the coverage action).

2. Flag requirements with no artifact linkage (Waived requirements are excluded from untraced count)
3. Offer to link a requirement to an artifact
4. For the full interactive traceability explorer across the motivation chain (Driver → Goal → Strategy → Requirement → Capability → Work Package, with gap detection and contradictions), run `/ea-trace`.
