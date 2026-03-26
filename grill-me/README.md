# Grill Me

A Claude Code plugin for stress-testing strategies, decisions, and designs through relentless structured interviewing.

## Skills

| Skill | Best for |
|---|---|
| `grill-me-strategy` | Depth-first clarification of any strategy, decision, or design |
| `grill-me-stress-test` | Pressure-testing strategic logic, assumptions, and execution realism |
| `grill-me-boardroom` | Board and executive preparation — simulates tough panel questioning |
| `grill-me-premortem` | Risk discovery — assumes failure and works backwards |
| `grill-me-decision` | Converting sprawling discussion into a clean decision memo |
| `grill-me-design` | Critiquing service, org, UX, or concept design against design principles |
| `grill-me-boardroom-strategy` | Hybrid: depth + board pressure + pre-mortem — best for senior leadership work |

### When to use which

| Goal | Skill |
|---|---|
| Idea clarification | `grill-me-strategy` |
| Strategic rigour | `grill-me-stress-test` |
| Board or executive prep | `grill-me-boardroom` |
| Risk and failure discovery | `grill-me-premortem` |
| Turning discussion into a decision | `grill-me-decision` |
| Design quality | `grill-me-design` |
| Leadership work (strategy + board + risk) | `grill-me-boardroom-strategy` |

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

## License

[MIT](./LICENSE)
