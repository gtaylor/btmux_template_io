from btmux_template_io.common_calcs import calc_section_internal
from btmux_template_io.parsers.ssw.section_mapping import SECTION_MAP
from btmux_template_io.parsers.ssw.armor_mapping import MECH_ARMOR_MAP

from . common import add_basic_crit


def populate_armor_and_internals(xml_root, unit_obj):
    """
    Look through the section armor key/vals and get the values transferred
    over to the unit object.

    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    armor_element = xml_root.xpath('armor')[0]
    for child in armor_element:
        loc = child.tag
        if loc == 'type':
            continue
        elif loc == 'location':
            # Armor crit
            continue
        armor = int(child.text)

        loc_dict = MECH_ARMOR_MAP[loc]
        btmux_loc = loc_dict[unit_obj.unit_move_type]
        armor_or_rear = 'rear' if loc_dict.get('is_rear', False) else 'armor'
        internals = calc_section_internal(unit_obj.weight, btmux_loc)

        if btmux_loc not in unit_obj.sections:
            unit_obj.sections[btmux_loc] = {}
        unit_obj.sections[btmux_loc][armor_or_rear] = armor
        unit_obj.sections[btmux_loc]['internals'] = internals

    armor_type = xml_root.xpath('armor/type')[0].text
    if armor_type == 'Standard Armor':
        pass
    elif armor_type == 'Light Ferro-Fibrous':
        unit_obj.specials.add('LtFerroFibrous_Tech')
        _add_armor_or_internals_crit(armor_element, unit_obj, 'LtFerroFibrous')
    elif armor_type == 'Heavy Ferro-Fibrous':
        unit_obj.specials.add('HvyFerroFibrous_Tech')
        _add_armor_or_internals_crit(armor_element, unit_obj, 'HvyFerroFibrous')
    elif armor_type == 'Ferro-Fibrous':
        unit_obj.specials.add('FerroFibrous_Tech')
        _add_armor_or_internals_crit(armor_element, unit_obj, 'FerroFibrous')
    elif armor_type == 'Hardened Armor':
        unit_obj.specials.add('HardenedArmor_Tech')
    elif armor_type == 'Stealth Armor':
        unit_obj.specials.add('StealthArmor_Tech')
        _add_armor_or_internals_crit(armor_element, unit_obj, 'StealthArmor')
    else:
        raise ValueError("Unknown armor type: %s" % armor_type)

    internals_element = xml_root.xpath('structure')[0]
    internals_type = internals_element.xpath('type')[0].text
    if internals_type == 'Standard Structure':
        pass
    elif internals_type == 'Endo-Steel':
        unit_obj.specials.add('EndoSteel_Tech')
        _add_armor_or_internals_crit(internals_element, unit_obj, 'EndoSteel')
    elif internals_type == 'Composite Structure':
        unit_obj.specials.add('CompositeInternal_Tech')
    elif internals_type == 'Reinforced Structure':
        unit_obj.specials.add('ReinforcedInternal_Tech')
    else:
        raise ValueError("Unknown internals type: %s" % internals_type)


def _add_armor_or_internals_crit(armor_elem, unit_obj, armor_crit_name):
    armor_loc_elements = armor_elem.xpath('location')
    for loc_e in armor_loc_elements:
        btmux_section = SECTION_MAP[loc_e.text]
        crit_num = int(loc_e.get('index')) + 1

        add_basic_crit(btmux_section, crit_num, armor_crit_name, unit_obj)
