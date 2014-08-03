from btmux_template_io.parsers.ssw.populators.common import add_basic_crit


def populate_gyro(xml_root, unit_obj):
    """
    Different kinds of Gyros take different numbers of crits. Figure out
    how many crits the Gyro has and place accordingly.

    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    gyro_type = xml_root.xpath('gyro')[0].text
    if gyro_type == 'Standard Gyro':
        _add_gyro_crits(unit_obj, num_crits=4)
    elif gyro_type == 'Compact Gyro':
        _add_gyro_crits(unit_obj, num_crits=2)
        unit_obj.specials.add('CompactGyro_Tech')
    elif gyro_type == 'Extra-Light Gyro':
        _add_gyro_crits(unit_obj, num_crits=6)
        unit_obj.specials.add('XLGyro_Tech')
    else:
        raise ValueError("Unknown gyro type: %s" % gyro_type)


def _add_gyro_crits(unit_obj, num_crits, start_crit=4):
    """
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    :param int num_crits: Number of gyro crits to fill.
    :param int start_crit: The starting crit number for the gyro.
    """

    for crit in range(start_crit, start_crit + num_crits):
        add_basic_crit('center_torso', crit, 'Gyro', unit_obj)
