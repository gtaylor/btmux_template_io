from btmux_template_io.parsers.ssw.populators.common import add_basic_crit


def populate_head(xml_root, unit_obj):
    """
    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    cockpit_type = xml_root.xpath('cockpit/type')[0].text
    if 'Standard' in cockpit_type:
        add_basic_crit('head', 1, 'LifeSupport', unit_obj)
        add_basic_crit('head', 2, 'Sensors', unit_obj)
        add_basic_crit('head', 3, 'Cockpit', unit_obj)
        add_basic_crit('head', 5, 'Sensors', unit_obj)
        add_basic_crit('head', 6, 'LifeSupport', unit_obj)
    elif 'Small' in cockpit_type:
        unit_obj.specials.add('SmallCockpit_Tech')
        add_basic_crit('head', 1, 'LifeSupport', unit_obj)
        add_basic_crit('head', 2, 'Sensors', unit_obj)
        add_basic_crit('head', 3, 'Cockpit', unit_obj)
        add_basic_crit('head', 4, 'Sensors', unit_obj)
    else:
        raise ValueError("Unknown cockpit type: %s" % cockpit_type)
