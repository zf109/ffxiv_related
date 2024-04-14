import pps_calc as p
from pps_calc import time_cost


def test_time_cost():
    gcd = 2.5
    assert time_cost(2.5, 2.5, 0.103) == 2.603
    assert time_cost(.5, 2.5, 0.103) == 2.5
    assert time_cost(3.5, 2.5, 0.103) == 3.603

    assert time_cost(0, 2.5, 0.103) == 2.5


def test_skill_potency():
    # the test is subject to lastet patch update
    assert p.fire1.potency == 180
    assert p.fire3.potency == 260
    assert p.fire4.potency == 310
    assert p.despair.potency == 340

    assert p.xeno.potency == 880
    