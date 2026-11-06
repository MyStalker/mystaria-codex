# Mystaria — Canon Changelog, Supersession Ledger, and Open Questions

## November 5, 2026 — Racial naming conventions and 450-name library (APPROVED)

- **Explicit author approval:** All 15 reconciled racial naming traditions and all 30 proposed names per group (450 entries) were approved without requested revisions. The authoritative full list is `24_Racial_Naming_Conventions_and_Namebook.md`.
- **Naga:** Flexible inherited maternal syllables take precedence, alongside dynastic Coil and public/private names. **Kobolds:** Birth names exist before First Devotion; earned achievement names are reserved for free or accomplished Kobolds, with accomplishment not requiring freedom. **Moontouched:** Chosen adult names. **Bloomkin:** Artisan family names. **Thornguard:** Banner names. **Tidekin:** Primarily waterway surnames, with some story names. **Duskpaws:** Cache names. **Vren:** Bloodline names. **Corvyn:** Birth names and earned Ink Names. **Driders:** Verdict and optional reclaimed names. **Untouched Serpentari:** Ancient lineage and everyday shortened names. **Drakyn:** Hoard titles and ceremonial/common names. **Centaurs:** Forge and herd names. **Firstshaped:** Parent-race naming. **Nymbrin:** Alchemy and trade names.
- **No new NPCs or institutions:** These are reusable examples, not 450 newly established individuals, court rosters, families, historical events or magical true-name mechanics. Drider scarcity and Centaur demographics remain unchanged. No SP, Craft, race or Shimmer mechanic changes.
- **Files:** New `24_Racial_Naming_Conventions_and_Namebook.md`; cross-references in `00_Mystaria_Canon_Index.md`, `02_Races.md`, and `12_Languages_and_Linguistic_Customs.md`. This entry records explicit approval and supersedes any implication that the naming draft remains a proposal.


**Authority:** This is a revision index, not a new fictional skill tree. **Snapshot date:** November 4, 2026.  
**Editorial principle:** Latest explicit user approval outranks earlier drafts, source templates, assistant suggestions and outdated compendium passages. A proposal is not canon simply because it appears in a long reply.

## 1. Known source versions

| Artifact / history | Status in this library | Precedence |
|---|---|---|
| `Mystaria_Canon_Compendium.md` (Nov 1 consolidated) | Older world, races, shop and interface source | Still valid **where not contradicted** by later explicit decisions |
| `Mystaria_Warlock_Skill_Costs.md` | Older **partial** Warlock costs ledger | **Superseded** for individual rank effects by approved full Warlock file |
| `Mystaria_Warlock_Skills.md` | Original Warlock rank design, originally labeled proposed | Historically approved Nov 3; the November 4 replacement controls where different |
| `Mystaria_Warlock_Skills_Canon.md` | Formerly approved 25-rank MP/SP reference | **SUPERSEDED** for old technique names/effects/MP fees by the explicitly approved November 4 replacement in `04_Warlock_Manacraft.md` |
| `Mystaria_Jester_Craft_Canon.md` | Earlier living-Regalia abilities | Superseded by revised document on sentience and lore |
| `Mystaria_Jester_Craft_Canon_Revised.md` | Full 6-discipline, 126-SP reference with speaking Regalia | **CANON**; copied fully into `05_Jestercraft.md` |
| `Drakyn_Player_Field_Guide.html` | Drakyn player-facing guide | Correct on summarized approved lore; `06_Drakyn.md` is deeper mechanical dossier |
| Green / White Sorcery selection HTML menus | Choice *candidates*, not final approved choice export | Use base names/themes; **never assume all candidates selected** |
| Latest Sorcery approval discussion | Explicit user approval of Red revisions and 25 Black alterations | **CANON**; catalogued to the extent retrievable in `03_Sorcery.md` |
| Latest Centaur approval discussion | User canonized Centaurs, 12 materials including Celestite | **CANON** in `07_Centaurs_and_Smithcraft.md` |
| Later Smithcraft / equipment overhaul reply | Extensive suggested mechanical implementation | **PROPOSAL** only; keep distinct from approved original |

## 2. Canon approvals / revision history

### November 5, 2026 — Hero Gem wealth, consumables, shop buyback, and threat rewards (LATEST)

- **Explicit author approval:** `09_Equipment_and_Economy.md` now owns the typical Hero equipment-wealth curve `W(L) = 3 + 3997 × ((L−1)/99)^2.3` (levels 1–100), targeting **3 Gems in equipment at level 1** and **4,000 Gems of currently owned equipment at level 100**, with the latter reflecting a **typical Hero who replaces equipment at every quality tier**, not an unusually thrifty Hero.
- **Approved spending and resale:** By level 100, approximately **30% of all Gems ever earned** is spent on consumables. Gem Shops buy back **items they originally sold** for **half their original purchase price**. Replacement losses are incorporated into the typical earnings budget, not compensated by a free reimbursement.
- **Reference model:** Quality milestones at Hero levels **10, 25, 50, 75, 100** are balancing assumptions, **not equipment-use prerequisites**. The representative portfolio values are **19 / 157 / 796 / 2,049 / 4,000 Gems**; four complete replacement resales create **~1,510.5 Gems of cumulative losses**. With `E(L) = (W(L) + R(L)) / 0.70`, the level-100 lifetime target is **~7,872 Gems earned**, **~2,362 Gems spent on consumables**, and **4,000 Gems currently in equipment**. Half-Gem arithmetic does not establish a fractional Gem denomination.
- **Gem reward multipliers explicitly match existing XP multipliers:** **Horde ×0.1, Minion ×0.4, Henchman ×1, Elite ×2**. A **Boss** grants a special Gem reward equivalent to **two levels of budgeted Gem progression**, including milestone replacement allowance where applicable; the existing Boss **XP** reward of exactly two level advances remains unchanged. **Do not adopt** the unapproved Elite ×3 / Minion ×0.5 XP suggestions from the immediately preceding discussion.
- **Reward calibration:** Base Gem rewards derive from the incremental lifetime earnings budget `E(L+1) − E(L)` and expected qualifying encounter/quest pacing. The exact encounter/quest allocation and fractional reward rounding remain unresolved. The two-level Boss Gem formula `E(L+2) − E(L)` is specified for **L+2 ≤100**; beyond-level-100 Gem progression is unresolved.
- **No changes:** Patron-specific eligibility, mundane quest limits, XP math, tier gates, shop catalogue item prices, five quality benchmarks, SP, and equipment usage requirements. Reference: `09_Equipment_and_Economy.md`, indexed in `00_Mystaria_Canon_Index.md`.



### November 5, 2026 — Shimmer XP progression and enemy threat classes approved (LATEST)

- **Explicit user approval:** Hero XP required to advance from level **L** to **L + 1** is **`L × (L + 1)`**, as a per-level requirement, not cumulative lifetime XP. Example thresholds: level 1 **2 XP**, level 50 **2,550 XP**, level 100 **10,100 XP**. XP carries through level transitions.
- **Ordinary qualifying reward:** **`XP = 2 × encounter level × threat modifier`**. A defeated enemy uses its own level; a qualifying quest or nonviolent patron-approved achievement can use a GM-assigned equivalent challenge level. Round to nearest whole XP, minimum **1 XP for a qualifying encounter**. Patron-specific XP rules and the fact that mundane quests do not automatically award XP remain operative.
- **Threat modifiers and relative-level guidelines:** **Horde ×0.1** (enemy level ≤50% of Hero); **Minion ×0.4** (>50%–80%); **Henchman ×1** (>80%–110%); **Elite ×2** (>110%–140%); **Boss** (usually >140% or specially designated). These are **guidelines**; the GM assigns actual encounter class based on capabilities and context, not level ratio alone. The categories indicate swarmable trivial enemies, minor threats, near-peers, minibosses and prepared prolonged bosses respectively.
- **Boss exception:** A qualifying Boss grants the remaining XP to the next level **plus** the full XP for the following level, advancing the Hero **exactly two levels from the Hero's current level and progress**. At level 50 with no progress, the reward is **5,202 XP** and the Hero reaches level 52. Boss XP replaces, rather than multiplies, ordinary enemy XP.
- **Pacing:** One equal-level Henchman at level 1 yields the **2 XP** needed to level; at level 100, an equal-level Henchman gives **200 XP** against **10,100 XP**, so **51** encounters are needed from zero progress (approximately the requested 50).
- **Not approved by implication:** The previously floated anti-farming numerical restriction and any party XP division procedure remain unspecified; merely trivial/repetitive acts are not automatically patron-qualified. This approval does **not** change Shimmer attribute gains, Skill Point costs, rank prerequisites, or the goddesses' established reward criteria.
- **Owning file:** `01_World_and_Shimmer.md`; indexed in `00_Mystaria_Canon_Index.md`.


### November 5, 2026 — Style choice corrected to Direction 4 (LATEST)

- User explicitly corrected the selection: **Direction 4**, detailed ink-and-color fantasy, is the defining Mystaria style. Direction 5 is an archived alternative.
- Full guide now specifies delicate occasionally broken ink contours, sparse hatching, restrained translucent washes, subtle paper texture, economical expressive faces, practical clothing detail and grouped fur/feathers.
- Defining style reference is Race Image Origin — Direction 4, version 10. Original Race Image Origin v6 remains separately preserved.
- Adult female busty/voluptuous appearance, race-reference priority, deferred website work, collars and racial anatomy remain unchanged. Updated guide, index and repository instructions; historical selection below is superseded.

### November 5, 2026 — Direction 5 selection (SUPERSEDED by correction above); race references prioritized

- User selected the Japanese woodblock/modern anime hybrid as the defining style: rhythmic ink lines, designed negative space, layered flat scenery, stylized foliage/clouds, restrained separated pigments, selective textile patterns and subtle print texture, preserving animated characters and species anatomy.
- `11_Visual_Style_Guide.md` records the full specification and links to preserved Race Image Origin v6 and Direction 5 v11. Style reference acceptance does not canonize every anatomical detail or authorize site integration.
- Earlier uniform bold-outline cel rendering is superseded. Busty and voluptuous adult female appearance across all races, collars, emblems and purple identity remain operative.
- Race reference sheets take priority; earlier website illustration queue, placements and single-image composition restriction are deferred for this phase. Separate full-resolution views and later sheet assembly are recommended production workflow, not new lore.
- Updated guide, index, repository instructions and this ledger. Existing racial descriptions and mechanics are preserved.

### November 4, 2026 — Raw blue mana against wounded targets approved

- **Explicit user approval:** A Warlock's raw blue blast against a wounded target primarily causes **sensory overload and pain amplification**, with secondary **fractured bodily perception and disrupted coordination**.
- **Boundary:** Raw projection remains distinct from structured Sorcery; it does **not** freeze the target or become a splash of water. Approval is limited to this blue effect. Other optional proposals are not automatically canon.
- **Owning reference:** `04_Warlock_Manacraft.md`; navigation summary in `00_Mystaria_Canon_Index.md`. This adds an approved clarification where the dossier previously lacked a wounded-target raw-blue description; it does not replace the existing **Blue Hole — Shifting Depth**.
- **Preserved:** All existing Warlock skills, ranks, SP/MP costs, prerequisites, level gates, range, Handling Capacity, and external-source restrictions.
- **UNRESOLVED:** Exact duration, numerical penalties, resistance procedure, and damage formula for this effect. No new numerical mechanics are inferred.

### November 4, 2026 — Busty and voluptuous adult female appearance extended to all races

- **Latest explicit user direction:** Extend the busty and voluptuous description to adult females of every Mystaria race. The earlier Corvyn-specific direction remains included within this broader rule.
- **Implementation:** `02_Races.md` owns the setting-wide description; `11_Visual_Style_Guide.md` applies it to official art; `00_Mystaria_Canon_Index.md` records the expanded scope.
- **Anatomical continuity:** Interpret the description through each race's existing body plan and form, including Firstshaped; preserve species identity and do not add human body parts to forms that lack them. No numerical mechanics change. Individual image approval remains separate.

### November 4, 2026 — Global official-art style and Corvyn figures approved

- **Explicit user approval:** All official Mystaria artwork generated going forward must use the seven listed attributes: simplified strong shapes; clean varied bold outlines; expressive deliberately stylized proportions; two or three hard-edged cel-shading values and broad highlights; limited separated colors and colored shadows; large readable shapes with selective facial/focal detail; clear action lines, dynamic gestures and expressive hands.
- **Supersession:** Replaces the painterly living-storybook rendering requirement globally, including environments. Earlier Drider/Centaur controlled-linework guidance remains compatible within this global specification. Species anatomy and established forms remain controlling.
- **Racial appearance:** Adult female Corvyn characteristically have particularly busty, voluptuous figures. This supersedes the earlier blanket slender-figure description while preserving their avian features, independent arms and separate back wings. No numerical stats or mechanics change.
- **Updated references:** `11_Visual_Style_Guide.md`, `02_Races.md`, `00_Mystaria_Canon_Index.md`, and `AGENTS.md`, plus this ledger. Existing collars, emblems and purple identity remain operative. The style specification is approved; `vol-peoples` version 6 remains unapproved.

### November 4, 2026 — Official-art collar depiction philosophy approved

- **Explicit user direction:** In official art, slave races should usually be depicted wearing collars.
- **Owning reference:** `11_Visual_Style_Guide.md` records visible collars as the normal art-direction convention, with contextual and explicitly directed exceptions preserved by the word **usually**.
- **Scope:** Visual presentation only; no new racial classification, universal enslavement rule, legal status, or mechanics. This adds an explicit default where the guide previously had none.
- **Cross-reference:** `00_Mystaria_Canon_Index.md`. Individual illustrations still require separate approval; `vol-peoples` version 3 remains awaiting approval.

### November 4, 2026 — Drider and Centaur illustration style approved

- **Explicit user direction:** More anime-inspired character design for Driders and Centaurs, with **controlled linework, simplified facial features, and expressive posing**.
- Apply this character treatment within the painterly living-storybook presentation. This supersedes conflicting realistic facial rendering preferences for these races; current approved anatomy and mechanics are preserved.
- Updated `11_Visual_Style_Guide.md`, `02_Races.md`, `07_Centaurs_and_Smithcraft.md`, and `00_Mystaria_Canon_Index.md`.

### November 4, 2026 — Drider anatomy and scale revised (LATEST)

- **Explicit user correction:** Driders have dark skin reminiscent of a drow elf, pointed ears, **two arms**, and **six long spider-like legs** supporting an enormous arachnid lower body. They have **four solid-color eyes with no pupils**; eye color varies between individuals. Their long legs and imposing bodies make them **one of Mystaria's largest mortal races**.
- **Supersedes:** Earlier four-armed Drider descriptions and the former **Four-Arm Coordination** racial benefit. The revised anatomy has two arms and six spider-like legs; illustrations must use these counts.
- **Preserved:** All-female identity, divine origins, Courts, sacred silks, natural wall climbing, vibration detection and biological silk production. Arrest's separate divine appearance is unchanged.
- **Unspecified:** Exact dimensions, eye arrangement, precise skin palette, universal eye color, replacement racial ability and numerical attribute changes. Do not infer these from the new anatomy or scale.
- **Updated files:** `02_Races.md`, `01_World_and_Shimmer.md`, `11_Visual_Style_Guide.md`, `00_Mystaria_Canon_Index.md`, and this changelog.

### November 4, 2026 — Warlock direct MP Hand Capacity approved (LATEST)

- **Explicit approval:** Replace the old 1–3 spell-load system with direct temporary mana handling in **one hand**: **`max(1, floor(natural effective END / 5)) MP`**, i.e., **20% of natural effective END rounded down, minimum 1 MP**. For END 10/25/40/60/100/150/200, respective one-hand limits are **2/5/8/12/20/30/40 MP**.
- **Preserved restrictions:** A Warlock cannot generate or internally store mana, and retains the **30-second safe / 60-second absolute** hand-holding limits. The one-hand restriction remains; no implied doubled capacity, unlimited instantaneous absorption or bypass of the established throughput constraints. External mana sources and vessels are still essential.
- **Costs and other mechanics unchanged:** Existing 25 Manacraft ranks and **125 SP** mastery, all activation/upkeep/manifestation fees, prerequisites, range formula, Intelligence contest, and staging requirements continue unchanged. Questions about **same-action harvesting**, direct external payment of oversized fees, advanced effect scales and lifetimes remain unresolved; this capacity ruling does not settle them.
- **Supersedes:** The former **`max(1, ceil(natural effective END / 10)) MP` per spell-load** calculation, its 1–3 held-loads chart, and the missing category thresholds. Owning reference: `04_Warlock_Manacraft.md`; cross-reference: `00_Mystaria_Canon_Index.md`.


### November 4, 2026 — Red Sorcery alteration count reconciled (LATEST)

- **Explicit user approval:** Removed the **unidentified seventh Ignis alteration purchase**. The six named Ignis alterations (**Flame Arsenal I**, **Flame Arsenal II**, **Lingering Fire**, **Backdraft**, **Stormspark**, **Impossible Combustion**) remain unchanged; all other named Red abilities remain valid.
- **Operative ledger:** Ignis **6**, Varekh **5**, Darvok **4**, Ashal **5**, Ruveth **5** = **25 Red alterations**, alongside five base Incantations. Full Red mastery **90 SP ordinary / 60 SP Drakyn**. Uneven per-Incantation distribution is the approved total, not permission to invent a fifth Darvok alteration.
- **Supersedes:** the provisional 26th alteration, 93/62 SP Red pricing, and 453/302 SP five-color estimates based on that unapproved extra slot. The standard five-color total remains 450/300 SP, pending recovery of final Blue/Green/White itemizations.
- **Updated files:** `03_Sorcery.md`, `00_Mystaria_Canon_Index.md`, and this changelog. The earlier audit merge and unrelated mechanics are preserved.

### November 4, 2026 — Kobold Hero starting attributes approved (LATEST)

- **Explicit user decision:** Kobold base starting attributes **STR 2, DEX 8, END 3, INT 10, SPD 7** (base total 30). Racial percentage modifiers **STR −10%, DEX +10%, INT +20%**, yielding effective **STR 1.8, DEX 8.8, END 3, INT 12, SPD 7** (effective total **32.6**).
- **Racial index gap resolved:** Added Kobolds to `02_Races.md` and reconciled cross-references in the Canon Index and Languages document; `01_World_and_Shimmer.md` records this newer override alongside existing Hero stat mechanics. Earlier claims Kobold stats were unapproved or absent from the racial index are superseded.
- **Limits:** This approval specifies only statistics and multipliers. It does **not** establish a new Kobold racial affinity, skill-rank costs, starting SP balance, special ability or Orbcraft tree.


### November 4, 2026 — Repository audit reconciliation (approved corrections; review branch)

- **Restored missing canonical sources:** Reinstated `09_Equipment_and_Economy.md` (approved five-tier equipment baseline; clearly separated modular-equipment proposals and Moonlit Garden pricing conflicts) and the full `15_Naga_Psycraft_Canon.md` (Sovereign Sense, 15 approved ranks, 75 SP total, current **Psycraft / Psychics** terminology). These files existed in approved project sources but were absent from the GitHub repository.
- **Imperial games:** Replaced mistaken descriptions of rotating "Imperial capital venues" with **major Imperial cities** in `17_Imperial_Sports_and_Great_Coil_Circuit.md`. **Sathryx remains the sole capital**; venue rotation mechanics are otherwise unchanged.
- **Naga terminology:** Corrected outdated operative `Crowncraft` / `Crownmind` references to **Psycraft** / **Psychic(s)** in the races index and Wakecraft/Vren comparison passages. Historical explanation of superseded titles is retained where relevant. This changes names only, not abilities or costs.
- **Firstshaped rarity (new explicit user ruling):** Approximately **10% of Centaurs** are Firstshaped Ponies; approximately **5% of Drakyn** are Firstshaped. These supersede application of the older generic `~1 in 50` rate to those two races. The generic rate remains background for other races without an approved exception. Updated `02_Races.md`, `06_Drakyn.md`, `07_Centaurs_and_Smithcraft.md`.
- **Still NOT CANON / pending user review:** Kobold numerical starting attributes and racial modifiers were subsequently **approved** and added to `02_Races.md`; the former Red Sorcery Ignis discrepancy is now **resolved** by the author's explicit removal of the unidentified seventh purchase (25 alterations; 90/60 SP); Blue/Green/White final approved selections could not be recovered from the available candidate-menu sources; Warlock END handling thresholds were **resolved by the new direct 20%-of-END MP-per-hand formula**. Centaur clockwork redesign, exact other gaps and unrequested mechanics remain unchanged.

### November 4, 2026 — Mindprism / Mnemonic Arts / Living Reliquaries approved (LATEST)

- **Approved technology and vocabulary:** Retinal **Mindprism** uses specially calibrated **Cipherlight** for the **Mnemonic Arts**. Approved terms: **Echo, Echo Orb, Everseal, Mindwright, Deepprint, Echoing, Mindcut, Echo Vault, Memory Bond, Dreamcasting, Dreamcaster, Dreamhouse, Skillprint, Living Reliquary, Hollow Reliquary**. Ordinary direct Cipherlight beams remain dangerously confusing.
- **Recording/medical ruling:** Copying a memory consumes **extravagant amounts of actual mana**, is expensive and often impractical; a basic recording has a **firearm-purchase-level relative price**, not a fixed Gem amount. Individual calibration and extreme neurological strain apply. Broad Deepprints can take days or years. Magic cannot heal this particular neurological injury: time is required, and severe Mindcuts can leave permanent damage. **Mindcut erases the original source memories** but can be much faster; it may be used to induce amnesia.
- **Law of Returning Echoes:** Recorded memories cannot be destroyed by mortal technology. All copies remain tied to the original source. Unsealed Echoes return to the **living** original owner; a continuously maintained **Everseal** using some actual mana prevents return. If every surviving implanted copy is lost with its recipients, the memory returns to the still-living owner. **Death of the original owner ENDS automatic return.** Returned memory does not cure brain damage; divine interventions retain their own laws.
- **Skillprints and Shimmer:** An advanced **Skillprint** can bestow an **actual Shimmer skill counted as purchased at no SP cost**. Normal level gates, chains and racial/physical/magical prerequisites remain controlling; no innate mana or Shimmer for non-Heroes. **~5 SP worth of skills per month** is a modest safety benchmark, with neurological harm risk beyond it. Such Skillprints are rare, usually medium- or high-level Hero treasures. No normal SP purchase costs, rank names or unrelated Crafts are modified.
- **Culture:** **Dreamcasting** streams actual subjective experience **in real time**, as distinct from uploading a previously recorded Echo. **Dreamhouses** and professional Dreamcasters are a major entertainment industry. **Echo Vaults** use maintained Echo Orbs, **Memory Bonds** pledge memory collateral. **Living Reliquaries** are enslaved intelligent living archives of foreign memories, while **Hollow Reliquaries** have their own histories forcibly Mindcut away; neither has unlimited capacity or loses personhood.
- **Canon boundaries:** This is a new technology, not a new Shimmer purchase table, Craft skill tree, Warlock soul vessel, or divine memory rule. The detailed controlling document is `19_The_Mnemonic_Arts_and_Echo_Economy.md`. Supporting references: `18_The_Gilded_Coil_Imperial_Gazetteer.md`, `01_World_and_Shimmer.md`, `12_Languages_and_Linguistic_Customs.md`, `13_Wakecraft_The_Six_Arts_of_the_Living_Tide.md`, `00_Mystaria_Canon_Index.md`.
- **Open:** Exact MP and Gem prices, recording/upload timing formulae, Everseal mana and maintenance rates, host resistance/return timing, postmortem final Echo disposition, and staged Skillprint uploads. These are not settled by the approval.


### November 4, 2026 — Cipherlight, Coilnet Rainbows, language, and Mirrorwake (LATEST)

- **Approved name:** **Cipherlight** is the encoded, information-bearing optical medium of Kobold Orbcraft and Mirrorcraft; computational Orbs and Magic Mirrors encode/interpret it. **Lighthouses** act as beam relays. Reflective surfaces permit transmissions through water, including submerged and underground pipelines, potentially offering greater route security than exposed relays.
- **Approved coverage phenomenon:** An active Coilnet's coverage region is its **Rainbow**, visibly indicated by a subtle aurora-like upper-atmospheric shimmer; heavy traffic makes it stronger and more obvious. Even small independent networks (e.g. near a Drakyn lair) can attract interest. A new Rainbow can tip off guards to possible covert transmissions/foreign influence but does not prove a crime, pinpoint senders, or decode traffic.
- **Approved direct beam hazard:** Staring directly into Cipherlight produces **extreme confusion**. Numerical exposure and resistance mechanics were not specified.
- **Approved language:** The user approved the Kobold and regional sayings “You're speaking Cipherlight,” “Don't stare into the beam,” “Bright Rainbow!”, “Lost in the Rainbow,” “There's light beneath the water,” “All beam, no message,” “Under the same Rainbow,” “The Rainbow is burning,” “Beyond the Rainbow,” and “a beautiful headache.” These supplement rather than supersede older idioms. See `12_Languages_and_Linguistic_Customs.md`.
- **Approved regional reception:** Reactions vary among Imperial residents, Canopy populations, Vren, Duskpaws, Tidekin and remote Drakyn lairs. The regional security consequences appear in `18_The_Gilded_Coil_Imperial_Gazetteer.md`.
- **Approved Tidekin interaction:** **Mirrorwake detects Cipherlight through water exceptionally well** and retains strong, significant impressions of it. High-intensity traffic can overwhelm and obscure other water memories. Deliberate Cipherlight use can conceal evidence, and **particularly sophisticated interference can create false Mirrorwake evidence**. Detection does not automatically decrypt Coilnet communications; forging evidence is not automatically successful. This expands an environmental interaction only; **Mirrorwake ranks, SP costs and existing techniques are unchanged**. Owning reference `13_Wakecraft_The_Six_Arts_of_the_Living_Tide.md`.
- **Unresolved:** Precise optical coding, speed, range, atmospheric signal strength, direct-beam confusion duration, Mirrorwake forgery requirements and detection/contest tests. Do not invent quantitative standards.
- **Updated files:** `18_The_Gilded_Coil_Imperial_Gazetteer.md`, `12_Languages_and_Linguistic_Customs.md`, `13_Wakecraft_The_Six_Arts_of_the_Living_Tide.md`, `00_Mystaria_Canon_Index.md`, and this changelog.


### November 4, 2026 — Warlock Manacraft skill-tree replacement and MP costs approved

- **Explicit user decision:** Replace all five formerly approved Warlock skill trees with the recovered *Warlock Skills System, Revised* manuscript's **25 ranks**, without adopting its proposed progressive SP schedule. **All ranks cost 5 SP each**, five ranks per tree, **125 SP mastery**; existing Hero level gates I/1, II/10, III/25, IV/50, V/80 and rank prerequisites remain. Base Manabending remains free and Warlocks cannot generate or internally store mana.
- **New canonical progression:** Mana Reach — Unseen Hand, Crooked Thread, Binding Thread, Walk the Current, Ley Carving; Mana Power — Focused Expression, Flowing Expression, Sustained Expression, Pressure Geometry, Mana Singularity; Mana Harvest — Afterglow, Ambient Harvest, Hollow Radius, Fundamental Conversion, Soul Reaping; Mana Imbuement — Reservoir Seal, Triggered Release, Conditional Enchantment, Spell Imprint, Soulwork; Mana Dominion — Deflection, Spell Theft, Soul Hush, Sovereign Thread, Null Dominion.
- **Mana Singularity (V):** The five holes are **Red Furnace Heart; Blue Shifting Depth; Green Genesis Bloom; White Immutable Crown; Black Final Silence**. These are temporary energy concentrations, not literal infinite-mass black holes.
- **Base Manabending replaced:** Reach = `2 + 2 × effective INT` meters; safe temporary hand holding 30 sec, hard limit 60 sec. **Historical and superseded:** this original version handled `max(1, ceil(natural effective END / 10)) MP` per reference spell-load and held 1–3 loads; the subsequent November 4 direct-hand-capacity ruling above replaces this with **`max(1, floor(natural effective END / 5)) MP` in one hand**. The recovered absorption contest is `min(100%, Warlock INT / (2 × Caster INT) × 100%)`, with current Handling Capacity still limiting each interaction.
- **User approved MP costs in the preceding exchange:** Full rank-by-rank **activation, upkeep, released-energy and conditional fees** are now operative in `04_Warlock_Manacraft.md`, including **Mana Singularity 12 MP activation + minimum 20 MP manifestation energy; 4 MP/round + minimum 10 MP released per round**; **Ley Carving 12 MP activation, 6 MP/minute during alteration and at least 50 extra MP for a lasting regional alteration**; **Soul Reaping 20 MP activation + 5 MP/round**; **Soulwork 15 MP per soul vessel / 10 MP per construct, plus 5 MP/day or 4 MP/day respectively**; **Null Dominion 15 MP + 6 MP/round**. For the remaining 20 ranks, consult the subject dossier; do not infer old rank costs for different powers.
- **Superseded:** Former technique trees, notably Thousand Invisible Hands, Grand Expression, Great Reclamation, Living Arsenal and Absolute Reversal, and their rank-specific MP schedules; the recovered author's proposed **1/3/5/7/9 SP** schedule; approximate 2-meter basic Manabending range and END-sized hand reservoir where inconsistent. Prior **November 3 Warlock approval remains historically true**, not operative for conflicting techniques.
- **Still unresolved:** the former 1–3 spell-load thresholds were **RESOLVED** by direct MP Hand Capacity; higher-rank Imbuement seal/imprint lifetime, exact field radius/limits, same-action harvesting to pay activation, and payment of high activation fees directly from external sources without bypassing active handling remain unresolved. Do not make numerical claims absent explicit approval.
- Updated the owning `04_Warlock_Manacraft.md`, Canon Index and Canon Changelog copies in the downloadable November 4 update.

### November 4, 2026 — Gilded Coil homeland canon approved and reconciled

- The user **explicitly approved** the full early *The Gilded Coil — Heartland of the Naga Empire* manuscript **where compatible with newer canon**. The original source's proposed label is historical, not its current status. The complete owning reference is `18_The_Gilded_Coil_Imperial_Gazetteer.md`.
- **Sole capital:** **Sathryx**. The **Grand Coil Games rotate among major Imperial cities**, not multiple imperial capitals; `17_Imperial_Sports_and_Great_Coil_Circuit.md` is corrected accordingly. No change to approved competition types or calendar.
- **Enslaved population:** Enslaved residents are **a majority in central Imperial cities**. The source's proposed **50–65% estimate is rejected as a canon number**; no replacement numeric rate is established. Population conditions still vary across districts and the frontier.
- **Geography:** southeastern Mystaria, warm river basins, Inner Gardens, Outer Reaches, Silent Works; major Imperial cities **Sathryx**, **Velmora**, **Serrath Quay**, **Kheth-Vael** and their documented specializations.
- **Worldspindles:** Serpentari terraforming installations working through ancient Imperial Grammar and later Kobold **Coilworks**, including Orbs, control interfaces, energy regulators, and Magic Mirrors. Their five-color functions, maintenance demands, finite mana and natural-resource limitations, failure risks and environmental vulnerabilities are approved as described in the source.
- **Institutions:** Conclave of Coils and selected High Matriarch; Scale Register; Scale Guard, **Mirrorwardens**, Coil Tribunals, **Spindlewatch**; Imperial social/legal hierarchy, labor, commerce, law, ecology and regional military strengths/weaknesses.
- **Canon boundaries:** Later approved Psycraft (**Psychics**, not the superseded Crownmind title), Wakecraft, Starspawn, Warlocks, and Imperial sports remain controlling. No new equipment prices, magic-tree ranks, precise infrastructure costs, numerical police powers or unrecorded sporting rules are created here. The recovered source's illustrative external artwork URLs are not canon.

### November 4, 2026 — Six Imperial sports and Great Coil Circuit approved

- The user **explicitly approved the complete recovered *Games of the Gilded Coil* manuscript as canon**, including all six sports, the Great Coil Circuit, professional leagues, institutional roles, broadcast culture, sporting calendar and Grand Coil Games, athlete classes, slavery and emancipation tensions, commercial and political effects, and adventure hooks.
- Created `17_Imperial_Sports_and_Great_Coil_Circuit.md` as the detailed owning dossier: **Coilrun**, **Worldspindle Trials**, **Golden Conquest**, **Thousand Locks Regatta**, **Hollow Crown Expeditions**, **Starwarden Pursuit**.
- **No fabricated tabletop rules:** Original setting descriptions (e.g. typical Coilrun five-person teams, equal Worldspindle judging categories, Golden Conquest's nonlethal restriction) are preserved, but numeric scoring systems, exact standardized match durations and exhaustive eligibility/spell restrictions remain **UNSPECIFIED**.
- The original export's terminal **'awaiting approval'** label is superseded by this explicit user approval. Psycraft is the name of Naga magic; practitioners are **Psychics**. No new mechanical grants are implied by participating in sports.

### November 4, 2026 — Psycraft practitioner title corrected (latest ruling)

- The user explicitly established **Psychic** (plural **Psychics**) as the canonical practitioner title for Naga Psycraft. **Crownmind/Crownminds is noncanonical** and superseded wherever previously applied to practitioners.
- This change affects terminology only. **The Perfect Crown** remains the approved Rank V Telepathy technique. Other distinct established proper names containing *Crown* are unchanged, as are all 15 rank abilities, 75-SP mastery, Sovereign Sense, institutions, and mechanics.
- Updated `15_Naga_Psycraft_Canon.md`, `00_Mystaria_Canon_Index.md`, and `08_Other_Crafts.md` to use the new title consistently.

### November 4, 2026 — Naga Psycraft approved; Crowncraft renamed

- User explicitly approved the full recovered **Crowncraft — The Psychic Magic of the Naga** manuscript as **CANON**, with one exception: the magical tradition is now called **Psycraft**. **Crowncraft is superseded as the name of the tradition**, not as a separate surviving Craft.
- `15_Naga_Psycraft_Canon.md` is the controlling subject dossier. Naga are predominantly blue-affined; practitioners are **Psychics** under the subsequent November 4 terminology ruling (the earlier **Crownmind** title is superseded). Free **Sovereign Sense** includes **Unseen Touch**, **Felt Heart**, and **Moment's Warning**.
- Approved disciplines: **Psychokinesis** (I Invisible Grasp; II Phantom Fingers; III Kinetic Weave; IV Momentum Sovereignty; V Imperial Burden); **Telepathy** (I Heartreading; II Whispering Mind; III Velvet Enchantment; IV Sovereign Suggestion; V The Perfect Crown); **Divination** (I Premonition; II Forked Choice; III Unfolding Moment; IV Threads of Tomorrow; V The Thousand Futures). **15 ranks at 5 SP each = 75 SP**, Heroes start with 0 SP.
- The manuscript's cultural material is approved, including the three Imperial academies, Naga–Kobold manatech relationships and Crown Mirrors, imperial institutions and slavery dynamics, sports connections, and three universal limitations (concentration, finite mana, contestable effects).
- **Unspecified:** fixed MP prices for individual ranked techniques, precise ranges, numeric effect sizes and some competition regulations. These are not license to invent canon. Previous `08_Other_Crafts.md` statement that the Naga rank names are unavailable is superseded.


### November 4, 2026 — Blood Boon cost boundary clarified (latest ruling)

- The user explicitly instructed that the activation-cost table match the approved formula `ceil(Hero Level / 25)` MP. Exact level multiples of 25 remain at the lower cost (25 = 1 MP, 50 = 2 MP, 75 = 3 MP, 100 = 4 MP); costs rise at 26, 51, 76, 101, etc.
- Supersedes inconsistent MP figures in the original *Sanguine Arts — Revised Vren Abilities* table, not its ability-development milestones. `14_Vren_Sanguine_Arts_Canon.md` is updated accordingly.


### November 4, 2026 — Sanguine Arts approved (current ruling)

- The user explicitly approved both **The Six Disciplines of the Vren** and **The Sanguine Arts — Revised Vren Abilities**. The latter overrides conflicting rank details; unchanged material from the former remains canon.
- Created `14_Vren_Sanguine_Arts_Canon.md` as the full dedicated reference; **six Disciplines × five ranks × 5 SP = 150 SP**, starting Vren Hero SP 0; innate Blood Boon free. Black mana affinity.
- **Blood Boon** now lasts 1 minute with no upkeep, scales in cost with Hero level, cannot stack with itself, and can be shared through **Crimson Communion** at level 40 using Bloodbond Rank I or better (separate activation and cost per recipient).
- **Blood Magic IV:** Blood Temper replaces Scarlet Scripture. **Pulse Echo:** senses nearby blooded creatures without consent or an existing bond. **Beastheart III–V:** Fight or Flight, Predator's Fixation, The Deathless Beast replace Packbreaker, Feral Momentum, The Beast Uncrowned. **Celerity III:** Between Heartbeats replaces Hands Between Heartbeats.
- Beastheart grants **+5 effective STR per rank**, Celerity **+5 effective SPD per rank**, both after racial multipliers. Other four disciplines grant 0-MP cantrips at baseline.
- **RESOLVED November 4, 2026:** User ruled that Blood Boon activation costs must match `ceil(Hero Level / 25)` MP. At level 25 cost is **1 MP**; at level 26 cost is **2 MP**. Intervals: 1–25 = 1 MP; 26–50 = 2 MP; 51–75 = 3 MP; 76–100 = 4 MP; increase every 25 levels thereafter. Previously contradictory level-table costs are superseded; all ability-development milestones and durations remain intact. Other unspecified MP costs and hard range/duration parameters remain unspecified.
- Earlier `08_Other_Crafts.md` Vren summary is historical/overview only where inconsistent with the dedicated file.

### November 4, 2026 — Wakecraft six-arts approval added to modular library

- User approved `13_Wakecraft_The_Six_Arts_of_the_Living_Tide.md`: innate Hydrokinesis plus six skills (Wakeforce, Longwake, Deepdraw, Mirrorwake, Reefcalling, Saltwake), each five ranks for 150 SP total. Earlier three-technique Wakecraft overview is superseded as a complete progression source.


### November 4, 2026 — Linguistic expansion recovered and fully approved (current ruling)

- The user recovered the original full linguistic proposal (`Pasted text.txt`) and the subsequent revised proposal (`Pasted text (2).txt`). The user explicitly clarified that **the entire original proposal and all unchanged material are canon**, subject to **later revisions taking precedence**. Earlier unrecovered-source warnings in the November 4 draft are superseded.
- Approved `12_Languages_and_Linguistic_Customs.md` as the owning dossier for Roadspeech, Imperial Coil Speech, Canopy Cant, Red Cant, race-related speaking tendencies, insults, compliments, curses, phrase meanings and misuse, slang, social etiquette, slaveholder/enslaved speech, and illustrative dialogue. These are cultural tendencies, not mandatory racial accents.
- **Current Naga wording:** “Mind your tail.” and “A monarch needn't hiss.” Supersede “Mind your coils.” and “A crown needn't hiss.”
- **Current Kobold wording:** “Son of a glitch!”; “Almost done.”; “Bright as a first spark.”; “Are your scales just for show?” These supersede “Cracked lattice!”, “One more adjustment.”, “That's a First Spark”, and “You were never worth the imprint.” Added “Broken mirrors.” (bad luck / “Why me?”). **“Oops!”** is an imminent-catastrophe warning even when the speaker caused no error. Kobold imagery emphasizes illumination, Mirrors, Orbs and discovery over mechanical-part sayings.
- **Current Moontouched wording:** “Sweet Surrender!” and “Some doors are best left closed.” Supersede “Surrender's ears!” and “Not every door needs opening.”
- **Current Drider wording:** “You enjoy the sentence more than the verdict.” Supersedes the earlier “...more than the justice.”
- **Firstshaped slur:** **Pet** supersedes **Petshape**.
- **Muzzle-mouth:** Approved derogatory term for enslaved people frequently muzzled or gagged, especially in the Gilded Coil; **not** a legal slave category. May be used against people no longer restrained; rare reclaimed use among enslaved communities does not neutralize it.
- **Speaking in Colors:** Explicitly approved, definitive casual dialogue convention. The five magical energies are typically named by color (“shape the white,” “out of black”); the term **mana** remains standard in precise, academic, technical, mechanical, and Shimmer contexts. The magic mechanics themselves are unchanged.
- Added approved magical praise/insults/slang for the represented peoples. Treat scenes as examples of linguistic style, not new mechanical permissions.
- **RESOLVED November 4:** Kobold linguistic canon remains valid; Kobolds now appear in `02_Races.md` with explicitly approved starting attributes and modifiers. Any unapproved Orbcraft rank progression remains undocumented.
- Updated the Canon Index to reference the recovered and operative linguistic dossier.

### November 3, 2026 — Drakyn finalized

- Racial name changed permanently to **Drakyn**, singular and plural.
- Approved Starspawn-hunter origin, engineered Tiamat, Mana-eating physiology, hoards and Hoardgrowth, Treasure Compass, physical forms and egg-acquired elements.
- Approved all **five × five Wyrmcraft disciplines** and flexible magical gift dragonmarks, subject to stated unquantified balance questions.
- Approved native Sorcery discount **2 SP** per Incantation or alteration; standard one-color mastery **60 SP**.

### November 3, 2026 — Centaurs and Celestite finalized

- Approved race, culture, holy **Veyravel**, Saddle Vow, Yokebound, Ponies and green-mana Anvilcant.
- Revised initial Centaur DEX/END/INT **down by 2 each**: current base **STR 11 / DEX 3 / END 8 / INT 6 / SPD 10**; effective **13.75 / 3 / 8 / 6 / 12.5**.
- Approved twelve materials: Boughsteel, Trufula, Adamantite, Nullporcelain, Skyvein, Reprise Bronze, Oathsilver, Bellcopper, Hearthiron, Thornspring, Glassweave and **Celestite**.
- Expanded Bellcopper sonic use and Hearthiron glowing heat retention over years. Glassweave is transparent/tough, unlike anti-magic/brittle Nullporcelain.
- Approved Celestite's triune divine forging, anti-ley-line field, immortal severance, unconditional Drakyn treasure sense, XP/level soul erosion and conviction/False Apotheosis danger.
- Approved initial six Anvilcant trees, **150 SP** complete, plus Centaur half gear Soul Strain and half gear stat bonuses.

### November 3, 2026 — Smithcraft replacement design requested, **NOT YET CANON**

- User explicitly declared **Formwright and Monumentcraft blank/open for replacement**.
- User chose to preserve the equipment quality/Gem benchmarks, enable modular slots, use hybrid additional Soul Strain, add color-specific casting implements and conservatively priced rechargeable mana storage; the user also selected specific conceptual restrictions for clockwork.
- An assistant then proposed eight skills / **200 SP**, named Socketwright, Clockwright, Cogmarshal, Hostforge, plus detailed runes, socketed gems, Manacisterns, Cogmind Calamity and command economies.
- **This detailed proposal was never explicitly approved afterward.** Maintain the distinction: six-tree snapshot is last approved system, with two legacy branches under reconsideration. The 8-tree system is **not** automatically canonical.

### November 3, 2026 — Sorcery approvals

- Ordinary Incantations and alterations **3 SP each**; Drakyn **2 SP each**.
- Blue, Green, White color catalogues were approved earlier (five bases and five alterations each); their **exact 25 chosen names** are not all present in locally accessible export artifacts.
- **Black's five groups and 25 selected alterations explicitly approved.** Full named list in `03_Sorcery.md`.
- **Historical provisional Red accounting — SUPERSEDED November 4:** Earlier reporting listed **26 alteration purchases** and 93/62 SP, including one unidentified seventh Ignis slot. The author's later explicit ruling removed that unidentified purchase. The current approved ledger is **25 alterations** and **90/60 SP**, preserving all named effects.

### November 3, 2026 — Jestercraft superseded

- Replaced **inversion / curses / misfortune / Recompense / Final Inversion** Jester class with **artifact-bound living Regalia Craft**.
- Approved six free Rank I foundations and 36 individually purchased features: 18 modifiers at 3 SP, 18 applications at 4 SP = **126 SP**.
- Approved physical Stitches and their five states, regeneration costs, kinetic conversion with movement benchmarks, real resizing bows, far-reaching Seamcraft, Black Masquerade and rank-specific effects.
- Later clarified **Regalia are fully sentient and speak**, originated as punitive Serpentari garments, and mostly **chose to weaponize rather than hollow victims**.
- **Hollow Jesters remain**, but not via Final Inversion/Recompense.

### November 3, 2026 — Warlock rank file approved

- User supplied complete `Mystaria_Warlock_Skills.md`, initially labeled proposed, and explicitly **canonized its full rank descriptions and MP costs**.
- Integrated established **5 SP/rank** sequence across five trees: **25 ranks / 125 SP total**.
- Mana Reach, Mana Power, Mana Harvest, Mana Imbuement, Mana Dominion are transcribed fully in `04_Warlock_Manacraft.md`.
- The November 4 replacement **supersedes the old Reach progression**. Higher-rank Imbuement longevity and same-action activation funding remain unresolved; see the latest November 4 entry.

### November 3, 2026 — General Shimmer progression override

- Newer project decisions use **2 base-stat allocations per level**, plus **+1 to all five base stats every fifth level**; old Nov 1 compendium had **1 Attribute Point per level**. Newer explicit mechanic controls.
- Skill Points, attribute allocation points, Gems, MP and Soul Strain must remain distinct.

## 3. Superseded concepts not to revive silently

| Old assumption | Controlling later rule |
|---|---|
| Dragons called Vyrathi or similar names | **Drakyn** |
| Drakyn naturally regenerate mana at rest | **0 natural MP, 0 rest regeneration; must consume mana-bearing creatures** |
| Drakyn elemental identity purely inherited by genetics | **Element set by egg incubation environment** |
| Drakyn spell-gift mark only teaches concepts, not an Incantation | **May grant the purchased-knowledge effect directly, with recipient Soul Strain / SP buyoff** |
| Jester inversion, Recompense and Final Inversion | **Physical Stitch / Regalia six-discipline system** |
| Regalia merely semisentient or mute | **Fully sentient, speaking, independently motivated** |
| Hollow Jesters removed with inversion system | **Hollow Jesters still exist as rare narrative outcome** |
| Moontouched categorically unable to become Jesters | **Any race capable of Donning can bond with Regalia** |
| Warlock old per-rank MP costs | **The old techniques and their MP fees were superseded by the November 4 replacement; new approved costs govern** |
| Warlock rank effects absent | **Current recovered replacement 25 ranks and approved MP fees reside in `04_Warlock_Manacraft.md`** |
| Centaurs have initial DEX 5, END 10, INT 8 | **DEX 3, END 8, INT 6** |
| Celestite a mundane high-tier metal or extra numerical upgrade | **Unique divine relic outside regular five quality tiers** |
| Proposed 8-tree Anvilcant treated as already approved | **Not canon until explicitly approved** |
| Older Shimmer progression of 1 stat point per level | **Later 2 per level +1 all every fifth level** |

## 4. Priority unresolved issues (truthfully labeled)

1. **Red Sorcery purchase count — RESOLVED November 4:** the author removed the unidentified seventh Ignis purchase, establishing **25 Red alterations**, **90 SP ordinary / 60 SP Drakyn**; all named abilities remain.
2. **Approved Blue/Green/White chosen alterations:** obtain definitive exports or pasted selection lists, not just proposal menus.
3. **Revised Anvilcant:** decide whether to approve Socketwright + three clockwork branches, the 200-SP total and concrete rank mechanics; until then, document proposal separately.
4. **Modular equipment:** approve or revise slots, rune family rank values, socketed gem activation rates, multicolor surcharge and Manacistern caps/strain; current numbers are examples, not canon.
5. **Warlock Reach:** Former Rank IV remote-anchor language is superseded. The current basic range is `2 + 2 × effective INT` meters; Rank IV Walk the Current uses an existing ley line and does not have an approved fixed distance.
6. **Warlock Imbuement:** the former Living Arsenal is superseded. Rank I Reservoir Seal lasts one hour; Rank IV imprint and Rank V Soulwork lifespan remains unquantified aside from the approved daily upkeep fees.
7. **Warlock activation:** determine whether harvested mana from the same action can pay initial costs, and whether high fees may be incrementally routed from external sources; no automatic bypass of Handling Capacity.
8. **Drakyn Wyrmcraft:** outstanding Caught Breath prepaid cost/color, Songmark strain and cap, Silent Thunder mark strain, and precise metamagic surcharges.
9. **Firstshaped-specific racial rarity:** especially common in Centaurs/Drakyn vs older generic ~1 in 50.
10. **Other racial Craft trees:** complete, individually approved rank descriptions were not supplied; do not invent them in `08_Other_Crafts.md`.

## 5. Maintaining this library

1. When a new decision is explicitly canonized, update its owning dossier and **this changelog**; update `00_Mystaria_Canon_Index.md` if precedence or file boundaries change.
2. Preserve old approved details when revision scope is limited, but label superseded sections clearly rather than leaving contradictory alternatives as coequal rules.
3. When an ability remains a **proposal**, place it under a heading that explicitly says so and keep it separate from the operative rules.
4. Do not replace original project Files merely by generating a download in chat. Upload/replace the new files within the Mystaria Lore project's **Files section**.
5. In a different ChatGPT project conversation, open `00_Mystaria_Canon_Index.md` and the relevant subject files before adjudicating numerical mechanics.


## Approved Nymbrin canon and Hexen terminology — November 4, 2026
The author explicitly accepted **all current Nymbrin lore** and selected **Hexen** for mutants. Full approved content is preserved in `20_Nymbrin_Wetcraft_and_Hexen_Canon.md`: frog anatomy and rapid lifecycle, pools and absentee parenting, Golden Lease, ranks and debt enforcement, Baphomet observances, Duskpaw shared history/alliance, Wakebound, El Dorado and lost true stones, modern homunculi, six Wetcraft domains, permanent mutation, living machinery, ardor draughts, five intoxicants, Pazara/chitin, elementals, hex/Haze/clearbreaths and toxic dragon eggs.

**Supersession:** Golden Lease replaces Gilded Term; Hexen replaces provisional mutant collective names; playful tab/gig/bet speech supersedes the stronger legalistic characterization. Lost true stones violate equivalent exchange; modern stones obey it. Existing Nymbrin mutant legal protections are an explicit exception to general Hexen exclusion.

**Affected files:** 00 index, 01 world, 02 races, 06 Drakyn, 08 crafts, 09 economy, 10 changelog, 12 linguistics, 14 Vren, new 20 dossier and new 21 proposal. Cross-references preserve existing mechanics and keep the centaur modular overhaul unapproved.

**Gameplay direction:** all Nymbrin alchemy generates hex. Consumable power is tied to Gem cost, calibrated around a 30% Hero-budget allocation. `21_Nymbrin_Skill_Options_DRAFT.md` offers 12 candidates per discipline plus custom input; none of these newly generated techniques is approved by the preceding lore acceptance.

**Unresolved:** starting stats and numerical jumps; clutch size; full rank/SP/MP/action rules; exact pricing/yield and budget window; quantitative hex system; exact ancient chronology and stone manufacture; future elemental race. Starspawn retain their established God War origins and Duskpaws their Night of a Thousand Locks liberation.


## November 5, 2026 — Approved combat/endurance rules and clarification

**CANON:** Combat-only +10 offset before quadratic impact comparison, applied to attack and defense, without changing actual effective attributes or unrelated costs; exact impact thresholds 0–0.75 superficial, >0.75–1.75 solid (+1 injury), >1.75–3 devastating (+2), >3 overwhelming (+3). **Dagger = 1.0× STR, gauntlets = 1.0×, unarmed = 0.85×**; previous 0.85× dagger proposal superseded. Injury-stage stat penalties −5%, −10%, −15% total. Heroes and Legends have two extra Shimmer Guard injury buffers; Heroes' purple eye glow appears beyond the first wounded state, can be concealed at the price of full pain but with no further fixed numerical penalty; Legends receive only the extra guard states and may collapse immediately if their Guard is destroyed by loss of reputation and accumulated injuries exceed normal mortal capacity. A fully healthy protected Hero/Legend cannot ordinarily be removed with one overwhelming attack without DM exception. Superficial wounds recover on long rest; meaningful injuries require realistic healing durations, possibly permanent if not magically healed; magical treatment is standard. Recipient heal burn stacks with Soul Strain (5% superficial, 20% ordinary injury, 10% first extra Guard injury and 15% second extra Guard injury); up to two short rests partially reduce burn and a long rest removes it entirely. Guns' inherent damage is independent of Strength; damage/required-STR handling relationship, bracing, weight vs recoil, and extreme recoil injury (+1 wound state) approved in principle. **Adamantite** spelling confirmed (not Adamantine); **Crownsalt** may also be termed **gunpowder**. Trufula frame combustion restrictions remain in place.

**UNRESOLVED/PROPOSAL:** Numerical armor scaling/penetration and Centaur Smithcraft integration; exact firearm handling cutoffs, recoil wound trigger and sample gun ratings; short-rest heal-burn fraction and precise strain translation; coordinated attack numeric formula, separate physical/psychic tracks, precise Legend reputation threshold. The adopted armor combination formula remains a working formula pending full scaling balance. Dedicated owner: `22_Combat_Endurance_and_Shimmer_Guard.md`; cross-references: `01_World_and_Shimmer.md`, `07_Centaurs_and_Smithcraft.md`, `09_Equipment_and_Economy.md`, `00_Mystaria_Canon_Index.md`.

## November 5, 2026 — Power and Resistance vocabulary (CANON)

**Approved nomenclature:** **Power** is a broadly usable scaling result for attacks, spells and other effects, not necessarily damage. **Resistance** is **effective END** (without adding the combat-only +10); type-specific resistances can organize narrowly applicable bonuses or penalties. **Defense** covers withstanding/mitigating an effect through Resistance and applicable protection, and **never includes evasion**. Evasion is resolved separately. Continue to derive natural **Defense Power = (Resistance + 10)²** and attack **Power** quadratically, retaining impact thresholds, penalties and weapon ratios. No numeric spell scaling or armor stacking is approved by renaming the terms. Cross-reference `22_Combat_Endurance_and_Shimmer_Guard.md`; detailed modifier precedence for casting implements, armor, oil vulnerabilities and barriers remains **UNRESOLVED**.


## November 5, 2026 — Speed / evasion philosophy and pressure ladder (CANON scope)

**Approved:** Primary skill output focus on STR/DEX/INT (future general SP skills are anticipated but **not designed or priced**); SPD helps both avoiding and landing attacks, favoring evasion and never directly providing extra attacks per action. Evasion negates attacks, and rarer glancing blows mitigate **roughly half of resulting injury states**, not offensive Power; rounding not fixed. END/Resistance is reliable against repeated weaker attacks while SPD is relatively strong against single dangerous attacks. Armor directly penalizes SPD (exact rates pending). The baseline Evasion Ratio uses `(defender effective SPD + 10)/(attacker effective SPD + 10)` with the **preserved six-category table** in `22_Combat_Endurance_and_Shimmer_Guard.md`: Certain <0.50; Easy 0.50–0.79; Average 0.80–1.24; Hard 1.25–1.49; Very Hard 1.50–2.99; Impossible ≥3.00. Circumstances and clear routes control whether an extreme disparity can be overcome. **Four pressure states**: Open, Pressured, Trapped, **Extreme Pressure** (e.g. entire army converging), without making a target categorically helpless. Area attacks, coordinated opponents, encirclement and terrain counter evasion. **Shimmer Guard predicted evasion paths** are now an in-world feature and rare DM tool for extreme Speed mismatches, **not** guaranteed hit, extra attack, or +SPD; exact thresholds/effects still unresolved. The earlier percentage-based Proposal Three is **disfavored**, retained only if needed as hidden rare technical balancing, never a play-facing mechanic.

**Unresolved:** Exact pressure-category shifts, glancing rounding, armor SPD penalties, final deterministic hit method, Shimmer prediction trigger/benefit, and SP skills. **Separate proposal, NOT APPROVED:** shifting all racial starting attributes +10; that would affect racial modifier order, MP, Channel Limits and INT-based ranges. Existing actual attribute baselines and combat-only +10 remain operative until explicit approval.

## November 5, 2026 — Approved +10 starting-attribute migration (LATEST)

**CANON:** Increase every approved **Hero racial starting base attribute +10**, **before** racial percentage modifiers, intentionally increasing differences from racials; clamp all attributes, including special monsters, to absolute **minimum 1**. Monsters may still possess any stat in **1–9** (do not mass-upgrade monster stats). Rebase effective-stat milestones **25 → 35**, **100 → 110**. Replace the combat-only +10 formulas with direct squares of **new effective** STR/END and direct new SPD ratio (old +10 is superseded; no double count). Maintain original injury and six-tier evasion tables. Adopt the quadratic illustrative lifting benchmark `100 × (effective STR / 15)^2` lb for one-time waist-height lifting, with STR 10 ≈44 lb, STR 15 =100 lb and STR 25 ≈278 lb; anatomical limitations still apply.

**MAGIC:** Natural MP intentionally increases to floor(rebased effective END) for mana-producing races; **Moontouched and Drakyn retain 0 natural MP**. Attribute-derived **short-range magic and Channel Limits** use clamped legacy-equivalent INT `max(1, new effective INT − 10)` (e.g. Hydrokinesis `2 + max(1, INT − 10)` m; Manabending `2 + 2×max(1, INT − 10)` m). At new effective INT 11, these ranges are **3m/4m** respectively, not above 10m; previously longer-range magic's nature is preserved. Warlock temporary hand capacity uses `max(1, floor(max(1, new natural effective END − 10)/5))` to avoid an automatic handling buff. Channel Limits do NOT increase by two due only to stat rebase. Minor racial-percent differences in these conversions are intentional. All existing mana-derived ability costs must be **reviewed later**; no SP/MP costs automatically changed now. Further fixed attribute prerequisites and historic benchmark examples need audit. Owning revised files: `01_World_and_Shimmer.md`, `02_Races.md`, `04_Warlock_Manacraft.md`, `07_Centaurs_and_Smithcraft.md`, `13_Wakecraft_The_Six_Arts_of_the_Living_Tide.md`, `14_Vren_Sanguine_Arts_Canon.md`, `15_Naga_Psycraft_Canon.md`, `22_Combat_Endurance_and_Shimmer_Guard.md`.


## November 5, 2026 — DEX stealth/contingencies, non-Hero training, movement tiers (LATEST)

**CANON:** DEX combines precise timing and physical perception, improves conventional stealth **and counter-stealth** through quiet movement, cover and reading physical cues, and does **not** create visibility-proof stealth in the open. It does **not** automatically grant specialized trained crafts such as lockpicking. Prediction rule preserved at **DEX ≥ 75% of target SPD**; new exception **DEX ≥ 200% of target SPD** gives no penalty from an incorrect prediction (well-built contingencies), though unrelated tactical risks still apply. **Non-Hero mortals can increase attributes through training**; **Heroes cannot**, because Shimmer level/experience growth governs their stat gains. Ordinary marathon capability benchmark is **END 25**, not 15, subject to circumstances.

**High-speed attacks:** An actual sufficiently accelerated movement-assisted charge can obtain a **modest Power benefit**, based on **relative closing speed**. No extra attacks. If an opponent's matching movement cancels relative closing-speed difference, the movement-derived Power bonus is nullified. Maximum movement is **dash**; sprint is one chart tier below; sustainable jog two below. Numeric movement mph, required run-up, travel durations, and approximate **+25% Power at 100 mph and +50% at 500 mph** are still **UNRESOLVED/PROPOSED CALIBRATION**, not universally applied multipliers. Preserve existing firearm benchmarks, evasion difficulty and pressure categories.

**Proposed only: PROFICIENCIES**: Possible later general/mundane, SP-purchased, attribute-gated expertise, including lockpicking and ordinary crafts. **NONCANON and requires further development**; raise only if the author proposes adopting a general skill system from another RPG, **not when discussing Mystaria magic Skills/Crafts**. No SP costs, proficiencies, prerequisites or unlocks established. Owning files: `22_Combat_Endurance_and_Shimmer_Guard.md`, `01_World_and_Shimmer.md`, `07_Centaurs_and_Smithcraft.md`; navigation in `00_Mystaria_Canon_Index.md`.


## November 5, 2026 — Modular Anvilcant, Cogminds and divine equipment (LATEST)

**CANON — changed:** Author approved the **eight-discipline Anvilcant restructuring** (Orewhisper, Oathsteel, Thunderforge, Hearthsong, Socketwright, Clockwright, Cogmarshal, Hostforge) replacing Formwright/Monumentcraft; **40 ranks × 5 SP = 200 SP mastery**, retaining native level gates and existing four settled craft trees. New active magical rank details remain subject to review, not blanket approval of earlier proposals. Oathsteel natural effective **INT/END minima** increase by **+10** for qualities I–V: INT **18/26/40/60/90** and END **20/30/45/65/90**. **Cogmind Calamity lore approved**: world-altering Cindara clockwork needs direction and cannot normally think, while forbidden historic autonomous Cogminds escaped purpose constraints; exact history unresolved.

**CANON direction:** Choose **fully modular Architecture B**; equipment separates physical form, materials, quality and installed magic. Retire the **Moonlit Forge's independent +1 to +5 divine-reinforcement system and associated price ladder** for ongoing designs, retaining quality I–V and preserving older shop material as historical records only. Shimmer shop equipment can be purchased in advance at fair prices; usage requires appropriate stats. Centaur expertise and multi-skill/cooperative mastery required for the highest gear, implementation pending. Physical items limited by requirements, material, coverage, mass and speed burden; magical items mainly by Soul Strain rather than Gem price. No armor-suit stacking except appropriate light protective layers in gaps. Implements cannot multiply a single magic technique by being equipped multiple times. Weapons may use STR, DEX, either or both; more rewarding dual-scaling needs actual two-stat prerequisites. No numerical weapon/armor progression finalized.

**CANON reservoir lore:** Divine reservoirs formerly tentatively named Manacisterns recharge when a compatible-affinity creature **prays with devotion**; prayer may be directed to *anyone*, not merely goddesses. This exploits a simplified divine/devotional principle akin to Shimmer/Legend energy; most religious orthodoxy mistakenly claims otherwise, and knowledgeable smiths may be forbidden to voice the truth to masters. User targets approximately **1 MP per turn per 10 effective END**, **10% efficiency for unenthusiastic prayer**, **100% for wholehearted devotion**; exact charging-rounding, capacity and action details remain unresolved. Prayer is necessary and not replaced by passive rest or ordinary direct mana transfers.

**EXPLICIT PROPOSAL/UNRESOLVED:** Command Loom as craftable/purchasable Cogmarshal augment (not an SP tree); choice of reservoir names; Longsong +100% per rank duration; Thrift flat −1 to −5 MP versus 5%–25%; individual rune effects/numbers; equipment slots; numerical armor SPD/STR relief; tier attribute-requirement discounts and STR 400 weapon scale; shop advancement/cooperation prerequisites; precise Cogmind history and higher active Anvilcant ranks. Preserve existing costs, material identities, firearms and skill-rank requirements except explicit changes above. Owners: `07_Centaurs_and_Smithcraft.md`, `09_Equipment_and_Economy.md`; index update required.


## November 5, 2026 — Passive elemental rune resolution selection

**CANON SELECTED:** The author specifically selected **model B: Conditional Contact Effect**. Passive fire/ice/water/lightning/air/toxic runes apply a weaker, resisted **contact rider** on a weapon strike that genuinely contacts a protected surface or target, potentially affecting a wearer despite an otherwise superficial physical attack. A full dodge yields no contact effect. Not an independent full elemental Power attack (rejected A) and not default fractional physical-Power conversion (rejected C). Preserve rank-V full elemental transformation **replacing original material bonus**, special magic Resistance effectiveness, physical coverage/insulation, six-category Speed difficulties, END baseline and ordinary injury thresholds. **UNAPPROVED numerical proposal:** rank I–V intensity coefficients, contact bands, injury caps/durations, specific resistance/armor factor suggestions are in `24_Modular_Equipment_Design_Options_DRAFT.md`. Hex doses and combat side effects remain unresolved and must remain consistent with Nymbrin pollution lore. Owning references: `09_Equipment_and_Economy.md`, `22_Combat_Endurance_and_Shimmer_Guard.md`.


## November 5, 2026 — Leywell faithwells, Loom prices and Elemental Magnitude (LATEST)

**CANON:** Leywell is the official name; *well* is everyday shorthand and **faithwell** is common religious terminology for the same prayer-charged item. Command Loom portable Cogmarshal-graded Gem prices **12/28/55/90/140** by ranks I–V **approved**, without approving doubled Command Point capacities or other operations. High-grade clockwork **constructs derive basic attributes principally from materials, engineered chassis, gearing and construction**, rather than copying a magic sword's attribute-bonus model. Their integration with **Leywells, passive/active runes, Cogmarshal/Command Loom, material-specific core stat sheets** is *deferred until other crafting mechanics are completed*. Six previous machine names remain design candidates: Windling, Quickstep, Iron Servitor, Bulwark, Gearsteed, Siege Engine; **stat sheets, recipes and upkeep unapproved**.

**ELEMENTAL:** Rename *Contact Pressure* to **Elemental Magnitude**, establishing elemental/energy effect intensity and resistance as the baseline framework for energy-driven attacks and magical techniques, especially Sorcery (whose independent INT, MP, Incantation and alteration rules must remain). Elemental Magnitude should be visible as important information in future applicable spell entries. Establish three **Elemental Status** severity ranks independent of five passive rune ranks; status may increase own-element susceptibility, and rank III passive runes must be eligible to cause statuses under successful contact and relevant resistance. Standing water/soaking improves lightning contact where conductive path exists; no factor approved. **The author floated specific fire/ice/lightning/water/air/hex status effects as PROPOSALS**, not approved rank numbers or calculations. Universal energy 'immunity' is interpreted as **near-immunity**, including fire Drakyn versus heat; no absolute energy invulnerability or fixed bypass magnitude.

**RANK V:** Author accepted retaining ordinary appropriate physical-attack Power **plus the limited passive elemental rider** when a weapon becomes fully elemental, while **replacing original material special bonuses**. Exact handling where physical mass/shape changes is unresolved.

**NOT YET CANON:** General Elemental Magnitude mathematical formula for sorceries, all status thresholds/debuffs/durations, passive rank coefficients, ice freeze scaling and spell use, hex statistical penalties, construct stat blocks, Loom operating parameters. Relevant subject files `01_World_and_Shimmer.md`, `03_Sorcery.md`, `06_Drakyn.md`, `07_Centaurs_and_Smithcraft.md`, `09_Equipment_and_Economy.md`, `22_Combat_Endurance_and_Shimmer_Guard.md`; proposals `24_Modular_Equipment_Design_Options_DRAFT.md`.

## November 5, 2026 — Name and action-economy clarification

Mystaria is the canonical world name, superseding the mistaken name Cindara in the clockwork notes. The user outlined revised lightning, water, air and hex status goals. Detailed numbers still require review. Clockwork squads should act together on their commander's action and offer tactical choices rather than multiplying independent attack turns or complete individual injury trackers. Exact command limits, squad resilience and conditional attacks remain proposals. See `07_Centaurs_and_Smithcraft.md` and `22_Combat_Endurance_and_Shimmer_Guard.md` for full details.

## November 6, 2026 — Cogsong, mandatory Loom, squad reinforcement and Windling CP (LATEST)

**APPROVED:** Clockwork's encoded acoustic mechanical Starsong is officially named **Cogsong**. Command Looms are **mandatory**, not optional, for Cogmarshal control and Cogsong transmission. Their established prices **12/28/55/90/140 Gems** remain. The older proposal for native CP without a Loom and optional doubling by Loom is **SUPERSEDED**; a no-Loom commander cannot issue machine orders. Full CP-by-rank capacity and Loom quality interactions remain UNRESOLVED.

**APPROVED:** Standard ordinary homogeneous squad size **4 constructs**; fewer weaken, more strengthen, with no extra full attack per machine. **Reinforcement model B:** increasing a standard 4-machine squad to **5–8 machines** commits **+1 CP** beyond its baseline squad cost, with **one combined attack per order**; over eight must be separated into multiple ordinary squads. **Windlings are explicitly exempt**: every **1 CP controls 4 Windlings**, allowing large swarms, rather than applying ordinary reinforcement pricing or squad-size limits. Windling swarms remain subject to the commander's one-ordered-attack action economy, not unlimited individual attacks. Their suppression/evasion, damage, lifting, attrition and sniper counterplay numbers remain proposals.

**APPROVED:** Simple nonoffensive standing orders **persist until completed** without repeated commands; **each new attack requires a new commander command/action**. No indefinite automatic volley/suppression attack loop. Preserve one-type squads, passive support Gearsteeds/Bulwarks, special Windling swarms, Quickstep skirmish, independent Siege Engines, gear keys, power-dependent fallback, and field repair as previously approved in conversation. Files affected: `07_Centaurs_and_Smithcraft.md`, `12_Languages_and_Linguistic_Customs.md`, `00_Mystaria_Canon_Index.md`, `24_Modular_Equipment_Design_Options_DRAFT.md`. Unapproved: baseline CP by Cogmarshal rank, regular squad costs, Loom range and upkeep, exact numerical swarm combat benefits.

## November 6, 2026 — Cogmarshal CP progression explicitly approved (LATEST)

**CANON:** The user approved the mandatory-Loom Cogmarshal capacity table **I 2 CP / II 4 CP / III 6 CP / IV 8 CP / V 12 CP**. Earlier language marking 2/4/6/8/12 as a mere proposal is **SUPERSEDED**. The no-Loom/native CP model remains rejected: a functioning compatible **Cogsong Command Loom is mandatory**. With the separately approved **4 Windlings per CP**, theoretical maximum Windling counts when all CP are allocated to them are **8/16/24/32/48**. These are **control capacities, not extra attacks**. Each new offensive order still costs a meaningful commander action. Ordinary squad size four and +1 CP to reinforce to five–eight are unchanged. Rank SP costs and prerequisites, Loom Gem prices, support units and existing shutdown rules are preserved. **Still unresolved:** CP costs for non-Windling types, Loom grade/capacity compatibility, acoustic range, swarm pressure, protective screening, attrition, lift, MP upkeep and individual construct stat sheets. Owning reference: `07_Centaurs_and_Smithcraft.md`; design proposals: `24_Modular_Equipment_Design_Options_DRAFT.md`.

## November 6, 2026 — Windling tactical saturation, stat-gated pressure and sonic warfare (LATEST)

**APPROVED from immediately preceding user turn:** mandatory-Loom Cogmarshal CP by rank **2/4/6/8/12**; the earlier proposal status is superseded. Four Windlings per CP gives maximum counts 8/16/24/32/48 when fully allocated, without extra actions.

**APPROVED now:** Windlings use **flexible tactical saturation (option C)**, supporting harassment, screening, distraction and collective lifting. Tactical pressure is never automatic from simply acting or existing near an opponent; compare group-relevant stats and the target's defenses, with a **diminishing stat-based size multiplier and eventual hard cutoff** so a weak swarm cannot automatically pressure an overwhelming Hero. **Every squad type** benefits from additional member-count ability unlocks, not merely extra raw damage. Specific formulas, thresholds and unlock tables are **PROPOSALS**.

**APPROVED construct casualties:** For ordinary small/medium constructs, resolve damage as the **number of machines felled per attack**, constrained by Power/Resistance and the attack's actual physical coverage. Powerful wide greatsword attacks and flavor-described multiple dagger cuts can remove multiple constructs within **one existing attack action**, without granting extra attacks; single-target rifle fire generally affects one unless its actual coverage/piercing differs. **Largest Siege Engines** retain their own injury states. Exact counts, coverage and material stats remain unresolved.

**APPROVED Windling signature:** built-in **sonic music box** using harmful sound that does not interfere with Cogsong command frequencies. It causes brutal but usually nonlethal auditory harm to living targets and, after prolonged effort relative to combat constructs, can damage clockwork sonic receivers, cutting off reception of new Cogsong orders. Exact sonic magnitude, duration, hearing statuses, protection, repair and interaction with existing fallback orders remain **UNAPPROVED**.

Affected owners: `07_Centaurs_and_Smithcraft.md`, `22_Combat_Endurance_and_Shimmer_Guard.md`, `12_Languages_and_Linguistic_Customs.md`; design draft `24_Modular_Equipment_Design_Options_DRAFT.md`. Prior canon of mandatory Loom, homogeneous squads, standing orders, gear keys, Leywells and Cogmind Calamity remains unchanged.

## November 6, 2026 — Three-turn Windling targeted sonic pursuit (LATEST)

**CANON APPROVED:** A Windling swarm's primary offensive action is **targeted sonic distraction** using its Cogsong-compatible music boxes. **One commander attack action** instructs the assigned swarm to follow and harass **one specified target for up to three turns**, after which the offensive instruction expires. This is **one sustained attack command**, not three separate attack actions; new targets and fresh sonic assaults still require new command actions. The pursuit's three-turn duration is not prolonged by temporary obstruction or escape. Windlings must be very close to impose their sonic threat: separation of **approximately five meters from an ordinary swarm generally ends new exposure**. The target may escape, use effective sound barriers, physically cover/protect ears or strike the close-range Windlings; melee fighters have practical counterattacks. Stat-relative pressure, bounded size multipliers and the ability of high-SPD or well-defended creatures to ignore ineffectual threats remain canon. Existing injuries may persist after exposure ends.

**Cogsong and receiver boundaries:** Windling weapon frequencies are engineered not to jam their own Cogsong command channels. Sonic assault is an active offensive order, not free recurring damage during screen/carry tasks. Effective sustained exposure may eventually damage another construct's receiver, preventing new commands without automatically destroying chassis or Leywell. Exact acoustic effects, sonic magnitude, countermeasure bonuses, receiver failure thresholds, and interleaving multi-turn orders remain **UNAPPROVED**. This limited sustained-attack exception refines, rather than cancels, the standard rule that every new attack needs a command.

Owning files: `07_Centaurs_and_Smithcraft.md`, `22_Combat_Endurance_and_Shimmer_Guard.md`, `12_Languages_and_Linguistic_Customs.md`; status `10_Canon_Changelog.md`, index `00_Mystaria_Canon_Index.md`; draft calculations `24_Modular_Equipment_Design_Options_DRAFT.md`.

## November 6, 2026 — Weapon shapes, relative damage roles, dual wield and general hordes (LATEST)

**APPROVED directions from author:** Weapon form classes Light/Medium/Heavy and primary damage form with explicit alternative forms; separate Reach and Coverage; piercing Injury **1/5** and Armor Bypass **5/5**, slashing Injury **5/5** and Armor Bypass **1/5** with maximum coverage, blunt Injury **3/5** and Armor Bypass **3/5**. These are relative rankings, **not approved damage multipliers or bypass percentages**. Blunt reduces effective injury outcomes rather than being capped at one injury state, preserving devastating giant hammer strikes. Avoid counting both reduced Power and a separate injury cap.

**DUAL WIELD:** Secondary weapon assigned to **Attack** to challenge enemy evasion or **Defense** to aid wielder evasion; not two free full attacks. Sufficient STR allows one-handed and dual-heavy forms; the assistant's suggested **150% one-hand / 200% dual-heavy STR** thresholds are accepted as a working design for final testing, with DEX, geometry, balance and materials still to specify. Shields occupy a hand and contribute Defense; details postponed until armor, including block, coverage and movement effects.

**GROUPS:** The horde/mass combat framework must be generic for gangs, monster groups and armies, rather than Cogmarshal-only. Damage against covered multiple targets must assess attack coverage and sufficient Power; sweeping swords and suitably controlled rapid dagger attacks may fell several in one action, but cannot multiply actions or ignore Hero/Legend Guard. Explicit **development docket: revise horde enemies into coherent group/squad statistical units**, with remaining mathematical detail unresolved. Keep group pressure stat-gated.

**PROPOSALS ONLY:** class factors 1.00/1.15/1.30; piercing/slashing/blunt factors .90/1.10/1.00; armor bypass 40/0/20 percent, individual reach/coverage, exact dual-wield evasion effects and shield block; no automatic adoption. The latest +10 racial base rebase continues to supersede the old additive combat-only offset.

Owning subjects: `09_Equipment_and_Economy.md`, `22_Combat_Endurance_and_Shimmer_Guard.md`; design alternatives: `24_Modular_Equipment_Design_Options_DRAFT.md`; `07_Centaurs_and_Smithcraft.md` cross-reference and `00_Mystaria_Canon_Index.md`.

## November 6, 2026 — Reach classes, inside fighting, shield roles and Light baseline (LATEST)

**APPROVED:** Distinguish physical **Light/Medium/Heavy weapon handling class** from **Short/Medium/Long Reach** and attack Coverage. Short weapons work at grapple distance/where movement is possible. Medium weapons offer a general compromise. Long weapons, while effectively controlling distance, can **prevent ordinary Short weapon attacks until opponents close**, while making attacks by Medium users **harder** rather than strictly impossible. The long-wielder **loses reach-control advantage when meaningfully Pressured**, not simply when any harmless foe takes an action. Once a Short wielder successfully closes and **grapples inside** a Long weapon's usable reach, normal long-reach strikes against that opponent become **impossible** unless a qualifying grip technique or restored distance permits them; escape/other legal actions still possible. Exact reach distances, movement costs, evasion shifts, DEX/SPD implementation and exceptions are UNRESOLVED.

**PROFICIENCY DOCKET:** Add **Choking Up** as a suggested specialized technique that lets a fighter shorten grip on a long weapon to operate closer. **General mundane Proficiencies and this skill remain PROPOSED, not canon**; no cost/level gate approved.

**SHIELDS APPROVED DESIGN:** A handheld shield occupies one hand and may offer (1) **passive location-specific protection**, (2) **active directional blocking/parrying**, (3) **contextual evasive deflection**. Numerical adjustments, shield bash, equipment attachment, coverage and stacking deferred until armor. This complements, not replaces, dual-wield offhand Attack/Defense assignment. Do not give free full-body shield armor.

**WEAPON REFERENCE CHANGE:** The author called fixed **Dagger = 1.00×** merely a placeholder and accepts **Light weapon = 1.00× baseline attack-rating reference** instead. This supersedes the prior dagger-specific baseline lock. The individual dagger profile is open. Preserve established Gauntlets 1.00× and Unarmed 0.85× unless separately changed. Medium 1.15× and Heavy 1.30×, proposed form and armor-bypass coefficients, exact Reach/Coverage and attribute scaling remain proposals. **Armor Rating bypass is specifically postponed until armor design** rather than finalizing 40/0/20% now.

**COVERAGE LABEL PROPOSAL (not canon):** Proposed intuitive attack geometries **Point, Narrow, Sweep, Wide Sweep, Line**; replaces proposed Extended category because 'Extended' describes reach rather than area. Subject files `09_Equipment_and_Economy.md`, `22_Combat_Endurance_and_Shimmer_Guard.md`, `07_Centaurs_and_Smithcraft.md`; proposals `24_Modular_Equipment_Design_Options_DRAFT.md`. Preserve universal horde/army group-combat design task.


## November 6, 2026 — Coverage names, opportunity-based reach entry and STR/DEX melee scaling (LATEST)

**APPROVED:** Intuitive attack Coverage names **Point / Narrow / Sweep / Wide Sweep / Line** are now controlling terminology, separate from the already approved weapon Reach **Short/Medium/Long** and handling **Light/Medium/Heavy**. The earlier five labels 'Focused / Compact / Sweeping / Wide / Extended' are retired proposals. **Line does not automatically imply extra reach or penetration.** Preserve the illustrative dagger-versus-spear open approach, inside reach, and grapple comparison as a reusable teaching/design reference; it does not supply movement measurements.

**APPROVED:** Closing past a controlled Long weapon is decided by **tactical opportunity and execution, not a movement distance in feet/meters**. Blindly dashing forward while willing to be stabbed is not a guaranteed entry. A sufficiently fast, ready long-weapon defender can prevent the entry if their relative SPD and other circumstances warrant it. Accurate, player-stated **DEX predictions** by the defender may help under already-approved DEX >=75% of opponent SPD rules, with the >=200% contingency exception for wrong predictions, but do not automatically add prediction bonuses from mere numerical DEX. **Defender SPD >=1.5x attacker SPD is author-favored as a possible reach-control benchmark, NOT YET approved as an exact cutoff**; alternatives and corner cases remain for review. Existing Pressure can defeat Long-reach control; an established close grapple shuts out the Long weapon's ordinary strike.

**APPROVED WEAPON POWER MODEL:** `Power = (A * F)^2`; `A` is effective STR, effective DEX, max(STR,DEX) for Either, or **0.65(STR+DEX) for Both** when the weapon's minimum STR and DEX requirements are actually met. `F` is a single correctly calibrated weapon attack-rating multiplier with no double-counted component factors. The new racial base +10 is already part of effective stats, **no second historical combat-only +10**. This adopts the both-stat 0.65 starting coefficient; individual weapon factors, stat minimums and non-melee scaling remain unresolved. **Light weapon 1.00** remains the class reference, with dagger fixed 1.00 retired as placeholder. Existing gauntlet/unarmed reference multipliers remain unless separately changed. Armor-rating bypass % remains specifically deferred until the armor pass.

Subject owners: `09_Equipment_and_Economy.md` and `22_Combat_Endurance_and_Shimmer_Guard.md`; cross-reference `00_Mystaria_Canon_Index.md`; proposed detailed SPD cutoff, attack coverage counts and form coefficients in `24_Modular_Equipment_Design_Options_DRAFT.md`.

## November 6, 2026 — Graduated reach defense approved; transition to ranged shapes (LATEST)

**CANON CONFIRMED:** The author explicitly approved recommended **Model C** for defending Long-weapon reach against direct Short-weapon approaches: defender effective SPD / attacker effective SPD **below 1.25** = no special speed-based reach-control threshold; **1.25 to below 1.5** = approach substantially harder; **1.5 or greater** = a ready, properly controlling Long wielder may deny a straightforward unsupported rush. This is conditional on opportunity, actual defense, no sufficient Pressure and normal tactical counterplay. Willingness to take a hit does not force entry. Already-established successful DEX prediction can help; no automatic bonus for merely high DEX. No feet/meters required. Earlier Nov 6 entries marking Model C and 1.5 cutoff unapproved are **SUPERSEDED** in this narrow respect. Do not grant extra attack actions or automatic immunity to grapple.

**STATUS:** User approved previous suggestions on exact coverage names (Point/Narrow/Sweep/Wide Sweep/Line), STR/DEX/either/both `Power=(A*F)^2` with 0.65 both-stat coefficient, Light 1.00 reference, and earlier melee-shape foundations. Melee *design architecture* is sufficient to proceed to ranged shape review, but final individual F, STR/DEX requirements, reach/coverage target numbers, armor-specific bypass, shield statistics, material/quality and generic horde calculations remain unresolved. Do not silently approve numerical multipliers not explicitly selected.

**RANGED DRAFT DIRECTION (NOT CANON):** Explore bows, crossbows, firearms, thrown/manual weapons and mounted artillery, each with appropriate propulsion-based Power; respect already-approved firearms using construction/propellant/ammunition rather than shooter STR. Owner `09_Equipment_and_Economy.md`; cross-references `22_Combat_Endurance_and_Shimmer_Guard.md`, `00_Mystaria_Canon_Index.md`, design draft `24_Modular_Equipment_Design_Options_DRAFT.md`.

## November 6, 2026 — Battle saddles, ranged families and bow draw cap (LATEST)

**APPROVED by author:** Ranged-weapon taxonomy **bows, crossbows, firearms, thrown/manual launch, mounted/siege launchers**, with power sources specific to actual propulsion. Accept comparative **Close/Effective/Far/Extreme** range bands relative to weapon design, distinct from attack area/coverage and handling weight. **Bow Model A**: usable STR draw force up to the bow's **construction-defined maximum**; DEX precision for placement, not free uncapped damage. Crossbows draw from mechanically stored energy, loading/control via user or aids; firearms and artillery have **intrinsic gun/engine/propellant/ammunition Power**, while STR bears recoil/weight and DEX aims; thrown weapons may use wielder STR/DEX with defined shapes. Actual factors, draw force conversion, accuracy, range distances and reload mechanics remain unresolved.

**APPROVED battle saddles:** mounted **firearms and suitable mechanical crossbows** on Centaurs, quadrupedal Crownform/Firstshaped Drakyn and other applicable Firstshaped bodies. Centaurs can side-mount a machine gun or pull a cannon cart, subject to safe deployment, bracing and recoil. Crownform Drakyn keep their canon manipulating forelegs yet cannot rely on a normal upright two-leg shooting stance in true form. Saddles adapt aiming, positioning and firing controls; they **do not** directly enhance Power, erase recoil or grant extra attack actions. Not all ranged families are saddle compatible; specifically bows and manual throws need special construction if attempted.

**APPROVED ranged character philosophy:** STR users favor heavily reinforced/high-recoil/Adamantite-compatible firearms, while DEX users generally favor lighter-than-firearm ranged weapons or purpose-built light firearms such as Trufula designs; **Trufula's extreme fire vulnerability and approved propellant restrictions remain operative**. The design goal is a build tendency, not a class prohibition or an automatic DEX bullet-Power bonus.

**UNRESOLVED:** battle saddle costs, fit/capacity/racial variants, firing arc, reload procedure, bracing/recoil transfer, moving-fire tradeoffs, bow Power and draw maxima, range thresholds, accuracy and ammo profiles, universal horde casualties, material specifics. Affected: `09_Equipment_and_Economy.md`, `22_Combat_Endurance_and_Shimmer_Guard.md`, `06_Drakyn.md`, `07_Centaurs_and_Smithcraft.md`, `00_Mystaria_Canon_Index.md`; proposals `24_Modular_Equipment_Design_Options_DRAFT.md`.

## November 6, 2026 — Three PP pressure; Trapped independent; reload, aim and mounts (LATEST)

**APPROVED PRESSURE RULE:** Count **net meaningful Pressure Points (PP)**. **0 = Open**, **1–2 = Pressured with exactly the same evasion consequence**, **3+ = Extreme Pressure with no greater evasion penalty at higher totals**. Most independent effective circumstances contribute **1 PP**: credible flank, applicable reach advantage, reliable actual DEX prediction (wrong prediction can favor the *opponent*), small qualifying archer suppression, and an offhand Attack when it poses a genuine separate threat. Credible offhand Defense and other counters may remove/offset applicable PP; PP cannot go below zero. A qualifying four-Windling group may contribute 1, but accumulating enough saturation for Extreme Pressure through raw swarm scale should require **exponentially greater effective numbers/power**, not simple linear +1 per four Windlings. No automatic PP for a harmless attacker or mere simultaneous orders. Exact stacking/de-duplication/coordination and stat-relative swarm threshold remain unresolved.

**APPROVED TRAPPED SEPARATION:** **Trapped is separate**, not produced merely by three PP. Aware Trapped character **cannot ordinarily dodge** the applicable threat, but **can use other legal defenses** such as blocking, armor, wards or a viable reaction. Trapped is not automatically incapacitated or helpless; Extreme Pressure by itself does not eliminate ordinary evasion. This latest ruling supersedes the older ladder ordering that placed Trapped between Pressured and Extreme Pressure. Existing six evasion difficulty categories remain, with exact PP-induced difficulty modifier still open.

**APPROVED RELOAD:** Bows have negligible additional nocking/drawing opening; light crossbows create a modest vulnerability and heavier mechanical/other loading can be substantial. Careful loading of a **single-shot pistol** or a **high-capacity magazine** costs **one full-turn meaningful action**, during which attack openings are present. Siege reload exposes its operators, typically at least a full loading action, with engine-specific longer cycles still unresolved. Reload vulnerability is a contextual opening, not extra free turns for adjacent enemies.

**APPROVED AIMING:** One meaningful action can be spent **aiming** rather than firing, sacrificing one of two potential attacks for a better prospective hit. No automatic shot Power gain, armor bypass, guaranteed hit or new action; exact accuracy tier, retention/interrupt rules and pressure integration remain to define.

**APPROVED MOUNT ROLES:** Fixed side, articulated, heavy-support, assisted-loading mounts remain distinct, with combined rigs permitted when engineered. No free extra attacks or automatic recoil cancellation.

**FUTURE NONCANON PROFICIENCY OPTIONS:** Draft a time-reducing reload specialization and a vulnerability-reducing one; neither is an established purchased Skill/Proficiency or has approved SP costs. Preserve racial battle saddles, construct and general monster horde group design, existing firearm intrinsic-power rules. Owners: `22_Combat_Endurance_and_Shimmer_Guard.md`, `09_Equipment_and_Economy.md`; cross-ref `07_Centaurs_and_Smithcraft.md`; draft `24_Modular_Equipment_Design_Options_DRAFT.md`.
