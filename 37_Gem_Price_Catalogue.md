# Mystaria — Current Gem Price Catalogue and Encounter Reward Calibration

**Status: AUTHOR APPROVED, November 20, 2026.** This is the latest operative divine-Gem economic and catalogue repricing, ratified after approval of the escalating **7-to-997 Gems per equal-level Henchman** model and the author’s direction to reprice **all previously priced items, including Junk**. It supersedes contradictory older *Gem numbers*, not mechanical statistics, item identities, properties, racial suitability, shop stock/availability restrictions, Smithcraft requirements, MP, SP, Soul Strain, XP, cooldowns or patron qualification rules. Historical ledgers, archived proposals and retired Moonlit Forge prices are not current shop offers. `09_Equipment_and_Economy.md` retains the full economic doctrines; `01_World_and_Shimmer.md` governs XP and patron rewards.

## 1. Universal Gem reward schedule

For qualifying ordinary encounters at **Hero level L** (1–100):

```text
Equal-level Henchman base reward B(L) = 10L − 3 Gems.
Ordinary encounter reward = B(L) × (enemy/quest equivalent level ÷ Hero level) × threat modifier.
Modifiers: Horde ×0.1, Minion ×0.4, Henchman ×1, Elite ×2.
```

Equivalently `B(L) × (unrounded encounter XP equivalent / (2L))`, retaining the actual encounter's qualifying level and threat. Ordinary **XP itself** still uses `2 × encounter level × threat modifier` with its separately approved whole-XP rounding; do not compute Gem equivalence using the already-rounded XP when it distorts the ratio. GM-assessed patron-qualified quests, investigations, rescues and combat bypasses use the same **rough encounter equivalence**, before play or retroactively, with no mandatory combat/quest percentage division and no automatic double payment for resolving one challenge.

| Current Hero level | Base Gems / equal-level Henchman | XP to next level | Equal-level Henchmen from zero XP (whole enemies) |
|---:|---:|---:|---:|
| 1 | 7 | 2 | 1 |
| 10 | 97 | 110 | 6 |
| 25 | 247 | 650 | 13 |
| 50 | 497 | 2,550 | 26 |
| 75 | 747 | 5,700 | 38 |
| 100 | 997 | 10,100 | 51 |

**Currency settlement:** 100 Glints = 1 Gem; only whole Gems/Glints exist. Carry fractional-Glint *accounting* remainders forward to later qualifying awards (or bundle rewards at a quest/session milestone) rather than minting fractional coins, rounding every monster independently or giving unconditional kill drops. The encounter table is a divine **reward guideline**, contingent on patron qualification; actual mundane loot and commercial wages are separate.

**Boss exception unchanged in Gem terms:** A qualifying Boss gives exactly **one level of XP** from current progress under the November 20 ruling. Its distinct, previously approved **two-level Gem-budget** award continues as `E(L+2) − E(L)`, defined only if `L+2 ≤ 100`. The mismatch is explicit and remains subject to separate author review; it is NOT a simple ×2 Henchman Gem multiplier.

## 2. Gross rewards and owned-equipment wealth

The level progression budget counts the exact Henchman-equivalent number `(L+1)/2` for each level interval, **not** the rounded-up whole-monster count shown above:

```text
E(1) = 0 gross earned Gems since the level-1 starting point.
G(L) = (10L − 3) × (L+1) / 2 Gems gross budget for level L → L+1.
E(L) = sum for k=1...(L−1) of G(k).
At equipment milestones, R(L) = 0.5 × sum of prior sold reference
  complete portfolios among levels 10, 25, 50 and 75.
W(L) = 30 + 0.70 × E(L) − R(L).
```

The **30-Gem starting equipment portfolio is an in-kind planning baseline, not part of Gross Gems earned.** The gross budget retains **30% intended consumable use**, plus the previously approved expected **50% resale loss** when a *shop-sold and eligible* prior reference outfit is replaced at the next milestone. No guarantee of buyback for self-made, quest-found or other provenance-ineligible items. Starting granted Junk weapon/armor remain **in-kind gear, not cash**, and the 30-Gem level-1 portfolio remains a planning reference rather than a hard limit on included starter items.

| Hero level | Reference Quality | Gross lifetime earned E(L), approx. Gems | Cumulative replacement loss R(L), approx. | Owned-equipment target W(L), approx. Gems |
|---:|---|---:|---:|---:|
| 1 | Starter | 0 | 0 | 30 |
| 10 | I | 1,569 | 0 | 1,128 |
| 25 | II | 25,514 | 564.15 | 17,326 |
| 50 | III | 206,339 | 9,227 | 135,240 |
| 75 | IV | 698,726.5 | 76,847.14 | 412,291 |
| 100 | V | 1,658,926.5 | 282,992.84 | 878,286 |

Unrounded reference owned-wealth knots are `W1=30`, `W10=1128.3`, `W25=17325.65`, `W50=135240.325`, `W75=412291.4125`, `W100=878285.70625`; use these for calculations and rounded whole Gems for display. Reference level-100 consumables `≈497,677.95 Gems`. **At intermediate levels** budget the upcoming qualifying portfolio replacement loss *smoothly* across its preceding tier interval, rather than creating a false Gem windfall at the exact replacement level:

```text
For interval [a,b] in {[10,25], [25,50], [50,75], [75,100]}:
R_smooth(L) = R(a) + 0.5 × W(a) × (L−a)/(b−a).
R_smooth(L) = 0 for 1 ≤ L ≤ 10.
W_smooth(L) = 30 + 0.70 × E(L) − R_smooth(L).
```

These are **reference equipment-purchasing budgets**, not level-based purchases or automatic wallet grants. Actual wealth depends on rewards, purchases, resale eligibility, special finds, and campaign conditions. The cumulative wealth formula is deliberately **not** simple linear interpolation between tier milestones.

## 3. Finished ordinary physical equipment: current standard Gem rates

Standard finished matching-design divine prices are **material-neutral**; form/class, coverage, Quality and actually paid extras govern value. Mundane scarcity, smith access, item durability, flaws, divine Celestite forging and legal equipment requirements remain independent. A physical item does not get more AR, attack Power, better Quality or an enchantment merely because its price was raised.

| Ordinary item / Quality | I | II | III | IV | V |
|---|---:|---:|---:|---:|---:|
| Light one-handed weapon; Full Light armor | 80 | 240 | 4,000 | 32,000 | 100,000 |
| Medium one-handed weapon; Full Medium armor | 100 | 300 | 5,000 | 40,000 | 125,000 |
| Ordinary Medium-designed two-handed / Heavy-designed two-handed weapon; Full Heavy armor | 200 | 600 | 10,000 | 80,000 | 250,000 |
| Light shield | 50 | 150 | 2,500 | 20,000 | 62,500 |
| Medium shield; Heavy shield | 100 | 300 | 5,000 | 40,000 | 125,000 |

A true Medium *two-handed manufactured* form costs twice a corresponding Medium one-handed form. The matching **Medium/Heavy shield equals the Medium one-handed weapon**, while **Light shield is exactly half Medium shield** (not 150%); no shield tier receives unapproved combat benefits. Quality V ordinary Heavy two-handed and Full Heavy armor = **250,000 Gems**; ordinary Light weapon is still 80% of Medium one-handed. **Full/Standard/Partial armor price** remains **100%/75%/50% of the matching Full armor**, while actual physical protection/coverage and approved mobility burdens are unaltered.

| Armor coverage and class | I | II | III | IV | V |
|---|---:|---:|---:|---:|---:|
| Light Standard (75%) | 60 | 180 | 3,000 | 24,000 | 75,000 |
| Light Partial (50%) | 40 | 120 | 2,000 | 16,000 | 50,000 |
| Medium Standard (75%) | 75 | 225 | 3,750 | 30,000 | 93,750 |
| Medium Partial (50%) | 50 | 150 | 2,500 | 20,000 | 62,500 |
| Heavy Standard (75%) | 150 | 450 | 7,500 | 60,000 | 187,500 |
| Heavy Partial (50%) | 100 | 300 | 5,000 | 40,000 | 125,000 |

**Special engineering** (including exceptional-capacity bows and other intrinsically extraordinary apparatus) can require a Quality-independent construction floor. Never charge just `QV/16` for a Quality I STR400-capacity Greatbow if its engineering capability is unchanged. Costs for actually unapproved standalone quivers, bolts, cartridges, advanced sights, individual modifications, clockwork chassis, custom enchantment recipes and unresolved mechanical features remain **UNPRICED**, not secretly assigned a number by this standard table.

## 4. Junk: complete matching-Quality-I recalculation

**Junk = Quality I, Boughsteel-based, HALF the matching ordinary QI divine Gem value**, not Quality zero, not a discount for exotic designs, and not extra free durability. Existing specific Junk weapon accuracy effects, worn-armor evasion penalties, accessory stat pooling, shortened shield condition track and Junk-shield **0.90 × final Defense Power** remain unchanged. Start-of-campaign grant of **one eligible Junk weapon and one eligible Junk armor ensemble** remains an in-kind grant, even where total appraisal exceeds level-1 target W1=30. Light/Medium starter availability and Heavy beginner restrictions remain.

| Matching QI ordinary form | Ordinary QI | Junk QI |
|---|---:|---:|
| Light weapon / Full Light armor | 80 | **40** |
| Medium one-handed weapon / Full Medium armor | 100 | **50** |
| Medium/Heavy two-handed weapon / Full Heavy armor | 200 | **100** |
| Light shield | 50 | **25** |
| Medium or Heavy shield | 100 | **50** |
| Light Standard / Partial armor | 60 / 40 | **30 / 20** |
| Medium Standard / Partial armor | 75 / 50 | **37 Gems 50 Glints / 25** |
| Heavy Standard / Partial armor | 150 / 100 | **75 / 50** |

For an eligible *Junk accessory* use **half the matching QI accessory category price** from the reference band below: Head/Neck/Arms/Hands/Waist **25 Gems** each; Feet/Ring B **30 Gems** each; Ring A **35 Gems**. A Junk-starter *illustrative* Light weapon + Full Light outfit now appraises to **40 + 40 = 80 Gems** but does **not** award a new 80-Gem starting wallet or unlock other items.

## 5. Eleven-slot reference allocation bands (budget examples, not vendor offers)

The highest-priority item is an **actual finished item**, not a surcharge applied because someone calls it a "primary". These reference *allocations* preserve the author's eleven-slot philosophy; a genuinely purchased Heavy Full suit, medium weapon or shield still costs its **actual** class/coverage price above, not a cheaper row from this allocation table. Unapproved specific magical/rune effects are not silently included.

| Reference slot / Quality | I | II | III | IV | V |
|---|---:|---:|---:|---:|---:|
| Primary investment | 200 | 600 | 10,000 | 80,000 | 250,000 |
| Secondary armor allocation | 140 | 400 | 7,000 | 54,000 | 170,000 |
| Tertiary/offhand allocation | 70 | 200 | 3,500 | 27,000 | 85,000 |
| Head | 50 | 150 | 2,500 | 20,000 | 62,500 |
| Neck | 50 | 150 | 2,500 | 20,000 | 62,500 |
| Arms | 50 | 150 | 2,500 | 20,000 | 62,500 |
| Hands | 50 | 150 | 2,500 | 20,000 | 62,500 |
| Feet | 60 | 175 | 3,000 | 23,500 | 73,000 |
| Waist | 50 | 150 | 2,500 | 20,000 | 62,500 |
| Ring A | 70 | 200 | 3,500 | 27,000 | 85,000 |
| Ring B | 60 | 175 | 3,000 | 23,500 | 73,000 |

**Upper-tier purchase test (actual ordinary reference Heavy price):**

| Hero reference level | Wealth W(L), rounded | One Quality above | Ordinary Heavy finished price | Share of wealth |
|---:|---:|---|---:|---:|
| 10 | 1,128 | II | 600 | 53.2% |
| 25 | 17,326 | III | 10,000 | 57.7% |
| 50 | 135,240 | IV | 80,000 | 59.2% |
| 75 | 412,291 | V | 250,000 | 60.6% |

Above-tier purchases use real equipment rules, **not** additional level locks. Two Quality tiers above normally costs much more than the entire reference portfolio. For a level-100 six-V/five-III **illustrative** mix using lawful occupied slots, QV Full Heavy armor 250,000 + QV substantially enchanted Medium weapon 250,000 (ordinary 125,000 + actual magical package ≈125,000) + QV Medium shield 125,000 + QV neck 62,500 + QV waist 62,500 + QV ring A reference 85,000 + QIII head/arms/hands 2,500 each + QIII feet/ring B 3,000 each = **848,500 Gems**, leaving **29,786 of W100 ≈878,286**. Ring/neck numbers are budget envelopes, **not** independently approved item effects, rune installations or prices for particular named enchantments. Enchanted finished items typically cost **about twice the corresponding mundane finished form** for substantial installed magic, preserving all actual enchantment eligibility, slot limits and Soul Strain.

## 6. Tiered mana restoration (approved potion mechanics; new prices)

| Tier | MP restored per eligible single drink | Single-use, Gems | One-dose-per-day refillable, Gems |
|---|---:|---:|---:|
| I | 5 | **20** | **200** |
| II | 10 | **60** | **600** |
| III | 20 | **1,000** | **10,000** |
| IV | 40 | **8,000** | **80,000** |
| V | 80 | **25,000** | **250,000** |

An additional daily refillable dose adds **50% of the single-dose refillable price** at that same tier, preserving `base × [1 + 0.5 × (N−1)]`. These are divine Gem tariffs, not actual manufacturing availability or universal shop stock. Restoration, **Toxicity**, action use, MP caps and Warlock exceptions remain exactly the previously approved mechanics. **Older unquantified Mana Dew is NOT a live equivalent** to one of these drinks.

## 7. Ranged ammunition and engineered Quality-V bow references

- **Ordinary 40-arrow mixed Piercing/Slashing resupply:** **30 Gems per 40**, no included quiver; universal Shimmer ammunition slot capacity (30) and ordinary 20-arrow quiver capacity unchanged; material, head choice, recovery and shot accounting unchanged.
- **Willow Shortbow + 12 ordinary arrows:** **120 Gems** as the exact named Moonlit Garden starter package. The historical 20-Gem price is superseded.
- **Hand Crossbow + 12 bolts:** **160 Gems** as the exact named Moonlit Garden starter package. This does **not** establish a universal separately sold bolt bundle price.

| Advanced engineered bow, finished Quality V (without additional enchantments) | Gem reference price |
|---|---:|
| High-draw | **125,000** |
| Titan | **175,000** |
| Colossal composite | **250,000** |
| Legendary greatbow, full STR400-cap engineering | **300,000** |

The Greatbow costs **20% above the comparable ordinary QV Heavy two-handed weapon** of 250,000. Full approved draw caps (100/200/300/400), Power, handling minima, ammunition and one-arrow tempo are untouched. These are **pricing references for the established named Quality V designs**, not universal retailer stock or a license to grant QV enchanted features for free. **Quality I–IV intrinsically engineered bow floors remain unresolved** until item-specific manufacturing costs are set; the earlier 150/450/950/1750 and 320/480/640/800 QV lists are historical or provisional, not active recommendations.

## 8. Portable Cogsong Command Loom (mandatory Cogmarshal controller)

| Rank / Quality | I | II | III | IV | V |
|---|---:|---:|---:|---:|---:|
| Finished portable Loom Gem price | **120** | **360** | **6,000** | **48,000** | **150,000** |

Existing mandatory Loom functionality, Cogmarshal rank prerequisites, Cogsong control, physical operation, capacities and costs remain. No price-based access gate beyond the actual item and established skills; ordinary clockwork construct chassis still await separate actual component prices.

## 9. Moonlit Garden: current named early stock

These exact named stock items retain their existing **described function**, not fabricated bonus Quality, extra magic, upgraded statistics or discounted universal materials. Listed weapon/armor prices are adjusted by actual relative finished form; some simple nonstandard starter objects are individually priced rather than assumed equivalent to fully engineered Heavy equipment. Non-Junk items do **not** acquire Junk penalties from a cheap named-shop price.

| Early weapon | New Gems | Existing description preserved |
|---|---:|---|
| Traveler's Cudgel | **80** | Light club |
| Little Thorn Dagger | **80** | Compact knife |
| Wanderer's Sling | **80** | Simple stone sling |
| Knotted Walking Staff | **100** | Walking/defensive staff |
| Hearthguard Spear | **200** | Spear |
| Gardener's Handaxe | **80** | Light axe |
| Traveler's Shortsword | **100** | Shortsword |
| Willow Shortbow (12 arrows) | **120** | Named bow bundle |
| Hand Crossbow (12 bolts) | **160** | Named crossbow bundle |
| Guardian's Longsword | **100** | Longsword |
| Pilgrim's Warhammer | **200** | Warhammer |
| Mercybrand | **160** | Dagger with its previously described magical blunt option |

| Early armor/protection | New Gems | Existing description preserved |
|---|---:|---|
| Padded Tunic | **80** | Basic wearable protection |
| Traveler's Cloak | **40** | Weather cloak with pocket |
| Softstep Boots | **40** | Footwear with traction |
| Leather Bracers | **40** | Forearm protection |
| Leather Vest | **80** | Light protective vest |
| Willow Buckler | **50** | Small shield |
| Hearthguard Helm | **50** | Helm |
| Wayfarer's Chain Shirt | **100** | Medium armor |
| Guardian's Shield | **100** | Full-size shield |
| Briarplate Harness | **120** | Resizing Light armor |
| Moonweave Robe | **160** | Robe with described minor magic resistance |

**Named utility goods:** The previous starter (10/20/30)-Gem utility groups reprice by **×3** to **30/60/90 Gems**, respectively, preserving their exact existing function and item counts:

| 30 Gems | 60 Gems | 90 Gems |
|---|---|---|
| Everdry Matches | Whisperleaf Token ×2 | Homeward Compass |
| Little Compass | Gentle Translator | Friendship Ribbon |
| Traveler's Journal | Starlit Lantern | Waymark Chalk ×3 |
| Dewdrop Canteen | Starspawn Treat Pouch | Pocket Campsite |
| Mosslight Pebble | | |
| Pocket Repair Kit | | |

**Legacy early consumable names: price-calibration entries only, NOT live shop offers until the previously flagged healing, Toxicity or spell effects are validated.** This preserves the full list of older items without accidentally canonizing unfinished healing or Mana Dew effects:

| Historical stock name | Revalued illustrative Gems | Current sale status |
|---|---:|---|
| Honeyberry Ration ×3; Softleaf Bandage ×3; Warmth Drop ×2; Kindling Seed ×3; Antitoxin Sweet | 30 each bundle | Legacy effects require source-specific validation |
| Little Healing Vial; Mana Dew; Featherfall Candy; Cleansing Soap ×3 | 60 each bundle/item | NOT LIVE; Mana Dew is not the tiered mana potion |
| Moonlight Remedy; Calming Blossom ×2; Sanctuary Seed | 90 each bundle/item | NOT LIVE; healing/protection pricing still needs mechanics review |

The **Moonlit Forge independent +1…+5 reinforcement track is RETIRED**; archival rows and their former prices remain historical, not live Gem Shop goods. Pre-modular modification products (Blunted Mercy, Sure Grip, etc., and Comfortable Fit, Guardian Stitch, etc.) remain **mechanically unapproved as standalone current modular goods**. Their historical list-price groups can be provisionally revalued at 30 / 60 / 90 / 150 Gems corresponding to former 10 / 20 / 30 / 50, but **may not be sold as independent modular upgrades without separately approved compatible recipes/effects**.

## 10. Shimmer convenience and inventory upgrades (current Gem prices)

| Upgrade | Gems |
|---|---:|
| Item Sorting I | **5** |
| Item Appraisal I | **10** |
| Quest Reminder I | **30** |
| Pocket Inventory I (+4 slots) | **60** |
| Quick Equip I | **60** |
| Party Display I | **60** |
| Dialogue Notes I | **60** |
| Cartographer's Eye | **90** |
| Trailkeeper | **90** |
| Route Planner | **150** |
| Pocket Inventory II (+8 slots) | **180** |
| Shared Cartography | **240** |
| Traveling Armory | **240** |
| Party Link | **270** |
| Traveler's Inventory (+12 slots) | **300** |
| Shrinebound Company | **360** |
| Guardian's Embrace | **480** |
| Evergreen Satchel (+20 slots and enlarged item capacity) | **540** |
| Hearthstone Recall | **750** |

All other approved free Shimmer functions remain **free** (first six slots, basic mapping, clock, compass, tooltips, journal, patron network shrine-to-shrine travel). Premium functions retain their specific current limits, prerequisites and restrictions; these price changes do not add mechanics.

## 11. Scope, preservation, and open issues

1. **PRICE-ONLY conversion:** The old nominal equipment ladders `60/120/240/480/960`, QV 960 Heavy physical anchor, previous W10/25/50/75/100 `200/400/800/1600/3200`, prior potion `6/12/24/48/96`, shield tariff `15/30/60/120/240` Light and `30/60/120/240/480` Medium/Heavy, Loom tariff `120/280/550/900/1400`, starter-store amounts, Shimmer convenience tariffs and old approved bow reference numbers are **SUPERSEDED in the currently priced economy** by this catalogue. Do not multiply player attributes or equipment effectiveness along with Gems.
2. **No invented prices for truly unspecified designs:** Unique enchantments, engineered variants lacking numeric construction costs, special cartridges and bolts, exceptional artifacts, Celestite divine access/forge labor, actual mundane money, repair labor, Nymbrin alchemy without published finished effects, and incomplete manufacturer recipes remain unresolved. They are **not** made free by an absent tariff.
3. **No retroactive free value or rewriting history:** Existing campaign records, receipts and old Gem wallet balances retain historical provenance. Converting a particular saved game to this edition requires deliberate **individual ledger reconciliation**; do not blindly multiply every prior balance or issue compensatory coins. Shop buyback remains eligible-shop-original-price ×50%, not an arbitrage opportunity from relabeling old items with new prices.
4. **Design review:** Representative physical/soul-strain equipment viability, enchanted item value, QI–QV exotic bow floors, endgame ammunition economics, and the **Boss one-level XP versus two-level Gems** mismatch remain suitable for future balance testing. The resulting `W100≈878,286` is a reference owned portfolio target, **not** a mandatory 878,286-Gem cash balance or one-million-Gem standalone item requirement.
