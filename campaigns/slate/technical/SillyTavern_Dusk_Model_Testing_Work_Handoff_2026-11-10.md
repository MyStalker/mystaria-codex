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
