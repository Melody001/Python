#!/usr/bin/python
import sys

try:
	f = open(str(sys.argv[1]), 'r')
	while 1:
		line=f.readline()
		if line:
			print (line)
		if not line:
			break
		pass
    #print(str(f.read()))
finally:
    if f:
        f.close()