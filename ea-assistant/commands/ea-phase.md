---
name: ea-phase
description: Start, edit, or resume any TOGAF ADM phase for the active engagement
argument-hint: "[phase: Prelim|Req|A|B|C|D|E|F|G|H]"
allowed-tools: [Read, Write, Bash]
---

Navigate to a specific TOGAF ADM phase for the active engagement.

## Instructions

1. If no engagement is active in context, run the `/ea-open` flow first.

2. If a phase argument was provided, map it to the full phase name:
   - `Prelim` → Preliminary
   - `Req` or `Requirements` → Architecture Requirements
   - `A` → Architecture Vision
   - `B` → Business Architecture
   - `C` → prompt: Data Architecture or Application Architecture?
   - `C-Data` → Data/Information Architecture
   - `C-App` → Application Architecture
   - `D` → Technology Architecture
   - `E` → Opportunities & Solutions
   - `F` → Migration Planning
   - `G` → Implementation Governance
   - `H` → Architecture Change Management

   If no argument provided, display the phase picklist:
   ```
   Select an ADM phase:
   1. Preliminary         [✅ Complete]
   2. Requirements        [✅ Complete]
   3. Phase A — Vision    [🔄 In Progress]
   4. Phase B — Business  [⬜ Not Started]
   ...
   ```

3. Load the selected phase:
   - Update `currentPhase` in `engagement.json`
   - If phase status is `Not Started`, set to `In Progress` and record `startedAt`
   - If phase status is `Complete`, ask: "This phase is marked complete. Would you like to reopen it for editing?"

4. Display a phase summary:
   ```
   ═══════════════════════════════════════════════
   Phase A — Architecture Vision
   Engagement: Acme Retail Transformation
   Status: In Progress (started 2026-03-01)
   ═══════════════════════════════════════════════

   Required artifacts:
   ✅ Architecture Principles (Approved)
   🔄 Architecture Vision (Draft — interview in progress)
   ⬜ Statement of Architecture Work (not started)
   ⬜ Stakeholder Map (not started)

   Required inputs from previous phases:
   ✅ Organisation Model (from Prelim)
   ✅ Requirements Register (from Requirements phase)
   ```

5. **Requirements check-in** (every phase entry except the Requirements phase itself — Requirements Management is continuous in the ADM, not a one-time gate):
   - Read `requirements/requirements-index.json` (schema in the `ea-requirements-management` skill); fall back to the Requirements Register markdown under `artifacts/requirements/` if the index is absent; if neither exists, skip silently.
   - Filter to requirements whose `phase` field matches the entered phase (or `All`) and whose status is not Implemented/Superseded.
   - If any match, show a compact block between the phase summary and next actions:
     ```
     Requirements relevant to this phase: {N} open ({N} High priority)
       REQ-003  High   {title truncated}
       REQ-017  High   {title truncated}
       {…top 5 by priority}
     Review or update them with /ea-requirements — new requirements emerging
     from this phase's work should be captured as they surface, not batched.
     ```
   - If High-priority requirements for this phase have no linked artifact yet, add: "⚠️ {N} High-priority requirement(s) for this phase are not yet addressed by any artifact — run `/ea-requirements trace`."

6. Offer next actions:
   - Create a missing artifact → `/ea-artifact create [artifact-name]`
   - Continue an in-progress artifact interview → `/ea-interview resume`
   - View phase guidance → loads the `ea-engagement-lifecycle` skill and use the `ea-facilitator` agent
   - **Brainstorm about this phase** → opens a phase-scoped brainstorm session
   - **Review Phase {N} artifacts** → invoke `/ea-engage-review --quick` and offer to grill each artifact in the current phase using the recommended grill-me skill (see `ea-grill.md` skill mapping table)
   - Mark phase complete → verify all required artifacts exist first

   When the user selects "Brainstorm about this phase":
   - Invoke `/ea-brainstorm phase [phase]` (e.g. `/ea-brainstorm phase B` for Business Architecture).
   - The phase argument is already known from step 2 — pass it directly so the brainstorm command opens with the correct phase scope and session header.

7. When marking a phase complete:
   - Check all required artifacts for the phase exist in `artifacts/`
   - Warn if any artifacts are still in `Draft` status
   - Set phase `status` to `Complete` and `completedAt` timestamp
   - Update `lastModified` in `engagement.json`
   - Suggest the next recommended phase
   - **Requirements → Phase A bridge:** when the completed phase is Requirements, suggest Phase A directly and carry the register forward: "Requirements phase complete — {N} requirements captured ({N} High priority). Start Phase A now? The Architecture Vision interview will reference these requirements, and Requirements Management continues throughout the engagement (capture new REQ-NNN items as they emerge in any phase)."
