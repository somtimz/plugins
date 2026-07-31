# Phase B — Business Model Canvas Interview


**Goal:** Capture the nine building blocks of the business model before detailing capabilities and processes

**When to run:** Run this interview at the start of Phase B, before or alongside the Business Architecture interview. It is especially valuable for Greenfield and Brownfield engagements. For Assessment-only engagements, use it to baseline the current operating model.

**Key questions:**

### Customer Segments
1. Who are your most important customers or users? How would you group them into distinct segments?
2. For each segment: how large is it (volume, revenue contribution, strategic importance)?
3. Are there segments you serve today that you want to exit, grow, or enter in the future?

### Value Propositions
4. For each customer segment, what problem do you solve or what need do you satisfy?
5. What makes your offering different or better than alternatives available to that segment?
6. Which value proposition is most important to the organisation's long-term success?

### Channels
7. How do customers find out about what you offer today? What channels do you use to reach them?
8. How do customers purchase, access, or receive the product or service?
9. Are any channels underperforming or missing that you plan to add?

### Customer Relationships
10. What type of relationship do you maintain with each customer segment — personal, self-service, community, automated?
11. Is the primary goal of the relationship to acquire new customers, retain existing ones, or grow revenue per customer?
12. How do customers prefer to interact with you (in-person, digital, hybrid)?

### Revenue Streams
13. For what value do customers pay? What are all the ways the organisation generates revenue?
14. For each revenue stream, how is pricing determined (fixed, volume-based, negotiated, market-rate)?
15. Which revenue streams are most significant? Are any growing, declining, or at risk?

### Key Resources
16. What physical, intellectual, human, or financial assets are essential to delivering the Value Proposition?
17. Which of these resources are owned by the organisation, and which are leased or sourced from partners?
18. What would happen to the business model if you lost access to the most critical resource?

### Key Activities
19. What are the most important things the organisation must do well to make the business model work?
20. Are these activities production (making/delivering), problem-solving (consulting/knowledge), or platform-based (running a marketplace or network)?
21. Which activities are core and must stay internal, and which are candidates for outsourcing?

### Key Partnerships
22. Who are the most important external partners or suppliers the business model depends on?
23. For each partner: what do they provide, and what do you provide to them in return?
24. Are there partnerships that don't exist today that the target state will require?

### Cost Structure
25. What are the largest costs in operating the current business model?
26. Are costs primarily fixed (remain the same regardless of volume) or variable (scale with activity)?
27. Is the business model more cost-driven (minimise cost) or value-driven (justify premium pricing)?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Customer segments (who they are, size) | Business Model Canvas | `{{customer_segments}}` |
| Value propositions per segment | Business Model Canvas | `{{value_propositions}}` |
| Channels (awareness, delivery) | Business Model Canvas | `{{channels}}` |
| Customer relationship type and goal | Business Model Canvas | `{{customer_relationships}}` |
| Revenue streams and pricing | Business Model Canvas | `{{revenue_streams}}` |
| Key resources (type, owned vs. sourced) | Business Model Canvas | `{{key_resources}}` |
| Key activities (type, core vs. outsourced) | Business Model Canvas | `{{key_activities}}` |
| Key partnerships and what is exchanged | Business Model Canvas | `{{key_partnerships}}` |
| Cost structure (largest costs, fixed/variable) | Business Model Canvas | `{{cost_structure}}` |
| Business model narrative | Business Model Canvas | `{{business_model_summary}}` |
| Segment-to-service linkage | Business Architecture | `{{business_services}}`, `{{business_context}}` |
| Capability requirements from key activities | Business Architecture | `{{business_capabilities}}` |
| Process candidates from key activities | Business Architecture | `{{business_processes}}` |

**Facilitation Notes:**
- Run the BMC interview before the detailed Business Architecture questions — it creates a shared mental model of the business before diving into capability and process detail.
- The nine blocks are interdependent; if an answer changes one block, ask what it implies for related blocks (e.g., "If you add that channel, does it change your cost structure?").
- For Brownfield engagements, capture both current state and target state for each block — the differences are the transformation scope.
- The Value Proposition question is the most important anchor: capabilities, processes, and resources should all trace back to supporting at least one Value Proposition.
- If the organisation has multiple business units with different models, complete a separate canvas for each unit or product line.
- Use the BMC linkage table (Section 11 of the template) to connect each block to the corresponding Business Architecture element — this prevents the Business Architecture from drifting away from commercial reality.

---
