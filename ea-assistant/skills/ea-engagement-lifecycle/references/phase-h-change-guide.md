# Phase H Change Guide — ACR Triage, Classification, and ADM Re-entry

Operational guidance for Architecture Change Management. Used by `/ea-changes`, `/ea-phase H`, and the Phase H interview (see the facilitation notes in `phase-interview-questions.md`). The Change Request template captures the record; this guide governs how to **triage, classify, escalate, and route** each ACR-NNN.

## Change Drivers

Recognise where the change is coming from before classifying it:

| Driver | Typical signal |
|---|---|
| Strategic (top-down) | New business direction, merger/divestiture, regulatory regime change |
| Bottom-up correction | Implementation reveals the architecture doesn't work as designed |
| Operational | Incidents, performance/cost anomalies, capacity exhaustion |
| Technology refresh | Vendor end-of-life, platform deprecation, THR-NNN ring movement |
| External | Partner/interface changes, supply-chain or vendor events (VDR-NNN status change) |

## ACR Triage Flow

For each incoming ACR-NNN:

1. **Record** — ensure the Change Request artifact has: requester, driver (table above), affected artifacts/ABBs/SBBs, urgency.
2. **Impact assessment** — affected domains (B/C-Data/C-App/D), affected decisions (A3 rows / ADR-NNN that the change would contradict), affected registers (REQ/CST/POL/RIS). Include a security impact check (see Phase H section of `security-interview-questions.md`).
3. **Classify** — apply the classification table below.
4. **Route** — apply the escalation rules and (if applicable) the re-entry mapping.
5. **Close the loop** — update the Change Register (`/ea-changes`), supersede or amend affected ADRs, and record the decision in the owning artifact's A3.

## Classification (TOGAF three categories)

| Class | Definition | Test | Handling |
|---|---|---|---|
| **Simplification** | Removes or reduces something; no new capability; investment reduction | No target-architecture content changes; no ADR contradicted | Handle via change management: approve as waiver/minor change; update affected artifact(s) and registers; no ADM re-entry |
| **Incremental** | Bounded extension or modification within the existing target architecture's intent | Affects one domain; contradicts no Strategic-authority decision; fits existing principles and constraints | Handle via change management with a scoped update: re-enter only the affected domain phase (re-entry mapping below); ARB approval if any A3/ADR is amended |
| **Re-architecting** | Invalidates the target architecture's foundations | Contradicts a Strategic A3/ADR, breaks an Architecture Principle, changes business goals/drivers, or affects 2+ domains structurally | Initiate a new ADM cycle (or major iteration) starting at the re-entry phase; treat the current target as baseline; new Statement of Architecture Work |

**Rule of thumb:** if you find yourself amending the Architecture Vision or reversing a Strategic decision to accommodate the change, it is re-architecting — do not absorb it as a stack of "incremental" ACRs.

## Escalation Rules

| Condition | Decision authority | Timebox |
|---|---|---|
| Simplification | Lead architect (record in Change Register) | Decide within 1 review cycle |
| Incremental, no A3/ADR impact | Lead architect + affected domain owner | 2 weeks |
| Incremental, amends an A3 row or ADR | ARB (`/ea-arb new` agenda item; propagate via `/ea-arb close`) | Next ARB; expedite if delivery-blocking |
| Re-architecting | Sponsor + ARB — decision to launch a new cycle is itself an ADR | Sponsor decision within 30 days; record interim risk (RIS-NNN) while open |
| Urgent/emergency change | Lead architect may approve provisionally; retrospective ARB ratification at next meeting; mark the A3 row `Provisional` | Ratify at next ARB |

An ACR left undecided past its timebox is escalated one level and flagged in `/ea-changes` output.

## Re-entry Mapping

When a change requires re-entering the ADM, enter at the **earliest affected phase** and flow forward only through affected artifacts:

| Change touches | Re-enter at |
|---|---|
| Business goals, drivers, scope, stakeholders | Phase A (then forward) |
| Business capabilities, processes, org structure | Phase B |
| Data models, data governance, data platforms | Phase C-Data |
| Application portfolio, integration patterns | Phase C-App |
| Technology platform, infrastructure, hosting | Phase D |
| Work package content/sequencing only | Phase E (roadmap) / F (migration plan) |
| Governance/compliance approach only | Phase G |

Use `/ea-phase {X}` to re-enter (it prompts before reopening a completed phase) and record the reopening reason in the phase's notes. The requirements check-in on phase entry will re-surface affected REQ-NNN items.

## Outputs Checklist (per decided ACR)

- [ ] Change Register regenerated (`/ea-changes`)
- [ ] Affected ADRs superseded/amended (`/ea-adrs update`); A3 rows updated in owning artifacts
- [ ] Affected registers updated (REQ/CST/RIS/GAP)
- [ ] If re-entry: phase reopened with reason noted; downstream artifacts flagged for review (`/ea-consistency` after edits)
- [ ] Lessons fed back: principles/standards updates proposed where the change exposed a gap
