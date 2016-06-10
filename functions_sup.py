#!/usr/bin/python

def computepay(hours,rate):
	if hours <= 40:
		pay = hours * rate
	else:
		pay = 40 * rate + ( hours - 40 ) * ( 1.5 * rate )
	return pay

try:
	hours_in = raw_input ('Enter Hours')
	rate_in = raw_input ('Enter Rate')
	h = int(hours_in)
	r = int(rate_in)
except:
	print 'Error,please enter numeric input'
	exit() # or quit()

p = computepay(h,r)
print p

