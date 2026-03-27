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
| Business Architecture | Specific application or system names → Application Architecture; data entity definitions or schemas → Data Architecture; cloud or infrastructure decisions → Technology Architecture; regulatory/compliance requirements → Requirements Register |
| Data Architecture | Specific application or system names → Application Architecture; infrastructure or platform choices → Technology Architecture; data governance policies stated as binding rules → Architecture Principles |
| Application Architecture | Infrastructure or platform choices → Technology Architecture; data modelling or entity definitions → Data Architecture; integration standards stated as binding rules → Architecture Principles |
| Technology Architecture | Business process or capability descriptions → Business Architecture; data entity or model descriptions → Data Architecture; governance rules stated as principles → Architecture Principles |
| Requirements Register | Implementation approaches or technology choices → Technology / Application Architecture; gap statements → Gap Analysis; direction (goals / objectives) → engagement.json |
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

## Do NOT Flag

- Direction items (goals/objectives/strategies) during Phase A or Phase B interviews — these are expected content for those phases
- General contextual statements not attributable to a specific artifact field
- Answers to questions that explicitly ask for cross-domain context (e.g., a constraints question in Architecture Vision that legitimately invites technology references)
