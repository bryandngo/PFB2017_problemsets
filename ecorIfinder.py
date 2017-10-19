#!/usr/bin/env python3

import sys

dna = sys.argv[1]

ecorI = "GAATTC"

ecorIlocation = dna.find(ecorI)

re_location = ecorIlocation + 1 

fragment1 = dna[0:396]

fragment1_length = len(fragment1)

fragment2_length = len(dna)-fragment1_length

print("fragment1:", fragment1_length, "fragment2:", fragment2_length)

print("ECORI location:", re_location, "ECORI python location:", ecorIlocation)



