from btmux_template_io.parsers.ssw.populators.common import add_basic_crit


def populate_gyro(xml_root, unit_obj):
    """
    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    gyro_type = xml_root.xpath('gyro')[0].text
    if 'Standard' in gyro_type:
        _add_gyro_crits(unit_obj, 'center_torso', num_crits=4)
    elif 'Compact' in gyro_type:
        _add_gyro_crits(unit_obj, 'center_torso', num_crits=2)
        unit_obj.specials.add('CompactGyro_Tech')
    elif 'Extra-Light' in gyro_type:
        _add_gyro_crits(unit_obj, 'center_torso', num_crits=6)
        unit_obj.specials.add('XLGyro_Tech')
    else:
        raise ValueError("Unknown gyro type: %s" % gyro_type)


def _add_gyro_crits(unit_obj, btmux_section, num_crits, start_crit=4):
    """
    First three CT crits are always engines.
    """

    for crit in range(start_crit, start_crit + num_crits):
        add_basic_crit(btmux_section, crit, 'Gyro', unit_obj)
