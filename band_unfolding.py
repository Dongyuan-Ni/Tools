import numpy as np
from numpy.linalg import *
###########################################################
# 处理vaspkit band-unfolding后的数据 EBS.dat
###########################################################
with open('EBS.dat', 'r') as f:
    f.readline()
    data = f.readlines()

for i in data:
    if '#Kpoint-index' in i:
        data.remove(i)

for i in range(1, len(data)):
    if float(data[i].split()[0]) != 0:
        nbnds = i
        break
nkpts = int(len(data) / nbnds)

# eigen
kpts = []
energy = []
weight = []
for i in range(nbnds):
    for j in range(nkpts):
        line = data[i + nbnds * j].split()
        if float(line[0]) == 0:
            kpts.append('10')
            energy.append(' ')
            weight.append(' ')
        kpts.append(line[0])
        energy.append(line[1])
        weight.append(line[2])

with open('eigenEBS.dat', 'w') as f:
    for i in range(1, len(kpts)):
        f.write(str(kpts[i])+' '+str(energy[i])+' '+str(weight[i])+'\n')
