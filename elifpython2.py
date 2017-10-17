#!/usr/bin/env python3

import sys

count = int(sys.argv[1])

if count < 0: 
	message = "less than 0"
	print(count, message)

elif count < 20: 
	message = "is less than 20"
	print(count, message)

elif count > 20:
	message = "is greater than 20"
	print(count, message)

elif count != 20:
	message = "NOT TRUE"
	print(count, message) 

else: 
	message = "must be 20 "
	print(count, message)	
