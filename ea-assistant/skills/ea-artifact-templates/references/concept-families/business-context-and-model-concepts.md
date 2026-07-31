# Business Context & Model — Concept Definitions

### Business Context

**What it IS:**
Business Context is the **analysis discipline** that captures the external and internal conditions shaping the organisation and the engagement. It answers *"What is the environment telling us?"* by turning raw situational information into evidenced findings that can be traced into architecture direction and governance. Context is not a motivation item itself — it is the **input** that makes Drivers, Issues, Opportunities, Policies, and Constraints credible.

**Source techniques:**
- **PESTEL** — political, economic, social, technological, environmental, legal forces
- **SWOT** — strengths, weaknesses, opportunities, threats
- **Competitor / market analysis** — market position, disruptors, benchmarks
- **Regulatory scanning** — current and pending legislation, standards, supervisory guidance
- **Stakeholder power mapping** — influence, interest, concerns, expectations
- **Internal capability and maturity assessments** — current-state gaps and enablers

**Evidenced outputs:**
Business Context findings become detail files referenced from the Architecture Vision and Business Architecture. Each finding should cite its evidence and the direction/governance items it feeds:
- **Drivers (DRV-NNN)** — external/internal forces that make change necessary
- **Issues (ISS-NNN)** — systemic concerns threatening goals
- **Opportunities (OPP-NNN)** — favourable conditions to exploit
- **Policies (POL-NNN)** — governance positions derived from context
- **Constraints (CST-NNN)** — non-negotiable boundaries exposed by context

**What it is NOT:**
- Not a **Business Driver** — a driver is the force that creates pressure; context is the analysed finding that evidences the force
- Not a **Vision** or **Mission** — context describes conditions; vision/mission describe identity and aspiration
- Not a **Business Model Canvas** — context explains *why* the environment matters; the BMC explains *how* value is created, delivered, and captured
- Not a **Goal** or **Strategy** — context informs them but does not itself state what the organisation wants or how it will get there

**Common confusions:**
- "Increasing regulatory pressure" — the *finding* is **Business Context (CTX)** ✓; the force it creates is a **Driver (DRV-NNN)**
- "Our market share is declining" — this is **Business Context** ✓ (competitor/market finding). The resulting pressure is a Driver; the organisational consequence is an Issue
- "We must respond to AI disruption" — this is a **Driver** or **Strategy**, not Context, unless it is the documented analysis of *how* AI disruption is affecting the market

**TOGAF placement:** Preliminary / Phase A; inputs to the Architecture Vision (context section), Engagement Charter, and Business Architecture. Context findings are captured as CTX-NNN detail files and linked from the relevant artifacts.

**ArchiMate:** Context findings align with `Assessment` elements in the Motivation aspect — they assess the current situation and motivate change.

**Practitioner Notes:**
- Every CTX finding must be **evidenced**. A context statement without a source is an assumption; mark it as such or downgrade its weight.
- Anchor context to **decision-makers**. A PESTEL entry that no executive cares about is noise, not signal.
- **Maturity marker (L1→L5):** L1 = context is anecdotal; L3 = context is structured (PESTEL/SWOT), evidenced, and traced to direction; L5 = context is continuously refreshed from market, regulatory, and operational data
- **Economic framing:** Quantify impact where possible ("Regulation X affects $Y revenue segment by Z%")
- Distinguish **observed fact** from **interpretation** from **implication** in each finding

---

### Business Driver

**What it IS:**
A Business Driver is an external or internal force that makes the engagement necessary — it explains *why* the organisation needs to change now. Drivers are the bridge between the Mission (what we are) and the Goals (where we want to be). Every Driver must be evidenced: a driver without a verifiable source is an assumption, not a confirmed pressure.

**Structural parts** (engagement.json `direction.drivers[]`):
- **Statement** — one declarative sentence naming the force
- **Type** — External (market, regulatory, technology shift) / Internal (cost, capacity, leadership mandate)
- **Priority** — High / Medium / Low
- **Evidence / Source** — the event, report, regulatory instrument, or stakeholder statement that confirms this driver is real and current (e.g. "FY25 Board Risk Report p.12", "APRA CPS 230 effective Jan 2025")
- **Linked Goals** — G-NNN IDs this driver motivates

**What it is NOT:**
- Not a **Goal** — a driver is the force that creates pressure; a goal is the desired response to that pressure
- Not an **Issue** — a driver is the external or internal context; an issue is the organisational consequence of failing to respond to it
- Not a **Strategy** — a strategy is the chosen response; a driver is why a response is needed

**Common confusions:**
- "Increasing regulatory pressure" — this is a **Driver** ✓ (external force). The Goal it motivates might be "Achieve full regulatory compliance by Q2 2026"
- "We need to reduce costs" — this could be a Driver (internal cost pressure) OR a Goal depending on framing. If it is the *force* creating pressure on the engagement, it's a Driver; if it is what the engagement aims to achieve, it's a Goal
- "Our legacy platform is at end-of-life" — this is a Driver (internal technical force), not an Issue. The Issue is the *organisational consequence*: "Unplanned outages are increasing, threatening customer commitments"

**TOGAF placement:** Drivers Register (`/ea-drivers`); Architecture Vision §4 summary (Preliminary/Phase A); Engagement Charter §6.2. Drivers are captured in the Preliminary phase and refined in Phase A. All Drivers should be linked to at least one Goal — an unlinked Driver is out of scope or requires a new Goal.

**ArchiMate:** `Driver` element in the Motivation aspect. Motivates `Assessment`, which in turn motivates `Goal`.

**Practitioner Notes:**
- Every Driver must be **evidenced**. A driver without a verifiable source is an assumption, not a confirmed pressure.
- Anchor Drivers to **business outcomes**, not architecture artifacts. Each driver should link to at least one measurable Goal.
- **Maturity marker (L1→L5):** L1 = drivers listed without evidence; L3 = drivers linked to KPIs and revenue/cost; L5 = drivers continuously validated against market and operational data
- **Economic framing:** Quantify driver impact where possible ("Regulatory change X will cost $Y in non-compliance penalties by Z date")
- Frame drivers around **business scenarios**, not technical stacks

---

### Business Model Canvas

**What it IS:**
The Business Model Canvas (BMC) is a structured description of **how the organisation creates, delivers, and captures value**. It sits between the strategic direction (Vision, Mission, Goals, Strategies) and the Business Architecture / Operating Model: the strategy says *what* the enterprise wants to achieve; the BMC says *how value is produced and monetised*; the Business Architecture says *what capabilities and services are needed*; the Operating Model says *how they are organised and run*.

The BMC makes business-model assumptions explicit, testable, and traceable. Significant canvas elements, assumptions, and pivot hypotheses are captured as **BMC-NNN** detail files so they can be challenged and updated independently of the nine-block summary.

**Nine blocks and their register homes:**
| Block | Question it answers | Typical register home |
|---|---|---|
| **Customer Segments** | Who do we serve? | Stakeholder Map; Service consumers |
| **Value Propositions** | What value do we create for each segment? | Business Services (SVC-NNN); Value Streams (VS-NNN) |
| **Channels** | How do we reach and deliver to segments? | Operating Model §6; Service `deliveryChannel` |
| **Customer Relationships** | What relationship does each segment expect? | Operating Model §3; Stakeholder Map |
| **Revenue Streams** | How does the organisation capture value? | Cost Model Register (FIN-NNN) — revenue entries |
| **Key Resources** | What assets and capabilities are essential? | Capability Model (CAP-NNN); Architecture Repository |
| **Key Activities** | What must the organisation do well? | Capability Model (CAP-NNN); Business Processes (PROC-NNN) |
| **Key Partnerships** | Who do we rely on to make the model work? | Vendor Landscape (VDR-NNN); Sourcing model |
| **Cost Structure** | What are the main costs of operating the model? | Cost Model Register (FIN-NNN) — cost entries |

**What it is NOT:**
- Not a **Capability Model** — capabilities describe *what the org must be able to do*; the BMC describes *how value is created and captured*
- Not an **Operating Model** — the OM is execution design; the BMC is the value model that the OM must realise
- Not a **Strategy** — strategies are chosen courses of action; the BMC describes the resulting value-creation system
- Not a **Business Architecture** — business architecture is the stable blueprint of capabilities, services, processes, and value streams; the BMC is the input to that blueprint

**Common confusions:**
- "Our channel strategy is digital-first" — this is a **Strategy** (chosen approach), not a BMC block, until it is expressed as a Channel block with segments, value propositions, and delivery assumptions
- "We need a CRM" — this is an **SBB** or **Capability** discussion, not a BMC element, unless it is framed as a Key Partnership/Resource supporting a revenue stream
- "Reduce cost by 20%" — this is a **Goal/Objective**; the BMC's Cost Structure captures the cost model, not the target

**TOGAF placement:** Phase A/B boundary; authored as the `business-model-canvas.md` artifact in Phase B. It feeds the Business Architecture and Operating Model and is indexed by the Architecture Vision.

**ArchiMate:** The BMC spans Business layer concepts (Business Service, Value Stream, Business Process) and Motivation concepts (Outcome, Value) but has no single ArchiMate element.

**Practitioner Notes:**
- Populate the BMC for **both baseline and target** when significant business-model change is involved; otherwise baseline is sufficient and target changes emerge through the Business Architecture.
- Capture **interdependencies** between blocks explicitly — a Value Proposition unsupported by a Key Activity is a gap.
- **Maturity marker (L1→L5):** L1 = nine blocks listed with generic statements; L3 = blocks are evidenced, quantified, and linked to capabilities/services; L5 = BMC is continuously tested against market data and updated as a living artifact
- Use BMC-NNN detail files for **assumptions and pivot hypotheses** so they can be validated independently
- The BMC should be **reconciled** with the Capability Model and Operating Model — every block should have a traceable realization in one or both artifacts

---
