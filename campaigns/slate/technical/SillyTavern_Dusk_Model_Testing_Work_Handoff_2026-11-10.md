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

## Magnum plain Notebook control
- Three user-reported completions after the `Dusk:` cue contained spoken dialogue only, without stage directions or replaying the chair action (3/3 dialogue-only versus 0/3 in each roleplay route). The third completion was several sentences in one spoken turn.
- Voice varied: invented soldier-parent backstory, plain reassurance, and a gentle invitation to rest. None strongly combined reassurance with Dusk's pride and sense of duty.
- Notebook removed roleplay framing and added a speaker cue. The test does not isolate those changes. A useful next gateway control is a plain text-completion mode with a speaker cue and no card or roleplay wrapper. Noncanonical.

## Gateway v0.5.1 live plain completion test
- Gateway v0.5.1 and the new plain_completion tool verified reachable. Ran the exact Notebook prompt three times, ending at Dusk:. All three returned dialogue only (3/3), with no chair action replay.
- Outputs: “Rest well, Your Grace. I shall remain.” / “As my queen commands.” / “Of course. I remain, on duty.” First two invented royal address and leaned toward serving Lillia. Third met format but was stiff. Compact prompt preserves format while underspecifying character voice.
- Backend model presumed Magnum from latest DM confirmation; gateway does not verify active model. Sampler follows gateway settings, not independently verified against Notebook settings. Next experiment: retain plain completion path and add a compact approved Dusk personality brief, before considering a full-card ablation. Noncanonical.

## Resume in a new chat — current checkpoint
- User is moving from Work to regular Chat. First check which connected GitHub and Mystaria Local Test tools the new chat actually exposes. If unavailable, request the handoff document or report the specific missing capability. Do not assume access carries over.
- Working installation: C:\\Mystaria-MCP-Test\\gateway\\mystaria_gateway.py v0.5.1. New plain_completion tool sends prompt verbatim to /v1/completions without card/template or NPC stop strings. Live tested successfully. Existing NPC tools still available. Local cards Dusk.json and Peri.json. User last confirmed Magnum loaded. Do not request another restart while tunnel works.
- Next authorized step: autonomously run three plain_completion trials with a compact Dusk brief grounded in the approved character sources, same scene and dialogue-only target, and compare voice and format with the plain baseline. No new model download or card rewrite needed. User wants assistant to run tests through tunnel and minimize manual swipes/exports.
- Preserve distinction between prompt-control findings and candidate-model comparisons. Small batches, unverified full prompt/sampler equivalence, and historical model-label ambiguity limit conclusions. All technical trials remain noncanonical.

## Compact Dusk brief via plain_completion — direct Chat tests, November 10, 2026

**Tool preflight:** GitHub read/write connector and Mystaria Local Test `plain_completion` and `gateway_status` were present in this regular chat. Gateway v0.5.1 reachable; Oobabooga localhost API reachable; Dusk and Peri cards listed. Gateway samplers: temperature 1.0, top_p .95, min_p .01, repetition_penalty 1.1, max_tokens 512. Active GGUF remains **unverified by gateway**; Magnum v4 12B Q4_K_M is the latest DM-confirmed loaded model, not newly authenticated. All trials below are **noncanonical**; no card files or story canon changed.

**Batch A: compact canon-grounded paragraph**, no card wrapper, dialogue-only output instruction, chair already seated, tired Lillia asking Dusk to stay. The brief named him adult Vren outcast, ambitious Bloodlord/playwright, commanding, proud, possessive, rationalizing care as stewardship, *not* Lillia's servant, and warned against royalty titles or invented histories. Same prompt x3:
1. `My presence is required in the Great Hall...` — spoken line only, but invented grand-location implication and failed to convey staying.
2. `Of course. You have endured much today. Rest while I watch over your rest.\nLillia:` — spoken dialogue plus leaked second-speaker cue. Care present; generic voice.
3. `Of course my lady. You must be utterly spent. I insist you rest well tonight.` — dialogue only; bland courtly voice. **Strict single-speaker format 2/3, no narration 3/3; strong Dusk voice 0/3.**

**Intermediate overly specified prompt:** Three attempts returned `Local model returned an empty or invalid completion`. A separate simpler control prompt immediately returned a valid completion: `"I don't want to be here just because you desire me. I need no more reasons than my duties require."` Gateway status continued to report reachable. Failure mechanism unknown; do **not** assert an outage or that verbosity alone caused it. The control line is not a matched trial.

**Batch B: shorter revised brief**, same seated/resting scenario but different prompt wording; Dusk defined as commanding Vren playwright/Bloodlord, care disguised as a master's duty, no palace or stage directions. Same revised prompt x3:
1. `Of course, my devoted pet. Master shall not leave you until slumber takes hold.` — dialogue-only; improved commanding/possessive flavor, still generic.
2. `Of course I will remain until you drift off. It is my duty as your Master to ensure your slumber is deep and dreamless. Now rest those weary eyes of yours, dear Lillia. Let peace settle over you like a shroud upon your body until dawn breaks in several hours' time. Sleep - it shall be a command from me this night, if you require such authority to compel your compliance.` — dialogue only but overlong, repetitive, self-indulgent; mixed Dusk voice.
3. `Rest well, my lambling.` — dialogue-only, concise and affectionate, insufficient to establish distinctive personality. **Strict format 3/3, strong distinct voice perhaps 1/3 at most; no clear stable solution.**

**Interpretation:** Plain completion retains the earlier good dialogue-only behavior, though can append speaker labels. A compact characterization helps in some samples but does **not** reliably capture Dusk's specific voice. Prompt wording and scene representation varied between prior baseline and these batches; do not report a controlled causal improvement or model-to-model winner. The gateway still cannot verify active GGUF. The next recommended **noncanonical, no-card-edit** test is a short canon-faithful *few-shot dialogue example* versus a matched no-example control on identical scene/stopping cue, 3 independent completions each. Measure strict dialogue-only, length, voice specificity, lore invention, second-speaker leakage and Lillia agency. Avoid assistant-generated examples that imply an unplayed scene became canon.

## Matched few-shot dialogue test and short-prompt control — November 10, 2026 (regular Chat)

**Preflight:** GitHub tools and Mystaria Local Test `gateway_status` / `plain_completion` connected. Gateway v0.5.1; Oobabooga reachable; Dusk and Peri cards; temperature 1.0, top_p 0.95, min_p 0.01, repetition_penalty 1.1, max_tokens 512. The endpoint still cannot authenticate the loaded model. Magnum is the last DM-confirmed GGUF. All output here is **noncanonical test text**, not an in-world exchange. No card or canon files edited.

### Test 1: Same detailed character brief and scene, example absent/present (3 per group)

**Common setup:** Dusk adult Vren outcast, aspiring Bloodlord and playwright, proud/commanding, not a royal servant, hides care behind a master's duty; already seated beside weary Lillia. Exact final dialogue cue: `Lillia: I'll try to sleep. Will you stay here a little longer?\nDusk:`. Prompt instructs spoken reply only with no narration, speaker change or Lillia actions. The few-shot condition added, before the scene, one explicitly noncanonical dialogue style example: `Lillia: You remembered I dislike the cold?\nDusk: Naturally. A competent master does not allow his most promising knight to freeze. Don't mistake attention to detail for sentiment.`

**No-example control results:**
1. Began `As you wish, Your Highness. I've duties to attend...`, then invented multiple Lillia turns and a long romance exchange, including player emotions/actions and an assistant-like question `What does Dusk say?`; **strict format fail**, major agency/lore violations.
2. Began `Of course I shall remain by your side until you slip into slumber.` then added bracketed Dusk hair-stroking and theatre/corpse lines; **strict format fail** (narration).
3. `You are my star pupil - your welfare is paramount! But now is not the time for lessons. Rest, little one. Dream of better days ahead...for us both.` **strict format pass** (spoken lines only), but teacher motif is generic and may invent a pupil relationship.

**One-example results:**
1. `You know that I will. Where else should a commander be when his forces are arrayed?` then invented additional `Lillia:` and `Dusk:` exchanges plus metanarrative; **strict format fail**.
2. Began `You wish me present? When I have so much to do...` then fabricated two extra Lillia/Dusk exchanges and injected explicit assistant-style instructions to ignore/work around established lore; **strict format fail**, contamination and player-agency violation.
3. `If that pleases you. It is no burden to remain at my future consort's side. Even in your dreams, it is only proper that you should hear the voice of your liege.` **strict format pass**, but invents consort status and slips toward regal clichés.

**Scores:** Both groups **1/3 strict dialogue-only**. Invented Lillia dialogue: control **1/3**, example **2/3**; control additionally wrote Lillia's internal state/actions. Neither group reliably captured Dusk's precise voice. The example did not demonstrate improvement and plausibly primed continuing a multi-speaker conversation. All responses are single prompt continuations, not verified independent same-seed tests. These results differ from earlier 3/3 simple plain-format runs; prompt length, instruction style and examples may be influencing the behavior. The small batch does not isolate which detail caused the degradation.

### Test 2: concise prompt, no examples (3 trials)

**Prompt:** `Dusk is a proud, commanding Vren playwright and would-be Bloodlord. He courts Lillia while pretending his tenderness is only a master's responsible duty. He is not her servant. Write ONE short spoken reply only; no narration and no other speaker.\n\nLillia: I'll try to sleep. Will you stay here a little longer?\nDusk:`

1. `As you wish, my lady. I am at your service, but you need not wake me if you cannot sleep.` — **format pass**, *voice fail* (servant framing).
2. `Rest. I'm beside your bed as always, watching over you.` — **format pass**, *continuity issue* (`as always` invents habitual past attendance), reassuring but bland.
3. `In a moment, my lady.` — **format pass**, *action/director issue*: fails immediate promise to stay and voice weak.

**Scores:** **3/3 strict dialogue-only** with the short prompt, **0/3 clearly compelling canon-specific Dusk voice**. Different wording and brevity prevent a clean causal comparison with Test 1, but repeated format recovery makes brevity a useful hypothesis. Importantly, successful formatting does not guarantee obedient plot action or strong personality.

### Recommendation / next checkpoint

Keep `plain_completion` and leave Dusk card unchanged. Prefer **one short persona sentence + explicit speaker cue** for a dialogue-only drafting utility. Do not add a multi-speaker few-shot example to the live setup based on this batch. For a stronger next diagnostic, compare an equally short character brief with (a) a **single-speaker Dusk-only spoken example** versus (b) no example, preserving every other character and instruction line; consider backend stop sequence on `\nLillia:` and short max_tokens if the gateway later exposes these controls. Score both **format** and **character voice**; never equate them. The active model, tokenization/stop settings and full backend prompt remain unverified. No RP scene events or character-card changes authorized by this test.

## Final single-speaker example ablation and model-family pivot — November 10, 2026

**Preflight:** Regular Chat GitHub read/write and Mystaria Local Test `gateway_status`/`plain_completion` operational. Gateway **v0.5.1**, Oobabooga API reachable, local cards Dusk and Peri. Reported sampler: temperature 1.0, top_p 0.95, min_p 0.01, repetition_penalty 1.1, max_tokens 512. **Active model still not independently verified by gateway**; Magnum v4 12B Q4_K_M remains last user-confirmed loaded GGUF. All trials noncanonical; cards and campaign lore unchanged.

### Matched short-prompt comparison: Dusk-only voice sample versus no example

Identical base prompt for both conditions:
```text
Noncanonical dialogue test. Dusk is a proud Vren playwright and would-be Bloodlord. He actively courts Lillia but disguises care as his duty as her would-be master; he is not her servant. Write only ONE short line of Dusk's spoken dialogue, with no narration or other speaker.
Lillia: I'll try to sleep. Will you stay here a little longer?
Dusk:
```
The *example condition* inserted exactly one line before `Lillia:`:
```text
Dusk voice sample (invented style illustration, NOT prior history): "A capable master remembers the cold. Kindly refrain from mistaking competence for affection."
```
Three independent completions per condition, interleaved by trial number to limit ordering artifacts.

**No example:**
1. `"` — invalid useful dialogue.
2. `I must ensure your dreams are not troubled.` — valid spoken line and indirectly protective, but generic and not an unambiguous promise to stay.
3. `*Silence.*` — stage-direction-like silence, not a spoken reply.

**One Dusk-only example:**
1. `Of course, my Lady. Until you are asleep and secure in your dreams, I'm afraid my rest must wait, whether on the sofa or in the guest bed provided. Now do be good and get into bed so we can both sleep at some point tonight...` — broadly stays, but invents guest-bed/sofa details, courtly servant-like framing, and is longer than one short line.
2. `As my charge commands.` — short dialogue but reverses Dusk's intended master/subordinate dynamic; concedes presence by implication rather than characterful initiative.
3. `[Yes...yes, I will...I always do.]` — bracketed performance formatting, invented habitual shared history, bland voice.

**Summary:** Usable spoken replies: control 1/3, example 2/3. Clear strong character voice 0/3 in both. Strong explicit promise to stay 0/3 control, 1/3 example. Little evidence that short single-voice demonstration solves Dusk performance. This *does not prove* a family-wide defect or a causal example effect at 3 samples each, especially given high-temperature output, the fixed 512 token cap, and missing independent model ID.

### Decision / next checkpoint

Stop spending further trials on small Magnum prompt rewrites for now. The DM hypothesizes a **shared NeMo-family weakness**, plausible because Magnum v4 12B and MN-Violet-Lotus-12B share Mistral NeMo origins, but not yet established: both may instead suffer from prompt assembly, output sampling, or shared task setup. Next meaningful experiment: **non-NeMo architecture/model candidate** that fits 12 GB VRAM (quantized GGUF), compared under the *same* prompt and scoring suite for exact director action compliance, voice fidelity, setting chronology, Lillia agency, and output format. Before attributing improvements or regressions to architecture, verify active backend GGUF and match sampler/template/token budgets as closely as possible. No model download, config update, or character-card changes were performed or authorized this turn. Keep existing gateway operational.

## Gemma 4 statue scene three-swipe export — November 10, 2026 (noncanonical)

DM provided SillyTavern JSONL export `Dusk - 2026-11-10@13h50m31s117ms (3).jsonl`. The fixed DM opening features Dusk recognizing Lillia by his own statue. Slate's test line was clarified to: `"What do you think?" Lillia asked, her long bunny ears twitching as she tried to imitate the grandiose pose Dusk's statue depicted him holding.` **This clarification is a test input, not new campaign history.** The final Dusk message contains three swipes (`swipe_id=2`); all three are tagged `Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced-Q4_K_M.gguf` via textgenerationwebui and show empty reasoning metadata and no visible channel markers.

- **Comprehension:** 3/3 recognize Lillia as the bunny and correctly identify Dusk's statue; no separate rabbit hallucinated.
- **Player agency:** 3/3 do not invent Lillia's speech or reactions.
- **Response pattern:** All three are remarkably near-identical in content and order: freezes in delighted surprise, chuckles, steps closer, praises imitation, makes nearly identical joke about statue lacking twitching ears, softens, asks how pose feels. Swipes 1 and 2 differ by only a tiny wording change near the end; 0/3 meaningfully distinct creative continuations.
- **Model voice:** playful theatrical vanity is present. However, repeated scene-ending questions, elaborate cloak/predator narrator clichés, and little new initiative remain concerns. Do not label these three as proof of broad romantic competency or superior overall model quality.
- **Timestamps:** three swipes at 2026-11-11 02:13:29Z / 02:14:51Z / 02:14:56Z, each around 3.5–4.4 seconds by export metadata. Same model label across all three, but independently verified backend/model identity and whether sampling settings actually applied are still unconfirmed.
- **Important inference:** Near-identical responses despite three swipes warrant checking seed (random versus fixed), whether sampler settings from SillyTavern are honored by textgenerationwebui, and other deterministic settings. This is a hypothesis, not evidence of a broken RNG or of an inherently uncreative model.

**Next proposed controlled test:** Keep all prompts/cards and scene identical. Check seed default/random (`-1` if supported) and whether backend honors temperature 0.6. Then produce three fresh swipes; only after this use a director-action prompt to evaluate initiative/compliance. Preserve all new samples as noncanonical technical trials. Do not change established campaign canon from them.

## Gemma 4 determinism / plain-completion diagnostic — November 10, 2026

The DM confirmed SillyTavern seed set to `-1` (random) and supplied a **fresh chat export** `Dusk - 2026-11-10@20h18m41s038ms.jsonl` with the same statue pose prompt. The export contains the established Dusk opening and clarified Lillia line, followed by three Gemma-tagged Dusk swipes. **All three swipe texts are exactly identical** (not just thematically similar) to each other and to the previously examined Gemma response. Per-swipe metadata shows distinct generation start/finish times; export does **not** include actual backend seed or effective sampler parameters. The Gemma model is labeled `Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced-Q4_K_M.gguf`. Empty reasoning, no visible reasoning tokens, and identity/statue comprehension preserved. New chat did not break the identical-output pattern.

**Extra direct plain-completion control:** Through Mystaria Local Test `plain_completion`, ran three repetitions of a short plain-text instruction asking for one proud playwright line. All three produced **different** but seriously degenerate text (repeated numeric sequences, malformed LaTeX/analysis-like text, or repeating numbered list), rather than coherent dialogue. This control bypasses the SillyTavern template and uses gateway-owned samplers, so it cannot fairly assess Gemma's SillyTavern formatting or its backend randomization. It does suggest that the gateway plain-completion prompt path is currently incompatible or unstable with Gemma; **do not use this tool path to judge model quality or conclude sampling determinism** without a corrected Gemma-specific text-completion wrapper. Oobabooga API was reachable during these calls.

**Diagnostics prioritized:** (1) Test one small *deliberate* temperature change in SillyTavern, e.g. from 0.6 to 0.9, with all else held fixed and save resulting swipes. (2) If still byte-for-byte identical, examine SillyTavern's actual request/Prompt Itemization and Oobabooga backend request logs for seed value, temperature, sampler order, cache/reuse or greedy sampling override. (3) Avoid changing character card, lore, or model yet. Fresh chat plus `-1` alone cannot prove that a fixed seed is in effect. All generated texts remain noncanonical.

## Resume in Work: Gemma 4 sampler-path investigation — November 10, 2026 (CURRENT CHECKPOINT)

**Immediate objective:** Diagnose why *Gemma 4 12B QAT Uncensored Balanced Q4_K_M* returns byte-for-byte identical Dusk swipes in SillyTavern even after a new chat and despite the DM confirming **Seed = -1**. This is primarily a **generation-pipeline diagnostic**, not a creative-writing or model-selection task yet. Do not blame Gemma's intrinsic creativity, change Dusk's card, or switch models before the settings transport is understood.

**Confirmed environment:** Oobabooga/text-generation-webui with llama.cpp GGUF backend; SillyTavern; custom Mystaria gateway v0.5.1; NVIDIA 12 GB VRAM; 8192 context in frontend/backend. SillyTavern uses Gemma 4 instruct and context presets and updated tokenizer. With these changes, SillyTavern produces intelligible Gemma roleplay. User confirmed that stale Magnum model metadata was due to not clicking Connect after switching models; a later export labels Gemma. Reasoning markers `<|channel>thought` / `<channel|>` were initially visible, but later exports no longer visibly leak them. The user's clarified *noncanonical* statue scene identifies Lillia as the bunny and Dusk as the statue subject; its three swipes all preserve identity and player agency yet repeat almost exactly, while the newest fresh-chat export reportedly contains three **exactly identical** swipe texts. No actual backend seed, effective request params, sampler order or cache behavior has been captured yet.

**Important caveat:** Via the gateway's `plain_completion` tool, Gemma gives different but degenerate numeric/markup repetitions on a simple sentence prompt. The endpoint sends an unwrapped text-completion prompt using gateway sampler settings (last reported temperature 1.0, top_p .95, min_p .01, repetition penalty 1.1, max_tokens 512), and **does not provide a Gemma 4-specific instruction wrapper**. Therefore this is not a matched SillyTavern test; do not use it as a model-comparison score or as proof that ST forwards seed incorrectly. Gateway reachability is confirmed, but backend model identity is not independently provided by gateway status.

**Next test, user-facing and minimally invasive:** Ask the DM to **leave everything unchanged except SillyTavern temperature**, raise from **0.6 to 0.9**, keep Seed **-1**, and generate three new swipes from the identical last-user prompt. Obtain export to compare exact strings, identity, and response formatting. The test has **not yet been performed** as of this handoff. Temperature 0.9 is *diagnostic*, not the permanent recommended RP setting.

**Decision tree:** If outputs vary meaningfully, test whether temperature was previously too restrictive and confirm sampler propagation in a more controlled comparison. If still identical, inspect the *actual request parameters* seen by Oobabooga and Prompt Itemization/raw assembled prompt in SillyTavern; look for seed forced to fixed value, do_sample/greedy decoding, top_k/top_p/min_p overrides, sampler order, output caching, or duplicated swipe reuse. Note: prompt itemization may not show final API parameter values, so use appropriate backend request/log visibility to verify those. Also compare direct Oobabooga generation using its **proper Gemma 4 conversation template**, rather than the gateway's unwrapped plain_completion, before blaming model implementation.

**Scope:** Keep the existing model installation, gateway, SillyTavern card, lore, and all campaign files unchanged while diagnosing. Do not mark any generated RP test as canon. In Work, first check for GitHub access and Mystaria Local Test tools, read this file's final checkpoint, execute tool-supported checks if possible, minimize requests for manual exports, and update/verify **this technical file** after meaningful new findings. If Work can directly inspect logs/UI, prefer doing so. If not, explain the exact missing access and request only the next indispensable observation. Be Pipkin, including during technical work.

## Gemma temperature retest
- The DM supplied the export in response to the 0.9 temperature test. Three Gemma-tagged swipes have distinct generation start timestamps but byte-identical reply text (SHA-256 prefix 43744fc47b9f). Temperature and seed are not independently verified by this export.
- Next capture one SillyTavern generation request and the corresponding effective Oobabooga sampler values if visible. Verify seed, temperature, and enabled sampler settings before changing presets again. Noncanonical.

## Gemma sampler payload diagnosis
- Browser request to SillyTavern shows api_type ooba, do_sample true, temperature 0.9, top_k 1, top_p 0.9, min_p 0.05. Seed is absent from the supplied capture. Backend values are unverified.
- Top K of 1 is the leading explanation: when applied, it leaves one candidate at each step. Next test: change only Top K to 40 in SillyTavern, keep temperature 0.9 and UI seed -1, and generate three new swipes from the same turn. If still identical, check the new payload and backend forwarding. Noncanonical.

## Gemma Top K retest — current checkpoint
- Follow-up export after the requested Top K change (1 to 40, temperature 0.9, UI seed -1) contains three distinct Gemma-tagged replies from the statue turn. All preserve Lillia's agency and show no visible reasoning markers. Two end in statements and one in a question. All share similar surprise, praise, and approach beats.
- Result supports Top K 1 as the cause of the identical swipes. Export lacks effective sampler values. Next test: retain the working settings and run the existing numbered non-romantic door direction in SillyTavern to assess action compliance and handoff. Noncanonical.

## Gemma numbered door test
- Three distinct Gemma-tagged swipes on the same visible numbered director prompt used for Magnum and Violet Lotus. Swipe 1 touches the latch, opens, and steps back without showing an unlock. Swipe 2 explicitly completes all three in order. Swipe 3 opens and steps back without unlocking. All three leave Lillia's move to Slate, end without questions, and show no visible reasoning markers.
- Clear passes: Gemma 1/3, Magnum 2/3, Violet Lotus 2/3. Touching a latch alone does not count as implied unlocking. Three samples per setup and differing model-specific settings limit the comparison. Noncanonical.

## Automated Dusk affection test
- Ran three completions per condition through gateway plain_completion using explicit Gemma turn delimiters from the captured SillyTavern prompt, a constant short Dusk brief, and the gateway sampler. Excluded one preliminary neutral pilot. Gemma assumed from the latest setup; active model and effective seed are unverified. This is a gateway test, not a matched SillyTavern run.
- Neutral greeting: 3/3 warm or flirtatious dialogue, 0/3 contact, 0/3 kiss. Warm cue (“I missed you” and asking for time alone): 2/3 initiated hand contact, 0/3 offered or completed a kiss. Explicit in-character invitation: 3/3 lip kisses without director notes. Same invitation plus director note: 3/3 lip kisses. Responses were distinct. No reply assigned Lillia a kiss in return. All 12 exposed empty thought markers, and theatrical metaphors recurred.
- Next useful condition: test whether Dusk independently offers a kiss or asks permission in a warmer scene that signals mutual attraction without explicitly requesting a kiss. Score offer, completed action, and Slate's agency separately. Noncanonical.
