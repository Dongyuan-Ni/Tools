#!/usr/bin/env python
import os
import numpy as np

###########################################################
filename = 'POSCAR_pre'
# flist is for the order of atom who does not move
flist = list(np.linspace(1, 215, 215, dtype='int'))
fremove = [47]
###########################################################
for i in fremove:
	flist.remove(i)
data = []
with open(filename, 'r') as f:
	length = len(f.readlines())
	
with open(filename, 'r') as f:
	for i in range(7):
		data.append(f.readline())
	f.readline()
	data.append('Selective dynamics\n')
	data.append('Direct\n')
	for i in range(9, length+1):
		tmp = f.readline().strip('\n')
		if i-8 in flist:
			data.append(tmp+' '+'F F F\n')
		else:
			data.append(tmp+' '+'T T T\n')		
with open('POSCAR_new', 'w') as f:
	f.writelines(data)

