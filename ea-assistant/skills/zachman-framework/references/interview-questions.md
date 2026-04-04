# Zachman Interview Question Bank

Interview questions for filling empty Zachman cells, organised by row. Use with `/ea-zachman interview`.

## Row 1 — Contextual (Executive / Planner)

| Cell | Interview Question |
|---|---|
| R1,C1 | What are the major categories of things (entities, objects, subject areas) that are important to this business? List the key nouns of the domain — not a data model, just the vocabulary. |
| R1,C2 | What high-level business processes or functions are in scope for this engagement? List the main activities the organisation performs that this architecture must support. |
| R1,C3 | What are the relevant business locations — geographic sites, operational centres, or logical locations (e.g. web presence, shared services hub)? |
| R1,C4 | Who are the key players? List the business units, external organisations, regulators, and stakeholder groups that are in scope or materially affected. |
| R1,C5 | What are the significant business events, timeframes, and cycles that constrain or drive this engagement? (e.g. financial year end, regulatory reporting cycle, go-live target) |
| R1,C6 | What are the strategic goals and drivers behind this engagement? Why is this architecture being done? (Reference DRV-NNN and G-NNN IDs if already established.) |

## Row 2 — Conceptual (Business Owner)

| Cell | Interview Question |
|---|---|
| R2,C1 | Describe the key business entities and their relationships in business language — independent of any system. (e.g. "A Customer places many Orders; an Order contains Order Lines") |
| R2,C2 | What are the core business processes or value streams the organisation runs? Describe them in business terms — not system functions, but what the business does. |
| R2,C3 | How does the business connect its locations — what are the distribution, communication, and logistics networks that link them? |
| R2,C4 | Describe the organisational structure — business units, their relationships, and the key roles that operate the business processes. |
| R2,C5 | What are the key business lifecycle states or event sequences? (e.g. customer lifecycle, order fulfilment sequence, contract renewal cycle) |
| R2,C6 | What goals, strategies, issues, and problems has the organisation identified? How do they relate to each other? (Reference the motivation framework IDs already captured.) |

## Row 3 — Logical (Architect / Designer)

| Cell | Interview Question |
|---|---|
| R3,C1 | What are the data entities and their relationships required by the information systems — normalised and independent of any specific database? (Reference the logical data model if it exists.) |
| R3,C2 | What functions must the application systems perform to support the business processes? List the key application capabilities required. |
| R3,C3 | How are system functions logically distributed across nodes or zones — without specifying physical hardware? (e.g. "order processing at central node, customer portal at edge") |
| R3,C4 | Which roles interact with which systems, through which interfaces? Describe the human interface architecture and access control model. |
| R3,C5 | Describe the processing cycles, system state machines, and event-driven flows that govern system behaviour. |
| R3,C6 | What business rules govern system behaviour? List them in declarative, technology-independent form. (e.g. "A customer may not place an order if their account is suspended") |

## Row 4 — Physical (Engineer / Builder)

| Cell | Interview Question |
|---|---|
| R4,C1 | How is the logical data model translated into a technology-specific design? (Table structures, indexing strategy, storage technology, database platform) |
| R4,C2 | How are the system functions designed in technology-specific terms? (Component architecture, API design, microservices decomposition, technology choices) |
| R4,C3 | What is the physical technology infrastructure? (Servers, cloud regions, network topology, deployment zones, platform choices) |
| R4,C4 | How do users interact with the system at a technology level? (UI frameworks, authentication mechanisms, channel architecture, device support) |
| R4,C5 | What are the technology-level timing controls? (Scheduling mechanism, message queue design, transaction management, retry policies) |
| R4,C6 | How are business rules implemented in the technology? (Rule engine platform, decision service design, parameterised validation, policy enforcement) |
