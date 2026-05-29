---
name: ea-standards
description: Manage the Standards Information Base (STD-NNN) in the shared Architecture Repository — track adopted industry and regulatory standards, link to constraints, and surface compliance obligations during EA phase interviews. Requires a linked Architecture Repository.
argument-hint: "[list|add|link-constraint|surface] [STD-NNN] [--status Mandatory|Recommended|Informational|Deprecated] [--domain <domain>]"
allowed-tools: [Read, Write, Bash]
---

# /ea-standards — Standards Information Base

Uses skill: `ea-architecture-repository` → `references/sib-schema.md`

Requires: Architecture Repository linked via `engagement.json → repoPath` or active session repo (`/ea-repo open`).

---

## Mode: `list [--status <Mandatory|Recommended|Informational|Deprecated>] [--domain <domain>]`

Display the Standards Register table, filtered by adoption status and/or applicable domain.

Show: ID | Standard | Version | Body | Adoption Status | Domains | Linked Constraints

---

## Mode: `add`

Interview to create a new STD entry:

1. Standard name (e.g. "ISO 27001:2022", "NIST CSF 2.0", "BIAN v12")
2. Version / year
3. Issuing body (ISO | IEEE | NIST | TOGAF | BIAN | eTOM | Regulatory | Other)
4. Adoption status (Mandatory | Recommended | Informational | Deprecated)
5. Applicable domains (multi-select: Business | Data | Application | Technology)
6. Applicable ADM phases (multi-select: Prelim | A | B | C-Data | C-App | D | E | F | G | H)
7. Key requirements summary (brief, one paragraph)
8. Compliance evidence approach (brief — how would compliance be demonstrated in EA artifacts?)
9. Next review date (suggest 12 months from today)

Then:
1. Read `repo.json → sib.nextId` to get the new ID
2. Write `Architecture-Repository/sib/standards/STD-NNN.md` with YAML frontmatter and body sections
3. Update `repo.json → sib.nextId` to nextId + 1
4. Append row to `Architecture-Repository/sib/sib-index.md`
5. Update `standards-register.md` (add row to summary table and to correct status section)
6. Update `repo.json → lastModified`
7. Report: "✓ STD-NNN added: <name> [<adoptionStatus>]"

---

## Mode: `link-constraint <STD-NNN> <CST-NNN>`

Record that a per-engagement constraint enforces this standard:
1. Add `CST-NNN` to `STD-NNN.md → linkedCSTs[]`
2. Update `standards-register.md` Linked Constraints column for this STD row
3. Report: "✓ CST-NNN linked to STD-NNN"

Note: CST files live in the engagement's artifacts. This update is one-directional (STD records the link).

---

## Mode: `surface [--phase <phase>]`

Show standards applicable to the current ADM phase:
1. Filter STD entries where `applicablePhases` includes the current phase
2. Sort: Mandatory first, then Recommended, then Informational
3. For Technology-domain phases (C-App, D): additionally filter by `applicableDomains` includes Technology
4. Output: table of applicable standards with adoption status, domains, and compliance evidence approach

Used during Phase D interview (if repoPath set) to surface mandatory and recommended standards as compliance constraints.
