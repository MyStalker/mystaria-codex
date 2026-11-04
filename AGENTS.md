# Mystaria Codex — Repository Instructions

These instructions apply to the entire repository. Mystaria is an evolving fictional setting with a strict distinction between **approved canon** and **proposals**. Preserve the author's decisions; do not improvise missing rules.

## Start here, every task

1. Read `00_Mystaria_Canon_Index.md` first to find the owning canon references and document status.
2. Read `10_Canon_Changelog.md` for approvals, revisions, superseded rules, and unresolved matters.
3. Read the relevant subject-specific Markdown files **before** proposing or changing lore or mechanics.
4. For dialogue, stories and cultural expressions, read `12_Languages_and_Linguistic_Customs.md`; for illustrations, diagrams, sites and visual design, read `11_Visual_Style_Guide.md` and consult the approved visual reference artwork.
5. Check whether repository files are older than the most recent explicitly approved user decision. A file's presence or date alone does not make it authoritative.

## Canon precedence (highest first)

1. User's latest **explicit approval or correction**, when available in the task or verified source.
2. Latest **approved subject-specific canon reference**.
3. `10_Canon_Changelog.md` for revision status, supersession and open decisions.
4. Older master compendiums only where no newer approved material conflicts.

An assistant proposal, brainstorming transcript, worked example, or unapproved design is **not canon**. Where an approval is asserted but its details cannot be found, flag the missing source; do not guess.

## Canon editing rules

- **Only canonize explicitly approved changes.** Put speculative additions in clearly labeled `PROPOSAL` sections or separate draft files, not into operative canon.
- Preserve established names, race identities, spell and Craft ranks, **SP/MP costs**, level gates, prerequisites, affinities, handling limits, and Shimmer mechanics unless the user explicitly changes them.
- Do not invent numeric costs, formulas, rank effects, durations, prices, or lore merely to fill gaps. Mark missing details **UNRESOLVED**.
- Keep `SP`, attribute points, `MP`, `Gems`, and `Soul Strain` distinct.
- Respect existing exceptions (for example, Skillprints may count compatible Shimmer skills as purchased for zero SP, subject to their approved constraints).
- In ordinary in-world speech, refer to magical energy by **color** (red/blue/green/white/black); reserve `mana` for technical or mechanically precise language. Cultural speech patterns are tendencies, not mandatory accents.
- For visual work, Mystaria's identifying color is purple and the Shimmer is purple; preserve the approved **five mana symbols** and Living Storybook aesthetic. Never label new art or palette variations as approved without the user's explicit approval.
- Keep established canon intact outside the requested scope. Correct legacy contradictions only when supported by an approved ruling; otherwise report them.

## Files to update when canon changes

1. Update the **owning subject Markdown** with the full approved details; do not replace a detailed rule with a thin summary.
2. Update `10_Canon_Changelog.md` with what was approved, what it supersedes, affected files, and remaining unresolved questions.
3. Update `00_Mystaria_Canon_Index.md` if file navigation, scope, status, or precedence changes.
4. Update other cross-references only where genuinely affected, keeping terminology consistent.
5. Do not overwrite old content without preserving necessary valid details or marking supersession clearly.

## Working method

- For exploratory requests: propose options, identify balance implications, and explicitly label them **NOT YET CANON**.
- For requested approved updates: implement the exact scope; make a small, reviewable change on a branch / pull request when possible. **Do not merge without user approval.**
- For a rules question: cite or identify the owning file/section and distinguish firm canon from source gaps.
- For a larger reconciliation: compare subject files against the index and changelog; present conflicts with options instead of silently adjudicating them.
- Never assume ChatGPT Project attachments, chat history, downloaded ZIP files, and GitHub are automatically synchronized. GitHub is the versioned repository; apply approved new decisions explicitly.

## Before marking a task complete

- Read the changed passages in context; check for contradictory duplicate rules.
- Verify all numbers, costs, prerequisites, names and cross-reference paths against approved sources.
- Clearly report files changed, any unresolved issues, and what still needs the user's approval.
- State whether edits exist **only on a branch**, in an open pull request, or **merged**. Never say repository files were updated when no successful write occurred.
