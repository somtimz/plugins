# Phase-Specific Constraints

Runtime constraints loaded by `ea-facilitator`, `ea-interviewer`, and `ea-consistency-checker` when entering, working in, or validating a phase. These are plugin-level enforcement rules — distinct from the TOGAF quality gates in `phase-inputs-outputs.md`.

**How to use this file:**
- `ea-facilitator` — reads the entering phase's constraints when `/ea-phase` is invoked; surfaces any blocking gaps before starting work
- `ea-interviewer` — reads the active phase's constraints at session start; enforces ID and traceability rules inline as answers are recorded
- `ea-consistency-checker` — reads all phases' constraints when running a full or artifact-mode check; reports violations as Critical or Warning findings

---

## Constraint Severity

| Severity | Meaning |
|---|---|
| **Blocking** | Phase cannot be marked Complete until resolved |
| **Warning** | Should be resolved before marking Complete; surfaced in `/ea-status` and consistency reports |
| **Info** | Informational; surfaced in reports but does not block progress |

---

## Preliminary Phase

### Required Artifacts
| Artifact | Severity if absent |
|---|---|
| Architecture Principles | Warning |
| Engagement Charter | Warning |
| Governance Framework | Info |

### Content Constraints
| Constraint | Severity |
|---|---|
| Architecture Principles must contain at least 3 named principles | Warning |
| Engagement Charter must have `sponsor` field populated | Blocking |
| Engagement Charter must have `scope` section populated | Blocking |

### Traceability
None required at this phase — this phase establishes the foundation for traceability.

### Blocking Gates (must be true before marking Complete)
- [ ] At least one Architecture Principle artifact exists with `status: Draft` or higher
- [ ] `engagement.json → sponsor` is non-empty
- [ ] `engagement.json → scope` is non-empty

---

## Requirements Phase

### Required Artifacts
| Artifact | Severity if absent |
|---|---|
| Requirements Register | Blocking |
| Traceability Matrix | Warning |

### ID Constraints
| Constraint | Severity |
|---|---|
| Requirements Register must contain at least one REQ-NNN entry | Blocking |
| Every REQ-NNN must have a `Scope` column value of `Corporate` or `Project` | Blocking |
| Every REQ-NNN must have a non-empty `Motivation` field linking to a driver, goal, issue, problem, or objective | Warning |

### Traceability
| Rule | Severity |
|---|---|
| Every REQ-NNN `Motivation` value must reference a valid ID (DRV-NNN, G-NNN, OBJ-NNN, ISS-NNN, PRB-NNN) | Warning |

### Blocking Gates
- [ ] Requirements Register exists and has at least one REQ-NNN entry
- [ ] All REQ-NNN entries have a `Scope` value

---

## Phase A — Architecture Vision

### Required Artifacts
| Artifact | Severity if absent |
|---|---|
| Architecture Vision | Blocking |
| Statement of Architecture Work | Warning |
| Stakeholder Map | Warning |

### ID Constraints
| Constraint | Severity |
|---|---|
| At least one DRV-NNN (Business Driver) defined | Blocking |
| At least one G-NNN (Goal) defined | Blocking |
| At least one OBJ-NNN (Objective) defined | Warning |
| At least one STR-NNN (Strategy) defined | Warning |
| Every G-NNN must appear in §3 Goals | Blocking |
| Every OBJ-NNN must appear in §4 Objectives | Warning |
| Every STR-NNN must appear in §7 Strategic Direction Summary | Warning |

### Content Constraints
| Constraint | Severity |
|---|---|
| §1 Executive Summary must be populated (not `⚠️ Not answered`) | Blocking |
| §2 Business Drivers must contain at least one DRV-NNN entry | Blocking |
| §8 Scope must be populated | Blocking |
| §9 Stakeholders must list at least one stakeholder | Warning |
| §10 Architecture Principles must reference Preliminary phase principles | Warning |
| §14 Key Risks must be populated | Warning |
| Appendix A3 — Decision Log must be present | Warning |

### Traceability
| Rule | Severity |
|---|---|
| Every G-NNN must link to at least one DRV-NNN (`Business Driver(s)` column) | Warning |
| Every DRV-NNN must be referenced by at least one G-NNN (`Linked Goals` column) — orphan driver | Warning |
| Every OBJ-NNN must link to at least one G-NNN (`operationalises` relationship) | Warning |
| Every STR-NNN must reference at least one G-NNN in its `Supports Goal(s)` column | Warning |
| Every G-NNN must be referenced by at least one STR-NNN (`Linked Strategies` column) — goal with no delivery strategy | Warning |
| Every ISS-NNN must reference at least one G-NNN it threatens (`Threatens Goal(s)` column) | Warning |
| Every PRB-NNN must reference at least one OBJ-NNN it blocks | Info |

### Blocking Gates
- [ ] Architecture Vision exists with `status` of Draft or higher
- [ ] At least one DRV-NNN and one G-NNN defined
- [ ] §1 Executive Summary and §2 Business Drivers are populated
- [ ] Statement of Architecture Work exists (at minimum as a Draft)

---

## Phase B — Business Architecture

### Required Artifacts
| Artifact | Severity if absent |
|---|---|
| Business Architecture | Blocking |
| Business Model Canvas | Info |
| Gap Analysis (Phase B contribution) | Warning |

### ID Constraints
| Constraint | Severity |
|---|---|
| Business Architecture must reference at least one G-NNN from Phase A | Blocking |
| Business Architecture must reference at least one OBJ-NNN from Phase A | Warning |
| Any GAP-NNN identified must be registered in the Gap Analysis artifact | Warning |

### Content Constraints
| Constraint | Severity |
|---|---|
| Baseline business architecture section must be populated | Blocking |
| Target business architecture section must be populated | Blocking |
| Capability model section must be present and populated | Warning |
| Gap analysis section must list at least one gap | Warning |
| Appendix A3 — Decision Log must be present | Warning |

### Traceability
| Rule | Severity |
|---|---|
| Target business architecture must be traceable to at least one G-NNN or OBJ-NNN from Phase A | Blocking |
| Every GAP-NNN must reference the G-NNN or OBJ-NNN it prevents or blocks | Warning |
| Every REQ-NNN in scope for Business must appear in the Requirements Register | Warning |

### Blocking Gates
- [ ] Business Architecture exists with baseline and target sections populated
- [ ] At least one G-NNN or OBJ-NNN from Phase A is referenced
- [ ] Gap analysis contribution exists (inline or as a separate Gap Analysis artifact)

---

## Phase C — Data Architecture

### Required Artifacts
| Artifact | Severity if absent |
|---|---|
| Data Architecture | Blocking |
| Gap Analysis (Phase C-Data contribution) | Warning |

### Content Constraints
| Constraint | Severity |
|---|---|
| Baseline data architecture (logical or physical) must be populated | Blocking |
| Target data architecture must be populated | Blocking |
| Data architecture must reference or be consistent with Business Architecture's data entities | Warning |
| Appendix A3 — Decision Log must be present | Warning |

### Traceability
| Rule | Severity |
|---|---|
| Target data architecture must be traceable to at least one Business Architecture requirement or G-NNN | Blocking |
| GAP-NNN entries must reference the capability or data entity they concern | Warning |

### Blocking Gates
- [ ] Data Architecture exists with baseline and target sections populated
- [ ] At least one link to Business Architecture or Phase A goal established

---

## Phase C — Application Architecture

### Required Artifacts
| Artifact | Severity if absent |
|---|---|
| Application Architecture | Blocking |
| Gap Analysis (Phase C-App contribution) | Warning |

### Content Constraints
| Constraint | Severity |
|---|---|
| Baseline application architecture (application inventory) must be populated | Blocking |
| Target application architecture must be populated | Blocking |
| Application Architecture must be consistent with Data Architecture's data flows | Warning |
| Appendix A3 — Decision Log must be present | Warning |

### Traceability
| Rule | Severity |
|---|---|
| Target application architecture must be traceable to at least one Business or Data Architecture requirement | Blocking |
| Integration points between applications and data stores must be noted | Warning |

### Blocking Gates
- [ ] Application Architecture exists with baseline and target sections populated

---

## Phase D — Technology Architecture

### Required Artifacts
| Artifact | Severity if absent |
|---|---|
| Technology Architecture | Blocking |
| Gap Analysis (Phase D contribution) | Warning |

### Content Constraints
| Constraint | Severity |
|---|---|
| Baseline technology architecture (infrastructure inventory) must be populated | Blocking |
| Target technology architecture must be populated | Blocking |
| Technology Architecture must reference Application Architecture deployment needs | Warning |
| Technology standards compliance must be assessed | Warning |
| Appendix A3 — Decision Log must be present | Warning |

### Traceability
| Rule | Severity |
|---|---|
| Target technology architecture must be traceable to at least one Application or Data Architecture requirement | Blocking |
| Every ADR-NNN referenced must exist in the ADR Register | Warning |

### Blocking Gates
- [ ] Technology Architecture exists with baseline and target sections populated

---

## Phase E — Opportunities and Solutions

### Required Artifacts
| Artifact | Severity if absent |
|---|---|
| Gap Analysis (consolidated) | Blocking |
| Architecture Roadmap | Blocking |

### ID Constraints
| Constraint | Severity |
|---|---|
| At least one WP-NNN (Work Package) defined in the Architecture Roadmap | Blocking |
| At least one GAP-NNN consolidated from B, C, D gap analyses | Blocking |
| Every WP-NNN must link to at least one G-NNN, OBJ-NNN, or STR-NNN | Blocking |

### Content Constraints
| Constraint | Severity |
|---|---|
| Architecture Roadmap — Strategic Alignment section must be present and have at least one non-placeholder row | Blocking |
| Architecture Roadmap — `Advances Goals/Objectives` or `Executes Strategies` field must be populated for each WP | Blocking |
| Transition architectures defined (at least described inline if not a separate artifact) | Warning |
| Implementation and migration strategy direction stated | Warning |
| Appendix A3 — Decision Log must be present on Architecture Roadmap | Warning |

### Traceability
| Rule | Severity |
|---|---|
| Every G-NNN from Phase A must be covered by at least one WP-NNN (gap flagged if not) | Warning |
| Every STR-NNN from Phase A must be executed by at least one WP-NNN (gap flagged if not) | Warning |
| Every consolidated GAP-NNN must be addressed by at least one WP-NNN | Warning |

### Blocking Gates
- [ ] Architecture Roadmap exists with at least one WP-NNN
- [ ] Strategic Alignment section populated with WP → G/OBJ/STR links
- [ ] Consolidated Gap Analysis covers B, C, D domain gaps

---

## Phase F — Migration Planning

### Required Artifacts
| Artifact | Severity if absent |
|---|---|
| Migration Plan | Blocking |

### Content Constraints
| Constraint | Severity |
|---|---|
| Migration Plan must list all WP-NNN from the Architecture Roadmap with sequencing | Blocking |
| Each WP must have an effort estimate or wave assignment | Warning |
| Risk section must be populated | Warning |
| Dependencies between work packages must be noted | Warning |
| Appendix A3 — Decision Log must be present | Warning |

### Traceability
| Rule | Severity |
|---|---|
| Every WP-NNN in the Migration Plan must match a WP-NNN in the Architecture Roadmap | Blocking |
| Any new RIS-NNN introduced must be registered in the Risk Register | Warning |

### Blocking Gates
- [ ] Migration Plan exists
- [ ] All Architecture Roadmap WP-NNN entries are accounted for in the Migration Plan

---

## Phase G — Implementation Governance

### Required Artifacts
| Artifact | Severity if absent |
|---|---|
| Architecture Contract | Blocking |
| Implementation Governance Plan | Warning |
| Compliance Assessment (at least one) | Warning |

### Content Constraints
| Constraint | Severity |
|---|---|
| Architecture Contract must reference the Architecture Roadmap and Migration Plan | Blocking |
| All A3 Decision Log rows must have `governance state` of `Awaiting` or above (no `Provisional` remaining) | Warning |
| Compliance Assessment must cover at least one work package | Warning |
| Appendix A3 — Decision Log must be present on Architecture Contract | Warning |

### Traceability
| Rule | Severity |
|---|---|
| Architecture Contract must reference relevant ADR-NNN entries | Warning |
| Each Compliance Assessment must reference the WP-NNN it covers | Warning |

### Blocking Gates
- [ ] Architecture Contract exists and references the engagement's WP-NNN set
- [ ] At least one Compliance Assessment artifact exists

---

## Phase H — Architecture Change Management

### Required Artifacts
| Artifact | Severity if absent |
|---|---|
| Change Register | Blocking |

### Content Constraints
| Constraint | Severity |
|---|---|
| Change Register must aggregate all Phase G ACR artifacts | Blocking |
| Each change entry must have a disposition (dispensation / minor change / new ADM cycle) | Warning |
| Lessons learned section or note must be present | Info |

### Traceability
| Rule | Severity |
|---|---|
| Each change entry must reference the WP-NNN or artifact it affects | Warning |
| Any new ADM cycle trigger must produce a new Request for Architecture Work entry | Info |

### Blocking Gates
- [ ] Change Register exists with at least one entry reviewed and dispositioned

---

## Cross-Phase Rules (all phases)

These constraints apply regardless of the active phase and are enforced by `ea-consistency-checker` in every run.

| Rule | Severity |
|---|---|
| No ID prefix outside the approved scheme (G, OBJ, DRV, STR, ISS, PRB, MET, REQ, RIS, ADR, WP, GAP, CON) | Blocking |
| Every ID used in any artifact must be defined in at least one artifact (no broken references) | Warning |
| No artifact in `reviewStatus: Approved` modified without confirmation | Blocking |
| Every artifact in a `Complete` phase must have `status` of Draft or higher (not empty) | Warning |
| Concept definitions must not be paraphrased inline — reference `ea-concepts.md` | Info |
