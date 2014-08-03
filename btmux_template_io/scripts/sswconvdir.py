#!/usr/bin/env python
import os

import click
from btmux_template_io.parsers import ssw
from btmux_template_io.writer import write_to_file

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('indir', type=click.Path(exists=True), nargs=1)
@click.argument('outdir', type=click.Path(exists=True), nargs=1)
def convert(indir, outdir):
    """Converts an entire directory of MTF files to BTMux templates.

    \b
    Arguments:\b
    * indir: The directory full of SSW files to convert\b
    * outdir: The BTMux mechs directory to write the converted files to
    """

    print "=" * 80
    print "SSW dir:", indir
    print "BTMux dir:", outdir
    print "-" * 80

    for template_file in os.listdir(indir):
        if template_file.startswith('.'):
            continue
        if template_file.endswith('.ssi'):
            continue
        full_path = os.path.join(indir, template_file)
        if not os.path.isfile(full_path):
            continue

        print "  ", template_file

        in_fobj = open(full_path)
        unit = ssw.parse_from_string(in_fobj.read())
        in_fobj.close()

        write_path = os.path.join(outdir, unit.reference)
        out_fobj = open(write_path, 'wb')
        write_to_file(unit, out_fobj)
        out_fobj.close()

    print "=" * 80

if __name__ == '__main__':
    convert()
