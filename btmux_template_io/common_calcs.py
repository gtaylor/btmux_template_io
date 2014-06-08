import math

from btmux_template_io.defines import MAX_MECH_INTERNALS


def calc_section_internal(tonnage, section):
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


def calc_run_mp(walk_mp):
    return math.ceil(walk_mp * 1.5)


def calc_run_speed_from_walk_mp(walk_mp):
    run_mp = calc_run_mp(walk_mp)
    return run_mp * 10.75


def calc_jump_speed(jump_mp):
    return jump_mp * 10.75
