---
name: ea-horizon
description: Manage the Technology Horizon Register (THR-NNN) in the shared Architecture Repository — add technologies to the radar, update ring placement, and track PoC evidence. Requires a linked Architecture Repository.
argument-hint: "[list|add|update|surface|link-adr] [THR-NNN] [--ring Adopt|Trial|Assess|Hold]"
allowed-tools: [Read, Write, Bash]
---

# /ea-horizon — Technology Horizon Register

Uses skill: `ea-architecture-repository` → `references/technology-horizon-schema.md`

Requires: Architecture Repository linked via `engagement.json → repoPath` or active session repo (`/ea-repo open`).

---

## Mode: `list [--ring <Adopt|Trial|Assess|Hold>]`

Display the Technology Horizon Register. Default shows all rings grouped by ring level. `--ring` filters to one ring.

Show: ID | Name | Category | Rationale | Linked ABBs | Review Date

---

## Mode: `add`

Interview to create a new THR entry:

1. Technology name
2. Category (Platform | Language | Framework | Pattern | Practice | Tool | Standard)
3. Initial ring (Adopt | Trial | Assess | Hold)
4. Rationale — one-line reason for ring placement
5. Linked ABBs: "Which ABBs could this technology implement? (Enter ABB-NNN IDs or press Enter to skip)"
6. Linked VDRs: "Are there vendors implementing this technology already in the register? (Enter VDR-NNN IDs or press Enter to skip)"
7. PoC evidence: "Is there a PoC document or research note? (Enter path to ResearchAndReferences/ item or press Enter to skip)"
8. Next review date (suggest 12 months from today)

Then:
1. Read `repo.json → technologyHorizon.nextId` to get the new ID
2. Write `Architecture-Repository/technology-horizon/entries/THR-NNN.md` with YAML frontmatter and body sections
3. Set `addedDate` to today, `addedBy` to current user if known
4. Update `repo.json → technologyHorizon.nextId` to nextId + 1
5. Append row to `Architecture-Repository/technology-horizon/horizon-index.md`
6. Update `technology-horizon-register.md` (add row to correct ring table, update Radar Summary counts)
7. Update `repo.json → lastModified`
8. Report: "✓ THR-NNN added: <name> [<ring>]"

---

## Mode: `update <THR-NNN>`

Load `Architecture-Repository/technology-horizon/entries/<THR-NNN>.md`. Present current values. Prompt for changes. If ring changes:
1. Confirm the ring change
2. Add entry to `ringHistory[]`: `{ date: today, from: old-ring, to: new-ring, reason: <user-provided> }`
3. Update `ring` and `rationale`
4. Move row between ring tables in `technology-horizon-register.md`, update Radar Summary counts
5. Add entry to Ring History table in `technology-horizon-register.md`

Always update `reviewDate` to a new date if user provides one. Write back to entry file.

---

## Mode: `surface [--phase <phase>]`

Show THR entries relevant to the current engagement's context:
- Filter to ring = Adopt or Trial
- If `--phase D` or when called from Phase D interview context: cross-reference with ABBs present in the engagement's Technology Architecture
- Output: summarised list of Adopt/Trial technologies with rationale and any linked ABBs matching the engagement

---

## Mode: `link-adr <THR-NNN> <ADR-NNN>`

Record that an ADR references a technology horizon entry:
1. Add `ADR-NNN` to `THR-NNN.md → linkedADRs[]`
2. Report: "✓ ADR-NNN linked to THR-NNN"
