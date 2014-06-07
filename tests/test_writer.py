"""
Template parser tests.
"""

import os
import unittest
from StringIO import StringIO

from btmux_template_io.parser import parse_from_file
from btmux_template_io.writer import write_to_file


TEST_DIR = os.path.abspath(os.path.dirname(__file__))
SAMPLE_DIR = os.path.join(TEST_DIR, 'btmux_samples')


class BasicWriterTests(unittest.TestCase):

    def test_basic_mech_write(self):
        """
        Spot checks some basic mech loading values.
        """

        unit = parse_from_file(os.path.join(SAMPLE_DIR, 'AS7-D'))
        fobj = StringIO()
        write_to_file(unit, fobj)
        #print fobj.getvalue()
        # TODO: Compare to a golden standard.
