#!/usr/bin/python

str1 = raw_input("Hello, wanna check if the string is palindrome ? Enter a string and i will tell you : ")

strlen = len(str1)

j = strlen - 1
check = True
for i in range(0, strlen) :
	if str1[i] != str1[j] :
		check = False
		break
	else :
		j = j - 1


if check == True :
	print "The string is a palindrome, hurray !"
else :
	print "Nope this is not a palindrome"
