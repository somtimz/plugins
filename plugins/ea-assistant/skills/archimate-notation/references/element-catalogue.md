# ArchiMate 3.x Element Catalogue

This catalogue covers all ArchiMate 3.x element types organised by layer and aspect. For each element, the entry provides the layer, aspect, description, notation symbol description, and an example usage in an enterprise architecture context.

ArchiMate 3.x defines three main layers — Strategy, Business, Application, Technology, Physical, and Implementation & Migration — plus cross-cutting Motivation and Composition elements.

---

## Notation Conventions

ArchiMate uses a consistent visual grammar:
- **Shape:** Each element type has a defined shape (rectangle with a type badge).
- **Badge (internal icon):** A small icon in the top-right corner of the rectangle identifies the element type within its layer.
- **Colour (convention, not standard):** Many tools use colour conventions — yellow/gold for Business, light blue for Application, green for Technology. These are not mandated by the standard.
- **Aspect:** Passive Structure (things acted upon), Active Structure (things that act), Behaviour (actions performed).

---

## Motivation Layer

Elements in the Motivation layer describe the reasons, goals, and constraints that drive architecture decisions.

| Element | Description | Notation | Example |
|---|---|---|---|
| Stakeholder | A role or group with an interest in the architecture | Rectangle with stick-figure badge | "IT Director", "Regulator", "End Customer" |
| Driver | An external or internal condition motivating change | Rectangle with arrow-up badge | "Regulatory change (DORA)", "Cost pressure", "Customer growth" |
| Assessment | An evaluation of a driver — e.g., a risk or strength | Rectangle with magnifying glass badge | SWOT analysis result, risk assessment outcome |
| Goal | A high-level desired outcome | Rectangle with target/bullseye badge | "Reduce time-to-market", "Achieve 99.9% availability" |
| Outcome | A concrete end result associated with a goal | Rectangle with outcome badge | "Reduced incident response time by 40%" |
| Principle | A normative statement guiding architecture decisions | Rectangle with principle badge | "Prefer open standards", "Data is an asset" |
| Requirement | A statement of need that must be satisfied | Rectangle with requirement badge | "The system must support 10,000 concurrent users" |
| Constraint | A restriction on implementation choices | Rectangle with constraint badge | "Must deploy within existing AWS account", "Budget cap of $2M" |
| Meaning | The knowledge or expertise behind a concept | Rectangle with meaning badge | Definition of "Customer" as used in this enterprise |
| Value | The worth or benefit of something to stakeholders | Rectangle with value badge | "Real-time inventory visibility reduces stockouts" |

---

## Strategy Layer

The Strategy layer describes strategic capabilities and the high-level choices made to achieve goals.

| Element | Aspect | Description | Notation | Example |
|---|---|---|---|---|
| Resource | Passive Structure | An asset the enterprise owns or controls | Rectangle with resource badge | "Customer database", "Cloud platform budget", "Architecture team" |
| Capability | Behaviour | An ability the enterprise possesses or needs | Rectangle with capability badge | "Customer self-service", "Real-time analytics", "Omnichannel fulfilment" |
| Value Stream | Behaviour | A sequence of activities delivering value | Rectangle with value-stream badge | "Order-to-Cash", "Hire-to-Retire", "Procure-to-Pay" |
| Course of Action | Behaviour | A strategy or approach to achieve a goal | Rectangle with course-of-action badge | "Adopt cloud-native architecture", "Consolidate CRM systems" |

---

## Business Layer

The Business layer describes business processes, functions, and the organisational actors that perform them.

### Business Active Structure Elements

| Element | Description | Notation | Example |
|---|---|---|---|
| Business Actor | An organisational entity that performs behaviour | Rectangle with actor-person badge | "Finance department", "Customer", "Supplier" |
| Business Role | A responsibility assigned to an actor | Rectangle with role badge | "Order Processor", "Account Manager", "Approver" |
| Business Collaboration | Two or more business actors working together | Rounded rectangle with collaboration badge | "Sales and Operations Planning team" |
| Business Interface | A point of access to a business service | Rectangle with interface badge | "Phone channel", "Web portal", "Branch counter" |

### Business Behaviour Elements

| Element | Description | Notation | Example |
|---|---|---|---|
| Business Process | A sequence of business activities producing an outcome | Rectangle with process badge | "Customer Onboarding", "Invoice Processing" |
| Business Function | A stable capability grouping related activities | Rectangle with function badge | "Financial Reporting", "Human Resources Management" |
| Business Interaction | Behaviour performed by two or more collaborating actors | Rectangle with interaction badge | "Contract negotiation between buyer and supplier" |
| Business Event | Something that triggers or results from a process | Rectangle with event badge | "Order placed", "Payment received", "Contract expired" |
| Business Service | Externally visible behaviour offered to the environment | Rectangle with service badge | "Order placement service", "Account inquiry service" |

### Business Passive Structure Elements

| Element | Description | Notation | Example |
|---|---|---|---|
| Business Object | A concept used or created by the business | Rectangle with object badge | "Contract", "Invoice", "Customer Record", "Policy" |
| Contract | A formal or informal agreement | Rectangle with contract badge | "Service Level Agreement", "Employment contract" |
| Representation | A perceptible form of information | Rectangle with representation badge | "PDF invoice", "Paper form", "Screen layout" |
| Product | A coherent bundle of services and objects offered | Rectangle with product badge | "Premium savings account", "Managed IT service bundle" |

---

## Application Layer

The Application layer describes software applications and the services and data they provide.

### Application Active Structure Elements

| Element | Description | Notation | Example |
|---|---|---|---|
| Application Component | A modular, self-contained unit of software | Rectangle with component badge | "CRM System", "Payment Gateway", "API Gateway" |
| Application Collaboration | Multiple components working together | Rounded rectangle with collaboration badge | "Frontend + backend collaboration for checkout" |
| Application Interface | A point of access to an application service | Rectangle with interface badge | "REST API endpoint", "SOAP web service", "UI screen" |

### Application Behaviour Elements

| Element | Description | Notation | Example |
|---|---|---|---|
| Application Function | Internal capability of an application component | Rectangle with function badge | "Validate order", "Calculate tax", "Authenticate user" |
| Application Interaction | Behaviour involving multiple components | Rectangle with interaction badge | "Synchronous call from Order Service to Inventory Service" |
| Application Process | A sequenced set of application functions | Rectangle with process badge | "End-to-end checkout process across services" |
| Application Event | Something of significance to an application | Rectangle with event badge | "UserRegistered event", "OrderShipped event" |
| Application Service | Externally visible behaviour provided by a component | Rectangle with service badge | "Customer lookup service", "Report generation service" |

### Application Passive Structure Elements

| Element | Description | Notation | Example |
|---|---|---|---|
| Data Object | A unit of information managed by applications | Rectangle with data-object badge | "Customer record", "Transaction log", "Product catalogue" |

---

## Technology Layer

The Technology layer describes the hardware, infrastructure, and system software that support the application layer.

### Technology Active Structure Elements

| Element | Description | Notation | Example |
|---|---|---|---|
| Node | A computational or physical resource | Rectangle with node badge | "Application server", "Database server", "Container cluster" |
| Device | A physical hardware device | Rectangle with device badge | "Laptop", "ATM", "Network switch", "IoT sensor" |
| System Software | Software managing hardware resources | Rectangle with system-software badge | "Operating system", "Middleware", "Container runtime (Docker)" |
| Technology Collaboration | Multiple nodes working together | Rounded rectangle with collaboration badge | "Kubernetes cluster of 3 nodes" |
| Technology Interface | A point of access to a technology service | Rectangle with interface badge | "JDBC connection", "SSH endpoint", "HTTPS port" |
| Path | A communication link between nodes | Line with path symbol | "HTTPS link between web server and API server" |
| Communication Network | A set of communication links | Rectangle with network badge | "Corporate WAN", "Internet", "VPC" |

### Technology Behaviour Elements

| Element | Description | Notation | Example |
|---|---|---|---|
| Technology Function | Internal behaviour of a node | Rectangle with function badge | "Load balancing", "Data encryption at rest" |
| Technology Process | A sequenced set of technology functions | Rectangle with process badge | "Backup and recovery process", "Certificate rotation process" |
| Technology Interaction | Behaviour involving multiple nodes | Rectangle with interaction badge | "Data replication between primary and standby database" |
| Technology Event | A technology-level occurrence | Rectangle with event badge | "Node failure event", "CPU threshold exceeded" |
| Technology Service | Externally visible capability of infrastructure | Rectangle with service badge | "Database service", "Messaging service", "DNS service" |

### Technology Passive Structure Elements

| Element | Description | Notation | Example |
|---|---|---|---|
| Artefact | A piece of data used or produced by technology | Rectangle with artefact badge | "Deployment package", "Log file", "Configuration file", "Container image" |

---

## Physical Layer

The Physical layer describes the physical world — materials, machinery, and physical distribution networks.

| Element | Description | Example |
|---|---|---|
| Equipment | Physical machinery and devices | "Server rack", "Point-of-sale terminal", "Manufacturing robot" |
| Facility | A physical structure or location | "Data centre building", "Warehouse", "Office floor" |
| Distribution Network | A physical network for distributing goods or energy | "Logistics delivery network", "Power grid" |
| Material | Tangible goods consumed or produced | "Raw materials", "Packaged product", "Printed document" |

---

## Implementation and Migration Layer

Used for planning and tracking the transition from baseline to target architecture.

| Element | Description | Example |
|---|---|---|
| Work Package | A unit of work to implement a change | "Phase 1 CRM migration", "API gateway deployment sprint" |
| Deliverable | A formally defined result of work | "Architecture Definition Document", "Test report", "Deployed system" |
| Implementation Event | A significant milestone or event | "Go-live", "User acceptance sign-off", "Cutover date" |
| Gap | The difference between baseline and target | "Missing real-time reporting capability", "No API layer in baseline" |
| Plateau | A relatively stable state of architecture | "As-is state", "Transition state 1", "Target state" |

---

## Composite and Grouping Elements

| Element | Description | Example |
|---|---|---|
| Grouping | An arbitrary collection of related elements | "Domain: Customer Management" — groups all customer-related elements |
| Junction | A split or merge point in a relationship flow | Used to show that a service requires both A and B, or A or B |
| Location | A geographic or logical place | "Sydney data centre", "AWS ap-southeast-2 region", "Customer site" |

---

## Relationship Types Summary

| Relationship | Symbol | Meaning |
|---|---|---|
| Composition | Filled diamond line | One element is composed of another |
| Aggregation | Open diamond line | One element groups or contains another loosely |
| Assignment | Circle with line | Active structure assigned to behaviour |
| Realisation | Dashed arrow with open head | One element realises another (e.g., process realises service) |
| Serving | Line with filled arrowhead | One element serves another (provides a service to) |
| Access | Dashed line with open arrowhead | Behaviour accesses a passive element (read/write/read-write) |
| Influence | Dashed line with open arrow | One element influences another |
| Triggering | Solid line with filled arrowhead | One behaviour triggers another |
| Flow | Dashed line with filled arrowhead | Transfer of information or material |
| Specialisation | Line with open triangle | One element is a specialisation of another |
| Association | Plain line | Generic non-specific relationship |
