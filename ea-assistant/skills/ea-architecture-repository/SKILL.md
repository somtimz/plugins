---
name: ea-architecture-repository
description: Manages the shared TOGAF Architecture Repository — Standards Information Base (SIB/STD-NNN), Vendor Landscape Register (VDR-NNN), Technology Horizon Register (THR-NNN), and enterprise-level governance artefacts. Supports multi-engagement, multi-project sharing via the EA-Workspace/ sibling-folder layout.
version: 0.9.59
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
│   └── reference-library/
│       └── abb-catalogue.md
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
