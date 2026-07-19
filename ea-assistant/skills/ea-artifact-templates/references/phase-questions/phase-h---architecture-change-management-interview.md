# Phase H — Architecture Change Management Interview


**Goal:** Establish change management and architecture refresh

**Key questions:**
1. How are change requests to the architecture currently submitted and tracked?
2. What triggers a new ADM cycle versus a minor update or waiver?
3. How will the architecture be monitored for continued relevance over time?
4. Who is responsible for maintaining the architecture after this engagement concludes?
5. What is the planned cadence for architecture reviews after delivery?
6. How will lessons learned from this engagement be captured and used?

### Decision Quality Questions
> Ask these after completing the standard Phase H questions. Phase H is where decisions are revisited based on post-implementation evidence — adaptive governance depends on honest reassessment.

1. **[DECISION]** Which decisions made earlier in the engagement should be revisited based on post-implementation evidence? (e.g., technology choices that underperformed, assumptions that proved wrong.)
2. **[DECISION]** Are expired PAD-NNN entries reviewed and either resolved or formally closed? Orphan PADs create hidden delivery risk.
3. **[DECISION]** What is the process for converting post-implementation learnings into updated principles, standards, or reference architectures?
4. **[DECISION]** Are architecture decisions periodically stress-tested against new evidence? If not, the architecture becomes static and drifts from reality.
5. **[DECISION]** Which decisions from this engagement would you make differently with hindsight? Capture as lessons learned and feed back into the engagement charter for future work.

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Change request submission process | Change Request | `{{change_submission_process}}` |
| Change tracking approach | Change Request | `{{change_tracking}}` |
| ADM trigger criteria | Change Request | `{{adm_trigger_criteria}}` |
| Architecture monitoring approach | Change Request | `{{monitoring_approach}}` |
| Post-engagement ownership | Change Request | `{{architecture_owner}}` |
| Review cadence | Change Request | `{{review_cadence}}` |
| Lessons learned process | Change Request | `{{lessons_learned_process}}` |

**Facilitation Notes:**
- Phase H interviews often reveal that no one has thought about post-delivery ownership; treat this as a risk to flag immediately rather than leaving it for the client to resolve later.
- The ADM trigger criteria question prevents scope creep being managed as minor changes — agree on clear thresholds upfront.
- Ask for examples of how previous architecture changes were handled to calibrate the maturity of the change management process.
- Lessons learned capture is frequently skipped under delivery pressure; recommend a brief retrospective as a scheduled deliverable rather than an ad hoc activity.
- For ACR triage, classification thresholds, and re-entry mapping, use `skills/ea-engagement-lifecycle/references/phase-h-change-guide.md`.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase H? (y/n)"

Load the **Phase H — Architecture Change Management** section of `skills/ea-security/references/security-interview-questions.md` and ask its questions, routing answers per its output routing table (ACR security impact assessment, re-assessment triggers, control drift, policy/constraint review cycles, incident-learning feedback).

---
