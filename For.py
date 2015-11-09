#!/usr/bin/python

import math
import sys

sum=0
Result=0
parameters=len(sys.argv)

if(parameters<2):
	print("Please input no less than 2 paraResulteters!")
	exit()

n_char = sys.argv[1]
if(n_char.isdigit() == False):
		print("Please input an integer!")
		exit()
		
if(parameters==2):
	for i in range(0,int(sys.argv[1])):
		sum=sum+1
		Result=Result+sum
	print(Result)
	
if(parameters==3):
	if(int(sys.argv[1])<int(sys.argv[2])):
		for i in range(int(sys.argv[1]), int(sys.argv[2])+1):
			Result=Result+i
		print(Result)
	else:
		for i in range(int(sys.argv[2]), int(sys.argv[1])+1):
			Result=Result+i
		print(Result)

if(parameters>3):
	print("Please input no Resultore than 3 paraResulteters!")
	exit()






	








