# Mystaria Melee Power Calibration — DESIGN DRAFT

**NOT CANON.** November 6, 2026. This is the second weapon-shape design stage, testing all 31 candidate profiles in `25_Melee_Weapon_Catalogue_DRAFT.md`. Their per-weapon F, stat requirements, individual forms and coverage assignments remain unapproved. The user has approved the **visible Coverage column**, not the entire numerical register.

## Confirmed mechanics

`Power = (A * F)^2`. `A = STR`, `DEX`, `max(STR,DEX)` for Either, or **`0.65 * (STR+DEX)`** for Both, which requires both minima. These are effective, already-rebased stats; do not add old combat-only +10. F is one calibrated modifier, not a base class coefficient multiplied by another type coefficient. Gauntlet 1.00, unarmed 0.85 and Light 1.00 reference remain.

## Important property of the approved Both formula

At equal total STR+DEX, **Both-stat Power is invariant to the split** so long as the candidate's two prerequisites are met. For STR/DEX 40/40, 60/20, and 20/60, `A=.65*80=52`. A proposed Longsword F 1.10 consequently gives `(52*1.10)^2=3271.84` across all three. **This is a sum-based scaling rule with two separate minimum-stat gates, not an explicit statistical bonus for even distribution.** Changing the approved 0.65 coefficient or adding a new balanced-stat multiplier requires express new authorization.

Equal-total investment matters: at 40/40, the proposed Greatsword F 1.27 gives `(52*1.27)^2=4361.2816`, whereas an 80/0 STR specialist using a proposed Greataxe F 1.34 gives `(80*1.34)^2=11491.84`. Both-stat users gain flexibility, not necessarily optimal raw single-stat Power. At same A, F 1.34 is 79.56% higher *Power* than F 1.00 owing to squaring, so differences need deliberate purpose.

## Seven-column weapon comparison plus build results

Every row retains a prominent **Primary Coverage** field; numerical target counts, arc widths and multiple-hit algorithms are intentionally unfinished. All figures below are raw Power, not final wounds, actual attack hits or armor penetration. All weapon-specific prerequisites and Fs are trial data.

| ID | Weapon | Stat Scaling | Candidate minimum | Candidate F | **Primary Coverage** | Balanced 40/40 | STR-led 60/20 | DEX-led 20/60 | STR pure 80/0 | DEX pure 0/80 | Balanced 20/20 |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| L-01 | Dagger | DEX | DEX 8 | 1.00 | Point | 1,600 | 400 | 3,600 | Not eligible | 6,400 | 400 |
| L-02 | Stiletto | DEX | DEX 12 | 1.01 | Point | 1,632 | 408 | 3,672 | Not eligible | 6,529 | 408 |
| L-03 | Short knife | Either | STR 7 or DEX 7 | 0.97 | Narrow | 1,505 | 3,387 | 3,387 | 6,022 | 6,022 | 376 |
| L-04 | Cestus / knuckle weapon | STR | STR 9 | 1.00 | Narrow | 1,600 | 3,600 | 400 | 6,400 | Not eligible | 400 |
| L-05 | Hand axe | STR | STR 12 | 1.05 | Sweep | 1,764 | 3,969 | 441 | 7,056 | Not eligible | 441 |
| L-06 | Light pick | STR | STR 12 | 1.05 | Point | 1,764 | 3,969 | 441 | 7,056 | Not eligible | 441 |
| L-07 | Short club | STR | STR 8 | 0.97 | Narrow | 1,505 | 3,387 | 376 | 6,022 | Not eligible | 376 |
| L-08 | Sickle | DEX | DEX 12 | 1.00 | Narrow | 1,600 | 400 | 3,600 | Not eligible | 6,400 | 400 |
| M-01 | Arming sword | Either | STR 15 or DEX 15 | 1.14 | Sweep | 2,079 | 4,679 | 4,679 | 8,317 | 8,317 | 520 |
| M-02 | Longsword | Both | STR 18 and DEX 18 | 1.10 | Sweep | 3,272 | 3,272 | 3,272 | Not eligible | Not eligible | 818 |
| M-03 | Rapier | DEX | DEX 24 | 1.13 | Point | 2,043 | Not eligible | 4,597 | Not eligible | 8,172 | Not eligible |
| M-04 | Sabre | DEX | DEX 20 | 1.15 | Sweep | 2,116 | 529 | 4,761 | Not eligible | 8,464 | 529 |
| M-05 | Falchion | STR | STR 22 | 1.19 | Sweep | 2,266 | 5,098 | Not eligible | 9,063 | Not eligible | Not eligible |
| M-06 | Mace / flanged mace | STR | STR 20 | 1.17 | Narrow | 2,190 | 4,928 | 548 | 8,761 | Not eligible | 548 |
| M-07 | Warhammer | STR | STR 21 | 1.18 | Narrow | 2,228 | 5,013 | Not eligible | 8,911 | Not eligible | Not eligible |
| M-08 | War pick | STR | STR 22 | 1.17 | Point | 2,190 | 4,928 | Not eligible | 8,761 | Not eligible | Not eligible |
| M-09 | Battleaxe | STR | STR 23 | 1.20 | Sweep | 2,304 | 5,184 | Not eligible | 9,216 | Not eligible | Not eligible |
| M-10 | Short spear | Either | STR 15 or DEX 15 | 1.12 | Point | 2,007 | 4,516 | 4,516 | 8,028 | 8,028 | 502 |
| M-11 | Quarterstaff | Both | STR 13 and DEX 15 | 1.07 | Sweep | 3,096 | 3,096 | 3,096 | Not eligible | Not eligible | 774 |
| H-01 | Greatsword | Both | STR 35 and DEX 24 | 1.27 | Wide Sweep | 4,361 | Not eligible | Not eligible | Not eligible | Not eligible | Not eligible |
| H-02 | Zweihander | Both | STR 40 and DEX 28 | 1.29 | Wide Sweep | 4,500 | Not eligible | Not eligible | Not eligible | Not eligible | Not eligible |
| H-03 | Greataxe | STR | STR 39 | 1.34 | Wide Sweep | 2,873 | 6,464 | Not eligible | 11,492 | Not eligible | Not eligible |
| H-04 | Maul | STR | STR 40 | 1.32 | Sweep | 2,788 | 6,273 | Not eligible | 11,151 | Not eligible | Not eligible |
| H-05 | Great hammer | STR | STR 42 | 1.35 | Sweep | Not eligible | 6,561 | Not eligible | 11,664 | Not eligible | Not eligible |
| H-06 | Poleaxe | Both | STR 35 and DEX 24 | 1.26 | Point (top spike) | 4,293 | Not eligible | Not eligible | Not eligible | Not eligible | Not eligible |
| H-07 | Halberd | Both | STR 33 and DEX 25 | 1.25 | Sweep | 4,225 | Not eligible | Not eligible | Not eligible | Not eligible | Not eligible |
| H-08 | Glaive | Both | STR 30 and DEX 24 | 1.24 | Sweep | 4,158 | Not eligible | Not eligible | Not eligible | Not eligible | Not eligible |
| H-09 | Pike | Both | STR 28 and DEX 22 | 1.20 | Line | 3,894 | Not eligible | Not eligible | Not eligible | Not eligible | Not eligible |
| H-10 | Long spear | Either | STR 27 or DEX 27 | 1.20 | Point | 2,304 | 5,184 | 5,184 | 9,216 | 9,216 | Not eligible |
| H-11 | Lance | STR | STR 36 | 1.28 | Point | 2,621 | 5,898 | Not eligible | 10,486 | Not eligible | Not eligible |
| H-12 | Heavy flail | STR | STR 42 | 1.30 | Sweep | Not eligible | 6,084 | Not eligible | 10,816 | Not eligible | Not eligible |

## Highest raw Power from candidates in each build

- **Balanced 40/40:** largest raw eligible candidates are **Zweihander** (4500) and **Greatsword** (4361). Does not rank overall usefulness.
- **STR-led 60/20:** largest raw eligible candidates are **Great hammer** (6561) and **Greataxe** (6464). Does not rank overall usefulness.
- **DEX-led 20/60:** largest raw eligible candidates are **Long spear** (5184) and **Sabre** (4761). Does not rank overall usefulness.
- **STR pure 80/0:** largest raw eligible candidates are **Great hammer** (11664) and **Greataxe** (11492). Does not rank overall usefulness.
- **DEX pure 0/80:** largest raw eligible candidates are **Long spear** (9216) and **Sabre** (8464). Does not rank overall usefulness.
- **Balanced 20/20:** largest raw eligible candidates are **Longsword** (818) and **Quarterstaff** (774). Does not rank overall usefulness.

## Recommendations for author review, NOT approved

1. **Keep the current approved Both formula for now.** Represent Both as dual prerequisites plus sum-based output, not as an unseen new 'balanced-stat bonus'. If the author wants even STR/DEX to outscore unequal distributions at same total, that is a separate new formula decision.
2. **Tune minimums and F together.** Never scale every Medium by 1.15 or every Heavy by 1.30 on top of the already-listed individual F. Test equal total attribute investment and stat gating, not just 40 STR vs 40/40 STR/DEX.
3. **Distinguish primary and alternate strike leverage.** The catalogue presently shares primary F with pommel/haft/spike alternates. That could let a heavy cutting weapon deliver equal Power as a specialized blunt weapon through its pommel. **Option A (preferred): individual alternate-mode F**, justified by physical contact geometry; **Option B (rough test only): secondary F=0.85× primary for improvised haft/pommel and 0.95× for a purpose-built spike or side edge**, without stacking extra type factor. Both numeric ratios and all alternate F are NOT CANON.
4. **Define handling when minimums are missed** before finalizing weapon prerequisite gates. Both stat's 0.65 formula cannot legally activate without both its explicitly stated minima; no automatic partial Both scaling is approved. Further physical mass and SPD penalties for melee are unresolved; do not silently apply the firearm-specific 2%-SPD STR-shortfall model to every sword.
5. **Separate role from numeric Power.** Reach, grapple viability, attack geometry, real blade faces, offhand availability and later armor interaction can support a low-F shape. Slashing/Piercing/Blunt 5-point roles are relative qualitative guidelines, not automatic Power multipliers. The user wants quantitative coverage left unfinished here.
6. **Armor-first milestone remains binding:** Finish the five weapon-SHAPE tasks, then go DIRECTLY TO ARMOR before material/quality/enchantment and other weapon crafting. Weapons are not the totality of equipment.

## Next explicit approval requested

Are the individual `F` values and STR/DEX minima acceptable as a first numeric canon pass, or which family should be tuned before approval? Independently, should alternate attacks use separately calibrated F values rather than always sharing primary F? This draft does not change any existing approved weapon profile.


## November 6, 2026 — Approved design adjustments, exact numbers still provisional

**AUTHOR CHOICES:** Preserve the existing Both `0.65(STR+DEX)` coefficient, with dual minima. Melee secondary attacks should be slightly weaker in F than the main motion, with **greatsword secondary stabbing / Piercing** and emergency pommel limited to comparable **unarmed Power** rather than using a greatsword F and Both A. DEX-led melee weapons need a modest **Support STR minimum** (including legitimately equipped STR bonuses); STR-led melee weapon shapes have **no required reciprocal DEX minimum** solely for being STR-led, whereas STR-led ranged weapons should have some minimum DEX to aim and handle them.

**Additional numeric DRAFT ONLY:** The 31-shape main catalogue now shows a proposed secondary F=0.95× primary, not the prior 0.85× generic pommel/0.95× secondary rule; actual purpose-built distinct-head secondaries may need separately calibrated F. The 0.95 value and per-shape physical STR floors are **unapproved example numbers**, as are all existing individual primary values. If a weapon requires DEX for governing A, its small Support STR floor is an eligibility gate and does NOT replace DEX in its actual Power expression. If an Either-stat melee weapon opts for DEX scaling, apply the STR floor; if it opts for STR scaling, it does not acquire an automatic DEX floor. For Both, the STR minimum already exists. Ranged small handling-DEX numeric gates will be proposed in the ranged catalogue. The prior draft's recommendation to give improvised pommel strike a fraction of the full greatsword F is **superseded** by the author's stricter unarmed-damage ceiling. Existing full build comparison remains solely a test, and numerical coverage is untouched.
