"""
Solaris Skunk Werks (SSW) parser.
"""

from lxml import etree

from btmux_template_io.defines import BIPED_SECTIONS, QUAD_SECTIONS
from btmux_template_io.parsers.ssw.populators.weapons import \
    populate_artemis_crits
from btmux_template_io.unit import BTMuxUnit

from . populators.actuators import populate_actuators
from . populators.armor_and_ints import populate_armor_and_internals
from . populators.engines import populate_movement_and_engine
from . populators.enhancements import populate_enhancements
from . populators.equipment import populate_equipment
from . populators.gyros import populate_gyro
from . populators.head import populate_head
from . populators.heatsinks import populate_heatsinks
from . populators.jumpjets import populate_jumpjets


def parse_from_string(template_contents):
    """
    Given the full contents of a properly formed SSW file, parse it
    and return an object with the template's values set as attributes.

    :param str template_contents: The full contents of a valid template.
    :rtype: btmux_template_io.unit.BTMuxUnit
    :return: A BTMuxUnit instance with the template's values set in attributes.
    """

    unit_obj = BTMuxUnit()
    xml_root = etree.fromstring(template_contents)
    unit_obj.name = xml_root.get('name')
    unit_obj.reference = xml_root.get('model')
    unit_obj.weight = int(xml_root.get('tons'))
    # Hardcoded for now. Not super interested in vehicles, personally.
    unit_obj.unit_type = 'Mech'

    move_type = xml_root.xpath('motive_type')[0].text
    if move_type == 'Biped':
        unit_obj.unit_move_type = 'Biped'
    elif move_type == 'Quad':
        unit_obj.unit_move_type = 'Quad'
    else:
        raise ValueError('Unknown move type: %s' % move_type)

    _initialize_empty_sections(unit_obj)
    populate_head(xml_root, unit_obj)
    populate_gyro(xml_root, unit_obj)
    populate_movement_and_engine(xml_root, unit_obj)
    populate_jumpjets(xml_root, unit_obj)
    populate_heatsinks(xml_root, unit_obj)
    populate_armor_and_internals(xml_root, unit_obj)
    populate_actuators(xml_root, unit_obj)
    populate_enhancements(xml_root, unit_obj)
    populate_equipment(xml_root, unit_obj)
    populate_artemis_crits(unit_obj)
    _add_specials(xml_root, unit_obj)

    #unit_obj.print_crits()

    return unit_obj


def parse_from_file(template_path):
    """
    Given a properly formed MTF file, parse it and return an object with
    the template's values set as attributes.

    :param str template_path: Full path to a properly formed BTMux template.
    :rtype: btmux_template_io.unit.BTMuxUnit
    :return: A BTMuxUnit instance with the template's values set in attributes.
    """

    fobj = open(template_path, 'r')
    return parse_from_string(fobj.read())


def _initialize_empty_sections(unit_obj):
    """
    Pre-creates the section dicts for this unit.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    if unit_obj.unit_move_type == 'Biped':
        sections = BIPED_SECTIONS
    else:
        sections = QUAD_SECTIONS

    for btmux_section in sections:
        unit_obj.sections[btmux_section] = {
            'armor': 0,
            'internals': 0,
            'crits': [],
        }


def _add_specials(xml_root, unit_obj):
    """
    Adds some additional special techs to the unit.

    :param lxml.etree.Element xml_root: The root of the XML doc.
    :param btmux_template_io.unit.BTMuxUnit unit_obj: The unit instance
        being populated.
    """

    techbase = xml_root.xpath('techbase')[0].text
    if 'Clan' in techbase:
        unit_obj.specials.add('Clan')

    if 'LtFerroFibrous_Tech' in unit_obj.specials:
        try:
            unit_obj.specials.remove('FerroFibrous_Tech')
        except KeyError:
            pass

    unit_obj.autoset_additional_specials()
