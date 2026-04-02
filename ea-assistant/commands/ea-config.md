---
name: ea-config
description: Configure EA Assistant plugin settings and engagement rules
argument-hint: "[settings|rules|optouts|refresh]"
allowed-tools: [Read, Write, Bash]
---

Configure EA Assistant plugin settings, engagement rules, opt-outs, and refresh the engagement pointer doc.

## Instructions

## Engagement Resolution

Used by Sections 2, 3, and 4. Run this logic whenever a section requires an active engagement:

1. Check whether `EA-projects/` exists. If not, display:
   ```
   No EA-projects directory found. Run `/ea-new` to create your first engagement.
   ```
   Then stop.

2. Scan `EA-projects/*/engagement.json` for all files.

3. If exactly one engagement is found: use it silently and continue.

4. If multiple engagements are found: display a numbered list and ask the user to select:
   ```
   Multiple engagements found:
     1. acme-retail-transformation-2026
     2. finance-modernisation-2026
   Select engagement:
   ```
   Wait for selection; use the chosen slug for the remainder of the section.

5. If no engagements are found: display:
   ```
   No engagements found. Run `/ea-new` to create one.
   ```
   Then stop.

## Dispatcher

When this command runs:

1. Read the argument (if any).

2. If an argument is provided, dispatch directly:
   - `settings` → jump to Section 1
   - `rules` → run Engagement Resolution, then jump to Section 2
   - `optouts` → run Engagement Resolution, then jump to Section 3
   - `refresh` → run Engagement Resolution, then jump to Section 4
   - Anything else → display: `Unknown section "{arg}". Valid options: settings, rules, optouts, refresh.` and stop.

3. If no argument is provided, display the menu:
   ```
   EA Assistant Configuration

   1. Plugin settings     (.claude/ea-assistant.local.md)
   2. Engagement rules    (EA-projects/{slug}/.claude/rules/ea-engagement.md)
   3. Opt-out management  (EA-projects/{slug}/engagement.json)
   4. Refresh CLAUDE.md   (EA-projects/{slug}/CLAUDE.md)

   Select a section (1–4), or press Enter to exit:
   ```
   Wait for input.
   - `1` → Section 1
   - `2` → run Engagement Resolution, then Section 2
   - `3` → run Engagement Resolution, then Section 3
   - `4` → run Engagement Resolution, then Section 4
   - Empty / Enter → exit with no output

4. After completing any section, return to the menu (unless the user chose a direct subcommand).

## Section 1 — Plugin Settings

**File:** `.claude/ea-assistant.local.md`

**Settings schema:**

| Key | Default | Allowed values |
|---|---|---|
| `facilitatorStyle` | `patient` | `patient`, `direct`, `executive` |
| `audienceLevel` | `mixed` | `executive`, `architect`, `technical`, `mixed` |
| `requireConfirmBeforeRecord` | `false` | `true`, `false` |
| `researchPrompts` | `true` | `true`, `false` |
| `sessionSummary` | `true` | `true`, `false` |
| `requirementsRepoPath` | *(empty)* | any filesystem path |

**File format:** plain text `key: value` lines (not strict YAML). Each setting on its own line. Preserve any comment lines (`#`) on read; write only key-value lines back.

**Flow:**

1. Attempt to read `.claude/ea-assistant.local.md`. If missing, treat all values as their defaults.

2. Parse each `key: value` line. For `requirementsRepoPath`, treat a missing or blank value as `(not set)`.

3. Display the current settings:
   ```
   Plugin Settings — .claude/ea-assistant.local.md

     facilitatorStyle            {value}     (patient | direct | executive)
     audienceLevel               {value}     (executive | architect | technical | mixed)
     requireConfirmBeforeRecord  {value}     (true | false)
     researchPrompts             {value}     (true | false)
     sessionSummary              {value}     (true | false)
     requirementsRepoPath        {value}     (any path)

   Say "set <key> to <value>" to change a setting, or Enter to go back.
   ```

4. Wait for input.

5. On `set <key> to <value>`:
   - If `key` is not in the schema: display `Unknown setting "{key}". Valid settings: facilitatorStyle, audienceLevel, requireConfirmBeforeRecord, researchPrompts, sessionSummary, requirementsRepoPath.` and re-prompt.
   - If `value` is not in the allowed values for the key (for enum settings): display `Invalid value "{value}" for {key}. Allowed: {list}.` and re-prompt.
   - Otherwise: update the in-memory value, write all six settings to `.claude/ea-assistant.local.md` (overwrite), and confirm: `✓ {key} updated to "{value}"`
   - Loop — redisplay settings and re-prompt.

6. On empty input: return to the caller (menu or exit).

7. **File write format** — always write in this exact structure (preserves comments from the README):
   ```
   # EA Assistant — local plugin settings
   # See ea-assistant/README.md for documentation.

   facilitatorStyle: {value}
   audienceLevel: {value}
   requireConfirmBeforeRecord: {value}
   researchPrompts: {value}
   sessionSummary: {value}
   requirementsRepoPath: {value}
   ```
   If `requirementsRepoPath` has no value, write `requirementsRepoPath: ` (key present, empty value — do not omit the line).

## Section 2 — Engagement Rules

**File:** `EA-projects/{slug}/.claude/rules/ea-engagement.md`

The seeded boilerplate (Session Start, Artifacts, Concepts and References, IDs sections) is system-managed and must never be altered. Custom rules live in a `## Custom Rules` section at the end of the file.

**Flow:**

1. Read `EA-projects/{slug}/.claude/rules/ea-engagement.md`. If the file does not exist, display:
   ```
   Engagement rules file not found for {slug}.
   Run `/ea-new` or `/ea-migrate` to create it.
   ```
   Then return to the caller.

2. Locate the `## Custom Rules` section. If it does not exist, treat the custom rules list as empty. Do not display or allow editing of the boilerplate sections above it.

3. Display the custom rules list:
   ```
   Engagement Rules — {slug}

   Custom rules:
     1. {rule text}
     2. {rule text}
     (none)   ← if list is empty

   Say "add: <rule in your words>" to add a rule,
   "remove <N>" to remove a rule, or Enter to go back.
   ```

4. **Add flow** — on input starting with `add:`:
   a. Extract the text after `add:` and trim whitespace.
   b. Infer and rewrite it as a clean, imperative rule in the same style as the boilerplate rules (e.g. "Always validate data artifacts against GDPR Article 30 requirements before marking Approved"). The inferred rule should be a single sentence, begin with an imperative verb, and be unambiguous.
   c. Confirm with the user:
      ```
      Add this rule?
        → "{inferred rule}"
      (y / edit / n):
      ```
   d. On `y`: append the rule to the `## Custom Rules` section, write the file, confirm `✓ Rule added`, redisplay the list.
   e. On `edit`: ask "Enter your preferred wording:" — accept revised text, go back to step (c).
   f. On `n`: discard, re-prompt.

5. **Remove flow** — on input `remove <N>`:
   a. Confirm: `Remove rule {N}: "{rule text}"? (y/n)`
   b. On `y`: remove the entry from the list, rewrite the `## Custom Rules` section, write the file, confirm `✓ Rule removed`, redisplay the list.
   c. On `n`: re-prompt.

6. **File write rule:** When writing, preserve the boilerplate sections exactly as-is. Replace only the `## Custom Rules` section (or append it if absent). The `## Custom Rules` section format:
   ```markdown
   ## Custom Rules

   - {rule 1}
   - {rule 2}
   ```
   If the list is empty after a removal, write the section with just the heading and no bullets.

7. On empty input: return to the caller.

## Section 3 — Opt-Out Management

**Source:** `EA-projects/{slug}/engagement.json → optOuts[]`

**Note:** This section intentionally allows removal of opt-out entries. This overrides the append-only rule in `ea-engagement-lifecycle/SKILL.md`, which applies to the interviewer agent only. `/ea-config` is the designated administrative interface for correcting opt-outs.

**Flow:**

1. Read `EA-projects/{slug}/engagement.json`. If unreadable, display:
   ```
   Could not read engagement.json for {slug}: {error}
   ```
   Then return to the caller.

2. Extract `optOuts[]`. If the key is missing, treat it as an empty array.

3. If the list is empty, display:
   ```
   Opt-Out Management — {slug}

   No opt-outs recorded for this engagement.
   ```
   Then return to the caller.

4. Display the opt-outs:
   ```
   Opt-Out Management — {slug}

     1. {artifactId} / {questionRef or "—"}
        Reason: "{reason or (none)}"
        Added:  {timestamp}

     2. ...

   Say "remove <N>" to remove an opt-out, or Enter to go back.
   ```

5. **Remove flow** — on input `remove <N>`:
   a. Validate N is in range. If not, display `No opt-out #{N}.` and re-prompt.
   b. Confirm: `Remove opt-out for "{artifactId} / {questionRef}"? (y/n)`
   c. On `y`:
      - Read `engagement.json` fresh (do not use the in-memory copy).
      - Splice the entry at index N-1 from `optOuts[]`.
      - Update `lastModified` to the current ISO 8601 timestamp.
      - Write `engagement.json`.
      - Confirm `✓ Opt-out removed`, redisplay updated list.
   d. On `n`: re-prompt.

6. On empty input: return to the caller.
