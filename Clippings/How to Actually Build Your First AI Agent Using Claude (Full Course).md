---
title: "How to Actually Build Your First AI Agent Using Claude (Full Course)"
source: "https://x.com/eng_khairallah1/status/2065721530546373016"
author:
  - "[[@eng_khairallah1]]"
published: 2026-06-13
created: 2026-06-19
description: "Everyone is talking about AI agents.Save this :)AI agents that research for you. AI agents that write for you. AI agents that manage your in..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HKprdcDWsAA9WMW?format=jpg&name=large)

Everyone is talking about AI agents.

Save this :)

AI agents that research for you. AI agents that write for you. AI agents that manage your inbox, update your spreadsheets, compile your reports, and execute entire workflows while you are asleep.

It sounds incredible. It also sounds impossible if you are not technical.

**It is not impossible. I am going to prove it.**

By the end of this article you will have built a working AI agent that runs a complete task from start to finish without you touching anything. No coding required. No API keys. No terminal commands. Just Claude, clear instructions, and about 30 minutes of your time.

**This is the simplest path to your first agent. If you follow every step, you will have one running today.**

## What Is an AI Agent (In Normal Words)

Forget every technical definition you have read.

An AI agent is Claude doing multiple steps automatically instead of you doing them one at a time.

When you use Claude normally, the workflow looks like this:

You ask Claude to research a topic. You read the result. You ask Claude to write an outline. You review it. You ask Claude to write the article. You edit it. You ask Claude to format it. You copy it out.

**That is four separate steps. Each one requires you to read, approve, and issue the next instruction manually.**

An agent does all four steps in sequence automatically. You say "research this topic, create an outline, write a full article, and format it for publishing." Claude executes all four steps, one after another, and presents the finished result.

**That is the entire difference.** A chatbot does one thing and waits. An agent does a sequence of things and delivers a finished output.

## The 3 Types of Agents You Can Build Without Code

You do not need the API. You do not need the Agent SDK. You do not need to write a single line of code.

You can build three types of agents using only Claude's existing tools:

**Type 1: Chat Agent (Claude Projects)**

A Claude Project with a system prompt that defines a multi-step workflow. When you give it a task, it executes the full workflow automatically because the system prompt tells it exactly what sequence to follow.

**Type 2: File Agent (Claude Cowork)**

A Cowork task that processes files on your computer. It reads a folder, processes each file, creates outputs, and organizes everything. All from a single instruction.

**Type 3: Scheduled Agent (Cowork + /schedule)**

A Cowork task that runs automatically on a schedule. Your agent wakes up at 7am, checks your email, summarizes the important ones, and saves a briefing to your desktop. No input from you required.

**We are going to build all three. Starting with the simplest.**

## Build 1: The Research-to-Article Agent (15 Minutes)

This is a Chat Agent that takes a topic and produces a finished article. One input, one output.

**Step 1: Create a new Claude Project**

Open Claude. Click Projects. Click "Create Project." Name it "Article Agent."

**Step 2: Write the system prompt**

Paste this into the project's system prompt:

You are an autonomous article production agent. When the user gives you a topic, you execute the following workflow automatically without stopping for approval between steps: STEP 1 - RESEARCH Search the web for the latest information on this topic. Find 5-7 relevant sources. Extract the key insights, statistics, and expert perspectives. STEP 2 - ANGLE Based on your research, identify the most interesting angle. What does the reader already believe about this topic? How can we challenge or expand that belief? Choose the angle that would generate the most engagement. STEP 3 - OUTLINE Create a detailed article outline: - Opening hook (contrast between common belief and reality) - 5-7 main sections with bold subheadings - Specific data points or examples for each section - Closing CTA STEP 4 - WRITE Write the complete article. 2000-3000 words. Short paragraphs (3 sentences max). Bold the key insight in every section. Specific numbers over vague claims. Direct, conversational tone. Zero filler. STEP 5 - REVIEW Review the article against these quality criteria: - Does every section add new information? - Are all claims supported by specific numbers or examples? - Would a busy person stop reading at any point? If yes, fix those sections. - Is the opening hook genuinely compelling? Output the final article. Include a recommended title at the top. Execute all 5 steps in one response. Do not ask for approval between steps.

**Step 3: Test it**

Open a new conversation in your Article Agent project. Type one sentence:

"AI agents for beginners"

Claude executes all five steps. Research. Angle selection. Outline. Full draft. Quality review. You get a complete, polished article from a three-word input.

**That is your first agent.** It took 15 minutes to build and it replaces 2-3 hours of manual work every time you use it.

## Build 2: The File Processing Agent (15 Minutes)

This is a Cowork Agent that processes a folder of files automatically.

**Step 1: Open Claude Desktop and go to the Cowork tab**

Grant Cowork access to the folder you want to process.

**Step 2: Give it a batch processing instruction**

Go to my /Downloads folder. For every PDF file in there: 1. Read the document 2. Extract a summary (5 bullet points max) 3. Identify the 3 most important action items 4. Save a summary file in /Summaries with the same filename but .md extension After processing all files, create a master summary file called "all-summaries.md" that combines everything in one document, sorted by date. Process all files. Do not stop between files.

Claude processes every PDF in the folder. Reads each one. Extracts summaries. Creates individual files. Then creates a master document.

**One instruction. Entire folder processed.** If you have 20 PDFs, this saves you 2-3 hours of manual reading and note-taking.

## Build 3: The Scheduled Morning Agent (15 Minutes)

This is a Scheduled Agent that runs automatically every morning.

**Step 1: Open Cowork**

**Step 2: Type /schedule**

**Step 3: Configure the recurring task**

Every weekday at 7:00am: 1. Check my Gmail for any emails received since 5pm yesterday 2. Categorize each email: - ACTION REQUIRED (needs my response or decision) - FYI ONLY (informational, no response needed) - CAN IGNORE (newsletters, promotions, automated notifications) 3. For each ACTION REQUIRED email, draft a suggested response 4. Check my Google Calendar for today's meetings 5. For each meeting, note who is attending and the topic 6. Save everything to a file called "morning-brief-\[today's date\].md" in my /Daily folder Format: ## Urgent Emails \[list with drafted responses\] ## Today's Calendar \[meetings with attendee info\] ## FYI Items \[brief list\]

Set the schedule. Every weekday at 7am.

**From now on, you wake up to a complete daily briefing.** Emails sorted. Responses drafted. Calendar summarized. No effort required from you. The agent runs while you sleep.

## How to Make Your Agents Better Over Time

Your first version of any agent will be decent. Not perfect. Here is how to improve them:

**The Correction Rule:** Every time an agent output needs correction, update the system prompt or task description. "The summaries are too long" becomes a new rule: "Each summary must be under 100 words." After ten corrections, your agent is dramatically more precise.

**The Example Rule:** Upload examples of excellent output into your Project knowledge files. "Here are three articles that represent perfect output quality. Match this standard." Agents with examples outperform agents with only instructions.

**The Feedback Loop:** Once a week, review your agent's outputs from the past 7 days. What worked well? What needed fixing? Update the instructions accordingly. Agents that get weekly refinement produce 3-5x better output after a month than agents that never get updated.

## 5 Agent Ideas You Can Build Today

Now that you know the three types, here are five agents you can build immediately:

**1\. The Content Repurposer**

Input: One long-form article. Output: An X/Twitter thread, a LinkedIn post, an Instagram caption, a newsletter teaser, and a YouTube script outline. All in one response.

**2\. The Weekly Competitor Tracker**

Scheduled weekly. Searches the web for your top 3 competitors. Finds any new product launches, pricing changes, content published, or news coverage. Saves a competitive intelligence brief.

**3\. The Client Onboarding Agent**

Input: Client name and project description. Output: Welcome email, project timeline, intake questionnaire, and brand asset request. All customized with the client's details. Ready to send.

**4\. The Meeting Debrief Agent**

Input: Your raw meeting notes (even messy ones). Output: Clean summary with decisions made, action items with owners, open questions, and next steps. Formatted and ready to share with attendees.

**5\. The Invoice Processor**

Cowork agent that scans your /Receipts folder monthly. Extracts date, vendor, amount, and category from each receipt. Creates a categorized spreadsheet. Calculates totals. Saves to /Finance.

## The Big Picture

Here is what most people do not realize.

You did not just build three agents. You built the skill of building agents. That skill compounds. Every agent you build teaches you patterns you can reuse. Your system prompts get sharper. Your workflows get tighter. Your output quality gets higher.

Within a month of building agents, you will look at every repetitive task in your life and think: "I can agent that."

And you will be right. Because once you understand the pattern (define the steps, set the quality standards, automate the sequence), you can agent anything.

Most people will keep doing their work manually while talking about how cool AI agents sound.

The ones who build their first agent today will have a team of them running by the end of the month. And they will never go back to doing this work themselves.

**If you found this useful, follow me** [@eng\_khairallah1](https://x.com/@eng_khairallah1) **for more AI content like this. I post breakdowns, courses, and tools every week.**

**hope this was useful for you, Khairallah** **❤️**