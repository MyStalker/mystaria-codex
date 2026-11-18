"""Run exact screening, joint calibration, seeded simulations and diagnostics."""

import csv
import hashlib
import json
from dataclasses import asdict, replace
from itertools import product
from pathlib import Path

import numpy as np

from fixtures import *
from calibration import COEFFICIENTS, contacts, optimize, screens, threshold_chance
from simulate import Scenario, qualifies, simulate

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT/'results'
SEED = 20261118
TRIALS = 12000
PRECISION_TRIALS = 60000


def write_csv(name, rows):
    rows = list(rows)
    if not rows:
        return
    keys = list(dict.fromkeys(k for row in rows for k in row))
    with (RESULTS/(name+'.csv')).open('w',newline='',encoding='utf-8') as handle:
        out = csv.DictWriter(handle,keys)
        out.writeheader()
        out.writerows(rows)


def scenario_row(s, n=TRIALS):
    data,_ = simulate(s,n,SEED)
    return {**asdict(s),'attackers':'+'.join(s.attackers),**data}


def run_batch(name, scenarios, n=TRIALS):
    rows = []
    skipped = []
    for s in scenarios:
        if qualifies(s):
            rows.append(scenario_row(s,n))
        else:
            skipped.append(asdict(s))
    write_csv(name,rows)
    print(name,len(rows),'rows',len(rows)*n,'paired trials',len(skipped),'unqualified fixtures',flush=True)
    return rows,skipped


def exact_checks(recommended):
    choices = [(tag,coeff,formula,power)
               for tag,powers,coeff,formula in (
                   ('approved',APPROVED,0.,'linear'),
                   ('initial',INITIAL,.65,'linear'),
                   ('recommended',recommended,.5,'linear'))
               for power in [powers]]
    rows = []
    for tag,coeff,formula,powers in choices:
        for i,power in enumerate(powers):
            rows.extend({**row,'candidate':tag} for row in screens(power,coeff,formula,i))
    write_csv('exact_thresholds',rows)
    for formula,coeff in product(('linear','separate_squares'),COEFFICIENTS):
        write_csv('MR_'+formula+'_'+str(coeff),
                  ({**row,'candidate':'initial ladder'} for i,power in enumerate(INITIAL)
                   for row in screens(power,coeff,formula,i)))
    return rows


def population(recommended):
    for i,level in enumerate(LEVELS):
        for role,material,cl in product(ALLOC,ARMOR,CLASSES):
            for tag,ladder,coeff in (('approved',APPROVED,0),('initial',INITIAL,.65),
                                     ('recommended',recommended,.5)):
                yield Scenario(level,i+1,material,cl,role,power=ladder[i],coeff=coeff,
                               variant=tag,path='status-only')


def identities(recommended):
    for i,level in enumerate(LEVELS):
        for role,material,cl,element,contact_mode in product(
            ('generalist','END30','END50','physical','caster','zeroMP'),
            tuple(ARMOR)[:5],CLASSES,ELEMENTS,('status-only','normal')):
            yield Scenario(level,i+1,material,cl,role,attackers=(element,),
                           power=recommended[i],path=contact_mode,
                           wells='caster' if role=='caster' else 'martial')


def mundane(recommended):
    for i,level in enumerate(LEVELS):
        for role,material,cl,weapon,physics in product(
            ('generalist','END30','END50'),tuple(ARMOR)[:5],CLASSES,WEAPONS,
            ('approved','additive C')):
            base = Scenario(level,i+1,material,cl,role,weapon=weapon,physics=physics,
                            attacker_role='physical',power=recommended[i])
            yield replace(base,attackers=('Mundane',),variant='mundane')
            if i<4:
                yield replace(base,attackers=('Mundane',),variant='higher quality')
            yield replace(base,attackers=('Mundane',),variant='Sharpness')
            yield replace(base,variant='approved Fire',power=APPROVED[i],coeff=0)
            yield replace(base,variant='initial',power=INITIAL[i],coeff=.65)
            yield replace(base,variant='recommended')
            yield replace(base,variant='recommended optimized Mixed',mixed='Mixed-STR')


def synergies(recommended):
    for i,level in enumerate(LEVELS):
        for material,role,element in product(tuple(ARMOR)[:5],('generalist','END50'),ELEMENTS):
            base = Scenario(level,i+1,material,'Medium',role,power=recommended[i],path='status-only')
            yield replace(base,attackers=(element,element),variant='same-element pair')
            if element!='Air':
                yield replace(base,attackers=('Air',element),variant='Air first')
                yield replace(base,attackers=(element,'Air'),variant='Air second')
                yield replace(base,attackers=('Water',element),variant='Water pair')
    for i,level in enumerate(LEVELS):
        for material in tuple(ARMOR)[:5]:
            base = Scenario(level,i+1,material,power=recommended[i],path='status-only')
            yield replace(base,attackers=('Fire','Fire','Fire'),variant='triple Fire')
            yield replace(base,attackers=('Air','Fire','Ice'),variant='three-element team')
            yield replace(base,attackers=('Water','Air','Fire'),variant='Water Air Fire')
            yield replace(base,attackers=('Air','Air','Fire'),variant='two Air + Fire')


def sensitivities(recommended):
    for i,level in enumerate(LEVELS):
        for material in ('Boughsteel','Glassweave','Nullporcelain'):
            base = Scenario(level,i+1,material,power=recommended[i],path='status-only')
            for physics in ('approved','additive C'):
                yield replace(base,tier=i+2,quality=i+1,power=recommended[i+1],mixed='Full',
                              path='pure VI' if i==4 else 'normal',physics=physics,
                              variant='Full same-Quality weapon')
            for rates,water in product(('weak','initial','strong','proposed_water'),('snapshot','live')):
                yield replace(base,attackers=('Water','Fire'),rates=rates,water=water,
                              variant='Water erosion')
            for role,rates in product(('caster','generalist','zeroMP'),('weak','initial','strong','proposed_hex')):
                yield replace(base,attackers=('Hex',),role=role,rates=rates,
                              variant='Hex drains',wells='caster' if role=='caster' else 'martial')
            yield replace(base,attackers=('Hex',),wells='eleven',gear='none',variant='Hex eleven Leywells')
            yield replace(base,attackers=('Hex',),wells='mixed',variant='Hex Mixed target')
            yield replace(base,attackers=('Hex',),role='caster',wells='caster',
                          policy='caster',variant='Hex active caster')
            for basis in ('effective','base only'):
                yield replace(base,attackers=('Hex',),role='caster',wells='caster',
                              mp_basis=basis,variant='Hex MP capacity basis')
            if i==1:
                yield replace(base,power=1150,variant='Tier II Glassweave parity alternative')
            for rates in ('weak','initial','strong'):
                yield replace(base,attackers=('Acid',),rates=rates,path='normal',variant='Acid erosion')
            for pattern,overlap,refresh in product(('first','peak'),(False,True),(False,True)):
                yield replace(base,attackers=('Lightning',),lightning=pattern,overlap=overlap,
                              shock_refresh=refresh,variant='Lightning timing')
            for gate in ('including','prior'):
                yield replace(base,attackers=('Lightning',),lightning_gate=gate,
                              variant='Lightning current contact')
            for stun_rule in ('effective','raw'):
                yield replace(base,attackers=('Air','Lightning'),lightning_stun=stun_rule,
                              variant='Air Lightning stun rule')
            for escape,lock,role in product(('none','struggle','magic'),('raw','effective'),('generalist','physical','caster')):
                yield replace(base,attackers=('Air','Ice'),ice_escape=escape,ice_lock=lock,role=role,
                              variant='Ice escape')
            for accounting,blast in product(('raw','amplified'),('MR','END only')):
                yield replace(base,attackers=('Air','Fire','Hex'),air_accounting=accounting,blast_defense=blast,
                              variant='Air conversion')
            for shield in (0,1,2,3):
                yield replace(base,shield=shield,variant='shield contact',path='normal')
            for policy in ('hold','douse','duel','duel-douse'):
                yield replace(base,policy=policy,path='normal',variant='counterplay')
            for mode in ('Full','Quick','Double'):
                yield replace(base,attack_mode=mode,path='normal',variant='legal action mode')
            for covered in (False,True):
                yield replace(base,covered=covered,variant='covered/exposed')
            for delivery in (False,True):
                yield replace(base,delivery=delivery,variant='genuine pathway')
            for gear in ('peer','none'):
                yield replace(base,gear=gear,variant='equipment END')
            for shift in (-1,0,1,2):
                yield replace(base,hit_shift=shift,variant='accuracy sensitivity')
            for conductivity in (1,1.25,1.5):
                yield replace(base,attackers=('Lightning',),conductivity=conductivity,
                              variant='conditional metal bonus')
            for tick in ('end','next'):
                yield replace(base,fire_tick=tick,variant='fire tick timing')


def sixth(recommended):
    for power,coeff,variant in ((15000,.65,'initial VI'),(15000,.5,'15000 at final MR'),
                                 (recommended[5],.5,'recommended VI')):
        for material,cl,role,element in product(tuple(ARMOR)[:5],CLASSES,
                                               ('generalist','END30','END50','caster'),ELEMENTS):
            base = Scenario(100,6,material,cl,role,attackers=(element,),power=power,
                            coeff=coeff,variant=variant,path='pure VI')
            yield base
            if cl=='Medium' and role=='generalist':
                yield replace(base,starts=2,length=10,variant=variant+' second activation')
                yield replace(base,potency='Powerful',variant=variant+' Powerful cost')


def calibration_trials(fits):
    for loss,formula,coeff,powers in fits:
        for i,level in enumerate(LEVELS):
            for material,role in product(('Boughsteel','Glassweave','Nullporcelain'),('generalist','END30','END50')):
                yield Scenario(level,i+1,material,'Medium',role,power=powers[i],
                               coeff=coeff,model=formula,path='status-only',variant='joint fit')


def cross_element_fits(fits):
    for _,formula,coeff,powers in fits:
        if formula!='linear' or coeff not in (.4,.5,.65):
            continue
        for i,level in enumerate(LEVELS):
            for material,role,element in product(
                    ('Boughsteel','Glassweave','Nullporcelain'),('generalist','END50'),ELEMENTS):
                yield Scenario(level,i+1,material,'Medium',role,attackers=(element,),
                               power=powers[i],coeff=coeff,path='status-only',
                               variant='cross-element joint fit')


def ice_parties(recommended):
    for i in range(6):
        level=LEVELS[min(i,4)]
        for role,material,team in product(
                ('generalist','END50'),('Boughsteel','Glassweave','Nullporcelain'),
                (('Ice','Ice','Ice'),('Ice','Ice','Ice','Ice'),('Air','Ice','Ice','Ice'))):
            for lock in (('raw','effective') if 'Air' in team else ('raw',)):
                base=Scenario(level,i+1,material,'Medium',role,attackers=team,
                              power=recommended[i],path='status-only',ice_lock=lock,
                              variant='Ice party concentration',potency='Powerful')
                yield base
                if i==5:
                    yield replace(base,starts=2,length=10,variant='Ice party second activation')


def vi_specialists(recommended):
    for power,coeff,variant in ((15000,.65,'initial VI'),(15000,.5,'15000 at final MR'),
                                 (recommended[5],.5,'recommended VI')):
        for material,cl,role,element in product(tuple(ARMOR)[:5],('Medium','Heavy'),
                                               ('generalist','END50'),ELEMENTS):
            if cl=='Medium' and role=='generalist':
                continue
            yield Scenario(100,6,material,cl,role,attackers=(element,),power=power,
                           coeff=coeff,variant=variant+' second activation',path='pure VI',
                           starts=2,length=10,potency='Powerful')


def precision(recommended):
    rows = []
    for i,level in enumerate(LEVELS):
        for material in ('Boughsteel','Glassweave','Nullporcelain'):
            base = Scenario(level,i+1,material,'Medium',power=recommended[i],
                            attacker_role='physical',physics='additive C',variant='recommended')
            new,new_stages = simulate(base,PRECISION_TRIALS,SEED)
            old,old_stages = simulate(replace(base,variant='approved Fire',power=APPROVED[i],coeff=0),
                                      PRECISION_TRIALS,SEED)
            difference = new_stages-old_stages
            independent = [simulate(base,TRIALS,SEED+k)[0]['total'] for k in (1,2,3)]
            rows.append(dict(level=level,armor=material,n=PRECISION_TRIALS,
                             new=new['total'],approved=old['total'],delta=float(difference.mean()),
                             delta_se=float(difference.std(ddof=1)/np.sqrt(PRECISION_TRIALS)),
                             other_seed_min=min(independent),other_seed_max=max(independent)))
    write_csv('precision',rows)


def invariants(recommended):
    # Exact distribution must agree with brute-force Bernoulli histories.
    from calibration import distribution
    for rounds in (3,5):
        peak_probs = np.zeros(rounds+1)
        for history in product((0,1),repeat=rounds):
            pool=timer=peak=0
            weight=1.
            for hit in history:
                weight *= .65 if hit else .35
                if hit:
                    pool+=1
                    timer=3
                peak=max(peak,pool)
                timer=max(0,timer-1)
                if not timer:
                    pool=0
            peak_probs[:peak+1] += weight
        assert np.allclose(peak_probs,distribution(rounds,.65))
    base = Scenario(50,3,power=recommended[2],path='status-only')
    for blocked in (replace(base,delivery=False), replace(base,attackers=('Air',),delivery=False)):
        data,_ = simulate(blocked,1000,SEED)
        assert data['contact']==data['fire']==data['air']==data['meaningful']==0
    for element in ELEMENTS:
        data,_ = simulate(replace(base,attackers=(element,)),1000,SEED)
        assert 0<=data['total']<=5 and data['contact']<=data['attempts']
        assert data['max_AR_removed']<=data['ar'] and data['max_MR_removed']<=data['mr']
        assert data['MP']<=data['available_mp'] and data['Leywell']<=40
    fire,_ = simulate(base,1000,SEED)
    assert fire['fire']>0 and fire['tail']>0
    lightning,_ = simulate(replace(base,attackers=('Lightning',)),1000,SEED)
    assert lightning['PP_turns']==0
    static,_ = simulate(replace(base,attackers=('Lightning',),power=1),1000,SEED)
    assert static['lightning_denied']==static['shock_procs']==0
    shielded,_ = simulate(replace(base,shield=1,path='normal'),128,SEED)
    assert 0<=shielded['total']<=5 and shielded['shield_contacts']>0
    print('invariants passed',flush=True)


def main():
    RESULTS.mkdir(exist_ok=True)
    first_fits=optimize(vi_minimum=1.35)
    (RESULTS/'calibration_pass1.json').write_text(json.dumps(first_fits,indent=2),encoding='utf-8')
    fits = optimize()
    _,formula,coeff,recommended = fits[0]
    assert (formula,coeff)==('linear',.5)
    (RESULTS/'calibration.json').write_text(json.dumps(fits,indent=2),encoding='utf-8')
    (ROOT/'parameters.json').write_text(json.dumps(dict(
        source_main='930efc89269da5cc266976861fc5215b32c1a0b6',seed=SEED,trials=TRIALS,
        precision_trials=PRECISION_TRIALS,recommended=recommended,coefficient=coeff,
        formula='(effective END + coefficient * applicable MR)^2 * specific resistance',
        numpy=np.__version__,horizon=8,active_rounds=5,VI_horizon=12,
        VI_minimum_step=1.8,attacker_armor='unarmored',
        mp_basis='effective END including equipment minus Soul Strain'),indent=2),encoding='utf-8')
    invariants(recommended)
    exact_checks(recommended)
    skipped = []
    for name,scenarios in (
        ('calibration_trials',calibration_trials(fits)),
        ('cross_element_fits',cross_element_fits(fits)),
        ('ice_parties',ice_parties(recommended)),
        ('VI_extended',vi_specialists(recommended)),
        ('population',population(recommended)),('identities',identities(recommended)),
        ('mundane',mundane(recommended)),('synergies',synergies(recommended)),
        ('sensitivities',sensitivities(recommended)),('tier_VI',sixth(recommended))):
        _,skip=run_batch(name,scenarios)
        skipped.extend(dict(batch=name,**s) for s in skip)
    write_csv('unqualified',skipped)
    precision(recommended)
    manifest = {}
    for file in sorted(RESULTS.glob('*')):
        manifest[file.name]=dict(bytes=file.stat().st_size,sha256=hashlib.sha256(file.read_bytes()).hexdigest())
    (ROOT/'results_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print('recommended',recommended,'coefficient',coeff,flush=True)


if __name__=='__main__':
    main()
