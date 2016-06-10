#!/usr/bin/python

count = 0
sum = 0
while True:
	i = raw_input ('Enter a number:')
	if i == 'done': break
	if len(i) < 1 : break
	try:
		number = int(i)
	except:
		print 'Invalid input'
		continue # so that it does go to increment sum and count
	count = count + 1
        sum = sum + number 
avg = float(sum) / count
print avg
