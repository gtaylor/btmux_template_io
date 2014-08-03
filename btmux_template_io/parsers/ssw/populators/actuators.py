from btmux_template_io.defines import QUAD_LEGS, BIPED_LEGS, BIPED_ARMS

from . common import add_basic_crit


def populate_actuators(xml_root, unit_obj):
    """
    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    if unit_obj.unit_move_type == 'Quad':
        leg_sections = QUAD_LEGS
    else:
        leg_sections = BIPED_LEGS

    for section in leg_sections:
        _add_actuator('ShoulderOrHip', section, 1, unit_obj)
        _add_actuator('UpperActuator', section, 2, unit_obj)
        _add_actuator('LowerActuator', section, 3, unit_obj)
        _add_actuator('HandOrFootActuator', section, 4, unit_obj)

    if unit_obj.unit_move_type == 'Quad':
        # Quads have all actuators in the legs, so we're done.
        return

    for section in BIPED_ARMS:
        _add_actuator('ShoulderOrHip', section, 1, unit_obj)
        _add_actuator('UpperActuator', section, 2, unit_obj)

    actuators_e = xml_root.xpath('baseloadout/actuators')[0]
    has_left_lower = actuators_e.get('lla') == "TRUE"
    has_left_hand = actuators_e.get('lh') == "TRUE"
    has_right_lower = actuators_e.get('rla') == "TRUE"
    has_right_hand = actuators_e.get('rh') == "TRUE"

    if has_left_lower:
        _add_actuator('LowerActuator', 'left_arm', 3, unit_obj)
    if has_right_lower:
        _add_actuator('LowerActuator', 'right_arm', 3, unit_obj)
    if has_left_hand:
        _add_actuator('HandOrFootActuator', 'left_arm', 4, unit_obj)
    if has_right_hand:
        _add_actuator('HandOrFootActuator', 'right_arm', 4, unit_obj)


def _add_actuator(actuator_name, btmux_section, crit, unit_obj):
    add_basic_crit(btmux_section, crit, actuator_name, unit_obj)
