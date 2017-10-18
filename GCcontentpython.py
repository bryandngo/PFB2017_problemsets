#!/usr/bin/env python3

import sys

dna_sequence = sys.argv[1]

dna_length = len(dna_sequence)

G_count = dna_sequence.count('G')

C_count = dna_sequence.count('C')

GC_count = G_count + C_count  

fraction = GC_count / len(dna_sequence)

print('{0:4.2f}%'.format(fraction*100))








