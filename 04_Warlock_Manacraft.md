## November 20, 2026 — AUTHOR DECISION: Unified Channel Limit, Warlock migration, interrupted rituals and compounded entropy (LATEST)

**Approved channel design:**
- Remove the historical **−10 effective-INT offset** from the future modular **Channel Limit** equation. The INT portion now matters **half as much as before**; a natural starting mathematical expression is **effective INT / 10** rather than the legacy adjusted **ceil(max(1, effective INT − 10) / 5)**. **Craft-specific automatic Mastery supplies the other half of the intended resulting Channel Limit**, earned through that Craft's learned magical disciplines rather than a separately purchased Mastery skill. The numeric rank-to-Mastery schedule, rounding, baseline reference caster and how a literal 50/50 split varies across differently invested characters are **not yet approved**; do not accidentally erase Mastery's independence by setting it equal to INT-derived points for all characters. Previous Channel Limit math remains legacy reference pending complete migration.
- The normal one-action maximum is **half the applicable full Channel Limit**, with a **minimum of 1 MP when casting an eligible mana-costing spell** even if ordinary floor rounding would yield zero; two-action spells can use their full applicable limit. **Cantrips may cost 0 MP** and still obey normal legality and **at most one offensive attack per turn**. Zero MP does not mean a second attack.
- **Warlocks are to be integrated into the universal Channel Limit framework.** Their legacy **END-based one-hand Handling Capacity cap** was designed before the wider spell system and is to be **replaced**, not retained as an independent competing ceiling in the modular migration. This does not silently eliminate their author-approved **zero natural MP**, requirement for actual external mana sources, handling timing, magical eligibility, or resource/access restrictions; exact revised Warlock holding/transfer/casting calculations and relationship to the old safe 30-second/absolute 60-second holding window are pending.
- In **cooperative rituals**, the **ritual leader alone determines applicable spell skill prerequisites, ability ranks and Channel Limit**. Other participants add real mana, subject to the established **50% entropy loss on each ally's contributions**; they do not independently increase the spell's Channel Limit merely by joining, and there is **no participant-count cap**. The precise per-time-step throughput of all added contributions and the status of lead-caster mana as distinct from ally-contributed mana still require numeric specification.

**Approved interruption rule:** A ritual **interrupted before completion fails entirely**. A partially completed working **cannot be immediately discharged**, reduced to a smaller spell, or salvaged as a half-strength attack. What specifically counts as an interruption, and whether invested MP is unrecoverably consumed rather than returned, remain **OPEN** unless independently settled.

**Approved compounded entropy:** A **cooperative one-week ritual applies both losses sequentially**. Each ally's contributed mana first suffers **50% cooperative entropy**, then the ritual's resulting total investment (including contributions otherwise eligible) suffers **another 50% week-long entropy**. Thus **100 MP supplied by an ally yields 25 MP of effective ritual investment** before other legitimate costs. The lead caster's own contribution does not automatically suffer the ally-only contribution penalty but does incur the week-long penalty. Permanent-spell Soul Strain remains **entirely on the ritual leader**.

**Open:** Exact Craft Mastery rank formula, racial effects, rounding, cantrip capacity handling if nominal CL is zero, specialization exceptions, one-/two-action allocation under formal ritual timelines, multiple casters' contribution throughput, Warlock revised handling, partial ritual MP recovery, and interruption adjudication. Preserve existing approved discipline prerequisites until formally migrated.

---

## November 20, 2026 — AUTHOR APPROVAL: Ritual entropy, unlimited cooperative casters, and leader Soul Strain (LATEST)

**Approved:**
- **One-week rituals** (eight hours of work each day) lose **50% of mana invested to entropy**. Only half of the mana spent contributes to the ritual; sustaining a week-long working across daily sessions still permits legitimate mana replenishment between sessions. This is a specific efficiency loss, an explicit exception to the earlier decision against a generic *beneficial* ritual-efficiency multiplier.
- **Cooperative ritual casting** allows **unlimited participating casters** to pool effort for one ritual. The ritual uses the **lead caster's learned skills/capabilities** rather than requiring each collaborator to possess the leader's ranks. Multiple-caster contributions lose **50% of mana they spend to entropy**; actual mana sourcing, contribution and legal casting still apply. For example, a village of Wakecrafters may convene each morning and spend an hour collectively summoning rain, provided the final effect is otherwise legal under the rules.
- For **permanent spells created by cooperative rituals**, **all Soul Strain falls on exactly one individual: the ritual leader**, not divided among participants. Existing rules about XP buy-off and permanent Soul Strain for stat-increasing permanent buffs still govern.
- This permits grand cooperative workings but does not create mana, eliminate the leader's skill prerequisites, negate permanent ritual costs or grant unlimited output without genuine participants and investment.

**OPEN for calibration:** How to combine the 50% weekly entropy and 50% cooperative entropy when both apply (stacking versus one shared loss); whether the lead caster's own contribution to cooperative ritual suffers the group loss; per-person Channel Limit and ritual channel capacity, group synchronization, eligibility of different Crafts/mana colors and media, accumulated investment across daily sessions, interruptions, minimum participant contributions, conversion rounding, exact ritual Power and spell-price accounting. Do not assert an automatic 75% combined loss or a free unlimited group Channel Limit until approved.

**Relevant preexisting Channel Limit status (not changed by this approval):** The historical universal numeric baseline is `ceil(max(1, effective INT - 10)/5)` MP, with one-action casting restricted to `floor(full CL/2)`, two-action casting up to full CL, a shared turn-scale capacity with prepared defenses and no borrowing from future turns, plus specific Craft exceptions. The **November 19 modular revision** proposes **halving the INT-derived component and adding automatically earned Craft-specific Mastery**, but the exact numerical Mastery/rounding/multicraft formula is **not yet finalized**. Do not silently replace the old formula with guessed arithmetic. Cooperative ritual throughput and specialist Warlock hand Handling Capacity still need reconciliation with this framework.

---

## November 20, 2026 — AUTHOR DECISION: Ritual mana availability and channel capacity; no efficiency multiplier (LATEST)

**Author-approved resource boundaries:** A ritual can accept mana **during** its channeling; its entire MP cost does **not** need to be paid in the first six-second turn. A caster with 100 maximum MP cannot automatically cast a 150 MP ritual merely by waiting; completing that expenditure requires a real additional mana source **during** the casting, e.g. a Warlock replenishing the caster or a possible future mana potion (potions are **hypothetical, not established canon**). Spell/ritual channel capacity and actual available mana are distinct constraints. This does not authorize free mana regeneration during shorter rituals. The already approved week-long (eight-hour daily sessions) ritual can benefit from recovery **between** work sessions.

**Author-selected channel-capacity direction:** a **two-turn ritual doubles** ordinary per-spell channeling capacity (×2 baseline). At **one minute**, capacity **increases another 50%** (interpreted as ×3 baseline, subject to author's correction). By roughly a full-day-scale working, a caster should **generally be able to invest their entire legitimately available mana reserve**; how to distribute intermediate thresholds, and exactly whether the 8-hour tier satisfies this criterion, remains to calibrate. The standing ritual timing tiers remain 2 turns / 1 minute / 10 minutes / 1 hour / 8 hours / 1 week (8 hours daily). No formula for 10 minutes, 1 hour, 8 hours, or week-long throughput was approved in this ruling.

**No independent ritual-efficiency multiplier:** lengthier ritual channeling **does not** inherently grant a generic discount on MP costs or extra spell Power. Long-duration and large-area spells already realize huge economies of scale by affecting many things through one lawful large working rather than repeated small effects (e.g. forest-scale Morph). Preserve ordinary Magnitude, Duration, eligible medium/material, Power, mana supply, Channel Limit, action and resistance requirements. The area/duration price ladders remain explicitly **provisional**.

**Open:** exact intermediate capacity ratios, whether maximum personal MP or accessible external mana is the eight-hour ceiling in unusual cases, payment timing/capacity under mid-ritual refills, resource lock-in and interruption losses, combined participant contributions, and how Warlock zero-internal-MP handling operates during rituals. No mana potion system or cost, or new resource-recovery mechanism, is approved.

---

## November 20, 2026 — AUTHOR DECISION: Six ritual casting durations and weekly mana recovery (LATEST)

**Approved ritual timing ladder:** Ritual casting is extended channeling of magic, including in combat, rather than necessarily a separate type of spell. Six successive ritual time benchmarks are:
1. **2 turns** — shortest ritual; allows combat channeling into a larger spell.
2. **1 minute**.
3. **10 minutes**.
4. **1 hour**.
5. **8 hours**.
6. **1 week, with 8 hours of work per day**.

**Special weekly mana economy:** The **one-week ritual alone** permits the caster's maximum mana reserve to matter less, because the caster may **recover mana between the daily work sessions** and invest it toward the same working over several days. Do **not** assume that the shorter rituals also grant mana recovery between their stages or an automatic enlarged personal reserve. Normal available-mana, Channel Limit, legal casting and interruption constraints continue to matter until ritual-specific numeric rules are approved.

**Warlock Dispel illustration:** A short combat ritual can channel Dispel without the self-inflicted wound required by its accelerated form. Prior approved Dispel mechanics were **four channeling actions without a wound, or two actions with one wound**. The author now cites the **two-turn ritual as a no-wound alternative**. Treat the newer intent (two-turn safe ritual) as controlling for the prospective modular ritual framework, while **the exact reconciliation of turns, actions, and Dispel's historical four-action cost remains OPEN**. Do not quietly claim the historical cost table was formally migrated, or make all multi-action techniques wound-free by default.

**Still open for calibration:** Which spell capabilities or MP investments each ritual tier enables; casting/Channel Limit throughput and mana payment timing; interruption, protection and concentration checks; multiple participants; preparation and components; partial completion and resource loss; whether mana spent during a multi-day ritual remains invested safely between sessions; recovery rates; precise requirements for permanent spells and associated Soul Strain; and the treatment of rituals that overlap ordinary duration multipliers. The ritual timing ladder itself is author-selected, but **no general mana discount, spell Power multiplier, or ritual success percentage has been approved**.

---

## November 20, 2026 — AUTHOR CLARIFICATION: Blue Morph reversion has finite force; mundane manufacturing (LATEST)

**Approved:** When a temporary Blue Morph ends, the remaining morphed material attempts to return to its original shape, but **the reversion does not exert infinite or irresistible force**. Ordinary physical constraints, including a sufficiently strong surrounding mold, can resist that return. Consequently, **temporary Blue Morph can be used for durable mundane manufacturing without purchasing permanent spell duration**: for example, reshape scrap metal into a sword and promptly enclose it in a sufficiently durable mold before the spell expires; as the magic ends, the mold prevents full restoration and the metal remains physically deformed into the manufactured form. The resulting object is **mundane material**, not a permanent magical transformation or an exemption from matter conservation.

**Preserve existing boundaries:** The material must be eligible to Morph and obey the spell's Power, magnitude/material-area adjustments, targeting and normal casting requirements. Fundamental destruction still prevents ordinary reversion. Reversion does not undo injuries, movements, or other external consequences. **OPEN:** precise reversion-force formula versus the resistance/strength of molds, whether the material springs back partially, material integrity/work-hardening, and any detailed manufacturing times, tooling and quality calculations. Do not infer effortless perfect metalworking or an infinite-force shattering effect.

---

## November 20, 2026 — AUTHOR DECISION: Universal spell duration, buff escalation, instantaneous effects, and Blue Morph (LATEST)

**Approved rules and terminology:**
- **Permanent spells** require substantial mana and impose **Soul Strain** that the user must buy off with XP over time. When the permanent spell **increases attributes/stats**, the Soul Strain remains **permanent**, analogous to artificially increased stats from equipped items. Specific mana pricing, Soul Strain amounts, XP buy-off conversion, eligibility and exceptions are **OPEN**; do not silently assign numbers.
- **Multiple buff spells on one target have escalating MP costs:** the first applicable buff costs its ordinary MP price, the **second costs ×2**, the **third ×4**, and successive additional buffs continue doubling (fourth ×8, etc.). This is a safeguard against long-duration and permanent buff stacking. Exact definition of a qualifying buff, simultaneous versus sequential casting, recalculation after a buff expires, overlapping effects, ritual discounts, and how the multiplier applies to activation versus upkeep are **OPEN**.
- **Instantaneous** is the spell-duration/effect classification for magic whose *magical effect itself is brief*, but whose ordinary consequences on the world persist without continued magic, as with a fireball. Instantaneous does **not** mean permanent ongoing enchantment, undo damage, or waive normal action/casting requirements.
- **Reversion of temporary Blue Morph:** when the spell ends, remaining successfully morphed material is actively **morphed back into its original shape** rather than resetting the whole world. Events caused during the morph remain real; other unsupported objects, occupants, injuries and changes do not reverse. **Fundamentally destroyed material**, for example wood burned into ash, cannot unmorph back into its original form. A tree sunk into the ground can revert unharmed while an unsupported treehouse may be damaged.
- **Blue Morph accepts flesh** as a material with the **same two-area-category penalty as metal**. Morphing flesh constitutes **Transformation**, obeys its ordinary Power/targeting/resistance/delivery restrictions, and does not bypass unfinished universal Transformation rules.
- Earlier author's approved Morph directions preserved: **Animation is distinct from Morph**; a normal **1 MP single-target Morph** can reshape a handheld-scale object at ordinary legal casting range; one selected material category per casting, with minor variations included; **wood standard area, stone −1 area category, metal/flesh −2**, with **one-target floor**; matter is conserved; hostile applications that become attacks obey ordinary spell Power, Speed, attack and defense limits. Material hardness versus success continues to use lawful Power, not an extra automatic MP fee.
- **Magnitude area/cost working proposal:** Rank 0 one target **1 MP**; I adjacent targets **2 MP**; II 20-foot burst **4 MP**; III 100-foot burst **10 MP**; IV 1,000-foot burst **30 MP**; V 2-mile burst **60 MP**. These MP numbers are **provisional calibration**, not final approved universal costs. A large-area spell may take many turns to channel, to be designed under Rituals. Burst radius/placement interpretation and interaction with older merged Magnitude benchmarks await formal reconciliation.

**Author accepts provisional non-attack duration ladder for continued testing (NOT final numerical canon):**

| Duration | Proposed MP multiplier |
|---|---:|
| 1 turn | ×1 |
| 3 rounds | ×2 |
| 1 minute | ×3 |
| 10 minutes | ×5 |
| 1 hour | ×10 |
| 1 day | ×20 |
| 1 week | ×40 |
| Permanent | Special high-cost ritual plus Soul Strain |

**Design examples (not additional fixed costs):** A legendary Warlock may temporarily deform a forest to expose an ambushing army, with reversion around a minute later, using a comparatively brisk ritual. Permanently turning a forest into a grand citadel should be possible in principle but require one of the most substantial rituals available, rather than a cheap quick casting. Duration, ritual time and resources, casting Channel Limit, environmental interactions, precise permanent-object shape and Soul Strain amounts remain to be designed. These directions do not authorize free construction or permanent material creation.

---

## November 19, 2026 — AUTHOR APPROVAL: Basic Manashifting shields, slow passage and barrier-breaking (LATEST)

**Status and precedence:** The author's latest explicit November 19 rulings supersede older suggestions of mandatory omnidirectional basic Warlock shields or a depleting shield-HP pool. These are approved qualitative foundations for the modular Manacraft migration; exact structure-damage procedures, arc, and outstanding spell Power formula remain open. Preserve the existing historical Warlock skill/rank/SP ledger until separately migrated.

- **Creature-anchored White shield:** A normal basic magical overshield is **directional, anchored to its target, and follows the target's torso orientation**. Knocking its bearer prone rotates its protected arc along with that torso, potentially leaving ordinary attackers an opening. It remains protective on **each eligible attack** during its duration, not a one-hit resource pool. Its normal defensive presence does **not** prevent allied attacks from leaving or entering, and allies' attacks are ignored by the shield.
- **Fast versus slow passage:** The shield is an obstacle to **fast, harmful strikes**: a rapidly swung sword meets resistance and can rebound. **Slow deliberate penetration** is physically possible: a careful foe may slowly reach a hand or sword through the field, but that slow poke does **not** become an injurious strike merely by touching flesh. Legitimate approach, bodily passage, positional control and grappling can bring attackers inside the shield; ordinary basic anchored shields **do not protect against close-range attacks within a grapple**. This does not allow arbitrarily relabeling a fast attack as a slow one; determine lawful attack effects using the ordinary combat and positioning rules. A trip or other maneuver must itself be legally delivered; the shield is not automatically bypassed because a maneuver is called a trip.
- **One target, one anchor shield:** An individual target may bear **one ordinary anchored shield** at a time. Multiple separately cast directional shields remain permissible across distinct eligible targets, with actual action, MP, duration, upkeep, and Channel Limit restrictions; do not invent a generic prohibition on multiple shield castings.
- **Timing and Power, author-selected baseline:** A basic anchored White Mana shield applies **100% of its eligible spell Power for the current turn**, against each attack within its protected arc; the **three-round** version applies **50% of eligible spell Power** against each such attack during that duration. The analogous basic **Red imbuement** adds its independently calculated spell-Power rider to **all eligible attacks** over the same one-turn 100% or three-round 50% options, never multiplies an entire physical attack. No extra attacks are generated. Existing action economy and Channel Limit still govern the casting. Larger-area and specialist Concordance improvements are not established by this entry.
- **Black counter:** An eligible Black Mana attack contacting a magical shield **subtracts its own applicable Power from the shield's remaining protective Power**, possibly unraveling it entirely. The reduced protection **stays reduced for the remainder of that casting**, rather than refilling each round. Black's previously author-selected wound-exploitation bonus is **+50% of its own base spell Power per existing bodily wound, capped at +100%**; that bodily-wound bonus does not automatically apply to a shield, which has no bodily wounds. Global additive-rider philosophy remains: independently calculated mana/spell effects do not multiply the completed combined attack.
- **Barrier wall (White and Green structure interface):** Unlike permeable creature-anchored shields, a **world-anchored structural barrier** stops physical travel from either side, blocks allied as well as hostile attacks, and is **probably transparent** (transparency is a design proposal, not locked). White walls and Green-created physical structures should share the future common structure-building/structure-damage system. **A physical attack that overcomes structural barrier Power can physically break the barrier**; it is not indestructible or exclusively vulnerable to countermagic. The user considers **two or three structural wound states**, but explicitly defers the number, thresholds, and actual break sequence until structure-creation mechanics are designed. Black reduction to magical barrier Power remains relevant; exact interaction with a partially broken structure remains open.
- **Open for calibration:** Exact directional arc (90° versus 180° was suggested but not approved); facing/turning and slow-infiltration timing checks; whether a shield's Power subtracts before or after other defenses; the detailed multiple-hit shield contest; base spell Power, MP and Channel costs; barrier geometry, transparency, structure wounds, and relationship between Green-created physical matter and White walls; Concordance's specialist superior protection. Do not use any earlier illustration or experimental calculator as final canon.

---

## November 19, 2026 — AUTHOR APPROVAL: Spiritus astral projection consequences and Warlock full-system development (LATEST)

**Author confirms the following qualitative/numerical Soul-Shaping / Spiritus projection mechanics** for the planned modular Warlock system, superseding tentative alternative wording:
- **Abandoned physical body:** helpless while astrally projected.
- **Components:** the **Cognum and Anima transfer** into the incorporeal projection. The **Spiritus does not fully transfer**; it **stretches from the body and tears off a piece**, replacing what is lost through a **high upfront mana expenditure**. Preserve the established Corpus as physical body and avoid describing the entire Spiritus as freely detached. Exact Spiritus restoration, fragmentation and interaction with Soul Shred remain unresolved.
- **Short range:** a **visible tether** links projection and body, allowing the projected spirit to use **mana accessible to its host/body**. Warlocks retain **zero natural MP**; they still may shape accessible external mana, so this does not imply the host possesses a new innate MP pool.
- **Tether defense and severing:** the tether has **1 wound of durability**, uses the **projected spirit's Endurance**, and a **non-blunt attack against the tether incurs +1 difficulty**. If the tether is severed/destroyed, the spirit **immediately returns** to the body and the **body takes 1 wound**. Other attack/targeting/defense rules remain ordinary until further adjudication.
- **Long range:** projected spirit can **still shape mana from lawful accessible external sources**, including Warlocks; however it **cannot access the host body's mana through the short-range tether** and suffers an **approximately 50% reduction across all attributes**, pending the exact multiplier/rounding mechanics. No free generation, harvesting bypass or universal remote source access is implied.
- **Destruction of the spirit's projection:** whether short or long range, **the spirit reunites with its physical body and the body receives 3 wounds**, reflecting transferred soul injuries. For long-range projection, reunification takes **approximately one minute**. The user explicitly says three wounds usually incapacitates rather than kills outright, but actual survival still follows applicable wound rules and pre-existing injuries. **Short-range projected-spirit destruction is distinct from cutting its tether**: spirit destruction costs **3 wounds**, tether severance **1 wound**. Exact return timing for short-range spirit destruction is OPEN; do not import long-range one-minute delay automatically.
- **Future calibration:** upfront mana cost, tether reach/visibility, long-range boundary, projection duration, actions, targeting incorporeal beings, Spiritus restoration and Soul Shred interactions, rounding of ~50% attribute reductions, reentry, prior bodily wounds and defenses remain OPEN. No final MP/Channel Limit formula approved.

**Author confirms the preceding foundational Manashifting directions:** broad Red energy enhancement, Blue temporary nonchemical morphological adaptation to actual circumstances, Green physical/living repair and object growth, White order/finite overshield, Black entropy/darkness; Mana-Shaping, Spell-Shaping and eventually Soul-Shaping development, with Craft-unique Esotery; 100%-efficient lawful color-compatible Leywell filling. Soul creation and destruction remains deferred until other Crafts are developed.

**Design priority:** Carry Warlock/Manacraft through **a complete top-to-bottom modular calibration**, including Warlock-specific universal discipline applications, its external mana handling/economy, spell modifiers and full Craft-specific progression. Previous approved Manacraft skill fees/ledger remain authoritative until explicit migration. Proposed MP, SP, Power, object-creation and Channel Limit equations must be labeled exploratory until approved.

---

## November 19, 2026 — AUTHOR DIRECTION: Foundational Manashifting, Warlock disciplines and soul projection (LATEST)

**Status:** Author-approved qualitative direction for the **planned** modular Manacraft migration. Preserve existing approved historical five Warlock discipline/rank/SP/MP ledger until explicitly migrated; do not invent replacement numerical mechanics, no free abilities beyond explicit new conceptual directions.

**Fundamental raw mana expressions (not an exhaustive list):**
- **Red — Energize:** Enhances/transfers available energy through a relevant target or medium: a thrown rock accelerates, a burning object grows hotter, an electrical source can discharge more violently; a living target may be *sped up*, not automatically damaged. Red should interact with actually present energy/material rather than grant arbitrary source-free radiation, electricity, or other exotic energy. Unstructured destructive projection remains possible with lawful mana.
- **Blue — Adapt/Morph:** Temporarily alters **shape and physical arrangement**, not chemical composition. Flexible matter such as rope may move or weave in intricate ways; form changes can affect equipment. Organism adaptations are **responsive to immediate conditions rather than selected freely by caster**: e.g., gills under water, a survival change during freefall/crushing, but no arbitrary wings or muscle enhancement outside a qualifying threat. Blue can redirect energy and produce crude emotion/perception attacks; the previously approved wounded-target sensory-overload/pain and coordination effects remain.
- **Green — Grow/Heal/** **Repair** (replace any use of *regenerate* in the newly proposed five-color expression list with **repair** so objects are explicitly eligible). Green can heal or repair, stimulate growth, and create/expand natural material **including stone**, using mana and the emerging universal object-creation system. Novice/low-investment stone may be porous, impure, air-filled and weak; very high investment and skill can create extraordinarily dense/strong stone. Quality, volume, density, resistance and costs follow the future object-creation framework. Neither biological-only restriction nor automatic unlimited perfect matter creation is intended.
- **White — Organize/Order:** Grants a finite, overwhelmable **all-angle overshield** rather than automatically stacking huge END bonuses; may improve accuracy, clarity and cognition, increase radiant light, and **organize unordered physical items when spread through surrounding air** (e.g., tidy a messy pile). Exact sorting logic, scope and overshield calculations remain open. White restoring a confused person's coherence is a suitable effect, not automatic negation of every hostile mental condition.
- **Black — Degrade/Entropy:** Weakens, decays, exhausts, suppresses light to make darkness and deteriorates structures. Aiming into an existing wound may inflict more harm than an equivalent basic Red blast. Condition buildup and comparisons are still unpriced.

**Manashifting baseline:** Warlock raw mana manipulation remains broadly improvisational. Learned specialties expand its interactions and limitations rather than charging a rank for every trivial aim, move, shape or use. Keep actual external mana supply, eligible targets/materials, resistance and existing handling/resource rules. The above corrects exploratory claims that red necessarily injures creatures or Green is biological-only.

**Proposed Craft-specific specialties (direction, rank progressions OPEN):** **Mana-Shaping** explores unusual targets (air, organs, internal spaces), novel raw-mana expressions and eventual combinations of two mana colors into emergent effects; **Spell-Shaping** counters/rebounds selected colors, actively and deliberately reshapes allied spells by adding one's own investment/shaping, and eventually infuses different mana colors into existing spell structures. It **does not passively share all Warlock skills with the party**; every modification requires active shaping or mana investment and lawful access. **Soul-Shaping** concerns the four established soul components and finally the whole soul, but full mechanical design and high-level soul creation/destruction/restructuring are **DEFERRED pending development of Summoners, Cogmarshals and other peers**; don't finalize the five-rank placement yet. Craft-specific **Esotery** is a **discipline family every Craft may have, but the effects and purchased ranks are unique to that Craft**, not a universal cross-Craft skill; Wakecraft water optics do not give Pyromancy Brimstone.

**Soul-Shaping qualitative directions:** **Anima**'s main support application is to **transfer actual externally held compatible-color mana into another creature's natural MP pool**; recipient's mana color must match. **Do not include the earlier suggestion to change mana affinities**. Other established Anima casting-suppression possibilities may be explored. **Cognum** memory editing, theft and fabrication; **Corpus** bodily sculpting; **Spiritus** astral projection; high-tier integrated soul work may reshape, create or destroy souls, potentially with materials including other souls, but no mass-soul-merging or automatic power creation is approved as a finished technique. Soul integrity, free will, resisting, ethics and Starspawn exceptional protection must receive future treatment.

**Spiritus astral projection:** At short range, a projected incorporeal spirit remains attached to its body by a **visible tether**, enabling access through the tether to **mana held by its host/body**. At long range projection lacks access **through the tether** to the host body's mana and incurs **substantial penalties across attributes** (exact bands/costs/ranges OPEN). This does **not** cancel the Warlock-specific **0 natural MP** rule or create free spellcasting: the precise interaction for Warlocks accessing **external** mana while projected is explicitly OPEN. Resolve which soul components project, body vulnerability, tether severing, ordinary incorporeality, death, range, target contest, permission and reentry before final mechanics.

**Universal Transformation:** An eligible learned form/imbuement may be sustained for hours or potentially permanently, with major cost and **Soul Strain as a possible permanent-effect tradeoff**. The Craft must first possess the adaptation/effect and deliver its lawful medium; universal Transformation does not hand everyone Blue morphology or unrestricted biology. Numerical duration, costs and strain remain OPEN.

**Warlock mana economy:** The author's reaffirmed **existing sources** include willing allies, accessible ongoing spells and Leywells; universal Medium advancement opens increasingly unusual sources. **Warlocks can fill a properly color-matched conventional Leywell at 100% transfer efficiency**, meaning no mana is lost to a transfer tax, **not** that they conjure mana or ignore handling, capacity, permissions, timing or the Leywell's strict single-color identity. Specialized Primordial Leywells remain separate. This is a new explicit efficiency ruling; exact action/throughput and mana-timing mechanics remain for modular integration.

---

## November 19, 2026 — AUTHOR CLARIFICATIONS: Pattern Weaving, specialized Primordial Leywells, and Spirit Anchors (LATEST)

**Pattern Weaving:** A captured spell pattern is held **in one hand together with the mana of the original spell**. For example, on intercepting a blue Psychic spell, a Warlock may hold its original blue mana and pattern for subsequent lawful replication, **or fling it back as raw blue mana** rather than preserve/cast the pattern. A pattern is not a separately transferable store independent of that original mana; placing it in a container loses the pattern. Ordinary one-hand Handling Capacity, temporary-holding limits, contested capture, MP minimums, modifiers and effect scaling remain relevant; exact recast expenditure/timing and how a counterprojection interacts with hand limits remain open.

**Dispel:** The author expressly agrees with the previous interpretation: it seizes/disrupts an incoming spell's medium rather than harvesting its mana, with the approved twice-effective disruptive comparison and four actions or two actions plus one self-inflicted wound. Precise contest, reaction readiness and timing remain for modular spell calibration.

**Primordial Mana:** The author accepts **new, specialized Leywells** intended to hold prepared colorless Primordial Mana. Existing ordinary **single-color** Leywells still only accept their matching original colors. The specialized variant's construction, capacity, costs, input compatibility and safeguards remain to define, rather than granting an automatic conversion to existing ordinary Leywells.

**Ghost Mana, ghosts, and Phantoms:** Manifestation is **not simply location-based**. A lingering ghost or Phantom has a **Spirit Anchor**, an object deeply meaningful to that individual in life. The Spirit Anchor is necessary to its ghostly persistence/manifestation. **Destroying the Spirit Anchor releases the ghost permanently**, creating high stakes for its protection. A ghost that fails to absorb enough mana **goes dormant within its Spirit Anchor** until the anchor is touched, whereupon it **siphons the mana needed to manifest**. Ghosts commonly have **imperfect, emotionally shaped memories**. Hostile ghosts remain **Phantoms**, without automatic loyalty to their summoner, feeding on others' mana and pursuing unfinished business. Exact touch activation, energy demand, resistance, whether object damage short of destruction affects a ghost, dispelling versus true release, and exception handling remain open. Original ordinary Cognum decay remains the default; lingering ghosts are exceptional.

**Modular-spellcasting calibration backlog (not new numerical approvals):**
- *Universal:* action/MP/modifier scaling, Channel Limit and automatic Craft Mastery equation, attack Power and applicable protections, interaction between Power versus Range versus area versus effect count, exact consolidated Magnitude five-rank allocation, duration/upkeep/Autonomy triggers and remote scry ranges, temporary/permanent Transformation resistance and Execute adjudication.
- *Medium:* precise physical-material extraction throughput, source depletion, hot/cold ash, Hearthiron thermal-equivalence accounting, spell eligibility, connection sensing, and high-rank medium supply.
- *Wakecraft Esotery:* Mirrorwake evidence clarity and reach; Surface Dominion physical durability; Refraction illusion checks; Cloudcraft long-term ×2 efficiency and mobility/slow strengths; Abyssal Pressure output and resistance.
- *Pyromancy Esotery:* Breath of Flame oxygen enrichment/depletion as a function of **Power (not Range)**, spell MP modifiers, immediate fire-spread, suffocation, explosion thresholds; Ghostfire material choices; Brimstone creation durability/explosive Power, detonation and ash usage (its volatility is **not adjustable**); Ashen Reconstruction hot/cold quality, material and Phoenix Reversal timing; Cursed Flame material selection, combustion rate, oxygen dependence and sustain fee.
- *Warlock Esotery:* Ghost Mana emotional/word-memory resolution, Spirit Anchor manifestation, drain/siphon rate, dormancy and release; Pattern Weaving hand capacity/timing, minimum recast, original-pattern modifiers, raw-mana return, and transfer destruction; Dispel doubled contest, readiness and actions/wound; Mana Conduit END/MP and material-AR/MR tradeoffs; Primordial Mana five-color input ratios, 2× potency placement, random output distribution, Wild Magic event probabilities, specialized Leywell crafting/holding capacity.
- *Interface with existing Manacraft:* preserve approved Warlock zero innate MP, 30/60-second hand holding, END-based one-hand cap, existing absorption contest, original five discipline/skill ledger, Leywell strict color identities, and Soul Reaping special Execute cost/yield pending formal integrated migration.

**Workflow:** Complete universal modular spellcasting fundamentals before assigning unapproved numerical formulas or converting the historical SP/rank ledgers; approved thematic/rank directions are not a fully migrated price catalogue.

---

## November 19, 2026 — AUTHOR APPROVAL: Warlock Esotery ranks I–V (LATEST)

**Status:** Explicitly selected qualitative five-rank Esotery direction. Detailed mana costs, Power/resistance math, duration, SP ledger integration, numerical capacity interactions, and modular spell mechanics remain **OPEN**. This new proposed Esotery progression does not silently delete or rewrite the older approved five Warlock Manacraft skill tracks or their existing fees.

**I — Ghost Mana:** Warlocks may extract from objects and surroundings primarily **emotional imprints** of events. At low Power, a murder weapon might convey ominous emotion or a sense of wrongdoing; at higher Power, distinct fragments of spoken words may emerge. Objects are not intelligent or omniscient witnesses. At sites of especially great tragedy, a Warlock may seek to summon a true lingering **ghost**, where a departed creature's **Cognum has stubbornly adhered to the nearby environment**. Hostile ghosts are **Phantoms**. Summoning creates **no loyalty, obedience, or safety**: Phantoms feed on others' mana and seek to resolve unfinished business. Actual conditions for Cognum persistence, ghost intelligence, manifestation, summoning, resisting, feeding, and dismissal are not quantified. Ordinary Cognum decay at death remains the default; persistent ghosts are exceptional.

**II — Pattern Weaving:** When draining mana from an existing spell, the Warlock may also take its **spell pattern into one hand**. While personally holding the pattern, pushing mana through that hand **recreates the spell with the original caster's modifiers**. The Warlock may invest more or less mana in mana-scalable aspects, including Power, but **must spend at least the minimum mana necessary to cast the spell**; lower expenditure cannot erase the original rank/prerequisite or minimum costs. **Storing the captured pattern in a container destroys it.** Pattern Weaving does not teach the Warlock the spell permanently or grant general conventional spellcasting. Compatibility with the one-hand Handling Capacity, safe 30-second/absolute 60-second ordinary holding duration, source colors, spell eligibility, magical medium/delivery and Channel Limit is unresolved; do not invent a bypass or a new storage method.

**III — Dispel:** The Warlock seizes the **medium** of an incoming spell rather than absorbing its mana. Relative to ordinary absorption the disruptive effect is **twice as powerful**, but the spell's mana is forcibly blasted outward as **dissipated, unusable mana** instead of being kept by the Warlock. **Requires a total of four channeling actions**, or **two actions if the Warlock willingly suffers one wound**. Clarify later how the medium seizure, doubled Power, interruption timing, ordinary absorption contests, action prep, target selection and emitted energy behave; this is not an automatic all-purpose reaction, unresisted cancellation, mana gain, or a replacement for ordinary medium-seizure rules.

**IV — Mana Conduit:** The Warlock changes the **magical reactivity** of matter and living creatures, increasing or decreasing it at the expense of corresponding physical properties. At maximum effect, even **Glassweave** may reverse its normal physical-versus-magical robustness, becoming physically very strong and magically weak. Applied to a creature, one direction sharply **reduces END while multiplying maximum mana reserve by more than compensates for that decrease**; the reverse **strengthens END while shriveling the mana reserve**. Exact attribute tradeoff, minimums, defenses, duration, eligibility and material-specific MR/AR formula are OPEN. Warlocks' approved **zero natural MP** and one-hand Handling Capacity remain unchanged by default: creature mana-capacity modification does not silently give Warlocks internal mana storage.

**V — Primordial Mana:** Combine **all five existing colors of mana** into a single **colorless** mana form. This does **not** create a sixth ordinary mana color or permit using Primordial Mana as any chosen color. When it produces an effect, the **manifested mana color is random**, its output effects are **twice as potent** as ordinary mana, and Wild Magic may cause bizarre additional phenomena, including **small portals to the Celestial World** and unexpectedly intricate spell effects. Because access to all five input colors is difficult in battle, Warlocks commonly **prepare it ahead of time and store it in a Leywell**. Ordinary Leywells' established *one-color-only* acceptance conflicts with assuming they can hold colorless Primordial Mana: the author's pre-storage intention is approved, but **the requisite Leywell exception, special receptacle, or construction specification is OPEN**, so do not claim an ordinary single-color Leywell automatically supports colorless storage. Input amounts, conversion loss, actual random color distribution, wild-effect probabilities, multiplier placement and portal rules remain OPEN.

**Prior Pyromancy clarification (same conversation):** For **Breath of Flame**, increasing spell Power increases the **degree of oxygen concentration or removal within a small space**, **not the spell's Range**. Range and effect area are governed separately by the universal modular spell disciplines; no numeric concentration or suffocation threshold is yet approved.

---

## November 19, 2026 — CORRECTION: Soul-color reward and Hero/Legend Execute thresholds (LATEST)

The user expressly confirms Soul Reaping grants mana of the victim's **SOUL color**, not soil color. As a lethal **Execute**, its effective Power uses the latest universal wound progression: **ordinary targets ÷4/÷3/÷2/÷1 for 0/1/2/3+ wounds; Heroes/Legends automatically resist at 0–2 wounds, then face ÷3 at 3, ÷2 at 4, and ÷1 at 5+ wounds**. This supersedes the older Execute note's unfinished 4+-wound divisor and unconfirmed wording. Soul Reaping mana yield and whether its historical 20 MP activation/5 MP upkeep are revised versus the general 10 MP baseline remain **open**. Preserve the previous detailed exceptional soul protections pending explicit revision.

---

## November 19, 2026 — AUTHOR CORRECTION: Mana Harvest V Soul Reaping is a lethal Execute (LATEST)

**Soul Reaping is now a lethal Execute**, governed by the newest universal Execute framework in [Magical Media and Contests](35_Magical_Media_and_Contests.md): ordinary Execute baseline **10 MP and one-quarter of a comparable offensive spell's Power**, with the target's wounds reducing its 4× divisor by one per wound (mathematical handling of four or more wounds open). Heroes and Legends below three wounds automatically resist Executes. Successful Soul Reaping lethally executes its target and grants the Warlock a **massive but numerically not yet defined mana yield of the victim's soul color**, **not XP damage**. The user wrote 'soil' in the color sentence; this is provisionally read as 'soul' and remains to be confirmed. **This supersedes earlier Soul Reaping text insofar as it describes capturing a soul for later storage/transfer instead of a lethal Execute**, without eliminating the established exceptional protections of Astral Hearts and Celestial Recall or rules for other soul-containing abilities. The earlier rank-V **20 MP activation and 5 MP/round upkeep** have not been reconciled with the **10 MP default Execute cost**: neither silently overwrite the special price nor claim it remains final for the revised effect. Targeting, contact, mana yield and storage constraints remain open. Other XP-erosion mechanics elsewhere are unaffected. The historical Soul Reaping table and descriptive section below are superseded where inconsistent with this newest decision.

---

# Mystaria — Warlock / Manacraft: Authoritative Skill Reference

**Status:** **APPROVED CANON — revised November 4, 2026**. The user's latest explicit decision replaces the former 25-rank Warlock trees with the recovered *Warlock Skills System, Revised*. The separately approved MP activation and upkeep schedule is incorporated below. **Five skills × five ranks × 5 SP = 125 SP**; innate Manabending costs 0 SP. **Latest approved capacity override:** a single hand temporarily holds `max(1, floor(natural effective END / 5)) MP`; this supersedes the historical spell-load categories.

**Precedence:** The five recovered trees and this dossier supersede the conflicting older `Mystaria_Warlock_Skills_Canon.md` and its earlier copy in `04_Warlock_Manacraft.md`, including former Rank V techniques such as *Thousand Invisible Hands*, *Grand Expression*, *Great Reclamation*, *Living Arsenal* and *Absolute Reversal*. The older rank-specific MP prices belong to those superseded techniques and **do not automatically transfer** to differently functioning abilities. The new MP fees have separate explicit user approval. Earlier rules not in conflict remain valid.

**Identity:** Only chosen **Moontouched** Warlocks of **Surrender** use Manacraft. They have **0 natural MP, no internal reserve of spendable mana, and no independent conventional spellcasting**. Ordinary power is borrowed from sources and kept in suitable external vessels; the hand is only short-term handling space. Hero attribute advancement is separate from Skill Points.

## Skill Point costs and prerequisites

| Rank | Minimum Hero level | Cost for rank | Cumulative cost within discipline |
|---|---:|---:|---:|
| I | 1 | **5 SP** | 5 SP |
| II | 10 | **5 SP** | 10 SP |
| III | 25 | **5 SP** | 15 SP |
| IV | 50 | **5 SP** | 20 SP |
| V | 80 | **5 SP** | 25 SP |

Earlier ranks in a discipline are prerequisites for later ranks. These costs supersede the recovered manuscript's proposed **1/3/5/7/9 SP** schedule. All **25 ranks cost 125 SP**; no separate purchase is required for basic Manabending.

## Cost and handling conventions

- **Activation fee:** Consumed when beginning a technique; does not guarantee success against a resisting target.
- **Upkeep:** Paid at the specified interval to maintain an effect. Where the approved schedule states **per round**, use the established six-second round.
- **Released mana / manifestation energy:** Additional MP spent on the actual physical or magical effect, rather than the activation fee; costs are additive.
- **Stored mana:** Mana placed in a vessel; it remains available there until discharged or otherwise lost, and is additional to the sealing fee.
- **No personal reserve:** MP activation and upkeep draw on accessible **external** mana, not naturally generated MP in the Warlock's soul.
- **Handling limit:** The Warlock's hand can retain mana safely for **30 seconds** (absolute maximum **60 seconds**). Immediate controlled energy is constrained by Handling Capacity even if the external supply is enormous. Large transfers may be staged, but a single instantaneous effect may not exceed the applicable instantaneous limit merely by calling it a multi-step transfer.
- **Unresolved payment sequencing:** It has not been explicitly settled whether mana harvested in the very same action may pay that action's initial activation fee. Similarly, the suggestion to route large activation payments directly from an external reservoir without ever passing the fee through the hand is **not separately established as canon**; source access, control rate and timing still require adjudication. No unlimited bypass of Handling Capacity is permitted.
- **Old source notes:** Where old `04_Warlock_Manacraft.md` descriptions or MP fees contradict the new trees, they are historical, not parallel purchasable abilities.

---

## Full recovered system, with approved replacement mechanics

## Warlock Soul Anatomy

Warlocks have the same four soul parts. Their larger, more powerful **Anima** fills the space in the **Spiritus** where pure mana would ordinarily be stored. They need dietary managmins to survive. Their Anima uses trace amounts of mana to move other mana, always less than 1 MP. Warlocks have **0 natural MP** and draw on external mana to use Manacraft.

## I. Base Ability — Manabending

Manabending

Innate · Free

Every Moontouched Warlock possesses this ability without purchasing a skill rank.

| Property                  | Base mechanics                                               |
| ------------------------- | ------------------------------------------------------------ |
| Range                     | 2 + (2 × INT) meters                                         |
| Mana manipulation         | All five colors                                              |
| Absorption                | Drains accessible raw mana and portions of active spells     |
| Projection                | Releases raw mana into a target                              |
| Temporary storage         | One hand, safely for 30 seconds; absolute maximum 60 seconds |
| Handling Capacity         | `max(1, floor(natural effective END / 5)) MP` in one hand      |
| Conventional spellcasting | Impossible                                                   |
| Internal mana storage     | Impossible                                                   |

### Range scales significantly with Intelligence

Base Manabending Range

Range increases linearly with effective Intelligence, before Mana Reach specializations.



A Warlock with 100 Intelligence can manipulate accessible mana more than 200 meters away, even without specializing in Mana Reach.

However, range is not omniscience. They must perceive or otherwise locate the magical source, and ordinary Manabending cannot reach through solid magical barriers or concealed obstacles without appropriate techniques.

### Handling Capacity — Direct MP per Hand (approved November 4, 2026)

A Warlock can temporarily hold **one hand's worth of raw external mana**, not an internal reserve. The approved **MP per hand** limit replaces the earlier spell-load size, count, and END threshold system.

```text
Hand Capacity (MP) = max(1, floor(natural effective END / 5))
```

Thus capacity is **20% of natural effective END**, rounded down, with a **minimum of 1 MP**. This rule uses the natural effective END relevant to Warlock handling, not a separately purchased MP reserve or a new stat.

| Natural effective END | Maximum MP held in the one hand |
| ---: | ---: |
| 2 | 1 MP |
| 10 | 2 MP |
| 25 | 5 MP |
| 40 | 8 MP |
| 60 | 12 MP |
| 100 | 20 MP |
| 150 | 30 MP |
| 200 | 40 MP |

**Holding duration remains unchanged:** safe temporary holding is **30 seconds**, with an **absolute maximum of 60 seconds**. **Only one hand** is used for this handling allowance; two hands do not combine or double capacity under this ruling.

This is the upper bound on the quantity of mana immediately handled or absorbed in one interaction and, where an existing technique explicitly uses Handling Capacity as its throughput cap, that cap continues to apply. A large external supply does not make a Warlock capable of handling unlimited mana at once. Large transfers may be staged through external sources and vessels over time, subject to the existing handling limits and technique rules. The hand cannot hold a whole oversized spell just because the Warlock wins the absorption contest.

**Unchanged:** Manabending's range, INT absorption contest, all Manacraft skills, SP costs, activation/upkeep fees, prerequisites, external-source requirements, and the already unresolved payment-sequencing questions. In particular, the new hand-capacity formula **does not by itself authorize** paying an oversized activation cost directly from an external source or bypassing the limit through same-action harvesting.

### Raw Blue Projection Against Wounded Targets (approved November 4, 2026)

When a Warlock blasts a wounded target with **raw blue mana**, its primary effect is **sensory overload and amplification of the pain of existing wounds**. The target's bodily perception can also fracture, disrupting their sense of where their body is and how its movements fit together, with accompanying disorientation and impaired coordination.

This is an unstructured expression of raw blue energy, distinct from **structured Sorcery**. It does **not** freeze the target or turn into a splash of water. This approval establishes the wounded-target blue effect only; optional proposals for other colors or additional effects are not thereby canonized. The existing **Blue Hole — Shifting Depth** remains unchanged.

This clarification adds no skill or prerequisite and changes no established SP/MP cost, rank, level gate, range, Handling Capacity, or external-source requirement. **UNRESOLVED:** exact duration, numerical pain or coordination penalties, resistance procedure, and any damage formula for this effect have not been approved.

### Absorbing Hostile Magic

The approved Intelligence contest is:

\\[ \text{Absorbable fraction}=\min\left(100\\%,\frac{\text{Warlock INT}}{2\times\text{Caster INT}}\times100\\%\right) \\]

| Warlock INT compared to caster | Maximum absorption |
| ------------------------------ | ------------------ |
| Half                           | 25%                |
| Equal                          | 50%                |
| 1.5 times                      | 75%                |
| Twice or greater               | 100%               |

Handling Capacity still limits how much can be absorbed in one interaction. An oversized spell cannot be completely absorbed merely because the Warlock wins the Intelligence contest.

This contest also forms the foundation for advanced Dominion techniques, though controlling another's magic is generally more demanding than draining it.

## II. The Five Warlock Skills

The five disciplines now cover the complete range of Manabending:

| Skill          | Governs                                       | Rank V breakthrough                          |
| -------------- | --------------------------------------------- | -------------------------------------------- |
| Mana Reach     | Distance, connections, spatial manipulation   | Creating and destroying ley lines            |
| Mana Power     | Projection, concentration, raw mana effects   | Creating five-colored mana holes             |
| Mana Harvest   | Absorption, conversion, extraction            | Absorbing souls                              |
| Mana Imbuement | Storage, preparation, autonomous enchantments | Soul vessels and enduring magical constructs |
| Mana Dominion  | Spell control, suppression, magical authority | Creating absolute anti-magic zones           |

### 1. Mana Reach — The Invisible Hand

Mana Reach concerns the connections between magic, matter, and living creatures.

Higher ranks no longer simply extend maximum range. Intelligence already accomplishes that. Instead, this skill transforms the ways Warlocks establish and exploit connections.

| Rank | Technique        | New ability                                                                                                                                                                       |
| ---- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I    | Unseen Hand      | Manipulate individual magical sources with exceptional precision. Draw mana through tiny openings, extract it from specific components, or project it into hard-to-reach targets. |
| II   | Crooked Thread   | Bend mana connections around obstacles and through indirect pathways, allowing manipulation without a straight line of sight.                                                     |
| III  | Binding Thread   | Establish tangible mana tethers capable of pulling, holding, lifting, or restraining physical objects and living creatures.                                                       |
| IV   | Walk the Current | Attach a connection to an existing ley line or magical conduit, allowing Manabending to travel far beyond normal range along that established pathway.                            |
| V    | Ley Carving      | Create, reroute, or sever actual ley lines, permanently changing how ambient mana flows through a region.                                                                         |

#### Approved MP costs — Mana Reach

| Rank / technique | Activation | Upkeep | Conditions / limitations |
|---|---|---|---|
| I — Unseen Hand | 1 MP | 1 MP/minute | Precision connection; ordinary manipulation still obeys Handling Capacity. |
| II — Crooked Thread | 2 MP | 1 MP/minute | Indirect connection around obstacles; does not bypass magical resistance. |
| III — Binding Thread | 3 MP | 1 MP/round | Significant weight or resistance also requires additional suitable released mana; no free unlimited force. |
| IV — Walk the Current | 4 MP | 2 MP/minute | Requires an existing accessible ley line or conduit. |
| V — Ley Carving | 12 MP | 6 MP/minute during alteration | Lasting regional alteration requires **at least 50 additional MP invested**, with substantially more for larger changes; this floor does not guarantee success. |

**Cost accounting:** Activation/control fees consume external mana. Any separately specified released or stored mana is additional. Active handling still obeys the approved limit.


#### Rank V — Ley Carving

Ley lines are naturally occurring currents of magical energy passing through Mystaria.

A Grandmaster of Mana Reach can manipulate these currents directly.

They might establish a new ley line between two distant magical locations, redirect a natural current toward a settlement, or sever the line supplying a powerful enchanted fortress.

Creating a ley line does not create free mana. It opens a new pathway through which existing ambient mana can flow.

Destroying a ley line is equally consequential. The loss may affect local enchantments, Starspawn habitats, and surrounding magical ecosystems.

Permanent large-scale alterations require substantial energy, preparation, and a stable connection to the existing mana network.

Specialization: Mobility, physical manipulation, unconventional combat, exploration, and magical infrastructure.
### 2. Mana Power — The Shape of Raw Magic

Mana Power governs how borrowed mana expresses its natural properties when released.

An ordinary Warlock can discharge raw mana. A specialist can concentrate, direct, sustain, and arrange it into extraordinarily dangerous phenomena.

| Rank | Technique            | New ability                                                                                                                                |
| ---- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| I    | Focused Expression   | Select which natural property of a mana color to emphasize and release it in a precise direction.                                          |
| II   | Flowing Expression   | Shape a continuous release into streams, arcs, expanding surfaces, or concentrated jets rather than a single burst.                        |
| III  | Sustained Expression | Maintain a stable raw-mana phenomenon through continuous feeding, allowing it to remain active for as long as suitable energy is supplied. |
| IV   | Pressure Geometry    | Establish localized concentrations and gradients of mana that can contain, compress, repel, or redirect matter and magical energy.         |
| V    | Mana Singularity     | Create a temporary hole of concentrated mana, producing a powerful environmental phenomenon determined by its color.                       |

#### Approved MP costs — Mana Power

| Rank / technique | Activation | Upkeep | Conditions / limitations |
|---|---|---|---|
| I — Focused Expression | 1 MP + MP released | None | The natural effect consumes the released mana. |
| II — Flowing Expression | 2 MP + MP released | 1 MP/round + MP released | Continuous release consumes additional mana. |
| III — Sustained Expression | 3 MP | 1 MP/round + MP released | Must continually supply suitable external energy to maintain the expression. |
| IV — Pressure Geometry | 5 MP + MP released | 2 MP/round + MP released | Additional energy is required for the concentration/gradient. |
| V — Mana Singularity | 12 MP + minimum 20 MP manifestation energy | 4 MP/round + minimum 10 MP released per round | **32 MP minimum to create**, **14 MP minimum per 6-second round** thereafter. Same base costs for all five holes; additional energy may increase scale, effectiveness, or area subject to source and Handling Capacity. |

**Cost accounting:** Activation/control fees consume external mana. Any separately specified released or stored mana is additional. Active handling still obeys the approved limit.


#### Rank V — The Five Mana Holes

There are five distinct mana holes, one for each of Mystaria’s five mana colors.


Red Hole — Furnace Heart

A concentrated vortex of destructive energy. Produces intense heat, violent pressure, and explosive bursts, drawing nearby matter toward its burning center before violently releasing accumulated force.


Blue Hole — Shifting Depth

Creates a region of extreme adaptation and transformation. Materials become unstable in form, fluid movement becomes unpredictable, and light and perception distort around the hole.


Green Hole — Genesis Bloom

Releases concentrated life energy, causing extraordinary growth, accelerated biological processes, and rapid regeneration in nearby living matter. Uncontrolled growth may become destructive.


White Hole — Immutable Crown

Establishes a region of overwhelming stability, suppressing movement and reinforcing nearby matter. Its concentrated boundaries can become nearly impenetrable barriers or violently repel disturbances.


Black Hole — Final Silence

Creates a vortex of entropy that draws usable energy out of its surroundings, weakening structures, chilling matter, and degrading enchantments. Unlike a literal gravitational black hole, it does not possess infinite mass or unrestricted destructive power.

The holes are concentrations of mana, not permanent astronomical singularities.

Creating one requires an enormous external mana supply relative to ordinary Warlock attacks. Maintaining it is even more expensive.

A powerful Warlock might create a devastating hole for several seconds, while a Warlock with access to a large prepared reservoir or ley line might sustain one considerably longer.

Specialization: Offensive combat, powerful defenses, environmental manipulation, and extraordinary raw-mana phenomena.
### 3. Mana Harvest — The Hungry Vessel

Mana Harvest governs where magical energy comes from.

At its highest ranks, the distinction between existing mana and the physical universe begins to blur.

| Rank | Technique              | New ability                                                                                                                                                              |
| ---- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| I    | Afterglow              | Recover residual mana from recently expended spells, damaged enchantments, and dissipating magical effects.                                                              |
| II   | Ambient Harvest        | Extract loose mana directly from the environment, drawing upon the surrounding magical atmosphere or exposed ley currents.                                               |
| III  | Hollow Radius          | Establish a continuous draining field that siphons accessible mana throughout an area, including that powering nearby spells and enchantments.                           |
| IV   | Fundamental Conversion | Convert ordinary matter and natural energy—such as heat, motion, sunlight, and physical materials—into raw mana.                                                         |
| V    | Soul Reaping           | Extract and absorb the soul of a vulnerable living or recently deceased creature, temporarily containing it before transferring it into a suitable external soul vessel. |

#### Approved MP costs — Mana Harvest

| Rank / technique | Activation | Upkeep | Conditions / limitations |
|---|---|---|---|
| I — Afterglow | 1 MP per attempt | None | Recovery does not create new mana. |
| II — Ambient Harvest | 2 MP | None separately stated; covers 10 minutes | Only ambient accessible mana may be recovered. |
| III — Hollow Radius | 4 MP | 2 MP/round | Energy must be released, redirected, or stored externally; extraction rate respects Handling Capacity. |
| IV — Fundamental Conversion | 6 MP | 2 MP/round while converting | Proposed conversion throughput cap approved with cost package: **at most Handling Capacity per round**. Source material/energy is depleted. |
| V — Soul Reaping | 20 MP | 5 MP/round while extraction is attempted | Contested extraction; valid external storage or release required; no guaranteed control over Astral Hearts. |

**Cost accounting:** Activation/control fees consume external mana. Any separately specified released or stored mana is additional. Active handling still obeys the approved limit.


#### Rank III — Hollow Radius

Rather than draining individual enemies one at a time, a Warlock creates a region in which available mana naturally flows toward them.

The field can weaken active magical effects, interfere with equipment, and slowly deplete ambient energy.

The Warlock must continually release, redirect, or store the harvested energy externally. The field cannot absorb an unlimited quantity instantaneously, because the Warlock's Handling Capacity still restricts how quickly energy can pass through their conduit.

#### Rank IV — Fundamental Conversion

This is the first rank that allows a Warlock to extract mana from things that were not previously usable magical reservoirs.

Examples include converting the warmth of a bonfire into red mana, the movement of a waterfall into blue mana, or living vegetation into green mana.

The source loses the energy or material being converted. A fire may go cold, flowing water may slow, or vegetation may wither.

The color comes from the source's natural resonance or a compatible external catalyst. Already-existing mana cannot simply be changed from one color into another.

This is external conversion, not mana generation by the Warlock's soul.

#### Rank V — Soul Reaping

This is among the most frightening abilities a servant of Surrender can possess.

A sufficiently powerful Warlock can attempt to extract an exposed soul from its body.

A dying or spiritually weakened creature is considerably easier to affect. Removing the soul from a healthy, resisting individual requires an overwhelming magical contest and sustained contact or connection.

The Warlock cannot permanently store another soul within their own. A captured soul must eventually be released or transferred into an appropriate external vessel.

Starspawn Astral Hearts are especially resistant, and this technique cannot simply destroy their immortality or cancel Celestial Recall.

Soul Reaping is profoundly controversial within Surrender's faith, particularly when used without consent.

Specialization: Magical survival, resource acquisition, draining opponents, and forbidden spiritual manipulation.
### 4. Mana Imbuement — The Patient Hand

Mana Imbuement governs the relationship between borrowed energy and physical objects.

This discipline allows Warlocks to prepare extraordinary magical tools without learning conventional spellcasting.

| Rank | Technique               | New ability                                                                                                                                                 |
| ---- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I    | Reservoir Seal          | Turn suitable ordinary objects into temporary external mana vessels, preserving borrowed energy beyond the Warlock's one-minute hand limit.                 |
| II   | Triggered Release       | Imbue objects with mana that automatically discharges when a predetermined physical condition occurs.                                                       |
| III  | Conditional Enchantment | Establish more elaborate activation conditions based on recognizable magical signatures, spoken commands, environmental changes, or designated users.       |
| IV   | Spell Imprint           | Preserve the existing magical structure of a willing caster's spell inside a specially prepared object, allowing its original effect to activate later.     |
| V    | Soulwork                | Construct vessels capable of preserving disembodied mortal souls and create enduring, self-regulating magical mechanisms supplied by external mana sources. |

#### Approved MP costs — Mana Imbuement

| Rank / technique | Activation | Upkeep | Conditions / limitations |
|---|---|---|---|
| I — Reservoir Seal | 1 MP + MP stored | No periodic MP; seal lasts 1 hour | The mana stored remains external; 1-hour seal is the approved baseline, not a universal Rank V lifetime. |
| II — Triggered Release | 2 MP + MP stored | None beyond seal lifespan | If using a standard temporary seal, its duration still limits the trigger. |
| III — Conditional Enchantment | 3 MP + MP stored | None beyond seal lifespan | The trigger cannot impose unspecified perpetual duration. |
| IV — Spell Imprint | 6 MP + original spell’s mana | None beyond imprint lifespan | Only preserves an actual willing caster’s already-structured spell; exact imprint lifetime **UNRESOLVED**. |
| V — Soulwork | 15 MP per soul vessel; 10 MP per construct | 5 MP/day per active soul vessel; 4 MP/day per active construct | Daily costs maintain containment/control, not every construct action. Exact vessel lifespan/long-term logistics **UNRESOLVED**. |

**Cost accounting:** Activation/control fees consume external mana. Any separately specified released or stored mana is additional. Active handling still obeys the approved limit.


#### Rank IV — Spell Imprint

A Warlock cannot cast conventional spells, but can preserve an already constructed spell.

For instance, a green-mana healer could voluntarily supply a healing spell whose structure the Warlock captures inside a prepared gemstone.

The Warlock could later activate that gemstone to release the stored healing effect.

The Warlock has not learned to cast the spell independently; they have preserved its existing structure.

#### Rank V — Soulwork

At the pinnacle of Mana Imbuement, a Warlock can create soul vessels and extraordinarily sophisticated magical constructs.

A soul vessel can preserve a disembodied mortal soul without necessarily destroying its identity or consciousness. It does not automatically grant resurrection, control over that soul, or ownership of its memories.

How the brain-housed [Cognum](01_World_and_Shimmer.md#four-part-soul-anatomy) persists or functions during this form of disembodied preservation remains unresolved.

Soulwork also enables enduring magical devices capable of responding to changing circumstances and regulating their own energy supply.

These creations require compatible external power. They do not produce unlimited mana or automatically become genuinely intelligent.

Specialization: Magical equipment, traps, preparation, enchantment, and spiritual preservation.
### 5. Mana Dominion — The Authority of Nothing

Mana Dominion concerns control over existing magical structures and the connections between souls and their mana.

It is the most direct method of denying another spellcaster control over their own magic.

| Rank | Technique        | New ability                                                                                                                                                    |
| ---- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I    | Deflection       | Interfere with the direction or trajectory of an existing magical effect without fully absorbing it.                                                           |
| II   | Spell Theft      | Wrest control of an existing spell or mana-powered mechanism from its original user, redirecting its function without recreating the spell.                    |
| III  | Soul Hush        | Temporarily suppress a target soul's ability to shape or release mana, preventing conventional spellcasting while the suppression holds.                       |
| IV   | Sovereign Thread | Establish an invasive mana connection to a soul, enabling contested control of movement, magical activity, or physical restraint through the connection.       |
| V    | Null Dominion    | Establish a genuine anti-magic region in which active spellcasting, enchantments, and supernatural mana effects cannot manifest while the field is maintained. |

#### Approved MP costs — Mana Dominion

| Rank / technique | Activation | Upkeep | Conditions / limitations |
|---|---|---|---|
| I — Deflection | 1 MP + ceil(incoming spell MP ÷ 5) MP | None | Each begun 5 MP of incoming spell energy adds 1 MP; no automatic success. |
| II — Spell Theft | 4 MP | 1 MP/round | Must seize existing magic through a contest; does not grant the spell as learned knowledge. |
| III — Soul Hush | 6 MP | 2 MP/round | Temporary contested suppression without draining the target’s underlying mana. |
| IV — Sovereign Thread | 8 MP | 3 MP/round | Hostile attachment contested; does not erase free will or permanently dominate a soul. |
| V — Null Dominion | 15 MP | 6 MP/round | Cost for a comparatively small localized field; larger field requires more external energy, **no numerical area formula approved**. Sustain from outside the suppressed zone. |

**Cost accounting:** Activation/control fees consume external mana. Any separately specified released or stored mana is additional. Active handling still obeys the approved limit.


#### Rank III — Soul Hush

This technique suppresses magical activity without damaging the target's soul.

A successfully suppressed sorcerer may retain their entire mana pool yet become temporarily unable to shape spells.

The target can resist through Intelligence, established magical defenses, or by disrupting the connection.

The effect does not permanently remove racial magical affinities or erase learned abilities.

#### Rank IV — Sovereign Thread

The Warlock attaches a mana link to another creature's soul.

A voluntary link can support coordination, shared magical control, or physical assistance.

An unwilling link is much more difficult to establish and maintain. If successful, the Warlock can interfere with movement, forcibly guide limbs, restrain the target, or manipulate their ability to direct mana.

This is not effortless, permanent mind control. The target's will remains intact, and resistance, concentration, physical strength, and the Warlock's Handling Capacity all remain relevant.

However, a sufficiently powerful Warlock could turn an opponent's own body against them.

#### Rank V — Null Dominion

The Warlock creates an area where active magic effectively ceases to exist.

Within the region:

- Conventional spellcasting fails.
- Active magical effects are suppressed.
- Magical equipment loses its supernatural functions.
- External mana manifestations dissipate or are diverted at the boundary.
- Existing spells cannot normally cross the field intact.

The effect does not erase souls, destroy Astral Hearts, or permanently eliminate the underlying mana of Mystaria.

Because the field also suppresses the Warlock's own magic within it, the technique ordinarily needs to be sustained through a connection or energy source outside the suppressed region.

Larger and stronger fields require progressively greater external energy and sustained control.

Specialization: Countermagic, coercive bindings, magical dueling, and anti-magic warfare.

## IV. Specialization and Balance

The defining limitation of Grandmaster Manabending

The Warlock's reach and possibilities can become enormous, but the Warlock remains a narrow conduit.

Even at Rank V:

- Intelligence determines range, precision, and ability to overcome competing magical control.
- Endurance determines immediate Handling Capacity.
- External mana supplies determine the scale and duration of extraordinary effects.
- Preparation remains essential for large, lasting magical alterations.
- Enemy resistance matters, especially for soul manipulation and hostile magical connections.
- Racial anatomy and survivability still matter. A poorly defended Moontouched Warlock can be killed before completing an extraordinary technique.

A Mana Reach Grandmaster could reshape magical geography. A Mana Power Grandmaster could create a destructive singularity. A Mana Harvest Grandmaster could extract souls. An Imbuement Grandmaster could create exceptional magical artifacts. A Dominion Grandmaster could shut down an entire magical battlefield.

None needs the other four skills to become a successful Hero. However, Warlocks who combine disciplines become considerably more versatile.

This revision also preserves a particularly interesting contradiction in Surrender's patronage: the goddess who teaches that surrender must be voluntary has given her gentlest children the potential to take almost anything—including power, freedom, and souls—from those who resist them.

## Explicitly unresolved parameters — do not invent canon

1. **Hand Capacity — RESOLVED November 4, 2026:** the user explicitly replaced the older spell-load system with direct **one-hand** capacity `max(1, floor(natural effective END / 5)) MP`. No spell-load thresholds remain to adjudicate. The approved handling and transfer limits still govern instantaneous absorption and technique throughput.
2. **Expanded effects:** No fixed numeric area/radius, duration or environmental scale was approved for Ley Carving, Mana Singularity, Hollow Radius, Soul Reaping, Soulwork or Null Dominion beyond the stated qualitative and MP constraints.
3. **Imbuement longevity:** Rank I Reservoir Seal is one hour. Exact Rank IV Spell Imprint life and Rank V permanent device/soul-vessel life and vessel depletion rules are not independently specified, despite approved daily upkeep fees for Soulwork.
4. **Source-energy timing:** Whether same-action harvest can supply activation costs and whether large activations can be paid from sources by incremental direct feed remain unresolved.
5. **Contest details:** The absorption fraction formula is approved; exact opposed-roll procedures for controlling living souls, resisting Dominion, and manipulating hostile enchantments remain unspecified.

## Supersession record

- Recovered source: `Pasted text.txt`, *Mystaria — Warlock Skills System, Revised* (originally a proposal), superseding earlier 25-rank trees by explicit user decision on November 4, 2026.
- SP: **5 SP for every Rank I–V**; proposed progressive costs are superseded.
- Basic reach: **`2 + 2 × effective INT` meters**, not the previous approximate two-meter baseline. Skill-based Reach specializes pathway, connection and ley-line functionality.
- Capacity: **direct MP per hand**, `max(1, floor(natural effective END / 5)) MP`, in **one hand**. This supersedes the earlier **1–3 spell-loads** and `ceil(END / 10)` reference-load accounting. It remains temporary external mana handling, never an entire END-sized personal MP reserve.
- Cost package: previous assistant proposal for **all 25 techniques** explicitly approved by user before the November 4 reconciliation; recorded above.
- Former skill effects and obsolete MP prices are not purchasable alternative ranks. See `10_Canon_Changelog.md` for revision status.

## November 5, 2026 — Rebasing compatibility for effective INT/END (CANON)

The new racial Hero base attributes receive +10 **before** racial modifiers. To preserve the general Manabending range and *one-hand temporary handling limit* while accepting small race-modifier differences, use:

```text
Legacy-equivalent INT = max(1, new effective INT − 10)
Legacy-equivalent END = max(1, new natural effective END − 10)
Base Manabending range = 2 + 2 × legacy-equivalent INT meters
One-hand Handling Capacity = max(1, floor(legacy-equivalent END / 5)) MP
```

These formulas **supersede the earlier unadjusted effective INT/END examples** and do **not** increase the Warlock's hand throughput simply because the displayed attributes were rebased. A Warlock at new effective INT 11 has 4 m base Manabending reach. Warlocks **still have no natural MP** and retain the existing hand duration, one-hand limitation, all 25 skill ranks, MP costs and prerequisites. Ordinary personal MP for mana-producing races is intentionally raised elsewhere; existing Warlock spell/MP costs are scheduled for a future global balance review, not changed in this migration. All derived attributes and clamped formula inputs have minimum 1.
