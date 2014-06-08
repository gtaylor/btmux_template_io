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
    'Engine': {'crits': 3},
    'Gyro': {'crits': 4},
    'FerroFibrous': {},

    'Ecm': {'crits': 2},
    'CASE': {},
    'JumpJet': {},
    'Axe': {'crits': 3},

    'IS.MediumLaser': {},
    'IS.PPC': {'crits': 3},
    'IS.ERMediumLaser': {},

    'IS.MachineGun': {},
    'Ammo_IS.MachineGun': {'ammo_count': 200},
    'IS.AC/20': {'crits': 10},
    'Ammo_IS.AC/20': {'ammo_count': 5},

    'IS.LB20-XAC': {'crits': 6},
    'Ammo_IS.LB20-XAC': {'ammo_count': 10},

    'IS.SRM-6': {'crits': 2},
    'Ammo_IS.SRM-6': {'ammo_count': 15},

    'IS.LRM-10': {'crits': 2},
    'Ammo_IS.LRM-10': {'ammo_count': 12},
    'IS.LRM-20': {'crits': 5},
    'Ammo_IS.LRM-20': {'ammo_count': 6},
}
