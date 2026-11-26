HP measures how much ordinary damage you can withstand. Endurance gives you natural HP; health training can add more. Armor reduces damage before it reaches HP, while Evasion helps you avoid the hit altogether.

## Your ordinary health

Natural ordinary HP starts at **75**, then adds the contribution from effective END. Add eligible purchased HP separately under your table's training menu.

{{table:health-curve}}

Read the bands in order. END 60 contributes 50 × 4 plus 10 × 3.5, giving **310 natural HP** after adding the base 115. END 120 contributes 200 + 1115 + 60, giving **510 natural HP**. These are examples before health training or other lawful HP modifiers.

## Increasing your health

- Increase END to improve natural HP.
- Spend TP on health training using your table's selected benefits and cap.
- Use armor and suitable resistances to make the same HP last longer.
- Improve Evasion, positioning, and teamwork to reduce incoming hits.

Health training and natural HP remain separate on the sheet. This makes caps and level-scaled purchased benefits easier to check.

## Resolving damage

For a physical HP attack, fixed Armor Penetration first reduces applicable armor, to a minimum of zero. Subtract that remaining armor from the attack's final raw damage, again to a minimum of zero. Deduct the resulting damage from HP.

**Example:** an attack with 40 raw damage and 10 AP hits armor 25. Remaining armor is 15; HP damage is 25. Armor can fully stop an attack. A hit by itself does not guarantee HP damage.

Damage type, real coverage, shields, and specific resistances can change which defenses apply. See [equipment](/learn/equipment/) and [conditions](/learn/conditions/).

## Hero Shimmer Reserve

A qualifying Hero has a Shimmer Reserve equal to **100% of maximum ordinary HP**. Record it separately. Ordinary hits first reduce ordinary HP; when that is exhausted, the reserve activates to absorb further damage. The exact overflow edge at activation still needs table adjudication.

An intact, dormant Guard also protects against a single devastating attack. If its post-armor damage reaches **ceil(51% of full combined maximum HP)**, the Guard negates that whole hit and breaks. The unused reserve is forfeited; your ordinary HP stays at its preattack value. This emergency Break is unavailable after the reserve has activated.

::: detail Emergency Break example
With maximum ordinary HP 310 and reserve 310, full combined maximum is 620. The emergency threshold is ceil(0.51 × 620) = **317 post-armor damage**. Use maximum combined HP for this test, rather than your current HP or only your ordinary maximum.
:::

## Rest and medical care

{{table:sleep-recovery}}

Recovery is added to current ordinary HP and stops at its maximum. A qualifying Hero's sleep also fully restores Shimmer Reserve, including a Guard broken by emergency Break; medical attention is not required for that reset.

A broken Guard becomes available at the earlier of qualifying sleep or 24 hours after the Break. Whether the 24-hour timer alone refills the reserve remains unsettled. Your GM also determines what counts as qualifying sleep and medical attention.

## Hex exposure and poisoning

Hexed I and II begin at one and two times the applicable status threshold. Four times causes acute Hex Sickness; eight times causes a Hex-induced coma. Isolated exposure below half the threshold usually needs no chronic tracking, but repeated exposure can still cause lasting harm. Untreated coma outcomes are 10% recovery, 50% Hexen transformation and 40% death. Quality I healing improves recovery and reduces death by ten percentage points; Quality IV guarantees survival, not freedom from mutation. Living alchemy may prevent an incomplete mutation by extracting bodily Hex; reversing established Hexen transformation is a near-miraculous undertaking. Chronic exposure, organ damage and augmentation rejection require appropriate treatment. Exact chronic rates and treatment procedures remain table questions.

## Chronic Hex and inoculation

Ordinary creatures process about 3 Hex particles per day at the reference capacity; ordinary Hexen process 30. END governs tolerance and processing, with exact scaling settled at the table. Significant exposure can leave Hex Burden even after combat buildup clears; repeated near-limit incidents matter. Gradual adaptation can permanently increase Hex resistance while reducing health, mana output and lifespan.

| Inoculation | Hex resistance | Maximum HP, MP and mana output/recovery | Natural lifespan |
|---|---:|---:|---:|
| I | +10% | -2% | -5% |
| II | +20% | -4% | -10% |
| III | +35% | -7% | -20% |
| IV | +50% | -10% | -30% |
| V | +75% | -15% | -40% |

Apply the listed tier, not all previous tiers together. Exceptional Living Alchemy may reverse damage at the expense of resistance. Resolve a Hex coma once per medical crisis; the highest effective healing Quality shifts 10 percentage points per tier from death to recovery, capped at 40. Mutation remains 50% under conventional treatment. Recovery does not guarantee absence of lasting damage. Exact exposure conversion, inoculation advancement and crisis duration are table questions.

## Breathing Haze

Effective Haze 0/I/II/III/IV/V gives reference daily absorption of 0/1.5/6/24/96/384 Hex particles. Ordinary creatures process 2 + END/10 per day. Inoculation I–V reduces ambient absorption by 10/25/50/65/80%. Ordinary powered Clearbreaths and Purity Circles each lower effective Haze by two tiers; their ordinary protection does not stack. Haze I/II has no routine combat buildup; III adds 5/minute, IV 10/turn and V 40/turn. Rapidly absorbed Hex adds 10 buildup per particle; ambient acute disruption is not an extra retained particle dose. Infants temporarily retain maternal protection, children adapt faster and gradual inoculation carries lasting health costs. Sustained sickness may accelerate adaptation but is dangerous. Exact advancement schedules and exposure overlap require GM adjudication.

## Adaptation over time

Comfortable sustained exposure reaches inoculation I/II/III/IV/V at cumulative adult benchmarks of one week, three months, one year, five years and fifteen years. Children adapt twice as quickly. Persistent mild/moderate/severe sickness accelerates adaptation 2/3/4 times, but acute poisoning is a medical crisis, not safe training. Negligible exposure or environmental equilibrium can halt progress. Infants temporarily retain maternal absorption protection, not permanent inoculation. Tier V is uncommon and associated with prolonged dangerous exposure; wealthy protected residents may never inoculate.
