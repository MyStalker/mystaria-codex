# Mystaria — Modular Equipment Design Options

**STATUS: PROPOSAL / UNAPPROVED DETAILS ONLY.** This file is not an operative rulebook. Approved directions are in `07_Centaurs_and_Smithcraft.md` and `09_Equipment_and_Economy.md`. Keep all historical material identities, weapon baselines, five quality tiers, equipment affinity, and existing skill purchase gates unless expressly superseded.

## 1. Suggested passive runes (each family distinct; numeric effects need approval)

| Family | Proposal |
|---|---|
| Might | Increase effective STR within a shared item stat budget |
| Grace | Increase effective DEX within budget |
| Vigor | Increase effective END within budget |
| Insight | Increase effective INT within budget |
| Swiftness | Increase effective SPD within budget |
| Farreach | Extend applicable established magic range; no new targeting omniscience |
| Longsong | Add **+100% of base duration per rune rank**: ranks I–V produce 2×/3×/4×/5×/6× base duration; not 2^rank; exact upkeep interplay unresolved |
| Thrift | **Recommend 5%/10%/15%/20%/25% reduction in applicable MP activation costs** with minimum 1 MP and consistent rounding; flat −1/−2/−3/−4/−5 alternative risks making cheap powers effectively free |
| Conduit | Modest additional Channel Limit within approved ability restrictions; does not enlarge reservoirs |
| Steadfastness | Protect concentration from interruptions; no immunity |
| True Aim | Improve weapon precision, not prediction, and not automatic evasion negation |
| Guardian | Add a typed defensive ward or barrier (type and capacity specified at fabrication) |
| Quieting | Suppress equipment noise; does not make visible wearer invisible |
| Featherweight | Reduce equipment movement burden but not arbitrarily material inertia |
| Anchor | Resist disarming/forced displacement without granting extra attacks |
| Sentry | Alert user to defined intrusions; no omniscience |
| Wardshunt | Partial magic-type mitigation; only approved named threat type |
| Reservoir Link | Connect a compatible prayer reservoir as a source for explicitly permitted gem activation |

**Shared enchantment budget:** A quality's total numerical stat gains are limited by its established mixed/pure bonuses rather than multiplying per socket; duplicative family effects do not stack freely. Other runes and all activated gems have cumulative Soul Strain costs to be calibrated, without automatic SP creation. No free unrestricted spell access.

## 2. Proposed activated gem concepts (not approved mechanics)

Emberheart: ignite a limited fire burst; Dawnshield: brief directional ward; Lifebloom: limited restorative effect with recipient heal burn; Tideglass: water manipulation; Dreadstone: limited fear attempt opposed by Resistance; Stormpearl: short electrical discharge; Rootheart: localized binding; Gloamglass: area darkness. Final specific MP costs, Power, duration, area, resistance, and rank requirements all pending. These are item functions, not purchased Sorcery ranks.

## 3. Reservoir naming and charging

Short names: **Votive**, **Heartwell**, **Leywell**, **Vowcell**, **Soulfont**. Dramatic names: **Reliquary of the Unspoken Vow**, **Heart of the Faithful**, **Covenant Crucible**, **Vessel of a Thousand Prayers**. Suggested common term **Heartwell** and formal ceremonial term **Reliquary of the Unspoken Vow**.

Proposed fractional-charge tracking: full devotion restores `END/10 MP` for one active prayer turn; reluctant prayer `END/100 MP`; store fractional progress until whole MP accumulates. This is *recharge rate*, separate from quality-based storage capacity, discharge limits, compatible-affinity and explicit prayer action. One color per normal circuit. Maximum contributors, action length, rates and caps still need author approval.

## 4. Physical equipment design

**Weapon category proposal:** STR weapons use `(STR × form/material factor)^2` Power; DEX weapons use `(DEX × factor)^2`; simple 'either' weapons use `(max(STR,DEX) × factor)^2`; dual-stat weapons with BOTH stat requirements use `((STR+DEX) × balanced factor)^2`. The double-stat factor must be calibrated against equal total invested attributes and established weapon baselines. Any absolute 400-STR requirement is a gear ceiling target, not a character stat cap.

**Quality reduces required stats, not automatically raw Power:** proposed reduction Quality I–V **0/5/10/15/20%** from the physical design's STR and/or DEX handling requirement; these are not confirmed canon. Stronger forms, materials and heavy designs may have greater baseline Power multipliers, and also higher required attributes and SPD burden. Material does not grant free +stat enchantments.

**Proposed armor SPD burden:** `Penalty = base armor burden × max(0, 2 − effective STR / adjusted STR requirement)`, then effective SPD `max(1, SPD × (1 − penalty))`. At base burden 30%, STR requirement 30, and STR 30/45/60, the SPD penalty is 30%/15%/0%. Underlying armor may cover vulnerable gaps but never simply double-count armor rating at the same point. Work with `Defense Power = Resistance² + applicable Armor Rating²`; exact armor ratings still unresolved.

**Example speed burden and weapon form ideas:** Very light gear 5%, chain 15%, plate 30% base burden (all provisional). Dual scaling may be attractive at 60 STR +60 DEX versus single 105 STR +15 DEX when appropriate form factors are chosen; numeric playtesting needed to avoid disproportionately strong effects.

## 5. Shops, smith collaboration and inventory

**Option A, standardized vs bespoke:** Shimmer shops sell fair-price standardized goods including advanced items with stat requirements; Centaur smiths specialize in bespoke materials/fits and unusual combinations. Exceptional multi-skill items require cooperation or comprehensive personal mastery.

**Option B, Craft Intersection (recommended):** each extreme item requires evidenced contributions from appropriate Anvilcant disciplines: Orewhisper for exotic material, Oathsteel for enchantment quality, Socketwright for circuits, Hearthsong for stability, Thunderforge for firearms, and relevant Clockwright/Cogmarshal/Hostforge where applicable. A single multi-master smith or a team of master Centaurs and material sourcing can complete it. Shimmer goods are standardized and fair priced but cannot replicate all highest-end bespoke intersections through deity bypasses.

**Slot philosophy (proposal):** one outer armor chassis; optional light underlayer only for joints/gaps; one head, one neck, one arms/bracers, one hand/gloves, one feet/boots, one waist, two actively enchanted rings (more mundane rings may be worn), and held/accessible implements. One instance of a named spell cannot benefit simultaneously from multiple casting implements. Different sources of equipment magic add Soul Strain subject to quality budget and mutually exclusive families; distinct passive gear can remain modular.

**Open:** all numeric quality rating/penetration, armor coverage, weapon form multipliers, absolute STR/DEX requirements, single-vs-balanced scaling, momentum interaction, Soul Strain allocations, item slot count and capacity, prayer throughput and active rune mechanics.


## November 5, 2026 — Elemental passive contact rank I–V numerical design (PROPOSAL ONLY)

**Canon already chosen:** Model B / Conditional Contact Effect, not independent elemental damage packet and not mandatory physical Power conversion. **Everything numerical below is UNAPPROVED.**

### Procedure

1. Resolve existing hit/evasion and normal weapon Power versus appropriate Defense. A **complete dodge** produces no rune contact. If a barrier or shield stops the contact without a physical pathway to the bearer, adjudicate the struck object instead of automatically the bearer.
2. For actual relevant contact, identify the weapon's governing offensive attribute `A` (STR, DEX, or **STR+DEX on a qualifying balanced weapon**) and defender's **effective END**. For consistency with amplified balanced weapon scaling, the **proposed optional clamp** `A_contact = min(A, max(STR,DEX)×1.25)` applies only to passive runes, not physical balanced-weapon Power, preventing a dual-stat weapon from multiplying its free contact rider without limit. This clamp is not canon.
3. Calculate **Contact Pressure = A_contact / Elemental Resistance × Rune Rank Intensity × Material Contact Factor**. This is a *lightweight situational contact test*, NOT the usual quadratic attack Power ratio and cannot automatically overwrite normal injury results.
4. Match pressure bands below to elemental effects, then apply the rune rank cap and type-specific physical pathway. Damage from the rider advances **at most one additional injury state**, and only at ranks IV/V in this proposal. A rank I–III rune can never deal independent injury through this rider. An additional rider injury should not let a single strike jump beyond the normal injury-state maximum or bypass Hero/Legend Guard.
5. Repeated contact from the same elemental rune on the same target within an individual combat turn only worsens a status **once**. This anti-spam proposal matters especially for automatic passive effects and coordinated attacks. Multiple independent spell activations retain their own rules.

### Proposed numerical intensity and effect tiers

| Rank | Intensity coefficient | Cap / example |
|---|---:|---|
| I | 0.35 | Sensory signal or superficial physical-object change only |
| II | 0.55 | Small contact effect, 0 injury |
| III | 0.75 | Meaningful *minor* elemental condition under favorable contact; 0 injury |
| IV | 1.00 | Strong partial-element contact, up to **+1 injury** if pressure ≥1.50 |
| V | 1.25 | Entire weapon elemental (material bonus removed); up to **+1 injury** if pressure ≥1.50 |

| Contact Pressure | Proposed rider outcome |
|---|---|
| <0.50 | **Suppressed**; no appreciable target effect |
| 0.50–<1.00 | **Trace**; sensory/superficial effect only |
| 1.00–<1.50 | **Condition**; type-specific short-lived nuisance or impairment, no automatic injury |
| ≥1.50 | **Injury-eligible** only for rank IV/V; otherwise type-specific condition subject to rank limit |

If a rank I/II rune yields a high Contact Pressure due to weak Resistance, keep it within its rank's minor effect limit. Exact DEX/SPD effects of status, recovery timing and duration are unresolved; suggest one combat exchange for rank III, up to one turn for rank IV, more persistent effects only for rank V if established resisted conditions apply, but do **not** canonize these durations.

### Proposed elemental Resistance treatment

Start with natural **END**. Apply an expressly relevant established specific resistance/immunity first rather than inventing a second general defense. For numerical playtesting only, use:

| Threat-specific resistance | Elemental Resistance multiplier |
|---|---:|
| Vulnerable specifically to this element | ×0.75 END |
| No special resistance | ×1 END |
| Modest specific resistance | ×1.5 END |
| Strong specific resistance | ×3 END |
| Near-immunity / expressly immune | **Suppress this passive rider** unless existing source rule explicitly states otherwise |

The magic resistance factors above are **NOT** a replacement for existing specific resistance values, and cannot be applied as stackable flat END bonuses for unrelated threats. If a canonical spell/material defines another resistance interaction, that more-specific rule controls. Natural high END still matters for the contact rider.

### Proposed material pathways (no automatic transfer from a struck shield)

| Element | Example circumstance | Provisional Contact Factor |
|---|---|---:|
| Fire | Conductive metal armor in sustained/direct strike contact | ×1.25 |
| Fire | Proper insulated fire-resistant layer | ×0.5 or existing specified resistance |
| Ice | Chilled limb or vulnerable brittle components | ×1 ordinary; ×1.25 susceptible materials |
| Lightning | Conductive metal armor provides path to wearer | ×1.5 |
| Lightning | Proper glass/insulating armor | ×0.25 |
| Toxic/hex | Actual contamination transfer to target | ×1; otherwise 0 if sealed and no path |
| Water | Physically compatible transfer/wetness/pressure | ×1 |
| Air | Force reaches actual target through valid opening/contact | ×1 |

Do not double count separate vulnerability factors unless a specific source authorizes them. One material interaction factor per passive contact. These are abstract tabletop modifiers, not claims about literal real-world electrical or heat conduction of all metals.

### Type-specific rank progression sketches, all PROPOSALS

| Element | Ranks I–II | Rank III | Rank IV | Rank V |
|---|---|---|---|---|
| Fire | Heat/smolder, may char vulnerable material | Brief burn / heat armor, limited nuisance | Strong burn; eligible +1 injury at pressure ≥1.50 | Pure flame blade, material trait replaced; strongest passive burning |
| Ice | Condensation, small frost on hit | Brief localized chill/stiffness | Temporarily impair a limb or brittle susceptible armor; eligible +1 injury | Pure ice blade; freeze vulnerable material/limb more profoundly |
| Lightning | Static/discomfort | Brief muscle disruption via conductive path | Strong shock via metal; eligible +1 injury | Pure lightning weapon, material trait replaced; very poor vs insulators |
| Water | Dampen/disrupt surfaces | Brief fluid pressure or slipping opportunity | Stronger localized fluid force; eligible +1 injury | Pure water weapon; no automatic infinite water volume |
| Air | Puff/force sensation | Temporary loss of balance | Strong pressure or displacement, injury eligible | Pure wind weapon; not automatically a tornado or extra attack |
| Toxic/hex | Surface contamination with verified contact | Local contamination, risk to mana tools | Meaningful contamination, injury eligible only under a future specifically approved hex-injury rule | Pure toxic/hex form; material trait replaced; no automatic hex delirium |

**Important hex exception:** Even if Contact Pressure ≥1.50 at ranks IV/V, **do not automatically award an injury from toxic hex** until a dose/exposure rule exists. Current hex canon identifies pollution, magic-system instability and prolonged-exposure hex delirium, not an instant poison-wound scale. Store a narrative exposure and leave quantitative penalties unresolved. Respect Nymbrin alchemy's distinct hex production rules.

### Worked comparisons (not canon)

A wielder with **40 STR**, a fire rune rank IV (1.0), and a defender with **30 END** in ordinary heat-conductive plate (1.25 factor):
- Contact Pressure = 40/30 × 1.0 × 1.25 ≈ **1.67**, so at appropriate transmitted armor contact the **proposed +1 injury** is eligible even if physical Power fails to penetrate.
- If the defender additionally has **strong fire-specific resistance ×3**, Contact Pressure ≈ **0.56**, leaving **at most a trace**; near-immunity fully suppresses.
- A rank III shock rune (0.75) with A=40, END=30, conductive metal (×1.5) reaches **1.50**, but its rank III **no-injury cap** means a noticeable short-lived shock condition only. On an insulating glasslike shell (×0.25) the score is **0.25**, fully suppressed.

### Outstanding decisions

Whether exact elemental injury is added after normal physical injury or can substitute for it on a full elemental rank-V hit; whether passive contact is allowed on a glancing blow; balanced-weapon rune offensive-stat clamp; status duration and repeated-hit caps; exact % resistance modifiers where specific canon already defines protections; barriers/material contact; rune Soul Strain; rank-V effective weapon shape and how materials cease to matter; the full quantitative hex exposure system.
