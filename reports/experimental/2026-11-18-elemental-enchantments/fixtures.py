"""Numerical inputs from Mystaria main 930efc89269da5cc266976861fc5215b32c1a0b6."""

from dataclasses import dataclass
from fractions import Fraction
from math import ceil

LEVELS = (10, 25, 50, 75, 100)
APPROVED = (226, 554, 1335, 2456, 3914)
INITIAL = (430, 1350, 3800, 5800, 8100, 15000)
GEAR = (6, 12, 20, 28, 36)
QUALITY = (1, .95, .90, .85, .80)
STRAIN = (1, 2, 4, 6, 8)
STANDARD_COST = (2, 3, 4, 5, 6, 8)
POWERFUL_COST = (4, 5, 7, 10, 12, 24)
HIT = (1, 4, 8, 12, 17, 21)
SPEED = (.20, .80, 1.25, 2.50, 5.)
PENALTIES = (1., .95, .95, .95, .90, .85)
ELEMENTS = ('Fire', 'Ice', 'Lightning', 'Water', 'Air', 'Hex', 'Acid')
CLASSES = ('Light', 'Medium', 'Heavy')
ALLOC = {
    'generalist': (20,20,20,20,20), 'END30': (20,15,30,15,20),
    'END40': (20,15,40,10,15), 'END50': (20,10,50,5,15),
    'physical': (50,10,15,5,20), 'caster': (10,10,20,45,15),
    'zeroMP': (20,20,20,20,20),
}
# STR, DEX, END, INT, SPD. Relevant four Duskpaw bases and END/MP are
# verified separately in the progression sources. INT is not used for spell damage.
DUSKPAW = (13,20,14,17,17)
MOONTOUCHED = (11,17,12,15,20)
BOUGH_AR = ((25,28,30,32,35),(45,52,60,67,75),(75,85,95,105,115))
NULL_MR = ((45,55,65,75,85),(65,75,90,105,120),(90,105,120,140,170))
ZERO = (0,)*5
SHIELD_RATING = ((18,32,53,78,105),(24,43,71,104,140),(31,55,90,135,180))
SHIELD_STR = (10,27,62)
SHIELD_DEX = (12,14,16)


@dataclass(frozen=True)
class Hero:
    stats: tuple
    natural: tuple
    strain: int
    mp: int
    capacity: int


def allocate(level, role):
    exact = [Fraction((level-1)*2*p, 100) for p in ALLOC[role]]
    counts = [int(x) for x in exact]
    # Resolve equally sized remainders in attribute order.
    order = sorted(range(5), key=lambda i: (-(exact[i]-counts[i]), i))
    for i in order[:2*(level-1)-sum(counts)]:
        counts[i] += 1
    return counts


def hero(level, role, q, gear='peer', attack=False, item_mode='Mixed',mp_basis='effective'):
    zero = role == 'zeroMP'
    start = MOONTOUCHED if zero else DUSKPAW
    racial = (1,1,1,1,1.25) if zero else (1,1,1,1.25,1)
    natural = tuple((base+add+level//5)*factor for base,add,factor in
                    zip(start,allocate(level,role),racial))
    bonus = GEAR[q-1] if gear == 'peer' and not zero else 0
    # Five existing bonuses, one per attribute, model the prior peer gear budget.
    # The study weapon is an additional item. Its Mixed bonus is assigned to INT
    # for the controlled weapon contrast; another run assigns it to STR.
    extra = bonus//2 if attack and item_mode in ('Mixed','Mixed-STR') else 0
    index = 0 if item_mode == 'Mixed-STR' else 3
    effective = tuple(stat+bonus+(extra if i == index else 0)
                      for i,stat in enumerate(natural))
    strain = (5+bool(extra))*STRAIN[q-1] if bonus else 0
    capacity = 0 if zero else int(effective[2] if mp_basis=='effective' else natural[2])
    return Hero(effective,natural,strain,max(0,capacity-strain),capacity)


def supports(light, medium, heavy):
    def from_qv(n):
        return tuple(ceil(ceil(n/.8)*m-1e-10) for m in QUALITY[:-1])+(n,)
    return (from_qv(light),from_qv(medium),heavy)


# AR/MR, support, innate SPD reduction, post-shatter backing, Fire SR multiplier.
ARMOR = {
    'Boughsteel': (BOUGH_AR,(ZERO,)*3,supports(8,20,(45,43,41,39,36)),(.04,.11,.20),None,1),
    'Glassweave': (BOUGH_AR,BOUGH_AR,supports(8,19,(44,42,40,38,35)),(.04,.10,.19),(ZERO,)*3,1),
    'Nullporcelain': ((ZERO,)*3,NULL_MR,supports(6,14,(33,32,30,29,26)),(.03,.09,.15),(ZERO,)*3,1),
    'Boughsteel/Glassweave': (
        ((22,25,27,30,32),(42,48,55,62,68),(65,75,85,95,105)),
        ((15,18,22,26,30),(30,38,45,52,60),(45,55,62,70,80)),
        ((13,13,12,12,11),(30,29,27,26,24),(50,48,45,43,40)),(.05,.12,.20),
        ((15,18,20,22,25),(35,40,45,50,55),(65,72,78,84,90)),1),
    'Adamantite/Nullporcelain': (
        ((28,32,36,40,43),(55,65,75,87,100),(95,105,115,130,145)),
        ((35,42,50,58,65),(60,70,85,95,110),(75,90,105,125,145)),
        ((22,21,20,19,18),(53,51,48,46,43),(97,93,88,83,78)),(.07,.19,.28),
        ((25,28,31,35,38),(55,64,72,80,90),(85,95,105,120,135)),1),
    'Hearthiron': (((20,22,25,27,30),(35,40,45,52,60),(60,70,80,90,100)),
                 (ZERO,)*3,supports(12,28,(60,57,54,51,48)),(.07,.15,.25),None,3),
    'Trufula': (((20,22,25,27,30),(35,42,50,57,65),(60,70,80,90,100)),
                (ZERO,)*3,supports(5,11,(24,23,22,21,19)),(.02,.07,.12),None,.25),
}


@dataclass(frozen=True)
class Suit:
    ar: int
    mr: int
    support: int
    burden: float
    backing: int | None
    fire_resist: float


def suit(material, armor_class, q):
    ar,mr,support,burden,backing,fire = ARMOR[material]
    c,i = CLASSES.index(armor_class), q-1
    return Suit(ar[c][i],mr[c][i],support[c][i],burden[c],None if backing is None else backing[c][i],fire)


# Paired physical profiles, approved primary attack F and bypass, and archived
# Round 2 C Weapon Ratings. No quality multiplier is added to additive C.
WEAPONS = {
    'Hand axe': (1.05,0.,(23,27,33,38,49),6,'STR'),
    'Arming sword': (1.14,0.,(24,27,31,36,44),9,'Either'),
    'Mace': (1.17,.25,(28,31,36,41,50),10,'STR'),
}
