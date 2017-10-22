#!/usr/bin/env python3
import sys
import re

pattern = "Nobody"
line_count = 0

nobody_poem = open(sys.argv[1], "r")
for line in nobody_poem:				#nothing needs to be indented beneath open method
	line = line.rstrip()
	line_count += 1
	#found = re.findall(pattern, line)
	found = re.search(pattern, line)
	
	if found is not None:
	
		print("position in line:", found.span(), "line:", line_count)
		
		#print(found)
	


	
