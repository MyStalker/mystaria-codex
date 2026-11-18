"""Build a readable draft from the actual result tables."""

import csv
import json
from collections import defaultdict
from itertools import product
from pathlib import Path
from statistics import mean

from fixtures import *
from calibration import contacts, threshold_chance, sr

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results'
REPORT = ROOT/'Mystaria_Elemental_Enchantment_Balance_DRAFT.md'


def read(name):
    with (OUT/(name+'.csv')).open(encoding='utf-8') as f:
        return list(csv.DictReader(f))


def select(rows, **filters):
    return [r for r in rows if all(r.get(k)==str(v) for k,v in filters.items())]


def avg(rows, key):
    return mean(float(r[key]) for r in rows) if rows else 0


def num(value, digits=2):
    return f'{float(value):,.{digits}f}'


def pct(value):
    return f'{100*float(value):.1f}%'


def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |',
                      '| '+' | '.join(['---']*len(headers))+' |',
                      *['| '+' | '.join(str(x) for x in row)+' |' for row in rows]])+'\n'


def main():
    params=json.loads((ROOT/'parameters.json').read_text())
    powers=params['recommended']
    fit=json.loads((OUT/'calibration.json').read_text())
    population,identities,mundane,synergies,sensitivity,sixth,precision = [read(name) for name in
        ('population','identities','mundane','synergies','sensitivities','tier_VI','precision')]
    if (OUT/'VI_extended.csv').exists():
        sixth += read('VI_extended')
    exact=read('exact_thresholds')
    pieces=[]
    def add(text):
        pieces.append(text.strip()+'\n')
    add('''# Mystaria elemental enchantment balance study

**EXPERIMENTAL DRAFT — AUTHOR APPROVAL REQUIRED**

November 18, 2026. Source main commit `930efc89269da5cc266976861fc5215b32c1a0b6`.

This report evaluates experimental candidates awaiting explicit author approval.

## Executive summary

The initial ladder fails ordinary-tier consistency. Against a geared generalist in Medium Glassweave, ignition needs 8 / 5 / 3 / 3 / 4 legal contacts. Against Medium Nullporcelain it needs 11 / 6 / 4 / 5 / 5. Tier III therefore becomes a conspicuous anti-MR breakthrough, while Tier I Glassweave is much stronger than the requested modest reduction from the old Fire benchmark.

The recommended next test candidate uses shared Power **610 / 1,000 / 2,250 / 3,800 / 6,100 / 12,200**, with **typed SR = (effective END + 0.50 × applicable MR)² × specific resistance multiplier**. For the reference generalist in Medium armor, ordinary MR0 ignition stays at two contacts at all five milestones. Glassweave requires 4 / 5 / 4 / 4 / 4. Nullporcelain requires 6 / 7 / 6 / 6 / 5. These are deterministic healthy-target counts. Pressure, wounds, actual contact probability, cleansing, shattering and allies change combat outcomes.

This candidate leaves important targets partly unmet. Tier II Glassweave loses substantially more effectiveness than the requested modest reduction, while several later Glassweave fixtures tie the old Fire result because they occupy the same discrete contact and injury bands. Solo Ice freezes the reference MR0 generalist in about 56% of Tier I trials and cannot reach Frozen in the corresponding later-tier five-round fixtures. A separately tested Tier II Power of **1,150** keeps Glassweave closer to the old benchmark and weakens MR0 END50 protection. The close-scoring 0.40 joint fit is also compared across elements. The author should select these tradeoffs explicitly.

Material names alone cannot define universal effectiveness bands. For example, QV Light Nullporcelain has MR85 while Heavy Glassweave has MR115. Any monotone universal MR equation must respect that ordering. Greater END investment also reduces every elemental option, as intended. A universal ladder cannot make every MR0 END50 target highly vulnerable while keeping every generalist Glassweave target slightly below its earlier Fire benchmark.

Lightning's main benefit is denial of a second action. A Shocked target still has one action for a legal Quick Attack. Counting each Shocked turn as a fully skipped turn overstates its value. Ice's 4× and 12× thresholds become accessible primarily through teamwork, vulnerability or Air. Air and Water require explicit evaluation order, and percentage Hex needs a clearly defined capacity basis.

Tier VI 15,000 is viable as an aggressive design option, but its five-round activation permits several attacks per paid activation. Two paid uses can support ten attacking rounds. The cost limits encounter and expedition ammunition more strongly than immediate action denial. Other Tier VI elements still need an author-approved Standard-versus-Powerful cost assignment.

## Canon and scope audit

The index and changelog were retrieved first, followed by the requested subject references and repository instructions at the pinned main commit. `sources.json` lists the retrievals. Latest elemental directions control over historical conflicting paragraphs.

The latest GitHub main still treats additive Weapon Rating as experimental. Its approved physical model is `(A × F × Quality factor)²`, with Quality factor 1 / 1.01 / 1.02 / 1.03 / 1.04. The previous Burning Edge test used additive Candidate C. This study evaluates both. Candidate C uses `A² + WR²`, the archived C ladders and the current armor tables. Neither comparison authorizes a new physical rule.

Hero injury penalties are applied to effective attributes. The five injury advancements include Shimmer Guard, with penalties 0 / −5% / −5% / −5% / −10% / −15%. Incapacitation ends ordinary action. Armor defense is `END² + [AR × (1 − penetration)]²`. The obsolete combat-only +10 is omitted following the global racial rebase. Impact ratios above 0.75 / 1.75 / 3 produce 1 / 2 / 3 stages.

The seven elements share identical Power within every tested ladder. Elemental delivery follows genuine pathways, actual armor location and shield routing. Spell access, available media and mana color require their own approved rules.

## Shared six-tier Power comparison
''')
    add(table(['Effect tier','Level fixture','Approved Fire','Initial candidate','Recommended candidate','New / approved'],
              ((i+1,LEVELS[min(i,4)],f'{APPROVED[i]:,}' if i<5 else 'Open',f'{INITIAL[i]:,}',f'{p:,}',
                num(p/APPROVED[i])+'×' if i<5 else 'Open') for i,p in enumerate(powers))))
    add('''Ordinary reference tiers I–V are evaluated at levels 10 / 25 / 50 / 75 / 100. These pairings are test fixtures. Physical Quality access follows its existing availability and handling requirements. Mixed item Quality equals its effect tier. Full Quality I–V yields effect Tier II–VI, with zero stat bonus on that Full item.

## MR formulas and calibration

The additive-before-squaring candidate is `S = (E + cM)²R`. The alternative is `S = (E² + (cM)²)R`. `E` is current effective END, including full eligible item END and injuries. `M` is the applicable covered-surface MR. `R` is the established specific resistance multiplier, with reciprocal treatment for a defined weakness. MR0 preserves base `END²R`.

Both formula families were screened at coefficients 0.40 / 0.50 / 0.65 / 0.75 / 1.00. The first pass jointly fitted all six Powers and the MR coefficient. The second required Tier VI to reach at least 1.8 times Tier V Power. The looser first fit favored 8,900 for VI, which offered too small an exceptional step. This 1.8 constraint is a stated design judgment. The final fit selected 12,200, exactly twice V.

The loss function uses equal milestone weights and stated weights for reference generalists, END30 and END50, plus MR0, Medium Glassweave and Medium/Heavy Nullporcelain. Targets include approximately 88% five-round MR0 threshold access, a Glassweave target ten probability points below the old benchmark, and low ordinary Nullporcelain access. Contact-ratio penalties break discrete probability plateaus. The score reflects the stated design objective and its selected weights. `calibration.py` contains every weight, candidate bound and grid step.
''')
    add(table(['Formula','MR coefficient','Jointly fitted I–VI Powers','Design loss'],
              (('Add before square' if f=='linear' else 'Separate squares',c,
                ' / '.join(f'{p:,}' for p in ladder),num(loss,3)) for loss,f,c,ladder in fit)))
    rows=[]
    for c in (.40,.50,.65,.75,1.):
        for i in (0,2,4):
            e=hero(LEVELS[i],'generalist',i+1).stats[2]
            counts=[contacts(INITIAL[i],sr(e,suit(m,'Medium',i+1).mr,c)) for m in
                    ('Boughsteel','Glassweave','Nullporcelain')]
            rows.append((c,LEVELS[i],*counts))
    add(table(['c with initial ladder','Level','MR0 contacts','Glassweave contacts','Nullporcelain contacts'],rows))
    robustness=read('cross_element_fits') if (OUT/'cross_element_fits.csv').exists() else []
    if robustness:
        comparisons=[]
        for c in (.4,.5,.65):
            for level in LEVELS:
                base=select(robustness,coeff=c,level=level,role='generalist')
                fire_mr0=select(base,attackers='Fire',material='Boughsteel')
                fire_glass=select(base,attackers='Fire',material='Glassweave')
                fire_null=select(base,attackers='Fire',material='Nullporcelain')
                ice=select(base,attackers='Ice',material='Boughsteel')
                lightning=select(base,attackers='Lightning',material='Boughsteel')
                comparisons.append((c,level,num(avg(fire_mr0,'fire')),num(avg(fire_glass,'fire')),
                                    num(avg(fire_null,'fire')),pct(avg(ice,'freeze')),
                                    num(avg(lightning,'lightning_denied'))))
        add('### Cross-element recheck of the close joint fits')
        add(table(['Joint-fit c','Level','MR0 Fire stages','Glassweave Fire stages','Nullporcelain Fire stages',
                   'Solo MR0 Ice freezes','Solo MR0 Lightning actions denied'],comparisons))
    add('''Coupling the initial 0.65 coefficient to the initial Power ladder produces the early/middle swing. A re-fitted 0.65 ladder remains a credible option. The 0.50 fit gives the lowest score under this report's selected targets, with 0.40 close behind. Separate squares removes the END×MR cross term and changes how general MR complements END. It needs its own ladder.

## Character population and equipment

The neutral-END reference race is Duskpaw. Starting base STR13 / DEX20 / END14 / INT17 / SPD17 and INT +25% are applied, with two discretionary points per level gained and +1 to all base attributes at every fifth level. Allocations use whole points through a largest-remainder distribution. Racial modifiers precede item bonuses.

Allocations in STR / DEX / END / INT / SPD order are generalist 20/20/20/20/20%, END30 20/15/30/15/20%, END40 20/15/40/10/15%, END50 20/10/50/5/15%, physical 50/10/15/5/20%, caster 10/10/20/45/15%. The zero-personal-MP control uses Moontouched with its actual starting attributes and SPD +25%.

The peer equipment fixture supplies +6 / +12 / +20 / +28 / +36 to each attribute at the matching milestone, preserving the prior benchmark's full equipment contributions. At level 100 this is 180 total equipment attribute points. Five pure-stat items account for these five bonuses. Their strain is 5 / 10 / 20 / 30 / 40. The test weapon is a separate Mixed item with its own strain and half-size bonus, allocated to INT for a controlled physical comparison. An additional weapon test allocates it to STR. Full VI supplies zero weapon stats. The primary MP reserve follows the canon's effective-END formula, including the eligible equipment END bonus, then subtracts equipment Soul Strain. END governs the ordinary personal MP capacity. A first-pass assumption excluded equipment END from MP. All affected results were rerun with equipment END included, and the excluded-equipment interpretation remains an explicit Hex sensitivity.

This is a controlled gear fixture. Acquisition of that distribution depends on each build and its actual budget. The zero-MP control uses mundane gear because ordinary natural mana cannot fund the assumed equipment strain. External Warlock mana and alternative strain-capacity arrangements require separate character-specific rules. A no-bonus gear sensitivity is included.
''')
    add(table(['Level','Quality','Generalist END','END30','END40','END50','Physical END','Natural MP / available generalist MP','Gear stat total'],
              ((l,i+1,*[num(hero(l,b,i+1).stats[2],0) for b in ('generalist','END30','END40','END50','physical')],
                f'{hero(l,"generalist",i+1).capacity} / {hero(l,"generalist",i+1).mp}',
                5*GEAR[i]) for i,l in enumerate(LEVELS))))
    add('''All Light / Medium / Heavy profiles use the approved pure and composite tables. Full coverage applies the rating of the actual protected surface. Support STR qualification is enforced before a fixture enters a result table. Unqualified profiles are retained in `unqualified.csv`. The study avoids underqualified gear and the associated movement penalty. Coverage sensitivities compare actual covered contact against a legal exposed contact. Each covered or exposed contact is explicitly specified.

Ceramic armor advances Intact → Cracked → Shattered on real Solid physical impacts and shatters immediately on Devastating or Overwhelming physical impacts. Cracked retains full protection. Shattered pure armor loses AR/MR. The two composites retain their approved backing AR and lose MR. Support STR and intrinsic SPD burden remain unchanged. Energy-only contact leaves ceramic condition intact.

## Exact contact requirements and probability

For a healthy target with fixed SR and per-contact Power `P`, reaching an inclusive threshold `tS` requires `ceil(tS/P)` contacts. Exceeding SR requires `floor(S/P)+1`. Fire, Water, Air, Hex and Acid use the strict >1 threshold. Ice and Lightning use ≥1 according to the latest direction. Half, 4× and 12× use inclusive thresholds.

The following matrix uses Fire's strict >1 threshold. Each cell gives Light / Medium / Heavy contact counts. A dash means the reference wearer fails the actual armor support gate.
''')
    main_rows=[]
    for role in ('generalist','END30','END40','END50'):
        for i,l in enumerate(LEVELS):
            cells=[]
            for m in tuple(ARMOR)[:5]:
                cell=[]
                for cl in CLASSES:
                    selected=select(exact,candidate='recommended',level=l,tier=i+1,armor=m,armor_class=cl,role=role)
                    cell.append(selected[0]['main_contacts'] if selected else '—')
                cells.append(' / '.join(cell))
            main_rows.append((role,l,*cells))
    add(table(['END allocation','Level','Boughsteel L/M/H','Glassweave L/M/H','Bough/Glass L/M/H','Nullporcelain L/M/H','Adamant/Null L/M/H'],
              ((r[0],r[1],r[2],r[3],r[5],r[4],r[6]) for r in main_rows)))
    add(table(['Contacts needed before expiry','Within 3 rounds, p=.65','Within 5 rounds, p=.65','Within 5 rounds, p=.45','Two attackers, 5 rounds, p=.65 each'],
              ((k,pct(threshold_chance(k,3)),pct(threshold_chance(k)),pct(threshold_chance(k,5,.45)),pct(threshold_chance(k,5,.65,2)))
               for k in range(1,11))))
    add('''These exact Bernoulli calculations track the three-target-turn timer and maximum live accumulated contacts. The application-turn tick and two following target-turn ticks exhaust an unrefreshed condition. The values represent specified contact probabilities, without Pressure or injury feedback. They distinguish legal contact counts from hit probabilities.

## Simulation procedure and uncertainty

Every ordinary scenario uses 12,000 trials and seed **20261118**, with NumPy PCG64 d20 histories. Each matchup reuses the same random histories for paired comparisons. There are 60,000-trial paired precision checks and three additional seeds for selected weapon contrasts. Scenario-trials share histories. Use the per-fixture and paired uncertainty intervals when interpreting those correlated results.

Each attacker takes one ordinary legal Full Attack per turn for five rounds. Attackers are unarmored in this controlled matrix, including the counterattack fixture. A Double Strike sensitivity uses two independent d20 results, 60% physical Power per hit, and the existing self-PP, with both weapons paid separately. A Quick Attack sensitivity applies the existing one-category accuracy cost and full physical Power. These actions retain one offensive attack-action per turn.

The ordinary observation window is eight rounds, including the post-activation tail. The second-activation VI window covers ten attack rounds and two further target turns. Contacts add magnitude before the defender's turn. The target resolves action availability, optional escape/cleanse/counterattack, then Fire and Hex ticks, then timers. A valid application permits effects on that target turn and two following turns. A separate Fire first-tick timing sensitivity is provided. Every ordinary tick stops after incapacity. Recorded stages are actual capped injury advancement, with separate potential event-stage counters.

Hit probability follows the approved Naked d20 pilot and current Combat Speed. One ongoing PP from a relevant elemental condition makes incoming attacks one category easier at net PP1–2. Three or more distinct valid PPs make them two easier. Each elemental PP source supplies one ongoing point throughout its ticks. Ice's SPD decrease affects SPD only, then Combat Speed is recomputed using DEX/4 and armor. Frozen and Stunned have separate ordinary-action effects.

Physical shields use the same attack d20 for natural miss / actual shield collision / body contact. A body rider requires actual bodily delivery. Real durability and shield-breaking physical overflow are included. The conditional elemental delivery on a breaking overflow remains conservative unless genuine delivery is separately established. Glassweave/Nullporcelain spell interception cannot be fully simulated because magical absorption/overflow conversion remains open. Spell-shield numerical conversion awaits author approval.

Per-scenario binomial 95% sampling half-width is at most about **0.90 percentage points** at 12,000 trials and **0.40 points** at 60,000. For a bounded 0–5-stage outcome, a conservative 95% half-width is 0.045 stages at 12,000 trials. Individual standard errors are retained for primary outcomes. Systematic uncertainty from unresolved rules exceeds sampling noise in several cases.

### Reference Fire outcomes with status delivery isolated

This fixture supplies legal elemental contact while suppressing the accompanying physical injury, preserving the target long enough to observe the elemental effect. It is an analysis control. Integrated enchanted-weapon fixtures follow separately. Parenthetical tail probability records at least one injury after round five.
''')
    rows=[]
    for i,l in enumerate(LEVELS):
        for m in ('Boughsteel','Glassweave','Nullporcelain'):
            cells=[]
            for tag in ('approved','initial','recommended'):
                r=select(population,level=l,material=m,armor_class='Medium',role='generalist',variant=tag)[0]
                cells.append(f'{num(r["fire"])} stages, {pct(r["fire_wound"])} injured ({pct(r["tail"])} tail)')
            rows.append((l,m,*cells))
    add(table(['Level','Medium armor','Approved END-only Fire','Initial candidate','Recommended candidate'],rows))
    add('''The approved column deliberately isolates the older END-only benchmark. Its equal results across MR materials describe that historical comparison. The newest MR-aware direction is evaluated in the candidate columns.

## The seven elemental identities

The table below averages only matched legal Medium-armor generalist fixtures over the five milestones and first five armor constructions. These conditional means describe this deliberately equal-weight scenario set. Identity fixtures use the recommended shared ladder and initial erosion/drain percentages.
''')
    rows=[]
    for element in ELEMENTS:
        r=select(identities,attackers=element,path='status-only',role='generalist',armor_class='Medium')
        rows.append((element,pct(avg(r,'meaningful')),num(avg(r,'total')),num(avg(r,'PP_turns')),
                     num(avg(r,'ice_denied')+avg(r,'lightning_denied')),
                     num(avg(r,'MP')),num(avg(r,'Leywell')),num(avg(r,'max_AR_removed')),num(avg(r,'max_MR_removed'))))
    add(table(['Element','Any meaningful outcome','Injury stages','PP-turns','Ordinary actions denied','Personal MP drained','Leywell MP drained','Peak AR points removed','Peak MR points removed'],rows))
    add('''### Fire

Fire remains the straightforward injury benchmark. Burning preserves accumulated rounds on refresh. Engulfed causes two stages each round, compared with Burning's one every second round. The specified cadence therefore jumps to four times Burning's long-run rate. The report preserves these explicit rates.

No-MR generalists face materially higher and earlier Fire output. END investment delays ignition and the 4× transition. Consequences can persist beyond the five-round weapon activation through the target timer. One available mundane douse can erase a large pool when the target still has an action and sufficient suitable water. Its action cost is a scenario assumption. Trufula's special extinguishing requirement is preserved.

### Ice

At ≥1× SR the target has SPD ×0.85 and half ordinary movement tiles. The report uses fractional movement allowance loss, since the ordinary tile baseline and halving-rounding rule remain open. Frozen at 4× prevents ordinary actions while allowing the modeled special struggle. Entombed at 12× prevents self-escape until the ordinary timer expires or external rescue applies.

A single per-turn STR² struggle is the default. An alternate no-struggle case quantifies the difference, and a separately labeled hypothetical eligible 6-MP magic escape is tested for casters. The hypothetical escape serves as a conditional scenario assumption. The action limit of eligible magic while Frozen is unresolved. The model spends the special escape opportunity during that frozen turn, then ordinary actions resume on a subsequent turn.

Without refresh, Frozen and Entombed expire with the three-turn status in this test. Their expiry follows the finite target-status timer. Continued reapplication can keep them alive. Net Ice gain per refreshed target turn is approximately `successful applications × P − STR²`. A STR-led target can clear a just-crossed threshold quickly. A low-STR caster may remain frozen throughout repeated incoming contact. The struggle must reduce the actual stored Ice pool. Virtual Air contribution is recalculated from its own surviving pool.
''')
    rows=[]
    for role in ('generalist','physical','caster','END50'):
        for team in ('Ice','Ice+Ice','Air+Ice'):
            if '+' in team:
                r=select(synergies,role=role,attackers=team,armor_class='Medium',material='Boughsteel')
            else:
                r=select(identities,role=role,attackers=team,path='status-only',armor_class='Medium',material='Boughsteel')
            if r:
                rows.append((role,team,pct(avg(r,'freeze')),pct(avg(r,'entomb')),num(avg(r,'ice_denied')),num(avg(r,'struggles')),num(avg(r,'escapes'))))
    add(table(['Target build','Attackers','Frozen at least once','Entombed at least once','Ordinary actions denied','STR² struggles used','Successful struggles'],rows))
    ice_levels=[]
    for level in LEVELS:
        r=select(identities,level=level,role='generalist',attackers='Ice',path='status-only',
                 armor_class='Medium',material='Boughsteel')
        ice_levels.append((level,pct(avg(r,'freeze')),pct(avg(r,'entomb')),
                           num(avg(r,'ice_denied')),num(avg(r,'escapes'))))
    add(table(['Level, solo Ice versus MR0','Frozen fights','Entombed fights','Actions denied','Successful struggles'],ice_levels))
    if (OUT/'ice_parties.csv').exists():
        parties=read('ice_parties')
        party_rows=[]
        for tier,team,lock,variant in product((1,3,5,6),('Ice+Ice+Ice','Ice+Ice+Ice+Ice','Air+Ice+Ice+Ice'),
                                             ('raw','effective'),('Ice party concentration','Ice party second activation')):
            r=select(parties,tier=tier,attackers=team,ice_lock=lock,variant=variant,
                     material='Boughsteel',role='generalist')
            if r:
                party_rows.append((tier,team,lock,'10 rounds' if 'second' in variant else '5 rounds',
                                   pct(avg(r,'freeze')),pct(avg(r,'entomb')),num(avg(r,'ice_denied'))))
        add(table(['Effect tier','Concentrated team','Lock threshold','Attack window','Frozen','Entombed','Actions denied'],party_rows))
    add('''Air's effective-magnitude freeze interpretation can make struggles ineffective, because clearing stored Ice leaves the borrowed Air contribution active. The alternate raw-Ice lock thresholds retain Air's half-PP and slow support while avoiding a borrowed-magnitude hard lock. This raw-lock restriction is a proposed change to final-effect amplification and needs author approval.

Tier I is a severity outlier in the recommended fit. Its high Power relative to the reference END makes solo freezing more accessible than in later ordinary tiers. The close-scoring 0.40 joint fit lowers that opening-tier risk and gives up some Nullporcelain suppression. This is another reason to treat the minimum design-loss score as a candidate for author judgment.

### Lightning

Static stores magnitude until an eligible discharge. A successful discharge consumes its pool. The default decision includes the current successful hit, then discharges at ≥1× SR. A separate case requires the previously stored pool to qualify before the present attack. Subthreshold discharge consumption remains unresolved and is avoided by rational play in the primary fixtures.

Shocked removes one of two actions. A defender can still Quick Attack with the remaining action. Full Attack, ordinary two-action recharge and Double Strike become unavailable while only one action remains. An interruption cancels the already-in-progress action as part of the same action loss. Adding another lost action on top would change the stated economy and can create an unintended full skip.

At 4×, the main timing case has one Stunned/Trapped turn overlapping the three Shocked turns. A non-overlap sensitivity gives an extra Shocked turn. The model keeps a single active Stunned timer. Reapplying Shocked is compared with ignoring applications until the existing duration expires. Repeated refresh can maintain the one-action tax even when repeated 4× stuns are rare.
''')
    rows=[]
    for pattern,overlap,refresh in product(('first','peak'),(True,False),(True,False)):
        r=select(sensitivity,variant='Lightning timing',material='Boughsteel',lightning=pattern,overlap=overlap,shock_refresh=refresh)
        rows.append((pattern,'Overlap' if overlap else 'Follow after stun','Refresh' if refresh else 'No active refresh',
                     pct(avg(r,'shocked')),pct(avg(r,'stunned')),num(avg(r,'lightning_denied')),pct(avg(r,'denied_four'))))
    add(table(['Discharge policy','Timing','Reapplication','Shocked fights','Stunned fights','Actions denied','4+ consecutive taxed turns'],rows))
    add('''The peak policy stores for 4× when possible, then accepts a ≥1× discharge on the final attacking round. The first-threshold policy usually suppresses access to 4× by consuming Static earlier. A future one-turn post-stun recovery restriction can address repeated incapacitation. It should leave ordinary Shocked refresh as a separately approved question.

### Hex

The initial drain is 5% / 15% / 30% of the resource's available starting capacity each affected target turn, rounded up to whole MP separately per reservoir. Personal MP and each relevant item's Leywell are tracked separately. Soul Strain reduces personal availability before combat and is never drained as MP. A 4× rising edge ends modeled ongoing active effects, with installations and permanent stat benefits retained.

At zero personal MP, >1× Hex uses Fire's every-second-affected-round injury cadence, and 4× uses two stages per round. This is an unapproved damage candidate. The zero-MP control can therefore be injured without a prior mana reservoir. Below the principal threshold Hex supplies its ordinary PP and any applicable drain. Rounding matters at low capacity. A 5% debit from a 10-MP well rounds to 1 MP, effectively 10% of that full well. A 15% debit from a 15-MP personal reserve rounds to 3 MP, effectively 20%.

The caster and generalist have ordinary END-derived MP. END supplies the ordinary caster MP reserve. The primary targets carry one or two Full items alongside their five Blank stat items, within the eleven-slot limit. Their main Full well capacities are 20/30/40/50/60 MP. A second caster Full well has capacity 20/20/20/30/40 MP. These Full items contribute zero stats and zero equipment Soul Strain. A Mixed-target sensitivity instead includes one ordinary 10/20/30/40/50-MP well, its complete Mixed INT bonus and its extra Soul Strain. The eleven-well stress fixture uses eleven Full items and removes the five Blank stat items, preserving slot legality and their actual loss of bonuses.

Active cast expenditure is a separate sensitivity using a hypothetical 3-MP nonoffensive utility action alongside a legal Quick counterattack. That utility action remains a hypothetical scenario. The effect-ending diagnostic is conditional on a qualifying ongoing effect being present throughout the observation window. Actual five-round target item effects can naturally expire earlier, lowering the late termination opportunity. The short exchanges begin with their recorded resources and debit each actual expenditure.
''')
    rows=[]
    for rates in ('weak','initial','proposed_hex','strong'):
        for role in ('generalist','caster','zeroMP'):
            r=select(sensitivity,variant='Hex drains',material='Boughsteel',rates=rates,role=role)
            rows.append((rates,role,num(avg(r,'available_mp')),num(avg(r,'MP')),num(avg(r,'Leywell')),num(avg(r,'hex')),pct(avg(r,'drained_out'))))
    add(table(['Drain ladder','Target','Starting personal MP','MP drained','Leywell MP drained','Hex stages','Personal reserve emptied'],rows))
    add('''The 10% / 25% / 40% alternative is recommended for another author-directed Hex test. It more often empties a small ordinary reserve during sustained >1× contact. Percentage-of-current-MP would asymptotically drain unless a floor intervenes, while percentage-of-natural-capacity would punish strained characters more sharply. Those are different designs. Source scope, fixed starting capacity, rounding and damage onset require approval together.

### Water and Acid

The erosion tests use weak 3% / 8% / 20%, initial 5% / 15% / 30%, and strong 10% / 25% / 50% bands. A Water-specific 5% / 20% / 35% option is also included. Erosion is a current severity modifier of original intact AR/MR, with a floor of zero. The current band applies once to the original applicable rating. Reapplication refreshes magnitude. Expiry restores this temporary modifier. Permanent corrosion/restoration is unresolved.

For Acid, reducing AR by fraction `e` reduces the armor-squared defense term by `2e−e²`. The initial bands therefore remove 9.75% / 27.75% / 51% of the armor component. Total defense reduction is smaller because END² remains. Existing physical bypass applies once to the reduced AR. Acid's benefit grows with the number of allied physical attacks. Threshold crossings make it potent near an injury boundary and sometimes yield no added stage on a particular weapon.

For Water, the comparable MR defense effect is governed by `(END + c × MR × (1−e))²`. With no applicable MR, Water's ordinary erosion has no target value. The snapshot case determines Water's own band using MR before its own erosion. Its reduction then applies to other elements. The live case repeatedly recalculates Water against its eroded MR until the finite severity ladder stabilizes, using at most four monotone evaluations. It can cascade across a band without another contact. Every evaluation starts from the original rating and raw pools.
''')
    rows=[]
    for rates,water in product(('weak','initial','proposed_water','strong'),('snapshot','live')):
        r=select(sensitivity,variant='Water erosion',material='Glassweave',rates=rates,water=water)
        rows.append((rates,water,num(avg(r,'max_MR_removed')),num(avg(r,'fire')),num(avg(r,'water_cascade'))))
    add(table(['Water erosion','Self-SR policy','Peak MR points removed','Paired Fire stages','Cascade events per scenario'],rows))
    rows=[]
    for rates in ('weak','initial','strong'):
        r=select(sensitivity,variant='Acid erosion',material='Boughsteel',rates=rates)
        rows.append((rates,num(avg(r,'max_AR_removed')),num(avg(r,'physical')),num(avg(r,'total')),pct(avg(r,'meaningful'))))
    add(table(['Acid erosion','Peak AR points removed','Physical stages','Total stages','Meaningful fights'],rows))
    add('''The initial Acid 5% / 15% / 30% bands are the recommended retention candidate. Water needs more help as a support-only choice, so 5% / 20% / 35% with snapshot self-SR is the recommended next candidate. Team gains and action economy justify keeping erosion temporary and non-compounding during this pass.

### Air, cross-element ordering and explosion

For every element with a genuinely active nonzero raw pool, half-SR Air adds half its own raw magnitude. Above Air SR, final other-element magnitude is `(raw element + 0.5 × raw Air) × 2`. Air never amplifies itself, creates an absent condition, writes virtual magnitude into stored pools, or refreshes another element's timer. Every evaluation starts from raw stored pools.

At ≥4× Air SR, the primary explosion conversion is `blast Power = 4 × sum(raw accumulated pools, including Air)`. It resolves once against `END² + applicable MR²`, then normal injury-stage thresholds and Shimmer Guard. The alternative tests amplified pool summation and an END-only blast defense. These conversion rules remain proposals because the author's quadruple-Power direction does not specify defense or pool accounting. The proposed explosion targets the affected creature.

A useful mathematical check is that Air alone at its trigger already stores ≥4× its SR. Multiplying its pool by four gives ≥16× SR. On an MR0 equal-defense target, that is normally an Overwhelming three-stage hit. Apply the existing Overwhelming injury cap. Summing several pools can increase raw Power greatly, while injury per explosion remains capped by the existing three-stage impact result.

The raw-pool conversion avoids multiplying the same stored energy through the half-Air contribution, ×2 final effects and ×4 blast in succession. The amplified-pool alternative can be much larger without changing the capped injury category in an already Overwhelming case. Clearing all magnitude can also remove a valuable ongoing Fire/Hex or erosion effect, so explosion timing creates real tradeoffs.
''')
    rows=[]
    for element in ('Fire','Ice','Lightning','Water','Hex','Acid'):
        for pair in ((element,element),('Air',element),('Water',element)):
            r=select(synergies,role='generalist',armor_class='Medium',attackers='+'.join(pair),material='Boughsteel')
            rows.append(('+'.join(pair),pct(avg(r,'meaningful')),num(avg(r,'total')),
                         num(avg(r,'lightning_denied')+avg(r,'ice_denied')),
                         pct(avg(r,'freeze')),pct(avg(r,'entomb')),num(avg(r,'explosions'))))
    for pattern in ('Air+Air','Air+Air+Fire'):
        r=select(synergies,role='generalist',armor_class='Medium',attackers=pattern,material='Boughsteel')
        rows.append((pattern,pct(avg(r,'meaningful')),num(avg(r,'total')),
                     num(avg(r,'lightning_denied')+avg(r,'ice_denied')),
                     pct(avg(r,'freeze')),pct(avg(r,'entomb')),num(avg(r,'explosions'))))
    add(table(['Team against MR0','Meaningful','Total stages','Actions denied','Frozen','Entombed','Explosions'],rows))
    rows=[]
    for air,blast in product(('raw','amplified'),('MR','END only')):
        r=select(sensitivity,variant='Air conversion',air_accounting=air,blast_defense=blast)
        rows.append((air,blast,num(avg(r,'blast_Power'),0),num(avg(r,'air')),num(avg(r,'explosions'))))
    add(table(['Blast source pools','Blast defense','Mean released Power','Blast stages','Explosions'],rows))
    add('''A Fire/Hex combination can incapacitate the target before Air reaches its explosion threshold, suppressing observed explosions in that fixture. Concentrated Air teams supply a separate explosion test. An algebraic accounting example illustrates the conversion issue. With raw Air 4S and another raw element 2S, raw-pool expenditure releases 24S Power. Counting the borrowed and doubled pool first releases 48S. Both exceed the ordinary three-stage Overwhelming injury boundary against an equal MR0 defense.

Air-first and Air-second contact orders are both recorded in `synergies.csv`. Water–Air feedback is explicitly finite and re-evaluated from unmodified pools. Mutual eroding-resistance and amplification ordering can still move the exact contact at which a threshold crosses. Snapshot Water with one-pass Air avoids self-justifying Water bands. The explosion uses the pre-clear eroded-MR snapshot, then clears the pools. Independently discharged Shocked retains its own timer in this model. Hex's peak cancellation is checked on the target tick, so an earlier Air explosion can clear its pool first. These timer and same-turn ordering choices require confirmation. The proposed raw-Ice hard-lock threshold and raw-Lightning ≥4× stun threshold reduce support-driven hard locks while preserving Air's substantial lower-band benefits. Each restriction requires explicit approval.

## Mundane, higher-Quality and Sharpness comparison

The physical test set uses Hand axe Slashing, Arming sword Slashing and Mace Blunt. Their approved F values are 1.05 / 1.14 / 1.17, with 0% / 0% / 25% armor bypass. Additive C WR ladders are 23/27/33/38/49, 24/27/31/36/44, and 28/31/36/41/50. The attacker is the physical specialist, the target generalist / END30 / END50, and both approved and additive-C physical equations are evaluated.

The higher-Quality comparator upgrades the weapon's physical construction alone. A constant external gear budget makes that contrast inspectable. Sharpness multiplies final physical Power by `1 + 0.10 × effect tier`. Treating that percentage as attack-rating would square the improvement and represent a different enchantment. Its MP tariff is unapproved, so this comparator evaluates physical performance without assigning an activation price. The primary Mixed elemental and Sharpness weapon bonus is assigned to INT to hold physical attributes fixed. The separately reported optimized Mixed case assigns the full legitimate Mixed bonus to STR.

Integrated results stop on target incapacity and include ceramic armor breakage. A strong mundane blow can erase MR before later elemental hits, especially through pure Nullporcelain AR0. Such results measure combined physical and elemental tactics. The isolated status controls quantify intact-MR resistance. An elemental rider contributes only on surviving legal body contact. The comparison includes tactical outcomes elsewhere in the report rather than converting status into hypothetical wounds.
''')
    rows=[]
    for l,physics in product(LEVELS,('approved','additive C')):
        base=select(mundane,level=l,physics=physics,role='generalist',armor_class='Medium',material='Boughsteel')
        variants=('mundane','recommended','higher quality','Sharpness','approved Fire')
        cells=[num(avg(select(base,variant=v),'total')) if select(base,variant=v) else '—' for v in variants]
        rows.append((l,physics,*cells))
    add(table(['Level','Physical formula','Mundane','Recommended Fire','Weapon Q+1','Sharpness','Approved Fire'],rows))
    add(table(['Paired additive-C check','New stages','Old stages','Difference','95% paired difference interval','Other-seed new-stage range'],
              ((f'L{r["level"]} {r["armor"]}',num(r['new']),num(r['approved']),num(r['delta']),
                f'{num(float(r["delta"])-1.96*float(r["delta_se"]))} to {num(float(r["delta"])+1.96*float(r["delta_se"]))}',
                f'{num(r["other_seed_min"])}–{num(r["other_seed_max"])}') for r in precision)))
    add('''### Full versus Mixed at the same physical Quality

The following generalist-attacker control keeps the same physical weapon Quality and external gear. Mixed's stat bonus is assigned to INT for this controlled comparison. Full loses that bonus and receives the next effect tier and its ordinary MP cost. The VI row uses the explicitly pure elemental blade control, so its physical injury packet differs from ordinary Mixed V.
''')
    full_rows=[]
    for level,material in product(LEVELS,('Boughsteel','Glassweave')):
        full=select(sensitivity,level=level,material=material,variant='Full same-Quality weapon',physics='approved')
        mixed=select(sensitivity,level=level,material=material,variant='legal action mode',attack_mode='Full')
        if full and mixed:
            full_rows.append((level,material,num(avg(mixed,'total')),num(avg(full,'total')),
                              f'{int(float(mixed[0]["activation_cost"]))} / {int(float(full[0]["activation_cost"]))}',
                              f'{int(float(mixed[0]["capacity"]))} / {int(float(full[0]["capacity"]))}'))
    add(table(['Level','Medium armor','Mixed stages','Full stages','Mixed / Full activation MP','Mixed / Full Leywell capacity'],full_rows))
    add('''Both displayed stage columns use the approved physical formula. The Full weapon is also tested under additive C in `sensitivities.csv`. Stat allocation to STR increases Mixed's physical value, as the separate optimized-Mixed weapon matrix records.

No elemental status can improve a hit that never gains a valid contact route. Higher physical Quality, Sharpness, different penetration, a genuine exposed gap or a mundane physical attack can therefore be better against a strong intact MR defense. Their value is separately constrained by armor, hit difficulty and the target's endurance.

## Tier VI and resources

The table uses level-100 geared targets, current QV armor and the default five-round activation. The purely elemental blade control delivers its elemental packet. Other elemental VI weapon manifestations still require an approved design.
''')
    rows=[]
    for role,m,variant in product(('generalist','END50'),('Boughsteel','Glassweave','Nullporcelain'),
                                 ('initial VI','15000 at final MR','recommended VI')):
        r=select(sixth,role=role,material=m,armor_class='Heavy',attackers='Fire',variant=variant)
        if r:
            r=r[0]
            rows.append((role,m,variant,num(r['fire']),pct(r['Fire_main_r5']),pct(r['Fire_peak_r5']),pct(r['tail'])) )
    add(table(['Target','Heavy armor','VI candidate','Fire stages','Burning by round 5','Engulfed by round 5','Post-expiry injury'],rows))
    vi_rows=[]
    for material,cl,role in (('Boughsteel','Medium','generalist'),('Nullporcelain','Heavy','END50')):
        for element in ELEMENTS:
            r=select(sixth,material=material,armor_class=cl,role=role,attackers=element,variant='recommended VI')
            vi_rows.append((f'{role}, {cl} {material}',element,pct(avg(r,'meaningful')),
                            num(avg(r,'total')),num(avg(r,'ice_denied')+avg(r,'lightning_denied')),
                            num(avg(r,'MP')),num(avg(r,'Leywell'))))
    add(table(['VI target','Element','Meaningful','Injury stages','Actions denied','Personal MP drained','Leywell MP drained'],vi_rows))
    vi_ammo=[]
    for material,role in product(('Boughsteel','Glassweave','Nullporcelain'),('generalist','END50')):
        first=select(sixth,material=material,armor_class='Heavy',role=role,attackers='Fire',variant='recommended VI')
        second=select(sixth,material=material,armor_class='Heavy',role=role,attackers='Fire',variant='recommended VI second activation')
        vi_ammo.append((material,role,num(avg(first,'fire')),num(avg(second,'fire')),
                        num(avg(second,'paid_MP')),pct(avg(second,'defender_down'))))
    add(table(['Heavy armor','Target','One VI activation, Fire stages','Up to two activations, Fire stages',
               'Mean stored MP paid for two-use opportunity','Incapacitated with up to two activations'],vi_ammo))
    add(table(['Effect tier','Mixed / Full item Quality','Leywell capacity','Standard activation MP','Powerful activation MP','Full-well Standard / Powerful uses','MP to refill empty well at 90%'],
              ((i+1,f'{i+1 if i<5 else "—"} / {i if i>0 else "—"}',10*(i+1),STANDARD_COST[i],POWERFUL_COST[i],
                f'{10*(i+1)//STANDARD_COST[i]} / {10*(i+1)//POWERFUL_COST[i]}',
                __import__('math').ceil(10*(i+1)/.9)) for i in range(6))))
    add('''All activations last five combat rounds. Passive/modifying activation costs zero combat actions, while each actual attack still spends its legal action cost. Leywell recharge spends personal MP, deposits `floor(0.90 × spent MP)` up to capacity and costs two actions. Equipment bonuses keep their normal constant Soul Strain. Activated elemental effects have zero Soul Strain.

Burning Edge I–V uses the existing Standard bands 2/3/4/5/6 MP in the reference test. The VI Mana Blade uses its approved Powerful 24 MP and a 60-MP well, yielding two activations and 12 MP remaining. Reloading that spent 48 MP requires at least 54 compatible personal MP and the genuine recharge operation. Other elements' proposed VI costs are compared at Standard 8 and Powerful 24. Assuming every VI effect has only two activations would silently assign all of them the Powerful band.

### Counterplay and persistence
''')
    rows=[]
    for policy in ('hold','douse','duel','duel-douse'):
        r=select(sensitivity,variant='counterplay',material='Boughsteel',policy=policy)
        rows.append((policy,num(avg(r,'contact')),num(avg(r,'fire')),num(avg(r,'total')),pct(avg(r,'tail')),
                     num(avg(r,'douse_actions')),num(avg(r,'defender_attacks')),pct(avg(r,'attacker_down'))))
    add(table(['Defender scenario','Contacts','Fire stages','Total stages','Tail fights','Douse actions','Counterattacks','Attacker incapacitated'],rows))
    add('''The hold scenario keeps a target available until incapacitation. The duel scenario gives the defender its legal Full or Quick counterattack and applies attacker wounds. Douse scenarios assume one available suitable mundane douse costing one action. These are scenario assumptions. A universal cleanse-action cost awaits author approval. Ordinary positioning, retreat, real terrain, reach entry and specific spells remain important outside the closed-contact fixture.

## Specific resistance

Hearthiron Fire ×3 resistance enters as `R=3` after the MR/END expression. It multiplies each status threshold, preserving a substantial independent defense. Its old blanket Ice weakness is superseded and is omitted. Pure Trufula's Fire ×4 weakness is modeled as `R=0.25`. Genuine Trufula composites use their separately approved Fire ×2 and qualifying conductive Lightning ×3 vulnerabilities only when the appropriate exposed pathway exists. The generic 1.25× / 1.50× lightning contact bonuses are sensitivity assumptions, not approved metal bonuses.

Applying a resistance multiplier after squaring preserves its stated factor. Multiplying END or MR by the resistance factor before squaring would square that protection. An exposed body location cannot borrow the covered surface's MR. Existing Helm MR and magical shield exceptions retain their separate application rules.

## Exploit and ordering docket

- Repeated eligible contact refreshes a three-turn pool indefinitely while attacks continue. The five-round activation is the attacker's resource window, and the target status has its own expiry.
- Multiple same-element attackers legally add to one pool. Each uses its own legal attack action. Coordinated teams can cross 4× and 12× thresholds far earlier than a solo user.
- PP from Fire, Ice, Hex and Acid can coexist, reaching the existing three-PP shield restriction. Whether every proposed status source is independently meaningful in a given scene remains a real tactical check.
- Lightning refresh can maintain a one-action tax. A 4× stun additionally removes the surviving action and normal dodge. Adding separate interruption losses or permitting stun extension can produce a full lock.
- Air final effects must remain virtual. Writing them into raw storage and re-amplifying each evaluation would create runaway magnitude.
- Water applies its selected MR reduction once to the original applicable rating. Live self-SR can cross bands once by feedback, even with unchanged raw magnitude.
- Hex draining each of eleven wells multiplies total resource loss by equipment count. Ending ongoing effects on every peak tick also needs an explicit new-effect timing rule. Installations and permanent stats survive the end of a five-round activation.
- Ceramic breakage can turn an anti-elemental duel into an MR0 duel. Shattering requires the approved physical impact. Pure Nullporcelain's AR0 is an intentional physical weakness.
- Air's explosion consumes support pools and can prematurely remove a valuable ongoing effect. The transition needs a single ordered resolution and no repeated explosion from the same consumed magnitude.

## Answers to the balance questions

**A. Universal Power.** The initial ladder misses consistent ordinary-tier matchups. The revised shared ladder stabilizes the core Medium-armor reference counts. Complete class/END consistency is mathematically unavailable under a monotone universal equation and the existing overlapping MR ranges.

**B. MR coefficient.** 0.50 is preferred within the explicitly weighted joint search. Re-fitted 0.40 and 0.65 remain defensible alternatives. 0.65 with the initial ladder makes early Glassweave too resistant and middle-tier elemental attacks too effective against MR.

**C. VI.** 15,000 deliberately pushes earlier 4× transitions. 12,200 gives a clear twofold V step while preserving stronger specialist resistance. The 24-MP cost constrains repeat encounters but still buys five rounds of applications. Generic VI cost-band assignment remains open.

**D. Ice.** Frozen and Entombed are realistic mainly through combined attacks, vulnerability and Air. STR² can break a marginal lock and loses effectiveness under low STR or sustained multiple attackers. An amplified Ice hard lock can invalidate that escape route unless raw thresholds or another special rule apply. Duration, allowed magic and external rescue require decisions.

**E. Lightning.** One action removed for three turns is a strong tactical tax, especially against two-action options, while Quick Attack preserves retaliation. Saving for 4× competes with earlier ordinary shocks. Overlapping stun with Shocked and forbidding active stun extension limits lock potential. Recovery and refresh remain important policy choices.

**F. Hex.** Percentage-of-starting-reserve drains scale with actual MP and remain effective against item-heavy targets. Zero-MP injury makes the element useful against exhausted or naturally empty targets. The initial percentages may delay damage through most of a five-round activation. The stronger 10/25/40 candidate trades earlier damage for stronger resource denial.

**G. Water and Acid.** Acid's initial values can move important physical injury boundaries, particularly in coordinated teams. Water is specialized support and has little erosion value against MR0. A stronger Water middle band and snapshot self-SR make that support more predictable. Team scaling is intrinsic and should be acknowledged in encounter design.

**H. Air.** It has a distinct support role and can enable severe conditions from modest raw pools. Finite one-pass virtual amplification and raw-pool expenditure avoid recursive growth. Explosion defense, hard-control thresholds and exact order need approval.

**I. Specific resistance.** The multiplicative placement retains established resistance and vulnerability factors. MR and specific resistance can coexist. Material protections depend on real coverage and delivery. Superseded Hearthiron Ice weakness is excluded.

**J. Overall.** Fire offers direct injury, Ice control and movement denial, Lightning action pressure, Hex resource destruction with a damage fallback, Acid physical teamwork, Water magical teamwork, and Air cross-element amplification. Their counterplay and costs differ. Balance is contingent on the unresolved timing and conversion rules below.

## Material unresolved mechanics

1. Exact target-turn tick, expiry and initiative boundary. The study's attacker-before-defender schedule is explicit. Attacking after the target's turn changes when three turns are counted. A temporary Air/Water downgrade below Burning resets the model's current Burning counter. Whether to preserve earlier Burning rounds through that downgrade remains unresolved. Ordinary matching Fire refresh preserves the counter.
2. Ordinary movement-tile baseline and halving-rounding. The model reports fractional allowance loss.
3. Frozen struggle frequency and whether it consumes the special opportunity, which magic remains legal, external rescue and Entombed expiry.
4. Lightning current-hit versus prior-pool discharge eligibility, failed-discharge pool expenditure, refresh, interruption scheduling and post-stun recovery. Older no-chain-stun wording needs reconciliation with the newer framework.
5. Water's own SR recalculation, Air-before-Water ordering and persistent-versus-temporary MR erosion.
6. Acid temporary-versus-permanent corrosion, material applicability, recovery and rounding.
7. Hex percentage basis, rounding, exact personal/item scope, effect-ending edge, additional peak drain and zero-MP injury timing. The model uses peak drain as the increased drain. An extra instantaneous peak drain remains untested until an amount is chosen. Personal MP is tracked from its starting available reserve. Clipping current MP when wounds lower the END-derived maximum needs explicit accounting rules.
8. Air explosion pool accounting, MR/AR applicability, typed resistance, whether a pure single-pool explosion qualifies, voluntary versus automatic detonation and any splash area.
9. Generic metal Lightning conduction bonus and its actual route. The proposed numeric bonus requires a qualifying conductive route.
10. Full VI manifestation, legal media and whether it replaces a physical blade's ordinary damage. The VI Fire control uses a pure elemental attack.
11. Exact magical shield absorption and excess-power status conversion. Physical shield routing is implemented, while spell-shield numerical absorption remains unresolved.
12. Legal stat-affinity/slot assignment and affordability of a complete gear loadout. The 180-stat peer budget is a faithful controlled benchmark, with explicit strain accounting. The primary MP interpretation counts full eligible equipment END, with an equipment-excluded Hex sensitivity preserved for comparison.

## Reproduction and result files

Use Python 3.10+ with NumPy 2.x. Run `python run_study.py`, followed by `python report.py`, from this directory. The reproduction runs offline. `fixtures.py` records progression, armor, resources and physical profiles. `calibration.py` performs exact contact-chain enumeration and monotone dynamic-programming fitting. `simulate.py` implements the d20 scenarios. `run_study.py` defines every population and sensitivity.

`results/exact_thresholds.csv` contains exact counts and three/five-round probabilities by level, material, armor class and END investment. `MR_*.csv` retain fixed-initial-ladder coefficient/formula tests. `population.csv`, `identities.csv`, `mundane.csv`, `synergies.csv`, `sensitivities.csv` and `tier_VI.csv` retain the seeded scenario summaries. `precision.csv` retains paired uncertainty and independent-seed checks. `unqualified.csv` preserves excluded illegal equipment pairings. `results_manifest.json` stores SHA-256 checksums. Assertions check contact-chain enumeration, bounded injuries and erosion, resource limits, no effect without delivery, inert Static and post-activation Fire persistence.

''')
    batches=('calibration_trials','cross_element_fits','ice_parties','VI_extended','population','identities','mundane','synergies','sensitivities','tier_VI')
    add(table(['Simulation batch','Legal fixtures','Trials per fixture','Scenario-trials'],
              ((name,len(read(name)),params['trials'],f'{len(read(name))*params["trials"]:,}') for name in batches)))
    add('''## Decisions Required From the Author

Each item is a separate proposal requiring approval, rejection or modification.

1. **Joint Power and MR candidate** — The primary pair is **610 / 1,000 / 2,250 / 3,800 / 6,100 / 12,200 with c=0.50**. The close alternative is **490 / 975 / 2,050 / 3,800 / 5,800 / 10,500 with c=0.40**, giving steadier ordinary Glassweave results and removing the opening-tier solo Ice freeze in the reference control, with less Nullporcelain suppression. Choose the pair together. Every element uses that pair's same Power. A separate primary-pair Tier II option of **1,150** keeps Glassweave closer to its old benchmark at the expense of END50 counterplay. VI 15,000 gives faster severe effects against ordinary MR.
2. **Typed SR** — `(effective END + c × applicable MR)² × specific resistance multiplier`, using the coefficient paired with the selected ladder. Accept overlapping Light/Medium/Heavy material matchups. A material name alone cannot impose a stronger outcome than a higher numerical MR from another suit.
3. **Fire** — retain the approved half-SR PP, >1× every-second-round injury, ≥4× two stages per round, three-turn duration and preserved Burning counter. Choose target-turn tick/expiry boundaries.
4. **Ice** — retain current thresholds and one STR² struggle per affected turn. Entombed expires with the three-turn condition unless refreshed or externally resolved. Choose whether the 4× and 12× locks require raw Ice, protecting struggle counterplay from borrowed Air magnitude. Confirm legal magic and movement rounding.
5. **Lightning** — discharge may include the current contact. Shocked removes one action for three turns, with the first Stunned turn overlapping that duration. Ignore attempts to extend an active Stunned condition. Choose Shocked refresh and whether a one-full-turn recovery after Stunned should be added. Count an interrupted action within the stated action loss.
6. **Hex** — test 10% / 25% / 40% of each relevant resource's starting available capacity per turn, separately rounded up. At zero personal MP, use Fire's injury cadence at the corresponding >1× and 4× bands. Define relevant item scope and peak-effect termination. An additional instantaneous drain would require its own specified amount.
7. **Acid** — retain the initial 5% / 15% / 30% temporary AR erosion, based on original applicable AR, floor zero, without per-turn compounding. Permanent corrosion remains a separate decision.
8. **Water** — test 5% / 20% / 35% temporary MR erosion. Determine its own band using pre-self-erosion MR, then apply that erosion to other elements. Keep a finite, documented Air interaction order.
9. **Air** — use virtual `(other raw pool + half raw Air) × 2` at the applicable bands, without creating absent statuses or refreshing their timers. At ≥4× Air SR, expend raw pools once at `4 × sum(raw pools)`, with normal quadratic impact injury and a proposed `END² + applicable MR²` blast defense. Choose whether hard Ice locks and 4× Lightning stun require raw magnitude. The proposed blast affects the target only.
10. **Tier VI cost and form** — keep the 60-MP well, approved Mana Blade 24-MP five-round activation and two full-well uses. Assign Standard 8 versus Powerful 24 separately for other VI effects after their manifestations and legal delivery are specified.
''')
    REPORT.write_text('\n'.join(pieces),encoding='utf-8')
    print(REPORT)


if __name__=='__main__':
    main()
