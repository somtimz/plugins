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
