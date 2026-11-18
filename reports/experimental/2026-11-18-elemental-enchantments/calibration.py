"""Exact contact-chain screening and a monotone joint Power/MR fit."""

from functools import cache
from itertools import product
from math import floor, ceil, inf
import numpy as np

from fixtures import APPROVED, INITIAL, LEVELS, ARMOR, CLASSES, hero, suit

COEFFICIENTS = (.40,.50,.65,.75,1.)
EFFECTS = (.5,1,4,12)


def sr(end, mr, coeff, formula='linear', specific=1):
    shaped = (end+coeff*mr)**2 if formula == 'linear' else end**2+(coeff*mr)**2
    return shaped*specific


def contacts(power, resistance, threshold=1, strict=True):
    quotient = threshold*resistance/power
    rounded = round(quotient, 10)
    return max(1, floor(rounded)+1 if strict else ceil(rounded))


@cache
def distribution(rounds, p, attackers=1):
    """Exact distribution of peak live contacts after `rounds`, with 3 target ticks."""
    states = {(0,0,0):1.}
    for _ in range(rounds):
        following = {}
        for outcomes in product((0,1), repeat=attackers):
            n = sum(outcomes)
            weight = p**n*(1-p)**(attackers-n)
            for (pool,timer,peak),prob in states.items():
                total = pool+n
                ttl = 2 if n else max(0,timer-1)
                key = (total if ttl else 0, ttl, max(peak,total))
                following[key] = following.get(key,0)+prob*weight
        states = following
    return tuple(sum(v for (_,_,peak),v in states.items() if peak >= n)
                 for n in range(rounds*attackers+1))


def threshold_chance(n, rounds=5, p=.65, attackers=1):
    probabilities = distribution(rounds,p,attackers)
    return probabilities[n] if n < len(probabilities) else 0.


def screens(power, coeff, formula, i):
    level,quality = LEVELS[min(i,4)],min(i+1,5)
    for role, material, armor_class in product(('generalist','END30','END40','END50'), ARMOR, CLASSES):
        character = hero(level,role,quality)
        armor = suit(material,armor_class,quality)
        if character.stats[0] < armor.support:
            continue
        end = character.stats[2]
        resistance = sr(end,armor.mr,coeff,formula,armor.fire_resist)
        ns = [contacts(power,resistance,b,strict=b==1) for b in EFFECTS]
        result = dict(level=level,tier=i+1,armor=material,armor_class=armor_class,role=role,
                      end=end,mr=armor.mr,resistance=resistance,power=power,coefficient=coeff,formula=formula)
        for threshold,n in zip(('half','main','peak','entomb'),ns):
            result[f'{threshold}_contacts'] = n
            for turns in (3,5):
                for label, p, team in (('peer',.65,1),('guard',.45,1),('pair',.65,2),('hard',.20,1)):
                    result[f'{threshold}_r{turns}_{label}'] = threshold_chance(n,turns,p,team)
        yield result


def score(powers, coefficient, formula, i):
    """Exact probabilities plus a contact-ratio loss to break probability plateaus."""
    q = min(i+1,5)
    level = LEVELS[q-1]
    e = hero(level,'generalist',q).stats[2]
    probabilities = np.array(distribution(5,.65))
    total = np.zeros_like(powers,dtype=float)

    def add(end, material, cls, goal_prob, goal_ratio, weight):
        item = suit(material,cls,q)
        r = sr(end,item.mr,coefficient,formula)
        ratio = r/powers
        chances = probabilities[np.minimum(5,np.floor(ratio+1e-10).astype(int)+1)]
        chances = np.where(ratio>=5-1e-10,0.,chances)
        ratio_penalty = ((ratio-goal_ratio)/max(goal_ratio,1))**2
        total[:] += weight*((chances-goal_prob)**2+.16*ratio_penalty)

    if i < 5:
        baseline_n = contacts(APPROVED[i],e*e)
        baseline = max(0.,threshold_chance(baseline_n)-.10)
        add(e,'Boughsteel','Medium',.88,2.15,3)
        add(e,'Glassweave','Medium',baseline,baseline_n+.05,3)
        add(e,'Nullporcelain','Medium',.06,5.5,2)
        add(e,'Nullporcelain','Heavy',.01,7.1,1.)
        add(hero(level,'END30',q).stats[2],'Boughsteel','Medium',.63,2.9,1.)
        add(hero(level,'END50',q).stats[2],'Boughsteel','Medium',.23,4.3,1.)
    else:
        add(e,'Boughsteel','Medium',.97,1.1,2.)
        add(e,'Glassweave','Medium',.77,2.4,2.)
        add(e,'Nullporcelain','Medium',.32,3.9,2.)
        add(e,'Nullporcelain','Heavy',.10,5.2,2.)
        add(hero(level,'END50',q).stats[2],'Nullporcelain','Heavy',.00,8.,1.)
        peak_n = np.ceil(4*e*e/powers-1e-10).astype(int)
        peak_p = np.where(peak_n<=5,probabilities[np.minimum(peak_n,5)],0.)
        total += 3*(peak_p-.34)**2
    return total


def fit_one(coeff, formula, vi_minimum=1.8):
    grids = [np.arange(lo,hi+1,step) for lo,hi,step in (
        (180,850,10),(450,2000,25),(1100,5000,50),
        (2500,8500,50),(4000,13000,100),(8500,22000,100))]
    previous_grid = np.array([0])
    previous_loss = np.array([0.])
    predecessors = []
    for i,grid in enumerate(grids):
        local = score(grid,coeff,formula,i)
        pointer = []
        for ix,p in enumerate(grid):
            # Explicit design choice for pass two: require an exceptional VI step.
            allowed = previous_grid <= (p/vi_minimum if i==5 else p-1)
            reachable = np.where(allowed,previous_loss,inf)
            best = int(np.argmin(reachable))
            local[ix] += reachable[best]
            pointer.append(best)
        previous_grid,previous_loss = grid,local
        predecessors.append(pointer)
    ix = int(np.argmin(previous_loss))
    total_loss = float(previous_loss[ix])
    powers = []
    for grid,previous in zip(reversed(grids),reversed(predecessors)):
        powers.append(int(grid[ix]))
        ix = previous[ix]
    return tuple(reversed(powers)),total_loss


def optimize(vi_minimum=1.8):
    return sorted((loss,formula,coeff,powers)
                  for formula,coeff in product(('linear','separate_squares'), COEFFICIENTS)
                  for powers,loss in [fit_one(coeff,formula,vi_minimum)])
