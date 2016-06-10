#!/usr/bin/python

filename = raw_input ('Enter the filename')
try:
	filehandle = open(filename)
except:
	print 'No such file exists'
	exit()

for line in filehandle:
	print line.upper()
