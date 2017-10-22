#!/usr/bin/env python3
import sys
import re

pattern = "Nobody"
new_poem = open("BRYAN.txt", "w")
nobody_poem = open(sys.argv[1], "r")

for line in nobody_poem:                                #nothing needs to be indented beneath open method
	line = line.rstrip()
	found = re.search(pattern, line)
	bryanpoem = re.sub(pattern, 'BRYAN', line)

	new_poem.write(bryanpoem)

nobody_poem.close()
new_poem.close()

with open('/Users/admin/PFB2017_problemsets/BRYAN.txt',"r") as newfile:
	contents = newfile.read()
	print ("NEW POEM:", ('\n'), contents)		
