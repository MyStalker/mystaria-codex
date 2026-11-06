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

## Design interpretation of the proposed numbers

**F is one total attack-rating multiplier for the entire listed shape/mode**. Do **not** multiply F again by a separate global Heavy ×1.30 or Piercing ×0.90, Slashing ×1.10, Blunt ×1.00: those previous numbers are *not* approved, and double counting would distort the formula. To limit escalating quadratic gaps, the proposal keeps most Light F near 1, Medium near 1.1–1.2, Heavy near 1.2–1.35. Larger F is not automatically superior overall: reach, actual attack geometry, stat minima, attributes, timing, room and offhand options matter.

**Stat prerequisites shown are current post-rebase effective attributes**, not pre-rebase racial baseline + combat bonus. For Either, the minimum attaches to the attribute actually used to operate the weapon; do not freely pick a 5 STR character's huge DEX while ignoring the DEX minimum. For Both, **both minimums must be met**; if not, the Both-specific scaling formula is not available, and a separate underqualified-use ruling will be needed. Merely failing a stat minimum is not a license to invoke the better attribute without prerequisites. These requirements are *first-pass calibration only*, not automatic gates for all races, sizes or materials.

The primary attack mode alone defines its intended ordinary coverage. An alternate listed below is possible only if the build has the relevant point/edge/poll/spike; missing components invalidate that mode. Alternate damage form uses the **same proposed shape F as the base starting test** (no invented stacked form multiplier); whether a materially different motion deserves a separate F is open. For point-vs-sweep advantage, use *geometry and later armor pass* rather than adding an unapproved damage-form coefficient.

## Proposed full weapon shape register

The `Stat profile` column uses approved STR / DEX / Either / Both labels; **all row values are proposals**. Suffixes "(poll)", "(tip)", "(beak)" etc mean construction-dependent alternates.

| ID | Shape | Class | Reach | Stat profile | Proposed minimum | Proposed F | Primary attack / Coverage | Alternative attack / Coverage | Distinguishing note |
|---|---|---|---|---|---|---:|---|---|---|
| L-01 | Dagger | Light | Short | DEX | DEX 8 | 1.00 | Piercing / Point | Slashing / Narrow | Grapple and tight-space utility; not exclusive 1.00 baseline |
| L-02 | Stiletto | Light | Short | DEX | DEX 12 | 1.01 | Piercing / Point | None | Focused needle; little area coverage |
| L-03 | Short knife | Light | Short | Either | STR 7 or DEX 7 | 0.97 | Slashing / Narrow | Piercing / Point | Small versatile edge |
| L-04 | Cestus / knuckle weapon | Light | Short | STR | STR 9 | 1.00 | Blunt / Narrow | None | Preserve approved gauntlet F=1.00 reference where relevant |
| L-05 | Hand axe | Light | Short | STR | STR 12 | 1.05 | Slashing / Sweep | Blunt / Narrow (poll) | Small head-heavy cutter; alternate only with a real poll |
| L-06 | Light pick | Light | Short | STR | STR 12 | 1.05 | Piercing / Point | Blunt / Narrow (hammer poll) | Point pressure vs broad-cut weakness |
| L-07 | Short club | Light | Short | STR | STR 8 | 0.97 | Blunt / Narrow | None | Simple impact weapon |
| L-08 | Sickle | Light | Short | DEX | DEX 12 | 1.00 | Slashing / Narrow | Piercing / Point (tip) | Hook geometry contextual, no automatic disarm |
| M-01 | Arming sword | Medium | Medium | Either | STR 15 or DEX 15 | 1.14 | Slashing / Sweep | Piercing / Point; Blunt / Narrow (pommel) | General-purpose cutting blade |
| M-02 | Longsword | Medium | Medium | Both | STR 18 and DEX 18 | 1.10 | Slashing / Sweep | Piercing / Point; Blunt / Narrow (hilt) | Both-stat scaling; alternate grip not extra attack |
| M-03 | Rapier | Medium | Medium | DEX | DEX 24 | 1.13 | Piercing / Point | Slashing / Narrow (edged design) | Strong point-line precision, not broad cutting |
| M-04 | Sabre | Medium | Medium | DEX | DEX 20 | 1.15 | Slashing / Sweep | Piercing / Point (usable tip) | Cut-oriented curved blade |
| M-05 | Falchion | Medium | Medium | STR | STR 22 | 1.19 | Slashing / Sweep | Blunt / Narrow (pommel) | Wide cutting mass balanced by handling |
| M-06 | Mace / flanged mace | Medium | Medium | STR | STR 20 | 1.17 | Blunt / Narrow | Piercing / Point (purpose-built spike) | Flanges do not grant automatic armor bypass |
| M-07 | Warhammer | Medium | Medium | STR | STR 21 | 1.18 | Blunt / Narrow | Piercing / Point (beak) | Beak only when actually present |
| M-08 | War pick | Medium | Medium | STR | STR 22 | 1.17 | Piercing / Point | Blunt / Narrow (hammer face) | Concentrated point |
| M-09 | Battleaxe | Medium | Medium | STR | STR 23 | 1.20 | Slashing / Sweep | Blunt / Narrow (poll) | Handle and leverage matter |
| M-10 | Short spear | Medium | Medium | Either | STR 15 or DEX 15 | 1.12 | Piercing / Point | Blunt / Narrow (butt) | Medium reach; close grapple still needs space |
| M-11 | Quarterstaff | Medium | Medium | Both | STR 13 and DEX 15 | 1.07 | Blunt / Sweep | Blunt / Narrow (butt thrust) | No piercing without a genuine point |
| H-01 | Greatsword | Heavy | Long | Both | STR 35 and DEX 24 | 1.27 | Slashing / Wide Sweep | Piercing / Point; Blunt / Narrow (pommel) | Large arcs require room |
| H-02 | Zweihander | Heavy | Long | Both | STR 40 and DEX 28 | 1.29 | Slashing / Wide Sweep | Piercing / Point; Blunt / Narrow (guard) | Length and grip constrain cramped fights |
| H-03 | Greataxe | Heavy | Medium | STR | STR 39 | 1.34 | Slashing / Wide Sweep | Blunt / Narrow (poll) | Reach Medium despite Heavy mass |
| H-04 | Maul | Heavy | Medium | STR | STR 40 | 1.32 | Blunt / Sweep | None | Extreme blows can exceed ordinary injury states |
| H-05 | Great hammer | Heavy | Medium | STR | STR 42 | 1.35 | Blunt / Sweep | Piercing / Point (spiked side) | Crushing head; spike optional by build |
| H-06 | Poleaxe | Heavy | Long | Both | STR 35 and DEX 24 | 1.26 | Piercing / Point (top spike) | Slashing / Sweep (axe); Blunt / Narrow (hammer) | Three faces only if built with them |
| H-07 | Halberd | Heavy | Long | Both | STR 33 and DEX 25 | 1.25 | Slashing / Sweep | Piercing / Point (top spike); Blunt / Narrow (butt) | Reach control, multiple real heads |
| H-08 | Glaive | Heavy | Long | Both | STR 30 and DEX 24 | 1.24 | Slashing / Sweep | Piercing / Point (pointed tip) | Draw cuts, exposed in grapples |
| H-09 | Pike | Heavy | Long | Both | STR 28 and DEX 22 | 1.20 | Piercing / Line | Blunt / Narrow (butt) | Line is an attack path; not automatic penetration |
| H-10 | Long spear | Heavy | Long | Either | STR 27 or DEX 27 | 1.20 | Piercing / Point | Blunt / Narrow (butt) | Long reach not automatically Wide Sweep |
| H-11 | Lance | Heavy | Long | STR | STR 36 | 1.28 | Piercing / Point | Blunt / Narrow (butt) | Designed for supported charge; mounted charge Power separate |
| H-12 | Heavy flail | Heavy | Medium | STR | STR 42 | 1.30 | Blunt / Sweep | None | Articulation and recovery hazardous, not guaranteed shield bypass |

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
