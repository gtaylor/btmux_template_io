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
    'Ferro-Fibrous': {'name': 'FerroFibrous', 'add_special': 'FerroFibrous_Tech'},

    'ISGuardianECM': {'name': 'Ecm', 'add_special': 'ECM'},
    'ISCASE': {'name': 'CASE'},
    'Jump Jet': {'name': 'JumpJet'},
    'Hatchet': {'name': 'Axe'},

    'Medium Laser': {'name': 'IS.MediumLaser'},
    'Medium Laser (R)': {'name': 'IS.MediumLaser', 'flags': 'RearMount'},
    'PPC': {'name': 'IS.PPC'},
    'ISERMediumLaser': {'name': 'IS.ERMediumLaser'},

    'Machine Gun': {'name': 'IS.MachineGun'},
    'IS Ammo MG - Full': {'name': 'Ammo_IS.MachineGun'},
    'Autocannon/20': {'name': 'IS.AC/20'},
    'IS Ammo AC/20': {'name': 'Ammo_IS.AC/20'},

    # TODO: Fix crit combining with GOL-1H
    'LRM 10': {'name': 'IS.LRM-10'},
    'IS Ammo LRM-10': {'name': 'Ammo_IS.LRM-10'},
    'LRM 20': {'name': 'IS.LRM-20'},
    'IS Ammo LRM-20': {'name': 'Ammo_IS.LRM-20'},

    'SRM 6': {'name': 'IS.SRM-6'},
    'IS Ammo SRM-6': {'name': 'Ammo_IS.SRM-6'},

    'ISLBXAC20': {'name': 'IS.LB20-XAC'},
    'ISLBXAC20 CL Ammo': {'name': 'Ammo_IS.LB20-XAC', 'flags': 'LBX/Cluster'},
    'ISLBXAC20 Ammo': {'name': 'Ammo_IS.LB20-XAC'},
}
