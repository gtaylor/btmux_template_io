#!/usr/bin/env python
"""
Converts MTF template files to BTMux.
"""

import click
from btmux_template_io.parsers import mtf
from btmux_template_io.writer import write_to_file

@click.command()
@click.argument('input', type=click.File('rb'), nargs=-1)
@click.argument('output', type=click.File('wb'))
def convert(input, output):

    for fobj in input:
        unit = mtf.parse_from_string(fobj.read())
        from pprint import pprint
        pprint(unit.sections)
        write_to_file(unit, output)

if __name__ == '__main__':
    convert()
