"""
Template parser tests.
"""

import os
from pprint import pprint
import unittest

from btmux_template_io.parsers import btmux
from btmux_template_io.parsers import ssw


TEST_DIR = os.path.abspath(os.path.dirname(__file__))
BTMUX_SAMPLE_DIR = os.path.join(TEST_DIR, 'btmux_samples')
SSW_SAMPLE_DIR = '/Users/gtaylor/workspace/sos_units/mechs'


class SSWParserTests(unittest.TestCase):

    def _load_sample(self, path):
        return ssw.parse_from_file(os.path.join(SSW_SAMPLE_DIR, path))

    def test_basic_mech_load(self):
        """
        Spot checks some basic mech loading values.
        """

        #self._load_sample('Nova NVA-1.ssw')
        # Jumpjets
        #self._load_sample('Ashman ASH-1.ssw')
        # TSM
        #unit = self._load_sample('Takam TAK-4M.ssw')
        # Ammo
        #unit = self._load_sample('Orcus ORC-1.ssw')
        # Artemis
        unit = self._load_sample('Porcupine YSR-2.ssw')
        #pprint(unit.sections)

    def test_spammy_load(self):
        """
        Go through our samples directory and make sure everything loads
        without errors.
        """

        for template_file in os.listdir(SSW_SAMPLE_DIR):
            if template_file.startswith('.'):
                continue
            elif template_file.endswith('.ssi'):
                continue
            full_path = os.path.join(SSW_SAMPLE_DIR, template_file)
            if not os.path.isfile(full_path):
                continue
            print template_file
            self._load_sample(full_path)


class BTMuxParserTests(unittest.TestCase):

    def _load_sample(self, path):
        return btmux.parse_from_file(os.path.join(BTMUX_SAMPLE_DIR, path))

    def test_invalid_load(self):
        """
        Attempt to parse a non-existent file.
        """

        self.assertRaises(IOError, self._load_sample, 'bogus_file')

    def test_basic_mech_load(self):
        """
        Spot checks some basic mech loading values.
        """

        unit = self._load_sample('MAD-9M')
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

        self.skipTest('Temporary')

        SPAM_DIR = '/Users/gtaylor/workspace/btmux/game/mechs'
        for template_file in os.listdir(SPAM_DIR):
            full_path = os.path.join(SPAM_DIR, template_file)
            if not os.path.isfile(full_path):
                continue
            #print template_file
            self._load_sample(full_path)

    def test_armor_total(self):
        """
        Tests the armor point counting property.
        """

        unit = self._load_sample('MAD-9M')
        self.assertEqual(unit.armor_total, 197)

    def test_internals_total(self):
        """
        Tests the internals point counting property.
        """

        unit = self._load_sample('MAD-9M')
        self.assertEqual(unit.internals_total, 114)

    def test_engine_rating_calc(self):
        """
        Tests the calculation of engine ratings.
        """

        unit = self._load_sample('MAD-9M')
        self.assertEqual(unit.engine_size, 300)

    def test_jumpjet_stuff(self):
        """
        Tests the jumpjet counting and range calculations.
        """

        unit = self._load_sample('JR7-D')
        self.assertEqual(unit.jumpjet_total, 3)
        self.assertEqual(unit.jumpjet_range, 5)

    def test_fliparms_autoset(self):
        """
        Tests the autosetting of fliparms special.
        """

        unit = self._load_sample('JR7-D')
        self.assertTrue('FlipArms' in unit.specials)
        unit = self._load_sample('AS7-D')
        self.assertTrue('FlipArms' not in unit.specials)
