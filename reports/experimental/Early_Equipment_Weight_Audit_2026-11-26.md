# Early equipment accessibility — November 26, 2026 (PROPOSAL / deterministic research)

**Historical research snapshot; the author subsequently approved the baseline equipment values, Handling ladder and ordinary ranged conversion.** Current rules live in the owning equipment/melee/ranged/shield references; remaining material, grip and ammo quantity questions are still open. The following preserves the original proposal-stage audit. The level-one 2 stat / 2 SP / 2 TP grant is approved separately (commit e4e9229bd1d66f11f8a699766faacd7a483ba9ec). At the time of this audit, item values and conversions were candidates, not replacements for historical profiles. Prior approved independent eligibility direction, END Barbarian access, and provisional Hulking 150% Weight / Deflection 75% Weight are preserved.

## Baseline conventional melee candidates

Use shared equipped capacity floor(20 + effective STR + effective END), minimum zero. No unrelated generic attribute gate. Scaling, reach, lawful hands, geometry, special properties, attack modes and actual material/Quality construction remain separate. Heavy weapons can still require genuinely justified control; no universal STR gate, including Hulking. Candidate ordinary one/two-handed grips follow actual item, not class alone. Unresolved cases do not default to legal. Weight is an abstract equipment budget, not pounds.

| ID | Shape | Weight |
|---|---|---:|
| L-01 | Dagger | 2 |
| L-02 | Stiletto | 2 |
| L-03 | Short knife | 2 |
| L-04 | Cestus / knuckle weapon | 2 |
| L-05 | Hand axe | 4 |
| L-06 | Light pick | 3 |
| L-07 | Short club | 3 |
| L-08 | Sickle | 3 |
| M-01 | Arming sword | 6 |
| M-02 | Longsword | 8 |
| M-03 | Rapier | 6 |
| M-04 | Sabre | 6 |
| M-05 | Falchion | 7 |
| M-06 | Mace / flanged mace | 6 |
| M-07 | Warhammer | 7 |
| M-08 | War pick | 6 |
| M-09 | Battleaxe | 8 |
| M-10 | Short spear | 6 |
| M-11 | Quarterstaff | 6 |
| H-01 | Greatsword | 18 |
| H-02 | Zweihander | 22 |
| H-03 | Greataxe | 20 |
| H-04 | Maul | 24 |
| H-05 | Great hammer | 24 |
| H-06 | Poleaxe | 18 |
| H-07 | Halberd | 16 |
| H-08 | Glaive | 14 |
| H-09 | Pike | 16 |
| H-10 | Long spear | 12 |
| H-11 | Lance | 18 |
| H-12 | Heavy flail | 20 |
| separate named item | Traveler's Shortsword | 5 |

No new WR or damage profile for shortsword. Conventional Light/Medium/Heavy complete armor Weight 6/12/24; shields 4/8/16; implement 2–4; no component/coverage-specific Weight or material/Quality modifiers assigned yet. The 31 shape register stays unchanged until approval. Honed discount not assumed in this audit; provisional Hulking multiplier 1.5, Deflection 0.75. Preserve actual rounding/coverage rules; no new rounding declared. Proposed QI–V Honed/Deflection DEX 6/18/32/46/60, no Junk specialties. Only Deflection L25/L100 18/60 and 75% Weight are prior approved provisional standards; mapping to Quality and remaining handling are candidates.

## Ranged conversion candidate

Below subtract 10, minimum 1, from the November 6 approved *test* baseline thresholds, not older raw candidate rows. For bows these are candidate minimum controlled-draw gates, not full draw, new physical draw cap or Power. Crossbow support is candidate cocking burden for ordinary unassisted use, not necessarily the requirement to carry/fire a preloaded bow. Firearm recoil independently retained; no authorization for full-auto or shortfall exceptions. Physical constraints, aids, ammo and actual modes remain. Special engineered bows, special material guns, saddle gun and automatic-volley recoil require separate conversion; no automatic subtraction applied to them.

| Item | Candidate Weight | Support/draw STR | DEX | Single-shot recoil STR |
|---|---:|---:|---:|---:|
| Shortbow | 4 | 1 | 1 | — |
| Recurve bow | 5 | 3 | 1 | — |
| Longbow | 7 | 8 | 3 | — |
| Composite bow | 7 | 7 | 5 | — |
| Warbow | 12 | 15 | 5 | — |
| Mounted recurve | 6 | 6 | 6 | — |
| Hand crossbow | 4 | 1 | 1 | — |
| Hunting crossbow | 7 | 1 | 2 | — |
| Military crossbow | 8 | 6 | 5 | — |
| Arbalest | 14 | 13 | 7 | — |
| Repeating crossbow | 8 | 5 | 8 | — |
| Battle-saddle crossbow | mounted | rated mount | 10 | — |
| Single-shot pistol | 4 | 1 | 2 | 5 |
| Revolver | 5 | 1 | 4 | 8 |
| Automatic pistol | 5 | 2 | 7 | 10 |
| Musket | 8 | 5 | 5 | 13 |
| Carbine | 8 | 8 | 8 | 15 |
| Automatic carbine | 8 | 11 | 11 | 20 |
| Precision rifle | 12 | 16 | 15 | 25 |
| Scattergun | 8 | 9 | 7 | 20 |

Manual/thrown candidate Weight: throwing dagger 2, axe 4, javelin 5, dart 1, sling 2, bolas 2. Candidate ordinary sling STR/DEX 1/1; other release gates unresolved. Do not invent automatic restraint or shot Power. Mount transferred Weight and specific frame support uncalibrated.

## Deterministic level-one capacity checks

13 racial arrays from 02_Races.md; 21 allocations per race (0, 1 or 2 of the new stat points distributed among five attributes, without an added allocation cap). Apply racial multipliers to base increments and floor capacity once. No bonuses, no material discounts, no Grip/price/availability or actual combat simulation. For each race/item pair report unspent and at least one allocation passing; allocation counts include allocations to INT and Skill even where those don't change eligibility.

| Test | Race/item pairs | Unspent passes | At least one allocation passes | All allocation-state passes / checks |
|---|---:|---:|---:|---:|
| 31 conventional shapes alone | 403 | 401 | 403 | 8427/8463 |
| 31 with Light armor | 403 | 382 | 390 | 8070/8463 |
| 31 with Medium armor | 403 | 347 | 361 | 7389/8463 |
| 12 Heavy Hulking + Light armor | 156 | 79 | 96 | 1745/3276 |
| Shortsword + Light armor | 13 | 13 | 13 | 273/273 |
| Shortsword + Medium armor | 13 | 13 | 13 | 273/273 |
| Arming sword + Light shield + Medium armor | 13 | 13 | 13 | 273/273 |
| QI Honed dagger + Light armor (no discount) | 13 | 10 | 12 | 217/273 |
| QI Light Deflection + dagger | 13 | 10 | 12 | 217/273 |
| Shortbow + Light armor | 13 | 13 | 13 | 273/273 |
| Hand crossbow + Light armor | 13 | 13 | 13 | 273/273 |
| Single-shot pistol + Light armor | 13 | 8 | 9 | 169/273 |
| Revolver + Light armor | 13 | 4 | 7 | 102/273 |
| Musket + Light armor | 13 | 1 | 2 | 22/273 |

Total 31,395 deterministic checks (overlapping scenario groups, not unique builds). All 13 races fit ordinary starter shortsword + Light or Medium ensemble in every allocation state, even without spending points. No race forced to invest attributes merely to meet ordinary equipment Weight. Weight-only eligibility does not certify real body fit, lawful hands, mounted operation, ammunition, reload, Craft access, or purchase. Conventional Heavy weapon alone is accessible to most level-one races with this candidate Weight ladder; combined armor and Hulking cost matter. If too permissive, calibrate specific weights, not a universal STR gate. The candidate QI DEX 6 gates exclude Centaur at level one even with two allocated points; Thornguard and Kharak can reach them.

## Starter package boundary

Existing grant: one eligible Junk QI Boughsteel weapon and one Junk QI Boughsteel armor ensemble, ordinary Light, qualified Medium at GM discretion, not Heavy. No free shield or Gems. 30 Gems is reference equipment wealth, not a shopping purse; 50-Gem Junk implement price does not prove it is granted. Preserve availability, body fit and actual Craft rules. No finalized item prices changed. Ranged ammunition and implement access through grant need separate confirmation. Legal one-handed arming sword + shield capacity is a separate loadout check, not a free starter bundle. Heavy armor excluded from normal starting grant even if it fits. Full armor coverage, individual material and Quality Weight, exact Honed discount, Grip exceptions, special ranged conversions and actual item cards remain open.
