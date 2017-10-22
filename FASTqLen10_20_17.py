#!/usr/bin/env python3

import sys
import re

total_lines = 0
total_characters = 0

with open ("/Users/admin/PFB2017_problemsets/Python_05.fastq", "r") as fastq:

	#content_fastq = fastq.read()			# reads in files ALL at once
	
	for line in fastq:	
	
		wordlist = line.rstrip().split()
		total_lines += 1
		total_characters += len(line)		# length of line on each iteration will be our number of characters  
		avg_length_line = total_characters / total_lines

print("lines:" , total_lines, "\t","characters:", total_characters, "\t", "avg length of line:" , avg_length_line)



