# Research Agent

A Claude Code plugin providing a Lead Research Analyst agent that conducts deep, evidence-based research into any topic, codebase, or document set.

## Agent

| Agent | Description |
|---|---|
| `research-agent` | Deep research with evidence gathering, contradiction detection, and executive-ready synthesis |

## What it does

The agent works in three phases:

1. **Discovery & Mapping** — identifies Core Pillars and Known Unknowns before drawing any conclusions
2. **Evidence Gathering** — finds primary evidence for every claim; actively seeks counter-evidence and contradictions; traces execution flows in codebases
3. **Synthesis** — produces a structured report with Executive Summary, Evidence Base, Risks & Uncertainties, Strategic Implications, and Recommended Next Steps

Every major conclusion carries a **Confidence Score** (High / Med / Low). Dead ends are reported immediately rather than papered over.

Before starting, the agent asks one question about the **Depth vs. Breadth** trade-off to calibrate scope.

## Installation

```bash
/plugin install research-agent
```

## Usage

Point the agent at what you want researched:

```
@research-agent

Analyse the authentication system in this codebase — how it works, where it is fragile, and what a senior engineer should know before touching it.
```

```
@research-agent

Research the current state of event sourcing patterns in distributed systems.
```

## License

[MIT](./LICENSE)
