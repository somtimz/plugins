---
name: ea-brainstorm
description: Capture freeform thoughts, concerns, and context about the current EA engagement — or a specific phase — for use during interviews
argument-hint: "[phase: Prelim|A|B|C|D|E|F|G|H] (optional)"
allowed-tools: [Read, Write, Glob]
---

Capture freeform brainstorm notes for the active EA engagement.

## Instructions

1. **Require an active engagement.** Check for `engagement.json` in context. If no engagement is active, prompt: "No engagement is currently active. Run `/ea-open` to open one first."

1b. **Extract slug.** Read `engagement.json` and extract the `slug` field. Use it in all file paths throughout this command (e.g. `EA-projects/{slug}/brainstorm/brainstorm-notes.md`).

2. **Resolve phase scope.** If a phase argument was provided (e.g. `/ea-brainstorm phase B`), map it to a full phase name:
   - `Prelim` → Preliminary
   - `Req` or `Requirements` → Architecture Requirements Management
   - `A` → Architecture Vision
   - `B` → Business Architecture
   - `C` → Information Systems Architecture
   - `D` → Technology Architecture
   - `E` → Opportunities & Solutions
   - `F` → Migration Planning
   - `G` → Implementation Governance
   - `H` → Architecture Change Management

   Note the phase scope for use in the session header and opening prompt.

3. **Check for existing notes.** Look for `EA-projects/{slug}/brainstorm/brainstorm-notes.md`.
   - If found, read the frontmatter to get `sessions` and `lastUpdated`.
   - Show: "You have {N} brainstorm session(s) — last updated {date}."
   - Offer: "Would you like to view existing notes first, or go straight to adding new thoughts?"
   - If the user wants to view, display the full file content, then ask if they want to add more.
   - If not found, continue silently to the capture session.

4. **Build `BRAINSTORM_DATA` and launch the brainstorm pad.**

   Construct the `BRAINSTORM_DATA` object based on the resolved phase. Use the table below to look up the phase-specific values. If no phase argument was provided, set all fields to `null`.

   **Phase hint table:**

   | Phase | subtitle | concerns hint | goals hint | constraints hint | opportunities hint | assumptions hint | other hint |
   |---|---|---|---|---|---|---|---|
   | Preliminary | Focus on governance readiness and framework setup. | Governance gaps, lack of sponsorship, conflicting stakeholder expectations | What does architecture success look like for this organisation? | Existing standards, budget, team capacity, compliance mandates | Capability improvements, standardisation wins, quick governance wins | Organisational readiness, stakeholder availability, framework maturity | Tailoring needs, external references, special context |
   | Architecture Requirements Management | Focus on capturing and tracing requirements across the engagement. | Requirements volatility, conflicting stakeholder needs, traceability gaps | Complete, traceable requirements baseline, Zachman cell coverage | Requirements sign-off process, change control, scope boundaries | Requirement pattern reuse, automated traceability, shared requirements repo | Stakeholder availability for validation, scope stability, documentation quality | Corporate vs project requirements distinction, waiver candidates, source documents |
   | Architecture Vision | Focus on strategic intent and the problem being solved. | Scope creep, misaligned stakeholder expectations, unclear success criteria | Strategic objectives, high-level outcomes, business problem being solved | Time-to-value, budget envelope, regulatory obligations | Business value propositions, capability gaps to close, quick wins | Current state baseline, stakeholder alignment, sponsor commitment | Risk appetite, key stakeholders, governance context |
   | Business Architecture | Focus on capabilities, processes, and operating model. | Process silos, duplicate capabilities, unclear ownership, change resistance | Target business capabilities, operating model improvements, value streams | Org structure, existing processes, HR and change capacity | Process optimisation, capability consolidation, new value streams | Business process stability, workforce capacity to change, sponsor commitment | Business Model Canvas inputs, stakeholder concerns, regulatory context |
   | Information Systems Architecture | Focus on data and application landscape. | Data quality, application sprawl, integration complexity, legacy constraints | Target data landscape, application rationalisation, integration patterns | Existing contracts, data sovereignty, system lifespans | API enablement, data product opportunities, application consolidation | Data ownership clarity, system inventory accuracy, integration maturity | Migration complexity, system interdependencies, vendor relationships |
   | Technology Architecture | Focus on platform, infrastructure, and technical decisions. | Platform lock-in, security posture, technical debt, skills gaps | Target platform, infrastructure principles, cloud/hybrid strategy | Existing infrastructure, vendor agreements, security policies | Cloud adoption, automation, platform standardisation, cost optimisation | Cloud readiness, vendor support timelines, network capacity | Technology radar inputs, emerging tech candidates, decommission targets |
   | Opportunities & Solutions | Focus on solution options and delivery sequencing. | Sequencing dependencies, transition risks, resource constraints for delivery | Target solution portfolio, delivery waves, architecture packages | Budget cycles, programme capacity, dependency ordering | Quick win projects, building-block reuse, parallel workstreams | Programme delivery capacity, funding approval timelines, vendor availability | Work package candidates, gap-closure priorities, make-vs-buy considerations |
   | Migration Planning | Focus on transition sequencing and cut-over safety. | Cut-over risk, data migration integrity, rollback complexity | Migration sequence, transition architectures, steady-state target | Downtime windows, data volume, parallel-run costs | Phased delivery value, incremental decommissioning, user adoption sequencing | Migration tool readiness, data cleanliness, testing environment availability | Contingency plans, stakeholder communication needs, pilot candidates |
   | Implementation Governance | Focus on keeping delivery aligned with architecture intent. | Compliance drift, change requests undermining architecture, delivery gaps | Architecture compliance, decision quality, governance effectiveness | Project autonomy limits, governance overhead, review capacity | Architecture review streamlining, compliance automation, pattern library | Project team architecture awareness, governance authority, escalation paths | Dispensation criteria, review frequency, architecture board composition |
   | Architecture Change Management | Focus on monitoring for drift and triggering ADM re-entry. | Unplanned architecture drift, technology obsolescence, stakeholder fatigue | Architecture refresh cycle, change trigger criteria, continuous improvement | Change capacity, ongoing programme commitments, architecture team bandwidth | Lessons-learned integration, architecture pattern updates, tooling improvements | Change velocity, stakeholder engagement sustainability, capability maturity | Sunset criteria, ADM re-entry triggers, architecture debt backlog |

   Set `BRAINSTORM_DATA.phase` to the full phase label (e.g. `"Phase D — Technology Architecture"`). If the phase has no letter prefix (Preliminary, Requirements), use just the name (e.g. `"Preliminary"`).

   Load the `ea-interview-ui` skill and present the **Brainstorm Pad** artifact with the constructed `BRAINSTORM_DATA`.

   - If phase-scoped, announce: "Opening a brainstorm pad scoped to {Phase Name}. Fill in thoughts freely across any category, then click 'Done' and paste the results back."
   - If not phase-scoped: "Opening the brainstorm pad. Fill in any thoughts across the categories, then click 'Done' and paste the results back."
   - The app handles all input — do not run a parallel chat Q&A.

5. **Wait for the user to paste their notes.** The app's result screen has a "Copy to clipboard" button. When the user pastes the `BRAINSTORM NOTES` block back into the chat, proceed to step 6.

6. **Save the pasted notes.** Parse the `BRAINSTORM NOTES` block from the user's paste. The categories are already structured by the app (Concerns / Goals & Vision / Constraints / Opportunities / Assumptions / Other) — use them as-is; do not re-categorise.

   **Append** a new session block to `EA-projects/{slug}/brainstorm/brainstorm-notes.md`. Never overwrite prior sessions. If the file does not exist, create it.

   **File format:**
   ```markdown
   ---
   engagement: {name}
   lastUpdated: YYYY-MM-DD
   sessions: N
   ---

   ## Session N — YYYY-MM-DD [Phase B — Business Architecture] (only if phase-scoped)

   ### Concerns
   - {thought}

   ### Goals & Vision
   - {thought}

   ### Constraints
   - {thought}

   ### Opportunities
   - {thought}

   ### Assumptions
   - {thought}

   ### Other
   - {thought}
   ```

   When creating the file for the first time, set `sessions: 1` in the frontmatter.

   When updating an existing file:
   - Increment `sessions` by 1 in the frontmatter
   - Update `lastUpdated` to today's date
   - Append the new session block after all existing content

7. **Confirm.** After saving:
   > "Saved. These notes will be available when you run `/ea-interview` — the interviewer will reference relevant thoughts as it asks questions."

   If this was a phase-scoped session, also note:
   > "You can also open the phase directly with `/ea-phase {phase}` and select 'Brainstorm about this phase' from the next actions."
