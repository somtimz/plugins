# Requirements Management — The Central Hub


Requirements Management is not a phase but a continuous process that sits at the centre of the ADM wheel. It ensures that requirements identified in any phase are captured, stored, and fed into the relevant phases.

### Key Activities
- Capture emerging requirements as they arise in any phase.
- Assess the impact of requirements on current and target architectures.
- Prioritise requirements based on business value and strategic alignment.
- Maintain a Requirements Repository linked to the Architecture Repository.

### Artefacts
| Artefact | Description |
|---|---|
| Requirements Impact Assessment | Analysis of how a requirement affects the architecture |
| Architecture Requirements Specification | Detailed requirements for architecture components |
| Requirements Traceability Matrix | Linkage of requirements to architecture decisions and work packages |

### Deep Tactics
- Capture requirements **as they emerge** in any phase — don't wait for a formal requirements phase.
- Assess **impact before priority** — a high-priority requirement with low architectural impact should not block design.
- Link every requirement to **at least one architecture decision or work package** — orphan requirements create hidden gaps.
- Maintain a **living Requirements Repository** — update it continuously, not just at phase boundaries.
- Use requirements to **test the architecture** — if a requirement cannot be traced to a component, the architecture is incomplete.

### Hidden Mechanics
- Requirements Management is the **central nervous system** of the ADM — it coordinates signals across all phases.
- Poor requirement traceability is the **root cause of scope creep** — untraced requirements reappear as "surprises" in implementation.

### Maturity Indicators
- **L1:** Requirements are captured in documents and updated manually; traceability is weak
- **L3:** Requirements repository is linked to architecture repository; impact assessments are standard practice
- **L5:** Requirements flow is automated; traceability is validated by fitness functions; impact is predicted before approval