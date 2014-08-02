"""
Dicts that map armor locations in MTF to section names in BTMux.
"""

MECH_ARMOR_MAP = {
    'la': {'Biped': 'left_arm', 'Quad': 'front_left_leg'},
    'ra': {'Biped': 'right_arm', 'Quad': 'front_right_leg'},
    'll': {'Biped': 'left_leg', 'Quad': 'rear_left_leg'},
    'rl': {'Biped': 'right_leg', 'Quad': 'rear_right_leg'},
    'lt': {'Biped': 'left_torso', 'Quad': 'left_torso'},
    'ltr': {'Biped': 'left_torso', 'Quad': 'left_torso', 'is_rear': True},
    'rt': {'Biped': 'right_torso', 'Quad': 'right_torso'},
    'rtr': {'Biped': 'right_torso', 'Quad': 'right_torso', 'is_rear': True},
    'ct': {'Biped': 'center_torso', 'Quad': 'center_torso'},
    'ctr': {'Biped': 'center_torso', 'Quad': 'center_torso', 'is_rear': True},
    'hd': {'Biped': 'head', 'Quad': 'head'},
}
