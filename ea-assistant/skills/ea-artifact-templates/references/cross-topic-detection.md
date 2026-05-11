# Cross-Topic Detection

Used by `ea-interviewer` at step 7b (Text mode) and before routing in Phase Interview mode. Runs after receiving an Answered answer, before writing it to the artifact.

## Detection Process

1. Scan the answer text for signals using the cues below.
2. If **no signal** found → proceed directly to writing the answer.
3. If a **signal is found** → increment the in-memory flag counter by 1. Present inline:

   > ⚠️ **Cross-topic signal:** Your answer mentions **{detected topic}** — this is typically captured in **{Target Artifact}** → `{{target_field}}`.
   >
   > **1.** Write this to {Target Artifact} now
   > **2.** Flag for later (saved in interview notes)
   > **3.** Continue as-is — record only here
   >
   > *(type 1, 2, or 3 — or press Enter to continue as-is)*

4. Handle the response:
   - **Option 1:** Check if the target artifact exists. If yes, write the flagged content to the specified field and confirm. Add artifact name to flagged-artifacts list. If the artifact does not yet exist, fall back to Option 2.
   - **Option 2:** Append to `## Flagged for Later` in the current session's interview notes: `- [{HH:MM}] {flagged content} → suggested artifact: {artifact} / field: {field}`. Add artifact name to flagged-artifacts list.
   - **Option 3 / Enter:** Record in the current artifact only.

5. After handling, **immediately continue** to the next question. Do not re-raise the same flag.

## Signal Map

| If currently interviewing… | Flag these signals → Target Artifact |
|---|---|
| Architecture Principles | Technology product/vendor names, version numbers → Technology Architecture; specific process descriptions → Business Architecture; "must…" / "shall…" statements → Requirements Register; risk language ("we might fail…") → Architecture Vision |
| Architecture Vision | Specific technology platform names → Technology Architecture; detailed process steps → Business Architecture; data entity names or schemas → Data Architecture; delivery timelines, waves, or phased rollout → Architecture Roadmap |
| Architecture Vision | EA-layer signals (governance process, architecture standard, review board, reference architecture, model validation framework) → Architecture Principles or Governance Framework (EA layer); see **Two Layers signal** below |
| Business Architecture | Specific application or system names → Application Architecture; data entity definitions or schemas → Data Architecture; cloud or infrastructure decisions → Technology Architecture; regulatory/compliance requirements → Requirements Register |
| Business Architecture | EA-layer signals (governance, standard, review board, reference architecture, architecture process, approval workflow for solutions) → Governance Framework or Architecture Principles (EA layer); see **Two Layers signal** below |
| Data Architecture | Specific application or system names → Application Architecture; infrastructure or platform choices → Technology Architecture; data governance policies stated as binding rules → Architecture Principles |
| Application Architecture | Infrastructure or platform choices → Technology Architecture; data modelling or entity definitions → Data Architecture; integration standards stated as binding rules → Architecture Principles |
| Technology Architecture | Business process or capability descriptions → Business Architecture; data entity or model descriptions → Data Architecture; governance rules stated as principles → Architecture Principles |
| Requirements Register | Implementation approaches or technology choices → Technology / Application Architecture; gap statements → Gap Analysis; direction (goals / objectives) → engagement.json; story-format language ("as a X, I want Y") → flag as STY-NNN in Stories subsection, not a REQ-NNN row |
| Business / App / Tech Architecture (ABB field) | Vendor or product name in an ABB description → SBB Register (SBB-NNN); specific implementation detail in capability → ABB-NNN |
| User Story (STY-NNN) | Binding obligation language ("must", "shall", "required to") inside a story → extract as REQ-NNN in Requirements Register |
| Gap Analysis | Strategic direction or goal statements → Architecture Vision; technology decisions → Technology Architecture; new requirements → Requirements Register |
| Architecture Roadmap | Cut-over or rollback procedures → Migration Plan; risk items → Architecture Vision or Statement of Architecture Work |
| Migration Plan | Business goals or strategic rationale → Architecture Vision; requirements → Requirements Register |

## Signal Detection Cues

- **Technology:** specific product/vendor names, "Azure / AWS / GCP", version numbers, infra terms (compute, storage, network zone, Kubernetes, container)
- **Business:** "our process for…", "the team responsible…", capability names, org unit names, "customer journey"
- **Data:** entity or table names, "master data", "data model", "data quality", "duplicate records"
- **Application:** specific system names (Salesforce, SAP, CRM, ERP, "legacy system"), "application portfolio"
- **Requirement:** "must…", "shall…", "the system needs to…", "compliance requires…", "regulatory requirement"
- **Risk:** "we might…", "if X fails…", "the risk is…", likelihood/impact language ("high likelihood", "critical impact")
- **Direction:** goal/objective/strategy language during a non-Vision/non-direction interview ("our goal is…", "our strategy is…", "we want to achieve…")
- **Two Layers (EA-layer):** "governance process", "architecture standard", "reference architecture", "review board", "approval workflow", "model validation", "compliance framework" — when captured in a business-layer artifact (Business Architecture, Business Model Canvas, Stakeholder Map) → Governance Framework, Architecture Principles, or Implementation Governance Plan
- **Two Layers (Business-layer):** "customer journey", "revenue stream", "order-to-cash", "case management", "customer onboarding" — when captured in an EA-layer artifact (Architecture Principles, Governance Framework, Compliance Assessment) → Business Architecture or Business Model Canvas
- **User Story → Requirement:** "As a {role}, I want {goal} so that {benefit}" pattern, or story-format language ("acceptance criteria", "given/when/then", "BDD scenario") appearing in a Requirement field — the underlying need is a REQ-NNN; the story is a STY-NNN delivery item
- **Vendor in ABB → SBB:** a vendor, product, or brand name (e.g. "AWS S3", "Vault by HashiCorp", "Datadog") appearing in an Architecture Building Block description — ABBs must be vendor-neutral; vendor specifics belong in an SBB-NNN entry in the SBB Register
- **Implementation detail in Capability → ABB/SBB:** specific technical implementation language ("using Kubernetes", "deployed on Azure", "built with FastAPI") appearing in a capability description — capabilities describe WHAT is needed; implementation choices belong in ABB-NNN or SBB-NNN
- **"Must/shall" language in Story → Requirement:** a user story (STY-NNN) that contains binding obligation language ("must", "shall", "the system is required to") — extract as a separate REQ-NNN; stories express desired behaviour, not contractual constraints
- **Binding restriction language in Requirement → Constraint:** a requirement (REQ-NNN) row that describes an implementation restriction ("cannot use X", "must deploy within Y", "prohibited from Z", "limited to", "restricted to", "capped at") — extract as a separate CST-NNN in the Constraints Register; requirements define outcomes, not boundaries
- **Constraint without CST-NNN → flag:** any artifact containing free-text constraint language ("must use existing AWS account", "budget capped at", "no new vendors") without a `CST-NNN` ID or `Referenced Constraints` field — prompt to create via `/ea-constraints add`
- **SBB vendor lock-in without constraint source:** an SBB "Constraints / Lock-in Risk" field containing restriction text but no `Referenced Constraints: [CST-NNN]` link — flag as untraced; offer to create CST-NNN or link existing

## Do NOT Flag

- Direction items (goals/objectives/strategies) during Phase A or Phase B interviews — these are expected content for those phases
- General contextual statements not attributable to a specific artifact field
- Answers to questions that explicitly ask for cross-domain context (e.g., a constraints question in Architecture Vision that legitimately invites technology references)
- Answers to questions that explicitly ask for governance, standards, or EA capability context (e.g., a "Governance Framework" or "Architecture Principles" question that legitimately invites EA-layer content)
