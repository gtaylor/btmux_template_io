"""
Dicts that map armor locations in MTF to section names in BTMux.
"""

BIPED_ARMOR_MAP = (
    ('LA Armor', 'left_arm'),
    ('RA Armor', 'right_arm'),
    ('LL Armor', 'left_leg'),
    ('RL Armor', 'right_leg'),
    ('LT Armor', 'left_torso'),
    ('RT Armor', 'right_torso'),
    ('CT Armor', 'center_torso'),
    ('HD Armor', 'head'),
)

QUAD_ARMOR_MAP = (
    ('FLL Armor', 'front_left_leg'),
    ('FRL Armor', 'front_right_leg'),
    ('LT Armor', 'left_torso'),
    ('RT Armor', 'right_torso'),
    ('CT Armor', 'center_torso'),
    ('RLL Armor', 'rear_left_leg'),
    ('RRL Armor', 'rear_right_leg'),
    ('HD Armor', 'head'),
)

REAR_ARMOR_MAP = (
    ('RTL Armor', 'left_torso'),
    ('RTR Armor', 'right_torso'),
    ('RTC Armor', 'center_torso'),
)
