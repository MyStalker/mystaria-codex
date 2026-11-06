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


## November 5, 2026 — Elemental Magnitude and elemental status design (PROPOSAL ONLY)

**APPROVED SOURCE DIRECTIONS:** 'Contact Pressure' is renamed **Elemental Magnitude** for energy attacks and especially Sorcery, while retaining an attack-type-appropriate source of Power. Three Elemental Status severity ranks exist conceptually; rank III passive element runes are allowed to cause resisted status. Energy status can weaken its own element Resistance. Wetness increases lightning transfer with real conductive pathways. All specific numbers below are new suggestions and remain **UNAPPROVED**.

### Suggested universal energy metadata

For applicable magic or weapon effect, list: (1) energy/element category, (2) original Power/skill/MP source, (3) **Elemental Magnitude** and delivery route, (4) applicable **Specific Resistance** and material transfer, (5) Elemental Status, (6) recovery and continuing cost. Do not apply elemental formulas to every healing/psychic/non-energy effect. Preserve approved Incantations, alterations and prerequisites. Existing passive-rune draft 'Contact Pressure' arithmetic should henceforth be **read as Elemental Magnitude** where applicable, **not as a second new stat**.

Passive weapon test (only a numerical PROPOSAL): `EM = (relevant offensive attribute / type-adjusted Resistance) × rune intensity × applicable contact factor`. Source for Sorcery must instead derive from the **actual spell's approved INT/MP scaling**, which has not been numerically specified for all Sorceries. These are different delivery/source formulas within shared elemental outcome conventions.

Suggested EM status thresholds: **<0.5 negligible**, **0.5–<1 trace**, **1–<1.5 condition rank 1**, **1.5–<2.25 condition rank 2**, **≥2.25 condition rank 3**. Source/rune rank caps still matter: passive rune I–II no lasting status, rank III may produce status rank 1, rune IV up to status rank 2, rune V up to status rank 3. Higher-output activated Sorcery effects could attain higher status tiers under their own balancing rules. Do not confuse passive rune I–V with *Elemental Status* 1–3. Passive rune IV/V independent injury remains maximum +1 from the contact rider per connected attack, and for hex injury waits for the separate hex system.

### Status-specific susceptibility proposal

A successful elemental status weakens **only its own type-specific Resistance** by **10% / 20% / 30%** for severity rank 1/2/3. This applies when *later attacks* of that type test EM, including legitimate activated spells; **never lower the END stat globally** and do not alter unrelated elements. The debuff is tied to the current highest severity, not an unlimited stack of multiple status instances. A second valid later contact of equal/higher EM may intensify one status rank if source rank and resistance permit; max 3; limit status advancement to once per combat round per element and do not make a failed hit or blocked pathway count. Mitigation and recovery are evaluated against protected **pre-status Resistance** when determining whether a new hit can newly worsen status to avoid an automatic unbreakable positive-feedback loop. Strong specific elemental resistance still strongly mitigates and near-immunity can be challenged only by an exceptional source/overwhelming appropriate EM (numeric bypass threshold not fixed).

### Suggested distinct elemental conditions (severity 1/2/3)

| Element | Rank 1 condition | Rank 2 condition | Rank 3 condition |
|---|---|---|---|
| Fire, **Burning** | Smoldering: one **burn tick every third round** if severity/Resistance supports it | Burning: burn tick **every other round** | Engulfed: burn tick **every round** |
| Ice, **Frozen** | Freeze one limb / localized joint | Immobilize roughly half the body | Freeze entire body, temporary but extreme control |
| Lightning, **Shocked** | One-round stun-like interruption of a task/action | One-round stun plus temporary malfunction of conductive gear | One-round stun plus strong interruption of active electrical systems; never automatic 3-round lockdown |
| Water, **Drenched / Surged** | Knock prone if unbraced | Knock prone + push about **5 ft** | Knock prone + push about **15 ft** |
| Air, **Buffeted** | Push about **5 ft**, usually no prone | Push **15 ft** | Push **30 ft**; more displacement than water but less direct physical harm |
| Toxic/Hex, **Hexbound** | Candidate reduced stat or magical disturbance | Larger stat penalty, contaminated equipment | Severe but temporary stat penalty and instability; **not instant hex delirium** |

Fire **burn tick suggestion**: A tick is a periodic attempted elemental injury/condition, **not automatically one injury state**: require active burning, viable fuel/path and a resistance test. At severity 1/2, ticks are usually superficial; injury advancement eligibility is restricted by appropriate effective magnitude/source rank and existing injury-state cap. No tick may bypass Hero/Legend Guard. Successful fire suppression ends status even if the scheduled tick has not occurred; additional fire hits do not multiply tick counts. Otherwise a rank III passive sword could kill heavily armored foes through guaranteed uncounterable damage.

Ice duration suggestion: **Full-body freeze at severity 3** lasts `max(1,min(3,ceil(90 / effective END)))` rounds if not broken early, while rank 1/2 freeze lasts at most that long, often shorter. At END 15 -> 3 rounds; END 30 -> 3 rounds; END 60 -> 2 rounds; END 90+ -> 1 round. Specialized ice resistance, heat, forceful rescue, external magic, breaking the ice, and appropriate physical capabilities may shorten duration. **Do not automatically allow a rune III to fully freeze**, because its status tier is capped at 1. The immobilized character's armor/END/Guard remain relevant, and displacement or ongoing violence can break the ice.

Lightning one-round stun suggestion: On a **qualifying hit and type-specific Resistance failure**, interfere with **the next intended action** for at most one combat round. Additional shocks within that window refresh neither duration nor add new stun rounds. For severe ranks, add equipment disruption rather than extra stun duration. Do not make insulated targets or native lightning-resistant Drakyn trivially helpless; no automatic equal-power stun lock.

Water/air suggested displacement must require a physical force pathway and scale against END and anchoring, mass, terrain, restraints and relevant elements; the listed distances are **unbraced humanoid maximum reference examples, not automatic movement**. Air specializes in launching further but less directly injuring. Water can be better at knocking prone, saturating armor or creating exposed wetness; being wet has a **proposed +25% lightning contact transfer factor** only where an effective conductive path reaches the target; insulated suits and barriers can negate the effect. Consequential falling or hazardous terrain damage uses existing physical combat rules, not an extra free elemental injury.

### Toxic/hex status alternatives

**A. Focused Attribute Suppression (recommend):** The target's highest usable *effective* stat (or one stat specified by valid toxin design) suffers temporary **−5%/−10%/−15%** at statuses 1/2/3. This does **not** reduce *base attributes* or delete Hero progression; minimum final attribute 1. End of exposure and conventional/magical purification can restore stats. Strong anti-hex resistances protect. Fixed one-stat suppression protects against universal stacking and creates tactical choices.

**B. Mana System Corruption:** Rather than direct stat penalties, hex causes fluctuating Channel Limit, Leywell/gem reliability, mana expenditure and strain. This mirrors Nymbrin Haze lore but risks complex spellcasting bookkeeping.

**C. General Debilitation:** Hex applies a smaller global effective-stat penalty **−2%/−5%/−8%** at statuses 1/2/3. The tradeoff is greater intuitive breadth but it can overshadow ordinary injury states, stack unpleasantly with existing wound penalties and hurt every build the same way.

**Important canon separation:** Nymbrin hex is accumulated magical pollution and prolonged exposure can cause **hex delirium**, with paranoia, perception distortion and unreliable magical control. No instant madness, automatic permanent mutation, or universal dose-free injury from passive rune contact. Elemental status is a transient combat-layer proposal; any actual long-term hex burden/exposure mechanics must be separately approved in the Nymbrin dossier.

### Design checks still required

- A status-level resistance reduction is helpful without letting each hit escalate exponentially; source rank caps, 1 advancement/round and recovery must resist stun/freeze/burn-lock.
- Balancing the rank-V pure-element weapon: **keep appropriate ordinary weapon Power plus bounded passive rider while sacrificing the original material's special property**, and evaluate any physical reach/weight change separately.
- No existing Sorcery damage numbers are invented, no gem price/MP/SP changes, no elemental absolute immunities (even native fire Drakyn have near-immunity), and no construct builds are canonized automatically.

### Clockwork follow-up docket — revisit after the remaining crafting rules

| Named family | Intended niche | Material-to-stat illustration (not a stat block) | Possible integrations |
|---|---|---|---|
| **Windling** | Tiny aerial/hovering messenger, observation, scouting | Lightweight/frame materials primarily set SPD/END and flight load | Leywell power, observation passive rune, programmed alert/signal gem |
| **Quickstep** | Agile ground/climbing scout, porter | Light frame and elastic joints shape SPD/DEX/STR | Leywell, mobility/stealth runes, control circuit |
| **Iron Servitor** | Workhorse laborer and combat machine | Structural material and gears set STR/END and working speed | Leywell, stat-modifying passive runes, sorcery gem for one programmed action |
| **Bulwark** | Heavy shielded defensive machine | Dense armor materials increase END/mass but reduce SPD | Leywell, wards, defensive spell crystal |
| **Gearsteed** | Transport, cavalry mount, hauling | Drive train and frame set STR, SPD, load capacity | Leywell, propulsion and protection runes, transport control |
| **Siege Engine** | Heavy attack/large construction platform | Frame/mount/ammunition establish STR/END/movement and intrinsic firearm/artillery damage | Multiple materials, one/more Leywells, heavy Sorcery gem, Cogmarshal Loom coordination |

Each construct needs **material-based STR/DEX/END/INT/SPD values**, dimensions/mass, material weaknesses (including Trufula flame hazard), quality/reliability, Clockwright fabrication gates, relevant Orewhisper/Hostforge/Oathsteel/Socketwright contributions under Mastery Intersection, hardware/controller, compatible Leywell capacity/discharge, runes and sorcery crystal, cost in Gems/materials, MP per combat turn vs maintenance, and operational behavior when out of controller range. **None of these numeric construct sheets or recipes has been approved.** Prior approximate examples: scout 1 MP/turn, Iron Servitor 2, Bulwark 4, siege ≥8; Quickstep/Gearsteed rates unspecified.

## November 5, 2026 — Squad command design questions (PROPOSAL)

**World name:** Mystaria. Cindara was a mistaken world label.

**Elemental status proposals:** Lightning I cancels the current action, next turn movement remains possible; II prevents action only; III makes the target drop held objects and become Trapped for evasion. Never chain stun from additional shocks. Water II/III pushes 5/15 m and emphasizes knocking prone. Air II/III launches 10/30 m, favors displacement over immediate damage. All distances require Resistance, mass, terrain and anchoring assessment. Hex specializes in reducing creature/Leywell MP, interrupting magical equipment, and lightly improving shield interaction. Serious effects after depletion require strong Elemental Magnitude, not merely zero MP. Timings, rates, thresholds are all unresolved.

**Group action prototype (not canon):** One commander action orders one squad to shoot, relocate, shield an ally, or suppress an area. Group members perform one coordinated effect; additional bodies improve available formation, coverage and reliability without granting an independent full attack to each. Suppressive fire primarily increases pressure; a potential attack against a Trapped foe is a prepared conditional resolution using that squad's existing action budget, not a free fresh full action. Multiple squads need explicit commander actions or a well-bounded order capacity. No independent per-unit wound tracks by default: model squads through shared integrity/cohesion and individual casualties when dramatically relevant. A single boss construct can retain its own wound progression. Current Command Points 1/2/3/4/6 or 2/4/6/8/12 with Loom are older UNAPPROVED proposals.

**Open choices:** A single command per action vs command capacity bundled in one action; whether a group can carry out a standing defensive instruction without spending full new actions; shared squad integrity versus threshold casualties; unit count as coverage rather than additive Power; free suppression reaction limit, commander interruptions and line-of-control; mixed-material stats and joint upkeep; remote actions while the commander attacks independently.

## November 6, 2026 — Approved Cogmarshal decisions and remaining numerical proposals

**Author-approved supersession:** The command language is **Cogsong**, not Cogchant or other working names. Command Looms are **mandatory**, not optional boosters. Previous example native Cogmarshal CP 1/2/3/4/6 and Loom-doubled CP 2/4/6/8/12 do **not** constitute approved progression and the no-Loom capacity model is superseded. The only fixed CP relationships now approved are **1 CP per 4 Windlings** and **+1 CP to reinforce a standard four-machine non-Windling squad to 5–8**. A standard non-Windling homogeneous squad is **four machines**; more than eight should form another squad. Simple nonoffensive standing orders persist until complete; each new attack consumes a new meaningful command action, not a permanent automated firing loop. Windlings uniquely form arbitrarily large swarms subject to total CP and normal commanded-action limits, countering single-target snipers by target saturation; do not give them independent full injury-state/attack actions.

**PROPOSAL, NOT CANON:** For a mandatory matching Loom, use CP capacities by Cogmarshal rank **2/4/6/8/12**. Baseline ordinary Windling-excluded four-machine squad cost **1 CP**, Bulwark four-machine support formation **2 CP**, Gearsteed support formation **1 CP**, individual Siege Engines **3 CP** standard / **4 CP** exceptional; these are NOT approved. A four-Servitor squad plus two reinforcements would cost 2 CP if the ordinary base 1 CP proposal is accepted. A 12-CP rank-V commander could theoretically control 48 Windlings but must still spend their action on each new offensive swarm order. No single attack gets multiplied by 48, and per-machine Leywell energy remains a separate constraint. If a commander's Loom is stolen or broken and not repaired, there is no alternative vocal Cogsong channel. Exact acoustic range/latency, signal disruption, capacity by quality, squad effects, mass-lift, and swarm attrition still require author approval.

## November 6, 2026 — CP capacity approved; Windling combat models pending

**CANON UPDATE:** Cogmarshal mandatory-Loom CP capacity is now **2/4/6/8/12** at ranks I–V, not a proposal. Four Windlings cost 1 CP; 8/16/24/32/48 are maximum Windlings if all CP committed. The previous draft label 'PROPOSAL' for these CP capacities is superseded. Other construct CP costs and Windling combat numbers remain draft-only.

**Windling swarm options (NOT CANON):**
- **A: Evasion Pressure.** Four Windlings exert a pressure contribution toward existing evasion categories, but the pressure contribution must be bounded by actual position, target access and the existing pressure ladder; a direct +1 step per CP without cap is likely too strong.
- **B: Swarm Screen.** Windlings form moving protective cover that obstructs single-target ranged lines and may intercept targeted shots; avoid unconditional immunity or indefinite free projectile negation, and distinguish bullets from wide-area effects.
- **C: Tactical Saturation (recommended).** Allocate Windlings in four-unit flights to one active task (screen, distract, harry, lift, obstruct); one commander action issues the coordinated order, and every new attack requires a new command. Multiple flights extend coverage, reliability and options rather than generating separate full damage packets. A flight can be removed by suitable single-target attacks or disproportionately disrupted by area attacks. Screens should not simply ignore accurate shots, and all lifting must respect mass and material-derived construct STR. A shared swarm-cohesion model could avoid per-Windling injury states.
- **Suggested anti-sniper balance:** A single-target rifle attack normally can eliminate or disable only one Windling unless it has an explicit piercing, blast, ricochet or other multi-target capability. Sniper damage does not transfer automatically to additional Windlings, while splash/area spells and suppression can threaten multiple. This is a PROPOSAL, not an approved rule. A screen could impose a bounded existing evasion/cover modifier rather than complete protection.
- **Open:** Windling base attributes from materials, individual and group integrity, attack pressure, maximum screen protection, how many flights one command may coordinate, whether four Windlings are enough to lift a standard Hero, and the exact pressure category interaction. No numerical pressure values or injury thresholds approved.

## November 6, 2026 — Windling sonic pursuit implementation notes (DRAFT; NOT NUMERICAL CANON)

**Approved rule to implement:** Commanded Windlings execute one targeted sonic distraction/pursuit on one specified target for **up to 3 turns** per one original offensive Cogsong order. The swarm does not gain three separate offensive commands, cannot autonomously choose a different target, and does not refresh the timer for failure to reach. The attack requires close proximity; a target around **5 m from most ordinary Windlings** ordinarily stops new exposure. Covered ears, effective sound barriers, escape and melee counterattack are valid. No automatic evasion pressure when the swarm's statistics cannot threaten the target. The sonic device remains designed not to interfere with Cogsong messages.

**PROPOSED turn model:** Count the turn of successful command initiation as Turn 1; subsequent Turn 2 and Turn 3 can maintain the same previously ordered sonic exposure while the swarm can legally follow its designated enemy. No separate full attack roll every turn: a sustained exposure track may escalate at most once per turn only if the swarm maintains valid close-range line-of-sound and overcomes relevant sound/hearing Resistance. Ending exposure by leaving range or covering ears interrupts new dose accumulation; previously inflicted hearing harm follows its own duration/recovery rule (TBD). A new target, unrelated offensive duty or refreshed exposure order consumes a new commander attack action. Several swarms covering the same enemy should not trivially generate additive free injury states; the strongest qualifying exposure plus reasonable coordination should govern. Exact initiative order, dose caps, audible occlusion, temporary protection efficacy, atypical long-range emitters and sonic receiver thresholds UNAPPROVED.

**Potential balance test:** For an ordinary hearing-vulnerable humanoid, define a narrow sound-contact zone terminating short of 5 m and apply a stat-qualified, capped hearing/aiming debuff only with meaningful exposure. Sound attenuation falls steeply outside this zone. Avoid inventing a base Windling SPD/STR/sonic stat before material-derived construct sheets are designed.

## November 6, 2026 — Weapon shapes, dual wield, shields and horde mechanics (PROPOSALS ONLY)

**Approved qualitative guide:** Light/Medium/Heavy shape classes; primary and explicitly supported alternate damage forms; separate reach and attack coverage; Piercing Injury 1/5 Bypass 5/5, Slashing Injury 5/5 Bypass 1/5 maximum coverage, Blunt Injury 3/5 Bypass 3/5 medium coverage. These are **ratings, not numerical combat percentages**. Lower blunt injury through the effective ratio rather than a blanket one-state cap.

**Representative proposed form inventory:** Light dagger, stiletto, short knife, brass knuckles/cestus, hand axe, light pick, short club, sickle; Medium arming sword, one-handed longsword, rapier, saber, falchion, mace/flanged mace, warhammer, war pick, battleaxe, short spear, quarterstaff; Heavy greatsword, zweihander, great axe, maul, great hammer, poleaxe, halberd, glaive, pike, long spear, lance, heavy flail. Weapon-specific alternate strikes use legitimate weapon points, backs, hafts or spikes; no universal 'piercing with a blunt ball' privilege. Distinguish material-based mass and practical handling from the light/medium/heavy *design form*. Normal heavy means generally two-handed but sufficiently skilled/strong users can wield two heavies, subject to grip geometry.

**Illustrative numeric model only:** shape attack-rating coefficient Light **1.00**, Medium **1.15**, Heavy **1.30**; damage form injury coefficient Piercing **0.90**, Slashing **1.10**, Blunt **1.00**; physical armor rating bypass Piercing **40%**, Slashing **0%**, Blunt **20%**. The form coefficients may need shape-specific normalization against established approved Dagger 1.00 and Gauntlet 1.00; do not automatically override those or double-count a class and explicit weapon multiplier. No extra blunt injury cap. Do not apply bypass to universal END/Resistance, wards, psychic defenses, or Shimmer Guard. Armor effectiveness must respect anatomical coverage and material behavior. Actual bypass applied BEFORE squaring armor-rating contribution. Test against no armor, chain/plate and mixed material; piercing should not automatically outperform heavy blunt against all targets.

**Dual-wield implementation candidates:** Offhand Attack = one capped improvement to the difficulty of avoiding a credible two-weapon threat, e.g. **one evasion difficulty category toward harder to dodge** only if relative SPD, reach, maneuver space and DEX justify it; never shift more than one category by simply holding a second weapon and never create an independent damage packet. Offhand Defense = **one easier evasion difficulty category** when an offhand weapon can actually intercept/deflect or cover escape, subject to similar checks and no double count with shield blocking. Alternate conservative proposal: apply a smaller relative SPD factor for evasion only instead of directly shifting a full category. Choose one before final numbers. Stronger weapons in both hands do not automatically double Power.

**Handling working proposal:** 150% of standard heavy STR requirement permits one-hand heavy; 200% permits two heavy weapons simultaneously, assuming adequate independent hands, physical grip clearance and DEX/coordination. Quality-reduced requirements, unusual race anatomy and very long lever/polearm restrictions need explicit calibration; high STR doesn't automatically negate polearm geometry or return long-range reach for free. The exact DEX requirement is open.

**Shield design docket:** Holding shield uses one hand and provides physical Defense. Distinguish passive location-specific armor/coverage, active directional parry/block and evasion effect where appropriate, damage to shield, shield bash attack, deployable or forearm-strapped models, dual-wield conflict, and material interaction; specific block % and SPD impact to be developed alongside armor. No inherent full-body blanket armor.

**Attack coverage and groups:** Every attack has reach geometry, covered number of enemy bodies and actual destructive capacity; determine targets physically covered, then applicable attack Power against each target's Resistance/armor. Slash generally wide, pierce narrow, blunt medium. A single greatsword sweep or several narrated dagger cuts in one action may kill several weak hordelings; no fresh full actions and no free Power propagation outside reach/arc. Precise gunshots usually strike one unless projectile behavior differs. Explore whether divided Power/attack momentum reduces destructive output across repeated contacts. Hordes/gangs/armies need generic group stat blocks, group injury / numbers felled, pressure from comparative stats rather than automatic headcount, and exceptions for Hero/Legend Shimmer Guard. **Horde terminology and exact general squad model are unresolved**, not automatically Cogmarshal CP.

**Open after shape review:** final multipliers; STR vs DEX vs either vs both formula; weapon attribute/handling gates, reach/coverage, armor rating/bypass math, shield defense, multi-target count/power distribution, material mass density and costs, quality, enchantments, ranged/thrown/natural shapes, and monster group thresholds.

## November 6, 2026 — Weapon reach and coverage (NONCANON numeric docket)

Approved fundamentals: Reach Short/Medium/Long is separate from handling Light/Medium/Heavy and attack Coverage. Short suits grappling. Long can prevent ordinary Short attacks while controlling distance and make Medium attackers struggle to close, but genuine Pressure breaks reach control. A successful Short-range grapple inside a Long weapon prevents ordinary long-reach attacks. Choking Up is a proposed future mundane Proficiency, not an approved purchased skill. Shields take a hand and have three future armor functions: passive covered-area protection, active directional block, and context-dependent evasive deflection. Light weapon 1.00 replaces fixed dagger 1.00 as baseline. Numerical armor bypass is deferred.

Coverage naming proposal requiring author review: **Point / Narrow / Sweep / Wide Sweep / Line**. Point and Line distinguish contact concentration from aligned-target attack path; neither automatically bypasses a second target. Reach and Coverage are independent; longer weapon does not automatically mean wide sweep. Exact dimensions, target counts, reach contests, speed/dexterity interaction and repositioning still open. Next review: STR/DEX/either/both weapon Power and handling formula, respecting the approved base +10 rebase.


## November 6, 2026 — Final coverage vocabulary and reach-entry SPD candidates (NOT NUMERIC CANON)

**Already approved:** Coverage names **Point, Narrow, Sweep, Wide Sweep, Line**; handling Light/Medium/Heavy distinct from Reach Short/Medium/Long; opportunity-and-execution movement past a long reach weapon (not fixed meters); existing stat-qualified Pressure and DEX prediction can alter reach control; recklessly accepting a hit does not automatically secure inside reach. The approved both-stat melee Power model is `A = 0.65(STR + DEX)` only if BOTH weapon stat minima are satisfied; other profiles use STR, DEX or max(STR,DEX), and overall Power is `(A * F)^2` with correctly calibrated nonduplicated F. No extra post-rebase combat +10.

**PROPOSED reach-control threshold alternatives, not yet canon:**
- **Model A (author suggestion):** A long weapon user with effective SPD >= **1.5× approaching Short fighter SPD** can maintain control versus a straightforward committed dash, assuming unbroken line, awareness, usable weapon/space and no qualifying Pressure. A precise, accurately grounded DEX prediction adds tactical advantage using already-approved prediction rules rather than granting a separate automatic bonus. Speed superiority is NOT permanent grapple immunity: cover, multi-angle attacks, terrain, ambush, magic, feints and pressure create openings.
- **Model B (softer):** SPD >= **1.25×** lets the defender reliably check a direct approach but leaves more possibility for deception and forced close combat; must be carefully distinguished from the existing evasion difficulty categories to avoid duplicate bonuses.
- **Model C (tiered):** >=1.25× significantly inhibits a direct rush, while >=1.5× denies unprepared direct entry when effective reach control is maintained; adds nuance but more bookkeeping.

**Preserved illustrative teaching chart:** (1) **Open Approach:** dagger Short versus spear Long, spear can maintain reach control and deny a blind straight approach; (2) **Inside Reach:** successfully executed opportunity/entry nullifies long-weapon normal striking geometry; (3) **Grapple:** short dagger remains usable while long spear cannot make an ordinary strike against the grappling foe. It is a tactical depiction, not a feet/meters map or automatic combat lock. The user requested keeping this chart for future rulebook work.

**Next pass:** determine final reach-control SPD threshold and precise stat minimums per form; assign shape-specific F factors (Light 1.00 base; Medium 1.15/Heavy 1.30 tentative), then materials, armor bypass and item quality. Covering multiple enemies with Point/Narrow/Sweep/Wide Sweep/Line remains subject to action/Power/physical coverage and universally applies to hordes, armies and constructs.

## November 6, 2026 — Ranged equipment shapes (PROPOSAL, awaiting author selection)

**Model C is approved:** Long controlling defender SPD versus rushing Short attacker: <1.25 normal opportunity adjudication; 1.25–<1.5 harder direct entry; >=1.5 straightforward unsupported rush can be denied, conditional on genuine control and absent relevant Pressure. Use pre-existing DEX prediction rules and no movement in feet. The previous options A/B and Model C-as-proposal statements are superseded.

**Ranged families to review:** (1) muscle-drawn bows: shortbow, recurve/composite, longbow, warbow; (2) stored-energy crossbows: hand, hunting, military, arbalest; (3) chemical firearms: pistol, revolver, carbine, musket, rifle, scattergun, heavy portable; (4) manually launched/thrown: dart, throwing knife/axe, javelin, sling, bolas; (5) siege/mounted: ballista, repeating launcher, cannon, mortar. Distinguish weapon family propulsion from handheld **Light/Medium/Heavy handling**. Each item needs declared attack delivery (Point/Line/area as actual trajectory/fragmentation), appropriate piercing/slashing/blunt impact type, intrinsic range/aiming requirements, loading/shot economy, body/hand requirements, materials and quality, ammunition, noise/concealment, reliability, and defensive response/cover.

**Power-source design proposals:** Drawn bows: bow-specific draw tension/build + shooter STR capacity + arrow characteristics determine intrinsic shot energy; DEX affects precision/shot placement, not free physical damage. Crossbows: stored mechanism energy and ammunition set shot Power; STR or tools affect cocking/reload and handling, DEX targeting. Firearms: construction, propellant (Crownsalt), barrel/chamber and ammunition set intrinsic shot Power, not user's STR; STR for recoil and wielding, DEX for target precision. Thrown: STR- or DEX- or either-based user's approved physical attack formula `(A*F)^2` with throw/form applicability, not automatically the same melee modifier; geometry, ammunition and SPD of actual projectile matter. Siege weapons: intrinsic engineering, mounting, crew and ammunition affect Power and area; no free personal STR scaling. These formulas beyond firearms remain **noncanon design**.

**Unresolved core choices:** Do bows scale damage with STR alone up to their draw cap, or use fixed Power once minimum draw met? Is DEX only aim or also eligible on graceful light bows? Are crossbow reload tools limited by turn actions? Ranged firing while grappled and physical long-weapon weakness; comparative range bands (no distance charts required except specific weapons/spells); firearm spread and multiple projectile coverage; penetration/ammunition traits and material interactions deferred to armor; multi-target firearm/bow effects and horde casualty counts. Aim should interact with existing SPD-based evasion ladder and DEX prediction, not grant automatic hits or extra actions.

## November 6, 2026 — Ranged weapon family operating models and battle-saddle configuration (DRAFT ONLY)

**Approved framework:** Five families Bow/Crossbow/Firearm/Thrown-or-Manual/Mounted-or-Siege. Close/Effective/Far/Extreme are relative weapon range bands. Bow model A uses wielder STR up to an engineered draw cap, DEX for accurate aim. Crossbows use mechanical stored energy; firearms and artillery intrinsic charge/projectile Power not shooter STR; thrown weapons use appropriate STR/DEX physical Power. Body-mounted battle saddles fit Centaur, Crownform Drakyn and qualifying Firstshaped anatomies and suit firearms/crossbows, not automatically bows, slings or throws. Side mounts need usable arc, reload, aiming input, physical clearance, stability and recoil management. Centaur cannon carts must be braced/deployed to actually fire safely unless specially engineered. Strong users may handle Adamantite-reinforced massive guns; DEX users prefer light designs, but Trufula is highly flammable and needs safe propellant/thermal design.

**PROPOSED firing/reload procedure, not canon:** Distinguish **Ready**, **Aim**, **Fire**, **Reload**, **Recover** as activities rather than obligatory new character actions every turn. Actual weapon type defines which activities cost an attack/movement action or turn; don't force pre-aim for every ordinary shot. Light bows can be repeatedly drawn and released but require ammunition each time. Warbows have high STR minimums and demanding draw. Crossbows shoot stored energy but have cocking/reload cycle, sometimes tools or levers; hand crossbows may need bracing or a free hand to load. Firearms have single-shot/loaded-many configurations with reload differentiated from recoil recovery, mechanical action cycling and ammunition supply. Reloading under grapple/while galloping becomes harder if controls unavailable; a saddle may use engineered reload assistance without infinite free ammo.

**PROPOSED range behavior:** Close = normal good shot only if gun can be aligned, but long rifle/crossbow awkward in a grapple; Effective = intended aimed use; Far = harder evasion/aiming contest for shooter, potential energy loss if relevant; Extreme = technically viable only for appropriate designs/exceptional circumstances, with no default guaranteed hit. Physical geometry/cover plus target SPD and attacker DEX govern aiming; do not grant extra attack actions or make every bullet dodgeable in close melee without regard to projectile speed.

**PROPOSED power/failure/casualty rules:** Bows cap physical drawn shot Power at bow's material/structural limit. Crossbow mechanism energy sets Power, with material limits and reload energy input; firearms intrinsic chamber/propellant/ammunition damage, weapon recoil and shooter STR capacity; throwing attacks require relevant STR/DEX but no uncapped long-distance accuracy. Point bullets/bolts normally threaten one; Line through multiple foes requires specific penetrative projectile and retained Power; scatter and blast cover several appropriately exposed foes. All apply to generic hordes/armies and clockworks, no firearm gets unlimited kills merely because its single projectile has great Power. Mounted side guns generally have limited arcs and body-turning constraints; powerful mounts can improve bracing but must not entirely nullify recoil by fiat.

**OPEN NUMBERS:** bow draw cap formula, STR gain before cap, shot Power, accuracy and reload pace per type, saddle support capacity/turning/aim interfaces, movement fire, artillery deployment, mechanical cycling, ammo traits and damage/armor bypass deferred. No new Gem price, SP gate, MP cost or racial stat bonus.

## November 6, 2026 — Pressure-points and ranged reload/aim tuning (DRAFT; not canon numbers)

**Approved PP skeleton:** net 0 Open, net 1–2 Pressured (same effect), net >=3 Extreme Pressure (capped). Typical meaningful threats +1 PP, countermeasures remove qualifying PP, no free duplicate PP for the same cause. Trapped is independent of PP: ordinary dodge impossible against relevant incoming threat, but aware target may actively shield, block, interrupt or employ suitable protective resources. The preexisting evasion ratio/difficulty categories remain. Exact PP modifier to the six-tier difficulty ladder, number of effects allowed to stack and timing remain undecided.

**Swarms:** A four-unit Windling flight *may* qualify for one point only if relative stats, effective sound/physical threat and range pass the existing credible-threat gate. Proposed *nonlinear* saturation requirement for successive independent PP from one coordinated group should be far beyond linear 4/8/12 bodies; possible example benchmarks **4/16/64 effective Windling-equivalent threats** for first/second/third PP are **purely illustrative and not approved**, and 64 exceeds the current 48 max controlled by Cogmarshal V if relying on Windlings alone. Do not use raw numeric headcount without stats and circumstances: formations that flank, pin, fill exits or integrate allies might create independent meaningful sources at smaller counts without granting free multi-attacks. Need a shared universal monster horde/army mechanic.

**Aiming bonus options (proposals):** aim action grants one hit-difficulty-tier improvement, or one situational PP applied against the aimed target, or improves prediction quality; choose one only after testing, never multiply all of them. Aim yields one shot across two actions instead of two shots. Aiming while being threatened can be interrupted or penalized; exact retention, switching targets and aiming through cover unknown.

**Reload vulnerability possibilities:** lightweight crossbow reloading could create a +1 situational PP for a qualifying opponent while loading, or deny an otherwise available defensive maneuver; which applies is pending. Full-turn pistol/magazine reloading exposes combatant to real, stat-qualified attacks but never auto-grants extra turns to all observers. Siege crews may have long exposure windows, specialized brace/loading equipment and dedicated protection. Draft reload Proficiencies: *Rapid Reload* (time) and *Protected Reload* (exposure) at as-yet unknown SP costs; no automatic access.

**Mounting:** Fixed (stable restrictive arc), Articulated (wide aim arc), Heavy-Supported (load/recoil engineering), Assisted-Loading (real mechanical reload aid); can combine where fit, cost and materials support. Exact stationary/moving accuracy trade-offs and reload automation remain unapproved.

## November 6, 2026 — Rapid-fire numerical experiments (PROPOSAL)

Approved qualitative rule: extra ammunition allows ranged suppression of a credible target/area or bounded close-range physical damage amplification. Each is one normal attack action, not an attack action per projectile. Pressure categories now produce one easier hit-difficulty tier at 1–2 PP or two easier tiers at 3+ PP, capped. Aiming instead of firing gives one tier of benefit on a valid subsequent shot; do not also add a separate aiming PP.

**Suggested trial numbers (not approved):** ranged suppression from a real firing line contributes one PP; close concentrated burst contributes plus 35% final physical Power (other trials +25% or +50%), with neither mode giving the other mode's reward. Additional ammunition requirements, actual suppression durations, mechanical capacity, recoil, movement and multi-target coverage require later balancing. Avoid attack-rating coefficient stacking with final Power and avoid automatic hits through cover.


## November 6, 2026 — Magazine and recoil calibration following rapid-fire approval (PROPOSAL ONLY)

**Already approved:** +1 relevant PP from suppressive full-auto ranged volley; +35% **final physical Power** from a close concentrated burst, as alternatives during one normal attack action. Dual wield Attack, Defense, suppressive fire and close burst cannot stack same-user weapon benefits, even if using two automatic pistols. All guns need capacity listing, all automatic weapons need full-auto volley ammunition cost, and stock magazines must only permit one complete full burst before reload. Upgraded magazines/feed systems can support more than one full burst. The upcoming Proficiencies system may offer rapid shooting for normally nonrapid bows/other weapons; this is only a future option, not a purchasable skill currently.

**Possible calibration profiles (illustrative, NOT CANON):** automatic pistol normal capacity **12** rounds, full-auto volley cost **8** rounds (only 1 full volley per stock magazine); upgraded magazine **24** rounds (3 full volleys); light automatic carbine normal capacity **20**, volley cost **12**, upgrade 36; heavier automatic rifle normal capacity **30**, volley cost **18**, upgrade 54. Each is an equipment profile suggestion not a universal automatic weapon law. Distinguish single-shot ammo from burst ammo and consider rounds carried, magazine mass, recoil, reloading vulnerability, exposed reload windows and weapon form limits. No automatic half-volley Power increase from leftover cartridges. Different high-rate firearms could have entirely different optimum volley counts.

**Next testing model:** independent firearm intrinsic shot Power determined by gun construction/propellant/ammunition; weapon has **Carry/Support STR Requirement** and **Recoil-Control STR Requirement**, possibly different. DEX affects aim, handling transitions and targeting but not raw shot Power. An adequate mount may change support STR with mass/load distribution and recoil transfer, but cannot magically remove momentum or send all recoil through unbraced anatomy. Test ordinary stand-fire, braced-fire, battle-saddle side-mount, cart/braced cannon and moving-fire as separate configurations. Numeric required STR, handling penalties, recoil thresholds and quality/material changes are NOT canon. Clarify whether recoil from burst fire uses an increased burden over single-shot recoil, whether a full-auto volley can be aimed, and which modes can occur when bracing/firing within grapple. Advance to numerical ranged family chart only after this framework is reviewed.

## November 6, 2026 — Point Blank and handling-requirement calibration (DRAFT)

**Approved:** Point Blank for full-auto Concentrated Burst is normally **within 10 meters** and is required for the previously approved ×1.35 FINAL physical Power, assuming viable aim, physical access and almost every bullet plausibly connecting despite recoil. A rare GM discretion note extends this eligibility for physically enormous targets when nearly the entire volley should connect beyond ten meters; the exception is NOT a normal weapon range or material/stat tuning input. Extended magazines and some modifications can increase both STR and DEX requirements. Sophisticated scopes can improve useful precise range when DEX supports it. No approved numeric modifier costs or scope distance increases yet.

**Proposed Support/Recoil STR calibration:** Maintain separate weapon requirements for supporting/maneuvering and for safely controlling discharge/recovery. A gun may be comfortably supported yet too much recoil for the user, or manageable in recoil yet too heavy to reposition. Unsupported handheld support depends on hands/body strength; braced weapons transfer some load into an external stable surface; body-mounted saddle load and recoil transfer through chassis/body without free cancellation; carriage-mounted artillery transfers load and recoil into properly deployed carriage and terrain, provided anchoring exists. Mounts change *how requirements are met*, not intrinsic attack Power. Distinguish DEX for aiming, fast retargeting and using complicated attachment controls from the actual ballistic Damage Rating. No exact STR reductions or DEX penalty gates approved; draft illustrative proposals for later testing, not fixed arbitrary percentages.
