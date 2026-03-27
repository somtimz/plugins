# Grill Me

A Claude Code plugin for stress-testing strategies, decisions, and designs through relentless structured interviewing.

## Skills

| Skill | Best for |
|---|---|
| `grill-me-stress-test` | Pressure-testing strategic logic, assumptions, and execution realism |
| `grill-me-premortem` | Risk discovery and risk register review — generate new risks or critique existing ones |
| `grill-me-decision` | Converting sprawling discussion into a clean decision memo |
| `grill-me-design` | Critiquing service, org, UX, or concept design against design principles |
| `grill-me-software-design` | Deep technical review of software architecture — patterns, coupling, APIs, data models, testability |
| `grill-me-infra-design` | Deep technical review of infrastructure — topology, resilience, blast radius, cost, observability |
| `grill-me-artifact` | Section-by-section review of a structured document — completeness, traceability, consistency |
| `grill-me-diagram` | Visual design review of architecture diagrams — topology, missing components, anti-patterns |
| `grill-me-boardroom-strategy` | Hybrid: strategic depth + board pressure + pre-mortem — the most comprehensive review |

### When to use which

| Goal | Skill |
|---|---|
| Clarify or stress-test a strategy | `grill-me-stress-test` |
| Generate risks (pre-mortem) | `grill-me-premortem` (mode: Generate) |
| Review an existing risk register | `grill-me-premortem` (mode: Review) |
| Turn discussion into a decision | `grill-me-decision` |
| Board or executive preparation | `grill-me-boardroom-strategy` |
| Service, UX, or org design quality | `grill-me-design` |
| Software architecture review | `grill-me-software-design` |
| Infrastructure and reliability review | `grill-me-infra-design` |
| Structured document quality check | `grill-me-artifact` |
| Architecture diagram review | `grill-me-diagram` |

## Installation

```bash
/plugin install grill-me
```

## Usage

Invoke any skill and describe what you want stress-tested:

```
/grill-me-boardroom-strategy

We are planning to consolidate three regional IT teams into a single shared services function over 18 months.
```

The skill interviews you one question at a time, then produces a structured synthesis when the topic is sufficiently tested.

### Risk review example

```
/grill-me-premortem

Here is our risk register for the ERP migration project:
[paste risk table or reference artifact]
```

The skill will ask whether you want to **generate** new risks (pre-mortem) or **review** existing ones. If you provide a risk register, it defaults to review mode.

## License

[MIT](./LICENSE)
