#!/usr/bin/python
import sys
import os

file= open(str(sys.argv[1]), 'r')
fileadd= open(str(sys.argv[2]), 'r')
content=file.read()
contentadd=fileadd.read()
file.close()
fileadd.close()
pos=content.find("!")
if pos !=-1:
	content=(" ") + content[:pos] + contentadd + content[pos:]
	file=open(str(sys.argv[1]),'w')
	file.write(content)
	file.close()
	print("OK~")


		
		
		
