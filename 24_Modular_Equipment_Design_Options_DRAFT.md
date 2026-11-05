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


## November 5, 2026 — Elemental contact, Loom prices and integration tests (PROPOSAL ONLY)

### Command Loom Gem prices and mobile hardware (not approved)

| Cogmarshal rank required to craft/operate | Loom quality | Gem price proposal | Historical proposed total CP with Loom |
|---|---|---:|---:|
| I | I | 12 | 2 |
| II | II | 28 | 4 |
| III | III | 55 | 6 |
| IV | IV | 90 | 8 |
| V | V | 140 | 12 |

Loom is carried as a compact **remote control** rather than a fixed engine. Level gates, physical control methods, mana consumption, reliable radio/light/tether command range, remote interference and individual construct maintenance still need review. It cannot think for its operator, grant Cogmarshal ranks, or create additional actions beyond already approved mechanics. Gem prices buy the Loom only, not an army of constructs or fuel.

### Three distinct passive elemental damage-resolution options

**A: Dual Power Packet**. Once a weapon strike physically contacts armor, calculate normal physical Power vs applicable physical Defense, and calculate a separate lower elemental Power packet against natural Resistance and type-specific magical protection. Ordinary armor is not assumed to block every elemental contact; fire or conductive lightning may reach the wearer when the physical edge cannot pierce. Elemental packet Power per rank, injury thresholds and whether contacting armor counts are unresolved. Strong type-specific resistance can negate the packet. Pros: matches Power/Resistance engine; cons: extra per-hit calculation.

**B: Conditional Contact Rider (recommended for simplicity).** A physically connected strike, even when physical injury is superficial, applies a specific small elemental rider. At ranks I–IV, its direct injury advancement is capped at at most one state, and magical/specific resistance can reduce it to mere sensation or negate it entirely; many lower-rank contacts should leave only superficial effects. The rider only works when the attack makes meaningful contact, not after a complete dodge. Fire: heat/burn, ice: chilled limb/brittle eligible armor, water: wetness/pressure, lightning: conductive-vs-insulating armor, air: brief destabilizing force, toxic: hex contamination with separate later-defined systemic effects. Pros: one fast GM judgement; cons: must establish defensible type-specific thresholds and avoid guaranteed injury on every contact.

**C: Damage Conversion**. Convert a bounded share of ordinary weapon Power into elemental Power; split vs physical coverage and elemental protection. At ranks I–IV retain mostly physical Power; at rank V the weapon becomes wholly elemental and forfeits original material benefits. Pros: strong thematic consistency; cons: can accidentally weaken weapons and has complex mixed resistance resolution.

**Rank philosophy shared across options:** I faint contact, II clear but still weak effect, III meaningful specialized interaction, IV significant partial-element strike, V complete elemental form; the rank V item's **original material property/bonus is replaced**, not added. Exact damage Power shares, Magic/Specific Resistance calculations, rank-V physical handling and object persistence are unapproved. All nonactivated passive effects should be less potent than analogous Sorcery gem activations. No passive effect follows a target who fully evades.

### Magic-specific interactions (not approved numerical values)

- **Fire:** heat may affect conductive armor underneath even when the edge fails to puncture, but magic resistance to fire suppresses it.
- **Ice:** chill/freeze an exposed limb or degrade eligible brittle material after sufficient contact; immunity/ice-resistant material matters.
- **Water:** impact or conduction effects only if consistent with valid water mechanisms, not limitless free water creation.
- **Lightning:** effective against conductive armor, weaker against suitable glass/insulating armor; equipment material/coverage decides.
- **Air:** brief displacement/pressure effect, constrained by resistance and environmental anchoring.
- **Toxic/hex:** contact contamination can build toward the already established hex pollution effects such as hex delirium, magical instability and other delayed consequences. **Numerical doses, duration, resistance, armor passage, rates and side-effects are RESERVED for future explicit design**. Do not mistake this for free approved Nymbrin alchemy or assume every contact causes delirium.

### Quality handling tests

**New current rule:** base physical stat requirement × (1 − quality percentage) − 5 points per individually required attribute, minimum 1. Quality I through V percent reduction 0%, 5%, 10%, 15%, 20%. So a base requirement of 100 is 95 at Quality I, 75 at Quality V. A balanced weapon that normally requires 100 STR *and* 100 DEX needs 75 in **each** at Quality V. Requirement rounding still needs approval.

### Armor Speed penalty examples

Testing only: base chain burden 15% requiring 20 STR; base plate burden 30% requiring 30 STR; wearing both when covering distinct areas means add remaining penalties after independent Strength relief. At STR 30, chain residual 7.5%, plate 30%, combined 37.5%. At STR 60 both can become 0%. Speed floor 1, penetration/coverage and other actual physical burdens remain separate.

### First balance pass agenda

1. Use comparative specialization builds with equal stat-point investment, including STR 400 tests and dual-attribute balanced weapons, preserving unarmed/dagger baselines.
2. Set actual Armor Ratings per material, physical form, and I–V craftsmanship before tuning Speed burdens.
3. Establish enchantment's shared stat-boost budget, per-rune/per-gem cumulative Soul Strain and useful spell frequency considering dual-mode Thrift and extended Longsong.
4. Set a chosen passive elemental contact procedure without defeating END or special magic Resistance.
5. Fix Cogmarshal Command Loom portable control limitations and activated spell gem imprint costs/knowledge requirements.
