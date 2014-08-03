from btmux_template_io.parsers.ssw.section_mapping import SECTION_MAP


def add_crit(btmux_section, item_tuple, unit_obj):
    item_slots, _ = item_tuple
    for crit in unit_obj.sections[btmux_section]['crits']:
        inserted_critnums = set(item_slots)
        existing_critnums = set(crit[0])
        if inserted_critnums.intersection(existing_critnums):
            raise ValueError("Overlapping crits on %s crit %s" % (
                btmux_section, item_slots))
    unit_obj.sections[btmux_section]['crits'].append(item_tuple)
    unit_obj.sort_crits()


def add_basic_crit(btmux_section, crit_num, item_name, unit_obj):
    item_data = {
        'name': item_name,
        'ammo_count': None,
        'flags': None,
    }

    if isinstance(crit_num, int):
        item_slots = [crit_num]
    elif isinstance(crit_num, list):
        item_slots = crit_num
    else:
        raise TypeError('crit_num must be an int or list.')

    item_tuple = (item_slots, item_data)
    add_crit(btmux_section, item_tuple, unit_obj)


def add_crits_from_locations(top_e, item_name, unit_obj, crits_per_item=1):
    loc_elements = top_e.xpath('location')
    for loc_e in loc_elements:
        btmux_section = SECTION_MAP[loc_e.text]
        crit_num = int(loc_e.get('index')) + 1
        if crits_per_item > 1:
            crits = range(crit_num, crit_num + crits_per_item)
        else:
            crits = crit_num

        add_basic_crit(btmux_section, crits, item_name, unit_obj)
