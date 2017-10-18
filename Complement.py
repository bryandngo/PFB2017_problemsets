#!/usr/bin/env python3

import sys

dna_sequence = sys.argv[1] 

dna_sequence_A = dna_sequence.replace("A","t")

dna_sequence_T = dna_sequence_A.replace("T","a")

dna_sequence_C = dna_sequence_T.replace("C","g")

dna_sequence_G = dna_sequence_C.replace("G","c") 

reverse_complement = dna_sequence_G[::-1]

reverse_complement = reverse_complement.upper()

print(reverse_complement)



