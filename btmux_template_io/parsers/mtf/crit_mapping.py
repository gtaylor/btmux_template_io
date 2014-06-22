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
    'Engine': {'name': 'Engine'},
    'Fusion Engine': {'name': 'Engine'},
    'Gyro': {'name': 'Gyro'},
    'Ferro-Fibrous': {'name': 'FerroFibrous'},
    'IS Ferro-Fibrous': {'name': 'FerroFibrous'},
    'CL Ferro-Fibrous': {'name': 'FerroFibrous'},
    'Clan Ferro-Fibrous': {'name': 'FerroFibrous'},
    'Heavy Ferro-Fibrous': {'name': 'HvyFerroFibrous'},
    'Light Ferro-Fibrous': {'name': 'LtFerroFibrous'},
    'IS Light Ferro-Fibrous': {'name': 'LtFerroFibrous'},
    'Stealth Armor': {'name': 'StealthArmor'},
    'Stealth': {'name': 'StealthArmor'},
    'Endo Steel': {'name': 'EndoSteel'},
    'Endo-Steel': {'name': 'EndoSteel'},
    'IS Endo-Steel': {'name': 'EndoSteel'},
    'IS Endo Steel': {'name': 'EndoSteel'},
    'Clan Endo-Steel': {'name': 'EndoSteel'},
    'ISDoubleHeatSink': {'name': 'HeatSink'},
    'CLDouble Heat Sink': {'name': 'HeatSink'},
    'CLDoubleHeatSink': {'name': 'HeatSink'},
    'ISDouble Heat Sink': {'name': 'HeatSink'},
    'ISCollapsibleCommandModule': {'name': None},
    'Communications Equipment (2 ton)': {'name': None},
    'TSM': {'name': 'TripleStrengthMyomer'},
    'Triple Strength Myomer': {'name': 'TripleStrengthMyomer'},
    'ISTargeting Computer': {'name': 'TargetingComputer'},
    'CLTargeting Computer': {'name': 'TargetingComputer'},
    'ISTAG': {'name': 'TAG'},
    'CLTAG': {'name': 'TAG'},
    'ISC3SlaveUnit': {'name': 'C3Slave'},
    'ISC3MasterComputer': {'name': 'C3Master'},
    'ISC3MasterUnit': {'name': 'C3Master'},
    'ISImprovedC3CPU': {'name': 'C3i'},
    'ISC3iUnit': {'name': 'C3i'},

    'ISElectronicWarfareEquipment': {'name': 'Ecm'},
    'ISGuardianECM': {'name': 'Ecm'},
    'ISGuardianECMSuite': {'name': 'Ecm'},
    'ISAngelECMSuite': {'name': 'AngelEcm'},
    'CLAngelECMSuite': {'name': 'AngelEcm'},
    'CLECMSuite': {'name': 'Ecm'},
    'ISArtemisIV': {'name': 'ArtemisIV'},
    'CLArtemisIV': {'name': 'ArtemisIV'},
    'ISCASE': {'name': 'CASE'},
    'CLCASEII': {'name': 'CASE'},
    'CLActiveProbe': {'name': 'BeagleProbe'},
    'CLLightActiveProbe': {'name': 'BeagleProbe', 'add_special': 'LightBAP'},
    'ISBeagleActiveProbe': {'name': 'BeagleProbe'},
    'BeagleActiveProbe': {'name': 'BeagleProbe'},
    'BloodhoundActiveProbe': {'name': 'BloodhoundProbe'},
    'ISMASC': {'name': 'Masc'},
    'CLMASC': {'name': 'Masc'},
    'Jump Jet': {'name': 'JumpJet'},
    'ImprovedJump Jet': {'name': 'JumpJet', 'add_special': 'ImprovedJJ_Tech'},
    'Improved Jump Jet': {'name': 'JumpJet', 'add_special': 'ImprovedJJ_Tech'},
    'Mek Null Signature System': {'name': 'NullSig_Device'},

    'Claw': {'name': 'Claw'},
    'ISClaw': {'name': 'Claw'},
    'Hatchet': {'name': 'Axe'},
    'ISHatchet': {'name': 'Axe'},
    'Mace': {'name': 'Mace'},
    'ISMace': {'name': 'Mace'},
    'Sword': {'name': 'Sword'},
    'ISSword': {'name': 'Sword'},

    'ISNarcBeacon': {'name': 'IS.NarcBeacon'},
    'ISNarc Pods': {'name': 'Ammo_IS.NarcBeacon'},
    'ISiNarc Pods': {'name': 'IS.iNarcBeacon'},
    'ISImprovedNarc': {'name': 'IS.iNarcBeacon'},
    'IS Ammo iNarc': {'name': 'Ammo_IS.iNarcBeacon'},

    'CLNarcBeacon': {'name': 'CL.NarcBeacon'},
    'CLNarc Pods': {'name': 'Ammo_CL.NarcBeacon'},

    'ISAntiMissileSystem': {'name': 'IS.Anti-MissileSystem'},
    'ISAMS Ammo': {'name': 'Ammo_IS.Anti-MissileSystem'},
    'IS AMS Ammo': {'name': 'Ammo_IS.Anti-MissileSystem'},

    'CLAntiMissileSystem': {'name': 'CL.Anti-MissileSystem'},
    'Clan AMS Ammo': {'name': 'Ammo_CL.Anti-MissileSystem'},
    'CLAMS Ammo': {'name': 'Ammo_CL.Anti-MissileSystem'},

    'IS Coolant Pod': {'name': 'IS.CoolantGun'},

    'ISSmallLaser': {'name': 'IS.SmallLaser'},
    'ISSmallLaser (R)': {'name': 'IS.SmallLaser', 'flags': 'RearMount'},
    'Small Laser': {'name': 'IS.SmallLaser'},
    'Small Laser (R)': {'name': 'IS.SmallLaser', 'flags': 'RearMount'},
    'ISMediumLaser': {'name': 'IS.MediumLaser'},
    'ISMediumLaser (R)': {'name': 'IS.MediumLaser', 'flags': 'RearMount'},
    'Medium Laser': {'name': 'IS.MediumLaser'},
    'Medium Laser (R)': {'name': 'IS.MediumLaser', 'flags': 'RearMount'},
    'ISLargeLaser': {'name': 'IS.LargeLaser'},
    'ISLargeLaser (R)': {'name': 'IS.LargeLaser', 'flags': 'RearMount'},
    'Large Laser': {'name': 'IS.LargeLaser'},
    'Large Laser (R)': {'name': 'IS.LargeLaser', 'flags': 'RearMount'},

    'ISPPC': {'name': 'IS.PPC'},
    'PPC': {'name': 'IS.PPC'},
    'Particle Cannon': {'name': 'IS.PPC'},
    'ISSNPPC': {'name': 'IS.SnubNosedPPC'},
    'Light PPC': {'name': 'IS.LightPPC'},
    'ISLightPPC': {'name': 'IS.LightPPC'},
    'Heavy PPC': {'name': 'IS.HeavyPPC'},
    'ISHeavyPPC': {'name': 'IS.HeavyPPC'},

    'ISSmallPulseLaser': {'name': 'IS.SmallPulseLaser'},
    'ISSmallPulseLaser (R)': {'name': 'IS.SmallPulseLaser', 'flags': 'RearMount'},
    'ISMediumPulseLaser': {'name': 'IS.MediumPulseLaser'},
    'ISMediumPulseLaser (R)': {'name': 'IS.MediumPulseLaser', 'flags': 'RearMount'},
    'ISLargePulseLaser': {'name': 'IS.LargePulseLaser'},
    'ISLargePulseLaser (R)': {'name': 'IS.LargePulseLaser', 'flags': 'RearMount'},

    'ISSmallXPulseLaser': {'name': 'IS.X-SmallPulseLaser'},
    'ISMediumXPulseLaser': {'name': 'IS.X-MediumPulseLaser'},
    'ISLargeXPulseLaser': {'name': 'IS.X-LargePulseLaser'},

    'CLSmallPulseLaser': {'name': 'CL.SmallPulseLaser'},
    'CLMediumPulseLaser': {'name': 'CL.MediumPulseLaser'},
    'CLLargePulseLaser': {'name': 'CL.LargePulseLaser'},

    'ISERSmallLaser': {'name': 'IS.ERSmallLaser'},
    'ISERSmallLaser (R)': {'name': 'IS.ERSmallLaser', 'flags': 'RearMount'},
    'ISERMediumLaser': {'name': 'IS.ERMediumLaser'},
    'ISERMediumLaser (R)': {'name': 'IS.ERMediumLaser', 'flags': 'RearMount'},
    'ISERLargeLaser': {'name': 'IS.ERLargeLaser'},
    'ISERPPC': {'name': 'IS.ERPPC'},

    'ISPlasmaRifle': {'name': 'IS.PlasmaRifle'},
    'ISPlasmaRifleAmmo': {'name': 'Ammo_IS.PlasmaRifle'},
    'ISPlasmaRifle Ammo': {'name': 'Ammo_IS.PlasmaRifle'},

    'CLERMicroLaser': {'name': 'CL.ERMicroLaser'},
    'CLERMicroLaser (R)': {'name': 'CL.ERMicroLaser', 'flags': 'RearMount'},

    'CLMicroPulseLaser': {'name': 'CL.MicroPulseLaser'},

    'CLERSmallLaser': {'name': 'CL.ERSmallLaser'},
    'CLERSmallLaser (R)': {'name': 'CL.ERSmallLaser', 'flags': 'RearMount'},
    'CLERMediumLaser': {'name': 'CL.ERMediumLaser'},
    'CLERMediumLaser (R)': {'name': 'CL.ERMediumLaser', 'flags': 'RearMount'},
    'CLERLargeLaser': {'name': 'CL.ERLargeLaser'},
    'CLERLargeLaser (R)': {'name': 'CL.ERLargeLaser', 'flags': 'RearMount'},
    'CLERPPC': {'name': 'CL.ERPPC'},

    'CLERSmallPulseLaser': {'name': 'CL.ERSmallPulseLaser'},
    'CLERSmallPulseLaser (R)': {'name': 'CL.ERSmallPulseLaser', 'flags': 'RearMount'},
    'CLERMediumPulseLaser': {'name': 'CL.ERMediumPulseLaser'},
    'CLERMediumPulseLaser (R)': {'name': 'CL.ERMediumPulseLaser', 'flags': 'RearMount'},
    'CLERLargePulseLaser': {'name': 'CL.ERLargePulseLaser'},
    'CLERLargePulseLaser (R)': {'name': 'CL.ERLargePulseLaser', 'flags': 'RearMount'},

    'CLHeavySmallLaser': {'name': 'CL.HeavySmallLaser'},
    'CLHeavySmallLaser (R)': {'name': 'CL.HeavySmallLaser', 'flags': 'RearMount'},
    'CLHeavyMediumLaser': {'name': 'CL.HeavyMediumLaser'},
    'CLHeavyMediumLaser (R)': {'name': 'CL.HeavyMediumLaser', 'flags': 'RearMount'},
    'CLHeavyLargeLaser': {'name': 'CL.HeavyLargeLaser'},
    'CLHeavyLargeLaser (R)': {'name': 'CL.HeavyLargeLaser', 'flags': 'RearMount'},

    'Flamer': {'name': 'IS.Flamer'},
    'Flamer (R)': {'name': 'IS.Flamer', 'flags': 'RearMount'},
    'ISFlamer': {'name': 'IS.Flamer'},
    'ISFlamer (R)': {'name': 'IS.Flamer', 'flags': 'RearMount'},
    'Machine Gun': {'name': 'IS.MachineGun'},
    'Machine Gun (R)': {'name': 'IS.MachineGun', 'flags': 'RearMount'},
    'ISMachine Gun': {'name': 'IS.MachineGun'},
    'ISMachine Gun (R)': {'name': 'IS.MachineGun', 'flags': 'RearMount'},
    'IS Ammo MG - Full': {'name': 'Ammo_IS.MachineGun'},
    'ISMG Ammo (200)': {'name': 'Ammo_IS.MachineGun'},
    'IS Machine Gun Ammo - Half': {'name': 'Ammo_IS.MachineGun', 'ammo_count': 100, 'flags': 'Hotload'},
    'ISMG Ammo (100)': {'name': 'Ammo_IS.MachineGun', 'ammo_count': 100, 'flags': 'Hotload'},

    'CLFlamer': {'name': 'CL.Flamer'},
    'CLFlamer (R)': {'name': 'CL.Flamer', 'flags': 'RearMount'},

    'ISHeavyMG': {'name': 'IS.HeavyMachineGun'},
    'ISHeavyMG Ammo (100)': {'name': 'Ammo_IS.HeavyMachineGun'},
    'ISHeavyMG Ammo (50)': {'name': 'Ammo_IS.HeavyMachineGun', 'ammo_count': 50, 'flags': 'Hotload'},

    'CLLightMG': {'name': 'CL.LightMachineGun'},
    'CLHeavyMG': {'name': 'CL.HeavyMachineGun'},

    'CLMG': {'name': 'CL.MachineGun'},
    'CLMG (R)': {'name': 'CL.MachineGun', 'flags': 'RearMount'},
    'Clan Machine Gun Ammo - Full': {'name': 'Ammo_CL.MachineGun'},
    'CLMG Ammo (200)': {'name': 'Ammo_CL.MachineGun'},
    'Clan Machine Gun Ammo - Half': {'name': 'Ammo_CL.MachineGun', 'ammo_count': 100, 'flags': 'Hotload'},
    'CLMG Ammo (100)': {'name': 'Ammo_CL.MachineGun', 'ammo_count': 100, 'flags': 'Hotload'},

    'Clan Light Machine Gun Ammo - Full': {'name': 'Ammo_CL.LightMachineGun'},
    'Clan Light Machine Gun Ammo - Half': {'name': 'Ammo_CL.LightMachineGun', 'ammo_count': 50, 'flags': 'Hotload'},
    'Clan Heavy Machine Gun Ammo - Full': {'name': 'Ammo_CL.HeavyMachineGun'},
    'Clan Heavy Machine Gun Ammo - Half': {'name': 'Ammo_CL.HeavyMachineGun', 'ammo_count': 50, 'flags': 'Hotload'},

    'Autocannon/2': {'name': 'IS.AC/2'},
    'ISAC2': {'name': 'IS.AC/2'},
    'ISAC2 Ammo': {'name': 'Ammo_IS.AC/2'},
    'IS Ammo AC/2': {'name': 'Ammo_IS.AC/2'},

    'Autocannon/5': {'name': 'IS.AC/5'},
    'ISAC5': {'name': 'IS.AC/5'},
    'ISAC5 Ammo': {'name': 'Ammo_IS.AC/5'},
    'IS Ammo AC/5': {'name': 'Ammo_IS.AC/5'},

    'Autocannon/10': {'name': 'IS.AC/10'},
    'ISAC10': {'name': 'IS.AC/10'},
    'ISAC10 Ammo': {'name': 'Ammo_IS.AC/10'},
    'IS Ammo AC/10': {'name': 'Ammo_IS.AC/10'},

    'Autocannon/20': {'name': 'IS.AC/20'},
    'ISAC20': {'name': 'IS.AC/20'},
    'ISAC20 Ammo': {'name': 'Ammo_IS.AC/20'},
    'IS Ammo AC/20': {'name': 'Ammo_IS.AC/20'},

    'ISRotaryAC2': {'name': 'IS.RotaryAC/2'},
    'ISRotaryAC2 Ammo': {'name': 'Ammo_IS.RotaryAC/2'},
    'ISRotaryAC5': {'name': 'IS.RotaryAC/5'},
    'ISRotaryAC5 Ammo': {'name': 'Ammo_IS.RotaryAC/5'},
    'IS Rotary AC/5 Ammo': {'name': 'Ammo_IS.RotaryAC/5'},

    'CLRotaryAC2': {'name': 'CL.RotaryAC/2'},
    'CLRotaryAC2 Ammo': {'name': 'Ammo_IS.RotaryAC/2'},
    'CLRotaryAC5': {'name': 'CL.RotaryAC/5'},
    'CLRotaryAC5 Ammo': {'name': 'Ammo_IS.RotaryAC/5'},

    'Light Auto Cannon/2': {'name': 'IS.LightAC/2'},
    'ISLAC2': {'name': 'IS.LightAC/2'},
    'ISLAC2 Ammo': {'name': 'Ammo_IS.LightAC/2'},
    'IS Ammo LAC/2': {'name': 'Ammo_IS.LightAC/2'},
    'Light Auto Cannon/5': {'name': 'IS.LightAC/5'},
    'ISLAC5': {'name': 'IS.LightAC/5'},
    'ISLAC5 Ammo': {'name': 'Ammo_IS.LightAC/5'},
    'IS Ammo LAC/5': {'name': 'Ammo_IS.LightAC/5'},

    'ISUltraAC2': {'name': 'IS.UltraAC/2'},
    'IS Ultra AC/2 Ammo': {'name': 'Ammo_IS.UltraAC/2'},
    'ISUltraAC2 Ammo': {'name': 'Ammo_IS.UltraAC/2'},

    'ISUltraAC5': {'name': 'IS.UltraAC/5'},
    'IS Ultra AC/5 Ammo': {'name': 'Ammo_IS.UltraAC/5'},
    'ISUltraAC5 Ammo': {'name': 'Ammo_IS.UltraAC/5'},

    'ISUltraAC10': {'name': 'IS.UltraAC/10'},
    'IS Ultra AC/10 Ammo': {'name': 'Ammo_IS.UltraAC/10'},
    'ISUltraAC10 Ammo': {'name': 'Ammo_IS.UltraAC/10'},

    'ISUltraAC20': {'name': 'IS.UltraAC/20'},
    'IS Ultra AC/20 Ammo': {'name': 'Ammo_IS.UltraAC/20'},
    'ISUltraAC20 Ammo': {'name': 'Ammo_IS.UltraAC/20'},

    'ISMagshotGR': {'name': 'IS.MagshotGaussRifle'},
    'IS Magshot GR Ammo': {'name': 'Ammo_IS.MagshotGaussRifle'},
    'ISMagshotGR Ammo': {'name': 'Ammo_IS.MagshotGaussRifle'},

    'ISGaussRifle': {'name': 'IS.GaussRifle'},
    'ISGauss Ammo': {'name': 'Ammo_IS.GaussRifle'},
    'IS Gauss Ammo': {'name': 'Ammo_IS.GaussRifle'},

    'ISHeavyGaussRifle': {'name': 'IS.HeavyGaussRifle'},
    'ISHeavyGauss Ammo': {'name': 'Ammo_IS.HeavyGaussRifle'},
    'IS Heavy Gauss Rifle Ammo': {'name': 'Ammo_IS.HeavyGaussRifle'},

    'ISLightGaussRifle': {'name': 'IS.LightGaussRifle'},
    'IS Light Gauss Ammo': {'name': 'Ammo_IS.LightGaussRifle'},
    'ISLightGauss Ammo': {'name': 'Ammo_IS.LightGaussRifle'},

    'CLGaussRifle': {'name': 'CL.GaussRifle'},
    'CLGauss Ammo': {'name': 'Ammo_CL.GaussRifle'},
    'Clan Gauss Ammo': {'name': 'Ammo_CL.GaussRifle'},

    'CLUltraAC2': {'name': 'CL.UltraAC/2'},
    'CLUltraAC2 Ammo': {'name': 'Ammo_CL.UltraAC/2'},
    'Clan Ultra AC/2 Ammo': {'name': 'Ammo_CL.UltraAC/2'},
    'CLUltraAC5': {'name': 'CL.UltraAC/5'},
    'CLUltraAC5 Ammo': {'name': 'Ammo_CL.UltraAC/5'},
    'Clan Ultra AC/5 Ammo': {'name': 'Ammo_CL.UltraAC/5'},
    'CLUltraAC10': {'name': 'CL.UltraAC/10'},
    'CLUltraAC10 Ammo': {'name': 'Ammo_CL.UltraAC/10'},
    'Clan Ultra AC/10 Ammo': {'name': 'Ammo_CL.UltraAC/10'},
    'CLUltraAC20': {'name': 'CL.UltraAC/20'},
    'CLUltraAC20 Ammo': {'name': 'Ammo_CL.UltraAC/20'},
    'Clan Ultra AC/20 Ammo': {'name': 'Ammo_CL.UltraAC/20'},

    'RL10': {'name': 'IS.RL-10'},
    'RL15': {'name': 'IS.RL-15'},
    'RL20': {'name': 'IS.RL-20'},

    'MRM 10': {'name': 'IS.MRM-10'},
    'ISMRM10': {'name': 'IS.MRM-10'},
    'ISMRM10 Ammo': {'name': 'Ammo_IS.MRM-10'},
    'IS MRM 10 Ammo': {'name': 'Ammo_IS.MRM-10'},
    'MRM 20': {'name': 'IS.MRM-20'},
    'ISMRM20': {'name': 'IS.MRM-20'},
    'ISMRM20 Ammo': {'name': 'Ammo_IS.MRM-20'},
    'IS MRM 20 Ammo': {'name': 'Ammo_IS.MRM-20'},
    'MRM 30': {'name': 'IS.MRM-30'},
    'ISMRM30': {'name': 'IS.MRM-30'},
    'ISMRM30 Ammo': {'name': 'Ammo_IS.MRM-30'},
    'IS MRM 30 Ammo': {'name': 'Ammo_IS.MRM-30'},
    'MRM 40': {'name': 'IS.MRM-40'},
    'ISMRM40': {'name': 'IS.MRM-40'},
    'ISMRM40 Ammo': {'name': 'Ammo_IS.MRM-40'},
    'IS MRM 40 Ammo': {'name': 'Ammo_IS.MRM-40'},

    'Thunderbolt 5': {'name': 'IS.Thunderbolt-5'},
    'IS Ammo Thunderbolt-5': {'name': 'Ammo_IS.Thunderbolt-5'},
    'Thunderbolt 10': {'name': 'IS.Thunderbolt-10'},
    'IS Ammo Thunderbolt-10': {'name': 'Ammo_IS.Thunderbolt-10'},
    'Thunderbolt 15': {'name': 'IS.Thunderbolt-15'},
    'IS Ammo Thunderbolt-15': {'name': 'Ammo_IS.Thunderbolt-15'},
    'Thunderbolt 20': {'name': 'IS.Thunderbolt-20'},
    'IS Ammo Thunderbolt-20': {'name': 'Ammo_IS.Thunderbolt-20'},

    'LRM 5': {'name': 'IS.LRM-5'},
    'ISLRM5': {'name': 'IS.LRM-5'},
    'IS Ammo LRM-5': {'name': 'Ammo_IS.LRM-5'},
    'ISLRM5 Ammo': {'name': 'Ammo_IS.LRM-5'},
    'ISLRM5 Ammo Artemis-capable': {'name': 'Ammo_IS.LRM-5', 'flags': 'Artemis/Mine'},
    'IS Ammo LRM-5 Artemis-capable': {'name': 'Ammo_IS.LRM-5', 'flags': 'Artemis/Mine'},

    'CLLRM5': {'name': 'CL.LRM-5'},
    'CLLRM5 Ammo': {'name': 'Ammo_CL.LRM-5'},
    'Clan Ammo LRM-5': {'name': 'Ammo_CL.LRM-5'},
    'Clan Ammo LRM-5 (Clan) Artemis-capable': {'name': 'Ammo_CL.LRM-5', 'flags': 'Artemis/Mine'},
    'CLLRM5 Ammo (Clan) Artemis-capable': {'name': 'Ammo_CL.LRM-5', 'flags': 'Artemis/Mine'},
    'CLLRM10': {'name': 'CL.LRM-10'},
    'CLLRM10 Ammo': {'name': 'Ammo_CL.LRM-10'},
    'Clan Ammo LRM-10': {'name': 'Ammo_CL.LRM-10'},
    'Clan Ammo LRM-10 (Clan) Artemis-capable': {'name': 'Ammo_CL.LRM-10', 'flags': 'Artemis/Mine'},
    'CLLRM10 Ammo (Clan) Artemis-capable': {'name': 'Ammo_CL.LRM-10', 'flags': 'Artemis/Mine'},
    'CLLRM15': {'name': 'CL.LRM-15'},
    'CLLRM15 Ammo': {'name': 'Ammo_CL.LRM-15'},
    'Clan Ammo LRM-15': {'name': 'Ammo_CL.LRM-15'},
    'Clan Ammo LRM-15 (Clan) Artemis-capable': {'name': 'Ammo_CL.LRM-15', 'flags': 'Artemis/Mine'},
    'CLLRM15 Ammo (Clan) Artemis-capable': {'name': 'Ammo_CL.LRM-15', 'flags': 'Artemis/Mine'},
    'CLLRM20': {'name': 'CL.LRM-20'},
    'CLLRM20 Ammo': {'name': 'Ammo_CL.LRM-20'},
    'Clan Ammo LRM-20': {'name': 'Ammo_CL.LRM-20'},
    'Clan Ammo LRM-20 (Clan) Artemis-capable': {'name': 'Ammo_CL.LRM-20', 'flags': 'Artemis/Mine'},
    'CLLRM20 Ammo (Clan) Artemis-capable': {'name': 'Ammo_CL.LRM-20', 'flags': 'Artemis/Mine'},

    'LRM 10': {'name': 'IS.LRM-10'},
    'ISLRM10': {'name': 'IS.LRM-10'},
    'IS Ammo LRM-10': {'name': 'Ammo_IS.LRM-10'},
    'ISLRM10 Ammo': {'name': 'Ammo_IS.LRM-10'},
    'ISLRM10 Ammo Artemis-capable': {'name': 'Ammo_IS.LRM-10', 'flags': 'Artemis/Mine'},
    'IS Ammo LRM-10 Artemis-capable': {'name': 'Ammo_IS.LRM-10', 'flags': 'Artemis/Mine'},

    'LRM 15': {'name': 'IS.LRM-15'},
    'ISLRM15': {'name': 'IS.LRM-15'},
    'IS Ammo LRM-15': {'name': 'Ammo_IS.LRM-15'},
    'ISLRM15 Ammo': {'name': 'Ammo_IS.LRM-15'},
    'ISLRM15 Ammo Artemis-capable': {'name': 'Ammo_IS.LRM-15', 'flags': 'Artemis/Mine'},
    'IS Ammo LRM-15 Artemis-capable': {'name': 'Ammo_IS.LRM-15', 'flags': 'Artemis/Mine'},

    'LRM 20': {'name': 'IS.LRM-20'},
    'ISLRM20': {'name': 'IS.LRM-20'},
    'ISLRM20 (R)': {'name': 'IS.LRM-20', 'flags': 'RearMount'},
    'IS Ammo LRM-20': {'name': 'Ammo_IS.LRM-20'},
    'ISLRM20 Ammo': {'name': 'Ammo_IS.LRM-20'},
    'ISLRM20 Ammo Artemis-capable': {'name': 'Ammo_IS.LRM-20', 'flags': 'Artemis/Mine'},
    'IS Ammo LRM-20 Artemis-capable': {'name': 'Ammo_IS.LRM-20', 'flags': 'Artemis/Mine'},

    'ISMML3': {'name': 'IS.MML-3'},
    'ISMML3 SRM Ammo': {'name': 'Ammo_IS.MML-3'},
    'IS Ammo MML-3 SRM': {'name': 'Ammo_IS.MML-3'},
    'IS Ammo MML-3 SRM Artemis-capable': {'name': 'Ammo_IS.MML-3', 'flags': 'Artemis/Mine'},
    'ISMML3 LRM Ammo': {'name': 'Ammo_IS.MML-3', 'ammo_count': 40},
    'IS Ammo MML-3 LRM': {'name': 'Ammo_IS.MML-3', 'ammo_count': 40},
    'IS Ammo MML-3 LRM Artemis-capable': {'name': 'Ammo_IS.MML-3', 'ammo_count': 40, 'flags': 'Artemis/Mine'},
    'ISMML5': {'name': 'IS.MML-5'},
    'ISMML5 SRM Ammo': {'name': 'Ammo_IS.MML-5'},
    'IS Ammo MML-5 SRM': {'name': 'Ammo_IS.MML-5'},
    'IS Ammo MML-5 SRM Artemis-capable': {'name': 'Ammo_IS.MML-5', 'flags': 'Artemis/Mine'},
    'ISMML5 LRM Ammo': {'name': 'Ammo_IS.MML-5', 'ammo_count': 24},
    'IS Ammo MML-5 LRM': {'name': 'Ammo_IS.MML-5', 'ammo_count': 24},
    'IS Ammo MML-5 LRM Artemis-capable': {'name': 'Ammo_IS.MML-5', 'ammo_count': 24, 'flags': 'Artemis/Mine'},
    'ISMML7': {'name': 'IS.MML-7'},
    'ISMML7 SRM Ammo': {'name': 'Ammo_IS.MML-7'},
    'IS Ammo MML-7 SRM': {'name': 'Ammo_IS.MML-7'},
    'IS Ammo MML-7 SRM Artemis-capable': {'name': 'Ammo_IS.MML-7', 'flags': 'Artemis/Mine'},
    'ISMML7 LRM Ammo': {'name': 'Ammo_IS.MML-7', 'ammo_count': 17},
    'IS Ammo MML-7 LRM': {'name': 'Ammo_IS.MML-7', 'ammo_count': 17},
    'IS Ammo MML-7 LRM Artemis-capable': {'name': 'Ammo_IS.MML-7', 'ammo_count': 17, 'flags': 'Artemis/Mine'},
    'ISMML9': {'name': 'IS.MML-9'},
    'ISMML9 SRM Ammo': {'name': 'Ammo_IS.MML-9'},
    'IS Ammo MML-9 SRM': {'name': 'Ammo_IS.MML-9'},
    'IS Ammo MML-9 SRM Artemis-capable': {'name': 'Ammo_IS.MML-9', 'flags': 'Artemis/Mine'},
    'ISMML9 LRM Ammo': {'name': 'Ammo_IS.MML-9', 'ammo_count': 13},
    'IS Ammo MML-9 LRM': {'name': 'Ammo_IS.MML-9', 'ammo_count': 13},
    'IS Ammo MML-9 LRM Artemis-capable': {'name': 'Ammo_IS.MML-9', 'ammo_count': 13, 'flags': 'Artemis/Mine'},

    'CLATM3': {'name': 'CL.ATM-3'},
    'CLATM3 Ammo': {'name': 'Ammo_CL.ATM-3'},
    'Clan Ammo ATM-3': {'name': 'Ammo_CL.ATM-3'},
    'CLATM3 HE Ammo': {'name': 'Ammo_CL.ATM-3', 'flags': 'HighExplosive'},
    'Clan Ammo ATM-3 HE': {'name': 'Ammo_CL.ATM-3', 'flags': 'HighExplosive'},
    # We don't have ER ammo
    'CLATM3 ER Ammo': {'name': 'Ammo_CL.ATM-3'},
    'Clan Ammo ATM-3 ER': {'name': 'Ammo_CL.ATM-3'},
    'CLATM6': {'name': 'CL.ATM-6'},
    'CLATM6 Ammo': {'name': 'Ammo_CL.ATM-6'},
    'Clan Ammo ATM-6': {'name': 'Ammo_CL.ATM-6'},
    'CLATM6 HE Ammo': {'name': 'Ammo_CL.ATM-6', 'flags': 'HighExplosive'},
    'Clan Ammo ATM-6 HE': {'name': 'Ammo_CL.ATM-6', 'flags': 'HighExplosive'},
    'CLATM6 ER Ammo': {'name': 'Ammo_CL.ATM-6'},
    'Clan Ammo ATM-6 ER': {'name': 'Ammo_CL.ATM-6'},
    'CLATM9': {'name': 'CL.ATM-9'},
    'CLATM9 Ammo': {'name': 'Ammo_CL.ATM-9'},
    'Clan Ammo ATM-9': {'name': 'Ammo_CL.ATM-9'},
    'Clan Ammo ATM-9 HE': {'name': 'Ammo_CL.ATM-9', 'flags': 'HighExplosive'},
    'CLATM9 HE Ammo': {'name': 'Ammo_CL.ATM-9', 'flags': 'HighExplosive'},
    'CLATM9 ER Ammo': {'name': 'Ammo_CL.ATM-9'},
    'Clan Ammo ATM-9 ER': {'name': 'Ammo_CL.ATM-9'},
    'CLATM12': {'name': 'CL.ATM-12'},
    'CLATM12 Ammo': {'name': 'Ammo_CL.ATM-12'},
    'Clan Ammo ATM-12': {'name': 'Ammo_CL.ATM-12'},
    'Clan Ammo ATM-12 HE': {'name': 'Ammo_CL.ATM-12', 'flags': 'HighExplosive'},
    'CLATM12 HE Ammo': {'name': 'Ammo_CL.ATM-12', 'flags': 'HighExplosive'},
    'CLATM12 ER Ammo': {'name': 'Ammo_CL.ATM-12'},
    'Clan Ammo ATM-12 ER': {'name': 'Ammo_CL.ATM-12'},

    'SRM 2': {'name': 'IS.SRM-2'},
    'SRM 2 (R)': {'name': 'IS.SRM-2', 'flags': 'RearMount'},
    'ISSRM2': {'name': 'IS.SRM-2'},
    'ISSRM2 Ammo': {'name': 'Ammo_IS.SRM-2'},
    'IS Ammo SRM-2': {'name': 'Ammo_IS.SRM-2'},
    'IS Ammo SRM-2 Narc-capable': {'name': 'Ammo_IS.SRM-2', 'flags': 'Narc/Smoke'},
    'IS Ammo SRM-2 Artemis-capable': {'name': 'Ammo_IS.SRM-2', 'flags': 'Artemis/Mine'},
    'ISSRM2 Ammo Artemis-capable': {'name': 'Ammo_IS.SRM-2', 'flags': 'Artemis/Mine'},
    'SRM 4': {'name': 'IS.SRM-4'},
    'SRM 4 (R)': {'name': 'IS.SRM-4', 'flags': 'RearMount'},
    'ISSRM4': {'name': 'IS.SRM-4'},
    'ISSRM4 Ammo': {'name': 'Ammo_IS.SRM-4'},
    'IS Ammo SRM-4': {'name': 'Ammo_IS.SRM-4'},
    'IS Ammo SRM-4 Narc-capable': {'name': 'Ammo_IS.SRM-4', 'flags': 'Narc/Smoke'},
    'IS Ammo SRM-4 Artemis-capable': {'name': 'Ammo_IS.SRM-4', 'flags': 'Artemis/Mine'},
    'ISSRM4 Ammo Artemis-capable': {'name': 'Ammo_IS.SRM-4', 'flags': 'Artemis/Mine'},
    'SRM 6': {'name': 'IS.SRM-6'},
    'SRM 6 (R)': {'name': 'IS.SRM-6'},
    'ISSRM6': {'name': 'IS.SRM-6'},
    'ISSRM6 Ammo': {'name': 'Ammo_IS.SRM-6'},
    'IS Ammo SRM-6': {'name': 'Ammo_IS.SRM-6'},
    'IS Ammo SRM-6 Narc-capable': {'name': 'Ammo_IS.SRM-6', 'flags': 'Narc/Smoke'},
    'IS Ammo SRM-6 Artemis-capable': {'name': 'Ammo_IS.SRM-6', 'flags': 'Artemis/Mine'},
    'ISSRM6 Ammo Artemis-capable': {'name': 'Ammo_IS.SRM-6', 'flags': 'Artemis/Mine'},

    'CLSRM2': {'name': 'CL.SRM-2'},
    'CLSRM2 Ammo': {'name': 'Ammo_CL.SRM-2'},
    'Clan Ammo SRM-2': {'name': 'Ammo_CL.SRM-2'},
    'Clan Ammo SRM-2 (Clan) Narc-capable': {'name': 'Ammo_CL.SRM-2', 'flags': 'Narc/Smoke'},
    'CLSRM4': {'name': 'CL.SRM-4'},
    'CLSRM4 Ammo': {'name': 'Ammo_CL.SRM-4'},
    'Clan Ammo SRM-4': {'name': 'Ammo_CL.SRM-4'},
    'Clan Ammo SRM-4 (Clan) Narc-capable': {'name': 'Ammo_CL.SRM-4', 'flags': 'Narc/Smoke'},
    'CLSRM6': {'name': 'CL.SRM-6'},
    'CLSRM6 Ammo': {'name': 'Ammo_CL.SRM-6'},
    'Clan Ammo SRM-6 (Clan) Narc-capable': {'name': 'Ammo_CL.SRM-6', 'flags': 'Narc/Smoke'},
    'Clan Ammo SRM-6': {'name': 'Ammo_CL.SRM-6'},

    'CLStreakSRM2 (OS)': {'name': 'CL.StreakSRM-2', 'flags': 'OneShot'},
    'CLStreakSRM4 (OS)': {'name': 'CL.StreakSRM-4', 'flags': 'OneShot'},
    'CLStreakSRM6 (OS)': {'name': 'CL.StreakSRM-6', 'flags': 'OneShot'},

    'ISStreakSRM2': {'name': 'IS.StreakSRM-2'},
    'ISStreakSRM2 (R)': {'name': 'IS.StreakSRM-2', 'flags': 'RearMount'},
    'ISStreakSRM2OS': {'name': 'IS.StreakSRM-2', 'flags': 'OneShot'},
    'ISStreakSRM2 Ammo': {'name': 'Ammo_IS.StreakSRM-2'},
    'IS Streak SRM 2 Ammo': {'name': 'Ammo_IS.StreakSRM-2'},
    'ISStreakSRM4': {'name': 'IS.StreakSRM-4'},
    'ISStreakSRM4 (R)': {'name': 'IS.StreakSRM-4', 'flags': 'RearMount'},
    'ISStreakSRM4OS': {'name': 'IS.StreakSRM-4', 'flags': 'OneShot'},
    'ISStreakSRM4 Ammo': {'name': 'Ammo_IS.StreakSRM-4'},
    'IS Streak SRM 4 Ammo': {'name': 'Ammo_IS.StreakSRM-4'},
    'ISStreakSRM6': {'name': 'IS.StreakSRM-6'},
    'ISStreakSRM6 (R)': {'name': 'IS.StreakSRM-6', 'flags': 'RearMount'},
    'ISStreakSRM6OS': {'name': 'IS.StreakSRM-6', 'flags': 'OneShot'},
    'ISStreakSRM6 Ammo': {'name': 'Ammo_IS.StreakSRM-6'},
    'IS Streak SRM 6 Ammo': {'name': 'Ammo_IS.StreakSRM-6'},

    'CLStreakSRM2': {'name': 'CL.StreakSRM-2'},
    'CLStreakSRM2 Ammo': {'name': 'Ammo_CL.StreakSRM-2'},
    'Clan Streak SRM 2 Ammo': {'name': 'Ammo_CL.StreakSRM-2'},
    'CLStreakSRM4': {'name': 'CL.StreakSRM-4'},
    'CLStreakSRM4 Ammo': {'name': 'Ammo_CL.StreakSRM-4'},
    'Clan Streak SRM 4 Ammo': {'name': 'Ammo_CL.StreakSRM-4'},
    'CLStreakSRM6': {'name': 'CL.StreakSRM-6'},
    'CLStreakSRM6 Ammo': {'name': 'Ammo_CL.StreakSRM-6'},
    'Clan Streak SRM 6 Ammo': {'name': 'Ammo_CL.StreakSRM-6'},

    'ISLBXAC2': {'name': 'IS.LB2-XAC'},
    'ISLBXAC2 CL Ammo': {'name': 'Ammo_IS.LB2-XAC', 'flags': 'LBX/Cluster'},
    'ISLBXAC2 Ammo': {'name': 'Ammo_IS.LB2-XAC'},
    'IS LB 2-X AC Ammo': {'name': 'Ammo_IS.LB2-XAC'},
    'IS LB 2-X Cluster Ammo': {'name': 'Ammo_IS.LB2-XAC', 'flags': 'LBX/Cluster'},

    'ISLBXAC5': {'name': 'IS.LB5-XAC'},
    'ISLBXAC5 CL Ammo': {'name': 'Ammo_IS.LB5-XAC', 'flags': 'LBX/Cluster'},
    'ISLBXAC5 Ammo': {'name': 'Ammo_IS.LB5-XAC'},
    'IS LB 5-X AC Ammo': {'name': 'Ammo_IS.LB5-XAC'},
    'IS LB 5-X Cluster Ammo': {'name': 'Ammo_IS.LB5-XAC', 'flags': 'LBX/Cluster'},

    'ISLBXAC10': {'name': 'IS.LB10-XAC'},
    'ISLBXAC10 CL Ammo': {'name': 'Ammo_IS.LB10-XAC', 'flags': 'LBX/Cluster'},
    'ISLBXAC10 Ammo': {'name': 'Ammo_IS.LB10-XAC'},
    'IS LB 10-X AC Ammo': {'name': 'Ammo_IS.LB10-XAC'},
    'IS LB 10-X Cluster Ammo': {'name': 'Ammo_IS.LB10-XAC', 'flags': 'LBX/Cluster'},

    'ISLBXAC20': {'name': 'IS.LB20-XAC'},
    'ISLBXAC20 CL Ammo': {'name': 'Ammo_IS.LB20-XAC', 'flags': 'LBX/Cluster'},
    'ISLBXAC20 Ammo': {'name': 'Ammo_IS.LB20-XAC'},
    'IS LB 20-X AC Ammo': {'name': 'Ammo_IS.LB20-XAC'},
    'IS LB 20-X Cluster Ammo': {'name': 'Ammo_IS.LB20-XAC', 'flags': 'LBX/Cluster'},

    'CLLBXAC2': {'name': 'CL.LB2-XAC'},
    'CLLBXAC2 Ammo': {'name': 'Ammo_CL.LB2-XAC'},
    'Clan LB 2-X AC Ammo': {'name': 'Ammo_CL.LB2-XAC'},
    'CLLBXAC2 CL Ammo': {'name': 'Ammo_CL.LB2-XAC', 'flags': 'LBX/Cluster'},
    'Clan LB 2-X Cluster Ammo': {'name': 'Ammo_CL.LB2-XAC', 'flags': 'LBX/Cluster'},
    'CLLBXAC5': {'name': 'CL.LB5-XAC'},
    'CLLBXAC5 Ammo': {'name': 'Ammo_CL.LB5-XAC'},
    'Clan LB 5-X AC Ammo': {'name': 'Ammo_CL.LB5-XAC'},
    'CLLBXAC5 CL Ammo': {'name': 'Ammo_CL.LB5-XAC', 'flags': 'LBX/Cluster'},
    'Clan LB 5-X Cluster Ammo': {'name': 'Ammo_CL.LB5-XAC', 'flags': 'LBX/Cluster'},
    'CLLBXAC10': {'name': 'CL.LB10-XAC'},
    'CLLBXAC10 Ammo': {'name': 'Ammo_CL.LB10-XAC'},
    'Clan LB 10-X AC Ammo': {'name': 'Ammo_CL.LB10-XAC'},
    'CLLBXAC10 CL Ammo': {'name': 'Ammo_CL.LB10-XAC', 'flags': 'LBX/Cluster'},
    'Clan LB 10-X Cluster Ammo': {'name': 'Ammo_CL.LB10-XAC', 'flags': 'LBX/Cluster'},
    'CLLBXAC20': {'name': 'CL.LB20-XAC'},
    'CLLBXAC20 Ammo': {'name': 'Ammo_CL.LB20-XAC'},
    'Clan LB 20-X AC Ammo': {'name': 'Ammo_CL.LB20-XAC'},
    'CLLBXAC20 CL Ammo': {'name': 'Ammo_CL.LB20-XAC', 'flags': 'LBX/Cluster'},
    'Clan LB 20-X Cluster Ammo': {'name': 'Ammo_CL.LB20-XAC', 'flags': 'LBX/Cluster'},

    'ISArrowIVSystem': {'name': 'IS.ArrowIVSystem'},
}
