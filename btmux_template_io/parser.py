"""
Top-level API for the template parser. BTMux template files are comprised
of two segments:

    * What we'll call the "header" section. This contains stuff like the total
      heatsink count, mech type, movement type, etc.
    * The unit's sections+crit list. This shows what things occupy which
      crit numbers in each section.

The stuff in the header section gets plunked into attributes on the
parsed unit object. See the HEADER_FIELDS dict for a map of header keys
to attributes.

The sections get stuffed into a dict named ``sections`` on the unit object.
"""

import re

from btmux_template_io.unit import BTMuxUnit


# TODO: Get more specific than (.*) with these groups.
HEADER_RE = re.compile(r'^(?P<field_name>[a-zA-Z_]+)(.*){(?P<field_value>.*)}$')
SECTION_RE = re.compile(r'^([ ]*)(?P<field_name>[\w-]+)(.*){(?P<field_value>.*)}$')

# Maps the header field's name in the template to attributes on the eventual
# unit object. We also cast the values for convenience.
HEADER_FIELDS = {
    'Name': {'type': str, 'unit_attr': 'name'},
    'Reference': {'type': str, 'unit_attr': 'reference'},
    'Unit_Era': {'type': str, 'unit_attr': 'unit_era'},
    'Unit_TRO': {'type': str, 'unit_attr': 'unit_tro'},
    'Type': {'type': str, 'unit_attr': 'unit_type'},
    'Move_Type': {'type': str, 'unit_attr': 'unit_move_type'},
    'Tons': {'type': int, 'unit_attr': 'weight'},
    'Heat_Sinks': {'type': int, 'unit_attr': 'heatsink_total'},
    'Computer': {'type': int, 'unit_attr': 'computer_level'},
    'Radio': {'type': int, 'unit_attr': 'radio_level'},
    'Radio_Range': {'type': int, 'unit_attr': 'radio_range'},
    'RadioType': {'type': int, 'unit_attr': 'radio_type'},
    'Tac_Range': {'type': int, 'unit_attr': 'tactical_range'},
    'LRS_Range': {'type': int, 'unit_attr': 'lrs_range'},
    'Scan_Range': {'type': int, 'unit_attr': 'scan_range'},
    'Fuel': {'type': int, 'unit_attr': 'fuel'},
    'Cargo_Space': {'type': int, 'unit_attr': 'cargo_space'},
    'Max_Suits': {'type': int, 'unit_attr': 'battlesuit_total'},
    'Mech_BV': {'type': int, 'unit_attr': 'battle_value'},
    'Max_Speed': {'type': float, 'unit_attr': 'max_speed'},
    'Jump_Speed': {'type': float, 'unit_attr': 'jump_speed'},
    'Comment': {'type': str, 'unit_attr': 'templater_comment'},
    'Specials': {'type': list, 'unit_attr': 'specials'},
    'InfantrySpecials': {'type': list, 'unit_attr': 'infantry_specials'},
}


def parse_from_string(template_contents, unit_obj=None):
    """
    Given the full contents of a properly formed template file, parse it
    and return an object with the template's values set as attributes.

    :param str template_contents: The full contents of a valid template.
    :keyword unit_obj: If you want to pass in your own unit instance to use,
        do so here. Otherwise we'll use our default :py:class:`BTMuxUnit`
        class.
    :rtype: btmux_template_io.unit.BTMuxUnit
    :return: A BTMuxUnit instance with the template's values set in attributes.
    """

    if not unit_obj:
        unit_obj = BTMuxUnit()
    lines = template_contents.split('\n')

    section_indices = []
    # Find the lines that unit sections occur on.
    for line_num, line in enumerate(lines):
        if line and '{' not in line:
            section_indices.append(line_num)
    # Now that we know where the section lines are, parse all the way up
    # until we hit the line before the first section. We can assume all of
    # the previous lines are headers.
    _parse_header_fields(lines, section_indices[0], unit_obj)
    # Now we'll go back and parse each section by reading until we hit the
    # line before the next section.
    for section_start in section_indices:
        _parse_section(lines, section_start, unit_obj)
    return unit_obj


def parse_from_file(template_path, unit_obj=None):
    """
    Given a properly formed template file, parse it and return an object with
    the template's values set as attributes.

    :param str template_path: Full path to a properly formed BTMux template.
    :keyword unit_obj: If you want to pass in your own unit instance to use,
        do so here. Otherwise we'll use our default :py:class:`BTMuxUnit`
        class.
    :rtype: btmux_template_io.unit.BTMuxUnit
    :return: A BTMuxUnit instance with the template's values set in attributes.
    """

    fobj = open(template_path, 'r')
    return parse_from_string(fobj.read(), unit_obj=unit_obj)


def _parse_header_fields(template_lines, header_end_line_num, unit_obj):
    """
    Parse the header segment of the template file. Attributes end up
    set directly on ``unit_obj``.

    :param list template_lines: The template contents split into lines.
    :param int header_end_line_num: The line number of the first section, so
        we can parse all the way up to the previous line.
    :param unit_obj: The object to set the parsed attributes on.
    """

    header_line_nums = range(0, header_end_line_num)
    for line_no in header_line_nums:
        # Example header line:
        # Specials         { DoubleHS FerroFibrous_Tech XLEngine_Tech ECM }
        line = template_lines[line_no]
        matches = re.match(HEADER_RE, line)
        field_name = matches.group('field_name').strip()
        field_value = matches.group('field_value').strip()

        field_type = HEADER_FIELDS[field_name]['type']
        if field_type == list:
            # This is a List type header. Split it up by spaces and that's it.
            parsed_value = field_value.split()
        else:
            parsed_value = field_type(field_value)

        unit_attr = HEADER_FIELDS[field_name]['unit_attr']
        setattr(unit_obj, unit_attr, parsed_value)


def _parse_section(template_lines, section_start_line_num, unit_obj):
    """
    Parse a section segment in the template file. The ``sections``
    attribute on ``unit_obj`` will contain the result of this.

    :param list template_lines: The template contents split into lines.
    :param int section_start_line_num: The first line in the section to parse.
    :param unit_obj: The object to set the sections attribute on.
    """

    section_name = template_lines[section_start_line_num]
    section_data = {}
    crits = []

    line_num = section_start_line_num + 1
    while True:
        line = template_lines[line_num]
        if '{' not in line:
            # We've ran into the next section (or EOF). Go no further.
            break
        matches = re.match(SECTION_RE, line)
        field_name = matches.group('field_name').strip()
        field_value = matches.group('field_value').strip()

        if field_name.startswith('CRIT'):
            # This is a crit line.
            crits.append(_parse_crit(field_name, field_value))
        else:
            # This is an armor or internal total field.
            section_data[field_name.lower()] = int(field_value)

        line_num += 1
    section_data['crits'] = crits
    unit_obj.sections[section_name] = section_data


def _parse_crit(raw_field_name, field_value):
    """
    Within each section, there are crit fields that show what is contained
    in each section. This takes a raw crit field name/value and makes sense
    out of it.

    :param str raw_field_name: The name of the crit field.
    :param str field_value: The field's crit contents value.
    :rtype: tuple
    :returns: A tuple in the form of ([crit_numbers], crit_data_dict)
    """

    value_split = field_value.split()
    crit_name = value_split[0]
    ammo_tons = value_split[1]
    flags = value_split[2]
    # TODO: There is a third value, but I'm not sure what it is.

    ammo_tons = None if ammo_tons == '-' else ammo_tons
    flags = None if flags == '-' else flags
    crit_data = {'name': crit_name, 'ammo_tons': ammo_tons, 'flags': flags}

    _, field_name = raw_field_name.split('CRIT_')
    if '-' in field_name:
        begin, end = field_name.split('-')
        crit_range = range(int(begin), int(end) + 1)
        return crit_range, crit_data
    else:
        return [int(field_name)], crit_data
