from btmux_template_io.item_table import ITEM_TABLE
from btmux_template_io.parsers.ssw.crit_mapping import PHYSICAL_WEAPON_MAP, \
    EQUIPMENT_MAP

from . ammo import add_ammo
from . common import add_crits_from_locations
from . weapons import add_weapon


def populate_equipment(xml_root, unit_obj):
    """
    Equipment is the general term for an item within a mech. Weapons,
    ammo, melee weapons, etc.

    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    equipment_elements = xml_root.xpath('baseloadout/equipment')
    for equip_e in equipment_elements:
        e_type = equip_e.xpath('type')[0].text
        e_name = equip_e.xpath('name')[0].text

        if e_type in ['energy', 'ballistic', 'missile']:
            add_weapon(equip_e, unit_obj)
        elif 'Anti-Missile' in e_name and '@' not in e_name:
            # These are of type equipment, but BTMux handles them like weapons.
            add_weapon(equip_e, unit_obj)
        elif e_type == 'ammunition':
            add_ammo(equip_e, unit_obj)
        elif e_type == 'physical':
            _add_equipment(equip_e, unit_obj, PHYSICAL_WEAPON_MAP)
        elif e_type in ['equipment', 'CASE']:
            _add_equipment(equip_e, unit_obj, EQUIPMENT_MAP)
        else:
            raise ValueError("Invalid equipment type: %s" % e_type)


def _add_equipment(equip_e, unit_obj, map_dict):
    ssw_name = equip_e.xpath('name')[0].text
    try:
        mapped_add_special = map_dict[ssw_name].get('add_special')
    except KeyError:
        raise ValueError("Unknown equipment type: %s" % ssw_name)

    if mapped_add_special:
        unit_obj.specials.add(mapped_add_special)

    btmux_name = map_dict[ssw_name]['name']

    if not btmux_name:
        # Probably something like a SearchLight, which has no crit in BTMux.
        return

    data_dict = ITEM_TABLE[btmux_name]
    if 'tons_per_crit' in data_dict:
        crits_per_item = int(round(
            float(unit_obj.weight) / data_dict['tons_per_crit'], 0))
    else:
        crits_per_item = data_dict.get('crits', 1)

    add_special = data_dict.get('add_special')
    if add_special:
        unit_obj.specials.add(add_special)

    add_crits_from_locations(
        equip_e,
        btmux_name,
        unit_obj,
        crits_per_item=crits_per_item)
