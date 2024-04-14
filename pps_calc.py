from pydantic import BaseModel

CONST_MULT = 1.3
ENOCHIAN_MULT = 1.23
GCD = 2.33

caster_tax = .103
af1, af2, af3 = 1.4, 1.6, 1.8


class Skill(BaseModel):
    potency: int
    cast_time: float
    recast_time: float
    is_ability: bool = False


def time_cost(cast_time: float, gcd: float = GCD, caster_tax: float = caster_tax):
    return max(cast_time + caster_tax, gcd)


fire1 = Skill(
    potency=180,
    cast_time=GCD,
    recast_time=GCD,
)


fire3 = Skill(
    potency=260,
    cast_time= 1.4 * GCD,
    recast_time=GCD,
)

fire4 = Skill(
    potency=310,
    cast_time= 1.12 * GCD,
    recast_time=GCD,
)

fire_paradox = Skill(
    potency=500,
    cast_time=GCD,
    recast_time=GCD,
)

despair = Skill(
    potency=340,
    cast_time=1.2 * GCD,
    recast_time=GCD,
)

ice_paradox = Skill(
    potency=500,
    cast_time=0,
    recast_time=GCD,
)

blz3 = Skill(
    potency=260,
    cast_time= 1.4 * GCD,
    recast_time=GCD,
)

blz4 = Skill(
    potency=310,
    cast_time= 1.12 * GCD,
    recast_time=GCD,
)

xeno = Skill(
    potency=880,
    cast_time=0,
    recast_time=GCD,
)

# easier to calc without use enochian and const mul, given all spells will have them
af3_mod = af3
af1_mod = af1

ui_fire_pot_mod = .7
ui_fire_time_mod = 0.5
af_ice_pot_mod = .7
af_ice_time_mod = 0.5


## standard rot pps

# standard af total potency
low_pot_f3_pot = fire3.potency * ui_fire_pot_mod
std_fire_spell_pot = (6 * fire4.potency  + despair.potency) * af3_mod
fire_standard_pot = low_pot_f3_pot + std_fire_spell_pot + fire_paradox.potency + xeno.potency

# standard af total time
fire_standard_time = time_cost(fire3.cast_time * ui_fire_time_mod) + 6 * time_cost(fire4.cast_time)  + time_cost(fire_paradox.cast_time) + time_cost(despair.cast_time) + time_cost(xeno.cast_time)


# standard ui total potency
low_pot_b3_pot = blz3.potency * ui_fire_pot_mod
ice_standard_pot = low_pot_b3_pot + blz4.potency + ice_paradox.potency

# standard ui total time
ice_standard_time = time_cost(blz3.cast_time * af_ice_time_mod) + time_cost(blz4.cast_time) + time_cost(ice_paradox.cast_time)

std_total_pot = fire_standard_pot + ice_standard_pot
std_total_time = fire_standard_time + ice_standard_time

std_rot_pps = (fire_standard_pot + ice_standard_pot) / (fire_standard_time + ice_standard_time)


# double trans
db_trans1_pot = xeno.potency + ice_paradox.potency + af1_mod * fire3.potency + (3 * fire4.potency  + despair.potency) * af3_mod
db_trans1_time = time_cost(xeno.cast_time) + time_cost(ice_paradox.cast_time) + GCD + 3 * time_cost(fire4.cast_time) + time_cost(despair.cast_time)
db_rot_pps = db_trans1_pot / db_trans1_time


# double trans 1f4
db_trans2_pot = xeno.potency + ice_paradox.potency + af1_mod * fire3.potency + (1 * fire4.potency  + despair.potency) * af3_mod
db_trans2_time = time_cost(xeno.cast_time) + time_cost(ice_paradox.cast_time) + GCD + 1 * time_cost(fire4.cast_time) + time_cost(despair.cast_time)
db2_rot_pps = db_trans2_pot / db_trans2_time


db_rot_pps / std_rot_pps
db2_rot_pps / std_rot_pps
