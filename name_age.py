#!/usr/bin/python

# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old
import time

name = raw_input("Enter your Name ")

age = raw_input("Please enter your age ")

a = int(age)

# get current year and find the year when the person will be 100 yrs

curYear = time.strftime("%Y")
print "Current year is %s " %(curYear)
if a < 100 :
	hunYear = (100 - a ) + int(curYear)	
	print "You will be 100 years old in the year : %d" %(hunYear)
