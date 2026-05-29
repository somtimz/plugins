---
artifactId: standards-register
artifact: Standards Register
engagement: "{{engagement_name}}"
phase: All
status: Active
templateVersion: 0.9.55
reviewStatus: Not Reviewed
lastModified: "{{YYYY-MM-DDTHH:MM:SSZ}}"
taxonomy:
  domain: Cross-cutting
  category: Register
  audience: Architecture
  layer: Reference
  sensitivity: Internal
relatedArtifacts: []
diagrams: []
links: []
---

# Standards Information Base

**Engagement:** {{engagement_name}}  
**Architecture Repository:** {{repo_path}}  
**Owner:** {{repo_owner}}  
**Last Updated:** {{YYYY-MM-DD}}

> Tracks adopted industry and regulatory standards relevant to the organisation's architecture. Maintained in the shared Architecture Repository. Commands: `/ea-standards add`, `/ea-standards list`, `/ea-standards surface`.

---

## Summary

| Adoption Status | Count |
|---|---|
| Mandatory | 0 |
| Recommended | 0 |
| Informational | 0 |
| Deprecated | 0 |

---

## Standards Register

| ID | Standard | Version | Body | Adoption Status | Domains | Linked Constraints |
|---|---|---|---|---|---|---|
| _(none yet)_ | | | | | | |

---

## Mandatory Standards

_Standards the organisation must comply with. Non-compliance creates architecture risk._

_No mandatory standards recorded yet. Run `/ea-standards add` to add the first standard._

---

## Recommended Standards

_Standards representing best practice. Adoption is expected unless explicitly waived._

_No recommended standards recorded yet._

---

## Informational Standards

_Standards tracked for awareness. No compliance obligation._

_No informational standards recorded yet._

---

## Deprecated Standards

_Standards no longer applicable to the organisation. Retained for historical reference._

_No deprecated standards recorded yet._

---

## Appendix A — Linking Standards to Constraints

When a standard mandates specific architecture behaviours, create a constraint (CST-NNN) via `/ea-constraints add` and link it to this STD entry via `/ea-standards link-constraint STD-NNN CST-NNN`. This propagates compliance obligations into engagement artifacts automatically.

## Appendix B — Review Cadence

Recommended: review the SIB annually or when:
- A regulatory change is announced
- An industry reference model (e.g. BIAN, eTOM) releases a new version
- A mandatory standard's version is superseded
- An engagement is started in a new regulatory jurisdiction
