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
