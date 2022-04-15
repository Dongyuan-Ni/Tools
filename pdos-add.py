import numpy as np
import csv
import os

num_orbits = 9
###########################################################
# 处理split_dos脚本运行之后的数据（DOS1-DOSn）
###########################################################
fname = os.listdir('.')
tmp = []
for i in fname:
    if 'DOS' not in i:
        tmp.append(i)
for i in tmp:
    fname.remove(i)
###########################################################
with open(fname[0])as f:
    f_csv = csv.reader(f)
    state = list(f_csv)
    #######Check whether the length is 9001#######
    if len(state) != 9001:
        state.remove(state[0])
    #######Check whether the length is 9001#######
    data = np.zeros((len(state), num_orbits))
    energy = np.zeros((len(state), 1))
    combination = np.zeros((len(state), 2))
    for i in range(len(state)):
        energy[i] = float(state[i][0].split()[0])
###########################################################

###########################################################
num_atoms = len(fname)
print('Total number of atoms: {}'.format(num_atoms))
for name in fname:
    print('Read file: {}'.format(name))
    with open(name)as f:
        f_csv = csv.reader(f)
        state = list(f_csv)
        #######Check whether the length is 9001#######
        if len(state) != 9001:
            state.remove(state[0])
        #######Check whether the length is 9001#######
        for i in range(len(state)):
            a = [float(tmp) for tmp in state[i][0].split()[1:]]
            for j in range(len(a)):
                data[i, j] += a[j]
###########################################################
final = np.hstack((energy, data))

combination[:, 0] = final[:, 0]
combination[:, 1] = np.sum(final[:, 1:], axis=1)/num_atoms
np.savetxt('gray.dat', combination)
print('DOS-Combine.....Done.')

