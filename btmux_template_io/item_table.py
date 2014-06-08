"""
Master table of crits. Ammo, actuators, systems, weapons, etc.
"""

ITEM_TABLE = {
    'ShoulderOrHip': {},
    'UpperActuator': {},
    'LowerActuator': {},
    'HandOrFootActuator': {},
    'HeatSink': {},
    'LifeSupport': {},
    'Sensors': {},
    'Cockpit': {},
    'Engine': {},
    'Gyro': {},

    'IS.MediumLaser': {},

    'IS.AC/20': {'crits': 10},
    'Ammo_IS.AC/20': {'ammo_count': 5},

    'IS.SRM-6': {'crits': 2},
    'Ammo_IS.SRM-6': {'ammo_count': 15},

    'IS.LRM-20': {'crits': 5},
    'Ammo_IS.LRM-20': {'ammo_count': 6},
}
