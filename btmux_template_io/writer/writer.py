import string
import datetime
from collections import OrderedDict


def write_to_file(unit, fobj):
    """
    Writes a unit out to a file-like object in the BTMux standard format.

    :param btmux_template_io.unit.BTMuxUnit unit: The unit instance to write.
    :param fobj: A file-like object.
    """

    _write_all_headers(unit, fobj)
    _write_all_sections(unit, fobj)


def _write_all_headers(unit, fobj):
    """
    Writes the top header section of the template file.

    :param btmux_template_io.unit.BTMuxUnit unit: The unit instance to write.
    :param fobj: A file-like object.
    """

    now = datetime.datetime.now()
    # Case and order is significant.
    header_map = (
        ('Name', unit.name),
        ('Reference', unit.reference),
        ('Type', unit.unit_type),
        ('Unit_Era', unit.unit_era),
        ('Unit_TRO', unit.unit_tro),
        ('Move_Type', unit.unit_move_type),
        ('Tons', unit.weight),
        ('Comment', "Saved by: btmux_maplib_io(Python) at %s" % now.ctime()),
        ('Computer', 4),
        ('Radio', 5),
        ('Heat_Sinks', unit.heatsink_total),
        ('Mech_BV', unit.battle_value),
        ('Cargo_Space', unit.cargo_space),
        ('Max_Suits', unit.battlesuit_total),
        ('Max_Speed', '%.2f' % unit.max_speed),
        ('Specials', unit.specials),
    )

    for header_name, header_value in header_map:
        if not header_value:
            continue
        if isinstance(header_value, list):
            header_value = ' '.join(header_value)
        header_str = "{header_name:<16} {{ {header_value} }}\n".format(
            header_name=header_name, header_value=header_value)
        fobj.write(header_str)


def _write_all_sections(unit, fobj):
    """
    Immediately following the headers are the unit's sections. This includes
    the section name, armor/internal levels, and crit contents.

    :param btmux_template_io.unit.BTMuxUnit unit: The unit instance to write.
    :param fobj: A file-like object.
    """

    for section_name, section_data in unit.sections.items():
        _write_section_start(section_name, fobj)
        _write_section_values(section_data, fobj)
        _write_section_crits(section_data, fobj)


def _write_section_start(section_name, fobj):
    """
    Write the beginning of the section. Currently just the name.
    :param str section_name: The name of the section
    :param fobj: A file-like object.
    """

    fobj.write(string.capwords(section_name, '_') + '\n')


def _write_section_values(section_data, fobj):
    """
    Writes the section armor/internal/rear/config values.

    :param dict section_data: The raw section data from the BTMuxUnit.
    :param fobj: A file-like object.
    """

    # Order is significant.
    section_dict = OrderedDict()
    section_dict['Armor'] = section_data.get('armor')
    section_dict['Internals'] = section_data.get('internals')
    section_dict['Rear'] = section_data.get('rear')
    section_dict['Config'] = section_data.get('config')

    for name, value in section_dict.items():
        if not value:
            continue
        val_str = "  {name:<14} {{ {value} }}\n".format(
            name=name, value=value)
        fobj.write(val_str)


def _write_section_crits(section_data, fobj):
    """
    After the section values come the crit contents. They look something like::

        CRIT_1		  { ShoulderOrHip - - }

    Go through our section data dict and spit out the properly formed
    crit entries. Some weapons span multiple crits, so we have to handle that
    case as well::

        CRIT_9-10		  { IS.SRM-6 - - }

    :param dict section_data: The raw section data from the BTMuxUnit.
    :param fobj: A file-like object.
    """

    for crit in section_data['crits']:
        crits, crit_contents = crit
        first_crit = crits[0]
        last_crit = crits[-1]
        if first_crit == last_crit:
            crit_name = 'CRIT_%d' % first_crit
        else:
            crit_name = 'CRIT_%d-%d' % (first_crit, last_crit)
        _write_crit(crit_name, crit_contents, fobj)


def _write_crit(crit_name, crit_contents, fobj):
    """
    At this point we have a crit name and a crit contents dict that contains
    the part name and some config values for it. Write the crit line.

    :param str crit_name: Name of the crit. This is ``CRIT_<slotRange>``.
    :param dict crit_contents: Contents of the crit, plus some config values.
    :param fobj: A file-like object.
    """

    part = crit_contents['name']
    ammo_count = crit_contents['ammo_count'] or '-'
    flags = crit_contents['flags'] or '-'

    val_str = "    {crit_name:<12} {{ {part} {ammo_count} {flags} }}\n".format(
        crit_name=crit_name, part=part, ammo_count=ammo_count, flags=flags)
    fobj.write(val_str)
