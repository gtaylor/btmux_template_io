import math
from collections import OrderedDict

from . defines import LIGHT_WEIGHT_CLASS, \
    MEDIUM_WEIGHT_CLASS, HEAVY_WEIGHT_CLASS, ASSAULT_WEIGHT_CLASS


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
        self.manufacturer = None
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
        self.specials = set([])
        self.infantry_specials = set([])
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
    def weapons_payload(self):
        """
        :rtype: dict
        :returns: A dict of weapon payload details.
        """

        weap_dict = {}
        for crits, crit_data in self.crits:
            crit_name = crit_data['name']
            if crit_name[0:3] not in ['IS.', 'CL.']:
                continue
            if crit_name not in weap_dict:
                weap_dict[crit_name] = 1
                continue
            weap_dict[crit_name] += 1
        return weap_dict

    @property
    def ammo_payload(self):
        """
        :rtype: dict
        :returns: A dict of ammo payload details.
        """

        ammo_dict = {}
        for crits, crit_data in self.crits:
            crit_name = crit_data['name']
            if not crit_name.startswith('Ammo'):
                continue
            if crit_name not in ammo_dict:
                ammo_dict[crit_name] = {'tons': 0, 'shots': 0, 'flags': None}
            ammo_dict[crit_name]['tons'] += 1
            ammo_dict[crit_name]['shots'] += crit_data['ammo_count']
            # Lump all of this together for now.
            #ammo_dict[crit_name]['flags'] = crit_data['flags']

        return ammo_dict

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

        return int(self.weight * math.floor(((self.max_speed / 10.75) / 3.0) * 2.0))

    @property
    def walk_mp(self):
        """
        :rtype: int
        :returns: The unit's walk MP.
        """

        return self.engine_size / self.weight

    @property
    def run_mp(self):
        """
        :rtype: int
        :returns: The unit's run MP.
        """

        return int(math.ceil(self.walk_mp * 1.5))

    @property
    def weight_class(self):
        """
        :rtype: str
        :returns: The unit's weight class.
        """

        if self.weight < 40:
            return LIGHT_WEIGHT_CLASS
        elif 40 <= self.weight < 60:
            return MEDIUM_WEIGHT_CLASS
        elif 60 <= self.weight < 80:
            return HEAVY_WEIGHT_CLASS
        else:
            return ASSAULT_WEIGHT_CLASS

    def sort_crits(self):
        """
        If you shuffle around crits, sort them here afterwards to ensure
        correct output.
        """

        for section_name, section_data in self.sections.items():
            section_data['crits'] = sorted(
                section_data['crits'], key=lambda ctuple: ctuple[0][0])

    def print_crits(self):
        """
        Prints a crude representation of the unit's crits for debugging purposes.
        """

        for section_name in self.sections.keys():
            print "========== %s =========" % section_name
            section_crits = self.sections[section_name]['crits']
            for crit in section_crits:
                crit_list, crit_dict = crit
                crit_name = crit_dict['name']
                print section_name, crit_list, crit_name, crit_dict['flags']

    def autoset_firemodes(self):
        """
        Looks through the mech's ammo payload to see if there are any weapons
        that have no standard ammo. If so, auto-set the weapon to fire
        the special ammo.
        """

        ammo_dict = {}
        for crits, crit_data in self.crits:
            crit_name = crit_data['name']
            if not crit_name.startswith('Ammo'):
                continue
            if crit_name not in ammo_dict:
                ammo_dict[crit_name] = {'standard': 0, 'others': []}

            if crit_data['flags']:
                ammo_dict[crit_name]['others'].append(crit_data['flags'])
            else:
                ammo_dict[crit_name]['standard'] += 1

        for ammo_name, ammo_tracker in ammo_dict.items():
            if 'MachineGun' in ammo_name:
                # MGs re-use/abuses the Hotload flag for half ton ammo. Bleh.
                continue
            if ammo_tracker['standard'] == 0 and ammo_tracker['others']:
                weap_name = ammo_name.replace('Ammo_', '')
                # Naively pick the first special ammo type.
                weap_flag = ammo_tracker['others'][0]
                self.change_weapon_firemode(weap_name, weap_flag)

    def change_weapon_firemode(self, weap_name, weap_flag):
        """
        :param str weap_name: The weapon name whose firemode to change. This
            will match all weapons of this name, not just one.
        :param str weap_flag: The firemode flag to set on the weapon.
        """

        for crits, crit_data in self.crits:
            crit_name = crit_data['name']
            if crit_name == weap_name:
                crit_data['flags'] = weap_flag

    def autoset_additional_specials(self):
        """
        There are a few specials that have to be calculated based off of the
        status of certain crits (FlipArms, etc). This will update
        the ``specials`` set attrib accordingly.
        """

        if self.unit_type == 'Mech' and self.unit_move_type == 'Biped':
            imflippinout = True
            for section in ['left_arm', 'right_arm']:
                contents = self.sections[section]['crits'][2:4]
                for _, crit_data in contents:
                    if crit_data['name'] in ['LowerActuator', 'HandOrFootActuator']:
                        imflippinout = False
                        break
            if imflippinout:
                self.specials.add('FlipArms')
            else:
                try:
                    self.specials.remove('FlipArms')
                except KeyError:
                    pass
