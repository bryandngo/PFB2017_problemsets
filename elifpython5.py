#!/usr/bin/env python3

import sys 

count = float(sys.argv[1])

if count == 0:
        message = "is 0"
        print(count, message)

elif count == 50:
        message = "is 50"
        print (count, message)

elif count > 50 and count%3 == 0:
        message = "is greater than 50 and is divisible by 3"
        print (count, message)

elif count < 50 and count%2 == 0:
        message = "is less than 50 and is divisible by 2"
        print (count, message)

elif count < 0:
	message = "is negative"
	print (count, message) 



