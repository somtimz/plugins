# ArchiMate 3.x Viewpoints Reference Guide

A viewpoint defines the perspective from which an architecture view is constructed. ArchiMate 3.x defines a set of standard viewpoints, each suited to specific stakeholder concerns. This guide describes each standard viewpoint: its purpose, intended audience, the ArchiMate elements and relationships used, and example scenarios where it is most useful.

---

## Understanding Viewpoints

A **viewpoint** is a specification of the construction method for a view. A **view** is the resulting diagram produced by applying a viewpoint to the architecture model.

ArchiMate groups viewpoints into categories based on their purpose:
- **Basic viewpoints:** Introduce single-layer or single-aspect content
- **Motivation viewpoints:** Address drivers, goals, principles, and requirements
- **Strategy viewpoints:** Address capabilities, resources, and strategic courses of action
- **Layered viewpoints:** Show content across multiple layers
- **Implementation viewpoints:** Address migration and transition

---

## Motivation Viewpoints

### Stakeholder Viewpoint

**Purpose:** To identify the stakeholders involved in the architecture work and their key concerns, goals, and the drivers influencing them.

**Audience:** Enterprise architect, architecture governance board, executive sponsors.

**Elements Used:** Stakeholder, Driver, Assessment, Goal, Outcome, Principle, Requirement, Constraint, Value.

**Key Relationships:** Association, Influence.

**Example Scenario:** At the start of an ADM Phase A engagement, the architect produces a Stakeholder Viewpoint to show which business and IT stakeholders are invested in the programme, what their primary drivers are (e.g., cost reduction, compliance, customer satisfaction), and what goals they need the architecture to support.

---

### Goal Realisation Viewpoint

**Purpose:** To show how high-level goals are refined into more specific requirements, outcomes, and constraints.

**Audience:** Business owners, programme sponsors, requirements managers.

**Elements Used:** Goal, Outcome, Principle, Requirement, Constraint, Driver, Assessment.

**Key Relationships:** Influence, Realisation, Association.

**Example Scenario:** A financial services firm needs to show how its strategic goal of "Achieving regulatory compliance with DORA" is refined into a set of architectural principles (e.g., "Resilience by design"), requirements (e.g., "RTO < 4 hours for critical services"), and constraints (e.g., "Must use approved cloud regions only").

---

### Requirements Realisation Viewpoint

**Purpose:** To show how architecture elements address requirements.

**Audience:** Solution architects, business analysts, project managers.

**Elements Used:** Requirement, Constraint, Business Process, Application Component, Technology Node, and any realising elements.

**Key Relationships:** Realisation, Association.

**Example Scenario:** Used to demonstrate traceability — that a specific application service realises a documented functional requirement, and that a technology node satisfies a performance constraint.

---

### Motivation Viewpoint

**Purpose:** To show the full motivational context in one view: drivers, assessments, goals, principles, requirements, and constraints in their relationships.

**Audience:** Senior stakeholders, auditors, programme governance.

**Elements Used:** All Motivation layer elements.

**Key Relationships:** Influence, Association, Realisation.

**Example Scenario:** Produced as an executive summary artefact at the end of Phase A or at programme gate reviews, demonstrating that all architectural decisions can be traced back to documented strategic drivers.

---

## Strategy Viewpoints

### Capability Viewpoint

**Purpose:** To show the capabilities an enterprise possesses, needs, or plans to develop, and how they relate to each other.

**Audience:** Business strategists, capability planners, enterprise architects.

**Elements Used:** Capability, Resource, Course of Action.

**Key Relationships:** Composition, Aggregation, Realisation, Association.

**Example Scenario:** A retail organisation uses a Capability Viewpoint to show its current "Digital Commerce" capability gaps: it has "Online Catalogue" and "Payment Processing" capabilities but lacks "Real-time Inventory Visibility" and "Personalised Recommendations." This drives the roadmap.

---

### Strategy Viewpoint

**Purpose:** To show how capabilities, resources, and courses of action relate to the overall strategic direction.

**Audience:** Executive leadership, business strategy teams.

**Elements Used:** Resource, Capability, Value Stream, Course of Action.

**Key Relationships:** Realisation, Serving, Association.

**Example Scenario:** A bank uses a Strategy Viewpoint to show that its "Cloud Migration" course of action leverages its existing "DevOps Capability" and "Public Cloud Agreements" (resources) and will realise the "Platform Modernisation" capability needed to reduce time-to-market.

---

### Value Stream Viewpoint

**Purpose:** To show value streams and the capabilities that support them.

**Audience:** Business owners, process improvement teams, enterprise architects.

**Elements Used:** Value Stream, Capability, Course of Action, Resource.

**Key Relationships:** Composition, Association, Serving.

**Example Scenario:** Showing the "Order-to-Cash" value stream decomposed into stages (Quotation, Order Acceptance, Fulfilment, Invoicing, Collection) and mapping each stage to the business capabilities that enable it.

---

## Business Layer Viewpoints

### Business Process Viewpoint

**Purpose:** To show the sequence of business processes, the actors performing them, and the business objects consumed and produced.

**Audience:** Business process owners, business analysts, operational managers.

**Elements Used:** Business Actor, Business Role, Business Process, Business Event, Business Object, Business Service, Business Interface.

**Key Relationships:** Triggering, Flow, Assignment, Serving, Access.

**Example Scenario:** Documenting the "Customer Complaint Handling" process showing which roles are involved at each step, what data objects are created (e.g., "Complaint Record"), and how the process is triggered (e.g., "Complaint Received" event).

---

### Business Function Viewpoint

**Purpose:** To show the grouping of business activities into stable functional areas and the relationships between functions.

**Audience:** Business architects, capability planners.

**Elements Used:** Business Actor, Business Role, Business Function, Business Interface.

**Key Relationships:** Composition, Assignment, Serving.

**Example Scenario:** Used in Phase B to show the major business functions (Finance, HR, Sales, Operations) and how they relate, before decomposing each into processes.

---

### Organisation Viewpoint

**Purpose:** To show the organisational structure: business actors, roles, and their relationships.

**Audience:** HR, senior management, organisational designers.

**Elements Used:** Business Actor, Business Role, Business Collaboration, Location.

**Key Relationships:** Composition, Aggregation, Association, Assignment.

**Example Scenario:** Mapping out the post-merger organisational structure to identify where duplicate roles exist and where consolidation is possible.

---

### Actor Co-operation Viewpoint

**Purpose:** To show how actors (internal and external) work together, and what roles and interfaces they interact through.

**Audience:** Business analysts, relationship managers, integration architects.

**Elements Used:** Business Actor, Business Role, Business Collaboration, Business Interface, Business Service, Application Component, Application Service.

**Key Relationships:** Assignment, Serving, Association, Composition.

**Example Scenario:** Mapping the collaboration between a bank, its customers, and a payment network to understand which actors use which services and through which interfaces.

---

### Information Structure Viewpoint

**Purpose:** To show the business information entities, their attributes (descriptively), and their relationships — the conceptual data model.

**Audience:** Business data owners, data architects, integration designers.

**Elements Used:** Business Object, Representation, Meaning.

**Key Relationships:** Association, Specialisation, Composition, Aggregation.

**Example Scenario:** Documenting the canonical business entity model for a telecoms company: Customer, Account, Product, Subscription, Service, and their relationships — used to govern data exchange between systems.

---

### Product Viewpoint

**Purpose:** To show the products the business offers, the services and processes they are composed of, and the actors involved.

**Audience:** Product managers, business architects, marketing.

**Elements Used:** Product, Business Service, Business Process, Business Actor, Business Role, Business Interface.

**Key Relationships:** Composition, Aggregation, Realisation, Association.

**Example Scenario:** Mapping a bank's "Business Current Account" product to the services it bundles (online banking, overdraft facility, payment processing) and the internal processes that deliver each.

---

## Application Layer Viewpoints

### Application Viewpoint (Behaviour)

**Purpose:** To show how application components collaborate and communicate to realise application behaviour.

**Audience:** Solution architects, integration architects, development leads.

**Elements Used:** Application Component, Application Collaboration, Application Service, Application Function, Application Interaction, Application Interface, Data Object.

**Key Relationships:** Serving, Triggering, Flow, Composition, Assignment.

**Example Scenario:** Showing how the Order Management System orchestrates calls to the Inventory Service, Pricing Engine, and Notification Service to process a customer order.

---

### Application Cooperation Viewpoint

**Purpose:** To show the relationships between application components, especially integration and communication patterns.

**Audience:** Integration architects, middleware teams, solution architects.

**Elements Used:** Application Component, Application Interface, Application Service, Application Collaboration.

**Key Relationships:** Serving, Association, Composition.

**Example Scenario:** A map of all application components and their integration points in a complex enterprise landscape, showing where point-to-point integrations should be replaced with an enterprise service bus.

---

### Application Usage Viewpoint

**Purpose:** To show how business processes and roles use application services.

**Audience:** Business process owners, solution architects, business analysts.

**Elements Used:** Business Role, Business Process, Application Service, Application Component, Application Interface.

**Key Relationships:** Serving, Assignment.

**Example Scenario:** Showing which business roles (e.g., Claims Processor, Underwriter) use which application services (e.g., Claims Management System, Policy Administration) at which stage of the Claims Handling process.

---

## Technology Layer Viewpoints

### Infrastructure (Technology) Viewpoint

**Purpose:** To show the technology components (nodes, devices, system software) and their communication paths.

**Audience:** Infrastructure architects, operations teams, security architects.

**Elements Used:** Node, Device, System Software, Technology Interface, Path, Communication Network, Artefact.

**Key Relationships:** Composition, Assignment, Serving, Association.

**Example Scenario:** The cloud landing zone design showing VPCs, subnets, load balancers, Kubernetes clusters, and their communication paths with security zone boundaries.

---

### Technology Usage Viewpoint

**Purpose:** To show how application components are deployed on technology nodes.

**Audience:** Solution architects, infrastructure architects, operations.

**Elements Used:** Application Component, Node, Device, System Software, Artefact, Technology Service.

**Key Relationships:** Assignment, Realisation, Serving.

**Example Scenario:** Showing how each microservice in an e-commerce platform is deployed onto a container cluster, what the container runtime is, and which shared technology services (databases, message queues) they depend on.

---

### Deployment and Use Viewpoint

**Purpose:** To show the full stack from business use through to physical deployment, in a single view.

**Audience:** Solution architects, delivery teams, DevOps.

**Elements Used:** Business Process/Role + Application Component + Node/Device (all three layers stacked).

**Key Relationships:** Serving, Assignment, Realisation.

**Example Scenario:** An end-to-end view showing that the "Checkout" business process is supported by the "Checkout Application," which is deployed on a Kubernetes node in the "Production AWS cluster."

---

## Layered Viewpoints

### Layered Viewpoint

**Purpose:** To provide a comprehensive view across all layers — Business, Application, Technology — showing how elements in each layer are connected.

**Audience:** Enterprise architects, CTO/CIO, solution architects.

**Elements Used:** All layers and aspects — typically a curated subset for readability.

**Key Relationships:** All inter-layer relationships: Serving, Realisation, Assignment.

**Example Scenario:** An architecture overview diagram for a new digital channel showing the end-to-end stack: business processes → application services → platform infrastructure, in a single coherent layered diagram. Used as a "communication diagram" for executive audiences.

---

## Implementation and Migration Viewpoints

### Project Viewpoint

**Purpose:** To show the relationships between work packages, projects, and the architecture elements they implement or affect.

**Audience:** Programme managers, project managers, architects.

**Elements Used:** Work Package, Deliverable, Implementation Event, Business Actor, Application Component, Technology Node.

**Key Relationships:** Association, Triggering, Flow, Realisation.

**Example Scenario:** A programme plan showing which projects deliver which capabilities, what deliverables are produced, and the sequencing dependencies between work packages.

---

### Migration Viewpoint

**Purpose:** To show the transition from baseline to target through one or more plateau states.

**Audience:** Enterprise architects, programme management, business owners.

**Elements Used:** Plateau, Gap, Work Package, all architecture elements.

**Key Relationships:** Association, Realisation.

**Example Scenario:** Showing the "As-Is" plateau (legacy CRM), "Transition" plateau (CRM coexistence with new platform), and "Target" plateau (single CRM platform) with the gaps and work packages that move the architecture from one plateau to the next.

---

### Implementation and Migration Viewpoint

**Purpose:** To show both implementation projects and migration elements together — a combined roadmap view.

**Audience:** Programme sponsors, enterprise architects, delivery leads.

**Elements Used:** Work Package, Deliverable, Plateau, Gap, Implementation Event, and the architecture elements being changed.

**Key Relationships:** Association, Triggering, Realisation, Flow.

**Example Scenario:** A timeline-structured view showing quarterly plateaus, what changes are delivered in each phase, and how gaps are progressively closed on the path from baseline to target state.
