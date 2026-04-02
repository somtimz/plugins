# /ea-config Command Design

**Date:** 2026-04-02
**Plugin:** ea-assistant
**File to create:** `ea-assistant/commands/ea-config.md`

---

## Overview

A single command that exposes four configuration sections for EA Assistant. Supports both a guided menu (bare invocation) and direct subcommands for power users.

---

## Command File

- **Path:** `ea-assistant/commands/ea-config.md`
- **Frontmatter:**
  - `name: ea-config`
  - `description: Configure EA Assistant plugin settings and engagement rules`
  - `allowed-tools: [Read, Write, Bash]`

---

## Invocation Modes

| Invocation | Behaviour |
|---|---|
| `/ea-config` | Show numbered menu of all sections |
| `/ea-config settings` | Jump directly to plugin settings |
| `/ea-config rules` | Jump directly to engagement rules |
| `/ea-config optouts` | Jump directly to opt-out management |
| `/ea-config refresh` | Regenerate engagement CLAUDE.md immediately |

---

## Menu (bare invocation)

```
EA Assistant Configuration

1. Plugin settings     (.claude/ea-assistant.local.md)
2. Engagement rules    (EA-projects/{slug}/.claude/rules/ea-engagement.md)
3. Opt-out management  (EA-projects/{slug}/engagement.json)
4. Refresh CLAUDE.md   (EA-projects/{slug}/CLAUDE.md)

Select a section (or press Enter to exit):
```

---

## Engagement Resolution (sections 2, 3, 4)

Applies to any section that requires an active engagement:

1. Scan `EA-projects/` for subdirectories containing `engagement.json`
2. If exactly one found: use it silently
3. If multiple found: display a numbered list and ask the user to select
4. If none found: display "No engagements found. Run `/ea-new` to create one." and exit

---

## Section 1 — Plugin Settings

**File:** `.claude/ea-assistant.local.md` (created with defaults if missing)

**File format:** plain text `key: value` lines (not strict YAML). Each setting on its own line. Comments (`#`) are preserved on read but the command writes only key-value lines.

**Settings schema:**

| Key | Default | Allowed values |
|---|---|---|
| `facilitatorStyle` | `patient` | `patient`, `direct`, `executive` |
| `audienceLevel` | `mixed` | `executive`, `architect`, `technical`, `mixed` |
| `requireConfirmBeforeRecord` | `false` | `true`, `false` |
| `researchPrompts` | `true` | `true`, `false` |
| `sessionSummary` | `true` | `true`, `false` |
| `requirementsRepoPath` | *(empty)* | any path |

**Display format:**
```
Plugin Settings — .claude/ea-assistant.local.md

  facilitatorStyle            patient     (patient | direct | executive)
  audienceLevel               mixed       (executive | architect | technical | mixed)
  requireConfirmBeforeRecord  false       (true | false)
  researchPrompts             true        (true | false)
  sessionSummary              true        (true | false)
  requirementsRepoPath        (not set)   (any path)

Say "set <key> to <value>" to change a setting, or Enter to go back.
```

**Edit flow:**
1. Accept freeform input: `set facilitatorStyle to direct`
2. Parse key and value; validate against allowed values
3. If invalid: show allowed values and re-prompt
4. Write updated value to file
5. Confirm: `✓ facilitatorStyle updated to "direct"`
6. Loop — allow multiple changes in one session

---

## Section 2 — Engagement Rules

**File:** `EA-projects/{slug}/.claude/rules/ea-engagement.md`

**Display format:**
```
Engagement Rules — {slug}

Current custom rules:
  1. Always use ArchiMate notation for all layer diagrams
  2. This organisation uses SAFe — map phases to PI Planning cycles

Say "add: <rule in your words>" to add a rule,
"remove <N>" to remove a rule,
or Enter to go back.
```

**Add flow:**
1. Accept freeform input after `add:` prefix
2. Infer intent and rewrite as a clean, imperative rule in the same style as the boilerplate
3. Show inferred rule: `Add this rule? → "Always validate data artifacts against GDPR Article 30 requirements before marking Approved" (y/edit/n)`
4. On `y`: append to the custom rules section of `ea-engagement.md`
5. On `edit`: accept revised wording and confirm again
6. On `n`: discard

**Remove flow:**
1. `remove <N>` — confirm: `Remove rule N: "<text>"? (y/n)`
2. On `y`: remove entry, rewrite file, confirm `✓ Rule removed`

**File structure:** preserve the seeded boilerplate block; custom rules live in a clearly delimited `## Custom Rules` section appended after the boilerplate. If the section doesn't exist yet, create it on first add.

---

## Section 3 — Opt-Out Management

**Source:** `EA-projects/{slug}/engagement.json → optOuts[]`

**Display format:**
```
Opt-Out Management — {slug}

  1. architecture-vision / executive_summary
     Reason: "Not yet available — revisit in Phase A review"
     Added:  2026-03-15T10:22:00Z

  2. business-architecture / stakeholder_analysis
     Reason: ""
     Added:  2026-03-20T14:05:00Z

Say "remove <N>" to remove an opt-out, or Enter to go back.
```

**Remove flow:**
1. `remove <N>` — confirm: `Remove opt-out for "<artifactId> / <questionRef>"? (y/n)`
2. On `y`: splice entry from `optOuts[]`, write `engagement.json`, confirm `✓ Opt-out removed`

**Empty state:** "No opt-outs recorded for this engagement."

**Note:** Removal intentionally overrides the append-only rule in `ea-engagement-lifecycle/SKILL.md`, which applies to the interviewer agent only. `/ea-config` is the designated administrative interface for opt-out correction.

---

## Section 4 — Refresh CLAUDE.md

**File:** `EA-projects/{slug}/CLAUDE.md`

**Flow:**
1. Resolve engagement
2. Read `engagement.json`
3. Regenerate `CLAUDE.md` using the Project CLAUDE.md template (same template used by `/ea-new` and `/ea-open`)
4. Write file and confirm: `✓ CLAUDE.md refreshed for {slug}`

**Use cases:** after manual edits to `engagement.json`, after `/ea-migrate`, or any time the pointer doc is stale without needing the full `/ea-open` flow.

---

## Error Handling

| Condition | Behaviour |
|---|---|
| `.claude/ea-assistant.local.md` missing | Create with all defaults on first write |
| `ea-engagement.md` missing | Display error: "Engagement rules file not found. Run `/ea-new` or `/ea-migrate` to create it." |
| Invalid setting value | Show allowed values, re-prompt |
| `engagement.json` unreadable | Display parse error and exit section |
| No `optOuts[]` key in JSON | Treat as empty array |
| `EA-projects/` directory missing | Display "No EA-projects directory found. Run `/ea-new` to create your first engagement." and exit |

---

## Out of Scope

- Global/cross-engagement rule management (future)
- Editing `engagement.json` fields other than `optOuts[]` (use `/ea-open` for that)
- Managing plugin version or migration state (use `/ea-migrate`)
