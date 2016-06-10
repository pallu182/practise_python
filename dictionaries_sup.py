#!/usr/bin/python


handle = open('mbox-short_sup.txt')
counts = dict()
for line in handle:
        each_line = line.split()
        for word in each_line:
                counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword,bigcount
