"""
Template parser tests.
"""

import os
import unittest
from StringIO import StringIO

from btmux_template_io.parsers import btmux
from btmux_template_io.parsers import mtf
from btmux_template_io.writer import write_to_file


TEST_DIR = os.path.abspath(os.path.dirname(__file__))
BTMUX_SAMPLE_DIR = os.path.join(TEST_DIR, 'btmux_samples')
MTF_SAMPLE_DIR = os.path.join(TEST_DIR, 'mtf_samples')


class BTMuxWriterTests(unittest.TestCase):

    def test_basic_mech_write(self):
        """
        Spot checks some basic mech loading values.
        """

        unit = btmux.parse_from_file(os.path.join(BTMUX_SAMPLE_DIR, 'AS7-D'))
        fobj = StringIO()
        write_to_file(unit, fobj)
        #print fobj.getvalue()
        # TODO: Compare to a golden standard.


class MTFWriterTests(unittest.TestCase):

    def test_basic_mech_write(self):

        unit = mtf.parse_from_file(os.path.join(MTF_SAMPLE_DIR, 'Goliath GOL-1H.mtf'))
        fobj = StringIO()
        write_to_file(unit, fobj)
        #print fobj.getvalue()
        # TODO: Compare to a golden standard.
