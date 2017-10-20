#!/usr/bin/env python3

file_object = open("/Users/admin/Python5ProblemSet/Python_05.txt", "r")
contents = file_object.read()
variable = contents.upper()

outfile = open("/Users/admin/Python5ProblemSet/Python_05_uc.txt", "w")
outfile.write(variable) 

print(variable,"File was Opened and Modified on 10-19-17")



