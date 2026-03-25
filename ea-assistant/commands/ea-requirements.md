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
- `list corporate` — show only Corporate-scoped requirements
- `list project` — show only Project-scoped requirements
- `list corporate waived` — combine scope and status filters (any valid status value accepted)

Offer: add a requirement, sync from repo, view traceability.

---

### Mode: `add`

1. Ask for:
   - Requirement statement (required)
   - Category: Functional / Non-Functional / Constraint / Principle
   - Priority: High / Medium / Low
   - Source: stakeholder name or document reference
   - ADM phase relevance
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
