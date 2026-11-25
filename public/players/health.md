HP measures how much ordinary damage you can withstand. Endurance gives you natural HP; health training can add more. Armor reduces damage before it reaches HP, while Evasion helps you avoid the hit altogether.

## Your ordinary health

Natural ordinary HP starts at **75**, then adds the contribution from effective END. Add eligible purchased HP separately under your table's training menu.

{{table:health-curve}}

Read the bands in order. END 60 contributes 50 × 4 plus 10 × 3.5, giving **310 natural HP** after adding the base 75. END 120 contributes 200 + 175 + 60, giving **510 natural HP**. These are examples before health training or other lawful HP modifiers.

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
