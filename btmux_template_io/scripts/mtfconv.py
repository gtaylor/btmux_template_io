#!/usr/bin/env python
"""
Converts MTF template files to BTMux.
"""

import click
from btmux_template_io.parsers import mtf
from btmux_template_io.writer import write_to_file

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('input', type=click.File('rb'), nargs=1)
@click.argument('output', type=click.File('wb'))
def convert(input, output):
    """Converts an MTF file (input) to a BTMux mech file (output)."""

    unit = mtf.parse_from_string(input.read())
    write_to_file(unit, output)

if __name__ == '__main__':
    convert()
