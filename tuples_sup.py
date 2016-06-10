#!/usr/bin/python


handle = open('mbox-short_sup.txt')
counts = dict()
for line in handle:
	each_line = line.split()
	for word in each_line:
		counts[word] = counts.get(word,0) + 1

tmp = list()
for k,v in counts.items():
	tmp.append((v,k))

tmp.sort(reverse=True)

for i,j in tmp[:10]:
	print i,j
	
