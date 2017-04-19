#!/usr/bin/env python

from random import randint

testlist = []

def RandintList(Min,Max,Times):
	for element in xrange(Times):
		testlist.append(randint(Min,Max))
RandintList(0,100,5)
otherlist = testlist[:]

final_length = len(otherlist) - 1
n = 0

while	n < final_length:
	m = 0
	flag = 1
	while m < final_length - n:
		if otherlist[m] > otherlist[m+1]:
			otherlist[m],otherlist[m+1] = otherlist[m+1],otherlist[m]
			flag = 0
		m += 1
		print otherlist
	n += 1
	if flag:
		break

print otherlist

