# AI Security Guidance for TOGAF ADM

As organisations shift from traditional software into the **GenAI and Agentic AI era**, security architecture must evolve. This reference integrates **ISO/IEC 42001** (AI Management System), **NIST AI RMF** (Risk Management Framework), and **OWASP Top 10 for LLMs** (Technical Vulnerabilities) into the standard TOGAF ADM lifecycle.

Load this reference when the engagement involves AI systems, GenAI capabilities, agentic workflows, or when the user asks about AI security architecture.

---

## 1. Strategic AI Security Alignment

AI security is unique because it introduces **non-deterministic risks** (hallucinations, bias) and **new attack surfaces** (prompt injection). Treat these three frameworks as a unified stack:

- **ISO/IEC 42001** — Provides the **Management System (AIMS)**. The governance shell that ensures leadership accountability, policy, and continuous improvement for AI.
- **NIST AI RMF** — Provides the **Risk Lexicon**. Use its Govern / Map / Measure / Manage functions to translate technical AI risks into business impact summaries for stakeholders.
- **OWASP Top 10 for LLMs** — Provides the **Technical Controls**. The tactical checklist for developers and security engineers to mitigate specific GenAI threats (e.g. Prompt Injection LLM01, Insecure Output Handling LLM02).

---

## 2. Enhanced ADM Lifecycle for AI Security

| ADM Phase | AI-Enhanced Security Activities | Supporting Standard |
| :--- | :--- | :--- |
| **Preliminary** | Establish the AI Management System (AIMS) scope. Define "AI Trustworthiness" principles tailored to the organisation's risk appetite. | ISO/IEC 42001 (Cl. 4–6) |
| **Phase A: Vision** | Identify AI-specific stakeholders (Data Scientists, Model Owners). Define the high-level AI risk profile (e.g. Internal vs. Public-facing GenAI). | NIST AI RMF (Govern) |
| **Phase B: Business** | Map business capabilities to AI "impact zones." Establish human-in-the-loop requirements for automated decisions. | ISO/IEC 42001 (Annex A.4) |
| **Phase C: IS Architecture** | **Data:** Define RAG security controls. **Application:** Model-agnostic design with integrated guardrails against the OWASP LLM Top 10. | OWASP LLM Top 10 |
| **Phase D: Technology** | Architecture of AI Firewalls and Prompt Gateways. Secure storage for model weights and training datasets. VPC zoning for AI inference engines. | NIST AI RMF (Measure/Manage) |
| **Phase E: Opportunities** | Evaluate AI-as-a-Service vs. self-hosted models. Conduct Red Teaming for the candidate AI architecture. | MITRE ATLAS |
| **Phase G: Governance** | Ensure implementation conforms to the ISO 42001 AIMS. Validate that OWASP-suggested mitigations (e.g. input sanitisation) are present in code. | ISO 42001 (Internal Audit) |

---

## 3. OWASP Top 10 for LLMs — Phase C Focus

While TOGAF addresses broad enterprise structure, the **OWASP Top 10 for LLM Applications** fills the gap in **Phase C (Application Architecture)**. Every target architecture should demonstrate how it addresses:

- **Direct & Indirect Prompt Injection (LLM01)** — System-level guardrails preventing external inputs from hijacking model instructions.
- **Sensitive Information Disclosure (LLM06)** — PII-masking layers between the LLM and the user interface.
- **Insecure Output Handling (LLM02)** — Treating LLM outputs as untrusted data to be sanitised before execution (critical in Agentic AI scenarios).
- **Training Data Poisoning (LLM03)** — Integrity controls on ground-truth data used for fine-tuning or RAG corpus construction.

---

## 4. Critical Synthesis and Design Conflicts

**Speed vs. Governance**
ISO 42001 requires rigorous documentation; GenAI projects often follow rapid prototyping cadences. Synthesis: use automated AI Policy Orchestration tools to map real-time code changes to compliance artefacts, reducing documentation lag.

**The Attribution Problem**
In agentic workflows where AI triggers other systems, responsibility for a security failure is ambiguous. Apply the **Principle of Least Privilege** not just to users but to AI Agents themselves — scope each agent's permissions to the minimum required for its declared function (consistent with Zero Trust and NIST SP 800-207).

---

## References

- [AI Risk Frameworks Shaping Enterprise Compliance — Alice](https://alice.io/blog/ai-risk-management-frameworks-nist-owasp-mitre-maestro-iso)
- [NIST AI RMF vs ISO 42001: 5 Key Differences — Vanta](https://www.vanta.com/resources/nist-ai-rmf-and-iso-42001)
- [NIST AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [ISO/IEC 42001 AI Management System Standard](https://www.iso.org/standard/81230.html)
