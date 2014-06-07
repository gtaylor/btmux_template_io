"""
Template parser tests.
"""

import os
import unittest

from btmux_template_io.parsers.btmux import parse_from_file


TEST_DIR = os.path.abspath(os.path.dirname(__file__))
SAMPLE_DIR = os.path.join(TEST_DIR, 'btmux_samples')


class BasicParserTests(unittest.TestCase):

    def test_invalid_load(self):
        """
        Attempt to parse a non-existent file.
        """

        self.assertRaises(IOError, parse_from_file, 'bogus_file')

    def test_basic_mech_load(self):
        """
        Spot checks some basic mech loading values.
        """

        unit = parse_from_file(os.path.join(SAMPLE_DIR, 'MAD-9M'))
        self.assertEqual(unit.reference, 'MAD-9M')
        self.assertEqual(unit.unit_type, 'Mech')
        self.assertEqual(unit.heatsink_total, 32)
        mech_sections = {
            'left_arm', 'right_arm', 'left_torso', 'right_torso',
            'center_torso', 'left_leg', 'right_leg', 'head',
        }
        parsed_sections = set(unit.sections.keys())
        # All sections listed above should be in the loaded unit obj,
        # so the result should be an empty set.
        self.assertEqual(mech_sections - parsed_sections, set([]))
        mech_specials = {
            'DoubleHS', 'FerroFibrous_Tech', 'XLEngine_Tech', 'ECM',
            'Searchlight'}
        parsed_specials = set(unit.specials)
        self.assertEqual(mech_specials - parsed_specials, set([]))

    def test_spammy_load(self):
        """
        Go through our samples directory and make sure everything loads
        without errors.
        """

        SPAM_DIR = '/Users/gtaylor/workspace/btmux/game/mechs'
        for template_file in os.listdir(SPAM_DIR):
            full_path = os.path.join(SPAM_DIR, template_file)
            if not os.path.isfile(full_path):
                continue
            #print template_file
            parse_from_file(full_path)


class BTMuxUnitTests(unittest.TestCase):
    """
    Tests some of the convenience methods/properties on BTMuxUnit.
    """

    def test_armor_total(self):
        """
        Tests the armor point counting property.
        """

        unit = parse_from_file(os.path.join(SAMPLE_DIR, 'MAD-9M'))
        self.assertEqual(unit.armor_total, 197)

    def test_internals_total(self):
        """
        Tests the internals point counting property.
        """

        unit = parse_from_file(os.path.join(SAMPLE_DIR, 'MAD-9M'))
        self.assertEqual(unit.internals_total, 114)

    def test_engine_rating_calc(self):
        """
        Tests the calculation of engine ratings.
        """

        unit = parse_from_file(os.path.join(SAMPLE_DIR, 'MAD-9M'))
        self.assertEqual(unit.engine_size, 300)

    def test_jumpjet_stuff(self):
        """
        Tests the jumpjet counting and range calculations.
        """

        unit = parse_from_file(os.path.join(SAMPLE_DIR, 'JR7-D'))
        self.assertEqual(unit.jumpjet_total, 3)
        self.assertEqual(unit.jumpjet_range, 5)
