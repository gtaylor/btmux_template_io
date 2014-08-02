
def add_crit(btmux_section, item_tuple, unit_obj):
    unit_obj.sections[btmux_section]['crits'].append(item_tuple)


def add_basic_crit(btmux_section, crit_num, item_name, unit_obj):
    item_data = {
        'name': item_name,
        'ammo_count': None,
        'flags': None,
    }

    item_slots = [crit_num]
    item_tuple = (item_slots, item_data)
    add_crit(btmux_section, item_tuple, unit_obj)
