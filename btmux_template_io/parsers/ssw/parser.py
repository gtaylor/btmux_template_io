"""
Solaris Skunk Werks (SSW) parser.
"""

from lxml import etree
from btmux_template_io.defines import QUAD_LEGS, BIPED_LEGS, BIPED_ARMS, \
    BIPED_SECTIONS, QUAD_SECTIONS, EMPTY_SECTION_DICT

from btmux_template_io.item_table import ITEM_TABLE, WEAPON_TABLE
from btmux_template_io.parsers.ssw.populators.armor_and_ints import \
    populate_armor_and_internals
from btmux_template_io.parsers.ssw.populators.common import add_crit
from btmux_template_io.parsers.ssw.populators.engines import \
    populate_movement_and_engine
from btmux_template_io.parsers.ssw.populators.gyros import populate_gyro
from btmux_template_io.parsers.ssw.populators.head import populate_head
from btmux_template_io.parsers.ssw.section_mapping import SECTION_MAP
from btmux_template_io.unit import BTMuxUnit
from btmux_template_io.common_calcs import calc_jump_speed
from btmux_template_io.parsers.ssw.crit_mapping import CRIT_MAP, \
    AMMO_FLAG_MAPPING


def parse_from_string(template_contents):
    """
    Given the full contents of a properly formed MTF file, parse it
    and return an object with the template's values set as attributes.

    :param str template_contents: The full contents of a valid template.
    :rtype: btmux_template_io.unit.BTMuxUnit
    :return: A BTMuxUnit instance with the template's values set in attributes.
    """

    unit_obj = BTMuxUnit()
    xml_root = etree.fromstring(template_contents)
    unit_obj.name = xml_root.get('name')
    unit_obj.reference = xml_root.get('model')
    unit_obj.weight = int(xml_root.get('tons'))
    # Hardcoded for now. Not super interested in vehicles, personally.
    unit_obj.unit_type = 'Mech'

    move_type = xml_root.xpath('motive_type')[0].text
    if move_type == 'Biped':
        unit_obj.unit_move_type = 'Biped'
    elif move_type == 'Quad':
        unit_obj.unit_move_type = 'Quad'
    else:
        raise ValueError('Unknown move type: %s' % move_type)

    _initialize_empty_sections(unit_obj)
    populate_head(xml_root, unit_obj)
    populate_gyro(xml_root, unit_obj)
    populate_movement_and_engine(xml_root, unit_obj)
    _set_jumpjets(xml_root, unit_obj)
    _set_heatsinks(xml_root, unit_obj)
    populate_armor_and_internals(xml_root, unit_obj)
    _set_actuators(xml_root, unit_obj)
    _set_enhancements(xml_root, unit_obj)
    _set_equipment(xml_root, unit_obj)
    _add_specials(xml_root, unit_obj)

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


def _initialize_empty_sections(unit_obj):
    if unit_obj.unit_move_type == 'Biped':
        sections = BIPED_SECTIONS
    else:
        sections = QUAD_SECTIONS

    for btmux_section in sections:
        unit_obj.sections[btmux_section] = EMPTY_SECTION_DICT


def _set_jumpjets(xml_root, unit_obj):
    """
    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    jj_element = xml_root.xpath('baseloadout/jumpjets')
    if not jj_element:
        unit_obj.jump_speed = 0.0
        return

    jump_mp = int(jj_element[0].get('number'))
    jump_speed = calc_jump_speed(jump_mp)
    unit_obj.jump_speed = jump_speed

    # TODO: Load JJ crits.


def _set_heatsinks(xml_root, unit_obj):
    """
    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    hs_total = int(xml_root.xpath('baseloadout/heatsinks')[0].get('number'))
    hs_type = xml_root.xpath('baseloadout/heatsinks/type')[0].text

    if hs_type.startswith('Single'):
        unit_obj.heatsink_total = hs_total
    elif hs_type.startswith('Double'):
        unit_obj.heatsink_total = hs_total * 2
        unit_obj.specials.add('DoubleHS')
    else:
        raise ValueError("Unknown HS type: %s" % hs_type)

    # TODO: Load HS crits.


def _set_actuators(xml_root, unit_obj):
    """
    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    if unit_obj.unit_move_type == 'Quad':
        leg_sections = QUAD_LEGS
    else:
        leg_sections = BIPED_LEGS

    for section in leg_sections:
        _add_actuator('ShoulderOrHip', section, 1, unit_obj)
        _add_actuator('UpperActuator', section, 2, unit_obj)
        _add_actuator('LowerActuator', section, 3, unit_obj)
        _add_actuator('HandOrFootActuator', section, 4, unit_obj)

    if unit_obj.unit_move_type == 'Quad':
        # Quads have all actuators in the legs, so we're done.
        return

    for section in BIPED_ARMS:
        _add_actuator('ShoulderOrHip', section, 1, unit_obj)
        _add_actuator('UpperActuator', section, 2, unit_obj)

    actuators_e = xml_root.xpath('baseloadout/actuators')[0]
    has_left_lower = actuators_e.get('lla') == "TRUE"
    has_left_hand = actuators_e.get('lh') == "TRUE"
    has_right_lower = actuators_e.get('rla') == "TRUE"
    has_right_hand = actuators_e.get('rh') == "TRUE"

    if has_left_lower:
        _add_actuator('LowerActuator', 'left_arm', 3, unit_obj)
    if has_right_lower:
        _add_actuator('LowerActuator', 'right_arm', 3, unit_obj)
    if has_left_hand:
        _add_actuator('HandOrFootActuator', 'right_arm', 4, unit_obj)
    if has_right_hand:
        _add_actuator('HandOrFootActuator', 'left_arm', 4, unit_obj)


def _add_actuator(actuator_name, btmux_section, crit, unit_obj):
    item_data = {
        'name': actuator_name,
        'ammo_count': None,
        'flags': None,
    }

    item_slots = [crit]
    item_tuple = (item_slots, item_data)
    add_crit(btmux_section, item_tuple, unit_obj)


def _set_enhancements(xml_root, unit_obj):
    enhancement_e = xml_root.xpath('enhancement')
    for enh_e in enhancement_e:
        e_type = enh_e.xpath('type')[0].text
        if e_type == "TSM":
            unit_obj.specials.add('TripleMyomerTech')


def _set_equipment(xml_root, unit_obj):
    equipment_elements = xml_root.xpath('baseloadout/equipment')
    for equip_e in equipment_elements:
        e_type = equip_e.xpath('type')[0].text

        if e_type in ['energy', 'ballistic', 'missile']:
            _add_weapon(equip_e, unit_obj)
        elif e_type == 'ammunition':
            _add_ammo(equip_e, unit_obj)
        elif e_type == 'physical':
            _add_physical_weapon(equip_e, unit_obj)
        elif e_type == 'equipment':
            _add_equipment(equip_e, unit_obj)
        elif e_type == 'CASE':
            _add_case(equip_e, unit_obj)
        else:
            raise ValueError("Invalid equipment type: %s" % e_type)

    # TODO: Add Artemis after LRM/SRM crits if present.


def _add_weapon(equip_e, unit_obj):
    # TODO: splitlocation tag detection
    splitloc_e = equip_e.xpath('splitlocation')
    if splitloc_e:
        raise ValueError("Split crits not yet supported.")

    e_name = equip_e.xpath('name')[0].text
    name_split = e_name.split()
    if name_split[0] == '(R)':
        flags = 'RearMount'
        name_split = name_split[1:]
    else:
        flags = None

    techbase = 'CL' if 'CL' in name_split[0] else 'IS'
    weap_name = ' '.join(name_split[1:])

    btmux_name = techbase + "." + CRIT_MAP[weap_name]['name']
    item_data = WEAPON_TABLE[btmux_name]

    mapped_flags = CRIT_MAP[weap_name].get('flags')
    if mapped_flags:
        # NOTE: This will override RearMount because of the shitty BTMux template
        # format.
        flags = mapped_flags

    location_e = equip_e.xpath('location')[0]
    ssw_section = location_e.text
    btmux_section = SECTION_MAP[ssw_section]

    first_crit_num = int(location_e.get('index'))
    num_crits = item_data['crits']

    item_data = {
        'name': btmux_name,
        'ammo_count': None,
        'flags': flags,
    }

    item_slots = range(first_crit_num, first_crit_num + num_crits)
    item_tuple = (item_slots, item_data)
    add_crit(btmux_section, item_tuple, unit_obj)


def _add_ammo(equip_e, unit_obj):
    e_name = equip_e.xpath('name')[0].text
    name_split = e_name.split('@')
    print name_split

    techbase = 'CL' if 'CL' in name_split[0] else 'IS'
    weap_name = ' '.join(name_split[1:]).strip()
    if '(' in weap_name:
        atype_begin = weap_name.index('(') + 1
        atype_end = weap_name.index(')')
        atype = weap_name[atype_begin:atype_end]
        weap_name = weap_name[:atype_begin - 1].strip()
        flags = AMMO_FLAG_MAPPING[atype]['flags']
        ammo_count_override = AMMO_FLAG_MAPPING[atype].get('ammo_count')
    else:
        flags = None
        ammo_count_override = None

    btmux_name = techbase + "." + CRIT_MAP[weap_name]['name']
    item_data = WEAPON_TABLE[btmux_name]

    if flags and 'Artemis' in flags:
        unit_obj.specials.add('ArtemisIV')

    item_data = {
        'name': btmux_name,
        'ammo_count': ammo_count_override if ammo_count_override else item_data['ammo_count'],
        'flags': flags,
    }
    print item_data


def _add_equipment(equip_e, unit_obj):
    pass


def _add_physical_weapon(equip_e, unit_obj):
    pass


def _add_case(equip_e, unit_obj):
    pass


def _add_special_from_mtf_map(mtf_name, unit_obj):
    added_special = CRIT_MAP[mtf_name].get('add_special')
    if added_special:
        unit_obj.specials.add(added_special)


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


def _add_specials(xml_root, unit_obj):
    """
    Adds some additional special techs to the unit.

    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    techbase = xml_root.xpath('techbase')[0].text
    if 'Clan' in techbase:
        unit_obj.specials.add('Clan')

    if 'LtFerroFibrous_Tech' in unit_obj.specials:
        try:
            unit_obj.specials.remove('FerroFibrous_Tech')
        except KeyError:
            pass

    #unit_obj.autoset_additional_specials()
