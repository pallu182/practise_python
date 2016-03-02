#!/usr/bin/python


def is_prime(x):
	if x == 1 :
		return False
	if x > 1 and  x <= 3:
		return  True
	for i in range(2,x):
		if (x%i) == 0:
			return False
	return True

num = int(input("Give me a number: "))

if is_prime(num):
    print ( str(num) + " is a prime number" )
else:
    print ( str(num) + " is not a prime number" )
