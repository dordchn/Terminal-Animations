#!/usr/bin/env python
import time
from random import randrange
import sys
import os
from sys import stdout

epsilon=0.001
rows, cols = os.popen('stty size', 'r').read().split()
rows = int(rows)
cols = int(cols)

##################################################################################

os.system("clear")
cleaner='\n'*rows
print cleaner

position=randrange(cols)
direction = randrange(2)*2-1
speed=0
symbol='O'

source=int(position)
dest=position

while 1:
	if abs(speed)<epsilon: speed = 0

	# randomize new destination
	if position*direction>=dest*direction or speed==0:
		speed=0
		source=int(position)
		direction*=-1
		if direction>0: # right
			dest = int(position)+randrange(cols-int(position))
		else: # left
			dest = randrange(int(position))

	# Make a move
	if abs(int(position)-dest)>0.5*abs(dest-source):
		speed+=0.1
	else:
		speed-=0.1
	position+=speed*direction
	print ' '*int(position)+symbol+(cols-int(position)-1)*' '

	time.sleep(0.03)