#!/usr/bin/env python3

import sys

dna_sequence = sys.argv[1]

dna_length = len(dna_sequence)

T_count = dna_sequence.count('T')

A_count = dna_sequence.count('A')

AT_count = T_count + A_count

fraction = AT_count / len(dna_sequence)

print('{0:4.2f}%'.format(fraction*100))



