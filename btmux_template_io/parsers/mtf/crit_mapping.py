"""
Contains everything needed to map MTF crit names to BTMux.
"""

CRIT_MAP = {
    'Hip': {'name': 'ShoulderOrHip'},
    'Shoulder': {'name': 'ShoulderOrHip'},
    'Upper Arm Actuator': {'name': 'UpperActuator'},
    'Lower Arm Actuator': {'name': 'LowerActuator'},
    'Upper Leg Actuator': {'name': 'UpperActuator'},
    'Lower Leg Actuator': {'name': 'LowerActuator'},
    'Hand Actuator': {'name': 'HandOrFootActuator'},
    'Foot Actuator': {'name': 'HandOrFootActuator'},
    'Heat Sink': {'name': 'HeatSink'},
    'Life Support': {'name': 'LifeSupport'},
    'Sensors': {'name': 'Sensors'},
    'Cockpit': {'name': 'Cockpit'},
    'Fusion Engine': {'name': 'Engine'},
    'Gyro': {'name': 'Gyro'},


    'Medium Laser': {'name': 'IS.MediumLaser'},
    'Medium Laser (R)': {'name': 'IS.MediumLaser', 'flags': 'RearMount'},

    'Autocannon/20': {'name': 'IS.AC/20'},
    'IS Ammo AC/20': {'name': 'Ammo_IS.AC/20'},

    'LRM 20': {'name': 'IS.LRM-20'},
    'IS Ammo LRM-20': {'name': 'Ammo_IS.LRM-20'},

    'SRM 6': {'name': 'IS.SRM-6'},
    'IS Ammo SRM-6': {'name': 'Ammo_IS.SRM-6'},
}
