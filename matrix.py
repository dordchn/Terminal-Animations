#!/usr/bin/env python
import time
from random import randrange
import sys
import os
from sys import stdout

############ Dor Cohen (dordchn@gmail.com) ##############

os.system("clear")

rows, cols = os.popen('stty size', 'r').read().split()
rows = int(rows)
cols = int(cols)

counters=[0] * cols
time.sleep(1)
texts=['Wake up, Neo..','The Matrix has you...']
for text in texts:
	for letter in text: stdout.write(letter); stdout.flush(); time.sleep(0.1)
	time.sleep(2)
	os.system("clear")

cleaner='\n'*(rows)
print cleaner

while 1:
	row=''
	for i in range(len(counters)):
		if counters[i]==0:
			counters[i]=(randrange(15)+5)
			if randrange(10)>0: counters[i]*=-1
		if counters[i]>0:
			row+=chr(randrange(90)+33)
			counters[i]-=1
		else:
			row+=' '
			counters[i]+=1
	print row
	time.sleep(0.05)
