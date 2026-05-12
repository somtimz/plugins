# ABB Catalogue — Standard Reference Architecture Building Blocks

A reusable catalogue of vendor-neutral Architecture Building Blocks (ABBs) organised by domain. Use these as starting points when populating the ABB Register in Phase C and Phase D. Each name follows the **noun-phrase convention** (logical function, not action or product). Parenthetical notes are illustrative — do not treat them as implementation mandates.

---

## Core Infrastructure ABBs

| ABB Name | Logical Function | Typical Categories |
|---|---|---|
| Compute Services | Provides virtualised or abstracted compute resources for running workloads | VMs, containers, serverless functions |
| Storage Services | Provides durable, scalable persistence for structured and unstructured data | Block, file, object storage |
| Network Services | Provides Layer 2/3 connectivity, segmentation, and traffic management across the estate | LAN, WAN, routing, switching |
| DNS Services | Provides name resolution and service discovery for internal and external endpoints | Internal DNS, external DNS, conditional forwarding |
| Load Balancing Service | Distributes incoming traffic across multiple backend instances to ensure availability and performance | Layer 4, Layer 7, global |
| Virtualisation Platform | Provides the hypervisor or abstraction layer that hosts virtual workloads | Type-1, Type-2, hosted |
| Cloud Infrastructure Platform | Provides foundational cloud-native compute, storage, and networking primitives consumed by higher-level services | Public, private, hybrid |

---

## Identity & Security ABBs

| ABB Name | Logical Function | Typical Categories |
|---|---|---|
| Identity and Access Management | Manages identity lifecycle, entitlements, and access policies across systems | Provisioning, de-provisioning, access reviews |
| Directory Services | Provides a centralised repository of users, groups, and organisational structure | Hierarchical, federated, cloud-native |
| Authentication Services | Verifies identity claims and issues security tokens for session establishment | Single sign-on, multi-factor, certificate-based |
| Endpoint Security Service | Protects endpoints from malware, exploitation, and unauthorised access | Anti-malware, EDR, application control |
| Network Security Service | Inspects, filters, and monitors network traffic to enforce security policy | Firewall, intrusion detection/prevention, proxy |
| Secrets Management Service | Securely stores, rotates, and distributes sensitive credentials and cryptographic material | Vault, key management, certificate lifecycle |
| Security Monitoring Service | Collects, correlates, and alerts on security events and indicators of compromise | SIEM, SOAR, threat intelligence |

---

## Platform & Application ABBs

| ABB Name | Logical Function | Typical Categories |
|---|---|---|
| Application Hosting Platform | Provides the runtime environment for deploying and executing application code | Web server, application server, serverless runtime |
| Database Services | Provides structured or semi-structured data storage with query, transaction, and indexing capabilities | Relational, document, key-value, graph, time-series |
| API Gateway Service | Acts as a single entry point for API consumers, handling routing, transformation, rate limiting, and security | Internal, external, partner |
| Integration Services | Enables reliable message exchange and data flow between disparate systems | ESB, message queue, event bus, file transfer |
| Container Platform | Provides orchestration, scheduling, and lifecycle management for containerised workloads | Orchestration, registry, networking, storage |
| Delivery Automation Platform | Automates build, test, packaging, and deployment activities across the software lifecycle | CI pipeline, CD pipeline, artifact repository |
| Configuration Management Service | Maintains desired state definitions and enforces consistency across infrastructure and application configurations | Declarative, imperative, policy-as-code |

---

## Data & Analytics ABBs

| ABB Name | Logical Function | Typical Categories |
|---|---|---|
| Data Lake Storage | Provides a scalable repository for raw, unprocessed data in native formats | Structured, semi-structured, unstructured |
| Data Warehouse Service | Provides an integrated, subject-oriented store optimised for analytical querying and reporting | Relational, columnar, massively parallel |
| Data Integration Service | Extracts, transforms, and loads data between source and target systems | Batch, streaming, change-data-capture |
| Business Intelligence Platform | Enables self-service and governed reporting, dashboarding, and exploratory analytics | Ad-hoc, scheduled, embedded |

---

## Operations & Support ABBs

| ABB Name | Logical Function | Typical Categories |
|---|---|---|
| Monitoring and Alerting Service | Collects metrics, traces, and health signals and raises alerts when thresholds are breached | Infrastructure, application, synthetic |
| Logging Service | Aggregates, indexes, and retains log data from applications and infrastructure for search and audit | Structured, unstructured, long-term archival |
| Backup and Recovery Service | Creates and restores copies of data and systems to meet recovery objectives | Full, incremental, snapshot, immutable |
| IT Service Management Platform | Manages incident, problem, change, and service-request lifecycles | Ticketing, knowledge base, SLA tracking |
| Asset and Configuration Management Service | Maintains an authoritative inventory of hardware, software, and configuration items and their relationships | Discovery, reconciliation, dependency mapping |

---

## End-User & Collaboration ABBs

| ABB Name | Logical Function | Typical Categories |
|---|---|---|
| End-User Computing Platform | Provides the workspace, device, and virtual-desktop environment for knowledge workers | Physical, virtual (VDI), web-based |
| Email and Messaging Service | Provides electronic messaging, calendaring, and contact management for the organisation | On-premise, cloud, hybrid |
| Collaboration Platform | Enables real-time and asynchronous teamwork, document co-authoring, and persistent conversation channels | Chat, video, whiteboard, shared workspace |
| Mobile Device Management Service | Enforces security policy, distributes applications, and manages the lifecycle of mobile endpoints | Corporate-owned, BYOD, containerised |

---

## Usage Notes

- **Start from this catalogue** when defining ABBs in Phase C/D to promote reuse and naming consistency.
- **Do not copy vendor names** into the Name or Description fields — the parenthetical examples in the table above are for reference only.
- **Map each ABB to at least one REQ-NNN** to ensure traceability.
- **Split or combine** catalogue entries as needed for your engagement's granularity — e.g. "Database Services" can be split into "Relational Database Service" and "NoSQL Database Service" if both are required.
- **Add domain-specific ABBs** not listed here; this catalogue covers common enterprise infrastructure, not industry-specific components.

---

*See `ea-concepts.md` for the full ABB definition, naming convention, and disambiguation from SBBs, Capabilities, and Requirements.*
