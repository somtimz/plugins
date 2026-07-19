# Phase G — Implementation Governance


### Objectives
- Ensure conformance of implemented solutions with the Target Architecture.
- Perform architecture oversight of implementation projects.

### Key Inputs
- Implementation and Migration Plan
- Architecture Definition Documents from previous phases
- Architecture Contract

### Major Steps
1. Confirm scope and priorities with implementation teams.
2. Identify deployment resources and skills.
3. Guide development of deployment plans.
4. Perform architecture reviews of deliverables.
5. Update the Architecture Repository with as-built information.
6. Issue Architecture Compliance Certificates.

### Key Questions
- Are implementation projects conforming to the agreed architecture?
- What deviations have been requested and are they justified?
- What lessons are being learned for future ADM cycles?

### Artefacts Produced
| Artefact | Description |
|---|---|
| Architecture Contract | Formal agreement between architecture and implementation teams |
| Compliance Assessment | Formal review of implementation against architecture |
| Architecture Compliance Certificate | Sign-off artefact for conformant deliverables |
| Updated Architecture Repository | As-built views and lessons learned |

### Deep Tactics
- Provide **embedded guidance**, not remote review — architects should sit with delivery teams, not gatekeep from a distance.
- Use **automated checks** in CI/CD to validate conformance — reduce governance latency and increase consistency.
- Focus governance effort on **high-risk, irreversible decisions** — don't review every line of code.
- **Track deviations explicitly** — every deviation should be accepted (with risk sign-off) or remediated, not just documented.
- **Measure governance by outcomes** — decision speed, delivery quality, and alignment, not checklist coverage.

### Hidden Mechanics
- Phase G is where **architecture intent meets delivery reality**. Without tight feedback loops, implementation drift is inevitable.
- Governance that is not tied to **funding or deployment consequences** is performative — it produces evidence of compliance without ensuring alignment.

### Maturity Indicators
- **L1:** Governance is checklist-based and centralized; deviations are documented but rarely remediated
- **L3:** Governance is selective and outcome-oriented; automated checks exist for core standards; deviations require explicit acceptance
- **L5:** Governance is largely automated; architects are embedded partners; metrics tie governance to delivery outcomes

---
