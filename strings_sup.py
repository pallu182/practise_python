#!/usr/bin/python

x = 'X-DSPAM-Confidence: 0.8475'
print x

pos = x.find(':')
num_full = x[pos+1:]
num = num_full.strip()

print num
