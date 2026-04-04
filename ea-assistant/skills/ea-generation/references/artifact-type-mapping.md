# Artifact Type Mapping

Maps artifact names to the `--type` value passed to the generation scripts, and defines the primary output format.

| Artifact Name | `{script-type}` | Primary Format | Mermaid Available |
|---|---|---|---|
| Architecture Vision | `vision` | docx | No |
| Stakeholder Map | `stakeholder-map` | mermaid | Yes |
| Business Architecture | `business` | docx | No |
| Gap Analysis | `gap-analysis` | docx | No |
| Architecture Roadmap | `roadmap` | mermaid | Yes |
| Requirements Register | `requirements-register` | docx | No |
| Capability Map | `capability-map` | mermaid | Yes |
| Application Portfolio | `app-portfolio` | docx | No |
| Data Architecture | `data` | docx | No |
| Migration Plan | `roadmap` | pptx | No |
| Risk Register | `risk-register` | docx | No |
| Implementation Roadmap | `roadmap` | pptx | No |

## Generation Mechanisms

| Mechanism | Used for |
|---|---|
| **python-docx / python-pptx scripts** (`generate-docx.py`, `generate-pptx.py`) | Individual structured artifacts — section-by-section formatting, embedded tables, diagram embedding |
| **pandoc** | Consolidated Architecture Report (`/ea-publish` only) — single-pass Markdown → DOCX for flat narrative |

When generating a single artifact via `/ea-generate docx`, always use the python-docx script. Pandoc is used only by `/ea-publish`.
