from btmux_template_io.parsers.ssw.section_mapping import SECTION_MAP

from . common import add_basic_crit


def populate_heatsinks(xml_root, unit_obj):
    """
    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    hs_element = xml_root.xpath('baseloadout/heatsinks')[0]
    hs_total = int(hs_element.get('number'))
    hs_type = hs_element.xpath('type')[0].text

    if hs_type == 'Single Heat Sink':
        unit_obj.heatsink_total = hs_total
        crits_per_hs = 1
    elif hs_type == 'Double Heat Sink':
        unit_obj.heatsink_total = hs_total * 2
        unit_obj.specials.add('DoubleHS')
        crits_per_hs = 3
    else:
        raise ValueError("Unknown HS type: %s" % hs_type)

    _add_hs_crits(hs_element, crits_per_hs, unit_obj)


def _add_hs_crits(hs_element, crits_per_hs, unit_obj):
    hs_loc_elements = hs_element.xpath('location')
    for loc_e in hs_loc_elements:
        btmux_section = SECTION_MAP[loc_e.text]
        crit_num = int(loc_e.get('index')) + 1
        if crits_per_hs > 1:
            crits = range(crit_num, crit_num + crits_per_hs)
        else:
            crits = [crit_num]

        for crit in crits:
            add_basic_crit(btmux_section, crit, 'HeatSink', unit_obj)
