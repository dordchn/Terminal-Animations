#!/usr/bin/env python
import time
from random import randrange
import sys
import os
from sys import stdout

############ Dor Cohen (dordchn@gmail.com) ##############

rows, cols = os.popen('stty size', 'r').read().split()
cols = int(cols)

bubble0=['      OOOOOOOO      ',
		 '    OO     xx OO    ',
		 '   O         x  O   ',
		 '   O          x O   ',
		 '    OO        OO    ',
		 '      OOOOOOOO      ',]

bubble1=['      OOOOOOOOOOOO      ',
		 '    OO         x  OO    ',
		 '   O            xx  O   ',
		 '   O             x  O   ',
		 '   O              x O   ',
		 '   O                O   ',
		 '    OO            OO    ',
		 '      OOOOOOOOOOOO      ',]

bubble2=['============================ ',
         '  ______    ______   _____   ',
         ' |  __  \  |  __  | |  __ \  ',
         ' | |  |  | | |  | | | |_\ |  ',
         ' | |__|  | | |__| | |  __  | ',
         ' |_____ /  |______| |_|  |_| ',
         '                             ',
         '============================ ',]

bubble3=['      OOOO      ',
         '    OO  x OO    ',
         '   O     x  O   ',
         '    OO    OO    ',
		 '      OOOO      ']

bubbles=[]
bubbles.append(bubble0);
bubbles.append(bubble1);
# bubbles.append(bubble2);
# bubbles.append(bubble3);

##################################################################################

bl_row=-1
bl_x=-1
bl_type=0

while 1:	
	if bl_row==-1: # New
		if randrange(10)>5:
			bl_row=0;
			bl_type=randrange(len(bubbles));
			bl_x=randrange(cols-len(bubbles[bl_type][0]));
		row=' '*cols
	else: #Continue
		row=' '*bl_x;
		row=row+bubbles[bl_type][bl_row]+' '*(cols-bl_x-len(bubbles[bl_type][0]))
		bl_row+=1;
		bl_height=len(bubbles[bl_type])
		if bl_row>bl_height-1: bl_row=-1
	print row
	time.sleep(0.05)
