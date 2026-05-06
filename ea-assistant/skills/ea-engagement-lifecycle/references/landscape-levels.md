# Architecture Landscape Levels

TOGAF 10 defines four architecture levels that determine the scope, depth, stakeholder set, and governance forum for an engagement. The `architectureLevel` field in `engagement.json` captures this classification.

---

## Overview

| Level | Timeframe | Sponsored By | Governed By |
|---|---|---|---|
| Strategic | 5+ years | Board / C-suite | Enterprise ARB |
| Segment | 2–5 years | Domain leadership | Domain ARB |
| Capability | 1–3 years | Capability owner | Portfolio board |
| Solution | Immediate | Project sponsor | Project board |

---

## Level Definitions

### Strategic Architecture

**Definition:** Enterprise-wide direction-setting architecture. Addresses the entire organisation (or a major division) and sets the long-horizon intent that Segment and Solution architectures must align to.

**Organisational scope:** All business units; sponsored and consumed by board members and C-suite. Outputs inform programme portfolio decisions.

**Timeframe:** 5+ years.

**Primary TOGAF artifacts and expected depth at this level:**

| Artifact | Depth at Strategic level |
|---|---|
| Architecture Vision | Full: board-consumable strategic intent, drivers–goals–objectives fully linked, 3–5 page executive narrative |
| Architecture Principles | Full: all 5+ principles with rationale and implications defined |
| Governance Framework | Full: all four elements (Direction, Decision, Execution, Control) documented |
| Business Architecture | High-level: capability model and operating model; no process decomposition |
| Data Architecture | High-level: data domains and governance stance only |
| Application Architecture | High-level: application landscape view only |
| Technology Architecture | High-level: strategic platform choices and standards only |
| Architecture Roadmap | Full: multi-wave, cross-programme |
| ADRs | Full: all strategic-authority decisions require complete A3.N rationale blocks |
| Statement of Architecture Work | Full |

**ADM tailoring notes:** All phases apply. Phases B–D emphasise baseline documentation and direction-setting at capability level (not process or component level). Phase E/F produce a strategic roadmap spanning multiple programmes.

**Governance forum:** Enterprise Architecture Review Board (ARB). Changes to strategic-level architectures require formal ARB vote.

---

### Segment Architecture

**Definition:** Architecture for a defined business segment or domain (e.g. retail banking, supply chain, HR). Sits below Strategic and above Capability. Governs a specific area of the business while remaining aligned to the Strategic Architecture.

**Organisational scope:** One or two business units; sponsored by domain leadership (VP, Director, Head of function).

**Timeframe:** 2–5 years.

**Primary TOGAF artifacts and expected depth at this level:**

| Artifact | Depth at Segment level |
|---|---|
| Architecture Vision | Full: domain-scoped vision linked to strategic goals |
| Architecture Principles | Full: domain-specific principles supplementing enterprise principles |
| Business Architecture | Full: process decomposition, capability model, operating model |
| Data Architecture | Full: data models, data flows, governance rules |
| Application Architecture | Full: application portfolio, integration patterns |
| Technology Architecture | Full: platform and infrastructure detail for the segment |
| Gap Analysis | Full: per-domain gaps with root cause |
| Architecture Roadmap | Full: programme-level, multi-year |
| ADRs | Full: all strategic and tactical decisions documented |

**ADM tailoring notes:** All phases apply. Strong emphasis on baseline documentation (as-is) in Phases B–D, since Segment Architectures often govern existing capability that needs transformation.

**Governance forum:** Domain Architecture Review Board or equivalent. Some decisions escalate to Enterprise ARB.

**Cascades from:** Strategic Architecture (must align to strategic direction and principles).
**Feeds into:** Capability and Solution Architectures.

---

### Capability Architecture

**Definition:** Architecture scoped to a specific business capability (e.g. Customer Onboarding, Order Management, Identity & Access Management). Bridges the gap between Segment direction and Solution delivery.

**Organisational scope:** Capability team or programme; sponsored by capability owner or product director.

**Timeframe:** 1–3 years.

**Primary TOGAF artifacts and expected depth at this level:**

| Artifact | Depth at Capability level |
|---|---|
| Architecture Vision | Abbreviated: capability-scoped, 1–2 page narrative |
| Business Architecture | Full for the capability: process steps, roles, capability attributes |
| Data Architecture | Full for capability data domains |
| Application Architecture | Full: components, interfaces, integration within capability scope |
| Technology Architecture | Selective: only components relevant to the capability |
| Gap Analysis | Full: gaps within the capability scope |
| Architecture Roadmap | Full: release-level, 1–3 year horizon |
| ADRs | Full for tactical and operational decisions; strategic decisions escalate |
| Requirements Register | Full |

**ADM tailoring notes:** Phase A is abbreviated (capability vision, not enterprise vision). Phases B–D are narrowly scoped to the capability boundary. Phase E/F produce a release roadmap. Phase G/H govern capability-level conformance.

**Governance forum:** Portfolio or programme board. Some decisions escalate to Domain ARB.

**Cascades from:** Segment Architecture.
**Feeds into:** Solution Architectures within the capability.

---

### Solution Architecture

**Definition:** Architecture for a specific project, initiative, or system. Immediate-term; governs how a particular change will be delivered. Must align to Capability, Segment, and Strategic architectures above.

**Organisational scope:** Project team; sponsored by project or product manager.

**Timeframe:** Immediate — typically 3–12 months per release or phase.

**Primary TOGAF artifacts and expected depth at this level:**

| Artifact | Depth at Solution level |
|---|---|
| Architecture Vision | Abbreviated: project-scoped, 1 page |
| Business Architecture | Selective: only business context relevant to the solution |
| Data Architecture | Full: detailed data model for the solution |
| Application Architecture | Full: component design, API contracts, integration detail |
| Technology Architecture | Full: deployment architecture, infrastructure, security controls |
| Architecture Contract | Full: binding conformance agreement between EA and delivery |
| Compliance Assessment | Full: conformance to standards |
| ADRs | Full: all tactical and operational decisions; major decisions escalate |
| Requirements Register | Full |

**ADM tailoring notes:** Phase A is a brief scoping exercise. Phases B–C are often collapsed into a Solution Architecture Definition document. Phase D is detailed. Phase G is the primary governance touchpoint (conformance). Phase H manages change during delivery.

**Governance forum:** Project or delivery board. Solution ADRs may be reviewed by Domain ARB if they deviate from Segment standards.

**Cascades from:** Capability Architecture (or directly from Segment if no Capability architecture exists).

---

## Level Selection Guide

Use these questions to determine the correct level:

1. **Who is sponsoring this engagement?** Board / C-suite → Strategic. Domain leadership → Segment. Capability owner → Capability. Project manager → Solution.
2. **How many business units does this affect?** All or most → Strategic. One or two → Segment. One team / product area → Capability or Solution.
3. **What is the planning horizon?** 5+ years → Strategic. 2–5 years → Segment. 1–3 years → Capability. Under 1 year → Solution.
4. **Is there an existing architecture this must align to?** If yes, you are at or below the level of that architecture.
5. **Will outputs govern other architectures?** If outputs will direct other architectures, you are at a higher level than those.

If answers point to different levels, default to the **higher** level — it is easier to narrow scope than to expand it.

---

## Depth Expectation Matrix

| Artifact | Strategic | Segment | Capability | Solution |
|---|---|---|---|---|
| Architecture Vision | Full | Full | Abbreviated | Abbreviated |
| Architecture Principles | Full | Full | Inherit + supplement | Inherit |
| Governance Framework | Full | Full | Not applicable | Not applicable |
| Stakeholder Map | Full | Full | Full | Abbreviated |
| Statement of Architecture Work | Full | Full | Full | Full |
| Business Architecture | High-level | Full | Scoped full | Selective |
| Data Architecture | High-level | Full | Scoped full | Full |
| Application Architecture | High-level | Full | Scoped full | Full |
| Technology Architecture | High-level | Full | Selective | Full |
| Gap Analysis | High-level | Full | Full | Full |
| Architecture Roadmap | Full (strategic) | Full (programme) | Full (release) | Not applicable |
| Migration Plan | High-level | Full | Selective | Full |
| Architecture Contract | Not applicable | Abbreviated | Full | Full |
| Compliance Assessment | Not applicable | Abbreviated | Full | Full |
| ADRs (strategic authority) | Required — full A3.N | Required — full A3.N | Escalate to Segment | Escalate to Capability |
| ADRs (tactical authority) | Full | Full | Full | Full |
| ADRs (operational authority) | Abbreviated | Abbreviated | Full | Full |

**Legend:** Full = all sections populated; Abbreviated = key sections only; High-level = summary/overview only; Selective = only sections relevant to scope; Not applicable = typically skipped at this level.

---

## Governance Appendix Rules by Level

| Appendix | Strategic | Segment | Capability | Solution |
|---|---|---|---|---|
| A3 — Decision Log | Required on all primary artifacts | Required on all primary artifacts | Required on all primary artifacts | Required on all primary artifacts |
| A3.N — Rationale blocks (Strategic authority decisions) | Required | Required | Required (escalate if cross-capability) | Required (escalate if cross-solution) |
| A4 — Stakeholder Concerns | Required on all primary artifacts | Required on all primary artifacts | Required on primary artifacts | Required on primary artifacts |
| A5 — Related Architecture Decisions | Required (T3-ADR) | Required (T3-ADR) | Required (T3-ADR) | Required (T3-ADR) |

**Note:** T3-ADR compliance (Appendix A5) applies at all levels. The distinction is in the authority level of ADRs and which governance forum ratifies them.

---

## How Levels Cascade

```
Strategic Architecture
  ↓ sets direction, principles, and standards for
Segment Architecture(s)
  ↓ defines capability models and domain rules for
Capability Architecture(s)
  ↓ specifies the solution pattern for
Solution Architecture(s)
```

Each level must trace its direction items upward:
- Segment goals and objectives should link to Strategic goals
- Capability requirements should trace to Segment objectives or gaps
- Solution requirements should trace to Capability requirements

The `/ea-consistency` command checks these linkages within an engagement. Cross-engagement traceability requires manual reference via `relatedArtifacts[]` in frontmatter.
