# Mystaria — Combat, Endurance, Injuries, Firearms and Shimmer Guard

**Status:** CANON for the author's explicit November 5, 2026 decisions and adopted baseline; numerical firearm handling/armor scaling details explicitly labeled UNRESOLVED or PROPOSAL. This dossier is the subject reference for combat. Read `00_Mystaria_Canon_Index.md` and `10_Canon_Changelog.md` first.

## 1. Damage and Endurance: quadratic comparison (CANON)

For physical and other applicable opposed attacks, compare effective attack and defense attributes using a **+10 combat-only offset**. Damage power and defensive resistance remain quadratic:

```text
Unarmed Attack Power = (effective STR + 10)^2
Natural Defense Power = (effective END + 10)^2
Impact Ratio = Attack Power / Defense Power
```

The +10 does **not** increase real Shimmer attributes, mana reserves, craft limits, skill prerequisites or costs. Endurance resists virtually all forms of hostile assault, including ordinary physical, magical and psychic attacks; special technique rules still govern their applicability. When an attack is not driven by STR (e.g. a gun), use the relevant independent attack rating. Existing racial modifiers apply to effective attributes before combat formulas.

Example: 1 effective STR gives 121 baseline power, 10 effective STR gives 400; the latter is about 3.31 times the former, not 100 times.

### Impact ratios (CANON)

| Impact ratio | Effect | Injury-state advancement |
|---|---|---:|
| 0 through **0.75**, inclusive | Superficial | 0 |
| Above **0.75** through **1.75**, inclusive | Solid | 1 |
| Above **1.75** through **3.0**, inclusive | Devastating | 2 |
| Above **3.0** | Overwhelming | 3 |

These are the **hard-system** thresholds as well as the guidance for a fast soft adjudication with little arithmetic. Anatomical plausibility, whether an attack actually connects, armor coverage, tactical positioning and technique-specific limits still matter. Equal attack and defense give ratio 1 and one meaningful injury; an ordinary evenly matched unprotected combatant is incapacitated after approximately three solid damaging strikes.

### Weapons (approved ratio changes; remaining tables under review)

For weapons scaling from STR, the working attack rating is `(effective STR + 10) × weapon multiplier` and power is the square of that rating. **Dagger: 1.0×. Gauntlets: 1.0×. Unarmed: 0.85×** (the former dagger multiplier). The previous dagger value 0.85× is superseded. The earlier **longsword 1.15× and greatsword 1.30×** are working design values, **not yet expressly confirmed as final weapon balance**. Accuracy, reach, circumstances and armor gaps are separate from raw impact. Gun damage does not scale directly with wielder STR.

## 2. Injury progression, Hero intervention and Legends (CANON)

Normal combat has three meaningful injury advancements: **Wounded** (first), **Gravely Wounded** (second), **Incapacitated** (third). They normally apply respectively **−5%, −10% total, and −15% total** to effective attributes; incapacitated characters ordinarily cannot act, so the final penalty matters only if an ability allows action. Apply injury penalties to actual effective attributes **before** adding the combat-only +10. The exact handling of distinct simultaneous bodily and psychic wounds is **UNRESOLVED**.

**Heroes and Legends** gain **two extra, low-penalty Shimmer Guard injury stages**. In the current adopted ordering this makes: Uninjured → Wounded (−5%) → Guard I (still −5%) → Guard II (still −5%) → Gravely Wounded (−10%) → Incapacitated (−15%). Each normal solid attack advances one state; overwhelming damage advances at most three, so a fully healthy Hero or Legend **cannot be incapacitated by a single attack unless the DM expressly decides otherwise**. These stages represent exceptional ability to continue despite real injuries, **not erasure of trauma**.

When a **Hero** crosses beyond the first wounded state and Shimmer Guard manifests, their eyes visibly emit the Shimmer's signature **purple light**. The Shimmer can flawlessly diagnose a Hero's personal injuries and suppress pain to let the Hero function where most mortals falter. A Hero may **turn off or conceal the visible Shimmer Guard glow**, but experiences the full corresponding pain. Turning off the glow **does not change the numerical injury penalties**; extreme pain may be adjudicated situationally, without a new fixed penalty.

**Legends** are renowned mortals or monsters whose reputation and mortal belief create their own Shimmer Guard. They gain the **two additional injury states and the visible Guard**, but **no other Hero/Shimmer bonuses**, including no guaranteed pain suppression or personal Shimmer diagnostic interface. Belief sustains this power; attack on a Legend's *legend*, including thorough humiliation or loss of renown, can temporarily or permanently disable their Shimmer Guard. **A Legend whose Guard vanishes can collapse immediately if their accumulated injuries exceed ordinary mortal capacity.** How reputation is measured, and thresholds for disabling the Guard, are **UNRESOLVED**.

### Healing, rest, and prognosis (CANON)

**Superficial injuries heal during a long rest.** Meaningful injuries may take **weeks or months** to heal naturally, and some would be permanent without magical intervention. Because magical healing is **standard medical practice** in Mystaria, untreated permanent damage is comparatively rare where appropriate care is available. A long rest does **not** automatically heal meaningful injuries.

**Heal burn** is strain inflicted **on the recipient** by healing magic, cumulative with ordinary Soul Strain. Approved target percentages: **superficial healing 5%**; **first ordinary injury state 20%**; **second injury (first extra Guard stage) 10%**; the further Guard-stage progression adds **5 percentage points per further Guard injury** (third injury / second extra stage: **15%**). Ordinary penalty-causing injury-state healing is approximately **20% per state**. Burn is charged for injuries actually healed, not for unhealed stages. Up to **two short rests per day** can remove some heal burn; a **long rest removes all heal burn**. Exact short-rest recovery percentages, strain caps and the precise mana-reserve conversion of percent heal burn are **UNRESOLVED**. Neither the Shimmer Guard buffer nor ordinary rest provides free magical tissue regeneration.

## 3. Armor (working combat formula, scaling NOT finalized)

Retain the **working** additive-in-power armor formula:

```text
Effective Defense Power = (effective END after injuries + 10)^2 + (Armor Rating after penetration)^2
Impact Ratio = Attack Power / Effective Defense Power
```

Mundane armor usually applies only where physically present; mundane armor need not resist psychic or magical assaults, while specific enchantments or materials may. **Numerical armor ratings, penetration percentages, how armor quality and Centaur crafting scale, and final integration with equipment-tier bonuses remain an UNFINISHED PROPOSAL.** Do not canonize past sample armor numbers as equipment quality rules. Preserve approved equipment cost, Soul Strain and Centaur equipment affinity until expressly revised.

## 4. Firearms, recoil and materials (CANON principles; thresholds unresolved)

Firearm damage is set primarily by **weapon construction, propellant and ammunition**, **not** directly by the shooter's Strength. Each gun should have an intrinsic **Damage Rating** and a **Strength Requirement**, their relationship balancing the weapon's power against handling demands. Being below its STR requirement makes aiming, control and recoil increasingly difficult; an extreme deficit prevents free use. Far-above-required STR can reduce felt recoil nearly to nothing. **Exact strength ratios/cutoffs are UNRESOLVED**; numbers suggested during brainstorming are proposals only.

Extremely heavy guns may be fired using a **brace, ground rest or mount**, but can be unsuitable for a mobile melee brawl. Magic such as Jester ribbons may offset the **weight/movement requirement** without automatically cancelling the gun's **recoil**. If extreme recoil actually causes injury, it is **severe and advances the wielder by one injury state** (not merely superficial harm). When the recoil injury occurs, and its threshold, remain unresolved. Specialized magic that truly absorbs impact must have an applicable, established effect.

**Adamantite** is the authoritative spelling for the exceptional metal; the alternate spelling “Adamantine” is not adopted. **Crownsalt** is the established powerful propellant; **gunpowder** is also an acceptable ordinary term for Crownsalt. Even **Trufula** guns can have enormous recoil by real-world standards; maintain established special noncombustive-propellant compatibility for Trufula frames rather than implying ordinary fire is safe. Adamantite and reinforced designs can be extraordinarily heavy; powerful propellant exists to challenge Adamantite armor, dragon scales and other formidable defenses.

## 5. Combined attacks (quadratic principle; implementation still provisional)

In a genuinely synchronized attack, weaker attackers can combine offensive **power**, potentially overwhelming a superior opponent (including Naga Psychics joining forces against a Serpentari). A prior suggested rule was `A_group = sqrt(sum(A_i^2))`, with a coordination factor for imperfect synchronization; these **exact aggregation and coordination numbers remain PROPOSAL** until approved. Separate, unsynchronized attacks are not automatically one combined strike. Splitting power among targets remains under design.

## 6. Open balance decisions

- Confirm final armor ratings and penetration, equipment-quality and **Centaur crafting** interactions.
- Set intrinsic firearm damage ratings, required STR, recoil thresholds, braced use and ammunition interactions.
- Specify short-rest heal-burn removal, percentage-to-Soul-Strain interaction and overall capacity.
- Resolve mixed physical/psychic injury tracking, precise wound-treatment time, and wound-specific disabling effects.
- Establish any exact combined-attack rules and the mechanics of weakening a Legend's public renown.
- Longsword/greatsword multipliers and any former revolver sample rating remain provisional, not final canon.

## November 5, 2026 — Power, Resistance, Defense and Evasion terminology (CANON)

- **Power** is the general numerical strength/output of an attack, spell, weapon or other scaling effect. It does **not** always mean damage: an effect can use Power for damage, a spell's strength, overcoming protection or another function explicitly defined by that ability.
- **Resistance** is the character's **effective END (Endurance)** as a baseline statistic, with the usual racial/equipment/injury adjustments that actually affect effective END. The combat-only +10 is **not** included in the Resistance statistic. Thus **Natural Defense Power = (Resistance + 10)²**.
- **Specific Resistance** is a convenient description for situational adjustments against a particular effect or damage type (for example, fire resistance, psychic resistance, piercing resistance). Its actual modifier and scope must come from an established spell, material, hazard or ability; **this terminology does not authorize blanket new resistances, stacking rules or bonus values**. Unless a rule explicitly changes effective END generally, a specific resistance modifier applies only to its named threat.
- **Defense** means the result of physically, magically or mentally withstanding an effect. Armor, wards and barriers may contribute separately to the overall defensive calculation as their established rules allow; **Defense has no role in evasion**.
- **Evasion** is avoiding an attack or exposure entirely, resolved separately using relevant speed/dexterity/positioning or established skills. A successful dodge is not a higher Defense score.

**Calculation vocabulary:** For an ordinary Strength-based weapon strike, `Power = ((effective STR + 10) × weapon modifier)^2`. For natural protection, `Defense Power = (Resistance + 10)^2`. `Impact Ratio = Power / Defense Power` when no other applicable defenses or modifiers intervene. Preserve the existing working armor model `Defense Power = (Resistance + 10)^2 + (effective armor rating)^2` for covered physical hits; final armor ratings and penetration remain **UNRESOLVED**. Firearm Power comes from the weapon/ammunition rather than the shooter's Strength. Spell Power depends on that spell's established scaling parameters, not an automatic conversion from STR.

**DM modifier order (organizational guidance, not a new stacking rule):** (1) establish whether the effect connects or is evaded; (2) identify the effect and its Power source (including weapon, implement, ammunition and known modifiers); (3) start with effective END as baseline Resistance and apply only relevant type-specific adjustments; (4) evaluate actual armor coverage, barrier effects, and vulnerabilities as separately applicable; (5) use the Impact Ratio thresholds only when the effect inflicts an injury-type attack. Record modifiers by their source and type instead of folding unrelated effects into one arbitrary END change. **The exact order for applying oil vulnerability, fire-resistant armor, barrier absorption, resistance stacking and spell-specific bonuses remains UNRESOLVED** until the underlying rules are set.

**Illustrative scenario, not a ruling on numerical effects:** A Sorcerer using an implement casts **Ignis** at a Thornguard in plate armor, coated in lantern oil and protected by a barrier. First decide whether Ignis connects. Determine Ignis's Power under its actual spell rules and the implement's approved effect, then apply any proven fire-specific Resistance, armor protection that really works against the spell, the actual barrier mechanism, and any oil-induced vulnerability. Do not assume that plate stops fire, that lantern oil changes effective END, or that all barriers merely increase END. Specific numerical modifiers, spell damage scaling and their precedence are **not yet canonical**.

This terminology clarification supersedes uses of “attack rating,” “effective Endurance” and “Defense” as interchangeable names for Power, Resistance and evasion in older summaries. It does **not** change the quadratic law, the +10 offset, the injury thresholds, or existing Sorcery skill/MP/SP costs.


## November 5, 2026 — Speed and Evasion: approved design direction

**Status:** **CANON for the design philosophy, difficulty ladder, pressure states, no-extra-attacks restriction, and Shimmer prediction feature.** Specific procedural modifiers, numerical armor SPD penalties, and a full hit-resolution algorithm are **UNRESOLVED**. Do not treat hypothetical frequencies as canon.

### Core principles

- **STR, DEX, INT** are the primary scaling attributes for thematic skill output. General-purpose, Skill-Point-purchased STR/DEX skills are planned for future development; **no names, SP prices, rank effects, or purchases are established here**. Specific magic can also scale with END under its existing rules.
- **END / Resistance** is the universal protection against landed harm. **SPD / Speed** helps a combatant evade and land attacks on fast opponents, with emphasis on **defensive** use; DEX remains distinct for accuracy and technique. Speed never independently grants extra attacks within an action. Special skills or magic that might alter action count are speculative, not granted.
- Evasion is separate from Defense, entirely negating a successfully dodged attack. **Glancing blows** are permitted as an intermediate result when an attack cannot wholly miss or wholly connect; they reduce the resulting **injury states by approximately half, NOT Power**. Exact rounding for odd injury counts remains **UNRESOLVED**. Glances should be less common than complete dodges. Targeted, high-quality attacks particularly invite evasion; armor/Resistance are especially dependable against repeated weaker strikes.
- Different combat circumstances are the principal counter to superior Speed: **area attacks, multiple coordinated enemies, constraints on escape paths, terrain and setup**; even extraordinary Speed does not guarantee absolute immunity in all situations. Extreme disparity may make a direct ordinary attack impossible in the *current circumstances* until the attacker changes those circumstances. Armor **directly penalizes SPD**, but numerical values and equipment-quality scaling remain an **UNFINISHED PROPOSAL**, coordinated with Centaur crafting.
- The design benchmark is that, against **one ordinary melee opponent in open conditions**, equal extra-stat investment in SPD versus END should yield **roughly comparable overall injury avoidance/mitigation**. END should be more consistent across multiple smaller attacks and area exposure; SPD should be strongest at evading individual dangerous hits. This is a balance goal, not an approved probability system.

### Approved baseline Evasion Ratio and difficulty ladder

The ratio compares defender and attacker **effective SPD**, using the combat-only offset; actual ability to dodge additionally depends on situation and the attack's nature.

```text
Evasion Ratio = (Defender effective SPD + 10) / (Attacker effective SPD + 10)
```

| Evasion Ratio | Difficulty to land a direct attack | Interpretation |
|---|---|---|
| Below **0.50** | **Certain** | A straightforward strike should ordinarily connect unless circumstances alter it |
| **0.50–0.79** | **Easy** | Defender needs favorable circumstances to evade |
| **0.80–1.24** | **Average** | Neither side has a major Speed advantage |
| **1.25–1.49** | **Hard** | Defender usually evades if aware and free to move |
| **1.50–2.99** | **Very Hard** | A direct hit normally needs a created opening |
| **3.00 and higher** | **Impossible** | Ordinary direct attacks cannot connect under unchanged circumstances |

The displayed decimal bands are human-friendly approximations; **exact treatment of gaps between hundredths is unresolved**. For human adjudication, compare to the shown boundaries and avoid needless precision. Difficulty is a default **before contextual adjustments**. **Certain does not bypass armor/Resistance** and **Impossible is not absolute invulnerability**.

### Four pressure states: open, pressured, trapped, extreme pressure

- **Open:** clear escape routes; the defender can benefit from their normal Speed advantage.
- **Pressured:** crowding, distraction, an ally flanking, partial confinement, or converging threats; evasion is harder and glancing blows become plausible.
- **Trapped:** meaningful escape routes are denied or attack coverage prevents a clean ordinary dodge; armor, barriers, Resistance and applicable magic become crucial.
- **Extreme Pressure:** unusually intense saturation such as a coordinated army of archers and swordsmen, overwhelming numbers and multiple overlapping attacks. The target is severely constrained **but never automatically helpless**: creative magical mobility, cover, disruptions, defensive techniques and favorable opportunities may still matter. Do not assume this state automatically makes every attack hit or authorizes unlimited group power.

Pressure changes the **circumstances** of an attack, not END/Resistance itself. The precise number of difficulty steps or die-less success procedures for each state is **UNRESOLVED**. Flanking by one ally and being targeted by a full formation should not be treated as equally oppressive.

### Shimmer prediction — approved feature, conditional DM intervention

For Heroes and Legends confronting overwhelming Speed discrepancies, **Shimmer Guard can display predicted evasion paths** (for Heroes, Shimmer-style purple path projections; Legends' manifestation follows their own Guard). This is an in-world sensory/anticipatory effect and a DM-facing mechanical aid when Speed disparities make ordinary attacks difficult to adjudicate or play. It can convey plausible movement/escape paths or openings and support adjudication of an otherwise impossible direct attack; it **does not** automatically boost SPD, grant extra actions, guarantee a hit, disclose certain future events, or override an opponent's abilities. Its numeric activation threshold, predictive certainty, and any explicit accuracy adjustment are **UNRESOLVED**. It should be used sparingly, when needed to preserve satisfying tactical counterplay, not treated as omniscience or ordinary always-on aim assistance.

### Rejected for routine play: percentage evasion model

The author explicitly **dislikes the prior Proposal Three / Bounded Evasion Curve** as a player-facing or GM-facing operational mechanic. Percent dodge frequencies may be used, if ever, **only as hidden, rare, highly technical playtesting calibration**, not as a published rule, random dodge check, mandated outcome frequency, or substitute for the approved difficulty ladder and tactical pressure. Do not canonize the earlier suggested percentages.

## November 5, 2026 — Global attribute rebase supersedes combat-only +10 (CANON)

**Priority note:** This later author-approved rule supersedes the older passages above that add +10 only while calculating combat. **Every approved Hero racial base attribute increases +10 before racial percentage modifiers**. After modifiers, all attributes are clamped to **minimum 1**, including monsters. Non-Hero monsters may have attributes **1–9**. The stronger influence of racial percentage modifiers is intentional.

Use **new effective STR directly** to derive weapon Power, **new effective END (Resistance) directly** to derive Defense Power, and **new effective SPD directly** in Speed comparisons:

```text
Strength-weapon Power = (new effective STR × weapon modifier)^2
Natural Defense Power = (new effective END / Resistance)^2
Working armored Defense Power = Resistance^2 + (effective Armor Rating)^2
Impact Ratio = Power / applicable Defense Power
Evasion Ratio = Defender new effective SPD / Attacker new effective SPD
```

The former combat-only +10 must **not** be added a second time. The six approved Speed difficulty categories, pressure states, impact thresholds, glancing rules, Shimmer Guard/injury progression, and unresolved armor scaling remain unchanged. The revised scale aims for average human Strength **15** and stronger-than-most-human Strength around **25**. Practical one-time waist-height lifting benchmark: **`100 × (effective STR / 15)^2` pounds**, rounded for table use and subject to anatomy/handling. Numerical firearm STR requirements, armor SPD penalties and primary-skill scaling remain pending.

## November 5, 2026 — Attribute identity, predictive Dexterity and high-stat limits (CANON)

**DEX and SPD roles:** Speed (SPD) governs physical velocity, immediate reflexes, reaction time, rapid target tracking and evasion. **Speed does not itself grant movement prediction, ballistic forecasting, perfect aim or additional attacks.** Dexterity (DEX) governs precise execution and anticipation of physical movements and patterns; it also covers practical fine-motor abilities such as stealth, manual craft, lockpicking and careful physical observation. Intelligence (INT) governs abstract reasoning, learning, memory and evidence-based forecasts. DEX prediction is not a substitute for INT's broader analytical reasoning.

**Combat anticipation, roleplay-first:** An attacker or defender with **effective DEX at least 75% of the target's effective SPD** can reliably exploit an **accurate, player-stated prediction of that target's movement or attack** to improve the attacker's tactical circumstances or their own escape conditions. This is not a guaranteed hit, dodge, or free extra attack. The DM adjudicates the consequence through the existing four pressure situations (Open, Pressured, Trapped, Extreme Pressure) and existing six difficulty categories. A well-supported prediction in combination with other threats may escalate pressure dramatically, including **Pressured to Extreme Pressure** when the physical circumstances warrant. **Wrong predictions significantly worsen the predictor's circumstances** by committing movement or aim to the wrong opening. A player can still attempt clever tactics below the 75% benchmark, but cannot assume similarly reliable timing. No new prediction-roll system, discrete "prediction skill", resource, or numerical pressure-step formula is established. Examples: aim for a target's expected dodge away from an ally's explosion; prepare for a Drakyn repeating a previously observed fireball pattern.

**Exceptional INT is not supernatural knowledge:** At around **INT 100**, photographic memory is the desired benchmark. At **INT 150**, machine-like memory and reliably extraordinary, seemingly prophetic calculations are appropriate **only with sufficient relevant data**, with less complicated predictions requiring less information. INT itself does not grant visions or unknown facts. A genuine psychic/precognitive Naga may acquire information supernaturally without leaving a cave; a mundane high-INT Hero predicting large-scale world events needs relevant observations or an intelligence network. Exact capacities and benchmark tiers beyond these commitments are to be illustrated in a separate unapproved attribute-chart draft.

**Exceptional END and environmental resilience:** At approximately **END 150**, brief lava exposure is survivable if the creature **escapes immediately**, not comfortably swimmable. At approximately **END 300**, ordinary lava exposure is closer to sunburn-level injury; extreme natural hazards are mostly survivable, with events such as **volcanic explosions** still potentially dangerous. Survival time without oxygen, food or water scales **approximately linearly**, rather than quadratically, with END; at **END 300**, unsupported oxygen deprivation endurance is **about 10×** the ordinary human reference, not 20× simply because the stat is 20× higher. Exact breath-holding formula, food/water multipliers, terminal-velocity fall thresholds and environmental damage ratings remain **PROPOSAL/UNRESOLVED**, and physical durability does not remove physiological needs.

**Exceptional precision:** The previous suggestion to grant unseen-target aiming, ricochets, and long-distance ballistic precision through SPD is superseded. These are **DEX-driven precision feats**, with SPD relevant for reacting to or physically tracking fast targets. The requested indicative benchmarks are DEX **100** for accurately targeting unseen positions with information, **150** for complex multiple ricochets, and **300** for suitably supported extreme long-range aiming. These remain illustrative **chart proposals**, not automatic skill unlocks, guaranteed hits, magical senses or free equipment range.

The author has not yet approved numerical sprint speeds, oxygen-duration formula, detailed DEX stat chart, or final benchmarks for ordinary stealth/perception; keep such examples **PROPOSED** until review.


## November 5, 2026 — Dexterity, contingencies, stealth, and speed-of-motion clarifications (LATEST CANON)

### Dexterity: precise physical anticipation and stealth

**DEX** combines the previously considered *Anticipating Hand* and *Perceptive Hand* concepts: observing physical cues, predicting immediate movement from evidence, choosing timing, and executing precise actions. It **improves stealth and the ability to detect or foil stealth** through traditional means: moving quietly, exploiting concealment, reading openings, noticing small motions and detecting tells. **High DEX is never literal invisibility**; an uncovered character standing plainly in the open is ordinarily visible. Speed remains rapid reaction and movement, not foresight; Intelligence remains general analysis and data-dependent prediction.

**Player-stated predictions and contingent plans:** When a character has **DEX ≥ 75% of an opponent's effective SPD**, a reasonably grounded, accurate prediction can reliably improve tactical circumstances as previously approved; an incorrect prediction normally significantly worsens the predictor's situation. **New exception: if DEX ≥ 200% of that target's effective SPD, an incorrect prediction incurs NO penalty attributable specifically to the wrong prediction**. Such a character is sufficiently precise and anticipatory to build effective contingencies into their actions. This is **not** a guarantee of success, an extra action, a free evasion, elimination of unrelated danger, or a new percentage-based hit calculation. The DM still considers the actual battlefield, attack/evasion ratio, four pressure situations, and other source-specific consequences.

**Mundane expertise is NOT automatically unlocked by DEX:** Specializations such as lockpicking, detailed artisan trades and other practiced mundane techniques may eventually form a separate **PROFICIENCIES** system, potentially purchasable with SP and gated by attribute prerequisites. **PROFICIENCIES IS A PROPOSAL, NOT CANON:** names, prerequisites, cost structure, ranks, applicability and interaction with ordinary Shimmer progression are not developed or approved. High DEX supports precision but does not automatically grant a profession's training. Revisit Proficiencies **when the author raises general skill systems from other tabletop RPGs**, **not** when they are discussing Mystaria's already established magical Skills or Crafts.

### Ordinary training versus Hero advancement

**Ordinary mortals can raise actual attributes through appropriate training.** This is an in-world avenue for improving strength, stamina and coordination; no numerical training schedule has been approved. **Heroes cannot gain attribute points merely by training** because their Shimmer governs their attribute progression through **experience/leveling**, preserving the existing +2 allocatable base points per level and +1 to all five base attributes every fifth level. Practice may still improve player tactics or allow mastery of appropriately purchased/learned techniques, without extra Hero attribute points.

**END 25, not 15, is the baseline for marathon-capable endurance** under appropriate conditions. At END 15 a creature has ordinary adult stamina and does not automatically possess marathon capacity. The longer-endurance superhuman/lava and approximately linear survival-needs guidelines remain unchanged. The exact marathon duration, athletic conditioning modifiers and all endurance-distance tables remain unresolved.

### High-speed impact and movement modes

**Approved design principle:** Movement at extraordinary speed can modestly increase the **Power of a suitable movement-assisted attack**, subject to **relative closing speed and sufficient run-up**, not automatically multiply every weapon or spell or grant extra attacks. A charging combatant must have **room and time to accelerate**; an exceptionally fast Hero cannot immediately apply full dash momentum from rest. If the opponent accelerates in the same direction to **cancel the relative closing-speed difference**, the speed-derived attack-Power bonus is **fully neutralized**. Opposing movement, collision geometry, attack mechanics and the user's actual dash trajectory matter.

**Three movement regimes:** **Dash** is the extreme maximum short-burst speed. **Sprint** is **one progression tier below** the character's dash speed; a **sustainable jog** is **two progression tiers below**. The currently discussed illustrative tier sequence (SPD 10/15/25/35/50/75/100/150/300 with draft dash speeds 10/15/22/30/45/75/110/200/500 mph) is **NOT YET APPROVED AS A NUMERIC SPEED TABLE**, and the exact duration/acceleration/terrain requirements are unresolved. This tier-language applies to the future speed chart, rather than treating dash as sustainable travel pace.

**Provisional, not yet finalized numerical calibration:** Approximately **+25% attack Power** at a roughly **100 mph effective charge** and **+50% attack Power** at a roughly **500 mph effective charge** were suggested as suitably *modest* boosts. Exact rounding, intermediate interpolation, minimum run-up, and whether a specific attack qualifies remain **UNRESOLVED/PROPOSED**, not binding multipliers. If approved later, bonuses should apply to final attack **Power**, not separately to squared STR, avoiding an unintended quadratic multiplier, and should not increase number of attacks. Special effects or existing skills could differ only under their own approved rules.

The existing six-category evasion ladder, the four pressure states and armor's pending SPD penalty continue unchanged. The bounded percentage-dodge model remains disfavored for ordinary gameplay.


## November 5, 2026 — Passive elemental impact selection (LATEST)

**Approved procedural choice:** passive elemental rune attacks use **Conditional Contact Effect (model B)** rather than independent full Power-packet or split-Power models. Resolve the existing attack's evasion and physical injury normally; when the weapon truly contacts the target or a relevant armor surface, a passive rune can have a separately resisted **limited elemental rider**, including when the physical injury result was superficial. An entirely evaded attack has **no rider**. Barriers/insulation/element-specific defenses protect as actually applicable. Contact consequences must not assume armor coverage or automatically bypass all END.

**Existing restrictions remain:** no new active action, no extra attack; rank-V elemental transformation forfeits the former material bonus; strong special Resistance can suppress/passively negate element effects. Exact numerical contact test, thresholds, and particular effect durations are **NOT YET APPROVED**, described only as proposals in `24_Modular_Equipment_Design_Options_DRAFT.md`. Toxic rune hex exposure does **not** have an approved dose or wound-time formula; honor `20_Nymbrin_Wetcraft_and_Hexen_Canon.md`.


## November 5, 2026 — Energy effects, Elemental Magnitude and rank-V form (LATEST)

**APPROVED CONCEPT:** Rename the provisional passive-rune measure **Contact Pressure** to **Elemental Magnitude**. The conditional-contact method remains approved for passive weapons; it becomes the **baseline resolution philosophy for energy-based attacks and magic, notably Sorcery**, while spells retain their own Power source, MP, affinity, Incantations, alterations and prerequisites. Passive weapon contact cannot be transferred unchanged to remote spell delivery, and non-energy magic is not necessarily an energy attack. Energy-focused combat/spell entries should ultimately list relevant Elemental Magnitude, element, potential Elemental Status and specific Resistance interactions as first-class properties. **Exact general spell formula, scaling, rank-I–V passive coefficients and status thresholds remain UNAPPROVED.**

**Elemental Statuses:** Three distinguishable severity ranks per elemental condition are being designed **separately from five rune quality ranks**. Rank III of a passive rune should be able to cause a resisted status in applicable situations. A status may reduce **type-specific Elemental Resistance** to its own element to reward repeat contact; this is not equivalent to reducing general END or every spell defense. Exact stack caps, reset timing, injury frequency, freeze durations, stun effects, launch distance and hex stat penalties remain **PROPOSALS**, not operative canon. Soaked or wet targets should be more susceptible to **electricity's contact transmission**, where an actual path exists; numeric factor unresolved.

**Rank-V elemental weapon detail APPROVED:** A wholly elemental weapon **retains ordinary appropriate weapon Power and may add its limited passive rider** under the existing Conditional Contact concept, **but forfeits the previous material's special bonus**. Material-bound mass/handling details in a fully elemental form are still unresolved; this does not automatically make a heavy weapon weightless or ignore its equipment requirements. A full dodge still avoids an applicable connected rider, and normal injury thresholds and Hero/Legend Guard protections remain.

**Energy near-immunity glossary:** No creature is absolutely invulnerable to a kind of energy simply because older shorthand calls it immune. Treat ordinary energy-type immunities as **near-immunity** that can be overwhelmed by sufficient intensity or specific vulnerabilities; no universal bypass number has been approved. This clarifies native Drakyn resistances without granting an automatic way to defeat them.


## November 5, 2026 — Refined elemental status targets and commander action-economy direction

**Author-stated Shocked status design, pending complete status integration:** **Shocked I** interrupts and cancels an action but permits normal movement on the creature's next turn. **Shocked II** prevents the victim taking an action for its defined stun window but imposes no other evasion or movement penalty by itself. **Shocked III** additionally causes dropped held items and helpless convulsions; treat the target as **Trapped** for evasion for the duration, not automatically as Extreme Pressure. **Repeated shocks must not chain or extend a current stun**. Exact initiative timing, post-stun immunity/recovery, full duration and status resistance thresholds remain **UNRESOLVED**.

**Water/Air displacement design targets, proposal for magnitude/anchoring rules:** Water Status II **5 meters**, III **15 meters**, with knockdown emphasis; Wind/Air Status II **10 meters**, III **30 meters**, emphasizing longer launch and secondary terrain hazards, generally lower direct damage. Earlier feet-based values are superseded as a design proposal. Status I Water prone and Air short displacement remain proposals. Mass, restraint, END, anchoring and physical line of travel must matter; distances are **not automatically guaranteed**.

**Hex revised design target (not finalized damage mechanics):** specialize in hunting mana-users and disrupting magical systems. Hex may drain MP from creatures and accessible Leywells, give limited extra efficacy versus magical shields, and disrupt/stun enchanted machines instead of applying the same biology-dependent effects. Once accessible MP is exhausted, sufficiently potent Hex may cause especially serious immediate injuries (up to a **proposed two injury-state advancement**) if the established impact/Guard rules allow it. **A target having 0 MP is not by itself sufficient to cause two injury states; require actual adequate Elemental Magnitude and applicable Resistance failure.** Hex numerical magnitude, storage targeting, side effects, shield bonuses and status ranks remain UNAPPROVED.

**Commander action economy philosophy:** A controller issuing a coordinated attack to several weaker constructs ordinarily spends one meaningful command action; the constructs act as **one tactical group**, not separate independent high-damage attacker turns. A suppressing-fire order is a proposed pressure-building alternative, with a conditional attack against a Trapped enemy to be budgeted, not free unlimited shots. Keep the existing six-tier evasion ladder, four pressure categories, damage-injury stages and no-extra-attacks design intact. Specific squad combat rules require author clarification.

## November 6, 2026 — Construct squad pressure and casualty direction (LATEST)

**Author-approved principle:** Evasion/tactical pressure is **not automatic merely because a construct acts, surrounds a creature or issues a harassment order**. Compare the attacking group's relevant stats and coordinated physical capacity against the target's relevant defensive stats. More squad members can create a bounded multiplier, but a hard disparity cutoff must prevent a horde of trivial machines from automatically pressuring a legendary fast or unthreatened Hero. Numerical multiplier and cutoff are **UNAPPROVED**; integrate with the existing six-tier evasion ladder and four pressure circumstances rather than inventing an independent evasion tier.

**Approved casualty abstraction:** Ordinary small/medium constructs fall as **a count of units disabled/felled per attack** when the attack's Power is sufficient against their material-based defenses, limited by the attack's real coverage. A narrow single-target rifle shot usually affects one; wide sword swings can fell several in one action if arc, reach and strength permit. Narrated repeated cuts by a fast dagger-user may represent **one existing attack action**, not grant extra attack actions. No unlimited spillover of damage outside the covered area. The largest Siege Engines retain individual injury states. Quantitative thresholds and coverage sizes unresolved.

**Windling sonic attack:** A built-in acoustic music box can produce painful, usually nonlethal hearing damage without jamming its own Cogsong command frequencies. Sustained attacks can damage other machines' acoustic Cogsong receivers over a longer period than ordinary combat-focused constructs need to inflict disabling damage. Receiver failure prevents receiving fresh orders, not automatically the destruction of the chassis or Leywell. Exact resistance, exposure and statuses remain unapproved.

## November 6, 2026 — Windling sustained sonic attack (APPROVED)

A commanded Windling swarm may use **one attack action** to establish a **targeted sonic distraction** of **one specified enemy for up to three turns**. The commanded swarm pursues this same target during that bounded order. This represents **a single sustained offensive action** rather than three separate attacks; replacing the target, restarting the three-turn pursuit or issuing another fresh offensive action needs a **new Cogsong command/commander action**. The three-turn clock is not extended by failure to reach, obstructions or target escape. Continued exposure can apply stat-qualified auditory interference, but **does not automatically produce an ordinary injury state or evasion pressure each round**.

**Very short range and defenses:** ordinary Windlings do not present a significant sonic threat once the target is separated from the swarm by around **5 meters**. Melee characters can readily counterattack against approaching machines. Escaping the sonic range, a meaningful acoustic barrier or covering/protecting the ears can avoid or reduce fresh exposure. Existing harm already incurred does not vanish merely by moving away. Pursuit depends on comparative SPD, accessibility and material capability: a legendary fast or well-insulated Hero can ignore an ineffectual swarm. Exact numeric exposure, type-specific hearing/sonic Resistance, effects of partial ear coverage, and initiative timing are **UNAPPROVED**, subject to combat-system compatibility.

One commanded multi-turn sonic attack is the explicitly approved special case to the broad rule 'each new attack requires a command', not permission for continuous standing offensive attack orders. The sonic music box is a deliberate weapon action, not free damaging background noise while the swarm screens or carries objects. Construct receiver disablement requires much more sustained effective exposure than the damage cycle of dedicated combat machines; failing receivers impede new Cogsong signals without automatically destroying chassis or Leywell.

## November 6, 2026 — Weapon form balance, dual wield and horde-group attacks

**Author-approved relative damage form ratings:** Piercing: Injury **1/5**, Armor Bypass **5/5**, narrowest area; Slashing: Injury **5/5**, Armor Bypass **1/5**, widest coverage; Blunt: Injury **3/5**, Armor Bypass **3/5**, middle coverage. These are design ranks, **not** numeric Power or bypass percent. Blunt should have a **reduced effective injury ratio, not a hard one-state cap**, so an overwhelmingly powerful blunt attack can inflict multiple injury states consistent with Shimmer Guard. Do not impose a second injury cap on top of ratio reduction. Distinguish piercing penetration from blunt transmission of trauma through plate; armor only protects covered locations as applicable.

**Approved form/dual-wield direction:** weapons have Light, Medium, Heavy handling forms, primary and optionally explicit alternative piercing/slashing/blunt attack forms, and independent Reach and Coverage. Adequate STR can allow normally two-handed weapons in one or both hands; working STR handling thresholds 150% one-hand heavy and 200% dual-heavy subject to material/geometric review, plus relevant DEX/control. The offhand may be assigned **Attack** (making an actual threat harder to evade) or **Defense** (improving the defender's evasion), not both at once. Exact modifier remains PROPOSAL; no automatic extra combat actions or unconditional tier shifts. Shield occupying a hand is a future armor owner concern, boosting appropriate Defense via block/coverage rather than universal evasion.

**Horde/army generalization:** Wide melee attacks and suitably capable precision combinations can threaten **multiple opponents in one existing attack action** when there is appropriate reach, arc, technique, relative SPD/DEX and actually sufficient Power/Resistance outcomes per target. Apply to monster hordes, gangs, armies and constructs, not merely commanded machines. Revisit monster group or squad mechanics and their interaction with the existing four pressure states and Hero/Legend Guard; no automatic meaningful threat from numerous individually ineffective low-stat enemies. Exact coverage per weapon, count felled, distribution of power, individual survivor injury state and swarm pressure aggregation remain unresolved.

**Combat math precedence:** the latest approved racial base +10 rebase prevents adding the earlier combat-only +10 again. Retain current quadratic comparison and established injury thresholds, do not inadvertently grant twice the attribute offset. Exact weapon shape Power factors, per-form armor bypass percentages, shield Defense and dual-wield evasion adjustments remain PROPOSED pending author testing.

## November 6, 2026 — Melee reach control, grapples and shield combat roles

**APPROVED:** Melee weapons have independent handling class, **Short/Medium/Long Reach**, and attack-specific Coverage. In open comparable engagements, a well-controlled Long weapon can **deny ordinary Short-reach attacks until the short fighter closes**, while a Medium-reach opponent may close with increased difficulty rather than being universally forbidden. Short weapons work wherever there is enough room to move, including effective grapple range. Once a Short fighter has closed **inside** the Long weapon's usable distance and **grappled**, ordinary Long-weapon attacks against that fighter are impossible until distance/control is restored or an applicable special technique is used. The fighter may still withdraw, use an alternate short weapon or undertake allowed unarmed escape; these are not free extra actions.

**Conditional defense:** Reach advantages require real control of space. Genuine existing-system **tactical pressure against the reach-controlling wielder** defeats that defense; mere presence of an opponent or an ineffective action does not create pressure. Stat comparisons, speed, movement, available terrain and geometry still matter. A Short-vs-Medium reach disparity may give a smaller nonautomatic advantage, but exact evasion/category and movement rules remain unapproved. Avoid absolute reach-lock against overwhelmingly stronger/faster enemies and do not treat range bands as fixed meter measurements before the author approves distances.

**Future NONCANON Proficiency candidate:** *Choking Up*, adapting long weapon grip to threaten nearer opponents; no purchased SP skill or numeric benefits established.

**Shield roles APPROVED IN PRINCIPLE:** (1) passive coverage of actually protected locations, (2) active directional block/parry contributing to Defense, (3) defensive maneuver potentially helping Evasion where real deflection/path alteration exists. Held shields occupy a hand. Detailed numerical stacking/block/dodge, strapped designs and bash attacks are future armor review, not automatic new bonuses. Preserve Evasion separately from Defense and no extra dual-wield attacks.

**FORM REFERENCE CHANGE:** The old mandatory individual **Dagger = 1.00×** was explicitly called a placeholder and is superseded by **Light-class baseline attack rating 1.00×**. This is not an across-the-board flat 1.00× for all unique light shapes; final individual forms and Medium/Heavy multipliers are under design. Keep approved Unarmed 0.85 and Gauntlets 1.00 until a later ruling. Preserve the approved racial +10 base rebase and no second combat-only +10.

**Universal mass-combat docket:** Distinguish attack coverage (point/narrow/arc/line), reaches and valid multi-target impact for **all** hordes, gangs, armies and construct formations; quantitative multi-target casualties and organized horde stats are unresolved.
