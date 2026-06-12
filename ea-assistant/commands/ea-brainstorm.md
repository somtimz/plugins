---
name: ea-brainstorm
description: Capture freeform thoughts, concerns, and context about the current EA engagement — or a specific phase — for use during interviews
argument-hint: "[phase: Prelim|A|B|C|D|E|F|G|H] (optional)"
allowed-tools: [Read, Write, Glob]
---

Capture freeform brainstorm notes for the active EA engagement.

## Instructions

1. **Require an active engagement.** Check for `engagement.json` in context. If no engagement is active, prompt: "No engagement is currently active. Run `/ea-open` to open one first."

1b. **Extract slug and resolve phase folder.** Read `engagement.json` and extract the `slug` field. Resolve the phase folder from the phase argument (or `currentPhase` if no argument):

   | Phase argument | Phase folder |
   |---|---|
   | `Prelim` | `preliminary` |
   | `Req` / `Requirements` | `requirements` |
   | `A` | `phase-a` |
   | `B` | `phase-b` |
   | `C` / `C-Data` | `phase-c-data` |
   | `C-App` | `phase-c-app` |
   | `D` | `phase-d` |
   | `E` | `phase-e` |
   | `F` | `phase-f` |
   | `G` | `phase-g` |
   | `H` | `phase-h` |
   | `engagement` | `cross-cutting` |
   | (none, and `currentPhase` is not set) | `cross-cutting` (engagement mode) |

   Brainstorm notes path: `EA-projects/{slug}/artifacts/{phase-folder}/notes/brainstorm/brainstorm-notes.md`

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
   - `engagement` → `"Engagement — Cross-Phase Strategic Context"`
   - (none, no `currentPhase` set) → `"Engagement — Cross-Phase Strategic Context"` (engagement mode inferred)

   If engagement mode is inferred (no argument and no active phase), announce before continuing:
   > "No phase is active — opening an engagement-level brainstorm pad. Captures strategic context before phase work begins."

   Note the phase scope for use in the session header and opening prompt.

3. **Check for existing notes.** Look for `EA-projects/{slug}/artifacts/{phase-folder}/notes/brainstorm/brainstorm-notes.md`.
   - If found, read the frontmatter to get `sessions` and `lastUpdated`.
   - Show: "You have {N} brainstorm session(s) — last updated {date}."
   - Offer: "Would you like to view existing notes first, or go straight to adding new thoughts?"
   - If the user wants to view, display the full file content, then ask if they want to add more.
   - If not found, continue silently to the capture session.

3b. **Pull upcoming interview questions.** Build a set of question prompts to show inside the pad as context:

   - **Artifact-scoped** (invoked from `/ea-interview` before a specific artifact): read the artifact template and extract all `{{placeholder}}` field names as question texts. If the artifact file already exists, also read it to skip fields that are already answered.
     - **Also extract guidance context:** Scan the same artifact file (or template if not yet created) for all `<details><summary>📋 Guidance</summary>...</details>` blocks. Build a `guidanceContext` map: `{section heading} → {guidance text}` (plain text). For each brainstorm thought category in the pad that maps to a section in this artifact, prepend a quality anchor to the category hint:
       > 📋 **What good looks like in this section:** {first 2 sentences of guidance text}
     This anchors the brainstorm to the artifact's documented quality standard before the user captures thoughts.
   - **Phase-scoped** (phase argument provided): read `skills/ea-artifact-templates/references/phase-interview-questions.md` for the relevant phase. Extract up to 8 key questions in order.
   - **Surface recommended matrices.** For phase-scoped sessions (phases Prelim, B, C-Data, C-App, D, E, F): read `skills/ea-artifact-templates/references/matrix-catalogue.md`, filter to entries whose Phase matches (excluding managed-elsewhere entries) and whose matrix file does not yet exist or has no filled cells. For each, add a `prefilled` entry: `{ questionRef: null, questionText: "[Matrix] {name} — {rowEntityLabel} × {columnEntityLabel}", answer: "{first elicitation question from the catalogue entry}", source: "matrix-catalogue", category: "relationships" }`. These hints prompt relationship statements that `/ea-interview` and `/ea-matrix new` later harvest as cell candidates. When any matrix hints were added, also inject a category card so they have a home in the pad: `{ id: "relationships", label: "Relationships", emoji: "🔗", hint: "Cross-element relationships — which application uses which data, who performs which role, what depends on what", suggestions: ["{rowEntityLabel} × {columnEntityLabel} pairs from the offered matrices"] }`.
   - **Filter engagement direction by phase relevance.** After extracting questions, also read `engagement.json → direction` and filter items by phase:
     - Phase A/Prelim: surface all goals and top-3 drivers by priority as context hints in the `goals` category
     - Phase B: surface goals/objectives linked to business capabilities; strategies; issues and problems
     - Phase C-Data/C-App: surface objectives with data or application targets; related strategies
     - Phase D: surface objectives with technology targets; strategies
     - Phase E/F: surface all objectives not yet linked to a work package (if `direction.gaps[]` exists, include top-3 unaddressed Critical/High gaps)
     - Phase G/H: surface objectives with governance targets; open issues
     Add these as additional entries in the `prefilled` list with `source: "direction"` so they appear in the pad as pre-loaded context tagged `[Direction]`.
   - **Engagement-scoped** (engagement mode): read Preliminary Parts 1–3 and Phase A §2–§6 from `phase-interview-questions.md`. Extract up to 10 key questions covering org context, drivers, goals, issues, and problems.
   - **Unscoped**: omit — leave `questions: null`.

   For each question, assign a `category` based on its topic:
   - Questions about ongoing failures, systemic threats, or known blockers → `"issues-problems"`
   - Questions about risks, stakeholder concerns → `"concerns"`
   - Questions about vision, goals, objectives, outcomes → `"goals"`
   - Questions about budget, time, policy, org limits → `"constraints"`
   - Questions about improvements, gaps to close, new capabilities → `"opportunities"`
   - Questions about baseline state, stakeholder readiness, preconditions → `"assumptions"`
   - Questions about measurement, KPIs, targets, baselines, success indicators → `"metrics"`
   - Questions about value streams, end-to-end stakeholder delivery chains → `"value-streams"`
   - Questions about use cases, actors, user goals, or interaction scenarios → `"use-cases"`
   - Questions about business processes, workflow steps, or process ownership → `"processes"`
   - Questions about conceptual data model, subject areas, entity relationships, or business-readable data structure → `"conceptual-model"`
   - Questions about logical data model, data attributes, normalisation, or storage structure → `"logical-model"`
   - Questions about platforms, runtime environments, or execution hosts → `"platforms"`
   - Questions about programming languages, frameworks, or runtime stacks → `"languages"`
   - Questions about infrastructure, compute, storage, hosting, or physical/virtual environments → `"infrastructure"`
   - Questions about network topology, segmentation, connectivity, or traffic patterns → `"network"`
   - Questions about relationships between elements — which application uses which data, who performs which role, what depends on what → `"relationships"`
   - All others → `"other"`

3c. **Pull pre-existing answers from documents.** Check whether any answers already exist that should be surfaced in the pad:

   - Read the artifact file (if it exists) and extract any fields that are already answered (non-placeholder, non-`⚠️ Not answered`, non-`⊘`). For each, record: `{ questionRef, questionText, answer, source: "artifact" }`.
   - Scan `EA-projects/{slug}/uploads/` for any previously processed documents. For each, check `artifacts/{phase-folder}/notes/interviews/` for a corresponding extraction note; extract Q&A pairs recorded against this artifact or phase. Record: `{ questionRef, questionText, answer, source: "{filename}" }`.
   - Read `ResearchAndReferences/research-index.md`. For each item tagged with the current phase or with topics matching the artifact or phase in scope, read the item's summary or first paragraph. Record as: `{ questionRef: null, questionText: item.title, answer: item.summary, source: "research: {item-title}" }`.
   - Scan all `artifacts/{phase-folder}/*.md` (excluding `notes/`) for completed artifacts in this phase. For each, extract top-level section headings and any populated fields that carry concrete values (not placeholders). Record as read-only context annotations: `{ questionRef: null, questionText: "{artifact-name} — {section}", answer: "{value}", source: "artifact: {artifact-id}" }`.
   - **Load detail files:** If a specific artifact is in scope, scan its tables for `[→](../details/{ID}.md)` links. For each linked file that exists at `artifacts/details/{ID}.md`, read it. Record the detail file's `title` and `summary` section as: `{ questionRef: null, questionText: "{ID}: {detail-title}", answer: "{detail-summary}", source: "detail: {ID}" }`. Detail file entries give the brainstorm pad richer item-level context for deep questions.
   - Deduplicate by `questionRef` — if both artifact and document have an answer for the same field, prefer the artifact value (it is the more authoritative state). Research, phase-artifact context, and detail file entries have no `questionRef` and are never deduplicated — they are surfaced as additional context only.
   - Set `prefilled` to the resulting list. If none found, set to `null`.

   If any prefilled entries were found, announce before launching the pad:
   > "Found {N} pre-existing answer(s) from {source(s)}. These will appear in the brainstorm pad marked with 📄 — you can keep, edit, or replace them."

3d. **Surface Issues and Problems explicitly.** Before launching the pad, ask two targeted questions in the chat (one at a time, wait for response):

   > "Before we open the brainstorm pad — **what is currently threatening or preventing your goals?** These could be patterns of dysfunction, unresolved conflicts, or capability gaps. We'll capture them as potential Issues [ISS?]."

   After the user responds, ask:

   > "And **what specific symptoms or blockers are actively preventing measurable progress** today? Things you can observe or measure — error rates, delays, failure counts. We'll capture these as potential Problems [PRB?]."

   Tag each response with `[ISS?]` or `[PRB?]` in the brainstorm pad's Issues & Problems category. These are not assigned ISS-NNN/PRB-NNN IDs here — IDs are assigned during `/ea-interview`. The tags flag them for formal assignment.

   If the user says "none" or "skip", proceed silently to step 4.

3e. **Inject Phase Intent Framing** (chat message only — not pad content).

   Read `skills/ea-engagement-lifecycle/references/adm-phase-guide.md`. Locate the section for the resolved phase. Extract:
   - First 2–3 bullet points from **Objectives**
   - First 3 bullet points from **Key Questions**
   - "What to decide now" and "What to defer" items from **Decision Flow**

   Present the following in the chat BEFORE launching the pad (this is a message to the user, not pad content):

   ---
   **{Phase Name} Brainstorm — What to focus on**

   This phase must establish:
   • {Objective 1}
   • {Objective 2}
   • {Objective 3}

   Key questions to surface answers for:
   • {Key Question 1}
   • {Key Question 2}
   • {Key Question 3}

   Decide now: {Decision Flow — decide now items}
   Defer: {Decision Flow — defer items}
   ---

   If `adm-phase-guide.md` is not found or the phase section is missing, skip this step silently. If engagement mode is active, skip this step silently.

4. **Build `BRAINSTORM_DATA` and launch the brainstorm pad.**

   Construct the `BRAINSTORM_DATA` object based on the resolved phase. Find the relevant `### Phase Name` section below for the phase-specific hint values. If the phase resolved to engagement mode, use the `### Engagement` section. Include `questions` (from step 3b) and `prefilled` (from step 3c) in the object.

   **Phase hints:**

   ### Engagement
   *Focus on pre-phase strategic context — direction and stakeholder landscape before detailed phase work begins.*

   | Dimension | Hint |
   |---|---|
   | Concerns | Misaligned sponsor expectations, unclear mandate, unresolved stakeholder conflicts, strategic threats with no owner |
   | Goals | Vision and mission alignment, strategic goals, high-level desired outcomes for the engagement |
   | Constraints | Regulatory obligations, budget envelope, board-level constraints, engagement scope boundaries |
   | Opportunities | Capabilities the org lacks but could gain, untapped value, quick wins before phase work |
   | Assumptions | Stakeholder availability, current-state baseline, org readiness, assumptions the engagement depends on |
   | Metrics | Engagement-level KPIs, benefits realisation targets, success indicators |
   | Other | Engagement type, governance context, related programmes, key stakeholder relationships |

   ### Preliminary
   *Focus on governance readiness and framework setup.*

   | Dimension | Hint |
   |---|---|
   | Concerns | Governance gaps, lack of sponsorship, conflicting stakeholder expectations |
   | Goals | What does architecture success look like for this organisation? |
   | Constraints | Existing standards, budget, team capacity, compliance mandates |
   | Opportunities | Capability improvements, standardisation wins, quick governance wins |
   | Assumptions | Organisational readiness, stakeholder availability, framework maturity |
   | Metrics | Governance effectiveness measures, architecture maturity indicators |
   | Other | Tailoring needs, external references, special context |

   ### Architecture Requirements Management
   *Focus on capturing and tracing requirements across the engagement.*

   | Dimension | Hint |
   |---|---|
   | Concerns | Requirements volatility, conflicting stakeholder needs, traceability gaps |
   | Goals | Complete, traceable requirements baseline, Zachman cell coverage |
   | Constraints | Requirements sign-off process, change control, scope boundaries |
   | Opportunities | Requirement pattern reuse, automated traceability, shared requirements repo |
   | Assumptions | Stakeholder availability for validation, scope stability, documentation quality |
   | Metrics | Requirements coverage %, traceability completeness, sign-off velocity |
   | Other | Corporate vs project requirements distinction, waiver candidates, source documents |

   ### Architecture Vision
   *Focus on strategic intent and the problem being solved.*

   | Dimension | Hint |
   |---|---|
   | Concerns | Scope creep, misaligned stakeholder expectations, unclear success criteria |
   | Goals | Strategic objectives, high-level outcomes, business problem being solved |
   | Constraints | Time-to-value, budget envelope, regulatory obligations |
   | Opportunities | Business value propositions, capability gaps to close, quick wins |
   | Assumptions | Current state baseline, stakeholder alignment, sponsor commitment |
   | Metrics | Executive KPIs, time-to-value signals, adoption rate, cost reduction targets |
   | Other | Risk appetite, key stakeholders, governance context |

   ### Business Architecture
   *Focus on capabilities, processes, value streams, use cases, and operating model.*

   | Dimension | Hint |
   |---|---|
   | Concerns | Process silos, duplicate capabilities, unclear ownership, change resistance, process steps owned by wrong actor, use case flows that span multiple siloed systems, business rules buried in spreadsheets or tribal knowledge |
   | Goals | Target business capabilities, operating model improvements, value streams end-to-end, clear use case coverage for each key actor, capabilities mapped to owning processes |
   | Constraints | Org structure, existing processes, HR and change capacity |
   | Opportunities | Process optimisation, capability consolidation, new value streams, digitise manual process steps, expose business services via API, consolidate duplicate processes serving the same actor goal |
   | Assumptions | Business process stability, workforce capacity to change, sponsor commitment |
   | Metrics | Business capability maturity, process cycle time, customer satisfaction scores |
   | Other | Business Model Canvas inputs, stakeholder concerns, regulatory context, use case actors and goals |
   | **Value Streams** | End-to-end chains of activity that deliver value to customers, stakeholders, or partners — from trigger to outcome |
   | **Use Cases** | Discrete goals pursued by specific actors (users, systems, or external parties) interacting with the business |
   | **Processes** | Business processes, their steps, owners, and the capabilities they exercise |

   ### Information Systems Architecture
   *Focus on data and application landscape, component design, service contracts, and user journeys.*

   | Dimension | Hint |
   |---|---|
   | Concerns | Data quality, application sprawl, integration complexity, legacy constraints, application components with unclear boundaries, API contracts undocumented or unstable, synchronous coupling creating brittle integrations |
   | Goals | Target data landscape, application rationalisation, integration patterns, clear component responsibilities with explicit service contracts, user journeys traceable through the application landscape, event-driven backbone for async flows |
   | Constraints | Existing contracts, data sovereignty, system lifespans |
   | Opportunities | API enablement, data product opportunities, application consolidation, decompose monolith along bounded contexts, introduce API gateway for external consumers, move commodity capabilities to SaaS |
   | Assumptions | Data ownership clarity, system inventory accuracy, integration maturity |
   | Metrics | Data quality scores, API throughput, integration error rates, system uptime |
   | Other | Migration complexity, system interdependencies, vendor relationships, use case traceability to application components |
   | **Conceptual Data Model** | Business-readable subject areas, entities, and relationships — independent of technology |
   | **Logical Data Model** | Structured data elements, attributes, and normalisation — how data is stored and related |

   ### Technology Architecture
   *Focus on platform, infrastructure, and technical decisions.*

   | Dimension | Hint |
   |---|---|
   | Concerns | Platform lock-in, security posture, technical debt, skills gaps |
   | Goals | Target platform, infrastructure principles, cloud/hybrid strategy |
   | Constraints | Existing infrastructure, vendor agreements, security policies |
   | Opportunities | Cloud adoption, automation, platform standardisation, cost optimisation |
   | Assumptions | Cloud readiness, vendor support timelines, network capacity |
   | Metrics | Infrastructure uptime, deployment frequency, security posture scores, cost per workload |
   | Other | Technology radar inputs, emerging tech candidates, decommission targets |
   | **Platforms** | Runtime platforms, execution environments, and hosting layers |
   | **Languages** | Programming languages, frameworks, and runtime stacks in use or under consideration |
   | **Infrastructure** | Compute, storage, and physical or virtual infrastructure — on-prem, cloud, or hybrid |
   | **Network** | Network topology, segmentation, connectivity, and traffic patterns between systems and zones |

   ### Opportunities & Solutions
   *Focus on solution options and delivery sequencing.*

   | Dimension | Hint |
   |---|---|
   | Concerns | Sequencing dependencies, transition risks, resource constraints for delivery |
   | Goals | Target solution portfolio, delivery waves, architecture packages |
   | Constraints | Budget cycles, programme capacity, dependency ordering |
   | Opportunities | Quick win projects, building-block reuse, parallel workstreams |
   | Assumptions | Programme delivery capacity, funding approval timelines, vendor availability |
   | Metrics | Work package delivery velocity, benefits realisation milestones, gap-closure rate |
   | Other | Work package candidates, gap-closure priorities, make-vs-buy considerations |

   ### Migration Planning
   *Focus on transition sequencing and cut-over safety.*

   | Dimension | Hint |
   |---|---|
   | Concerns | Cut-over risk, data migration integrity, rollback complexity |
   | Goals | Migration sequence, transition architectures, steady-state target |
   | Constraints | Downtime windows, data volume, parallel-run costs |
   | Opportunities | Phased delivery value, incremental decommissioning, user adoption sequencing |
   | Assumptions | Migration tool readiness, data cleanliness, testing environment availability |
   | Metrics | Migration completion %, cutover defect rate, parallel-run duration, rollback trigger thresholds |
   | Other | Contingency plans, stakeholder communication needs, pilot candidates |

   ### Implementation Governance
   *Focus on keeping delivery aligned with architecture intent.*

   | Dimension | Hint |
   |---|---|
   | Concerns | Compliance drift, change requests undermining architecture, delivery gaps |
   | Goals | Architecture compliance, decision quality, governance effectiveness |
   | Constraints | Project autonomy limits, governance overhead, review capacity |
   | Opportunities | Architecture review streamlining, compliance automation, pattern library |
   | Assumptions | Project team architecture awareness, governance authority, escalation paths |
   | Metrics | Compliance assessment pass rate, dispensation volume, review cycle time |
   | Other | Dispensation criteria, review frequency, architecture board composition |

   ### Architecture Change Management
   *Focus on monitoring for drift and triggering ADM re-entry.*

   | Dimension | Hint |
   |---|---|
   | Concerns | Unplanned architecture drift, technology obsolescence, stakeholder fatigue |
   | Goals | Architecture refresh cycle, change trigger criteria, continuous improvement |
   | Constraints | Change capacity, ongoing programme commitments, architecture team bandwidth |
   | Opportunities | Lessons-learned integration, architecture pattern updates, tooling improvements |
   | Assumptions | Change velocity, stakeholder engagement sustainability, capability maturity |
   | Metrics | Architecture debt backlog size, drift incident rate, re-entry trigger frequency |
   | Other | Sunset criteria, ADM re-entry triggers, architecture debt backlog |

   Set `BRAINSTORM_DATA.phase` to the full phase label (e.g. `"Phase D — Technology Architecture"`). If the phase has no letter prefix (Preliminary, Requirements), use just the name (e.g. `"Preliminary"`).

   Set `BRAINSTORM_DATA.subtitle` to the first Objectives bullet from the `adm-phase-guide.md` section for the resolved phase, prefixed with `"This phase must: "`. If `adm-phase-guide.md` was not readable or engagement mode is active, set `subtitle: null`.

   **Inject domain-specific categories when scoped to a domain phase.** In addition to the six default categories, append extra entries to `BRAINSTORM_DATA.categories` when the resolved phase matches:
   - **Phase B (Business Architecture):** `{ id: "value-streams", label: "Value Streams", emoji: "🌊", hint: "...", suggestions: [...] }`, `{ id: "use-cases", label: "Use Cases", emoji: "🎭", hint: "...", suggestions: [...] }`, `{ id: "processes", label: "Processes", emoji: "⚙️", hint: "...", suggestions: [...] }`
   - **Phase C-Data (Data Architecture):** `{ id: "conceptual-model", label: "Conceptual Data Model", emoji: "🗺️", hint: "...", suggestions: [...] }`, `{ id: "logical-model", label: "Logical Data Model", emoji: "📊", hint: "...", suggestions: [...] }`
   - **Phase D (Technology Architecture):** `{ id: "platforms", label: "Platforms", emoji: "🏗️", hint: "...", suggestions: [...] }`, `{ id: "languages", label: "Languages", emoji: "💻", hint: "...", suggestions: [...] }`, `{ id: "infrastructure", label: "Infrastructure", emoji: "🏢", hint: "...", suggestions: [...] }`, `{ id: "network", label: "Network", emoji: "🌐", hint: "...", suggestions: [...] }`

   For each extra category, copy the hint from the corresponding row in the phase hint table above and generate 2–4 concrete thought starters. If no starters are relevant, set `suggestions: null`.

   **Generate thought-starter suggestions for each category.** For each category (defaults + domain extras), derive 2–4 short, concrete thought starters relevant to the phase and engagement context. These are pre-written thought entries the user can click to add without typing — they should be specific enough to be immediately useful, not just restatements of the hint. Use the hint as the seed, then concretise. Example for Technology Architecture / concerns:
   - `"Legacy ERP creates vendor lock-in — no supported migration path before 2027"`
   - `"Security posture is reactive — no zero-trust or identity governance in place"`
   - `"Two key platform engineers leaving in Q3 — risk to delivery capacity"`

   Set `suggestions: null` for categories where generic suggestions would be meaningless (e.g., `other`). Only set suggestions when they genuinely help the user get started faster.

   Load the `ea-interview-ui` skill and present the **Brainstorm Pad** artifact with the constructed `BRAINSTORM_DATA`.

   - If phase-scoped, announce: "Opening a brainstorm pad scoped to {Phase Name}. Fill in thoughts freely across any category, then click 'Done' and paste the results back."
   - If engagement-scoped: "Opening an engagement-level brainstorm pad — captures strategic context before phase work begins. Fill in thoughts freely, then click 'Done' and paste the results back."
   - If not phase-scoped: "Opening the brainstorm pad. Fill in any thoughts across the categories, then click 'Done' and paste the results back."
   - The app handles all input — do not run a parallel chat Q&A.

5. **Wait for the user to paste their notes.** The app's result screen has a "Copy to clipboard" button. When the user pastes the `BRAINSTORM NOTES` block back into the chat, proceed to step 5b.

5b. **Detect and resolve conflicts.** Compare the user's brainstorm entries against any `prefilled` items from step 3c:

   A conflict exists when the paste-back contains both:
   - A `[📄 From: {source}]`-tagged entry (pre-filled from a document or artifact), AND
   - A user-written thought in the same category that addresses the same question or topic

   For each conflict detected, pause and present:

   ```
   ⚠️  Conflict — {question text}

   📄  {source}: {document / artifact answer}
   💭  Your brainstorm: {user thought}

   How would you like to resolve this?
   1. Keep document answer  (discard brainstorm thought)
   2. Keep brainstorm thought  (discard document answer)
   3. Combine both  (both recorded; interviewer will see both)
   4. Keep both separately  (record as distinct thoughts — no preference stated)

   Press Enter to keep both separately.
   ```

   Apply each resolution before saving. If the user chooses option 3 (Combine), merge into a single entry: `"{document answer} — {brainstorm thought}"`. If option 1 or 2, discard the other. If option 4 or Enter, record both entries with their original tags.

   If no conflicts are found, continue silently to step 6.

6. **Save the pasted notes.** Parse the `BRAINSTORM NOTES` block from the user's paste. The categories are already structured by the app (Issues & Problems / Concerns / Goals & Vision / Constraints / Opportunities / Metrics / Assumptions / Other) — use them as-is; do not re-categorise.

   **Append** a new session block to `EA-projects/{slug}/artifacts/{phase-folder}/notes/brainstorm/brainstorm-notes.md`. Never overwrite prior sessions. If the file does not exist, seed it from `templates/seeds/brainstorm-notes.md` (replace `{name}` → engagement name, `{phase}` → resolved phase label, `{today ISO 8601}` → today's date), then append the session block.

   **File format:**
   ```markdown
   ---
   engagement: {name}
   phase: {phase label, e.g. "Phase B — Business Architecture"}
   lastUpdated: YYYY-MM-DDTHH:MM:SSZ
   sessions: N
   ---

   ## Session N — YYYY-MM-DD [Phase B — Business Architecture] (only if phase-scoped)

   ### Issues & Problems
   - [ISS?] {systemic concern threatening a goal}
   - [PRB?] {specific observable symptom blocking an objective}

   ### Concerns
   - {thought}

   ### Goals & Vision
   - {thought}

   ### Constraints
   - {thought}
   - *(Promote to CST-NNN via `/ea-constraints add` when constraint is certain, sourced, and owned)*

   ### Opportunities
   - {thought}

   ### Metrics
   - {thought}

   ### Assumptions
   - {thought}

   ### Other
   - {thought}
   ```

   When the brainstorm pad includes domain-specific categories, additional sections may appear after the base set — for example `### Value Streams`, `### Use Cases`, `### Processes` (Phase B), `### Conceptual Data Model`, `### Logical Data Model` (Phase C-Data), or `### Platforms`, `### Languages`, `### Infrastructure`, `### Network` (Phase D). The app iterates over all categories dynamically, so these are included automatically when the user fills thoughts in them.

   Notes tagged `[ISS?]` and `[PRB?]` are pre-flagged for ISS-NNN/PRB-NNN assignment during the next `/ea-interview` session. The interviewer reads these tags and prompts for evidence and formal ID assignment.

   When creating the file for the first time, set `sessions: 1` in the frontmatter.

   When updating an existing file:
   - Increment `sessions` by 1 in the frontmatter
   - Update `lastUpdated` to today's date
   - Append the new session block after all existing content

6b. **Offer detail file recording for ID-bearing entries.** After saving the session, scan the newly written session's **Issues & Problems** and **Concerns** sections for entries that contain a recognised engagement ID pattern (e.g. `G-001`, `CAP-003`, `WP-007`).

   If any ID-bearing entries are found, offer:
   > "{N} brainstorm item(s) reference specific engagement IDs and can be linked to detail files:
   >   - [ISS?] CAP-003: capability gap threatening operational efficiency
   >   - [PRB?] G-001: measurable decline in goal attainment rate
   > Record these in their item detail files? (y / n / select)"

   - **y** — process all: for each ID-bearing entry, create the detail file if it does not exist (using `templates/item-detail.md`), then append to its Issues section: `- [brainstorm: {YYYY-MM-DD}] {entry text}` (retaining `[ISS?]`/`[PRB?]` marker). Update `lastModified` in each detail file.
   - **select** — list entries and let the user choose which to record.
   - **n** — skip silently; brainstorm entries remain in session notes only.

   Entries without a recognisable ID are not surfaced — they remain in brainstorm notes for later review during `/ea-interview`.

7. **Prompt for diagrams.** Before confirming, check whether any standard diagrams exist for the active phase by reading `skills/ea-artifact-templates/references/diagram-catalogue.md` (Coverage Table section). Then ask:

   > "Are there any diagrams or visual models that would help communicate these ideas? Standard diagrams for this phase:"

   List the 1–3 most relevant diagram names and filenames from the catalogue. Then offer:
   > "Would you like to create one now? I can delegate to the ea-diagram agent with your brainstorm notes as context."

   If the user says yes: delegate to the `ea-diagram` agent with a brief from the brainstorm notes and the appropriate Mermaid starter from the catalogue.
   If the user says no or there are no relevant diagrams: continue silently to step 8.

7b. **Research during brainstorm.** At any point — before launching the pad, while waiting for the user to paste results, or after pasting — the user can type `r: {query}` or `research: {query}` in the chat to trigger an inline research pause:

   1. Extract the query string.
   2. Acknowledge: `🔍 Research pause — looking up: "{query}"`
   3. Search `ResearchAndReferences/research-index.md` for items whose tags or title match terms in the query. Summarise matching items (title + key points, max 3–5 bullets each). Show "No matching items in ResearchAndReferences/" if none found.
   4. Perform a targeted synthesis on the query, flag confidence level (High / Medium / Low).
   5. Present findings:
      ```
      ## Research Findings: {query}

      **From engagement library:**
      - {matched item title}: {key points}

      **Broader synthesis:**
      - {key finding 1}
      - {key finding 2}

      Confidence: {High / Medium / Low}
      ```
   6. Ask: `Save to ResearchAndReferences? (y / n / edit title)`
      - `y` → write `ResearchAndReferences/{slug}-research-{YYYYMMDD}.md` with frontmatter (`researchType: note`, `title: {query}`, `addedDate: today`, `tags: [{phase}]`). Append entry to `research-index.md`.
      - `n` → findings available in-session only.
      - `edit title` → prompt for title, then save.
   7. If the brainstorm pad has not been launched yet: ask "Would you like to add these findings to the brainstorm pad as prefilled context?" If yes, add them as a `prefilled` entry with `source: "research: {query}"` before launching.
      If the pad is already open or results have been pasted: note the findings are available in-session for the interviewer to reference.

7c. **Advanced Practitioner Pause during brainstorm.** At any point, the user can type advanced-mode triggers in the chat to surface practitioner-level prompts:

| Trigger | Mode | What it does |
|---|---|---|
| `p: {topic}` or `pattern: {topic}` | Pattern discovery | Loads `advanced-patterns.md`, finds the pattern most relevant to `{topic}`, and presents: pattern name, when to use it, how it applies to the current phase/artifact, and one implementation suggestion |
| `f:` or `failure-mode:` | Failure-mode pre-mortem | Loads `failure-modes.md`, scans the 6 failure modes, and asks: "Which of these symptoms do you see in this engagement?" Present the detection checklist and let the user select |
| `o:` or `optionality:` | Optionality exploration | Prompts: "What decision in this phase is hardest to reverse? How could you preserve future flexibility?" Reference `practitioner-tips.md` Tip #40 and deep tactic #8 |
| `m:` or `maturity:` | Maturity assessment | Loads `adm-maturity-model.md`, asks: "What would this artifact look like at L3 vs L5?" Present the maturity indicators for the current phase and ask the user to self-assess |
| `e:` or `economics:` | Economic framing | Prompts: "How would you express this in financial terms — cost, risk, value, or TCO?" Guide the user to quantify the economic dimension of their brainstorm thought |

When triggered:
1. Acknowledge: `🔮 Practitioner pause — {mode}: {topic or current phase}`
2. Load the relevant reference file and extract the most relevant content for the current phase/artifact context.
3. Present 1–3 focused prompts or questions that help the user apply the advanced concept.
4. Accept the user's response and append it to the brainstorm notes under the `Other` category, tagged with `[{mode}]`.
5. Ask: "Would you like to continue with the brainstorm, or run another practitioner pause?"
6. If the user chooses to continue, return to the normal brainstorm flow.

8. **Confirm.** After saving:
   > "Saved. These notes will be available when you run `/ea-interview` — the interviewer will reference relevant thoughts as it asks questions."

   If this was a phase-scoped session, also note:
   > "You can also open the phase directly with `/ea-phase {phase}` and select 'Brainstorm about this phase' from the next actions."
