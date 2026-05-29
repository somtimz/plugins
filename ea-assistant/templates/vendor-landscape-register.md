---
artifact: Vendor Landscape Register
engagement: "{{engagement_name}}"
phase: All
status: Active
lastModified: "{{YYYY-MM-DDTHH:MM:SSZ}}"
taxonomy:
  domain: Technology
  category: Register
  audience: Architecture
  layer: Reference
  sensitivity: Internal
relatedArtifacts: []
diagrams: []
links: []
---

# Vendor Landscape Register

**Engagement:** {{engagement_name}}  
**Architecture Repository:** {{repo_path}}  
**Owner:** {{repo_owner}}  
**Last Updated:** {{YYYY-MM-DD}}

> Tracks vendor products assessed for the organisation's technology landscape. Maintained in the shared Architecture Repository — not per-engagement. Commands: `/ea-vendors add`, `/ea-vendors list`, `/ea-vendors update`.

---

## Summary

| Metric | Count |
|---|---|
| Total vendors | 0 |
| Active | 0 |
| Sunset / EoL | 0 |
| High lock-in risk | 0 |

---

## Vendor Register

| ID | Vendor | Product | Category | Roadmap Status | Lock-in Risk | Linked SBBs | Last Reviewed |
|---|---|---|---|---|---|---|---|
| _(none yet)_ | | | | | | | |

---

## Vendor Profiles

_No vendor profiles yet. Run `/ea-vendors add` to add the first vendor assessment._

---

## Appendix A — How to Add a Vendor

1. Run `/ea-vendors add`
2. Provide: vendor name, product name, category, current version, roadmap status, contract status, lock-in risk
3. Optionally link to ABBs (logical components this product implements)
4. The entry is saved to `Architecture-Repository/vendor-landscape/entries/VDR-NNN.md` and this register is updated

## Appendix B — Review Cadence

Recommended: review each VDR entry annually or when:
- Vendor announces major roadmap changes (e.g. EOL, acquisition)
- Contract renewal is due
- A new SBB is created referencing this vendor
- An ADR is raised that references this vendor
