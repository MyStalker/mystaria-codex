# Mystaria — Physical Shield Profiles and Material Handling

**CANON STATUS:** Main shield numerical package AUTHOR APPROVED November 13, 2026, through the author's direction to follow the Work shield decision report's recommendations. **Owning physical combat and interception rules:** [Combat, Endurance, and Shimmer Guard](22_Combat_Endurance_and_Shimmer_Guard.md). **Approved prices:** [Equipment and Economy](09_Equipment_and_Economy.md). [Canon Changelog](10_Canon_Changelog.md) records supersession.

**Source of approval:** `Mystaria_Shield_Decision_Report.md`, Work comparison against `main` at `57e1632`, containing 11 Hero races, 6 builds, every level 1–100, all five Qualities, Boughsteel/Trufula/Adamantite and sensitivity examples for other materials. The Work test report described **conditional physical interceptions and injury stages, NOT hit percentages or actual encounter win rates**. Its original source files are personal Library assets; the simulation scripts and CSV outputs were NOT part of the canon repository when this approval was recorded. Do not imply that they have been imported into GitHub.

## Approved conventional shield class and Quality Rating

| Quality | Light Boughsteel Rating | Medium Boughsteel Rating | Heavy Boughsteel Rating |
|---|---:|---:|---:|
| I | **18** | **24** | **31** |
| II | **32** | **43** | **55** |
| III | **53** | **71** | **90** |
| IV | **78** | **104** | **135** |
| V | **105** | **140** | **180** |

These are **Shield Ratings, not additional Armor Rating** on the wearer's body. **Shield Defense `D = Rating²`**, unaffected by END, torso AR, ordinary physical armor bypass and the direct body's defense term. A shield only protects when its real physical face can actually meet a legal hit, or when its actual edge qualifies for the narrower body-line obstruction rule below. Its mere possession is not a universal cover or passive Armor Rating bonus.

| Shield | QI Boughsteel minimum STR | QI minimum DEX | Guard-only body-line obstruction | Inherent shield SPD | Double Strike |
|---|---:|---:|---|---:|---|
| **Light** | **10** | **12** | **+0 categories** | **0%** | **Permitted** when qualified |
| **Medium** | **27** | **14** | **+1 category** on actual obstructed line | **0%** | **Permitted** when qualified |
| **Heavy** | **62** | **16** | **+1 category** on actual obstructed line | **0%** | **Forbidden**, despite ability to single bash |

**Material/Quality/handling calculation:** On an otherwise approved shield design, apply its **base QI class STR requirement × actual material support-STR factor × existing workmanship requirement discount × the already-approved sustained Equipment Load Synergy factor**, then **round the final STR requirement UP ONCE**. Calculate **base QI class DEX × existing workmanship requirement discount**, then **round that final DEX requirement UP ONCE**; do not apply the material STR factor to DEX. Retain the existing Quality I–V requirement-discount series **1.00/0.95/0.90/0.85/0.80**. The 75%-of-each-threshold eligibility, one largest equipment-shortfall SPD penalty across equipped items, wound recalculation, and minimum SPD retain their existing approved procedures. **There is no separate inherent shield speed multiplier to stack with actual armor mobility.** Item ownership, qualification and availability are distinct from level gates or starting-item grants.

For an unmodified Boughsteel **Quality V Heavy shield** with Heavy armor synergy 1.00, STR requirement = ceiling(62×0.80) = **50** and DEX requirement = ceiling(16×0.80) = **13**. The corresponding Trufula and Adamantite examples are **STR30** and **STR124**, respectively, with DEX13 in all three cases. Any legitimate armor-family synergy factor still applies when the loadout changes.

## Approved core material coefficients for actual legal shields

| Actual material | Shield Rating multiplier | Shield support STR multiplier | Quality V Heavy example |
|---|---:|---:|---:|
| **Boughsteel** | **×1.00** | **×1.00** | Rating180 / Heavy-synergy STR50 |
| **Trufula** | **×0.90** | **×0.60** | Rating162 / STR30 |
| **Adamantite** | **×1.15** | **×2.50** | Rating207 / STR124 |

**Derivation:** Multiply the reference Boughsteel Rating for that *class and Quality* by the applicable material Rating factor, then **round to nearest whole point with halves UP before squaring**. Apply no factor a second time to D. Reuse existing actual material hazards, material manufacture restrictions and access requirements; particularly Trufula's established flammability and Adamantite's material constraints. These multipliers are defensive shield factors, NOT a newly authorized global weapon F or body-armor AR change.

**Base Boughsteel shield impact contact thresholds (Power):**

| Quality | Light `D / 2D / 3D` | Medium `D / 2D / 3D` | Heavy `D / 2D / 3D` |
|---|---|---|---|
| I | 324 / 648 / 972 | 576 / 1,152 / 1,728 | 961 / 1,922 / 2,883 |
| II | 1,024 / 2,048 / 3,072 | 1,849 / 3,698 / 5,547 | 3,025 / 6,050 / 9,075 |
| III | 2,809 / 5,618 / 8,427 | 5,041 / 10,082 / 15,123 | 8,100 / 16,200 / 24,300 |
| IV | 6,084 / 12,168 / 18,252 | 10,816 / 21,632 / 32,448 | 18,225 / 36,450 / 54,675 |
| V | 11,025 / 22,050 / 33,075 | 19,600 / 39,200 / 58,800 | 32,400 / 64,800 / 97,200 |

These are **physical shield-contact attack-Power thresholds**, not damage against the body or guaranteed hit odds. Prepare the relevant material's own `D / 2D / 3D` on the character sheet to avoid repeated squaring at the table.

## Approved ordinary physical shield contact, durability and overflow

The existing durability track is **Intact (0 losses) → Dented (1) → Cracked (2) → Broken (3)**. Dented and Cracked remain **FULLY functional**. Physical actual-contact `P` compared against `D = Rating²` causes:
- `P < D`: **0 losses**.
- `D ≤ P < 2D`: **1 loss**.
- `2D ≤ P < 3D`: **2 losses**.
- `P ≥ 3D`: **3 losses**.

Apply no more losses than the shield has remaining, and never add an independent HP pool. The shield grants its full interception benefit while not Broken. Its **already approved only-on-break Power overflow** is resolved **only when a real shield-intercepted blow newly breaks it**. Let `R = 3 − losses already accumulated before this hit`. When the new blow breaks the shield, apply `P_body = max(0, P_attack − R × D)` *once* to the wearer's **torso** against the wearer's own effective END, real torso Armor Rating and the actual attack's standard body-armor penetration. If the hit does not break the shield, **zero attack Power passes through to the body**, even if the attack caused one or two shield losses. Existing approval of this formula/condition is preserved.

**Example:** Quality V Boughsteel Medium `Rating 140, D 19,600`. `P=45,000` takes 2 losses from Intact, **no torso overflow**. From Dented, `R=2`, the same hit breaks the shield and passes `max(0,45,000−39,200)=5,800` remaining Power toward ordinary torso defense. Actual contact from an incoming Double Strike or more than one opponent is resolved **per separate credible hit**, not merged into one combined larger blow. One facing cannot actively catch simultaneous opposite-front/rear threats.

## Approved shield positioning, Guard and tactical scope

- **Light Guard** grants **no automatic hit-difficulty category shift**, but still allows a real active interception on a physically possible line. **Medium and Heavy Guard** increase hit difficulty **by one category** only against an otherwise open body-target attack line genuinely obstructed by the shield's physical edge; apply this **once**. Heavy's larger surface may physically obstruct more distinct lines, but where Medium also obstructs the same line, both give exactly **+1**, NOT Heavy +2. No universal shield-facing arc, automatic 360° dodge, free category bump to uncovered limbs, or separate percentage-of-body coverage has been approved.
- A shot that actually contacts the shield is resolved as a **shield interception/contact** and not additionally as a separate body-target obstruction penalty. A true wall/cover may physically block the path entirely; do not count the same shield surface as both ordinary independent cover and new shield obstruction. An unobstructed flank, gap or limb gains **no shield category bonus**.
- **Guard (all shields):** One normal main-hand attack OR one **single** approved `STR F1.05` Narrow Bludgeoning shield bash as the attack action; eligible deliberate active block and shield positioning remain available. The ordinary 25% Bludgeoning body-armor bypass applies to a real bash hit, not to an incoming shield contact. There is no extra free bash on every block.
- **Deflect (all shields):** Voluntarily forgo **deliberate active block and intentional body-line obstruction** to gain the already-approved normal credible offhand Defense response, which can counter **one qualifying incoming Pressure Point** when physically addressable. An incidental physical shield collision is still a real object interaction, not a deliberate active intercept.
- **Double Strike (Light/Medium only):** Two independently eligible attacks in one action, one weapon and one shield bash, each **60% of its own final physical Power**, one real target per hand, the existing single self-imposed PP through start of next turn, and **no deliberate active shield block, shield-body obstruction, Deflect or regular offhand Attack/Defense benefit**. **Heavy shields may never Double Strike**, but can perform one full-Power normal F1.05 bash under eligible Guard. Heavy-armored fighters remain eligible for ordinary Double Strike with two genuinely separate legal weapons if they are not wielding a Heavy shield.
- Active shield interceptions still require an **aware, qualified, physically credible defense under net 3 PP**. The existing trapped, Extreme Pressure, real attack geometry, actual reach, attention to specific direction, and synchronized two-opponent opposite-angle rules are not overwritten. The report did **not** establish a new reaction-action economy, interception interrupt timing or universal projectile auto-parry.

**Shield bash material and Quality rule boundary:** Keep the **already-approved plain F1.05** (STR-led, Bludgeoning Narrow) as the **ordinary shield bash baseline across conventional shield materials and Qualities**. Do NOT automatically import material-specific *weapon* F bonuses, workmanship bash-F bonuses, special bash-head profiles or an extra attack from the shield's defensive Rating unless separately authorized by its actual offensive construction. Existing independently approved offensive item effects, if actually legal and operative, still apply under their own rules.

## Conditional special-material physical shield references (APPROVED ONLY FOR INDEPENDENTLY LEGAL DESIGNS)

The author's adoption of the Work report supports the following **conditional Rating/support-STR reference factors** for a shield made with a legitimate approved load-bearing face and qualifying actual supporting construction. This approval **does NOT authorize constructing an otherwise excluded composite, applying a dedicated worn-suit ability to a shield, or making an ordinary Quality I–IV Celestite item**. Until a particular design's manufacture and item legality are independently approved, these coefficients are **reference/calibration inputs, not a purchasable new product**.

| Material / independently valid face-and-frame example | Rating factor | Support STR factor |
|---|---:|---:|
| Nullporcelain | ×0.35 | ×0.80 |
| Skyvein | ×0.55 | ×0.70 |
| Reprise Bronze | ×0.90 | ×1.00 |
| Oathsilver | ×0.80 | ×0.85 |
| Bellcopper | ×1.00 | ×1.35 |
| Hearthiron | ×0.90 | ×1.35 |
| Thornspring | ×0.85 | ×0.75 |
| Glassweave | ×1.00 | ×1.00 |
| Celestite **(Quality V only, divine-creation requirements remain)** | ×1.20 | ×1.80 |
| Trufula frame, Boughsteel load-bearing face | ×1.00 | ×0.85 |
| Trufula frame, Adamantite load-bearing face | ×1.10 | ×1.75 |
| Glassweave face, Boughsteel frame | ×1.00 | ×1.00 |
| Nullporcelain inset, Boughsteel face | ×1.00 | ×1.00 |

These are **one integrated design's total shield coefficients**, not component multipliers that may be stacked. The declared actual **load-bearing face** determines physical shield-contact and ceramic breakage; a smaller decorative/anti-magic inset does **not** turn a Boughsteel face into a ceramic shatter shield. A genuine separately approved shield may inherit actual specific material dangers; it does **not** automatically acquire armor-only powers, magical protection, anti-magic contact effects, burst mobility or composite suit abilities that require a differently constructed item. Celestite remains extremely restricted and no ordinary catalogue availability is implied.

### Ceramic load-bearing shield shatter (approved shield-only application if design is legal)

For an independently permitted shield whose **actual load-bearing face is ceramic** (e.g. eligible all-Glassweave or Nullporcelain face), use its own `D=Shield Rating²`, but **replace** ordinary contact durability-loss brackets with the Work-tested shield-specific brittle thresholds:

- `P ≤ 0.75D`: **0 shield condition losses**.
- `0.75D < P ≤ 1.75D`: **2 shield condition losses**.
- `P > 1.75D`: **3 shield condition losses** (immediate break if intact).
  
The existing **Intact/Dented/Cracked full-function until Broken/Shattered** principle still applies to the shield's own protection. Broken/Shattered stops providing its own shield protective benefits until actual repair; wearer healing never repairs the item. If a ceramic threshold triggers breaking while `P < R×D`, the **already-approved torso overflow formula floors at zero**; shattering does not create additional attack Power. **These shield-contact thresholds are NOT new body-armor shatter triggers**: keep existing approved Solid/Devastating contact-injury based shattering for ceramic wearable armor.

## Evidence, unresolved questions, and scope limits

**Work report conditional break percentages (Boughsteel, successful declared shield interception in model cohort, not hit odds):**
- One-handed: Light 22.9%, Medium 9.2%, Heavy 3.0%.
- Two-handed: Light 39.4%, Medium 16.3%, Heavy 8.4%.
- Two-contact Double Strike on shield line: Light 26.1%, Medium 7.5%, Heavy 1.1%.
- Ranged: Light 20.1%, Medium 7.0%, Heavy 1.3%.

The 11-race × 6-build × 1–100-level Work sweep used benchmark Quality acquisition schedules and an **illustrative early arrow Power** where the ordinary ranged catalogue still lacked one. Opponent gear cohorts sometimes differed between shield classes because qualification changes which examples can wield the gear. These conditional fixture percentages are **not universal per-attack break probabilities**, full encounter win rates, automatic ranged-intercept timing or a randomized character-balance certificate.

**OUTSTANDING AND NOT NEW CANON:**
1. Junk-condition shield eligibility, Junk pricing application to any specific shield product, hit/wear adjustments and explicit implications of direct attacks on hands, strap fastenings or shield's structural vulnerabilities.
2. Shield manufacturing workloads (Work's 8/16/24 work-hour Light/Medium/Heavy suggestion is **OPTIONAL PROPOSAL**, not approved by shield combat test), actual mundane repairs, recovery amount per repair, equipment restoration and salvage, material costs and labor. Maintain the existing author-deferred crafting economy docket.
3. Exact reactive/interruption timing for active shield defense against shots, extreme angles and simultaneous sequencing. Do not assert free post-declaration projectile retro-blocking; ordinary shot/contact conditions remain subject to genuine physically plausible already approved timing.
4. Special physical/elemental integrity mechanisms: Acid, actual Fire and Lightning effects, ceramics exposed to unrelated magical energy, and actual material-specific anti-magic interactions require their own independent approved rule. Mere Shield Defense Rating does not create generic energy/psychic protection.
5. Construction recipes and permission for individual special-material shield faces/frames, actual overall mass and fabrication compatibility; prevent special suit-only mechanics from migrating onto tiny shields. Most optional material rows are reference inputs until item design legally exists.
6. Shield-specific bash-head/enchantment/Quality F scaling beyond existing plain F1.05; special launched-projectile weapon figures where ordinary ranged catalogue is still incomplete; actual hit probabilities, action-economy victory rates, exhaustive enemies and broad material balance.
7. Real reuse of Work's regression scripts: scripts/data are in a separate Library archive and **not confirmed copied into GitHub**. They should eventually be put under a maintainable test directory if the user authorizes code changes and repository safeguards permit.

**Do not silently change any approved weapon F, armor AR/MR/SPD, race stats, movement, hit-category thresholds, actual Pressure rules, weapon costs, shield price relationships, or other pre-existing system.** The older proposed QV shields 160/225/270 and earlier flat 30/50/75 are SUPERSEDED by this new approved Rating ladder.