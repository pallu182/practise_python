#!/usr/bin/python

import random

def get_list(num) :
	min = 1
	max = 1000
	retList = list()
	i = 0 
	while i < num :
		x = (random.randint(min,max))
		retList.append(x)
		i = i + 1

	return retList
		
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = list()
for i in  a :
	if (i in b) and (i not in c) :
		c.append(i)
		print i
# Get the number of elements in list 1

num1 = int(raw_input("Enter the number of elements in list1"))

num2 = int(raw_input("Enter the number of elements in the list2"))

l1 = get_list(num1)

print l1 
l2 = get_list(num2)
print l2 

print "Finding common elements "
d = list()
for i in l1 :
	if (i in l2) and ( i not in d ) :
		d.append(i)
		print d 
