---
name: ea-vendors
description: Manage the Vendor Landscape Register (VDR-NNN) in the shared Architecture Repository — add, list, update, link, and archive vendor assessments. Requires a linked Architecture Repository (repoPath in engagement.json or /ea-repo open).
---

# /ea-vendors — Vendor Landscape Register

Uses skill: `ea-architecture-repository` → `references/vendor-landscape-schema.md`

Requires: Architecture Repository linked via `engagement.json → repoPath` or active session repo (`/ea-repo open`).

---

## Mode: `list [--filter <field>=<value>]`

Display the vendor register table from `vendor-landscape-register.md`. Optional filters:
- `--filter category=SaaS`
- `--filter roadmapStatus=Active`
- `--filter lockInRisk=High`

Show: ID | Vendor | Product | Category | Roadmap Status | Lock-in Risk | Linked SBBs | Last Reviewed

---

## Mode: `add`

Interview to create a new VDR entry:

1. Vendor name
2. Product / service name
3. Category (IaaS | PaaS | SaaS | On-prem | Open-source | Consulting)
4. Current version assessed
5. Roadmap status (Active | Sunset | EoL | Unknown)
6. Contract status (Contracted | Evaluating | No contract | Expired)
7. Lock-in risk (Low | Medium | High) — prompt for rationale
8. Linked ABBs: "Which ABBs does this product implement? (Enter ABB-NNN IDs or press Enter to skip)"
9. Notes (optional)

Then:
1. Read `repo.json → vendorLandscape.nextId` to get the new ID (e.g. if nextId = 1, id = VDR-001)
2. Write `Architecture-Repository/vendor-landscape/entries/VDR-001.md` with the YAML frontmatter and body sections from the schema
3. Update `repo.json → vendorLandscape.nextId` to nextId + 1
4. Append a row to `Architecture-Repository/vendor-landscape/vendor-index.md`
5. Update `vendor-landscape-register.md` (add row to Vendor Register table and a stub profile in Vendor Profiles section)
6. Update `repo.json → lastModified`
7. Report: "✓ VDR-NNN added: <vendor> <product>"

---

## Mode: `update <VDR-NNN>`

Load `Architecture-Repository/vendor-landscape/entries/<VDR-NNN>.md`. Present current values one at a time. Prompt for changes. Update `lastReviewed` to today. Write back. Update `vendor-index.md` and `vendor-landscape-register.md` rows.

---

## Mode: `link-sbb <VDR-NNN> <SBB-NNN>`

Record that an SBB (per-engagement) implements this vendor product:
1. Add `SBB-NNN` to `VDR-NNN.md → linkedSBBs[]`
2. Report: "✓ SBB-NNN linked to VDR-NNN"

Note: SBB files live in the engagement's artifacts, not the Architecture Repository. This update is one-directional (VDR records the link).

---

## Mode: `archive <VDR-NNN>`

Mark vendor entry as archived:
1. Confirm: "Archive VDR-NNN (<vendor> <product>)? This marks it as EoL. (Y/n)"
2. Set `roadmapStatus → EoL` and add archive note with date to `notes` field
3. Update row in `vendor-index.md` and `vendor-landscape-register.md`
4. Report: "✓ VDR-NNN archived"
