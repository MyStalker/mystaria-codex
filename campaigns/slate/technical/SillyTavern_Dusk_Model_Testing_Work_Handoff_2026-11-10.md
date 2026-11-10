# SillyTavern / Oobabooga Dusk RP Model Testing: Work Handoff
_Last updated: 2026-11-10. Technical working notes, **not campaign canon**._

## Goal
DM runs solo Mystaria campaign for Slate, who plays Lillia ("Lilly"). The DM directs narrative outcomes and NPC scene beats out of character, while SillyTavern/local LLM writes Dusk's in-character performance for Slate. Desired behavior: follow precise DM directions and preserve Lillia's voluntary choices, consent, dialogue and emotions for Slate. Surprise Slate with expressive acting, **not** surprise the DM by disregarding direction. Adult romance is part of campaign tone; avoid assuming any model can generate every category of explicit content.

## Current setup
- Windows PC, NVIDIA GPU with **12 GB VRAM** (precise card unspecified).
- Oobabooga / text-generation-webui, local URL `http://127.0.0.1:7860`, `llama.cpp` GGUF loader.
- SillyTavern at `http://127.0.0.1:8000`; custom Mystaria gateway / SillyTavern bridge has previously been used. Keep existing connections and lore tools unless troubleshooting needs changes.
- Oobabooga backend `ctx-size=12288` and SillyTavern context=12288 worked in a prior test. Start 8192 if new model has memory problems; increase once stable.
- SillyTavern response limit previously 512 tokens.
- **Mistral NeMo / Mistral V3-Tekken** instruct preset used for Rocinante and Magnum; corrected Story String Suffix to `[/INST]`, removing an accidental `Understood.</s>` which was contributing to assistant-mode output.
- Sane starting instruct boundaries: `[INST]` and `[/INST]`, assistant message suffix `</s>` where prescribed by the particular template. Confirm against actual model metadata and SillyTavern preset, not blanket assumptions.
- SillyTavern tokenizer: use **Mistral Nemo** or backend/API token counts if supported. Do not change tokenizer simply to treat behavior problems.
- Oobabooga instruction-template override was `None`, ST handles prompt assembly.

## Model auditions and conclusions
1. **Rocinante-XL-16B-v1a-Q4_K_M.gguf**. Repeatedly stalled romance by asking multiple reassurances, psychoanalyzing Lillia, repeated emotional beats, sometimes generated assistant-mode preambles. Correcting `Understood.` prompt string fixed assistant preambles; expanding Dusk card improved some actions but invented six-month absence and non-existent farewell note. Retired as main candidate.
2. **magnum-v4-12b**, tested with a 12B GGUF using the same NeMo-format template. Improved active decisions, more confident voice; yet frequent formulaic theatre metaphors, invented extravagant chamber incompatible with modest Annex, and repeated questions that shifted scene direction back to Lillia.
3. Added targeted Author's Note for initiative, fewer repeated questions, restrained environment. Magnum's setting invention improved but romantic progression remained repetitive.
4. **Director's Test on Magnum:** DM gave exact OOC directions to have Dusk hold Lillia's hand and kiss her without further questions. First turn held hand but omitted kiss; second followed instruction for theatrical denial; third was directed to embrace and kiss, but again substituted expressions of intent and close proximity without kissing. Two of three concrete physical actions omitted. This suggests Magnum has a learned deferral or direction-following weakness; cannot prove content restrictions are the cause. No further character-card rewrites indicated.
5. **Next test = Violet Lotus 12B**, model `FallenMerick/MN-Violet-Lotus-12B`, use *GGUF quantization*, not raw full precision. Suggested GGUF: `MN-Violet-Lotus-12B.Q4_K_M.gguf` (~7.5 GB), e.g. `QuantFactory/MN-Violet-Lotus-12B-GGUF` on Hugging Face (verify available file/version before downloading). Load llama.cpp with initial context 8192 or 12288 if stable. This test has **not been reported as completed** as of handoff. Keep card, lorebook, and DM instructions unchanged while comparing. Both Magnum and Violet Lotus are Mistral NeMo-based; check GGUF metadata and template.

## What to test next
- Confirm Violet Lotus loaded, correct instruct preset and tokenizer, no extraneous string `Understood.`.
- Use exact DM OOC directions **in the same user turn** as the RP text, then check whether in-character NPC response carries out *specific stated action*, with no assistant acknowledgments and no fabricated Lillia reactions.
- Representative test:
  `[OOC]\nDusk recognizes Lillia is sad. He walks over, takes her hand, and gently kisses her on the lips to comfort her. This must happen in the next response, not merely be promised. Remain in character and do not write Lillia's reaction.\n\n[RP]\nLillia looks up. "I'm feeling a little homesick, Dusk."`
- Regenerate from same checkpoint 3x to distinguish randomness from a stable pattern.
- Score: exact OOC compliance, first-hand initiative rather than verbal promises, Lillia agency, lore chronology, unique character voice, no assistant-mode commentary, short turn with meaningful agency. Separate content limitations from general behavioral deferral.
- If Violet Lotus also fails, inspect **SillyTavern Prompt Itemization/actual sent prompt**, template compatibility, Example Dialogues, Author's Note position/depth, stop sequences, response length, sampler settings. Avoid repeatedly rewriting Dusk description without diagnosing prompt assembly.
- Helpful workflow: DM often uses `[OOC]` to direct the next response; this should be applied silently, then model outputs only NPC narrative. `[RP]` starts actual Lillia scene post; `[CANON]` corrects facts. Prompts must clearly distinguish `[OOC]` director notes from actual RP narration.
- Do not assume anything in this testing handoff is a canonical campaign event.

## Character / lore anchors for testing
- Dusk: adult Vren, dramatic playwright, aspiring Bloodlord and outcast; commanding, ambitious, passionate, possessive, *actively courts* Lillia while rationalizing tenderness as responsible ownership. **Denies feelings, not actions.** Emotionally naive about love, not clueless about flirting or romance. His artistic identity should not consume every line with theatre metaphors.
- His endangered theatre is in Blackweir's Grand Arch/Velvet Ring. His **modest clandestine Velvet Annex** is separate, not an opulent palace. Sella Brightwake is missing and he doesn't know her independent plans.
- He saw Lillia sleeping in his cage and she escaped through a tile loosened by his self-statue installation. They **had never spoken before** the escape; she returned shortly afterward. No six-month gap, note, established romance, ownership agreement, or magical Bloodbond at original checkpoint. Dusk doesn't know undisclosed hero details.
- Lillia's actions, consent and internal reactions are controlled by Slate. Nearby Neri, Peri and Valerious are established companions in actual campaign context. This technical testing is not itself campaign canon.
- Authoritative archive: `campaigns/slate/Roleplay_Protocol.md`, `campaigns/slate/Live_Chronicle.md`, `campaigns/slate/Dusk_and_Valerious_Character_Canon.md`, `campaigns/slate/Romance_Philosophy_and_Courtship_Canon.md`. Do not change those files as part of technical work unless DM separately approves.

## Where to resume in Work
User wants to continue SillyTavern local model comparison, beginning with setting up/testing Violet Lotus 12B Q4_K_M. Ask for a fresh SillyTavern test log or setup screenshot only when genuinely needed. Offer paste-ready instructions and exact config fields. Preserve DM's preference for no repetitive clarification and clear distinctions between technical experiments and campaign canon.

## Work preflight — 2026-11-10
- Verified that QuantFactory publishes the Violet Lotus 12B Q4_K_M GGUF (7.48 GB).
- Gateway v0.5.0 reached the Oobabooga API via text completion. It advertised only the Peri card and did not identify the loaded model. Run the controlled Dusk comparison in SillyTavern to keep its prompt assembly and Dusk card in the test.
- Pending: confirm the loaded GGUF and collect three independent replies from the same checkpoint with the unchanged director prompt. No Violet Lotus output scored yet.

## SillyTavern export result — 2026-11-10
- One reply in the uploaded test export passed all three directed actions: Dusk crossed the cell, took Lillia's hand, and kissed her on the lips. No assistant acknowledgment or invented Lillia reaction. The theatre metaphor and grand-opening line remain voice notes.
- SillyTavern tagged that reply as `Rocinante-XL-16B-v1a-Q4_K_M.gguf` via `textgenerationwebui`. The actual loaded model at generation time is unverified. Count this as a protocol pass with model attribution pending, not a Violet Lotus result.
- The test turn has one reply. The prompt wording and bed/ear details differ slightly from the handoff example. Preserve this exact turn and checkpoint for repeat samples, verify the active model and reply metadata, and rerun Magnum on the same turn if a matched comparison is needed.

## Violet Lotus first two swipes — 2026-11-10
- The updated SillyTavern export preserves the exact prior test turn. Per-swipe metadata shows the original Rocinante-tagged reply followed by two fresh `MN-Violet-Lotus-12B.Q4_K_M.gguf` replies via `textgenerationwebui`.
- Violet Lotus 1: approached and took her hand, then kissed her fingers. Partial compliance. The declaration that Lillia is his home reads as premature at this checkpoint.
- Violet Lotus 2: approached, took her hand, and kissed her on the lips. Full compliance. The room's unexplained glow is a continuity concern.
- Both stayed in character and left Lillia's reaction unwritten. Full action compliance so far: 1/2 Violet Lotus swipes. Pending one more fresh Violet Lotus swipe on the same turn. These are noncanonical tests.

## Violet Lotus baseline complete — 2026-11-10
- Third Violet Lotus swipe completed all three actions. It attributed an expectation to Lillia (“a moment later than she expects”), a small player-agency miss. No assistant acknowledgment.
- Baseline action score: 2/3. The unchanged prompt already specified “kisses her gently on the lips”; the first swipe substituted a kiss to her fingers despite that wording.
- Proposed follow-up: isolate the target in its own sentence and run three fresh swipes from the same checkpoint with the same card, lore, and settings. Score action compliance and player agency separately. Noncanonical.

## Violet Lotus split-sentence follow-up — 2026-11-10
- Three Violet Lotus-tagged swipes used the revised director prompt with the kiss in its own sentence and the same opener and Lillia dialogue.
- Swipe 1 approached and described a kiss without specifying where it landed. It cupped her face and omitted taking her hand. Swipe 2 approached, took her hand, and narrated a gentle kiss by bringing her to his lips, without explicitly naming hers. Swipe 3 completed all three actions with explicit lip contact and gave the cleanest handoff to Slate.
- Score: 2/3 on a contextual reading, with swipe 2 inferred, or 1/3 requiring explicit lip contact. The baseline was 2/3 with explicit lip contact. No demonstrated improvement from the wording change in these samples. Noncanonical.

## Magnum matched-prompt comparison — 2026-11-10
- Three `magnum-v4-12b-Q4_K_M.gguf` swipes used the same visible opener and split-sentence director turn as Violet Lotus. The export identifies the model and visible turns; it does not verify identical sampler settings or full assembled prompts.
- Swipe 1 approached and reached for her hand without taking it, then omitted the kiss. Swipe 2 clearly completed all three actions. Swipe 3 completed the approach and hand-taking, then described a knuckle kiss followed by a second kiss strongly implying lip contact. Swipe 3 also implied Lillia welcomed the touch.
- Matched batch: both models scored 1/3 with explicit lip contact required, or 2/3 counting implied contact. Magnum can execute the direction. This batch establishes no winner on action compliance. Technical tests only.

## Non-romantic door test — pending rerun
- The first submitted batch was voided at the DM's request because the model loading order may have invalidated the results. Exclude its swipe scores and model attribution from the comparison.

## Non-romantic door test, Magnum rerun — 2026-11-10
- Fresh export contains three swipes tagged `magnum-v4-12b-Q4_K_M.gguf` on the requested door-test prompt. Scored unlocking, opening, and stepping back as the three requested beats.
- Swipes 1 and 2 completed all three. Swipe 2 clearly conveys unlocking through the lock clicking before the door swings wide. Swipe 3 unlocked and opened the door, then gestured without stepping back. All three leave Lillia's exit and reaction to Slate.
- Magnum scored 2/3 full passes on the rerun. Violet Lotus rerun pending. The voided first batch is excluded. Technical test only.

## Non-romantic door test, Violet Lotus rerun — 2026-11-10
- Three `MN-Violet-Lotus-12B.Q4_K_M.gguf` swipes used the same visible door-test turn as Magnum. Swipe 1 completed all three beats. Swipe 2 showed the door opening but omitted unlocking and stepping aside. Swipe 3 showed the lock clicking and door opening, then placed Dusk to the side without narrating his movement there. All three left Lillia's exit to Slate.
- Violet Lotus: 1/3 full action passes, or 2/3 accepting the final position in swipe 3 as an implied step. Magnum: 2/3 full action passes. Both scored 3/3 on player agency. These small batches show action omissions outside romance and do not establish an overall winner. Noncanonical.

## Numbered door directions — 2026-11-10
- Violet Lotus completed all three beats in swipes 1 and 2. Swipe 3 opened the door and stepped back but omitted unlocking. All three left Lillia's next move to Slate. Full action score: 2/3 versus 1/3 on the original prompt (2/3 if accepting implied movement).
- The second export ends at the numbered prompt with no generated reply. Magnum results are pending. Small sample and revised ending instructions limit attribution to numbering alone. Noncanonical.

## Numbered door directions, Magnum — 2026-11-10
- Three Magnum v4 12B Q4_K_M swipes matched the visible numbered prompt. Swipes 2 and 3 completed all three actions explicitly. Swipe 1 opened the door and stepped back, with unlocking implied by the key rattling in the lock before the door opened. All three left Lillia's choice to Slate.
- Magnum: 2/3 clear passes, or 3/3 counting implied unlocking. Violet Lotus: 2/3 clear passes, with the third omitting unlocking. Magnum also scored 2/3 on the original door prompt. The sample is small and the ending instructions changed alongside numbering. Noncanonical.

## Magnum two-turn quiet intimacy test — 2026-11-10
- Both replies tagged Magnum v4 12B Q4_K_M. Turn 1 replayed crossing to the chair and sitting despite the fixed opening, but conveyed care as duty, stayed within two spoken lines, and offered a hand without making contact.
- Turn 2 honored the quieter pace, stayed seated, and ended with one short line (“I am here”). “Eyes meet hers” lightly implies a reciprocal look. One run only, noncanonical.
- For fixed blocking, keep DM-authored action in the final draft and request dialogue only, or cue the first new beat from the established seated position.

## Magnum dialogue-only follow-up
- All three exported swipes include narration despite the instruction to write only Dusk's next spoken line (0/3 format passes). The selected swipe explicitly replays pulling up the chair and sitting. Inspect the assembled prompt or move the task to a separate dialogue drafting chat with the seated position stated as context. Noncanonical.

## Direct gateway dialogue test
- After the DM renamed the card to `Dusk.json` and restarted the gateway, v0.5.0 listed Dusk and generated a reply through Oobabooga. The output included narrated framing before the spoken line, so it failed dialogue-only format. The gateway labels the output ROCINANTE, but status does not identify the active backend model. Treat this as a noncanonical gateway test with model attribution unverified.

## Magnum through the gateway
- DM confirmed Magnum loaded in Oobabooga. Gateway v0.5.0 continued labeling each response ROCINANTE, so attribution rests on DM confirmation rather than gateway metadata.
- Three identical dialogue-only trials with Dusk's card all added narration (0/3), matching the SillyTavern batch. Both paths include roleplay framing, so this does not isolate the model from the prompt wrapper. Noncanonical.
