from btmux_template_io.item_table import WEAPON_TABLE
from btmux_template_io.parsers.ssw.crit_mapping import AMMO_FLAG_MAPPING, \
    WEAPON_AND_AMMO_MAP
from btmux_template_io.parsers.ssw.populators.common import add_crit
from btmux_template_io.parsers.ssw.section_mapping import SECTION_MAP


def add_ammo(equip_e, unit_obj):
    e_name = equip_e.xpath('name')[0].text
    name_split = e_name.split('@')

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

    btmux_name = techbase + "." + WEAPON_AND_AMMO_MAP[weap_name]['name']
    item_data = WEAPON_TABLE[btmux_name]

    if flags and 'Artemis' in flags:
        unit_obj.specials.add('ArtemisIV')

    if ammo_count_override:
        ammo_count = ammo_count_override
    elif flags and 'Halfton' in flags:
        ammo_count = item_data['ammo_count'] / 2
    elif flags and 'Precision' in flags:
        ammo_count = item_data['ammo_count'] / 2
    else:
        ammo_count = item_data['ammo_count']

    item_data = {
        'name': 'Ammo_' + btmux_name,
        'ammo_count': ammo_count,
        'flags': flags,
    }

    location_e = equip_e.xpath('location')[0]
    ssw_section = location_e.text
    btmux_section = SECTION_MAP[ssw_section]
    crit_num = int(location_e.get('index')) + 1

    item_slots = [crit_num]
    item_tuple = (item_slots, item_data)
    add_crit(btmux_section, item_tuple, unit_obj)
