---
name: stakeholder-goal-classification
description: Reference classification of business goals by stakeholder perspective — Senior Management, Business Unit Manager, Staff, and Ultimate Client. Used by /ea-goals and /ea-interview to tag G-NNN goals with the stakeholder lens they primarily serve.
version: 0.9.86
---

# Stakeholder Goal Classification

Business goals can be viewed from multiple stakeholder perspectives. The classification below is derived from business-architecture practice and helps ensure goal coverage across the organisation and its external beneficiaries. It is a **lens**, not a hard ownership model — a single goal may serve more than one perspective.

Use the `stakeholder` field on `G-NNN` entries in `engagement.json → direction.goals[]` to record the primary perspective. The field is optional; when populated it appears in the Goals Register and can be used to filter or group goals during Phase-A interviewing and reporting.

## Categories

| Stakeholder | Typical Concerns | Example Goal Statements |
|---|---|---|
| **Senior Management** | Strategic performance, shareholder value, market position, regulatory posture, portfolio returns | "Increase market share in X segment", "Reduce enterprise risk exposure", "Improve EBITDA by Y%" |
| **Business Unit Manager** | Operational control, P&L accountability, product/service delivery, team performance, customer satisfaction within unit | "Shorten product time-to-market", "Reduce unit operating cost", "Improve customer retention in my segment" |
| **Staff** | Day-to-day effectiveness, tooling, workload, career development, safety, empowerment | "Eliminate manual re-keying", "Provide self-service access to data", "Reduce incident response time" |
| **Ultimate Client** | Outcome received, experience, cost, quality, trust, ease of doing business | "Receive order status in real time", "Resolve issues in one contact", "Pay only for value received" |

## Usage Rules

1. **Primary perspective only.** If a goal serves multiple stakeholders, pick the one whose outcome is most directly improved. Record other perspectives in the goal description or trace links.
2. **No invented categories.** Use only the four values above. If a goal does not map clearly, leave `stakeholder` blank rather than force a fit.
3. **Do not confuse with audience taxonomy.** The `audience` taxonomy (Executive / Business / Architecture / Delivery / Governance) used for artifact tailoring is separate. A goal classified as "Ultimate Client" may still be reported to an Executive audience.
4. **Link to direction.** A goal's stakeholder classification should be consistent with its linked drivers and objectives — a driver about customer churn should produce goals classified as Ultimate Client or Business Unit Manager, not Staff.

## Interview Prompt

When capturing goals in Phase A, ask:

> "From whose perspective is this goal most important — Senior Management, a Business Unit Manager, Staff, or the Ultimate Client?"

If the answer is ambiguous, capture the primary perspective and note secondary perspectives in the goal description.
