#!/usr/bin/env python3

import sys

sequence = ''

fasta = {}

with open("/Users/admin/PFB2017_problemsets/Python5ProblemSet/Python_05.fasta") as sequences: 
	sequences_content = sequences.read()
	for line in sequences_content.rstrip().split("\n"):			#reading in line by line does not open the entire file at once thereby saving memory
		if line.startswith(">"):
			name = line.rstrip('\n').replace(">",'')
			#sequence_name = line.rstrip('\n').replace(">","")	#designates sequence name and removes >
		else:
			#sequence = line.strip("\n")
			sequence = line
			if name not in fasta:					#initializing dictionary
			#if sequence_name not in fasta:
				fasta[name] = sequence				#name is the key and #sequence is the value
				#fasta[sequence_name] = sequence
			

			#combinedsequence = fasta[name] + sequence
			#combinedsequence = fasta[sequence_name] + sequence
		
			else:	
			
				fasta[name] = fasta[name] + sequence

			#or fasta[name]+= sequence
			#fasta[name] = combinedsequence
			#fasta[sequence_name] = combinedsequence


rev_fasta = dict.copy(fasta)


for name in rev_fasta:		
	compseq_A = rev_fasta[name].replace ("A","t")
	compseq_T = compseq_A.replace("T","a")
	compseq_C = compseq_T.replace("C","g")
	compseq_G = compseq_C.replace("G","c")

	revcompseq = compseq_G[::-1]
	revcompseq = revcompseq.upper()

	rev_fasta[name] = revcompseq

print("reverse complement:", rev_fasta) 
