from btmux_template_io.common_calcs import calc_walk_mp_from_engine_rating, \
    calc_run_speed_from_walk_mp
from btmux_template_io.parsers.ssw.populators.common import add_basic_crit


def populate_movement_and_engine(xml_root, unit_obj):
    """
    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    engine_e = xml_root.xpath('engine')[0]
    left_start = int(engine_e.get('lsstart', 0)) + 1
    right_start = int(engine_e.get('rsstart', 0)) + 1

    engine_type = engine_e.text
    if 'XXL' in engine_type:
        unit_obj.specials.add('XXL_Tech')
        torso_crits = 6
        _add_torso_crits('left_torso', left_start, torso_crits, unit_obj)
        _add_torso_crits('right_torso', right_start, torso_crits, unit_obj)
    elif 'XL' in engine_type:
        unit_obj.specials.add('XLEngine_Tech')
        torso_crits = 3
        _add_torso_crits('left_torso', left_start, torso_crits, unit_obj)
        _add_torso_crits('right_torso', right_start, torso_crits, unit_obj)
    elif 'Light Engine' in engine_type:
        unit_obj.specials.add('LightEngine_Tech')
        torso_crits = 2
        _add_torso_crits('left_torso', left_start, torso_crits, unit_obj)
        _add_torso_crits('right_torso', right_start, torso_crits, unit_obj)
    elif 'Compact Engine' in engine_type:
        unit_obj.specials.add('CompactEngine_Tech')
    elif 'Fusion' in engine_type:
        pass
    elif 'I.C.E.' in engine_type:
        unit_obj.specials.add('ICEEngine_Tech')
    else:
        raise ValueError("Unknown engine type: %s" % engine_type)

    _add_standard_ct_crits(unit_obj)

    engine_rating = int(xml_root.xpath('engine')[0].get('rating'))
    walk_mp = calc_walk_mp_from_engine_rating(engine_rating, unit_obj.weight)
    max_speed = calc_run_speed_from_walk_mp(walk_mp)
    unit_obj.max_speed = max_speed


def _add_standard_ct_crits(unit_obj):
    """
    First three CT crits are always engines.
    """

    # All engines have a first group of three crits.
    for crit in range(1, 4):
        _add_engine('center_torso', crit, unit_obj)

    if 'CompactEngine_Tech' in unit_obj.specials:
        # Compact engines are only three crits.
        return

    # Figure out where the second group of engine crits start.
    if 'CompactGyro_Tech' in unit_obj.specials:
        start_crit = 6
    elif 'Extra-Light' in unit_obj.specials:
        start_crit = 10
    else:
        start_crit = 8

    for crit in range(start_crit, start_crit + 3):
        _add_engine('center_torso', crit, unit_obj)


def _add_torso_crits(btmux_section, start_crit, num_crits, unit_obj):
    for crit in range(start_crit, start_crit + num_crits):
        _add_engine(btmux_section, crit, unit_obj)


def _add_engine(btmux_section, crit, unit_obj):
    add_basic_crit(btmux_section, crit, 'Engine', unit_obj)
