---
artifactId: technology-horizon-register
artifact: Technology Horizon Register
engagement: "{{engagement_name}}"
phase: All
status: Active
templateVersion: 0.9.55
reviewStatus: Not Reviewed
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

# Technology Horizon Register

**Engagement:** {{engagement_name}}  
**Architecture Repository:** {{repo_path}}  
**Owner:** {{repo_owner}}  
**Last Updated:** {{YYYY-MM-DD}}

> Technology radar tracking the organisation's position on emerging technologies, frameworks, and practices. Maintained in the shared Architecture Repository. Commands: `/ea-horizon add`, `/ea-horizon list`, `/ea-horizon update`.

---

## Radar Summary

| Ring | Count | Description |
|---|---|---|
| **Adopt** | 0 | Production-ready; use in new projects |
| **Trial** | 0 | Targeted PoC encouraged |
| **Assess** | 0 | Worth watching; too early to adopt |
| **Hold** | 0 | Do not start new work; migrate away |

---

## Adopt

_Technologies the organisation endorses for use in new projects._

| ID | Technology | Category | Rationale | Linked ABBs | Review Date |
|---|---|---|---|---|---|
| _(none yet)_ | | | | | |

---

## Trial

_Technologies showing promise; targeted proof-of-concept encouraged._

| ID | Technology | Category | Rationale | Linked ABBs | Review Date |
|---|---|---|---|---|---|
| _(none yet)_ | | | | | |

---

## Assess

_Technologies worth watching; too early for broad organisational use._

| ID | Technology | Category | Rationale | Linked ABBs | Review Date |
|---|---|---|---|---|---|
| _(none yet)_ | | | | | |

---

## Hold

_Technologies to avoid for new work; plan migration from existing usage._

| ID | Technology | Category | Rationale | Migration Target | Review Date |
|---|---|---|---|---|---|
| _(none yet)_ | | | | | |

---

## Ring History

_Records of technologies moving between rings._

| Date | Technology (ID) | From | To | Reason |
|---|---|---|---|---|
| _(none yet)_ | | | | |

---

## Appendix A — Ring Assessment Criteria

| Ring | Criteria |
|---|---|
| **Adopt** | Proven in production (internally or by credible reference organisations); stable API; strong community or vendor support; no significant lock-in risk |
| **Trial** | Demonstrated value in PoC or external production; worth investing in targeted exploration; some unknowns remain |
| **Assess** | Interesting signals; not ready to invest significantly; monitor at next review cycle |
| **Hold** | Problematic history (security, licensing, instability); superseded by better alternatives; or organisation has decided to standardise on something else |

## Appendix B — Review Cadence

Recommended: review the full radar annually. Trigger ad-hoc reviews when:
- A technology on the radar is referenced in a new ADR
- A vendor announces a major change affecting a technology (e.g. licensing, acquisition, EOL)
- A PoC completes for a Trial technology
- A significant new technology emerges warranting Assess placement
