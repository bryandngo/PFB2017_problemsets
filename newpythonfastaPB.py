#!/usr/bin/env python3

import sys

sequence = ''

fasta = {}

with open("/Users/admin/Python5ProblemSet/Python_05.fasta") as sequences: 
	sequences_content = sequences.read()
	for line in sequences_content.rstrip().split("\n"):
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
			
			#fasta[name] = combinedsequence
			#fasta[sequence_name] = combinedsequence

print(fasta) 
