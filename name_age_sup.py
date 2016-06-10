#!/usr/bin/python


# Input: Name and Age
# Output:Year during which you will be hundred years
 
import time

name = raw_input("Enter your name:")
age = raw_input("Enter your age:")

age_num = int(age)

current_year = time.strftime("%Y")

new_age = (100-age_num) + int(current_year )

print ("You will be 100 years in the year"),new_age
