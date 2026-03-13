# Zachman Framework — Cell Descriptions

The Zachman Framework is a two-dimensional classification schema for enterprise architecture. The rows represent perspectives (stakeholder viewpoints), and the columns represent interrogatives (abstraction dimensions). The intersection of a row and column produces a cell — a specific architectural concern for a specific stakeholder.

This reference describes all 36 cells, with purpose, example content, and example artefacts for each.

---

## Framework Overview

### Rows (Perspectives / Stakeholders)

| Row | Label | Stakeholder | Nature of Description |
|---|---|---|---|
| 1 | Contextual | Executive / Planner | Scope and context — what is in scope and why |
| 2 | Conceptual | Business Owner | Business concepts and relationships — what the business does |
| 3 | Logical | Designer / Architect | System logic — how the system will work |
| 4 | Physical | Builder / Developer | Technology specifics — how the system is built |
| 5 | Detailed | Implementer / Subcontractor | As-built detail — the actual implementation |
| 6 | Functioning | User | The working system as operated — reality |

### Columns (Interrogatives / Abstractions)

| Column | Interrogative | Domain |
|---|---|---|
| 1 | What | Data / Information |
| 2 | How | Function / Process |
| 3 | Where | Network / Location |
| 4 | Who | People / Organisation |
| 5 | When | Time / Event |
| 6 | Why | Motivation / Strategy |

---

## The 36 Cells — Summary Table

| | What (Data) | How (Function) | Where (Network) | Who (People) | When (Time) | Why (Motivation) |
|---|---|---|---|---|---|---|
| **Row 1 — Contextual** | Business objects in scope | Business processes in scope | Business locations | Business stakeholders | Business events and cycles | Business goals and drivers |
| **Row 2 — Conceptual** | Semantic model / Entity types | Business process model | Business logistics | Organisational model | Business event cycle | Business strategy model |
| **Row 3 — Logical** | Logical data model | Application function model | Distributed systems model | Human interface model | Processing cycle | Business rule model |
| **Row 4 — Physical** | Physical data model | System design | Technology architecture | Presentation architecture | Control structure | Rule design |
| **Row 5 — Detailed** | Data definition (DDL) | Program code | Network configuration | Security configuration | Timing definitions | Rule specifications |
| **Row 6 — Functioning** | Instantiated data | Running functions | Network as deployed | Users in roles | Events occurring | Goals enacted |

---

## Cell-by-Cell Descriptions

### Row 1 — Contextual (Executive / Planner Perspective)

#### Cell 1,1 — Scope / What (Things in the Business)
**Purpose:** Identifies the major categories of things important to the business — not detailed data models, just the vocabulary of the domain.
**Example Content:** "Customer, Product, Order, Invoice, Employee, Asset"
**Example Artefacts:** Glossary of business terms, subject area list, scope statement

#### Cell 1,2 — Scope / How (Business Processes in Scope)
**Purpose:** Lists the high-level processes or functions the enterprise performs. Sets the boundary for what processes are in scope.
**Example Content:** "Take customer orders, Manage inventory, Process payroll, Deliver products"
**Example Artefacts:** Value chain diagram, capability list, SIPOC at enterprise level

#### Cell 1,3 — Scope / Where (Business Locations)
**Purpose:** Identifies the geographic or logical locations relevant to the enterprise scope.
**Example Content:** "Sydney HQ, Melbourne Operations Centre, Customer-facing web presence"
**Example Artefacts:** Geographic scope map, list of business locations

#### Cell 1,4 — Scope / Who (Important People / Organisations)
**Purpose:** Identifies the key players: business units, external organisations, and roles relevant to the scope.
**Example Content:** "Sales division, Logistics partner, Regulatory body, End customer"
**Example Artefacts:** Stakeholder list, partner/supplier catalogue, organisation scope statement

#### Cell 1,5 — Scope / When (Business Events and Cycles)
**Purpose:** Identifies significant business events and cycles that constrain or drive the enterprise.
**Example Content:** "Financial year end, Product launch cycle, Regulatory reporting quarter"
**Example Artefacts:** Business calendar, event list, significant dates register

#### Cell 1,6 — Scope / Why (Business Goals and Strategy)
**Purpose:** Captures the enterprise's goals, objectives, and strategic drivers.
**Example Content:** "Grow market share by 15%, Reduce operational cost by 10%, Achieve ISO 27001 certification"
**Example Artefacts:** Strategic plan summary, objectives register, balanced scorecard

---

### Row 2 — Conceptual (Business Owner Perspective)

#### Cell 2,1 — Enterprise / What (Semantic Model)
**Purpose:** Defines the key business entities and their relationships in business language, independent of any system.
**Example Content:** Customer has many Orders; an Order contains Order Lines; each Order Line references a Product
**Example Artefacts:** Conceptual data model, entity relationship diagram (conceptual), subject area model

#### Cell 2,2 — Enterprise / How (Business Process Model)
**Purpose:** Describes what the business does — the processes, inputs, outputs, and controls — in business terms.
**Example Content:** Order-to-Cash process, Procure-to-Pay process, Hire-to-Retire process
**Example Artefacts:** Business process model (e.g., BPMN at business level), value stream map, capability model

#### Cell 2,3 — Enterprise / Where (Business Logistics Model)
**Purpose:** Describes how the business connects its locations — distribution, communication, and logistics networks.
**Example Content:** Warehouse to retail distribution network, data centre connectivity between locations
**Example Artefacts:** Logistics network diagram, business node connectivity diagram

#### Cell 2,4 — Enterprise / Who (Organisational Model)
**Purpose:** Defines the organisational units, roles, and their relationships in business terms.
**Example Content:** Organisational hierarchy, role definitions, RACI for key processes
**Example Artefacts:** Organisation chart, role catalogue, RACI matrix

#### Cell 2,5 — Enterprise / When (Business Event Cycle)
**Purpose:** Describes the sequence of business events, triggers, and states that govern business operations.
**Example Content:** Customer lifecycle states (Prospect → Active → Lapsed), order fulfilment sequence
**Example Artefacts:** Business event diagram, state-transition diagram (business level), process sequence model

#### Cell 2,6 — Enterprise / Why (Business Strategy Model)
**Purpose:** Articulates goals, strategies, tactics, and the relationships between them in a structured model.
**Example Content:** Goal decomposition tree, strategy map, means-end analysis
**Example Artefacts:** Business motivation model (BMM), strategy map, goal hierarchy diagram

---

### Row 3 — Logical (Designer / Architect Perspective)

#### Cell 3,1 — System / What (Logical Data Model)
**Purpose:** Defines the data entities, attributes, and relationships required by information systems, normalised and independent of any specific database technology.
**Example Content:** Normalised entity-relationship model showing all entities, attributes, primary keys, and relationships
**Example Artefacts:** Logical data model (LDM), canonical data model, entity-relationship diagram (logical)

#### Cell 3,2 — System / How (Application Function Model)
**Purpose:** Describes what functions the application systems must perform to support the business processes.
**Example Content:** Functional decomposition of an Order Management System; functions: Create Order, Validate Stock, Calculate Price, Confirm Order
**Example Artefacts:** Functional decomposition diagram, use case model, application function catalogue

#### Cell 3,3 — System / Where (Distributed Systems Architecture)
**Purpose:** Describes the logical distribution of system functions across nodes, without specifying physical hardware.
**Example Content:** "Order processing function deployed at data centre node; customer portal deployed at edge/CDN"
**Example Artefacts:** Distributed systems diagram, node connectivity diagram, logical deployment model

#### Cell 3,4 — System / Who (Human Interface Model)
**Purpose:** Describes the roles that interact with systems, the interfaces presented to them, and access control models.
**Example Content:** Role-to-application matrix, user interface structure, role-based access control model
**Example Artefacts:** Human interface architecture, role catalogue, access control matrix

#### Cell 3,5 — System / When (Processing Cycle / State Model)
**Purpose:** Describes processing sequences, system state transitions, and the scheduling of automated processes.
**Example Content:** Batch processing schedule, system state machine for an order, event-driven process flows
**Example Artefacts:** Process flow diagram (system level), state machine diagram, event-driven architecture model

#### Cell 3,6 — System / Why (Business Rule Model)
**Purpose:** Captures the business rules that govern system behaviour, expressed in a declarative, technology-independent form.
**Example Content:** "A customer may not place an order if their account is suspended"; "Credit limit must not be exceeded"
**Example Artefacts:** Business rule catalogue, decision table, rule specification document

---

### Row 4 — Physical (Builder / Developer Perspective)

#### Cell 4,1 — Technology / What (Physical Data Model)
**Purpose:** Translates the logical data model into a technology-specific design, including table structures, indexing, partitioning, and storage.
**Example Content:** SQL Server schema with table names, column types, indexes, foreign key constraints
**Example Artefacts:** Physical data model (PDM), database schema diagram, data dictionary

#### Cell 4,2 — Technology / How (System Design)
**Purpose:** Describes the design of software components, modules, APIs, and services in technology-specific terms.
**Example Content:** Microservice component diagram, API specification (OpenAPI), class diagram
**Example Artefacts:** Component design document, API specification, module decomposition diagram

#### Cell 4,3 — Technology / Where (Technology Architecture)
**Purpose:** Specifies the physical technology infrastructure: servers, network topology, cloud regions, and deployment zones.
**Example Content:** AWS VPC topology, on-premises rack layout, network segment definitions
**Example Artefacts:** Network topology diagram, infrastructure architecture diagram, cloud landing zone design

#### Cell 4,4 — Technology / Who (Presentation Architecture)
**Purpose:** Specifies how users interact with the system: UI frameworks, authentication mechanisms, and device/channel support.
**Example Content:** React SPA architecture, OAuth 2.0 / OIDC authentication flow, mobile-responsive design specification
**Example Artefacts:** UI architecture specification, authentication design, channel architecture document

#### Cell 4,5 — Technology / When (Control Structure)
**Purpose:** Specifies timing controls, scheduling mechanisms, and transaction management at a technology level.
**Example Content:** Cron job schedule, message queue retry policy, distributed transaction design
**Example Artefacts:** Scheduling specification, transaction design, control flow diagram (system level)

#### Cell 4,6 — Technology / Why (Rule Design)
**Purpose:** Specifies how business rules are implemented in the technology — rule engines, decision services, configuration parameters.
**Example Content:** Drools rule engine configuration, decision service API, parameterised validation rules
**Example Artefacts:** Rule engine design, decision service specification, validation rule implementation guide

---

### Row 5 — Detailed (Implementer / Subcontractor Perspective)

#### Cell 5,1 — Component / What (Data Definition)
**Purpose:** The actual, deployable definition of data structures — as-built DDL, schema files, data migration scripts.
**Example Content:** CREATE TABLE SQL scripts, JSON Schema definitions, Avro schema files
**Example Artefacts:** DDL scripts, schema registry entries, data migration scripts

#### Cell 5,2 — Component / How (Program Code)
**Purpose:** The actual program code that implements system functions.
**Example Content:** Source code in Java, Python, TypeScript; unit tests; configuration files
**Example Artefacts:** Source code repository, compiled artefacts, build scripts

#### Cell 5,3 — Component / Where (Network Configuration)
**Purpose:** The actual network and infrastructure configuration: firewall rules, DNS, load balancer config, Terraform/CloudFormation.
**Example Content:** Terraform infrastructure-as-code, NGINX configuration, AWS Security Group rules
**Example Artefacts:** Infrastructure-as-code files, network configuration scripts, deployment manifests

#### Cell 5,4 — Component / Who (Security Configuration)
**Purpose:** The actual configuration of identity, access, and security controls applied to the system.
**Example Content:** Active Directory group policies, IAM role definitions, certificate configurations
**Example Artefacts:** IAM policies, security configuration scripts, certificate management configuration

#### Cell 5,5 — Component / When (Timing Definitions)
**Purpose:** The actual scheduler configurations, event trigger definitions, and timing parameters.
**Example Content:** Kubernetes CronJob manifests, EventBridge rules, message queue consumer configuration
**Example Artefacts:** Scheduler configuration files, event bridge rules, queue configuration

#### Cell 5,6 — Component / Why (Rule Specifications)
**Purpose:** The actual rule implementations: code, configuration, or rule-engine assets that enforce business rules.
**Example Content:** Decision table XML, hard-coded validation functions, Drools DRL files
**Example Artefacts:** Rule files, decision tables, validation configuration

---

### Row 6 — Functioning (User Perspective)

Row 6 represents the actual running enterprise — not a model or specification, but reality. It cannot be documented in advance; it is observed and measured.

| Cell | Description |
|---|---|
| 6,1 — Real Data | Actual data instances stored in production databases |
| 6,2 — Real Functions | Software as it executes in production |
| 6,3 — Real Network | The live network as it is configured and operating |
| 6,4 — Real People | Users performing actual roles in the live system |
| 6,5 — Real Events | Business and system events as they occur |
| 6,6 — Real Goals | The enterprise as it actually operates — goals being pursued or not |
