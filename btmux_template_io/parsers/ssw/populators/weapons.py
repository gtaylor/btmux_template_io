from btmux_template_io.item_table import WEAPON_TABLE
from btmux_template_io.parsers.ssw.crit_mapping import WEAPON_AND_AMMO_MAP
from btmux_template_io.parsers.ssw.populators.common import add_crit, \
    add_basic_crit
from btmux_template_io.parsers.ssw.section_mapping import SECTION_MAP


def add_weapon(equip_e, unit_obj):
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

    btmux_name = techbase + "." + WEAPON_AND_AMMO_MAP[weap_name]['name']
    item_data = WEAPON_TABLE[btmux_name]
    add_special = item_data.get('add_special')
    if add_special:
        unit_obj.specials.add(add_special)

    mapped_flags = WEAPON_AND_AMMO_MAP[weap_name].get('flags')
    if mapped_flags:
        # NOTE: This will override RearMount because of the shitty BTMux template
        # format.
        flags = mapped_flags

    location_e = equip_e.xpath('location')[0]
    ssw_section = location_e.text
    btmux_section = SECTION_MAP[ssw_section]

    first_crit_num = int(location_e.get('index')) + 1
    num_crits = item_data['crits']

    item_data = {
        'name': btmux_name,
        'ammo_count': None,
        'flags': flags,
    }

    item_slots = range(first_crit_num, first_crit_num + num_crits)
    item_tuple = (item_slots, item_data)
    add_crit(btmux_section, item_tuple, unit_obj)


def populate_artemis_crits(unit_obj):
    """
    If the unit has artemis, all SRM and LRM launchers must be Artemis.
    """

    has_artemis = False
    for crit in unit_obj.crits:
        if crit[1]['flags'] == 'Artemis/Mine':
            # We found Artemis Ammo!
            has_artemis = True
            break

    if not has_artemis:
        return

    # Now stick an ArtemisIV crit after all SRM/LRM launchers and
    # set the weapon to fire Artemis ammo.
    for section_name in unit_obj.sections.keys():
        section_crits = unit_obj.sections[section_name]['crits']
        for crit in section_crits:
            crit_list, crit_dict = crit
            crit_name = crit_dict['name']
            if crit_name.startswith('IS.SRM') or \
                    crit_name.startswith('CL.SRM') or \
                    crit_name.startswith('IS.LRM') or \
                    crit_name.startswith('CL.LRM'):
                # Set the weapon to fire ArtemisIV.
                crit_dict['flags'] = 'Artemis/Mine'
                artemis_crit_num = crit_list[-1] + 1
                # Add an ArtemisIV crit directly after the launcher.
                add_basic_crit(
                    section_name, artemis_crit_num, 'ArtemisIV', unit_obj)
