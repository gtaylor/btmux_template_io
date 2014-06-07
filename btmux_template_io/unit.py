import math
from collections import OrderedDict


class BTMuxUnit(object):
    """
    A representation of a BattletechMUX unit.
    """

    def __init__(self):
        self.name = None
        self.reference = None
        self.unit_type = None
        self.unit_move_type = None
        self.unit_era = None
        self.unit_tro = None
        self.weight = None
        self.cargo_space = 0
        self.cargo_max_ton = 0
        self.battlesuit_total = 0
        self.heatsink_total = 10
        self.computer_level = None
        self.radio_level = None
        self.battle_value = None
        self.tactical_range = None
        self.lrs_range = None
        self.scan_range = None
        self.radio_range = None
        self.radio_type = None
        self.fuel = 0
        self.max_speed = None
        self.jump_speed = None
        self.templater_comment = None
        # NOTE: These only include what was in the template. BTMux calculates
        # a bunch of additional specials at unit load time.
        self.specials = []
        self.infantry_specials = []
        self.sections = OrderedDict()

    def __str__(self):
        return "<BTMuxUnit: %s %s>" % (self.reference, self.name)

    @property
    def crits(self):
        """
        :rtype: generator
        :returns: A generator that goes over all crits in all sections.
        """

        for section_name, section_dict in self.sections.items():
            for crit in section_dict['crits']:
                yield crit

    @property
    def jumpjet_total(self):
        """
        :rtype: int
        :returns: The total number of jumpjet crits.
        """

        jumpjet_counter = 0
        for crit_list, crit_data in self.crits:
            if crit_data['name'] == 'JumpJet':
                jumpjet_counter += 1
        return jumpjet_counter

    @property
    def jumpjet_range(self):
        """
        :rtype: int
        :returns: The jumpjet range of the unit (in hexes).
        """

        if not self.jump_speed:
            return 0
        return int(self.jump_speed / 10)

    @property
    def armor_total(self):
        """
        :rtype: int
        :returns: The total armor point count for the unit.
        """

        if not self.sections:
            return 0

        armor_total = 0
        for section_name, section_dict in self.sections.items():
            armor_total += section_dict.get('armor', 0)

        return armor_total

    @property
    def internals_total(self):
        """
        :rtype: int
        :returns: The total internals point count for the unit.
        """

        if not self.sections:
            return 0

        internals_total = 0
        for section_name, section_dict in self.sections.items():
            internals_total += section_dict.get('internals', 0)

        return internals_total

    @property
    def engine_size(self):
        """
        :rtype: int
        :returns: The unit's engine size rating.
        """

        return self.weight * math.floor(((self.max_speed / 10.75) / 3.0) * 2.0)
