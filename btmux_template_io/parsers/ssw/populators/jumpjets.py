from btmux_template_io.common_calcs import calc_jump_speed
from btmux_template_io.parsers.ssw.section_mapping import SECTION_MAP

from . common import add_basic_crit


def populate_jumpjets(xml_root, unit_obj):
    """
    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    jj_element = xml_root.xpath('baseloadout/jumpjets')
    if not jj_element:
        unit_obj.jump_speed = 0.0
        return
    jj_element = jj_element[0]

    jump_mp = int(jj_element.get('number'))
    jump_speed = calc_jump_speed(jump_mp)
    unit_obj.jump_speed = jump_speed

    jj_type = jj_element.xpath('type')[0].text
    if jj_type == 'Standard Jump Jet':
        # Standard JJs get no special tech in BTMux.
        pass
    else:
        raise ValueError("Unknown JJ type: %s" % jj_type)

    _add_jumpjet_crits(jj_element, unit_obj)


def _add_jumpjet_crits(jj_element, unit_obj):
    jj_loc_elements = jj_element.xpath('location')
    for loc_e in jj_loc_elements:
        btmux_section = SECTION_MAP[loc_e.text]
        crit_num = int(loc_e.get('index')) + 1

        add_basic_crit(btmux_section, crit_num, 'JumpJet', unit_obj)
