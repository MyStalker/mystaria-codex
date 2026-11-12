## November 11, 2026 — STR100–400 legendary bow ladder: 320-scenario quantitative test (NONCANON)

**STATUS: TEST RESULTS AND NEW NUMERIC PROPOSALS ONLY.** The author's explicit approval covers **testing** the previously approved high-strength archery progression and the **design requirement that some bow can exploit effective STR400**, not blanket approval of the new bow names, caps, draw minima, full-draw Powers, new arrow construction, handling, costs or ranges. This reproducible note is for future review; it does **not** supersede the approved high-draw bow's **14,500 full-draw Power** or existing mechanical rules.

### Test inputs

Use the **approved** physical model for a legally drawn and successfully landed conventional Piercing arrow: each item has separate full-draw rated Power `Pfull` and engineered cap `C`, with `Pshot = Pfull × (min(effective STR,C)/C)^2`. Use 50% ordinary Piercing AR bypass and `Defense Power = effective END² + (covered AR × 0.5)²` under the *later approved global effective-stat rebase*, not superseded `(END+10)^2` examples. Impact ratio `Pshot/Defense` gives Superficial (≤0.75, 0 injury stages), Solid (>0.75 to 1.75, 1), Devastating (>1.75 to 3.0, 2), Overwhelming (>3.0, 3). Test **no extra magical force, bonus material multiplier, Power falloff, specialized arrow penetration, Aim/cover hit probability or quality increment**.

**Recommended BALANCED numeric candidates (NOT CANON):**

| Distinct engineered bow | Proposed STR draw cap | Rated full-draw shot Power |
|---|---:|---:|
| Existing advanced high-draw bow | 100 (**cap remains proposed**) | **14,500 (previously approved)** |
| Titan bow | 200 | **45,000 proposed** |
| Reinforced colossal composite bow | 300 | **90,000 proposed** |
| Legendary greatbow | 400 | **150,000 proposed** |

**Batch:** 4 tested bows × 4 archer effective STR `[100, 200, 300, 400]` × 4 defender effective END `[100, 200, 300, 400]` × 5 armor sets `[AR0, QV Full Medium Boughsteel AR75, QV Full Heavy Boughsteel AR115, QV Full Medium Adamantite AR110, QV Full Heavy Adamantite AR170]` = **320 independent landed-hit scenarios**. All wearers assumed to meet their armor operation prerequisites; shot eligibility, practical arrow manufacture, character level, and weapon minimums are held out rather than invented. To reproduce, apply the equations above for each combination.

### Quadratic partial-draw Power grid

| Bow / shooter effective STR | 100 | 200 | 300 | 400 |
|---|---:|---:|---:|---:|
| High-draw, cap100 | 14,500 | 14,500 | 14,500 | 14,500 |
| Titan, cap200 | 11,250 | 45,000 | 45,000 | 45,000 |
| Colossal, cap300 | 10,000 | 40,000 | 90,000 | 90,000 |
| Greatbow, cap400 | 9,375 | 37,500 | 84,375 | 150,000 |

**No premature upgrade effect:** Highest Power among the four candidates is high-draw near STR100, Titan after about STR114, Colossal after about STR213, and Greatbow after about STR310. At STR200 the Titan's 45,000 beats the Greatbow's partial 37,500; at STR300 Colossal 90,000 beats Greatbow partial 84,375. Thresholds use the stated quadratic model and assume every bow can be legally drawn at that strength; future minimum controllable draw/handling and arrows may restrict access further.

### Injury comparison (QV Full Heavy Adamantite AR170, ordinary piercing)

**At matched archer STR and defender END:**

| Bow at own full cap | Archer STR = target END | Impact ratio | Injury stages |
|---|---:|---:|---:|
| High-draw | 100 | 0.842 | 1 (Solid) |
| Titan | 200 | 0.953 | 1 (Solid) |
| Colossal | 300 | 0.926 | 1 (Solid) |
| Greatbow | 400 | 0.897 | 1 (Solid) |

This **one injury against comparable-END exceptional plate** persists across all five tested QV/unarmored protection sets at each matching tier, with input ratios above 0.75 and at most 1.75. Individual Strength and END are reference values, **not level-locked character templates**.

**At each bow's full rated Power versus END100 / END200 / END300 / END400 wearing QV Full Heavy Adamantite:**

| Bow | END100 | END200 | END300 | END400 |
|---|---|---|---|---|
| High-draw STR100 | 1 | 0 | 0 | 0 |
| Titan STR200 | 2 | 1 | 0 | 0 |
| Colossal STR300 | 3 | 2 | 1 | 0 |
| Greatbow STR400 | 3 | 3 | 1 | 1 |

**Sensitivity trials, all UNAPPROVED:**

| Candidate schedule | STR100 cap | STR200 cap | STR300 cap | STR400 cap | Matched-END QV Adamantite Heavy result |
|---|---:|---:|---:|---:|---|
| Conservative | 14,500 | 42,000 | 80,000 | 130,000 | Solid at all four |
| **Balanced, recommended** | **14,500** | **45,000** | **90,000** | **150,000** | **Solid at all four** |
| Aggressive | 14,500 | 55,000 | 115,000 | 210,000 | Solid at all four |

Conservative Greatbow STR400 vs END200 QV Adamantite Heavy yields **Devastating** (130k / 47,225 = 2.753), whereas Balanced crosses into **Overwhelming** (150k / 47,225 = 3.176). Aggressive Greatbow vs END300 QV Adamantite Heavy reaches **Devastating** (210k / 97,225 = 2.160), versus Balanced **Solid** (150k / 97,225 = 1.543). Balanced thus rewards a legendary stat disparity without over-inflating damage against near-matched END300.

**Scenario count outcomes across the 320 balanced cases** (80 per bow, including all target material/class combinations at STR100/200/300/400): high-draw Superficial60/Solid20/Devastating0/Overwhelming0; Titan 46/19/3/12; Colossal 36/19/11/14; Greatbow 33/22/8/17. This is a grid count **not a probability distribution**; no assumed opponent occurrence frequencies, hit chances, ammunition shortages, setup actions or survival rolls.

### Comparison to older approved ranged designs

The **previously approved** shot Power anchors are advanced crossbow **17,000**, advanced arbalest **26,000**, precision rifle **15,000**, light precision firearm **11,800**. On a landed conventional piercing hit against END100 QV Full Heavy Adamantite, crossbow/arbalest/rifle yield **Solid** (1 stage). Against END200 in the same armor, all three become **Superficial**; a fully drawn Titan is **Solid**, and a fully drawn Greatbow is **Overwhelming**. The latter requires the enormous proposed STR400 and compatible legendary bow/arrows, so it is not free baseline firearm obsolescence. The arbalest still offers its distinct accessible STR70 winch support, fixed 26,000 Power and two-turn reload; rifle offers approved range up to 900 ft and magazine/recoil identity. **Do not extrapolate unapproved legendary bow range/reload/DEX minimums from these damage numbers.**

### Findings and design risks

1. **The ladder meets the approved goal:** every new cap creates a relevant high-Strength window; high-cap bows are intentionally inefficient for lower-Strength users. A legendary hero who remains on the cap100 bow is decisively under-equipped.
2. **Do not auto multiply by 16:** giving the STR400 bow an untested 232,000 shot Power derived from cap100's rated 14,500 would be a different, much more aggressive calibration, not a natural consequence of the accepted partial-draw formula. Each designed bow has its own calibrated full-draw rating.
3. **Overmatch can be Overwhelming:** legendary bows against opponents with dramatically lower END frequently reach 3 injury stages, including some QV Heavy Adamantite. The author has approved significant disparity in injury output for greatly superior weapon/material power; this warrants qualitative confirmation rather than arbitrary damage caps.
4. **System-wide END² dominates static armor at legendary END:** at END400, ordinary 50% Piercing through QV Heavy Adamantite gives Defense167,225 versus 160,000 unarmored, so armor changes physical Defense by only ~4.5%. This is a consequence of the **existing defense architecture**, not unique to bows. Reassess in later high-end armor/endurance balancing if necessary; do not silently alter AR or Piercing bypass here.
5. **Ammunition and action tempo require their own decisions:** very high-draw constructions need credibly rated arrows, strings, structure, safe nocking and physical positioning. Tests assumed **one legal conventional bowshot per attack action** as the older ordinary-bow baseline, but did **not approve** equal nock/draw tempo or a new extra reload cost for legendary greatbows. High-end bow ranges, projectile load, quality effects, controllable minimum draw, DEX/STR gates and fabrication materials remain open.

**Recommendation for next author review:** Preserve the existing cap100 high-draw proposal and test the **balanced new full-draw ratings 45k/90k/150k** with carefully differentiated minimum controllable draw, Handling DEX and custom arrow engineering. Compare early/mid/legendary equipment acquisition and vulnerability, rather than awarding free Power from a universal item-Quality factor. The legendary STR400 reach is approved; **numerical item values above are NOT canon until explicitly accepted**.

---

## November 11, 2026 — Legendary bows must exploit Strength through 400 (AUTHOR-APPROVED DESIGN GOAL)

**Explicit author direction:** Mystaria must offer **distinct engineered bow designs** whose full-draw capacity reaches **effective STR 400**. This is a **broad archery progression requirement**, not an instruction to raise the previously proposed advanced high-draw bow's STR100 cap to 400, not a grant of unlimited STR-to-Power on existing bows, and not a newly established universal STR400 maximum for all future equipment. At least one genuinely attainable-for-legendary-heroes bow construction must have a draw cap of 400 so that heroic Strength up to that value can contribute meaningfully to that bow's shot Power.

**Preserve approved bow physics:** For each legally drawable bow/arrow combination, `shot Power = that specific bow-and-arrow design's rated full-draw Power × [min(effective shooter STR, that design's engineered draw cap) / that engineered draw cap]^2`. The draw cap is the construction's maximum usable draw force. An archer beyond the cap cannot extract extra Power from *that particular bow*, but can progress to a stronger design. **Every model needs its own separately calibrated full-draw Power and its own engineering requirements**: do not apply the existing advanced bow's approved **14,500 full-draw Power** to a new STR400 bow or extrapolate 14,500 × (400/100)^2 = 232,000 as an approved stat. DEX continues to govern aiming/handling; the power budget is not an uncapped melee STR formula.

**Candidate architecture, NOT APPROVED NUMERIC WEAPON ROWS:** Retain the existing advanced high-draw bow's **proposed STR100 cap** as one design (its cap remains a candidate, while its rated full-draw Power 14,500 is an approved working benchmark). Illustrative *additional distinct* constructions might include a titan bow (cap200), reinforced colossal composite bow (cap300) and legendary greatbow (cap400). The labels, 200/300 milestones, structural components, full-draw Powers, Draw/Support STR floors, DEX handling, ammunition, materials, crafting, prices, range bands and availability are **unapproved proposals** and must be designed and tested before canonization. The *existence of bow designs capable of exploiting STR400* is approved; the item examples are not.

**Material, Quality and ammunition interaction:** Stronger materials, bow architecture, reinforcement and compatible arrows should plausibly permit higher engineered draw caps and distinct Power ratings; details are open. Do **not** introduce a universal ranged Quality-to-Power multiplier, automatically raise every bow's cap with Quality, assume workmanship universally increases available draw force, or double-count material effects. Existing approved Quality workmanship/requirement relief is distinct from engineered capacity; any model-specific quality/cap effect requires author approval. The mundane draw ceiling represents the bow, not a global archery prohibition. Maintain partial draw, handling limits, physical viability, distinct projectile requirements and the approved Close/Effective/Far/Extreme attack eligibility.

**Next calibration:** Propose a dedicated high-strength bow ladder and compare per-design full-draw Power, partial-draw usefulness, ammo engineering, draw/handling gates, reload/exposure and armor injury with the advanced arbalest and precision firearm at representative Strength 100/200/300/400. Avoid automatic one-hit extremes from casually copying one bow's Power rating into another. Do not silently replace approved arbalest or firearm statistics.

---

## November 11, 2026 — Advanced optic stability, attachment tradeoffs, and target-only magical glint (AUTHOR APPROVED)

**Approval scope:** The author approves the proposed movement/stability and attachment philosophy for the existing advanced precision sight, and adds its specific **magical glint drawback**. These rules apply to a **compatible fitted advanced precision sight**, not every naked eye, mundane optic, scope-shaped item, mundane ranged weapon, or unspecified magical detection effect.

### Aimed firing stability

- **Stable position:** Controlled changes of footing, careful leaning around a parapet or support, adjusting aim, and rotating an appropriately supported weapon can retain both ordinary Aim and the advanced sight's qualified Far/Extreme range-penalty relief **when genuine weapon stability and target tracking are maintained**. A stationary, actually well-supported mount can qualify. Bracing is physical, not merely declaring a posture.
- **Controlled repositioning that breaks the brace:** Walking away from a firing rest or otherwise losing a genuine stable shooting position removes the **advanced sight's additional** one-category Far/Extreme range-penalty relief. The ordinary paid Aim benefit **may persist only while the shooter actually maintains the relevant target tracking and uninterrupted preparation**. Repositioning alone is not an automatic loss of both advantages; nor does moving instantly create a new free brace.
- **Major disruption:** Knockback, loss of target tracking, a forced evasive maneuver that abandons the shot, or another genuinely disruptive event that breaks preparation defeats **both held Aim and the sight's conditional bonus**; acquiring them again requires eligible actions and positioning. Ordinary Pressure, cover, visibility, tactical movement and existing attack/defense rules determine when interruption genuinely occurs; this is not a global new movement difficulty penalty.
- **Mounts:** An ordinary moving saddle does **not** qualify as automatically stabilized. A specialized properly engineered moving stabilization system could be evaluated separately but none receives an unapproved free range benefit. Stable physical carriage or stationary mounting is evaluated normally under established mounted support/arc rules.

### Attachment fit, expenses, and actual vulnerability

- Advanced precision sights must be **physically compatible and properly fitted/calibrated** to their weapon. Installation and initial calibration normally happen **outside combat**; swapping an unattuned, unaligned or incompatible sight during an attack gives no free calibrated benefit. No new arbitrary install time, instant hot-swap rule, or extra combat setup action is created.
- The existing qualification is **effective DEX 100, actual stable/braced shot, and a paid Aim action**. A standard compatible advanced sight **does not impose a new universal Support STR gate, Recoil STR burden, hit penalty, or mandatory extra setup turn** merely because it is fitted. Unusually massive or elaborate variants may have their own real, author-approved requirements in the future, not invented now.
- Sights are **valuable specialist equipment** with meaningful acquisition and maintenance/repair costs. Exact **Gem values, materials, craftsmanship procedures, fitting times, mass, Quality rules and repairs** are **UNRESOLVED** pending the equipment economy pass, not numeric canon here.
- Direct meaningful damage or actual misalignment can impair or disable the sight's **enhanced precision benefit** until it is repaired/recalibrated; a normal discharge, ordinary incidental jostling, or ordinary movement does **not** automatically break the sight. An intact underlying weapon may still fire ordinarily where physically capable. No universal numeric sight durability track or automatic item-break trigger is created.

### Target-only magical glint: the sniper's tradeoff

- **AUTHOR-APPROVED SPECIAL WEAKNESS:** When an advanced precision sight is used to acquire/aim at a **specific intended target**, that target alone can perceive a **distinct magical glint associated with the sight's firing position** when it is within their ability to perceive it. **No other creature sees that special glint merely by being nearby, watching the same shooter, or being one of the intended target's allies.** The glint does not illuminate the environment or function as a public light source.
- This deliberately **compromises a hidden sniper's concealment against their intended target**: a target who can perceive the glint can discern and identify the associated sniper position sufficiently to **call it out**. It is not a magically broadcast teamwide location ping, guaranteed omniscience through opaque barriers, a free line-of-fire solution, or a generic ability to identify every sniper on a battlefield.
- **Failed lethal opening shot:** If the shot does **not kill or otherwise prevent the target from communicating**, a still-capable target can **warn allies and identify the firing position**. Those allies may then use the ordinary rules for warning, seeking cover, changing position, counterfire, coordinated Pressure, and pursuit. **Allies cannot perceive the glint themselves** merely because the target tells them. A victim actually killed or incapacitated before communicating cannot provide the warning through ordinary means.
- The magical tell **does not itself grant a free attack, free dodge, additional action, automatic PP, extra accuracy penalty, or cancellation of a legally prepared shot**. It may inform a target's legitimate later or otherwise available reactions and tactical choices under existing timing/action rules. The glint is not blocked by a mundane camouflage claim when an actual intended target can perceive it, but ordinary geometry/visibility and physical barriers remain meaningful. Do not invent a mandatory pre-shot warning turn or a universal immediate counterattack.
- This is an approved **magical perceptual trait of the advanced sight**, **not** an established MP expenditure, Soul Strain, gem/enchantment slot, learnable Sorcery skill, counterspell, free magical detection by uninvolved observers, or new exception to existing magical range rules. Its exact magical origin and exceptional sensory interactions are **UNRESOLVED**, not silently specified here.

**Preserved mechanics:** Advanced sight grants only one additional category of relief from the Far or Extreme **range** penalty if DEX >= 100, genuinely stable/braced, and a valid normal Aim action has been spent. Ordinary Aim itself grants one easier category, not another PP. There is no benefit at Close/Effective, change in shot Power/armor bypass, range extension past Extreme, cover bypass, automatic extra action, or newly approved material/price modifier. Existing historically unapproved attachment numeric options remain superseded as applicable by these explicit principles, rather than silently deleting prior test records.

---

## November 11, 2026 — Extreme is the outer limit for ordinary ranged attacks (AUTHOR APPROVED)

**Latest explicit decision:** There is **no ordinary ranged attack range beyond a weapon's own Extreme band**. For a ranged weapon whose item-specific band boundaries have been established, a target **past the upper Extreme distance is ineligible for an ordinary direct ranged shot**. Do not create a fifth distance band, add stacking penalties for shooting past Extreme, or allow a precision sight, extraordinary DEX, ordinary Aim, Pressure, higher Quality, or an unsupported attachment to extend this limit. The existing approved advanced precision sight grants only its Far/Extreme **accuracy relief within the listed bands**, never additional feet of range.

This is an **attack eligibility and game-design boundary**, not a claim that fired arrows, bullets or bolts magically cease moving at that distance or that sight and cover are the only physical variables. It does not set an as-yet-missing Extreme endpoint for another weapon, rewrite unrelated spell or magical effect ranges, or change the distinct approved 10-meter Concentrated Burst Point Blank condition. Extraordinary nonordinary attacks would require their own explicit source rule and author approval; none is newly created here.

**Supersession:** Earlier entries saying attack eligibility *past* Extreme remains unresolved are historical and **superseded by this approval** for ordinary ranged weapons with defined limits. Existing ranged working Power, armor bypass, Far/Extreme accuracy modifiers, Aim, advanced sight eligibility, cover and all five approved foot-based range endpoints are unchanged. Movement/stability and attachment-cost proposals remain unapproved pending author choice.

---

## November 11, 2026 — Advanced precision sights: Option A (AUTHOR-APPROVED WORKING CALIBRATION)

**Approved enhanced-sight procedure.** An advanced precision sight operated by a shooter with **effective DEX at least 100**, from a **stable, braced shooting position**, and with **a genuine Aim action spent to prepare the subsequent eligible shot**, reduces the weapon's ordinary **Far or Extreme range hit-difficulty penalty by one category**, to a minimum range penalty of zero. This is **in addition to** the normal Aim improvement of **one easier difficulty category** for the following valid shot, and **does not generate Pressure Points**.

| Original range band | Baseline penalty | Qualified aimed precision-sight penalty |
|---|---:|---:|
| Close | 0 harder | 0 harder |
| Effective | 0 harder | 0 harder |
| Far | +1 harder | 0 harder |
| Extreme | +2 harder | +1 harder |

**Boundaries:** Apply scope relief only to the **range component**, once per qualifying aimed shot; it is not a universal +1 for shots already at Close/Effective, a free Aim action, an additional attack, another PP, or an automatic extra precision bonus based on DEX beyond the qualifying threshold. It does not extend the weapon's established Far/Extreme distance boundaries or authorize shots beyond Extreme. Underlying firearm, bow and crossbow Power; ammo; cover; independent Support STR/Recoil STR/Handling DEX; recoil strain; evasion; Pressure; physical barriers; and sight lines remain unchanged. A target totally hidden behind a solid surface remains ineligible for ordinary direct fire regardless of Aim or optics. The equipped weapon must plausibly accept the sight; no blanket entitlement for arbitrary projectiles, siege mounts or unusual firing methods is created.

**Qualified vs ordinary use:** DEX100 and stable bracing are the working gates for exploiting the *enhanced range relief*, not general minimums for operating an otherwise lawful weapon or taking a normal Aim action. A shooter who does not meet the enhanced sight's conditions retains ordinary Aim and range rules. No universal attachment cost, Quality/STR reduction, optic mass, setup action, magnification, sighting-through-obscurement, or special scope durability is established by this approval. Losing the qualifying stable shooting posture or valid Aim means no enhanced benefit on that shot; whether such changes separately cancel normal held Aim continues under existing target-tracking/interruption rules.

**Supersession:** This adopts **Proposal A (range-penalty relief)** from the previous noncanon precision-sight tests as approved working calibration, including its stated effective DEX100, stable/braced posture, and paid Aim conditions. The competing **Proposal B (25% Effective/Far band extension)** remains **not approved**, not additive. Other older blanket statements that *all* scope numeric requirements and benefit ratings are unsettled are superseded **for this advanced sight only**. The separate DEX100 unseen-location, DEX150 ricochet, and DEX300 extreme precision *feat* illustrations are **not** approved or unlocked by this optic DEX gate.

---

## November 11, 2026 — Ranged accuracy and advanced sights: sensitivity tests (NONCANON WORKING NOTES)

**Status: TEST ONLY, NOT AUTHOR-APPROVED NEW MECHANICS.** Existing approved rules were tested: Close/Effective/Far/Extreme penalties 0/0/+1/+2 harder; Normal/Full/Amazing cover +1/+2/+3 harder; Aim -1 category to a subsequent valid shot but no PP; separately earned net 1-2 PP gives -1 category and 3+ PP gives -2. Cap at the six-tier difficulty ladder. Full obstruction invalidates an ordinary direct shot regardless of modifiers.

**Average baseline, Normal Cover (No Aim -> Aim -> Aim plus genuine PP1):** bow 250 ft Extreme: Impossible -> Very Hard -> Hard; crossbow 250 ft Far: Very Hard -> Hard -> Average; arbalest 400 ft Extreme: Impossible -> Very Hard -> Hard; rifle 400 ft Effective: Hard -> Average -> Easy; rifle 600 ft Far: Very Hard -> Hard -> Average; rifle 850 ft Extreme: Impossible -> Very Hard -> Hard. Hard baseline at Extreme with Normal Cover needs Aim plus genuine PP1 to reach Very Hard, whereas Very Hard baseline is still Impossible with these modest aids. At 400 ft bow/crossbow exceed listed range profiles; at 600/850 ft only the rifle is within an approved distance band; over-Extreme eligibility remains unresolved.

**High DEX:** Prediction can improve real tactics if accurately stated and justified at DEX >= 75% of target SPD; DEX >= 200% of target SPD removes the wrong-prediction-specific penalty. Neither grants automatic offensive PP or Aim, cancels cover, reduces range difficulty, or multiplies intrinsic shot Power. Combat's indicative DEX100 unseen, DEX150 ricochet, DEX300 extreme precision feats remain unapproved illustrative examples, not automatic unlocks. Recoil strain creates PP against the shooter, NOT their target.

**PROPOSAL A (unapproved, recommended for simplicity):** When a shooter has a suitable precision sight, provisional DEX >=100, stable braced position, and spends a real Aim action, reduce the Far or Extreme range penalty one further category, never below 0; ordinary Aim also still applies. Rifle vs Normal Cover with Aim: 400 ft stays Average (Effective), 600 ft improves Hard to Average, 850 ft improves Very Hard to Hard. Does not extend the Extreme boundary or bypass physical barriers.

**PROPOSAL B (unapproved):** Same experimental DEX100/stability/Aim prerequisites, but instead extend only the Effective and Far boundaries by 25% for this scoped shot; Close/Extreme fixed, ordinary Aim only. Rifle with Normal Cover and Aim: 600 ft stays Far/Hard, 700-800 ft becomes Far/Hard rather than Extreme/Very Hard, 850 ft stays Extreme/Very Hard. Arbalest at 400 ft stays Extreme (300 ft Far ×1.25 = 375 ft). This creates many weapon-specific intermediate cutoffs.

**Finding:** No numeric changes are needed to approved range/Cover/Aim/Pressure rules. A and B are alternative, noncanon attachment ideas for author review, not cumulative effects. The separate approved 10-meter Point Blank burst remains unchanged; it is not synonymous with Close and has not been converted to feet. Exact scope benefits, recoil and moving-fire interactions, line-of-sight stability, and beyond-Extreme firing remain unresolved.

---
## November 11, 2026 — Range-band hit-difficulty calibration approved (LATEST AUTHOR APPROVAL)

**Approved, Option A: accuracy-only range effects.** Resolve range **relative to the firing weapon's own valid Close / Effective / Far / Extreme distance bands**, applying a direct change to the existing **six-tier hit-difficulty ladder**:

| Weapon's range band | Additional difficulty to land a valid shot |
|---|---|
| Close | 0 categories |
| Effective | 0 categories |
| Far | **1 category harder** |
| Extreme | **2 categories harder** |

**No range-based reduction to physical shot Power, armor penetration, or injury severity occurs from these bands.** If an otherwise legal shot connects, determine its Power and applicable Defense through the existing ranged family, ammunition, armor, and injury rules; bow partial-draw reduction remains a distinct approved source of lower shot Power. Neither Close nor Effective grants an automatic bonus or hit. The rule supplies **no accuracy bonuses to invalid shots**, and does not declare that a projectile necessarily stops travelling beyond Extreme: out-of-profile distances and their shot eligibility remain for later author review.

**Combine ordinary tactical circumstances without inventing extra rules:** A real exposed target behind approved **Normal / Full / Amazing Cover** adds **1 / 2 / 3 harder categories**, respectively, not Pressure Points; use the actual applicable cover rather than stacking overlapping cover objects for the same exposed line. A separately spent valid **Aim action** makes its next eligible shot **one category easier** and grants **no PP from that same Aim**. Existing Pressure, cover, six-tier end-category caps, line of sight, physical barriers, evasion, handling, recoil, and aiming restrictions still apply. A fully blocking wall makes an ordinary direct shot **ineligible**, regardless of Aim or otherwise favorable difficulty. Aim, Pressure and range do not multiply the intrinsic shot Power.

**Range scope:** This category rule applies to lawful ranged attacks once their **weapon-specific range bands are established**. The five approved advanced test designs currently have explicit **feet** endpoints in the ranged catalogue. Other item-specific numerical bands remain unresolved. The previously approved **10-meter Point Blank Concentrated Burst requirement** is a *separate tactical condition* and is **not** converted, changed, or replaced by the new Close band. Existing arbalest Support STR70 / Handling DEX40 / hand-cocking STR170 or winch STR70 / one setup turn / two reload turns and all five approved shot Power benchmarks are unchanged. Scope and range-band interaction with unusual projectiles, indirect firing, visibility, firing beyond Extreme, or magical effects beyond ordinary physical shots require later specific decisions.

---

## November 11, 2026 — Advanced arbalest controlled access and five effective-range profiles (AUTHOR-APPROVED WORKING CALIBRATION)

**New author decision:** Choose the prior **Option A, controlled early availability** for the **advanced 26,000-Power arbalest**. Its working operating thresholds are **Support STR 70**, **Handling DEX 40**, **hand-cocking STR 170**, or **cocking with a suitable winch at STR 70**. It requires **one setup turn** and **two reload turns** after firing; the shot uses the normal attack action. This is the *advanced model*, not an overwrite of the original catalogue's entry arbalest (X-04) test requirements or Power. A winch does not eliminate the separate Support STR and Handling DEX gates, and no equipment is unlocked by character level. Existing approved workmanship and genuine rated-support rules apply where legitimately eligible; whether workmanship modifies the winch/hand-cocking **mechanism** gate, and when setup must be repeated, remain unresolved rather than invented. The 26,000 shot Power, ordinary Piercing 50% covered-AR bypass, and two-turn reload benchmark are preserved.

**Range approval:** Retain the exact previously offered numeric **Close / Effective / Far / Extreme upper boundaries**, but express every value **in FEET rather than meters, without numerical conversion**. Thus 15 m from the earlier proposal becomes **15 ft**, not an equivalent number of feet. These are approved **working weapon-specific range bands**, not final accuracy modifiers, guaranteed maximum projectile travel distances, ballistic Power falloff, line-of-sight overrides, or new spell/ranged global mechanics. All five profiles are additional advanced designs; entry models keep their preexisting, separately provisional range labels and handling values.

| Advanced design | Close through | Effective through | Far through | Extreme through |
|---|---:|---:|---:|---:|
| High-draw bow | 15 ft | 130 ft | 210 ft | 300 ft |
| Advanced crossbow | 15 ft | 150 ft | 250 ft | 350 ft |
| Advanced arbalest | 15 ft | 180 ft | 300 ft | 450 ft |
| Advanced precision rifle | 25 ft | 400 ft | 650 ft | 900 ft |
| Light precision firearm | 15 ft | 180 ft | 300 ft | 450 ft |

**Approval scope:** Only the **advanced arbalest's Option A handling and setup** and the **five proposed range breakpoints relabeled into feet** were accepted here. The suggested advanced high-draw bow draw STR35 / DEX30 / cap100, crossbow Support28 / DEX30 / cocking STR90 or lever40, rifle Support40 / Recoil70 / DEX50, and light precision firearm Support22 / Recoil38 / DEX40 are **still exploratory test proposals, not approved item requirements**. Approved ranged shot Powers remain 14,500 / 17,000 / 26,000 / 15,000 / 11,800; no blanket ranged Quality-to-Power multiplier is created. Previously approved *other* distances stated in meters, including the firearm Concentrated Burst's existing 10 m Point Blank condition, are not automatically altered by this weapon-range decision. The chosen feet ranges should be tested against existing accuracy, sight, cover, equipment handling, firing cycles, and battlefield geometry before adopting further modifiers.

---

## November 11, 2026 — Five advanced ranged Power benchmarks approved

Use the following **approved test ratings** for the first five advanced ranged profiles. The bow value is full-draw Power and follows the approved quadratic partial-draw rule. The other values are ordinary landed-shot Power for the test weapon and load. The plate comparisons used genuine Piercing with 50% base AR bypass.

| Advanced test profile | Shot Power |
|---|---:|
| High-draw bow | 14,500 at full draw |
| Advanced crossbow | 17,000 |
| Advanced arbalest | 26,000 |
| Advanced precision rifle | 15,000 |
| Light precision firearm | 11,800 |

At level 100 against Quality V Full Heavy Boughsteel, the advanced arbalest delivered two injury stages while the other four delivered one. Against matching Adamantite, the light precision firearm was Superficial and the others delivered one. At the level-50 benchmark, the advanced arbalest delivered three stages. Next test draw caps, cocking and setup, firearm Support STR, Recoil STR and Handling DEX, and item availability before finalizing individual profiles. These ratings do not finalize the handling, ammunition, availability, or range values.

---

## November 11, 2026 — Ranged Power progression by weapon design (author approved)

Build late-game ranged Power around distinct, higher-rated weapon designs. Give advanced bows, crossbows, and firearms their own Power ratings, handling requirements, and firing or reload tradeoffs. Do not introduce a shared ranged Quality multiplier as the mechanism for this progression. Entry models keep their own ratings when an advanced model is introduced. Bow Power remains subject to the approved quadratic partial-draw rule. Crossbow and firearm shot Power still derives from the weapon and its projectile or load. Keep the approved opening-hit emphasis for slower weapons. Exact advanced ratings, requirements, reloads, availability, materials, and ammunition remain under calibration.

---

## November 11, 2026 — Ranged draw, reload, and opening-hit benchmarks approved

**Bow draw.** For a shot the archer can legally make, usable draw is the lower of effective STR and the engineered draw cap. Shot Power is the bow-and-arrow full-draw Power multiplied by `(usable draw / draw cap)^2`. DEX governs aim and handling. Individual full-draw Power, draw caps, and minimum controllable partial draw remain open for item calibration.

**Reload pace.** Use one reload turn for most handheld profiles in the working comparison and two for the arbalest. A loaded shot takes its normal attack action. Time spent reloading is separate. Ordinary bow nocking and drawing use the existing bow procedure. Preserve the approved full-turn single-shot pistol and high-capacity magazine reloads. Individual capacity, cycling exceptions, and mounted or siege crew cycles remain subject to their own profiles.

**Damage target.** Give slower ranged weapons a stronger opening hit. Tune the stronger first hit and the full firing cycle together against unarmored, Medium-armored, and Heavy-armored targets. Equal sustained injury output is not the design target. This approval establishes the calibration method and pacing, not the menu's individual shot Power, ammunition, range, or mount test values.

---

# Mystaria Ranged Weapon Catalogue — STEP 3 DESIGN DRAFT

**Created November 6, 2026. All individual numeric specifications, ammunition counts and range assignments below are proposed and NOT CANON.** This is the third of five weapon-shape workstreams. The first two developed the melee shapes and their Power calibration; the user wants numerical multi-target coverage kept unresolved and ARMOR designed immediately after all five shape phases. A primary ranged Coverage column is shown prominently, consistent with the approved master melee chart presentation.

## Existing approved mechanical foundation

- Five physical propulsion families: **Bows**, **Crossbows**, **Firearms**, **Thrown/Manual**, **Mounted/Siege**. Relative weapon range bands **Close / Effective / Far / Extreme**; distance cutoffs are weapon-specific, not a universal meter ladder.
- **Bow Model A:** shooter STR controls how much force can be drawn up to the engineered bow maximum. Bow and ammunition construction set full-draw Power. The approved quadratic partial-draw rule is above. Individual caps and full-draw Power remain candidates.
- **Crossbows** use stored mechanical energy from their design; STR/cocking assistance affects operation/loading and DEX determines aim. A hand crossbow in established starting equipment comes with twelve bolts; this does NOT mean twelve bolts loaded at once.
- **Firearms** derive shot physical Power from frame, chamber, ammunition and propellant, **not** the shooter's STR/DEX. Each requires independent **Support STR**, **Recoil STR single/volley** and **Handling DEX**, a numeric loaded **Capacity**, and automatic types additionally **Full-Auto Volley Cost**. Mounts may physically transfer weight and recoil, not eliminate momentum or grant actions.
- **Thrown/manual** attacks draw on lawful STR/DEX input and physical projectile/ammunition, with all attack modes checked against realistic delivery. The author approved a modest **DEX handling minimum for STR-led ranged weapons**, not a DEX-derived bonus to Power.
- **Automatic Suppressive Fire:** qualified full volley produces **+1 meaningful PP** at range. **Concentrated Burst:** qualified full volley within **10 m Point Blank**, when almost every shot plausibly connects despite recoil, gives **×1.35 final physical Power**. Modes are alternatives and share one attack action, not separate bullet actions; one user's offhand Attack/Defense and burst/suppression benefits do not stack.
- **Recoil Strain:** by effective STR / supported applicable Recoil STR requirement: >=125% single/volley +0/+1 strain; 100–<125% +1/+2; 75–<100% +1/+2; 50–<75% +2/+3; <50% unsafe unsupported. 0/1/2/3+ accumulated strain creates 0/1/2/3 PP **against shooter**; full nonshooting turn clears, even spent moving/casting. No DEX penalty. One firing event can inflict at most **one recoil injury state** when legitimately injurious.
- Heavy equipment insufficiently supported may incur **2 percentage points of situational SPD loss per 1% missing applicable STR requirement**, floored at zero, greatest applicable shortfall counted once. A different group's actual mechanical draw vs support requirements require their own profiles; do not blindly apply firearm recoil rules to bows and crossbows.
- Eligible incoming shots against **Normal / Full / Amazing cover** are respectively one / two / three difficulty categories harder; cover is **not** PP. A fully blocking surface with no exposed target forbids ordinary direct targeting. Aim sacrifices an attack action for one category easier on a later valid shot.
- Careful **single-shot pistol** and **high-capacity-magazine reload** consume a full turn as approved; ordinary bow nock/draw has negligible special vulnerability, light crossbow modest opening, siege typically major exposure. Individual other reload times remain to be specified.
- Trufula is extremely flammable and requires a compatible pressure-safe noncombustive impulse arrangement; Crownsalt is an exceptionally potent combustible propellant. Adamantite reinforced frames can serve heavy STR users; don't assert universal alloy-derived final Damage Rating yet.

## Main ranged shape catalogue

**All numbers in this table are PROPOSAL ONLY.** `Support / draw STR` is an illustrative load or draw threshold; for bows the additional proposed `Cap` is the maximum draw-STR force the weapon design supports, not a no-penalty requirement; for guns `Recoil STR` lists single/volley. **DEX entries for every STR-powered ranged family are meaningful aiming/control floors, not direct Power scaling.** Loaded capacity and volley cost are shown as `cap / volley` for automatic guns. Primary Coverage is geometrical, not quantitative; unapproved suppression footprints are denoted explicitly. 'Effective: mid' etc are **comparative design labels only** and do not approve a range in meters.

| ID | Weapon | Family | Handling | Governing Power / aim | **Support or draw STR** | **Handling DEX floor** | **Recoil STR single / volley** | **Primary Coverage** | Proposed relative range | Capacity / volley or ammunition | Intrinsic Power / bow cap | Design note |
|---|---|---|---|---|---:|---:|---|---|---|---|---|---|
| B-01 | Shortbow | Bow | Light | STR draw / DEX aim | 16 | 12 | — | Point | Effective: short | 1 arrow / nock-draw | Cap 22 | Light hunting/backup |
| B-02 | Recurve bow | Bow | Light | STR draw / DEX aim | 21 | 15 | — | Point | Effective: mid | 1 arrow / nock-draw | Cap 32 | Mobile bend design |
| B-03 | Longbow | Bow | Medium | STR draw / DEX aim | 29 | 19 | — | Point | Effective: long | 1 arrow / nock-draw | Cap 43 | Long stave, open space |
| B-04 | Composite bow | Bow | Medium | STR draw / DEX aim | 26 | 22 | — | Point | Effective: long | 1 arrow / nock-draw | Cap 46 | Engineered composite draw cap |
| B-05 | Warbow | Bow | Heavy | STR draw / DEX aim | 38 | 21 | — | Point | Effective: long | 1 arrow / nock-draw | Cap 60 | Heavy draw specialist |
| B-06 | Mounted recurve | Bow | Medium | STR draw / DEX aim | 25 | 23 | — | Point | Effective: mid | 1 arrow / nock-draw | Cap 38 | Mount-friendly overall handling; not free mount attack |
| X-01 | Hand crossbow | Crossbow | Light | Mechanism / DEX aim | 10 | 15 | — | Point | Effective: short | 1 bolt loaded / modest reload | Stored Power TBD | The existing starter kit includes 12 loose bolts, not 12 loaded |
| X-02 | Hunting crossbow | Crossbow | Medium | Mechanism / DEX aim | 18 | 18 | — | Point | Effective: mid | 1 bolt loaded / meaningful reload | Stored Power TBD | Manual drawn or cocking aid |
| X-03 | Military crossbow | Crossbow | Medium | Mechanism / DEX aim | 25 | 22 | — | Point | Effective: long | 1 bolt loaded / heavier reload | Stored Power TBD | Winch/tool variant possible |
| X-04 | Arbalest | Crossbow | Heavy | Mechanism / DEX aim | 35 | 25 | — | Point | Effective: long | 1 bolt loaded / major reload | Stored Power TBD | Heavy external loading aids |
| X-05 | Repeating crossbow | Crossbow | Medium | Mechanism / DEX aim | 22 | 26 | — | Narrow | Effective: short-mid | 6 bolts candidate / cycling | Stored Power TBD | Not automatically qualified as gun-style full auto |
| X-06 | Battle-saddle crossbow | Crossbow | Heavy | Mechanism / DEX aim | 40 unsup. | 30 | — | Point | Effective: long | 1 bolt loaded / assisted optional | Stored Power TBD | Saddle load relief physically rated |
| G-01 | Single-shot pistol | Firearm | Light | Intrinsic / DEX aim | 14 | 18 | 20 / — | Point | Effective: short | 1 / full-turn careful reload | Power TBD | Compact single-shot firearm |
| G-02 | Revolver | Firearm | Light | Intrinsic / DEX aim | 18 | 20 | 25 / — | Point | Effective: short-mid | 6 / multi-cartridge reload TBD | Power TBD | Chamber count candidate |
| G-03 | Automatic pistol | Firearm | Light | Intrinsic / DEX aim | 20 | 24 | 27 / 38 | Point; suppression Narrow | Effective: short-mid | 12 / 8 volley | Power TBD | Stock mag one full volley |
| G-04 | Musket | Firearm | Medium | Intrinsic / DEX aim | 24 | 23 | 32 / — | Point | Effective: mid | 1 / careful full load TBD | Power TBD | Early long firearm |
| G-05 | Carbine | Firearm | Medium | Intrinsic / DEX aim | 30 | 26 | 35 / — | Point | Effective: mid | 8 / sequential or feed TBD | Power TBD | Nonautomatic form |
| G-06 | Automatic carbine | Firearm | Medium | Intrinsic / DEX aim | 35 | 30 | 40 / 55 | Point; suppression Narrow | Effective: mid | 20 / 12 volley | Power TBD | Stock mag one full volley |
| G-07 | Precision rifle | Firearm | Heavy | Intrinsic / DEX aim | 40 | 38 | 47 / — | Point | Effective: long | 5 / reload TBD | Power TBD | Advanced optic DEX higher if fitted |
| G-08 | Adamantite heavy automatic rifle | Firearm | Heavy | Intrinsic / DEX aim | 65 | 25 | 55 / 90 | Point; suppression Narrow | Effective: long | 30 / 18 volley | Power TBD | Illustrative Adamantite-compatible reinforced frame |
| G-09 | Scattergun | Firearm | Medium | Intrinsic / DEX aim | 35 | 26 | 45 / — | Narrow | Effective: short | 2 / manual reload TBD | Power TBD | Spread not guaranteed multiple hits |
| G-10 | Trufula-compatible precision firearm | Firearm | Light | Intrinsic / DEX aim | 16 | 28 | 22 / — | Point | Effective: mid-long | 6 / reload TBD | Power TBD | Pressure-safe noncombustive impulse; Trufula flammability |
| G-11 | Centaur heavy saddle automatic gun | Firearm | Heavy | Intrinsic / DEX aim | 100 unsup. | 35 | 110 / 140 unsup. | Point; suppression Narrow | Effective: long | 24 / 16 volley | Power TBD | Proposed rated saddle residual 45 Support, recoil 70/95 |
| T-01 | Throwing dagger | Thrown/manual | Light | DEX + small Support STR | 6 | 14 | — | Point | Effective: short | 1 / recover or ready next | Melee-like release Power TBD | Distinct from held dagger reach |
| T-02 | Throwing axe | Thrown/manual | Light | STR throw / DEX aim | 12 | 8 | — | Point | Effective: short | 1 / recover or ready next | Throw Power TBD | STR-led ranged DEX floor |
| T-03 | Javelin | Thrown/manual | Medium | STR throw / DEX aim | 18 | 10 | — | Point | Effective: mid | 1 / ready next | Throw Power TBD | Needs physical flight and room |
| T-04 | Throwing dart | Thrown/manual | Light | DEX + Support STR | 6 | 12 | — | Point | Effective: short | 1 / ready next | Throw Power TBD | No auto suppression |
| T-05 | Sling | Thrown/manual | Light | STR swing / DEX aim | 10 | 12 | — | Point | Effective: mid | 1 stone / ready next | Throw Power TBD | Established Wanderer's Sling in starter gear |
| T-06 | Bolas | Thrown/manual | Light | DEX + Support STR | 8 | 16 | — | Narrow | Effective: short | 1 / ready next | Restrain effects TBD | Entangling form not automatic Trapped |
| S-01 | Ballista | Mounted/siege | Heavy fixed | Stored mechanical / DEX aim | Mount rated | 20 | — | Line | Effective: long | 1 massive bolt / siege cycle | Stored Power TBD | Not automatic penetration through ranks |
| S-02 | Repeating ballista | Mounted/siege | Heavy fixed | Stored mechanical / DEX aim | Mount rated | 28 | — | Line | Effective: long | 6 bolts candidate / mechanical cycles | Stored Power TBD | Not free attacks |
| S-03 | Field cannon | Mounted/siege | Heavy carriage | Intrinsic / DEX aim | Deployed | 25 | Rated recoil | Point / potential Blast | Effective: long | 1 shell / siege cycle | Power TBD | Towing is not firing |
| S-04 | Mortar | Mounted/siege | Heavy carriage | Intrinsic / DEX aim | Deployed | 30 | Rated recoil | Potential Blast | Effective: long | 1 shell / siege cycle | Power TBD | Arcing shot and area depends on ammunition |
| S-05 | Grand siege cannon | Mounted/siege | Grand carriage | Intrinsic / DEX aim | Anchored | 35 | Rated recoil | Point / potential Blast | Effective: extreme | 1 shell / major siege cycle | Power TBD | Engineered load transfer and specialist crew |

## Ranged fire-mode eligibility and ammunition sanity

- The gun candidate Standard Magazine pairs **automatic pistol 12 loaded / 8 per volley**, **automatic carbine 20/12**, **heavy rifle 30/18**, and **saddle gun 24/16**. Each permits **one complete full-auto volley per stock magazine**, as the approved rule requires. Each numerical pair is **still only a candidate**. Upgraded magazines are a separate design and can raise relevant STR and DEX thresholds.
- A 12/8 automatic pistol can fire one complete 8-round volley and has four rounds remaining. It cannot fire another complete volley until reloaded; it can still use lawful normal fire with those four rounds. A 30/18 rifle likewise has twelve rounds left after one volley. No partial-volley bonus is invented.
- The existing hand-crossbow starter kit's **12 spare bolts** do not justify twelve simultaneous shots. Repeating crossbows are not automatically full-auto firearms eligible for the firearm rapid-fire Power option. Their own future mechanical rapid-fire Proficiency must be designed and approved.
- Each full-auto volley is one recoil event, with its own personal Recoil STR requirement. A properly rated Centaur saddle may reduce **personal residual requirements** but does not eliminate recoil or make a towed cannon stable while moving.
- **Important damage gap:** A gun's **intrinsic ballistic Power**, bow full-draw Power, mechanical crossbow stored-energy Power, throwing impact and siege charge still require explicit material-independent baseline calibration before final ranged item stats. **Do not substitute a fake weapon damage number or give a gun `(wielder STR*F)^2` without approval.**

## Cross-stat handling comparison

A **STR-led bow, javelin or sling** has a small DEX minimum to aim or control delivery; it need not scale Power directly with DEX. **A DEX-led thrown dart or throwing knife** has a small physical Support STR minimum like DEX-led melee weapon handling, where relevant. Bow's STR draw requirement and a gun's Recoil STR serve different physics; they cannot all be reduced to one weapon weight field.

## Following work, preserving author sequence

1. Review this 34-shape candidate register: family, ammunition, relative range, feasibility, DEX floor, bow cap, gun Support/Recoil STR and mount operation. Numbers are *not approved yet*.
2. Determine actual **intrinsic ranged Power baseline** without alloy/enchantment layering. Calibrate the remaining per-family Power models and individual shot ratings; keep armor-specific bypass and material modifiers separate.
3. Continue to **quantitative coverage/universal horde combat** and **mounts/rated supports**, the final two remaining shape tasks.
4. **Immediately proceed to ARMOR**, including shields and penetration; afterwards other weapon crafting and other equipment.

This file should not be renamed `CANON` or merged without explicit user approval of specific new numeric and item design choices.


## November 6, 2026 — REPLACEMENT RANGED REQUIREMENTS, AUTHOR-APPROVED TEST BASELINES (NOT FINAL)

These override the **numeric handling requirements** in the original ranged candidate chart for testing only. The original table's other columns (forms, proposed ammo, volley, coverage, etc.) remain separately provisional. For bows, STR is full intended draw and partial draw may be possible with lower force; do not change engineered caps. For crossbows, cocking equipment can alter operator burden. Firearm recoil remains separate from carry/load and normal intrinsic ballistic Power; full-auto volley thresholds are **not set by this new table**.

| ID | Shape | Support/draw STR | Handling DEX | Single-shot recoil STR |
|---|---|---:|---:|---:|
| B-01 | Shortbow | 10 | 9 | — |
| B-02 | Recurve bow | 13 | 11 | — |
| B-03 | Longbow | 18 | 13 | — |
| B-04 | Composite bow | 17 | 15 | — |
| B-05 | Warbow | 25 | 15 | — |
| B-06 | Mounted recurve | 16 | 16 | — |
| X-01 | Hand crossbow | 6 | 10 | — |
| X-02 | Hunting crossbow | 11 | 12 | — |
| X-03 | Military crossbow | 16 | 15 | — |
| X-04 | Arbalest | 23 | 17 | — |
| X-05 | Repeating crossbow | 15 | 18 | — |
| X-06 | Battle-saddle crossbow | rated mount | 20 | — |
| G-01 | Single-shot pistol | 9 | 12 | 15 |
| G-02 | Revolver | 11 | 14 | 18 |
| G-03 | Automatic pistol | 12 | 17 | 20 |
| G-04 | Musket | 15 | 15 | 23 |
| G-05 | Carbine | 18 | 18 | 25 |
| G-06 | Automatic carbine | 21 | 21 | 30 |
| G-07 | Precision rifle | 26 | 25 | 35 |
| G-09 | Scattergun | 19 | 17 | 30 |

**Not replaced by a numeric value in this approval:** special Adamantite/Trufula gun rows, Centaur saddle automatic gun, ordinary throwing/manual weapons, deployed siege equipment, full-auto volley recoil, and firearm/siege mount configurations. They retain proposal status and must be calibrated at materials/mounting stage. Ordinary reference ×1.00 / Trufula ×0.50 / Adamantite ×2.50 applies as an illustrative **STR/support factor only**, not automatic DEX or recoil change. Very heavy Adamantite cannons may require endgame STR specialism to wield *freely*; a rated carriage or battle saddle can transfer load and recoil differently. Trufula's propellant restriction is unchanged.
