# Mystaria Melee Weapon Catalogue — DESIGN DRAFT (not yet canon)

**Status:** PROPOSAL FOR AUTHOR REVIEW, created November 6, 2026. **Every numeric weapon-specific `F` and stat minimum, every individual assignment of STR/DEX/Either/Both, reach and coverage below is UNAPPROVED.** The approved shared framework is referenced, never silently changed. This draft is for *weapon shapes* only, not armor, material composition, quality, enchantments or prices.

## Author-approved production priority

1. Complete **five weapon-shape passes**: individual melee catalogue; melee Power and minimum-stat calibration; ranged individual profiles; numerical coverage and universal multi-target/horde resolution; physical mounts, handling and weapon-specific support interfaces.
2. **Immediately afterward develop ARMOR** (including shields, protective coverage, bodily armor, equipment-affected SPD, Resistance and armor penetration).
3. Only **after armor** return to the other weapon-crafting stages: material composition, equipment quality, modifications/enchantments, economy/pricing and remaining equipment categories such as tools, clothing, travel gear, specialist devices and accessories, in a separately approved order. **Weapons are not all equipment.** Existing approved prices, magic costs and systems remain unchanged.

Do not treat any of these *new numerical catalogue proposals* as canon without a new explicit author approval; the ordering instruction above **is approved**. Once the catalogue is approved, change this status in the reference and changelog.

## Existing approved melee system (not proposed)

- Handling **Light / Medium / Heavy**, Reach **Short / Medium / Long**, Coverage **Point / Narrow / Sweep / Wide Sweep / Line** are different fields; one does not determine another.
- `Power = (A × F)^2`, where `A` = user's **already-rebased effective STR**, **effective DEX**, **max(effective STR, effective DEX)** if Either, or **0.65 × (effective STR + effective DEX)** if Both **and both minima are satisfied**. Do not add the obsolete extra combat-only +10.
- **Light 1.00** is the approved baseline attack-rating reference, *not a universal mandatory F for every dagger or light item*. Approved older weapon baselines: **Gauntlets F 1.00, unarmed F 0.85** unless directly amended; these are not silently repriced.
- Piercing offers high armor bypass / lower injury tendency (relative **5/5 bypass, 1/5 injury**); Slashing favors injury and wider area (**1/5 bypass, 5/5 injury**); Blunt balances both (**3/5 and 3/5**) with no one-injury hard cap. **These are qualitative ratings, NOT % bypass or additional Power coefficients.**
- A weapon has a **primary attack mode** and only mechanically plausible **explicit alternates**; changing mode within one attack does not generate another action.
- One offhand weapon may choose **Attack OR Defense**, no free extra strike; an offhand attack doesn't grant an automatic second damage packet. Strong enough users may wield heavy forms with fewer hands, but size, DEX, geometry and actual safe control still matter. **150% one-hand / 200% dual-heavy thresholds remain working handling tests**, not fully universal canon for all grips.
- A Short grappler inside a Long weapon's functional space cannot be hit with its normal long strike until control is reestablished. Long-reach defender SPD / Short approacher SPD **<1.25** no additional reach gate, **1.25–<1.5** entry harder, **>=1.5** may deny unsupported direct rush if actually controlling the distance. Genuine Pressure defeats reach control, not weak enemy presence.
- Coverage permits only actually reachable enemies in an attack motion. **Line does not grant penetration**, and broad arcs do not multiply Power freely. Exact target counts and Power sharing across different targets are **pending**.
- Shields and armor ratings / penetration percentages are reserved for the **armor-first-after-shapes** pass, not preempted by this file.

## Author-approved changes in principle; numerical values still REVIEW ONLY

**Main secondary attack:** Weapons may provide a genuine secondary attack with **somewhat lower F than the primary**. The Greatsword's serious secondary is **Piercing / Point (blade thrust)**. Its blunt pommel strike is **not a meaningful heavy-weapon secondary** and must be **no more dangerous than a comparable unarmed strike**, even though the greatsword is massive. Do not evaluate such a pommel strike through the greatsword's Both-stat `A` and heavy F: evaluate an otherwise legal improvised pommel hit using **unarmed-equivalent Power as a ceiling** (unarmed approved F=0.85 with its appropriate STR base). This prevents the Two-Stat sum from secretly raising pommel damage above an ordinary punch. This applies in principle to other mundane pommel/haft/butt strikes unless the constructed head is a purpose-built striking weapon. Explicitly built double-headed weapons may have better secondary techniques once assessed separately.

**Asymmetric handling prerequisites:** **DEX-led melee equipment has a small physical STR floor** to carry, direct and recover its weapon. Compatible equipment-derived STR can satisfy this floor using the effective stat under existing item bonus rules. Both-stat weapons already require a STR and DEX minimum. **Pure STR-led melee weapons are NOT given a reciprocal DEX floor merely for being STR-led**. **STR-led RANGED weapons** should, however, have a small DEX handling requirement when aimed/operated, independently of primary STR scaling; the exact family/weapon minima belong to the future ranged chart. A weapon with Either scaling uses its qualifying STR mode without an additional DEX floor; its DEX-mode demands the stated small Support STR floor. Actual leverage, hand size and anatomy remain relevant.

**NEW UNAPPROVED numeric review defaults:** (a) a purpose-built alternative ordinary strike starts at `F_secondary=0.90*F_primary`, deliberately just a small reduction, rounded in this chart to three decimals; **0.90 is Quill's preferred PROPOSAL, not yet numeric canon**; (b) proposed DEX-mode STR floors vary from **6–18** by size/reach, shown explicitly in the register, **not approved**; (c) particularly awkward alternate actions and special multiheaded weapon profiles may demand individually tuned F rather than this blanket suggestion. **This is a provisional single-secondary display**, not authorization to delete physically valid further options in future finalization. All primary Fs, prerequisites and per-row coverage assignments remain pending author approval.


## Design interpretation of the proposed numbers

**F is one total attack-rating multiplier for the entire listed shape/mode**. Do **not** multiply F again by a separate global Heavy ×1.30 or Piercing ×0.90, Slashing ×1.10, Blunt ×1.00: those previous numbers are *not* approved, and double counting would distort the formula. To limit escalating quadratic gaps, the proposal keeps most Light F near 1, Medium near 1.1–1.2, Heavy near 1.2–1.35. Larger F is not automatically superior overall: reach, actual attack geometry, stat minima, attributes, timing, room and offhand options matter.

**Stat prerequisites shown are current post-rebase effective attributes**, not pre-rebase racial baseline + combat bonus. For Either, the minimum attaches to the attribute actually used to operate the weapon; do not freely pick a 5 STR character's huge DEX while ignoring the DEX minimum. For Both, **both minimums must be met**; if not, the Both-specific scaling formula is not available, and a separate underqualified-use ruling will be needed. Merely failing a stat minimum is not a license to invoke the better attribute without prerequisites. These requirements are *first-pass calibration only*, not automatic gates for all races, sizes or materials.

The primary attack mode alone defines its intended ordinary coverage. An alternate listed below is possible only if the build has the relevant point/edge/poll/spike; missing components invalidate that mode. **Superseded by the latest author ruling:** a weapon's primary attack and its genuine secondary should not default to identical F. The chart now uses a **proposed** secondary F of 0.90 times the primary pending specific approval; an emergency pommel strike remains capped by appropriate unarmed Power, not secondary F. Further built-in heads retain eligibility for individual-mode calibration. For point-vs-sweep advantage, use *geometry and later armor pass* rather than adding an unapproved damage-form coefficient.

## Proposed full weapon shape register

**The main chart has separate primary and secondary F fields, a prominent primary Coverage field, and DEX-mode Support STR floor; horizontal scrolling is expected. The secondary coefficients and numerical floors are proposals until user approval.**
**Main-chart display decision (author-approved):** Keep **Primary coverage** as a distinct prominent column directly beside primary damage form, visible alongside weapon Class, Reach, Scaling and F. Leave the catalogue wide, with horizontal scrolling where necessary, instead of dropping coverage from condensed listings. Each listed alternate attack still specifies its own coverage in the alternate column. Quantitative target counts/angles/ranges remain **UNRESOLVED** and must not be guessed. All per-weapon assignments and proposed F/stat values remain unapproved pending explicit catalogue review.

The `Stat profile` column uses approved STR / DEX / Either / Both labels; **all row values are proposals**. Suffixes "(poll)", "(tip)", "(beak)" etc mean construction-dependent alternates.

| ID | Weapon shape | Class | Reach | Scaling | Proposed Primary F | Primary form | **Primary coverage** | Secondary attack / coverage | **Proposed Secondary F** | Stat minimum | **DEX-mode Support STR floor** | Notes |
|---|---|---|---|---|---:|---|---|---|---:|---|---:|---|
| L-01 | Dagger | Light | Short | DEX | 1.00 | Piercing | **Point** | Slashing / Narrow | 0.900 | DEX 8 | 6 | Grapple and tight-space utility; not exclusive 1.00 baseline |
| L-02 | Stiletto | Light | Short | DEX | 1.01 | Piercing | **Point** | None | — | DEX 12 | 6 | Focused needle; little area coverage |
| L-03 | Short knife | Light | Short | Either | 0.97 | Slashing | **Narrow** | Piercing / Point | 0.873 | STR 7 or DEX 7 | 6 | Small versatile edge |
| L-04 | Cestus / knuckle weapon | Light | Short | STR | 1.00 | Blunt | **Narrow** | None | — | STR 9 | — | Preserve approved gauntlet F=1.00 reference where relevant |
| L-05 | Hand axe | Light | Short | STR | 1.05 | Slashing | **Sweep** | Blunt / Narrow (poll) | 0.945 | STR 12 | — | Small head-heavy cutter; alternate only with a real poll |
| L-06 | Light pick | Light | Short | STR | 1.05 | Piercing | **Point** | Blunt / Narrow (hammer poll) | 0.945 | STR 12 | — | Point pressure vs broad-cut weakness |
| L-07 | Short club | Light | Short | STR | 0.97 | Blunt | **Narrow** | None | — | STR 8 | — | Simple impact weapon |
| L-08 | Sickle | Light | Short | DEX | 1.00 | Slashing | **Narrow** | Piercing / Point (tip) | 0.900 | DEX 12 | 7 | Hook geometry contextual, no automatic disarm |
| M-01 | Arming sword | Medium | Medium | Either | 1.14 | Slashing | **Sweep** | Piercing / Point | 1.026 | STR 15 or DEX 15 | 10 | General-purpose cutting blade; emergency butt/hilt/pommel attack no stronger than comparable unarmed strike unless specially designed; other physically valid attack modes for later individual F calibration: Blunt / Narrow (pommel) |
| M-02 | Longsword | Medium | Medium | Both | 1.10 | Slashing | **Sweep** | Piercing / Point | 0.990 | STR 18 and DEX 18 | — | Both-stat scaling; alternate grip not extra attack; emergency butt/hilt/pommel attack no stronger than comparable unarmed strike unless specially designed; other physically valid attack modes for later individual F calibration: Blunt / Narrow (hilt) |
| M-03 | Rapier | Medium | Medium | DEX | 1.13 | Piercing | **Point** | Slashing / Narrow (edged design) | 1.017 | DEX 24 | 10 | Strong point-line precision, not broad cutting |
| M-04 | Sabre | Medium | Medium | DEX | 1.15 | Slashing | **Sweep** | Piercing / Point (usable tip) | 1.035 | DEX 20 | 12 | Cut-oriented curved blade |
| M-05 | Falchion | Medium | Medium | STR | 1.19 | Slashing | **Sweep** | Blunt / Narrow (pommel) | 1.071 | STR 22 | — | Wide cutting mass balanced by handling; emergency butt/hilt/pommel attack no stronger than comparable unarmed strike unless specially designed |
| M-06 | Mace / flanged mace | Medium | Medium | STR | 1.17 | Blunt | **Narrow** | Piercing / Point (purpose-built spike) | 1.053 | STR 20 | — | Flanges do not grant automatic armor bypass |
| M-07 | Warhammer | Medium | Medium | STR | 1.18 | Blunt | **Narrow** | Piercing / Point (beak) | 1.062 | STR 21 | — | Beak only when actually present |
| M-08 | War pick | Medium | Medium | STR | 1.17 | Piercing | **Point** | Blunt / Narrow (hammer face) | 1.053 | STR 22 | — | Concentrated point |
| M-09 | Battleaxe | Medium | Medium | STR | 1.20 | Slashing | **Sweep** | Blunt / Narrow (poll) | 1.080 | STR 23 | — | Handle and leverage matter |
| M-10 | Short spear | Medium | Medium | Either | 1.12 | Piercing | **Point** | Blunt / Narrow (butt) | 1.008 | STR 15 or DEX 15 | 12 | Medium reach; close grapple still needs space; emergency butt/hilt/pommel attack no stronger than comparable unarmed strike unless specially designed |
| M-11 | Quarterstaff | Medium | Medium | Both | 1.07 | Blunt | **Sweep** | Blunt / Narrow (butt thrust) | 0.963 | STR 13 and DEX 15 | — | No piercing without a genuine point; emergency butt/hilt/pommel attack no stronger than comparable unarmed strike unless specially designed |
| H-01 | Greatsword | Heavy | Long | Both | 1.27 | Slashing | **Wide Sweep** | Piercing / Point (blade thrust) | 1.143 | STR 35 and DEX 24 | — | Large arcs require room; pommel/blunt strike is at most unarmed-equivalent and not a full weapon secondary; emergency butt/hilt/pommel attack no stronger than comparable unarmed strike unless specially designed; other physically valid attack modes for later individual F calibration: Blunt / Narrow (pommel) |
| H-02 | Zweihander | Heavy | Long | Both | 1.29 | Slashing | **Wide Sweep** | Piercing / Point (blade thrust) | 1.161 | STR 40 and DEX 28 | — | Length and grip constrain cramped fights; pommel/blunt strike is at most unarmed-equivalent and not a full weapon secondary; emergency butt/hilt/pommel attack no stronger than comparable unarmed strike unless specially designed; other physically valid attack modes for later individual F calibration: Blunt / Narrow (guard) |
| H-03 | Greataxe | Heavy | Medium | STR | 1.34 | Slashing | **Wide Sweep** | Blunt / Narrow (poll) | 1.206 | STR 39 | — | Reach Medium despite Heavy mass |
| H-04 | Maul | Heavy | Medium | STR | 1.32 | Blunt | **Sweep** | None | — | STR 40 | — | Extreme blows can exceed ordinary injury states |
| H-05 | Great hammer | Heavy | Medium | STR | 1.35 | Blunt | **Sweep** | Piercing / Point (spiked side) | 1.215 | STR 42 | — | Crushing head; spike optional by build |
| H-06 | Poleaxe | Heavy | Long | Both | 1.26 | Piercing | **Point (top spike)** | Slashing / Sweep (axe) | 1.134 | STR 35 and DEX 24 | — | Three faces only if built with them; other physically valid attack modes for later individual F calibration: Blunt / Narrow (hammer) |
| H-07 | Halberd | Heavy | Long | Both | 1.25 | Slashing | **Sweep** | Piercing / Point (top spike) | 1.125 | STR 33 and DEX 25 | — | Reach control, multiple real heads; emergency butt/hilt/pommel attack no stronger than comparable unarmed strike unless specially designed; other physically valid attack modes for later individual F calibration: Blunt / Narrow (butt) |
| H-08 | Glaive | Heavy | Long | Both | 1.24 | Slashing | **Sweep** | Piercing / Point (pointed tip) | 1.116 | STR 30 and DEX 24 | — | Draw cuts, exposed in grapples |
| H-09 | Pike | Heavy | Long | Both | 1.20 | Piercing | **Line** | Blunt / Narrow (butt) | 1.080 | STR 28 and DEX 22 | — | Line is an attack path; not automatic penetration; emergency butt/hilt/pommel attack no stronger than comparable unarmed strike unless specially designed |
| H-10 | Long spear | Heavy | Long | Either | 1.20 | Piercing | **Point** | Blunt / Narrow (butt) | 1.080 | STR 27 or DEX 27 | 18 | Long reach not automatically Wide Sweep; emergency butt/hilt/pommel attack no stronger than comparable unarmed strike unless specially designed |
| H-11 | Lance | Heavy | Long | STR | 1.28 | Piercing | **Point** | Blunt / Narrow (butt) | 1.152 | STR 36 | — | Designed for supported charge; mounted charge Power separate; emergency butt/hilt/pommel attack no stronger than comparable unarmed strike unless specially designed |
| H-12 | Heavy flail | Heavy | Medium | STR | 1.30 | Blunt | **Sweep** | None | — | STR 42 | — | Articulation and recovery hazardous, not guaranteed shield bypass |

## Evaluation and mathematical fairness

1. **Comparative reference with 40 effective points in relevant primary stat:** F 1.00 gives Power `(40 × 1)^2 = 1600`; F 1.14 gives `2079.36`, about 30% above Light; F 1.34 gives `2872.96`, about 80% above Light. These are deliberately nontrivial differences under the quadratic formula and must be weighed against lost speed, requirements, one-hand flexibility and encounter reach.
2. **Both-stat weapons are inherently strong when attributes are balanced.** At STR 40 and DEX 40, `A=0.65(40+40)=52`, so proposed F 1.10 yields `(57.2)^2=3271.84` Power. This is about 104.5% above `1600` Light F 1.00 STR-only at 40, *even without a Heavy base bonus*. Thus Both-stat F in this draft is intentionally near or below similar one-stat shapes; this still may be overtuned and needs testing at multiple allocations before approval.
3. **Unequal investment:** With STR 60 DEX 20, Both A is also 52 and easily beats max(STR,DEX)=60 only if the Both F value is proportionately high; with STR 60 DEX 10, a Both weapon with STR 18 and DEX 18 fails eligibility. The balance cost of dual-stat investment and missing minima matters. Do not treat Both as a free 1.30x improvement in all builds.
4. **Gauntlets reference:** The gauntlet baseline is F 1.00, not the special Light-weapon ceiling; an ordinary gauntlet is NOT a purchase of extra turns, spells or shield defense. Unarmed F 0.85 remains unchanged.
5. **Size, strength and grips:** A Heavy greataxe may only have Medium Reach. A long pike may have less F than a greataxe while controlling approaches. A short knife can be more useful than a greatsword inside a successful grapple. Heavy handling is not synonymous with Long Reach.

### Suggested balancing checks before ratification

- Compare characters with balanced STR/DEX allocations at 20/20, 40/40 and 80/80 against specialists 40/10, 60/20 and 100/20 **under the same total attribute investment**, not just same STR. Test Both's 0.65 coefficient plus F for unintentionally dominant output.
- Check Light offhand Attack/Defense utility versus Medium generalist and Heavy reach and geometry; ensure there isn't a single best shape for every encounter.
- Compare Point, Narrow and Sweep weapon performance *without* armor first, then **defer** armor-specific bypass and material differences to the later dedicated armor stage.
- Test cramped grapples, open approaches with Model C reach control, statistically inferior hordes and equal-stat duelists.
- Check nonhumanoid anatomy, unusually long or short limbs, and Centaur/Drakyn mounting/handling; no new racial boosts invented.
- Keep qualitative blunt injury role without an automatic hard cap or secretly turning the 3/5 rating into 0.6× global Power.

## Melee shapes not conflated with the weapon-crafting pass

Axes, swords, spears and clubs define **shape**. Their final **construction material**, composite components, craftsmanship, wear, weighted balance, magical enhancements, explicit modifications, ammunition, durability and **Gems/Soul Strain** are separate systems. Resist pressure to assign every named alloy or quality rank its own new weapon shape. Gauntlet/shield armor specifics wait for armor; natural claws, tails, bites and race-specific limbs should eventually have appropriate natural attack profiles without automatically inheriting these handmade-weapon numbers.

## After approval: output of melee shape step

A canonical shape catalogue should contain one stable record for each design with ID, family, attack forms, legal coverage, effective-attribute rule, F, stat prerequisites, and any caveats. Unresolved numerical target counts and armor-vs-form interplay should remain marked for their designated passes. Shape catalogue **approval is a separate explicit author decision**; creating this proposal file does not grant it canon status.

## November 6, 2026 — Secondary F comparison and armor philosophy (REVIEW PROPOSAL)

The author suggests that secondary F be closer to **0.90 or 0.85** of primary, rather than the prior 0.95. **Quill recommends 0.90 for proper secondary strikes**: with the approved quadratic formula it yields **81% primary physical Power**, a substantial 19% reduction; 0.85 yields 72.25%, a 27.75% reduction. **Reserve 0.85 for exceptionally awkward or poor secondary weapon geometry, if the author later approves such cases.** The numeric ratios in this paragraph are NOT canon until explicitly adopted. A greatsword's pointed secondary blade thrust may be lethal against unarmored flesh but not specialize against plate like a purpose-made pike; that design distinction should involve distinct tip geometry, armor and the later armor-pass rules, not an invented piercing-bypass percentage today. Greatsword pommel remains unarmed-equivalent maximum, as already approved. The user has requested continuation to ranged weapon shapes while numerical secondary F remains on review.


## November 6, 2026 — REPLACEMENT MINIMA, AUTHOR-APPROVED TEST BASELINES (NOT FINAL)

These **supersede the earlier numerical minimums in the working table for all subsequent testing**, without ratifying final shape requirements. All figures are post-rebase **effective** stats and for ordinary reference materials. Existing shape/form/F/coverage entries are unaffected. For Either-stat items, the STR floor shown after the semicolon applies **only when using DEX mode**. Both requires both values.

| ID | Weapon | Replacement minimum |
|---|---|---|
| L-01 | Dagger | DEX 5; support STR 3 |
| L-02 | Stiletto | DEX 7; support STR 3 |
| L-03 | Short knife | STR 5 OR DEX 5; DEX-mode support STR 3 |
| L-04 | Cestus/knuckles | STR 4 |
| L-05 | Hand axe | STR 6 |
| L-06 | Light pick | STR 6 |
| L-07 | Short club | STR 3 |
| L-08 | Sickle | DEX 6; support STR 4 |
| M-01 | Arming sword | STR 9 OR DEX 9; DEX-mode support STR 5 |
| M-02 | Longsword | STR 12 AND DEX 10 |
| M-03 | Rapier | DEX 12; support STR 5 |
| M-04 | Sabre | DEX 11; support STR 6 |
| M-05 | Falchion | STR 12 |
| M-06 | Mace | STR 10 |
| M-07 | Warhammer | STR 11 |
| M-08 | War pick | STR 11 |
| M-09 | Battleaxe | STR 13 |
| M-10 | Short spear | STR 9 OR DEX 9; DEX-mode support STR 5 |
| M-11 | Quarterstaff | STR 8 AND DEX 8 |
| H-01 | Greatsword | STR 18 AND DEX 12 |
| H-02 | Zweihander | STR 21 AND DEX 13 |
| H-03 | Greataxe | STR 19 |
| H-04 | Maul | STR 19 |
| H-05 | Great hammer | STR 21 |
| H-06 | Poleaxe | STR 18 AND DEX 12 |
| H-07 | Halberd | STR 17 AND DEX 12 |
| H-08 | Glaive | STR 15 AND DEX 12 |
| H-09 | Pike | STR 14 AND DEX 11 |
| H-10 | Long spear | STR 13 OR DEX 13; DEX-mode support STR 8 |
| H-11 | Lance | STR 18; actual mounting/support geometry still applies |
| H-12 | Heavy flail | STR 22 |

**Test material factors (STR/support only):** conventional ×1.00; Trufula ×0.50; Adamantite ×2.50, round up. Do not universally multiply handling DEX or firearm recoil by material weight. Material approval and component composition are outstanding. Existing old requirements in the original register remain superseded **for testing only**, not operative final canon.
