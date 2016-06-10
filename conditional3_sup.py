#!/usr/bin/python

try:
	hours_in = raw_input ('Enter Hours')
	rate_in = raw_input ('Enter Rate')
	hours = int(hours_in)
	rate = int(rate_in)
except:
	print 'Error,please enter numeric input'
	exit() # or quit()

if hours <= 40:
	pay = hours * rate
else:
	pay = 40 * rate + ( hours - 40 ) * ( 1.5 * rate )
print pay
