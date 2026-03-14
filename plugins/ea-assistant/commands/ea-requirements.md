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

Display all requirements from `requirements/requirements.md`:

```
Architecture Requirements — Acme Retail Transformation
═══════════════════════════════════════════════════════
ID       Priority  Status    Title
───────────────────────────────────────────────────────
REQ-001  High      Approved  Omnichannel capability
REQ-002  High      Draft     Real-time inventory sync
REQ-003  Medium    Draft     Customer data privacy (GDPR)
REQ-004  Low       Deferred  Legacy system decommission
═══════════════════════════════════════════════════════
4 requirements (1 Approved, 2 Draft, 1 Deferred)
```

Offer: add a requirement, sync from repo, view traceability.

---

### Mode: `add`

1. Ask for:
   - Requirement statement (required)
   - Category: Functional / Non-Functional / Constraint / Principle
   - Priority: High / Medium / Low
   - Source: stakeholder name or document reference
   - ADM phase relevance
2. Generate next ID (REQ-{NNN})
3. Apply Zachman classification (offer default or ask)
4. Add to `requirements.md` and `requirements-index.json`
5. Set status to `Draft`

---

### Mode: `sync`

1. Read `requirementsRepoPath` from `engagement.json`
2. If path is empty, ask user to provide it and offer to save to `.claude/ea-assistant.local.md`
3. Delegate to the `ea-requirements-management` skill for the full sync workflow
4. Handle mixed formats: `.md`, `.docx`, `.xlsx`, `.csv`
5. Present extracted requirements for user confirmation before writing
6. Report sync summary: added, updated, conflicts

---

### Mode: `trace`

1. Generate a traceability matrix:

```
Requirements Traceability Matrix
══════════════════════════════════════════════════════════
Req ID  | Title              | Arch Vision | Biz Arch | App Arch
REQ-001 | Omnichannel cap.   | ✅          | ✅        | ⬜
REQ-002 | Real-time inventory| ⬜          | ✅        | ⬜
REQ-003 | GDPR compliance    | ✅          | ⬜        | ⬜
══════════════════════════════════════════════════════════
⚠️  2 requirements have no artifact coverage
```

2. Flag requirements with no artifact linkage
3. Offer to link a requirement to an artifact
