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
