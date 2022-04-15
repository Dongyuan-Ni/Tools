import numpy as np
import csv
import os
###########################################################
# 处理split_dos脚本运行之后的数据（DOS1-DOSn）
###########################################################
fname = os.listdir('.')
# fname.remove('.DS_Store')
fname.remove('pdos-add.py')
fname.remove('test.py')
###########################################################
with open(fname[0])as f:
    f_csv = csv.reader(f)
    state = list(f_csv)
    data = np.zeros((len(state), 3))
    energy = np.zeros((len(state), 1))
    for i in range(len(state)):
        energy[i] = np.float(state[i][0].split()[0])
###########################################################

###########################################################
for name in fname:
    with open(name)as f:
        f_csv = csv.reader(f)
        state = list(f_csv)
        for i in range(len(state)):
            a = [np.float(tmp) for tmp in state[i][0].split()[1:]]
            for j in range(len(a)):
                data[i, j] += a[j]
###########################################################
final = np.hstack((energy, data))
np.savetxt('dump.dat', final)
print('PDOS-Combine.....Done.')
