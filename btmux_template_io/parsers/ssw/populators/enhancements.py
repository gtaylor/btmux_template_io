from btmux_template_io.item_table import CRIT_TABLE
from btmux_template_io.parsers.ssw.crit_mapping import EQUIPMENT_MAP

from . common import add_crits_from_locations


def populate_enhancements(xml_root, unit_obj):
    """
    Enhancements are things like MASC, TAG, TSM, etc.

    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    enhancement_elements = xml_root.xpath('enhancement')
    for enhancement_e in enhancement_elements:
        e_type = enhancement_e.xpath('type')[0].text

        try:
            enhancement_data = EQUIPMENT_MAP[e_type]
        except KeyError:
            raise ValueError("Invalid enhancement type: %s" % e_type)

        _add_enhancement(enhancement_e, enhancement_data, unit_obj)


def _add_enhancement(enhancement_e, enhancement_data, unit_obj):
    btmux_name = enhancement_data['name']
    crits_per_item = CRIT_TABLE[btmux_name].get('crits', 1)

    add_special = CRIT_TABLE[btmux_name].get('add_special')
    if add_special:
        unit_obj.specials.add(add_special)

    add_crits_from_locations(
        enhancement_e,
        btmux_name,
        unit_obj,
        crits_per_item=crits_per_item)
