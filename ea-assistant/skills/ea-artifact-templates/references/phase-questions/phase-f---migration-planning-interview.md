# Phase F — Migration Planning Interview


**Goal:** Define the practical wave plan, resourcing, cut-over approach, and rollback strategy for delivering the architecture roadmap

**Key questions:**
1. How should the work packages be grouped into delivery waves — what natural groupings exist based on dependency, risk, or business value?
2. For each wave, what resources and skills are required, and are they available within the planned timeframe?
   - For each role: what is required vs. what is confirmed? Record gaps in the Wave Resource Summary table.
   - Are vendor or partner commitments in place for this wave? If not, flag as a delivery risk.
3. What is the organisation's capacity for change — how much disruption can be absorbed per wave without affecting business operations?

*Resource validation — run after all waves are defined:*
> "Looking across all waves: where are the resource peaks? Are there any waves where multiple high-FTE work packages overlap? Flag overlapping peaks as scheduling risks in the Risk Register."
4. How will data be migrated for each wave? (select all that apply)
   - [ ] ETL — batch extract, transform, and load jobs
   - [ ] Replication — continuous sync from source to target system
   - [ ] Dual-write — application writes to both old and new systems simultaneously
   - [ ] API-based migration — programmatic data transfer via APIs
   - [ ] Manual — human-led data entry or copy
   - [ ] Other: ___
5. What is the cut-over approach? (select one)
   - [ ] Hard cut-over — all users switch at once on a fixed date
   - [ ] Phased rollout — groups of users migrated in waves
   - [ ] Parallel running — old and new systems operate simultaneously for a period
   - [ ] Feature flags — gradual activation controlled by configuration
   - [ ] Strangler fig — new functionality incrementally replaces old
   - [ ] Other: ___
6. What are the rollback triggers and procedures for each wave — if something goes wrong, how quickly can you revert and who makes that call?
7. How will legacy systems be decommissioned once replacement capabilities are live?
8. What are the entry and exit criteria for each wave — what must be true before a wave begins and before the next one starts?
9. How will user transition and change management be handled across each wave?
10. What dependencies exist with third-party vendors, regulators, or external systems that constrain the migration sequence?

### Decision Quality Questions
> Ask these after completing the standard Phase F questions. Migration decisions are often irreversible and expensive — timing and evidence quality matter.

1. **[DECISION]** Are migration waves prioritised by evidence quality, not just impact? (Work packages with weak evidence should be deferred or given guardrails.)
2. **[DECISION]** For each wave: what is the rollback cost and timeline? Is the decision reversible within the wave's budget?
3. **[DECISION]** What is the minimum viable evidence required before each wave starts? Has it been gathered?
4. **[DECISION]** Are there legacy exit criteria defined for every system being replaced? Without exit criteria, legacy systems live forever.
5. **[DECISION]** Which migration decisions are being made under time pressure that may compromise evidence quality? Flag as risky commits.

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Wave groupings | Migration Plan | `{{wave_1_name}}` / `{{wave_2_name}}` |
| Resource requirements per wave | Migration Plan | Wave Resource Summary table (role / required / available / gap) |
| Organisational change capacity | Migration Plan | `{{migration_overview}}` |
| Resource peak conflicts across waves | Risk Register (via `/ea-risks add`) | New RIS-NNN — delivery risk |
| Data migration approach | Migration Plan | `{{data_migration_approach}}` |
| Cut-over approach | Migration Plan | `{{cutover_approach}}` |
| Rollback triggers | Migration Plan | `{{trigger_1}}` / `{{trigger_2}}` |
| Rollback procedures | Migration Plan | `{{procedure_1}}` / `{{procedure_2}}` |
| Decommissioning approach | Migration Plan | `{{decommissioning_approach}}` |
| Wave entry/exit criteria | Migration Plan | `{{wave_1_entry_criteria}}` / `{{wave_1_exit_criteria}}` |
| User transition approach | Migration Plan | `{{user_transition_approach}}` |
| External dependencies | Migration Plan | `{{wave_1_dependencies}}` / `{{wave_2_dependencies}}` |
| Migration risks | Migration Plan | `{{description}}` / `{{mitigation}}` (risk register rows) |

**Facilitation Notes:**
- Run wave planning as a visual exercise — use sticky notes or a whiteboard to group work packages; verbal discussion alone rarely produces a coherent wave structure.
- Change capacity is frequently overestimated by leadership; ask operational managers separately to get a realistic picture of how much disruption the organisation can absorb.
- Rollback planning is often skipped under time pressure — treat it as mandatory; a rollback that has not been rehearsed is not a rollback.
- Data migration approach must be agreed with data owners and the DBA/data engineering team before the Migration Plan is finalised; late surprises here cause the most delivery delays.
- External dependencies (regulatory approvals, vendor upgrade windows, third-party API changes) are frequently on the critical path; surface them early and track them explicitly.

**§D Diagrams — ask at close of session:**
> "One diagram makes the Migration Plan immediately clearer for delivery teams. Would you like to create it now?"
- **Migration Wave Diagram** — Gantt showing what moves in each wave and key transition checkpoints (`migration-plan-waves.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram file → `diagrams/`, filename added to Migration Plan frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for a Mermaid starter.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase F? (y/n)"

Load the **Phase F — Migration Planning** section of `skills/ea-security/references/security-interview-questions.md` and ask its questions, routing answers per its output routing table (migration data protection, coexistence/cutover risks, secrets rotation, secure decommissioning, third-party access, per-wave security go/no-go).

---
