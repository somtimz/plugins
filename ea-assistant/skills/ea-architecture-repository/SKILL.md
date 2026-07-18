---
name: ea-architecture-repository
description: Manages the shared TOGAF Architecture Repository — Standards Information Base (SIB/STD-NNN), Vendor Landscape Register (VDR-NNN), Technology Horizon Register (THR-NNN), and enterprise-level governance artefacts. Supports multi-engagement, multi-project sharing via the EA-Workspace/ sibling-folder layout.
version: 0.9.88
---

# Architecture Repository Skill

## Purpose

The Architecture Repository is the organisation-wide store for architecture reference material shared across all EA engagements and IT projects. It is NOT per-engagement — it lives at `EA-Workspace/Architecture-Repository/`, alongside `EA-Projects/`.

Each engagement opts in by setting `repoPath: "../../Architecture-Repository"` in `engagement.json`. See `references/repo-schema.md` for the full schema and directory structure.

## Key Concepts

### Standards Information Base (SIB — STD-NNN)
Stores adopted industry and regulatory standards:
- Regulatory requirements (e.g. GDPR, SOX, APRA CPS 234)
- Industry reference models (e.g. BIAN, eTOM, APQC PCF)
- Technology standards (e.g. ISO 27001, IEEE 802.11, NIST CSF)
- Each STD entry: id, name, version, issuingBody, adoptionStatus (Mandatory | Recommended | Informational | Deprecated), applicableDomains, linkedConstraints (CST-NNN), linkedPolicies (POL-NNN)
- Stored in: `Architecture-Repository/sib/standards/STD-NNN.md`

### Vendor Landscape Register (VDR-NNN)
Tracks vendor products and their organisation-wide assessment:
- Each VDR entry: id, vendor, product, category, version, roadmapStatus (Active | Sunset | EoL | Unknown), contractStatus, lockInRisk (Low | Medium | High), linkedABBs, linkedSBBs, linkedADRs, linkedSTDs
- Distinct from SBB: SBB is the per-engagement deployment decision; VDR is the organisation-wide vendor assessment
- Stored in: `Architecture-Repository/vendor-landscape/entries/VDR-NNN.md`
- See `references/vendor-landscape-schema.md` (created in Task 6)

### Technology Horizon Register (THR-NNN)
Technology radar tracking the organisation's position on emerging technologies:
- Ring: **Adopt** (production-ready, use in new projects) | **Trial** (targeted PoCs encouraged) | **Assess** (worth watching, too early to adopt) | **Hold** (do not start, migrate away)
- Each THR entry: id, name, category, ring, rationale, pocEvidence, linkedADRs, linkedVDRs, linkedABBs, ringHistory, reviewDate
- Stored in: `Architecture-Repository/technology-horizon/entries/THR-NNN.md`
- See `references/technology-horizon-schema.md` (created in Task 6)

### Reference Architecture Register (RA-NNN)
Stores reusable architectural patterns shared across engagements. A reference architecture is a **governed, reusable blueprint** for a *class* of solutions — prescriptive on patterns/constraints/interactions but not a solution architecture. For the full concept (what it is/isn't, boundary conditions, failure modes, the consistency-vs-freedom stress test), read the **Reference Architecture (RA-NNN)** definition in `skills/ea-artifact-templates/references/ea-concepts.md` — the single source of truth; do not restate it here.

- Governed blueprint per domain: capability alignment, logical service decomposition (ABB/SBB layer catalogues), **mandatory vs optional components**, approved integration patterns/mechanisms, information flows, **security trust boundaries**, data ownership & sovereignty, technology standards, NFR envelope, **governance checkpoints**, operational responsibilities, key decisions, constraints, and implied principles — per `templates/seeds/ra-entry-template.md` (guidance-driven, so RAs are interview-able, scorable, and grillable)
- Each RA entry: id, name, domain, status (Draft | Approved | Deprecated), source (internal | industry), linkedCAPs, linkedSTDs, linkedADRs, linkedSBBs
- `## Grill Checklist` and `## Governance Checkpoints & Conformance` drive `/ea-grill` RA compliance checks when an engagement adopts the RA
- Stored in: `Architecture-Repository/reference-library/entries/RA-NNN.md`
- Per-engagement local RAs (not shared): `artifacts/cross-cutting/reference-architectures/RA-NNN.md`
- See `references/reference-architecture-schema.md`

### Capability Library — Canonical Capability Map
The organisation's **canonical, reference business capability map** — the authoritative enterprise capability hierarchy that engagements seed and adopt from, so every engagement speaks the same capability language. For the Capability / Capability Model concept (what a capability is, components, attributes, value, map vs knowledge graph), read the **Capability Model** definition in `skills/ea-artifact-templates/references/ea-concepts.md`.

- A single hierarchical map (L1 domain → L2 capability → L3 sub-capability), box-in-box, non-flow; each canonical capability carries a stable `CAP-C-NNN` id, name, value/outcome, and description (no engagement-specific maturity or Supports — those are assessed per engagement)
- Stored in: `Architecture-Repository/capability-library/canonical-capability-map.md` (from seed `templates/seeds/canonical-capability-map.md`)
- **Adopt into an engagement:** `/ea-capabilities adopt` copies selected canonical domains/branches into the engagement's Business Architecture capability table, allocating fresh engagement `CAP-NNN` ids and recording `Source: canonical CAP-C-NNN`; the engagement then assesses Current/Target maturity and `Supports` locally
- The canonical map is technology- and organisation-neutral and stable; version it as the enterprise's capability taxonomy evolves

### Enterprise Governance
Principles, policies, and constraints that apply across ALL engagements (not per-engagement BP/DP/AP/TP):
- `Architecture-Repository/governance/enterprise-principles.md`
- `Architecture-Repository/governance/enterprise-policies.md`
- `Architecture-Repository/governance/enterprise-constraints.md`

## Workspace Structure

```
EA-Workspace/
├── workspace.json                    # lists all linked engagements and repo path
├── Architecture-Repository/
│   ├── repo.json                     # repo metadata and ID counters
│   ├── governance/
│   │   ├── enterprise-principles.md
│   │   ├── enterprise-policies.md
│   │   └── enterprise-constraints.md
│   ├── sib/
│   │   ├── sib-index.md
│   │   └── standards/               # STD-NNN.md files
│   ├── vendor-landscape/
│   │   ├── vendor-index.md
│   │   └── entries/                 # VDR-NNN.md files
│   ├── technology-horizon/
│   │   ├── horizon-index.md
│   │   └── entries/                 # THR-NNN.md files
│   ├── reference-library/
│   │   ├── reference-architecture-index.md
│   │   ├── entries/                 # RA-NNN.md files
│   │   └── abb-catalogue.md
│   └── capability-library/
│       └── canonical-capability-map.md   # canonical CAP-C-NNN hierarchy
└── EA-Projects/
    └── <slug>/
        ├── engagement.json           # repoPath: "../../Architecture-Repository"
        └── artifacts/
```

## Engagement Linking

When an engagement has `repoPath` set in `engagement.json`:
- `/ea-vendors`, `/ea-horizon`, `/ea-standards` resolve paths via `repoPath`
- `/ea-sbbs new` surfaces VDR context for the named vendor (roadmap status, lock-in risk)
- `/ea-adrs` surfaces THR/VDR context when the ADR type is technology/vendor selection
- Phase D interview (via `/ea-phase D`) surfaces THR entries with ring = Adopt or Trial as candidate SBBs
- Phase D interview surfaces STD entries with mandatory status and applicableDomains including Technology

## Commands

| Command | Purpose |
|---|---|
| `/ea-repo init [path]` | Initialise EA-Workspace with Architecture Repository |
| `/ea-repo link <slug>` | Link an engagement to the Architecture Repository |
| `/ea-repo status` | Show repo health: linked engagements, register counts, last modified |
| `/ea-repo open [path]` | Set active repository for session |
| `/ea-vendors` | Manage Vendor Landscape Register (VDR-NNN) |
| `/ea-horizon` | Manage Technology Horizon Register (THR-NNN) |
| `/ea-standards` | Manage Standards Information Base (STD-NNN) |
| `/ea-refarch [new|list|show|edit|adopt|unadopt|status]` | Manage Reference Architecture Register (RA-NNN) |
| `/ea-capabilities [list|add|update|map|score|adopt]` | Manage engagement capabilities (CAP-NNN) in Business Architecture; `adopt` seeds from the canonical capability map (`CAP-C-NNN`) |

## Initialization Workflow

When `/ea-repo init` is called:
1. Prompt user for: organisation name
2. Create `EA-Workspace/` directory
3. Write `workspace.json` from seed `workspace-json.md` (replace `{{organisation}}` with user input, `{{YYYY-MM-DD}}` with today, `{{YYYY-MM-DDTHH:MM:SSZ}}` with now)
4. Create `EA-Projects/` directory
5. Create `Architecture-Repository/` and all sub-directories
6. Write `repo.json` from seed `architecture-repo-json.md` (same placeholder substitution)
7. Write stub files for governance, sib, vendor-landscape, technology-horizon indexes
8. Report workspace path and offer to create first engagement via `/ea-new`

## Write Protocol

- Always read `repo.json` before writing; always update `lastModified` on every write
- ID allocation: read `repo.json → {register}.nextId`, use as new ID (format: `VDR-{nextId:03d}`), then increment and write back
- Enterprise governance files (`governance/`) require explicit user confirmation before overwrite
- Never write engagement-scoped data (REQ, GAP, RIS, etc.) into the Architecture Repository
- `workspace.json` must be updated whenever an engagement is linked or archived

## References

- `references/repo-schema.md` — workspace.json and repo.json field definitions, directory structure
- `references/vendor-landscape-schema.md` — VDR-NNN entry schema (Task 6)
- `references/technology-horizon-schema.md` — THR-NNN entry schema + ring model (Task 6)
- `references/sib-schema.md` — STD-NNN entry schema (Task 6)
