#!/usr/bin/python

import random

num1 = int(raw_input ("How many numbers do you want in the first list:"))

l1 = list()

for a1 in range(1,num1+1):
	l1.append(random.randint(1,1000))
print "l1" , l1

num2 = int(raw_input ("How many numbers do you want in the Second list:"))

l2 = list()

for a2 in range(1,num2+1):     
	l2.append(random.randint(1,1000))
print "l2" , l2

c=list()

for i in l1:
	if (i in l2) and (i not in c):
			c.append(i)


print c		
