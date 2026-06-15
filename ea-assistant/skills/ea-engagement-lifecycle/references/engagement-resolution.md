# Engagement Resolution Procedure

Check conversation context for the active engagement slug. If none is set, scan `EA-projects/*/engagement.json` (excluding `.archive/`) and display a numbered list of available engagements; ask the user to select one. Load `engagement.json` for the resolved engagement and extract `slug`, `name`, `currentPhase`, and any other fields the calling command needs.

If no engagements exist, offer to run `/ea-new` to create one.
