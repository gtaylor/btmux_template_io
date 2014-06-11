"""
MegaMek MTF parser.
"""

from btmux_template_io.item_table import ITEM_TABLE
from btmux_template_io.parsers.mtf.armor_mapping import BIPED_ARMOR_MAP, \
    QUAD_ARMOR_MAP, REAR_ARMOR_MAP
from btmux_template_io.unit import BTMuxUnit
from btmux_template_io.common_calcs import calc_section_internal, \
    calc_run_speed_from_walk_mp, calc_jump_speed

from btmux_template_io.parsers.mtf.crit_mapping import CRIT_MAP
from btmux_template_io.parsers.mtf.section_mapping import SECTION_MAP


def parse_from_string(template_contents):
    """
    Given the full contents of a properly formed MTF file, parse it
    and return an object with the template's values set as attributes.

    :param str template_contents: The full contents of a valid template.
    :rtype: btmux_template_io.unit.BTMuxUnit
    :return: A BTMuxUnit instance with the template's values set in attributes.
    """

    unit_obj = BTMuxUnit()
    lines = [line.strip() for line in template_contents.split('\n')]

    unit_obj.name = lines[1]
    unit_obj.reference = lines[2]
    value_dict = _get_value_dict(lines)

    _set_headers(value_dict, unit_obj)
    _set_armor(value_dict, unit_obj)
    _find_and_set_section_contents(lines, unit_obj)
    _add_specials(value_dict, unit_obj)

    return unit_obj


def parse_from_file(template_path):
    """
    Given a properly formed MTF file, parse it and return an object with
    the template's values set as attributes.

    :param str template_path: Full path to a properly formed BTMux template.
    :rtype: btmux_template_io.unit.BTMuxUnit
    :return: A BTMuxUnit instance with the template's values set in attributes.
    """

    fobj = open(template_path, 'r')
    return parse_from_string(fobj.read())


def _get_value_dict(template_lines):
    """
    Many of the lines in an MTF file are key/value in the form of::

        Heat Sinks:20 Single

    This function returns a dict of all of these key/val lines. Note that
    the section crit contents aren't included in this, since they aren't
    in key/val form.

    :param list template_lines: The template contents split into lines.
    :rtype: dict
    :returns: A dict of header values.
    """

    value_dict = dict()
    for line in template_lines:
        try:
            key, val = line.split(':')
        except ValueError:
            continue
        value_dict[key] = val
    return value_dict


def _set_headers(value_dict, unit_obj):
    """
    Looks through the key/value pairs and fills out what we can. These
    tend to be the stuff in a BTMux template file's header section.

    :param dict value_dict: Dict containing all key/val pairs.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    walk_mp = float(value_dict['Walk MP'])
    max_speed = calc_run_speed_from_walk_mp(walk_mp)
    jump_mp = float(value_dict['Jump MP'])
    jump_speed = calc_jump_speed(jump_mp)

    move_type = value_dict['Config']
    if move_type.lower() == 'biped omnimech':
        move_type = 'Biped'
    if move_type not in ['Biped', 'Quad']:
        raise ValueError('Unknown move type: %s' % move_type)

    unit_obj.unit_type = 'Mech'
    unit_obj.unit_move_type = move_type
    unit_obj.unit_tro = value_dict.get('Era')
    unit_obj.unit_era = value_dict.get('Source')
    unit_obj.weight = value_dict['Mass']
    unit_obj.max_speed = max_speed
    unit_obj.jump_speed = jump_speed

    hs_total, hs_type = value_dict['Heat Sinks'].split()
    hs_total = int(hs_total)
    if hs_type == 'Double':
        hs_total *= 2
    unit_obj.heatsink_total = hs_total


def _set_armor(value_dict, unit_obj):
    """
    Look through the section armor key/vals and get the values transferred
    over to the unit object.

    :param dict value_dict: Dict containing all key/val pairs.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    if unit_obj.unit_move_type == 'Biped':
        armor_map = BIPED_ARMOR_MAP
    else:
        armor_map = QUAD_ARMOR_MAP

    for mft_loc, btmux_loc in armor_map:
        unit_obj.sections[btmux_loc] = {
            'armor': int(value_dict[mft_loc]),
            # Internals aren't included in MTF files since they can be
            # calculated.
            'internals': calc_section_internal(unit_obj.weight, btmux_loc)
        }

    for mft_loc, btmux_loc in REAR_ARMOR_MAP:
        unit_obj.sections[btmux_loc]['rear'] = int(value_dict[mft_loc])


def _find_and_set_section_contents(template_lines, unit_obj):
    """
    Figure out which lines are sections. Hand the transfer of crits off to
    another function.

    :param list template_lines: The template contents split into lines.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    for line_num, line in enumerate(template_lines):
        if line.endswith('Leg:') or line.endswith('Arm:') or \
                line.endswith('Head:') or line.endswith('Torso:'):
            _set_section_contents(line_num, template_lines, unit_obj)


def _set_section_contents(section_start_line_num, template_lines, unit_obj):
    """
    Look through the section contents and transfer them over.

    :param int section_start_line_num: The line number that the section
        starts on.
    :param list template_lines: The template contents split into lines.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    section_name, _ = template_lines[section_start_line_num].split(':')
    # Convert the MTF section name to BTMux equivalent.
    btmux_section_name = SECTION_MAP[section_name]
    skip_counter = 0
    unit_obj.sections[btmux_section_name]['crits'] = []

    section_lines = template_lines[section_start_line_num + 1:]
    for crit_num, crit_line in enumerate(section_lines, start=1):
        if skip_counter > 0:
            # We're within a multi-crit weapon. Next!
            skip_counter -= 1
            continue
        crit_line = crit_line.strip()
        if crit_line == '-Empty-':
            continue
        if crit_line == '':
            # End of section.
            break
        #from pprint import pprint
        #pprint(unit_obj.sections[btmux_section_name]['crits'])
        assert crit_num < 13, "Crit numbers can't exceed 12: %s" % crit_num

        # Map MTF crit to BTMux and get some details on what we'll be writing.
        crit_data = CRIT_MAP[crit_line]
        btmux_item_name = crit_data['name']
        if not btmux_item_name:
            # We don't support this item.
            continue

        num_crits, item_slots = _calc_crits(btmux_item_name, crit_num)

        # If this is something like FerroFibrous, a special tech gets added
        # to the unit.
        _add_special_from_crit(btmux_item_name, unit_obj)
        # Adds the crit(s) to the unit_obj's sections dict under the
        # appropriate section.
        _set_section_item(
            btmux_item_name, btmux_section_name, crit_data, item_slots, unit_obj)

        if num_crits > 1:
            # Multi-crit weapon/item. We'll skip the next however many crits.
            skip_counter = num_crits - 1


def _add_special_from_crit(btmux_item_name, unit_obj):
    if btmux_item_name.startswith('Ammo_'):
        return
    added_special = ITEM_TABLE[btmux_item_name].get('add_special')
    if added_special:
        unit_obj.specials.add(added_special)


def _set_section_item(btmux_item_name, btmux_section_name, crit_data,
                      item_slots, unit_obj):
    item_data = {
        'name': btmux_item_name,
        'ammo_count': None,
        'flags': crit_data.get('flags'),
    }

    special_override = crit_data.get('add_special')
    if special_override:
        unit_obj.specials.add(special_override)

    if btmux_item_name.startswith('Ammo_'):
        _, weap_name = btmux_item_name.split('Ammo_')
        if crit_data.get('ammo_count'):
            # Override is used in the crit mapping for half-tons of ammo.
            ammo_count = crit_data['ammo_count']
        else:
            ammo_count = ITEM_TABLE[weap_name].get('ammo_count')
        item_data['ammo_count'] = ammo_count

    item_tuple = (item_slots, item_data)
    unit_obj.sections[btmux_section_name]['crits'].append(item_tuple)


def _calc_crits(btmux_item_name, crit_num):
    if btmux_item_name.startswith('Ammo_'):
        num_crits = 1
    else:
        num_crits = ITEM_TABLE[btmux_item_name].get('crits', 1)

    if num_crits == 1:
        item_slots = [crit_num]
    else:
        last_crit = crit_num + num_crits
        item_slots = range(crit_num, last_crit)

    return num_crits, item_slots


def _add_specials(value_dict, unit_obj):
    hs_total, hs_type = value_dict['Heat Sinks'].split()
    if hs_type == 'Single':
        pass
    elif hs_type == 'Double':
        unit_obj.specials.add('DoubleHS')
    else:
        raise ValueError("Unknown HS type: %s" % hs_type)

    armor = value_dict['Armor']
    if 'Standard' in armor:
        pass
    elif 'Ferro-Fibrous' in armor:
        unit_obj.specials.add('FerroFibrous_Tech')
    elif 'Hardened' in armor:
        unit_obj.specials.add('HardenedArmor_Tech')
    elif 'Stealth' in armor:
        unit_obj.specials.add('StealthArmor_Tech')
    else:
        raise ValueError("Unknown armor type: %s" % armor)

    internals = value_dict['Structure']
    if 'Standard' in internals:
        pass
    elif 'Endo' in internals:
        unit_obj.specials.add('EndoSteel_Tech')
    else:
        raise ValueError("Unknown internals type: %s" % internals)

    engine = value_dict['Engine']
    if 'XL' in engine:
        unit_obj.specials.add('XLEngine_Tech')
    elif 'Light Engine' in engine:
        unit_obj.specials.add('LightEngine_Tech')
    elif 'Compact Engine' in engine:
        unit_obj.specials.add('CompactEngine_Tech')
    elif 'Fusion' in engine:
        pass
    else:
        raise ValueError("Unknown engine type: %s" % engine)

    if 'Clan' in value_dict['TechBase']:
        unit_obj.specials.add('Clan')

    if 'Triple-Strength' in value_dict['Myomer']:
        unit_obj.specials.add('TripleMyomerTech')

    if 'LtFerroFibrous_Tech' in unit_obj.specials:
        try:
            unit_obj.specials.remove('FerroFibrous_Tech')
        except KeyError:
            pass

    unit_obj.autoset_additional_specials()
