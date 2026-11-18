"""Seeded, paired d20 scenario simulation. All unresolved choices are explicit."""

from dataclasses import dataclass
from functools import cache
from math import ceil

import numpy as np

from fixtures import (ELEMENTS, HIT,
                      PENALTIES, POWERFUL_COST, QUALITY, SHIELD_DEX, SHIELD_RATING,
                      SHIELD_STR, SPEED, STANDARD_COST, WEAPONS, hero, suit)

FIRE, ICE, LIGHTNING, WATER, AIR, HEX, ACID = range(7)
HORIZON = 8
MAX_ATTACKS = 4  # up to two legal Double Strikes in a team
COSTS = (STANDARD_COST, POWERFUL_COST)
RATES = {'weak': (.03,.08,.20), 'initial': (.05,.15,.30),
         'strong': (.10,.25,.50), 'proposed_water': (.05,.20,.35),
         'proposed_hex': (.10,.25,.40)}


@dataclass(frozen=True)
class Scenario:
    level: int
    tier: int
    material: str = 'Boughsteel'
    armor_class: str = 'Medium'
    role: str = 'generalist'
    attackers: tuple = ('Fire',)
    attacker_role: str = 'generalist'
    weapon: str = 'Hand axe'
    physics: str = 'approved'
    variant: str = 'best'
    model: str = 'linear'
    coeff: float = .5
    power: int = 0
    rates: str = 'initial'
    water: str = 'snapshot'
    shield: int = 0
    covered: bool = True
    delivery: bool = True
    policy: str = 'hold'
    path: str = 'normal'
    starts: int = 1
    attack_mode: str = 'Full'
    hit_shift: int = 0
    lightning: str = 'first'
    overlap: bool = True
    lightning_gate: str = 'including'
    lightning_stun: str = 'effective'
    shock_refresh: bool = True
    ice_escape: str = 'struggle'
    ice_lock: str = 'raw'
    air_accounting: str = 'raw'
    blast_defense: str = 'MR'
    gear: str = 'peer'
    mixed: str = 'Mixed'
    wells: str = 'martial'
    length: int = 5
    conductivity: float = 1.
    conduct_contact: bool = False
    potency: str = 'Standard'
    fire_tick: str = 'end'
    quality: int = 0
    mp_basis: str = 'effective'


def threshold_band(ratio, inclusive=False):
    return np.where(ratio>=4,3,np.where((ratio>=1) if inclusive else (ratio>1),2,
                                       np.where(ratio>=.5,1,0)))


def stage(power, defense):
    return (power>.75*defense).astype(np.int8)+(power>1.75*defense)+(power>3*defense)


def factor(indices):
    return np.take(PENALTIES,indices)


def governing(stats, weapon):
    return max(stats[0],stats[1]) if WEAPONS[weapon][-1]=='Either' else stats[0]


def physical_power(stat, q, key, physics):
    f,_,wr,_,_ = WEAPONS[key]
    if physics=='additive C':
        return stat**2+wr[q-1]**2
    return (stat*f*(1+.01*(q-1)))**2


def qualifies(s):
    q = s.quality or min(s.tier,5)
    d = hero(s.level,s.role,q,s.gear)
    a = hero(s.level,s.attacker_role,q,s.gear)
    armor = suit(s.material,s.armor_class,q)
    shield = (not s.shield or (
        d.stats[0]>=ceil(SHIELD_STR[s.shield-1]*QUALITY[q-1]) and
        d.stats[1]>=ceil(SHIELD_DEX[s.shield-1]*QUALITY[q-1])))
    return d.stats[0]>=armor.support and shield and governing(a.stats,s.weapon)>=WEAPONS[s.weapon][3]


@cache
def rolls(n, seed):
    rng = np.random.default_rng(seed)
    return (rng.integers(1,21,size=(HORIZON,MAX_ATTACKS,n),dtype=np.int8),
            rng.integers(1,21,size=(HORIZON,n),dtype=np.int8))


def simulate(s, n, seed):
    assert qualifies(s), s
    q = s.quality or min(s.tier,5)
    physical_q = min(q+int(s.variant=='higher quality'),5)
    study_enchanted = any(x in ELEMENTS for x in s.attackers)
    item_mode = ('Full' if s.tier==6 else s.mixed) if study_enchanted or s.variant=='Sharpness' else 'mundane'
    defender = hero(s.level,s.role,q,s.gear,attack=s.wells=='mixed',
                    item_mode='Mixed',mp_basis=s.mp_basis)
    attacker = hero(s.level,s.attacker_role,q,s.gear,True,item_mode,mp_basis=s.mp_basis)
    starting_armor = suit(s.material,s.armor_class,q)
    dstr,ddex,dend,_,dspd = defender.stats
    _,adex,_,_,aspd = attacker.stats
    normal_power = governing(attacker.stats,s.weapon)
    defend_power = governing(defender.stats,'Hand axe')
    shield_def = SHIELD_RATING[s.shield-1][q-1]**2 if s.shield else 1
    p_roll,d_roll = rolls(n,seed)
    horizon = max(HORIZON,s.length+2)
    if horizon>HORIZON:
        extra_rng = np.random.default_rng(seed+100)
        p_roll = np.concatenate((p_roll,extra_rng.integers(
            1,21,size=(horizon-HORIZON,MAX_ATTACKS,n),dtype=np.int8)))
        d_roll = np.concatenate((d_roll,extra_rng.integers(
            1,21,size=(horizon-HORIZON,n),dtype=np.int8)))
    def z(dtype=float):
        return np.zeros(n,dtype=dtype)

    pools = np.zeros((7,n))
    ttl = np.zeros((7,n),dtype=np.int8)
    wound, return_wound, shock, stun, fire_age, hex_age = [z(np.int8) for _ in range(6)]
    armor_damage, shield_damage = z(np.int8), z(np.int8)
    # Full items add no stats or strain and occupy slots beyond the five Blank
    # stat items. The eleven-Full stress case uses no other stat equipment.
    full_capacity = 10*(q+1)
    target_wells = {'none': (0,0), 'martial': (full_capacity,0),
                    'mixed': (10*q,0),
                    'caster': (full_capacity,10*max(2,q-1)),
                    'eleven': (full_capacity,)*11}[s.wells]
    well_max = np.array(target_wells)[:,None]
    well = np.tile(well_max,(1,n))
    personal = np.full(n,defender.mp,dtype=int)
    ongoing = np.full(n, bool(target_wells[0]),dtype=bool)
    doused = z(bool)
    actual = {key:z() for key in (
        'attempts','body','contact','shield_contacts','physical','fire','hex','air','post5',
        'nominal_fire','nominal_hex','nominal_air','PP_turns','ice_denied','lightning_denied',
        'interrupted','slowed_turns','tile_fraction_lost','frozen_turns','entomb_turns','struggles',
        'escapes','magic_escapes','stunned_turns','max_denied_run','denied_run','shock_procs',
        'stun_procs','MP','Leywell','magic_ends','AR_removed','MR_removed','max_AR_removed',
        'max_MR_removed','explosions','blast_Power','amplified_magnitude','activations',
        'paid_MP','douse_actions','defender_attacks','defender_stages','defender_spell_MP',
        'water_cascade','air_severe_assisted','shield_breaks','armor_shatters')}
    prev_hex_peak = z(bool)
    flags3,flags5 = np.zeros((3,7,n),bool),np.zeros((3,7,n),bool)
    flags = np.zeros((3,7,n),bool)
    entombed_ever = z(bool)
    half_ever = z(bool)
    meaningful = z(bool)
    specific = np.ones((7,1))
    specific[FIRE] = starting_armor.fire_resist if s.covered else 1
    if s.path=='Trufula composite':
        specific[FIRE] = .5
        specific[LIGHTNING] = 1/3
    rates = RATES[s.rates]
    active_turns = min(s.starts*5, s.length)
    # A conditional-target setup permits a declared plant, energy, acid or other
    # valid medium on the weapon. Armor visibility never changes the rider value.
    assignments = [(i,ELEMENTS.index(name) if name in ELEMENTS else None)
                   for i,name in enumerate(s.attackers)]
    if s.attack_mode=='Double':
        assignments = [(i,element) for i,element in assignments for _ in (0,1)]
    duel = s.policy in ('duel','duel-douse','caster')
    use_douse = s.policy in ('douse','duel-douse') and s.material!='Trufula'
    standard = 0 if s.potency=='Standard' else 1
    activation_cost = COSTS[1 if s.tier==6 and 'Fire' in s.attackers else standard][s.tier-1]
    cap = s.tier*10

    def armor_values():
        if not s.covered:
            return z(),z()
        if starting_armor.backing is None:
            return np.full(n,starting_armor.ar),np.full(n,starting_armor.mr)
        return (np.where(armor_damage>=2,starting_armor.backing,starting_armor.ar),
                np.where(armor_damage>=2,0,starting_armor.mr))

    def defense(mr):
        end = dend*factor(wound)
        base = (end+s.coeff*mr)**2 if s.model=='linear' else end**2+(s.coeff*mr)**2
        return base*specific

    def rate(band):
        return np.take((0.,*rates),band)

    def state():
        ar,mr = armor_values()
        unmod = defense(mr)
        air_ratio = pools[AIR]/unmod[AIR]
        wet = z()
        for _ in range(4 if s.water=='live' else 1):
            current = defense(mr*(1-wet)) if s.water=='live' else unmod
            air_ratio = pools[AIR]/current[AIR] if s.water=='live' else air_ratio
            boost = np.where(air_ratio>=.5,.5*pools[AIR],0.)
            doubled = np.where(air_ratio>1,2.,1.)
            effective = np.where(pools>0,(pools+boost)*doubled,0.)
            effective[AIR] = pools[AIR]
            w = threshold_band(effective[WATER]/current[WATER])
            wet = rate(w)
        water_effective = effective[WATER].copy()
        water_resistance = current[WATER].copy()
        mr_after = mr*(1-wet)
        resistance = defense(mr_after)
        # Snapshot Water at un-eroded MR, including Air's one-pass bonus.
        resistance[WATER] = water_resistance
        air_ratio = pools[AIR]/resistance[AIR]
        boost = np.where(air_ratio>=.5,.5*pools[AIR],0.)
        doubled = np.where(air_ratio>1,2.,1.)
        effective = np.where(pools>0,(pools+boost)*doubled,0.)
        effective[AIR] = pools[AIR]
        effective[WATER] = water_effective
        ratio = effective/resistance
        raw = pools/resistance
        acid_pct = rate(threshold_band(ratio[ACID]))
        return ratio,raw,effective,ar,mr,mr_after,acid_pct,wet,resistance

    def record(current, eligible):
        nonlocal half_ever, meaningful, entombed_ever
        r,raw,effective,ar,mr,mr_after,corrosion,wet,resistance = current
        active = eligible & (wound<5)
        cut = (r>1)
        cut[[ICE,LIGHTNING]] = r[[ICE,LIGHTNING]]>=1
        flags[0] |= (r>=.5)&active
        flags[1] |= cut&active
        flags[2] |= (r>=4)&active
        half_ever |= np.any((r[[FIRE,ICE,HEX,ACID]]>=.5),axis=0)&active
        ice_ratio = raw[ICE] if s.ice_lock=='raw' else r[ICE]
        entombed_ever |= (ice_ratio>=12)&active
        actual['max_AR_removed'] = np.maximum(actual['max_AR_removed'],ar*corrosion*active)
        actual['max_MR_removed'] = np.maximum(actual['max_MR_removed'],(mr-mr_after)*active)

    def injure(amount, channel, t):
        nonlocal wound
        planned = np.where(wound<5,amount,0).astype(np.int8)
        inflicted = np.minimum(5-wound,planned)
        if channel!='physical':
            actual['nominal_'+channel] += planned
        actual[channel] += inflicted
        if t>=5:
            actual['post5'] += inflicted
        wound += inflicted

    for t in range(horizon):
        before = wound < 5
        if t<active_turns and t%5==0:
            for index,element in assignments:
                if element is not None and (t//5+1)*activation_cost<=cap:
                    paying = before & ((return_wound<5) if index==0 else True)
                    actual['activations'] += paying
                    actual['paid_MP'] += activation_cost*paying
        for slot,(index,element) in enumerate(assignments):
            if t>=s.length:
                break
            alive = (wound<5)&((return_wound<5) if index==0 else True)
            dpen = factor(wound)
            apen = factor(return_wound) if index==0 else np.ones(n)
            current = state()
            r,raw,effective,ar,mr,mr_after,acid_pct,wet,_ = current
            pp = np.sum(r[[FIRE,ICE,HEX,ACID]]>=.5,axis=0)
            chilled = r[ICE]>=1
            d_speed = (dspd*np.where(chilled,.85,1.)+ddex/4)*(1-starting_armor.burden)*dpen
            a_speed = (aspd+adex/4)*apen
            base = np.searchsorted(SPEED,d_speed/a_speed,side='right')
            base = np.where(stun>0,0,base)
            base = np.clip(base-np.where(pp>=3,2,pp>0)+s.hit_shift+int(s.attack_mode=='Quick'),0,5)
            guard = (shield_damage<3)&(pp<3)
            shield_shift = 0 if s.shield==0 else (2 if s.shield==3 else 1)
            shielded = np.clip(base+guard*shield_shift,0,5)
            die = p_roll[t,slot]
            body = (die>=np.take(HIT,shielded))&alive
            intercepted = (die>=np.take(HIT,base))&~body&alive
            actual['attempts'] += alive
            actual['body'] += body
            actual['shield_contacts'] += intercepted
            power = physical_power(normal_power*apen,physical_q,s.weapon,s.physics)
            if s.attack_mode=='Double':
                power *= .60
            if s.variant=='Sharpness':
                power *= 1+.10*s.tier
            is_magical_blade = s.path in ('pure VI','status-only')
            power = np.where(is_magical_blade,0.,power)
            shield_loss = np.where(intercepted,np.minimum(3,np.floor(power/shield_def)),0).astype(np.int8)
            broken = intercepted & (shield_damage+shield_loss>=3)
            remaining_shield_capacity = (3-shield_damage).astype(float)*shield_def
            overflow = np.where(broken,np.maximum(0,power-remaining_shield_capacity),0.)
            shield_damage[:] = np.minimum(3,shield_damage+shield_loss)
            actual['shield_breaks'] += broken
            bypass = WEAPONS[s.weapon][1]
            defense_power = (dend*dpen)**2+(ar*(1-acid_pct)*(1-bypass))**2
            hit_stages = stage(np.where(body,power,overflow),defense_power)
            if starting_armor.backing is not None and s.covered:
                prior = armor_damage.copy()
                armor_damage[:] = np.minimum(2,armor_damage+np.minimum(2,hit_stages))
                actual['armor_shatters'] += (armor_damage==2)&(prior<2)
            injure(hit_stages,'physical',t)
            if element is None or t>=active_turns or (t//5+1)*activation_cost>cap:
                continue
            arrival = body.copy()
            if s.conduct_contact and element==LIGHTNING:
                arrival |= broken & (overflow>0)
            if not s.delivery:
                arrival[:] = False
            arrival &= wound<5
            actual['contact'] += arrival
            before_power = pools[element].copy()
            pools[element] += np.where(arrival,s.power*(s.conductivity if element==LIGHTNING else 1.),0.)
            ttl[element] = np.where(arrival,3,ttl[element])
            current = state()
            record(current,arrival)
            r,raw,effective,ar,mr,mr_after,acid_pct,wet,resistance = current
            actual['air_severe_assisted'] += (np.any((r>=4)&(raw<4),axis=0)&arrival)
            if s.water=='live':
                self_only = threshold_band(effective[WATER]/defense(mr)[WATER])
                actual['water_cascade'] += (threshold_band(r[WATER])>self_only)&arrival
            if element==LIGHTNING:
                choose = (r[LIGHTNING]>=(4 if s.lightning=='peak' and t<4 else 1))&arrival
                if s.lightning_gate=='prior':
                    choose &= ((before_power/resistance[LIGHTNING])>=1)
                stun_ratio = raw[LIGHTNING] if s.lightning_stun=='raw' else r[LIGHTNING]
                qualifies_stun = choose&(stun_ratio>=4)&(stun==0)
                may_shock = choose&((shock==0)|s.shock_refresh)
                actual['shock_procs'] += may_shock
                actual['stun_procs'] += qualifies_stun
                if s.policy=='interruption':
                    # Dedicated prepared-action fixture: one action is in progress
                    # on this defender turn. The lost action is included in denial.
                    actual['interrupted'] += may_shock&(shock==0)
                shock = np.where(may_shock,np.maximum(shock,3),shock)
                stun = np.where(qualifies_stun,1,stun)
                pools[LIGHTNING,choose] = 0
                ttl[LIGHTNING,choose] = 0
            if element==AIR or np.any(r[AIR]>=4):
                detonate = (r[AIR]>=4)&arrival
                payload = pools if s.air_accounting=='raw' else effective
                blast = 4*np.sum(payload,axis=0)
                actual['explosions'] += detonate
                actual['blast_Power'] += blast*detonate
                conversion = mr_after**2 if s.blast_defense=='MR' else 0.
                injure(np.where(detonate,stage(blast,(dend*factor(wound))**2+conversion),0),'air',t)
                pools[:,detonate] = 0
                ttl[:,detonate] = 0
                fire_age[detonate] = 0
                hex_age[detonate] = 0
        r,raw,effective,ar,mr,mr_after,acid_pct,wet,resistance = state()
        live = wound<5
        record((r,raw,effective,ar,mr,mr_after,acid_pct,wet,resistance),live)
        ice_lock = raw[ICE] if s.ice_lock=='raw' else r[ICE]
        frozen = (ice_lock>=4)&live
        entombed = (ice_lock>=12)&live
        slow = (r[ICE]>=1)&live
        stun_turn = (stun>0)&live
        shock_turn = (shock>0)&live
        blocked_by_ice = frozen&~stun_turn
        actions = np.where(frozen|stun_turn,0,np.where(shock_turn,1,2))
        actual['lightning_denied'] += (2*stun_turn+(shock_turn&~stun_turn))*live
        actual['ice_denied'] += np.where(blocked_by_ice,2-(shock_turn.astype(int)),0)
        actual['stunned_turns'] += stun_turn
        actual['frozen_turns'] += frozen
        actual['entomb_turns'] += entombed
        actual['slowed_turns'] += slow
        actual['tile_fraction_lost'] += np.where(frozen|stun_turn,1.,np.where(slow,.5,0.))*live
        actual['denied_run'] = np.where(live&(actions<2),actual['denied_run']+1,0.)
        actual['max_denied_run'] = np.maximum(actual['max_denied_run'],actual['denied_run'])
        actual['PP_turns'] += np.sum(r[[FIRE,ICE,HEX,ACID]]>=.5,axis=0)*live
        actual['AR_removed'] += ar*acid_pct*live
        actual['MR_removed'] += (mr-mr_after)*live
        actual['amplified_magnitude'] += np.sum(np.maximum(effective-pools,0.),axis=0)*live
        can_escape = frozen&~entombed&~stun_turn
        if s.ice_escape=='magic':
            uses_magic = can_escape&(personal>=6)&(s.role=='caster')
            personal -= 6*uses_magic
            actual['defender_spell_MP'] += 6*uses_magic
            actual['magic_escapes'] += uses_magic
            pools[ICE,uses_magic] = 0
            ttl[ICE,uses_magic] = 0
            can_escape &= ~uses_magic
        if s.ice_escape!='none':
            pools[ICE] = np.maximum(0,pools[ICE]-(dstr*factor(wound))**2*can_escape)
            actual['struggles'] += can_escape
            r_after,raw_after,*_ = state()
            actual['escapes'] += can_escape & ((raw_after[ICE] if s.ice_lock=='raw' else r_after[ICE])<4)
        burning = (r[FIRE]>1)&live
        if use_douse:
            extinguish = burning&~doused&(actions>=1)
            actual['douse_actions'] += extinguish
            doused |= extinguish
            actions -= extinguish
            pools[FIRE,extinguish] = 0
            ttl[FIRE,extinguish] = 0
            burning &= ~extinguish
        fire_age = np.where(burning,fire_age+1,0)
        eligible_fire = burning & ((s.fire_tick=='end')|(fire_age>1))
        fire_stages = np.where((r[FIRE]>=4)&eligible_fire,2,eligible_fire&(fire_age%2==0))
        injure(fire_stages,'fire',t)
        live = wound<5
        hex_band = threshold_band(r[HEX])*live
        drain_frac = rate(hex_band)
        personal_drain = np.minimum(personal,np.ceil(drain_frac*defender.mp-1e-11).astype(int))
        well_drain = np.minimum(well,np.ceil(drain_frac*well_max-1e-11).astype(int))
        personal -= personal_drain
        well -= well_drain
        actual['MP'] += personal_drain
        actual['Leywell'] += well_drain.sum(axis=0)
        hex_peak = (hex_band==3)
        ended = hex_peak&~prev_hex_peak&ongoing
        ongoing &= ~ended
        actual['magic_ends'] += ended
        prev_hex_peak = hex_peak
        hex_damage = (personal==0)&(hex_band>=2)
        hex_age = np.where(hex_damage,hex_age+1,0)
        injure(np.where(hex_damage&hex_peak,2,hex_damage&(hex_age%2==0)),'hex',t)
        # A Quick counterattack remains legal with one action. In the caster
        # fixture it represents a weapon action, with a separate legal mana use
        # only on turns where a second action is available.
        if duel:
            d_live = (wound<5)&(return_wound<5)
            can_counter = d_live&(actions>=1)
            d_bleed = factor(wound)
            a_bleed = factor(return_wound)
            a_body_speed = (aspd+adex/4)*a_bleed
            d_off_speed = (dspd*np.where(slow,.85,1.)+ddex/4)*d_bleed*(1-starting_armor.burden)
            counter_category = np.searchsorted(SPEED,a_body_speed/d_off_speed,side='right')
            quick_counter = (actions==1)|(s.policy=='caster')
            counter_category = np.clip(counter_category+quick_counter-int(s.attack_mode=='Double'),0,5)
            counter_hit = can_counter & (d_roll[t]>=np.take(HIT,counter_category))
            counter_power = physical_power(defend_power*d_bleed,q,'Hand axe',s.physics)
            a_end = attacker.stats[2]*a_bleed
            counter_stages = stage(np.where(counter_hit,counter_power,0.),a_end**2)
            counter_stages = np.minimum(5-return_wound,counter_stages)
            return_wound += counter_stages
            actual['defender_stages'] += counter_stages
            actual['defender_attacks'] += can_counter
            if s.policy=='caster':
                uses = d_live&(actions==2)&(personal>=3)
                personal -= 3*uses
                actual['defender_spell_MP'] += 3*uses
        meaningful |= (half_ever|(actual['MP']>0)|(actual['Leywell']>0)|
                       (actual['max_AR_removed']>0)|(actual['max_MR_removed']>0)|
                       (actual['lightning_denied']>0)|(actual['amplified_magnitude']>0)|
                       (actual['explosions']>0)|(actual['slowed_turns']>0))
        ttl[:] = np.maximum(0,ttl-1)
        pools[ttl==0] = 0
        fire_age[ttl[FIRE]==0] = 0
        hex_age[ttl[HEX]==0] = 0
        shock = np.maximum(0,shock-(s.overlap|(stun==0)))
        stun = np.maximum(0,stun-1)
        if t==2:
            flags3 = flags.copy()
        if t==4:
            flags5 = flags.copy()

    actual.pop('denied_run')
    actual.update(total=wound, defender_down=wound>=5, attacker_down=return_wound>=5,
                  fire_wound=actual['fire']>0, meaningful=meaningful,
                  freeze=actual['frozen_turns']>0, entomb=entombed_ever,
                  shocked=actual['shock_procs']>0, stunned=actual['stun_procs']>0,
                  drained_out=(personal==0)&(defender.mp>0),
                  tail=actual['post5']>0, shield_shattered=shield_damage>=3,
                  armor_shattered=armor_damage>=2, denied_four=actual['max_denied_run']>=4)
    for tag,frame in [('3',flags3),('5',flags5)]:
        for e in set(element for _,element in assignments if element is not None):
            for x,b in zip(('half','main','peak'),frame):
                actual[f'{ELEMENTS[e]}_{x}_r{tag}'] = b[e]
    for snapshot_key in ['Fire_half','Fire_main','Fire_peak']:
        # Keep table columns stable for unequipped benchmark rows.
        actual.setdefault(snapshot_key+'_r3',z())
        actual.setdefault(snapshot_key+'_r5',z())
    for key, array in list(actual.items()):
        if key in ('total','fire_wound','meaningful','freeze','entomb','shocked','stunned','tail',
                   'defender_down'):
            actual[key+'_se'] = array.astype(float).std(ddof=1)/np.sqrt(n)
    data = {k:float(np.mean(v)) for k,v in actual.items()}
    data.update(n=n,seed=seed,end=dend,str=dstr,available_mp=defender.mp,
                natural_mp=defender.capacity,
                soul_strain=defender.strain,ar=starting_armor.ar if s.covered else 0,
                mr=starting_armor.mr if s.covered else 0,armor_strength=starting_armor.support,
                activation_cost=activation_cost if study_enchanted else 0,
                capacity=cap if study_enchanted else 0)
    return data, wound
