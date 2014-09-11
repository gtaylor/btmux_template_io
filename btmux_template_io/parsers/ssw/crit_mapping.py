"""
Contains everything needed to map SSW crit names to BTMux.
"""

PHYSICAL_WEAPON_MAP = {
    'Hatchet': {'name': 'Axe'},
    'Mace': {'name': 'Mace'},
    'Claws': {'name': 'Claw'},
    'Sword': {'name': 'Sword'},
    'Dual Saw': {'name': 'Dual_Saw'},
}

EQUIPMENT_MAP = {
    'Angel ECM': {'name': 'AngelEcm'},
    'Guardian ECM Suite': {'name': 'Ecm'},
    'Improved C3 Computer': {'name': 'C3i'},
    'CASE': {'name': 'CASE'},
    'Bloodhound Active Probe': {'name': 'BloodhoundProbe'},
    'Beagle Active Probe': {'name': 'BeagleProbe'},
    'Searchlight': {'name': None, 'add_special': 'SearchLight'},
    'TAG': {'name': 'TAG'},
    'TSM': {'name': 'TripleStrengthMyomer'},
    'MASC': {'name': 'Masc'},
    '(IS) Targeting Computer': {'name': 'TargetingComputer'},
}

WEAPON_AND_AMMO_MAP = {
    'Machine Gun': {'name': 'MachineGun'},
    'Light Machine Gun': {'name': 'LightMachineGun'},
    'Heavy Machine Gun': {'name': 'HeavyMachineGun'},

    'Autocannon/2': {'name': 'AC/2'},
    'AC/2': {'name': 'AC/2'},
    'Autocannon/5': {'name': 'AC/5'},
    'AC/5': {'name': 'AC/5'},
    'Autocannon/10': {'name': 'AC/10'},
    'AC/10': {'name': 'AC/10'},
    'Autocannon/20': {'name': 'AC/20'},
    'AC/20': {'name': 'AC/20'},

    'Rotary AC/2': {'name': 'RotaryAC/2'},
    'Rotary AC/5': {'name': 'RotaryAC/5'},

    'Ultra AC/2': {'name': 'UltraAC/2'},
    'Ultra AC/5': {'name': 'UltraAC/5'},
    'Ultra AC/10': {'name': 'UltraAC/10'},
    'Ultra AC/20': {'name': 'UltraAC/20'},

    'LB 2-X AC': {'name': 'LB2-XAC'},
    'LB 5-X AC': {'name': 'LB5-XAC'},
    'LB 10-X AC': {'name': 'LB10-XAC'},
    'LB 20-X AC': {'name': 'LB20-XAC'},

    'Light AC/2': {'name': 'LightAC/2'},
    'Light AC/5': {'name': 'LightAC/5'},

    'Gauss Rifle': {'name': 'GaussRifle'},
    'Light Gauss Rifle': {'name': 'LightGaussRifle'},
    'Heavy Gauss Rifle': {'name': 'HeavyGaussRifle'},
    'Magshot Gauss Rifle': {'name': 'MagshotGaussRifle'},

    'Small Laser': {'name': 'SmallLaser'},
    'Medium Laser': {'name': 'MediumLaser'},
    'Medium Laser CP': {'name': 'MediumLaser'},
    'Large Laser': {'name': 'LargeLaser'},

    'ER Small Laser': {'name': 'ERSmallLaser'},
    'ER Medium Laser': {'name': 'ERMediumLaser'},
    'ER Large Laser': {'name': 'ERLargeLaser'},

    'Small Pulse Laser': {'name': 'SmallPulseLaser'},
    'Medium Pulse Laser': {'name': 'MediumPulseLaser'},
    'Large Pulse Laser': {'name': 'LargePulseLaser'},

    'Small X-Pulse Laser': {'name': 'X-SmallPulseLaser'},
    'Medium X-Pulse Laser': {'name': 'X-MediumPulseLaser'},
    'Large X-Pulse Laser': {'name': 'X-LargePulseLaser'},

    'Plasma Rifle': {'name': 'PlasmaRifle'},
    'Flamer': {'name': 'Flamer'},
    'Heavy Flamer': {'name': 'HeavyFlamer'},

    'PPC': {'name': 'PPC'},
    'Light PPC': {'name': 'LightPPC'},
    'Heavy PPC': {'name': 'HeavyPPC'},
    'Snub-Nose PPC': {'name': 'SnubNosedPPC'},
    'ER PPC': {'name': 'ERPPC'},

    'Anti-Missile System': {'name': 'Anti-MissileSystem'},
    'Laser Anti-Missile System': {'name': 'LaserAMS'},

    'SRM-2': {'name': 'SRM-2'},
    'SRM-4': {'name': 'SRM-4'},
    'SRM-6': {'name': 'SRM-6'},

    'Streak SRM-2': {'name': 'StreakSRM-2'},
    'Streak SRM-4': {'name': 'StreakSRM-4'},
    'Streak SRM-6': {'name': 'StreakSRM-6'},

    'MRM-10': {'name': 'MRM-10'},
    'MRM-20': {'name': 'MRM-20'},
    'MRM-30': {'name': 'MRM-30'},
    'MRM-40': {'name': 'MRM-40'},

    'MML-3': {'name': 'MML-3'},
    'MML-5': {'name': 'MML-5'},
    'MML-7': {'name': 'MML-7'},
    'MML-9': {'name': 'MML-9'},

    'LRM-5': {'name': 'LRM-5'},
    'LRM-10': {'name': 'LRM-10'},
    'LRM-15': {'name': 'LRM-15'},
    'LRM-20': {'name': 'LRM-20'},

    'Extended LRM-5': {'name': 'ELRM-5'},
    'ELRM-5': {'name': 'ELRM-5'},
    'Extended LRM-10': {'name': 'ELRM-10'},
    'ELRM-10': {'name': 'ELRM-10'},
    'Extended LRM-15': {'name': 'ELRM-15'},
    'ELRM-15': {'name': 'ELRM-15'},
    'Extended LRM-20': {'name': 'ELRM-20'},
    'ELRM-20': {'name': 'ELRM-20'},

    'Rocket Launcher 10': {'name': 'RL-10', 'flags': 'OneShot'},
    'Rocket Launcher 15': {'name': 'RL-15', 'flags': 'OneShot'},
    'Rocket Launcher 20': {'name': 'RL-20', 'flags': 'OneShot'},

    'Thunderbolt-5': {'name': 'Thunderbolt-5'},
    'Thunderbolt-10': {'name': 'Thunderbolt-10'},
    'Thunderbolt-15': {'name': 'Thunderbolt-15'},
    'Thunderbolt-20': {'name': 'Thunderbolt-20'},
}

AMMO_FLAG_MAPPING = {
    'Cluster': {'flags': 'LBX/Cluster'},
    'Slug': {'flags': None},
    'Precision': {'flags': 'Precision'},
    'Swarm': {'flags': 'Swarm'},
    'Swarm-I': {'flags': 'Swarm1'},
    '1/2': {'flags': 'Halfton'},
    'Inferno': {'flags': 'Inferno'},
    'Artemis IV Capable': {'flags': 'Artemis/Mine'},
    # MML
    'LRM': {'flags': None},
    'SRM': {'flags': None, 'ammo_count': 13},
    'Semi-Guided': {'flags': 'Sguided'},
}
