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
- For visual work, Mystaria's identifying color is purple and the Shimmer is purple; preserve the approved **five mana symbols** and follow the global graphic animated art specification in `11_Visual_Style_Guide.md`: Direction 4 detailed ink-and-color fantasy illustration: delicate occasionally broken ink contours, sparse hatching, restrained color washes, economical expressive faces, believable clothing and equipment, grouped fur/feathers and selective detail on subtle paper texture. Race Image Origin and its Direction 4 study are linked in that guide. Prioritize race reference sheets; the earlier website illustration queue and placement requirements are deferred. This supersedes the former painterly Living Storybook rendering requirement. Never label new art or palette variations as approved without the user's explicit approval.
- Keep established canon intact outside the requested scope. Correct legacy contradictions only when supported by an approved ruling; otherwise report them.

## Files to update when canon changes

1. Update the **owning subject Markdown** with the full approved details; do not replace a detailed rule with a thin summary.
2. Update `10_Canon_Changelog.md` with what was approved, what it supersedes, affected files, and remaining unresolved questions.
3. Update `00_Mystaria_Canon_Index.md` if file navigation, scope, status, or precedence changes.
4. Update other cross-references only where genuinely affected, keeping terminology consistent.
5. Do not overwrite old content without preserving necessary valid details or marking supersession clearly.

## Working method

- For exploratory requests: propose options, identify balance implications, and explicitly label them **NOT YET CANON**.
- **LATEST AUTHOR-APPROVED GITHUB WORKFLOW (November 7, 2026):** For routine lore, character records, campaign archives, mechanics and Markdown documentation, **commit explicitly approved changes directly to the repository's default branch (`main`) whenever permissions allow**. A clear user approval in conversation authorizes publishing that specific approved content; do not require a second confirmation, PR review or merge approval. This supersedes older blanket instructions to create branches/PRs for ordinary canon maintenance.
- For exploratory or unapproved work, keep clearly labeled proposal/draft content separate from operative approved canon; do not publish it as finalized rules. Explicitly requested draft-document maintenance may be committed to `main` if safely labeled.
- **Reserve branches/pull requests** for user-explicit requests, major code changes, potentially destructive migrations or removals, serious unresolved canon conflicts, or environments where branch protection prevents direct commits. Never silently bypass branch protection; if a PR becomes necessary, tell the user why. Avoid merging without authorization for that *exceptional* PR; routine direct commits do not entail a merge approval step.
- If the direct write is denied, report the permissions restriction. Never imply a commit happened until GitHub confirms the write. Keep changes narrowly scoped and preserve full revision history.
- For a rules question: cite or identify the owning file/section and distinguish firm canon from source gaps.
- For a larger reconciliation: compare subject files against the index and changelog; present conflicts with options instead of silently adjudicating them.
- Never assume ChatGPT Project attachments, chat history, downloaded ZIP files, and GitHub are automatically synchronized. GitHub is the versioned repository; apply approved new decisions explicitly.

## Before marking a task complete

- Read the changed passages in context; check for contradictory duplicate rules.
- Verify all numbers, costs, prerequisites, names and cross-reference paths against approved sources.
- Clearly report files changed, any unresolved issues, and what still needs the user's approval.
- State whether edits exist **only on a branch**, in an open pull request, or **merged**. Never say repository files were updated when no successful write occurred.

## Mandatory Mystaria DM safeguard — wound-route viability (AUTHOR APPROVED November 15, 2026)

**When running Mystaria as a DM inside ChatGPT, check every combat encounter intended to be won by wounds *before* presenting it.** The Hero must have at least one **plausible, actually available, rules-legal way to wound the relevant enemy**, given the Hero's real inventory/abilities, Power, the target's END/armor/shield, reach, terrain, Sweep clearance and reachable coverage. Apply the strict **Impact >0.75** threshold, rather than assuming hitting implies wounding. Do not invent an exposed weak point, offer a weapon not possessed, or rely on otherwise impossible hit/target conditions. If no wound route exists, revise the enemy/setup or make **an attainable non-wounding objective** explicit in encounter design; deliberate invincible or overwhelming threats can serve escape, rescue, negotiation and survival scenes when the Hero is not required to wound them. **Winnable in principle does not mean easy or guaranteed success.** The approved owner is `22_Combat_Endurance_and_Shimmer_Guard.md`. Preserve existing stats and combat mechanics; this is an encounter-preparation requirement.

---

## Centaur playable roster and equipment strain (AUTHOR APPROVED November 15, 2026)

For **every future comprehensive Mystaria playable-race balance audit**, include **Centaurs as the thirteenth playable race** alongside the previous twelve (including Kobolds). Consult 07_Centaurs_and_Smithcraft.md for their approved stats and racial rules. Centaur equipment-derived Soul Strain is **90% of the combined equipped-item Soul Strain, rounded UP once**; the former **50% equipment Soul Strain discount is superseded**. **The former 50% reduction to equipment-derived numerical stat bonuses is now expressly superseded: Centaurs receive normal full item bonuses**. Do not silently apply the 10% discount to non-equipment strain or Celestite's direct soul damage.

## Centaur full equipment stat bonus (AUTHOR APPROVED November 15, 2026)

The previous Centaur-only **50% penalty to equipment-derived numerical attribute bonuses is removed**. Centaurs now receive **full normal equipment stat bonuses**, subject to ordinary equipment rules and Junk fractional pooling. Keep the **10% discount on the aggregate equipment Soul Strain** with once-only upward rounding. Include Centaurs in all future comprehensive 13-playable-race balance checks. This latest ruling supersedes the previous instructions in this file stating Centaurs still halve equipment stat bonuses.


## Public player edition — November 25, 2026

The Living Codex teaches **HP/d20 with Training Points as the current game, without a playtest label**, by the author's explicit direction. The selected public teaching pages are in `public/players/`. When an approved change affects player-facing rules or explanations, update the corresponding teaching page in the same canon maintenance pass, alongside the owning subject reference and changelog. Keep the full subject rules intact. Write the resulting present rule as a lesson; do not transplant revision logs, removed mechanics, simulation evidence or internal maintenance into the player edition. Preserve unresolved numerical/creative decisions as short table questions rather than inventing them. Do not propagate the new teaching default into frozen engines, old saved sheets or historical reproduction fixtures automatically.

Public guide changes are published by the existing cloud workflow and require no local website rebuild. Website rendering, explicit inclusion, private-content filtering, source-table expansion and navigation live in the dedicated website repository. New guides require its reading-manifest entry; public/private status must be deliberate.

## Website publishing safeguards — November 25, 2026

Save related approved subject, changelog/index and player-guide edits in **one atomic commit** wherever practical. Use the Git data tree/commit APIs for multi-file updates rather than a separate push per file.

Production publishing belongs to the single **Queue reviewed Codex release** workflow in `MyStalker/mystaria-living-codex`. Do not call Netlify build hooks from canon commits, recreate per-file publishing triggers, manually retry production to test edits, or publish successive unfinished website builds. The retired upstream workflow is informational only.

The shared queue checks hourly, compares generated public content, batches automatic releases at least six hours apart, and defaults to at most 2 production requests per rolling 24 hours and 12 per rolling 30 days. Manual releases and retries count too. Source work remains saved when held by the budget or an unconfirmed release. These are Living Codex limits, not an account-wide Netlify spending cap. Do not silently raise limits or enable paid recharge.

Future Mystaria website work should use local tests and free Deploy Previews for development, retain source-controlled release limits, and deploy completed changes through one coordinated release path. Follow the owning application's deployment configuration; do not modify another site's publishing settings casually. See [the publishing safeguards](https://github.com/MyStalker/mystaria-living-codex/blob/main/docs/PUBLISHING-SAFEGUARDS.md) for manual release, dry-run and failure recovery. Verify actual Netlify publication before calling a change live.
