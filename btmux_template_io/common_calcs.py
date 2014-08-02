import math

from . defines import MAX_MECH_INTERNALS, WEAPON_SR_RANGE_MOD, \
    WEAPON_MR_RANGE_MOD, WEAPON_LR_RANGE_MOD
from . item_table import WEAPON_TABLE


def calc_section_internal(tonnage, section):
    """
    Given a unit tonnage and a section, calculate the number of internals
    it has.

    .. todo: Make this play nicely with other unit types aside from mechs.

    :param int tonnage: The unit's tonnage.
    :param str section: ONe of the sections on the unit.
    :rtype: int
    :returns: The number of internals on the section.
    """

    section = section.lower()
    if section.endswith('arm'):
        chart_section = 'arm'
    elif section.endswith('leg'):
        chart_section = 'leg'
    elif section.startswith('center'):
        chart_section = 'center_torso'
    elif section.endswith('torso'):
        chart_section = 'side_torso'
    elif section == 'head':
        # Heads always have 3 ints.
        return 3

    # noinspection PyUnboundLocalVariable
    return MAX_MECH_INTERNALS[int(tonnage)][chart_section]


def calc_walk_mp_from_engine_rating(engine_rating, unit_tonnage):
    """
    :param int engine_rating: The engine rating.
    :rtype: int
    :return: The walk MP.
    """

    return engine_rating / unit_tonnage


def calc_run_mp(walk_mp):
    """
    :param int walk_mp: The unit's walk MP.
    :rtype: int
    :returns: The unit's run MP.
    """

    return math.ceil(walk_mp * 1.5)


def calc_run_speed_from_walk_mp(walk_mp):
    """
    :param int walk_mp: The unit's walk MP.
    :rtype: float
    :returns: Max speed (in kph).
    """

    run_mp = calc_run_mp(walk_mp)
    return run_mp * 10.75


def calc_jump_speed(jump_mp):
    """
    :param int jump_mp: The unit's jump MP.
    :returns: The unit's jump speed (in kph).
    """

    return jump_mp * 10.75


def get_weapon_max_damage_output(weapon_name):
    """
    :param str weapon_name: The weapon whose max damage output to look up.
    :rtype: int
    :returns: The maximum theoretical damage output for a weapon. This is
        straightforward for all but missiles, since we have to figure out
        how many missiles are being fired.
    """

    weap_dat = WEAPON_TABLE[weapon_name]
    if weap_dat['weapon_type'] != 'Missile':
        return weap_dat['damage']

    name_split = weapon_name.split('-')
    try:
        missile_count = int(name_split[-1])
    except ValueError:
        missile_count = 1

    return weap_dat['damage'] * missile_count


def get_weapon_damage_mod_at_range(weapon_name, shot_range):
    """
    Given a weapon name and a range, return an approximate damage modifier
    percentage based on the added BTH difficulty.

    :param str weapon_name: The name of the weapon.
    :param int shot_range: Range (in hexes) for a theoretical shot.
    :rtype: float
    :returns: A float 0...1 to modify the max damage by.
    """

    weap_dat = WEAPON_TABLE[weapon_name]
    if shot_range <= weap_dat['min_range']:
        min_range = weap_dat['min_range']
        added_bth = min_range - shot_range + 1
        return (12 - added_bth) / 12.0
    elif shot_range <= weap_dat['short_range']:
        return WEAPON_SR_RANGE_MOD
    elif shot_range <= weap_dat['medium_range']:
        return WEAPON_MR_RANGE_MOD
    elif shot_range <= weap_dat['long_range']:
        return WEAPON_LR_RANGE_MOD
    else:
        return 0.0


def get_damage_chart(unit):
    """
    .. note:: This won't give you a great estimation of actual damage
        output, it's only meant to help you find the ratio of output to
        max output at each range.

    :param BTMuxUnit unit: The unit whose range chart to calculate.
    :rtype: list
    :returns: A list of approximate damage output at various ranges. The range
        matches the index of the number in the list. For example, item 1
        is approximate damage output at range 1.
    """

    range_chart = {}
    weapons_payload = unit.weapons_payload.items()

    for name, dat in weapons_payload:
        range_chart[name] = []
        max_damage = get_weapon_max_damage_output(name)
        for distance in range(0, 35):
            range_mod = get_weapon_damage_mod_at_range(name, distance)
            modded_damage = max_damage * range_mod
            range_chart[name].append(modded_damage)

    range_total = []
    for distance in range(0, 35):
        distance_total = 0
        for name, _ in weapons_payload:
            distance_total += range_chart[name][distance]
        range_total.append(distance_total)
    return range_total
