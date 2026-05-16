---
name: ea-git
description: Manage EA projects via git and GitHub — init, commit, push, sync, log, remote
argument-hint: "[init|status|commit|push|sync|log|remote] [args]"
allowed-tools: [Read, Write, Bash]
---

Manage version control for the `EA-projects/` workspace.

## Workspace Config

Git state is persisted in `EA-projects/.ea-workspace.json`:

```json
{
  "gitInitialized": true,
  "githubRepo": "owner/repo-name",
  "gitRemoteUrl": "https://github.com/owner/repo-name.git",
  "defaultBranch": "main",
  "createdAt": "YYYY-MM-DD"
}
```

All `git` commands run with `-C EA-projects/` (or the absolute path to `EA-projects/`) so they target the EA workspace repo, not any enclosing repo.

---

## Subcommand Dispatch

If no argument is provided, display a short help menu listing all subcommands with one-line descriptions, then stop.

Route the argument to the matching subcommand below.

---

## /ea-git init

Initialise `EA-projects/` as a git repository and optionally connect it to GitHub.

### Steps

1. **Locate EA-projects/**. Check for `EA-projects/` relative to the current working directory. If it does not exist, error:
   ```
   ❌ No EA-projects/ directory found.
   Run /ea-new to create your first engagement, then come back to /ea-git init.
   ```

2. **Check for existing git repo**. If `EA-projects/.git` exists, read `.ea-workspace.json` and display:
   ```
   ℹ️  EA-projects/ is already a git repository.
   Remote:      {gitRemoteUrl or "not set"}
   GitHub repo: {githubRepo or "not linked"}

   Run /ea-git status to see current state, or /ea-git remote set <url> to update the remote.
   ```
   Stop.

3. **Run `git init`**:
   ```bash
   git -C EA-projects/ init -b main
   ```

4. **Create `.gitignore`** at `EA-projects/.gitignore` from the template at `templates/seeds/ea-gitignore.md`. Strip the markdown fences — write only the raw gitignore content. If a `.gitignore` already exists, skip this step and inform the user.

5. **Initial commit**:
   ```bash
   git -C EA-projects/ add -A
   git -C EA-projects/ commit -m "chore: initialise EA projects workspace"
   ```

6. **Check for `gh` CLI**:
   ```bash
   which gh
   ```
   If not found:
   ```
   ℹ️  GitHub CLI (gh) is not installed — skipping GitHub repo creation.
   You can link a remote manually later with /ea-git remote set <url>.
   Install gh: https://cli.github.com/
   ```
   Proceed to step 9.

7. **Ask**:
   ```
   Create a private GitHub repository for EA-projects/? (y/n)
   ```
   If no, proceed to step 9.

8. **Create GitHub repo and push**:
   a. Run `gh auth status` to get the authenticated GitHub user (extract `Logged in to github.com as {user}`).
   b. Derive the default repo name from the working-directory name (the parent folder of `EA-projects/`). Slugify: lowercase, spaces → hyphens, strip specials.
   c. Show:
      ```
      GitHub repo name: {derived-name}
      Change it? (press Enter to accept, or type a new name)
      ```
   d. Confirm the repo will be created as **private** under the authenticated user's account.
   e. Create the remote repo and link it:
      ```bash
      gh repo create {user}/{repo-name} --private --description "EA projects workspace" --source EA-projects/ --remote origin
      ```
      If `--source` is unsupported by the installed `gh` version, fall back:
      ```bash
      gh repo create {user}/{repo-name} --private --description "EA projects workspace"
      git -C EA-projects/ remote add origin https://github.com/{user}/{repo-name}.git
      ```
   f. Push the initial commit:
      ```bash
      git -C EA-projects/ push -u origin main
      ```

9. **Write `EA-projects/.ea-workspace.json`** with the collected values.

10. **Confirm**:
    ```
    ✅ EA-projects/ initialised as a git repository.
    Remote: {url or "none — run /ea-git remote set <url> to add one"}

    Next: run /ea-git commit to checkpoint your current work,
    or /ea-git status to see what's tracked.
    ```

---

## /ea-git status

Show the current state of the EA-projects/ git repository.

### Steps

1. Check git is initialised (`EA-projects/.git` exists). If not, display:
   ```
   ❌ EA-projects/ is not a git repository. Run /ea-git init first.
   ```
   Stop.

2. Run the following and display results:
   ```bash
   git -C EA-projects/ status --short
   git -C EA-projects/ log --oneline -5
   git -C EA-projects/ status -sb | head -1
   ```

3. Format output:
   ```
   ## EA Projects — Git Status

   Branch: main  ·  ahead 0  ·  behind 0
   Remote: https://github.com/owner/repo-name

   ### Uncommitted changes (N files)

   M  acme-retail/engagement.json
   M  acme-retail/artifacts/phase-b/business-architecture.md
   A  acme-retail/artifacts/phase-a/architecture-vision.md

   ### Recent commits

   a1b2c3d  Update Phase B — Business Architecture
   e4f5g6h  Add Architecture Vision (Phase A)
   i7j8k9l  chore: initialise EA projects workspace
   ```

   If no uncommitted changes: `✅ Working tree clean — nothing to commit.`

   If no remote: `ℹ️  No remote configured. Run /ea-git remote set <url> to link GitHub.`

---

## /ea-git commit

Stage all changes in EA-projects/ and create a commit with a contextual message.

### Steps

1. Check git initialised. If not, error as above.

2. Check for changes:
   ```bash
   git -C EA-projects/ status --short
   ```
   If output is empty, display: `✅ Nothing to commit — working tree clean.` and stop.

3. Display changed files grouped by engagement slug (first path component):
   ```
   Changes to commit:

   acme-retail/ (3 files)
     M  artifacts/phase-b/business-architecture.md
     M  engagement.json
     A  artifacts/phase-a/architecture-vision.md

   finance-modernisation/ (1 file)
     M  engagement.json
   ```

4. **Generate a commit message** from the changed files:
   - Count unique engagement slugs touched.
   - Identify the most-edited engagement (most file changes).
   - Look at which artifact files changed to name them.
   - Produce a message like:
     - Single engagement, artifact changes: `"Update {Artifact Name} — {Engagement Name}"`
     - Multiple artifacts: `"Update Phase {X} artifacts — {Engagement Name}"`
     - Multiple engagements: `"Update {N} engagements — {artifact types}"`
     - Engagement.json only: `"Update engagement metadata — {Engagement Name}"`
   - If the user provided a message argument (`/ea-git commit "my message"`), skip generation and use it directly.

5. Display:
   ```
   Proposed commit message:
     "{generated message}"

   Accept? (y) / Edit (e) / Cancel (c)
   ```
   - **(y)** Proceed.
   - **(e)** Prompt: "Enter commit message:" — use whatever the user types.
   - **(c)** Cancel, no changes made.

6. Stage and commit:
   ```bash
   git -C EA-projects/ add -A
   git -C EA-projects/ commit -m "{message}"
   ```

7. Show commit hash and summary. Offer:
   ```
   Push to remote? (y/n)
   ```
   If yes, run `/ea-git push` flow.

---

## /ea-git push

Push committed changes to the GitHub remote.

### Steps

1. Check git initialised.

2. Check remote is configured:
   ```bash
   git -C EA-projects/ remote get-url origin
   ```
   If not set:
   ```
   ❌ No remote configured. Run /ea-git remote set <url> first,
   or /ea-git init to create and link a GitHub repo.
   ```
   Stop.

3. Check for unpushed commits:
   ```bash
   git -C EA-projects/ log @{u}..HEAD --oneline
   ```
   If empty: `✅ Already up-to-date with remote.` and stop.

4. Push:
   ```bash
   git -C EA-projects/ push
   ```
   On failure (e.g., rejected), display the git error and suggest:
   - Run `/ea-git sync` if the remote has changes you don't have locally.
   - Or `git -C EA-projects/ push --force-with-lease` if you are certain you want to overwrite (warn: destructive).

5. Confirm with pushed commit count.

---

## /ea-git sync

Pull remote changes then push local commits. Keeps local and remote in sync.

### Steps

1. Check git initialised and remote configured.

2. Pull with rebase to keep a clean history:
   ```bash
   git -C EA-projects/ pull --rebase
   ```
   On conflict, display the conflicting files and stop:
   ```
   ⚠️  Merge conflicts detected in:
     {file list}

   Resolve the conflicts manually, then run:
     git -C EA-projects/ rebase --continue
   and re-run /ea-git push.
   ```

3. If pull succeeded, push:
   ```bash
   git -C EA-projects/ push
   ```

4. Confirm: `✅ Synced with remote. {N commits pulled, M commits pushed}.`

---

## /ea-git log

Show the commit history for EA-projects/.

### Steps

1. Check git initialised.

2. Run:
   ```bash
   git -C EA-projects/ log --oneline --graph --decorate -20
   ```

3. Display the output with a header: `## EA Projects — Commit History (last 20)`.

---

## /ea-git remote

View or set the GitHub remote for EA-projects/.

### Subforms

**`/ea-git remote`** (no args) — show current remote:
```bash
git -C EA-projects/ remote -v
```

**`/ea-git remote set <url>`** — add or update the origin remote:
```bash
git -C EA-projects/ remote remove origin 2>/dev/null || true
git -C EA-projects/ remote add origin <url>
```
Update `gitRemoteUrl` in `.ea-workspace.json`. Confirm.

**`/ea-git remote remove`** — remove the origin remote:
```bash
git -C EA-projects/ remote remove origin
```
Set `gitRemoteUrl` and `githubRepo` to `""` in `.ea-workspace.json`. Confirm.

---

## Error Handling

- **`gh` auth errors**: If `gh` returns an auth error, display: "GitHub CLI is not authenticated. Run `gh auth login` first."
- **No commits yet**: Catch the "does not have any commits yet" error from git status and handle gracefully — show "No commits yet" rather than a git error.
- **Detached HEAD**: If `git status` shows detached HEAD, warn the user and suggest `git checkout main`.
