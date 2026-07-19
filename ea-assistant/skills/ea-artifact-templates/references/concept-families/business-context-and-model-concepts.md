# Business Context & Model — Concept Definitions



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
