#!/usr/bin/python

num = int(raw_input("Enter the number of fibonacci numbers to generate"))

if num == 1:
	print 1
elif num == 2:
	print 1,"\n", 1 
else:
	print 1
	print 1
	a = b = 1
	for i in range(2,num):
		c = a + b
		a = b
		b = c
		print c




