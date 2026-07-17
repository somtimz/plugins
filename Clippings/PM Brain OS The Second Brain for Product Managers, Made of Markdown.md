---
title: "PM Brain OS: The Second Brain for Product Managers, Made of Markdown"
source: "https://www.productcompass.pm/p/pm-brain-os"
author:
  - "[[Paweł Huryn]]"
published: 2026-05-20
created: 2026-06-19
description: "Open-source second brain for product managers. Markdown files + Claude Code skill. 17 PM scenarios, 99.5% eval pass. MIT-licensed. One-command install."
tags:
  - "clippings"
---
### A folder of files on your laptop. Claude reads them before answering, writes to them after, sweeps them every Friday. Open source. 17 synthetic PM scenarios, 404 of 406 checks pass (≈99.5%).

> ***Research preview.** The architecture has months of dogfooding behind it on my content work. The product as installed by real PMs in real organizations is days old. The eval suite is the floor; your install feedback is how it gets better. Monday May 26, I'm running a [live workshop session](https://go.productcompass.pm/premium) for paid subscribers, and there's a dedicated **#pm-brain** Slack channel for 1:1 install help. Details in §11.*

---

You manage one product. Your context lives in five places: Notion, Linear, Slack, your dashboards, and your head.

![Your context lives in five places: Notion, Linear, Slack, your dashboards, and your head.](https://substackcdn.com/image/fetch/$s_!Fhal!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e907f1f-e32a-4e97-939c-bc12e9c9b4ae_2472x1083.png)

Your context lives in five places: Notion, Linear, Slack, your dashboards, and your head.

You ship a feature. Six weeks later, nobody remembers why you killed the other option. The customer interview that should have informed the call is buried in a doc you forgot to link. The stakeholder who pushed back has a new concern, and the old one is gone.

I built a second brain for it.

Folder of markdown files in a git repo. A small operating manual (CLAUDE.md) tells Claude how to use them. The agent reads them before answering, writes to them after, sweeps them weekly.

> No vector database. No embeddings. No cloud. No auto-tagging. Everything is grep-able. You can open the entire brain in any editor.

It's also not an agent memory system. Those embed everything you feed them so the agent can recall it later. PM Brain does the opposite. You write down only what matters, in markdown you can read, and the agent reads what you wrote. The point isn't agent recall. It's PM judgment with an audit trail.

![A PM Brain doesn’t store everything. It promotes only what’s recurring, decision-relevant, or strategy-relevant.](https://substackcdn.com/image/fetch/$s_!6XBy!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf49c706-852e-4ba3-80f4-56d2d5cb8ec1_2474x1184.png)

A PM Brain doesn’t store everything. It promotes only what’s recurring, decision-relevant, or strategy-relevant.

A PM Brain doesn’t store everything. It promotes only what’s recurring, decision-relevant, or strategy-relevant. Everything else stays in working memory until it earns its way into the durable layer.

> This post is the long version. The short version is in the README. The shortest version: open Claude Code in an empty folder, run ***/pm-brain***, answer a five-batch interview, and you have a **working brain in 10 minutes**.

---

## What You’ll Learn

- Why your PM context decays at month three, and where the trail goes
- The five failure modes that kill most AI memory systems, and the five structural choices that answer them
- A week with PM Brain, told as Lena’s first five days on a real account
- The architecture: five knowledge areas, three lifecycle areas, one CLAUDE.md
- Provenance, the unique technical idea, and why it carries more weight than people expect
- The six commands you’ll actually use
- How to install it today, and what to do in week one

---

## 1\. Why This Exists

Most AI memory systems fail by month three. The same five failure modes show up across vector-DB memory, RAG over your docs, “AI second brain” apps, and most agent-memory frameworks:

1. Accumulate, never synthesize. Every interview gets stored. Nothing compresses. The system becomes a landfill.
2. Flatten contradictions into consensus. Three interviews say three things, summarized into one bland insight. The disagreement was the signal.
3. Drift silently from strategy. Two months of decisions point one way. The strategy doc points another. Nobody surfaces the tension.
4. Lose decision context. Why did we ship X? What were the alternatives? Most systems store the decision and lose the reasoning.
5. Overload context. The agent loads too much, gets confused, generates shallow output.

![PM Brain: Why most AI memory systems fail by month three](https://substackcdn.com/image/fetch/$s_!uOtz!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd5db56ec-29cc-40e4-b42d-78a38084f7b8_2443x947.png)

PM Brain: Why most AI memory systems fail by month three

PM Brain is structured around five corresponding design choices, each one targeting a specific failure:

1. Epistemic boundaries. Every claim is tagged: observation, interpretation, hypothesis, assumption, decision. A Slack comment is not automatically truth.
2. A maintenance model that runs. Weekly sweep. Stale evidence flagged, recurring patterns compressed, contradictions preserved.
3. Flag, never gate. The system surfaces. The PM decides. The moment it becomes a blocker, it dies.
4. Inspectable, not opaque. Markdown, repo-native, editable, version-controllable. Trust is the bottleneck.
5. Resists complexity creep. No taxonomies, no agent swarms, no graph ontologies. Opinionated and lightweight.

![Five failure modes show up consistently across vector-DB memory, RAG over your docs, “AI second brain” apps, and most agent-memory frameworks. ](https://substackcdn.com/image/fetch/$s_!nlvJ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96d80bf1-da8f-4d0a-968e-cbaef9886b7f_2490x996.png)

Five failure modes show up consistently across vector-DB memory, RAG over your docs, “AI second brain” apps, and most agent-memory frameworks.

Full mapping with the architecture choices behind each fix: [docs/why-this-matters.md](https://github.com/phuryn/pm-brain/blob/main/docs/why-this-matters.md).

---

## 2\. A Week With PM Brain: Lena’s First Five Days

The fastest way to see what PM Brain does is to watch someone use it. This is a short story. The character is invented, the artifacts are real-shaped, the team and the tool are not. The full version lives in [docs/walkthrough.md](https://github.com/phuryn/pm-brain/blob/main/docs/walkthrough.md).

**Lena Vasquez** just took over PM for a B2B project-collaboration tool called **Mosaic**. The previous PM left a Notion workspace, a Jira project, and a 3-month-old Miro discovery board.

### 🚀 Monday: onboarding

Lena plugs in the Notion, Jira, and Miro app connectors, then runs ***/pm-brain***. The skill enters **migration mode**, runs a five-batch interview (about 10 minutes), then reads through the three tools.

Forty-five minutes later: a folder of markdown files, an ***INDEX.md***, and a short onboarding report. Buried in it:

> **Tension surfaced.** The strategy doc says the north-star is *activation: 60% of new accounts invite a teammate by day 3*. But of 47 Jira tickets shipped in Q1 and Q2, 38 are tagged “enterprise permissions” or “admin tooling.” Only 4 touch the activation funnel.

A new PM usually catches this in week three, after they’ve already built plans on top of the official story. Lena has it on day one because the brain cross-checked two folders humans tend to read separately.

### 🎧 Tuesday: a discovery call

Lena has a 45-minute call with **Talia Brennan**, Head of Operations at Northridge Construction. Quiet user, seat count plateaued, no complaints. After the call: ***/ingest northridge-talia-transcript.md***.

Four things happen in parallel:

1. The transcript copies to ***source/interviews/...***. Read-only. Audit anchor.
2. A synthesis note lands in ***ingestion/interviews/...*** with observations tagged by speaker and date.
3. The brain tells Lena that two stakeholders flagged the same invite-link friction back in March, that there’s a candidate hypothesis the previous PM never tested, and that the Miro discovery board has a “magic-link onboarding?” sticky from January, never explored.
4. Talia’s observation lands as a new evidence row on the invite-link hypothesis. It promotes from ***candidate*** to ***proposed***. Three independent observations now.

One call. The weight of three.

### 📣 Wednesday: the loud stakeholder

Slack lights up. **Rahul Pillai** (marketing): *“We need to ship dark mode this quarter. Every demo asks for it. It’s killing conversion.”*

Loud, recent, plausible. A less-confident PM might tell engineering to start scoping.

Lena types into Claude: *“Rahul just messaged about dark mode. Capture as verbal stakeholder claim, flag any conflict with documented evidence.”*

The brain tags the claim ***(stakeholder-verbal, rahul-pillai, 2026-05-20)***. Then it surfaces what’s documented:

> - Q1 close-loss review: 27 demos analyzed. Dark mode flagged in 2 as a wishlist item. Zero blockers.
> - Cascadia Health interview, 2026-03-15: buyer named integrations and admin controls. Not dark mode.
> - Brillstone interview, 2026-04-18: same.
> - Q2 strategy doc: activation north-star, not feature parity.

The brain doesn’t argue with Rahul. It puts his verbal claim next to 27 sales calls, two customer interviews, and the team’s stated strategy, each wearing its actual provenance.

Lena replies: *“Want to dig into this. Friday.”* She has the documented case ready and a productive conversation booked.

### 👨🏭 Thursday: engineering proposes an alternative

1:1 with **Mateus Okafor** (engineering lead): *“What if we ran a 1-week spike on magic-invite-links? If it works, we save four weeks of UI.”*

Lena adds a line. The brain records the verbal, files it as a solution option on the invite-link hypothesis, findable next to Talia’s evidence and the Miro sticky from January. The suggestion doesn’t die in Slack scrollback.

### 🧘♀️ Friday: /review, then Monday’s prep is done

Lena runs ***/review***. One page:

> **This week**
> 
> - Strategy gap (still open): flagged Monday, not raised yet.
> - Invite-link hypothesis: ***candidate*** → ***proposed***. Three observations.
> - Dark mode tension (Rahul): verbal claim captured, flagged against documented evidence. Friday meeting is your action.
> - Magic-invite-links spike (Mateus): solution option logged.
> 
> **Drifting**
> 
> - ***enterprise-permissions-v2***: no new evidence in 47 days. Revive, demote, or archive?
> 
> **For your Monday strategy meeting**
> 
> 1. Open with the strategy-vs-shipped-work gap. Activation-first or enterprise-first? One is wrong.
> 2. Bring the invite-link hypothesis forward. Three observations + one engineering alternative. Ask for a go/no-go.
> 3. Park dark mode until Friday’s meeting with Rahul.

Lena reads this in five minutes. Monday’s prep is done.

**What Lena got, in five lines:**

- **Monday:** a real question to bring into your first strategy meeting, on day one
- **Tuesday:** one call that landed with the weight of three
- **Wednesday:** documented evidence ready when a loud voice contradicted it
- **Thursday:** an engineering suggestion that didn’t die in Slack
- **Friday:** a one-page summary that made Monday’s meeting easy

None of this is automation. It’s the brain doing the small, boring work of cross-referencing what she already knew, so the judgment work, which is her job, gets easier.

---

## 3\. The Architecture

Five knowledge areas, three lifecycle areas, four ingestion modes, one maintenance loop.

![PM Brain: The Architecture. Five knowledge areas, three lifecycle areas, four ingestion modes, one maintenance loop.](https://substackcdn.com/image/fetch/$s_!sbAH!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7c340a6-f40e-43bb-a52a-406d5caf3493_2488x1246.png)

PM Brain: The Architecture. Five knowledge areas, three lifecycle areas, four ingestion modes, one maintenance loop.

Plus ***source/*** (immutable copies of original artifacts), a maintenance log, and a docs folder.

Evidence flows in one direction. It fans out at the durable layer. The same artifact updates multiple destinations in parallel. Talia’s 45-minute interview touched six files: one source copy, one ingestion record, one insight promoted to ***knowledge/users/***, one hypothesis strengthened, one stakeholder touchpoint logged, and a candidate solution option logged on the hypothesis.

![PM Brain: The cognition pipeline. Evidence flows in one direction. It fans out at the durable layer.](https://substackcdn.com/image/fetch/$s_!Wezs!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37f537f0-1ff3-4517-94c5-bba8ffd721e7_2499x1120.png)

PM Brain: The cognition pipeline. Evidence flows in one direction. It fans out at the durable layer.

When a hypothesis is confirmed, it gets promoted and a decision record is auto-drafted (status: ***pending***, waiting for your sign-off). When a decision’s reversal condition triggers, the weekly sweep surfaces it.

Most systems mash hypotheses and decisions together. They become useless.

![PM Brain: The hypothesis / decision split.](https://substackcdn.com/image/fetch/$s_!UykB!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed0b9ac2-7b58-41c6-b3e7-c49e4afca9bf_2494x1045.png)

PM Brain: The hypothesis / decision split.

---

## 4\. Provenance: Every Claim Wears a Tag

This is the load-bearing technical idea.

![PM Brain. Provenance: Every Claim Wears a Tag.](https://substackcdn.com/image/fetch/$s_!T3cB!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f2ea091-f34f-469f-b66b-fcab886a23b0_2390x780.png)

PM Brain. Provenance: Every Claim Wears a Tag.

Every claim in ***hypotheses/***, ***decisions/***, and ***knowledge/users/insights.md*** carries a small tag, a **provenance marker**, that says where it came from.

The tags carry an implicit hierarchy: documented decisions outweigh documented research, which outweighs verbal claims, which outweighs PM intuition. The brain leans on that hierarchy when evidence conflicts. The leaning is in plain text. You can override it.

The brain **enforces the vocabulary, not the workflow**. PMs have intuitions. They hear things off-the-record from execs. They inherit claims with no clear pedigree. Those are legitimate inputs. The tag just makes them wear their actual provenance instead of laundering them through a fake ***ingestion/*** record.

Three months later your CTO asks: *“Why did we kill real-time alerts?”* You open the decision file. Every evidence row carries a tag. Path-typed tags walk in two clicks to the synthesis, then to the raw transcript. Non-path tags tell you honestly that no artifact exists. Both are auditable. Only a *missing* tag is a bug.

---

## 5\. The Six Commands

![PM Brain: The Six Commands](https://substackcdn.com/image/fetch/$s_!P0aR!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ab729c5-90e2-4ce5-8020-2b08f6cd5fc6_2470x1291.png)

PM Brain: The Six Commands

**/ingest** is the workhorse. **/plan** is where the system earns its keep. A new objective lands (”reduce onboarding drop-off 20% in Q3”) and the brain loads strategy, current metrics, user insights, active hypotheses, past decisions, stakeholder constraints, then drafts the six blocks.

That output is the difference between “another second brain” and a system that does product work with you.

---

## 6\. The Maintenance Sweep

Memory systems rot in predictable ways. The weekly sweep is the forcing function that catches those failure modes before they compound. Skip ***/review*** for a month and the brain becomes a graveyard. Run it weekly and the system pays you back every Friday.

![PM Brain: Memory systems rot in predictable ways](https://substackcdn.com/image/fetch/$s_!st7_!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93a2de03-8670-4bfd-9a21-8f4a136c840b_2476x1094.png)

PM Brain: Memory systems rot in predictable ways

Eight failure modes; six checks. Dated report in ***maintenance/log/***:

1. **Stale knowledge audit.** Files not updated in 6+ weeks. Still true? Archive?
2. **Stale evidence flagging.** Market intel past 30–60 days, interviews past 90, stakeholder assumptions past 30, strategy assumptions past quarterly. Flags; doesn’t auto-decay confidence. You decide what to refresh.
3. **Hypothesis and decision hygiene.** Active hypotheses with no evidence in 30+ days. Promoted hypotheses without a corresponding decision (drafts one). Decisions whose reversal condition triggered. Pending decisions older than 14 days with blocker impact (decision debt).
4. **Stakeholder cadence and strategy tensions.** High-influence stakeholders not touched in 3+ weeks. Recent decisions or signals diverging from strategy. Surfaced as tensions, not as drift to fix.
5. **Knowledge synthesis (compression).** The highest-leverage step. Identifies recurring patterns AND recurring contradictions. Preserves minority signals: the dissenting interview, the contrarian metric, the off-pattern stakeholder concern. Compression is additive, never destructive.
6. **Archival sweep.** Shipped features inactive 90+ days. Resolved hypotheses. Closed asks. Before archiving anything, extracts durable lessons.

Twenty minutes Friday afternoon. Set a recurring calendar reminder. Without it, the brain rots.

---

## 7\. Will This Stay Healthy After a Year?

Yes. The layer the agent loads by default (your durable knowledge of strategy, product, users, market) grows logarithmically by design. The raw layer grows linearly with your activity but stays cold unless something cites it.

![PM Brain: The layer the agent loads by default (your durable knowledge of strategy, product, users, market) grows logarithmically by design.](https://substackcdn.com/image/fetch/$s_!jYwF!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa50e919e-c3be-4a04-8c42-b8fca251502c_2484x1328.png)

PM Brain: The layer the agent loads by default (your durable knowledge of strategy, product, users, market) grows logarithmically by design.

Default loads target the durable + active layers. Brain age doesn’t change what routine commands read.

The architectural payoff: plain markdown in a git repo is forward-compatible with every future Claude, every future Cursor, every future agent. The format doesn’t bind to today’s tooling. Context windows expand; your brain stays the same shape.

*Longer version with the realistic envelope numbers (~50-100 interviews/year, 10-20 active hypotheses, 10-30 stakeholders) and the four on-demand triggers that pull old material into context: [docs/scaling.md](https://github.com/phuryn/pm-brain/blob/main/docs/scaling.md).*

---

## 8\. Does It Actually Work? The Test Scoreboard

PM Brain is new. The architecture isn’t. I’ve been running the same pattern (operating manual, tags, hypotheses, decisions, weekly maintenance sweep) on my content work for months.

PM Brain is that architecture adapted to PM-specific schemas, validated against 17 scenarios I designed from PM situations I’ve shipped through, with synthetic data generated across persona, stage, and risk dimensions.

> **404 of 406 individual checks pass (≈99.5%)** on Sonnet 4.6.

The split:

- Structural checks: 329 / 329 (100%). Files exist where they should. Links resolve. Evidence rows carry valid provenance tags. Decision schemas are valid. Hypothesis statuses match the evidence claims.
- LLM-judge content checks: 75 / 77 (≈97%). Rubrics evaluating whether the brain surfaced the right contradictions, drafted the right decisions, asked the right questions.

Each scenario is multi-turn. The harness spins up a fresh brain in a temp directory, replays the inputs through claude -p, runs structural assertions after every turn, and runs LLM-judge rubrics on substance at the end. Full breakdown and snapshots in [tests/RESULTS.md](https://github.com/phuryn/pm-brain/blob/main/tests/RESULTS.md).

The point isn’t 99.5%. Most “AI memory” projects don’t have an eval suite at all. When the skill changes, the suite tells you whether it got better or worse on real-shaped PM situations, with snapshots you can diff.

---

## 9\. What It Isn't

![What PM Brain Is Not Good At](https://substackcdn.com/image/fetch/$s_!xKSq!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca4ac64f-be2c-486b-a5b1-c7c3f6a28521_2485x915.png)

What PM Brain Is Not Good At

A few notes the grid doesn’t cover:

- **The ad-hoc inbox tempts laziness.** “I’ll route this later.” No. Every ad-hoc item gets resolved in the same session. The folder is a sorting bench. The moment it becomes a backlog, it becomes a graveyard.
- **Memory promotion requires judgment.** The agent proposes what to promote. The call is yours. Rubber-stamp everything and the durable layer fills with noise. Reject everything and the system never learns.
- **Stakeholder files feel awkward at first.** Writing down what your manager cares about, in a file, in your git repo, can feel like treating people as objects. The reframe that worked for me: this isn’t about them, it’s about your continuity. You forget. The file remembers.

---

## 10\. How to Start

### Install & migrate

Two stages:

- Skill is global; brains are per-product. One shell command installs the skill (macOS / Linux / WSL / Git Bash, or Windows PowerShell).
- Then in any folder, run claude and **/pm-brain**.

The skill auto-detects what’s in the directory:

- Empty folder = **greenfield**.
- Folder with existing PM artifacts (Notion exports, meeting notes, Jira CSV) = **migration**.

Either way, a five-batch interview captures your context. The scaffold drops in. The CLAUDE.md operating manual lands at the brain root. The brain commits locally. Never pushes.

Install commands, requirements, and troubleshooting: [github.com/phuryn/pm-brain.](https://github.com/phuryn/pm-brain)

### Next: Don’t backfill old artifacts retroactively

Migration handles your current state. Don’t backfill old artifacts retroactively. Two different things:

- **Migration mode, recommended:** When you point ***/pm-brain*** at a folder with your active strategy doc, your in-flight hypotheses, your recent decisions, and your current stakeholder list, the skill reads them, organizes them, and produces a short report on what it found. That’s the goal. Let migration absorb your *current* organized PM artifacts.
- **Backfilling everything, the trap:** The temptation is to spend a weekend manually feeding 200 old interview transcripts, six months of Slack threads, and every meeting note you’ve ever taken through ***/ingest***. Don’t. If a six-month-old interview matters, it’ll come up through current work and you’ll ingest it then, with the context to know *why* it matters. Forcing stale artifacts in now wastes a weekend and clogs the durable layer with stuff the agent has no context to promote properly.

### Week 1

The system dies if these three habits don’t take hold in week one. Do them in order, in the first seven days:

1. **Ingest one real artifact today.** Paste your most recent customer interview, meeting notes, or competitor screenshot. Watch where it lands in ***ingestion/***, then which durable areas it updates. This is how you learn what the system does.
2. **Prep your next 1:1.** Before your next conversation with your highest-friction stakeholder, run ***/prep*** . Let the agent surface what to ask. The first real value is here, not in the scaffold.
3. **Run** ***/review*** **Friday.** Set a recurring calendar reminder. Twenty minutes Friday afternoon. Without it, the brain rots.

That’s week one. Don’t add anything else.

### Week 2

Ingest two more interviews. Log one decision. Add one feature file for your most active feature. Open ***knowledge/strategy.md*** and fill in the ***Non-goals*** section if the interview didn’t capture it.

### Week 3

Second ***/review***. Now you can compare two reports. Patterns start showing up: recurring contradictions, drifting strategy, hypotheses with no evidence. This is when the system starts paying off.

### Week 4+

It compounds. Every meeting note, every market signal, every decision feeds the same loop. The brain learns the shape of your product as you work.

> The goal isn’t a complete brain. The goal is a brain that **compounds over time.**

---

## 11\. A Research Preview, with Help

PM Brain is a research preview. The architecture has months of dogfooding behind it on my content work; the product as installed by real PMs is new. I want to learn what breaks in real organizations, in the first week of use.

Three things to make adoption easier:

- **Live workshop session, Monday** ~~May 25~~ **May 26, for paid subscribers.** I’ll walk through install, migration, and the first week of usage live, then take questions. See: [https://go.productcompass.pm/premium](https://go.productcompass.pm/premium)
- **Dedicated** ***[#pm-brain](https://go.productcompass.pm/premium)*** **[Slack channel](https://go.productcompass.pm/premium) for 1:1 install help (paid members).** Office Hours members get the channel. I’m in there for install pain, first-week confusion, and the awkward moments where the system feels wrong but you can’t articulate why. Those are the highest-signal reports.
- **Public issues.** [github.com/phuryn/pm-brain/issues](https://github.com/phuryn/pm-brain/issues). Install bugs, feature requests, scenarios you want the eval suite to cover. Anyone can open one without a Substack subscription.

If you’re in a real product role and the system might fit your workflow, your install feedback in week one is what makes the next version better.

---

## 12\. Closing

Most product organizations repeatedly lose the same things: failed bets, abandoned assumptions, historical reasoning, unresolved tensions. The PM job is partly to remember these. The PM job is impossible when your context lives in five different places and none of them talk to each other.

One repo. One operating manual. An agent that reads it.

The brain isn’t a notes app you fill in. It’s a folder of plain-text files that grow with the work, traceable back to the source on every line, swept clean every Friday, free for anyone to use, and inspectable by anyone you trust.

P.S. The repo is at [github.com/phuryn/pm-brain](https://github.com/phuryn/pm-brain).

---

## Thanks for Reading The Product Compass

It’s amazing to learn and grow together.

Have a great rest of the week, Paweł

---

## Resources

### The PM Brain OS

- **The repo.** [github.com/phuryn/pm-brain](https://github.com/phuryn/pm-brain). Skill, example brain, docs, tests, all MIT licensed.
- **The walkthrough.** [Lena’s first five days](https://github.com/phuryn/pm-brain/blob/main/docs/walkthrough.md), the long version of Section 2.
- **Why this matters.** [Five failure modes that kill most AI memory systems](https://github.com/phuryn/pm-brain/blob/main/docs/why-this-matters.md), and the five structural choices that answer them.
- **The architecture doc.** [Two design decisions and one operating loop](https://github.com/phuryn/pm-brain/blob/main/docs/architecture.md).
- **Scaling.** [How the brain stays healthy as it grows](https://github.com/phuryn/pm-brain/blob/main/docs/scaling.md), growth shapes, compression mechanisms, realistic envelope numbers.
- **How it works.** [The technical version](https://github.com/phuryn/pm-brain/blob/main/docs/how-it-works.md), one ingestion, six files touched, end to end.
- **Prior art.** [What PM Brain borrows](https://github.com/phuryn/pm-brain/blob/main/docs/prior-art.md) from Zettelkasten / RAG / CLAUDE.md patterns, and what it rejects.
- **Glossary.** [Every term in plain English](https://github.com/phuryn/pm-brain/blob/main/docs/glossary.md).
- **Tests scoreboard.** [404 / 406 checks](https://github.com/phuryn/pm-brain/blob/main/tests/RESULTS.md), per-scenario snapshots, two residual failures called out honestly.
- **Issues.** [github.com/phuryn/pm-brain/issues](https://github.com/phuryn/pm-brain/issues). Install bugs, scenarios you want covered, feature requests. Open one.

### Composing with PM skills

![PM Brain, PM Skills](https://substackcdn.com/image/fetch/$s_!nNX6!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd041493-27e0-45ec-a4d2-5eade3cd1946_2170x725.png)

PM Brain, PM Skills

**PM Skills** (11K+ stars). [github.com/phuryn/pm-skills](https://github.com/phuryn/pm-skills). PM Brain is the memory layer; PM Skills is the workflow layer. They compose. A JTBD PM Skill extracts jobs from an interview using the proper framework; PM Brain makes sure that job updates the right user insight, hypothesis, stakeholder note, and decision record. The skill is how to do the work once. The brain is what we know across all the times we did it.

### Related newsletter posts

- *[Claude Code for PMs: The Beginner’s Guide](https://www.productcompass.pm/p/claude-code-beginners-guide)* (May 12). Everything to start.
- *[Claude Code Guide](https://www.productcompass.pm/p/claude-code-guide)* (Mar 8). Full version. The tool this runs on.
- *[Self-improving AI systems](https://www.productcompass.pm/p/self-improving-claude-system)* (Mar 16). The parent pattern for compounding agents.
- *[Intent Engineering Framework](https://www.productcompass.pm/p/intent-engineering-framework-for-ai-agents)* (Jan 13). The agent design language behind CLAUDE.md.
- *[What Is Product Discovery? The Ultimate Guide](https://www.productcompass.pm/p/what-exactly-is-product-discovery)* (updated 2025). Critical for PMs.