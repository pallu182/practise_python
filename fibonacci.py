#!/usr/bin/python

first = 1
sec	  = 1

tot = raw_input("Please enter how many fibonacci numbers you desire to generate : ")

if int(tot) >= 1 :
	print first
if int(tot) >= 2 :
	print sec

count = 2
while(True) :
	if count >= int(tot) :
		quit()	
	third = first + sec
	print third
	first = sec
	sec   = third
	count = count + 1

