#!/usr/bin/python


str1 = raw_input("Please enter a string to check if it is a palindrome:")
len1 = len(str1)

str2 = "" 
while len1 > 0:
	
	str2 = str2 + str1[len1 - 1]
	len1 = len1 - 1 

if str1.upper() == str2.upper():	
	print "It is a Palindrome :)"
else:
	print "It is not a Palindrome :("

