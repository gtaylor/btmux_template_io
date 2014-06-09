#!/bin/bash
"""
This module parses a copy/paste from the in-game ADDWEAP table, spitting out
a properly formed WEAPON_TABLE dict.

Assumes that you have a weapons.txt file in the same directory. Try to add
an invalid weapon to a unit as XCODE MECHREP and see the weapons table list::

    addweap invalid lt 1

Copy/paste everything between the ----- header/footers into weapons.txt.
Re-run this, copy what you see in stdout to btmux_template_io/item_table.py's
WEAPON_TABLE.
"""

fobj = open('weapons.txt')
lines = fobj.readlines()

print "WEAPON_TABLE = {"
for line in lines:
    name, heat, damage, min_range, short_range, med_range, long_range,\
    vrt, crits, ammo_per_ton = line.split()
    print "    '{name}': {{'crits': {crits}, 'ammo_count': {ammo_per_ton}}},".format(
        name=name, crits=crits, ammo_per_ton=ammo_per_ton,
    )
print "}"
