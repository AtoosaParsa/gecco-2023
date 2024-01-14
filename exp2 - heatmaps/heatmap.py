import constants as c
import numpy as np
import random
import matplotlib.pyplot as plt
import pickle
from os.path import exists

from switch_float import switch

stiffnesses = []
port1 = []
port2 = []

stiffnesses.append([9.1, 6.1, 6.8, 2.3, 7.2, 9.5, 8.5, 7.3, 1.4, 6.6, 6.5, 6.2, 7.9, 8.1, 1.6, 7.4, 4.3, 3.8, 3.9, 8.1, 9.4, 5.8, 4.9, 3.1, 9.4, 8.2, 6.3, 7.2, 5.9, 8.3])
port1.append(29)
port2.append(2)

stiffnesses.append([3.8, 8.4, 8.8, 1.7, 10.0, 6.6, 3.5, 9.3, 3.2, 8.7, 6.3, 6.0, 8.2, 7.2, 3.4, 4.9, 2.8, 8.8, 6.5, 2.3, 9.5, 6.7, 9.6, 2.0, 5.4, 4.6, 4.3, 6.6, 8.0, 7.7])
port1.append(29)
port2.append(2)

stiffnesses.append([5.7, 8.3, 1.4, 8.3, 4.7, 9.2, 9.3, 6.5, 2.7, 6.7, 3.7, 4.3, 5.1, 9.2, 5.6, 1.2, 3.8, 5.0, 4.1, 6.4, 7.0, 2.0, 6.0, 9.5, 5.3, 5.3, 9.5, 7.2, 5.2, 8.5])
port1.append(5)
port2.append(24)

stiffnesses.append([7.4, 7.1, 5.3, 1.6, 7.4, 7.0, 2.6, 7.1, 9.0, 7.1, 6.5, 7.9, 2.0, 1.5, 7.8, 1.3, 7.9, 4.3, 7.0, 6.8, 2.5, 5.9, 1.6, 9.3, 9.3, 6.0, 7.8, 6.7, 8.2, 8.2])
port1.append(29)
port2.append(0)

stiffnesses.append([8.3, 7.1, 1.0, 3.8, 6.8, 7.4, 5.9, 1.6, 6.6, 8.9, 9.0, 6.3, 8.2, 4.4, 7.6, 8.6, 9.9, 7.8, 6.1, 9.3, 6.2, 3.5, 8.0, 2.5, 9.0, 7.0, 9.4, 1.5, 9.3, 3.7])
port1.append(24)
port2.append(4)

for i in range(0, 5):
    print("configuration: "+str(i))
    inds = []
    nandness1 = []
    nandness2 = []
    worsts = []
    gains00 = []
    gains01 = []
    gains10 = []
    gains11 = []
    for ind in range(0, 30):
        print(ind, flush=True)
        # if this is the source or one of the input ports, skip it
        if ind == 3 or ind == port1[i] or ind == port2[i]:
            continue
        temp1, temp2, temp3, temp4, temp5, temp6, temp7 = switch.evaluate2(stiffnesses[i], port1[i], port2[i], ind)
        inds.append(ind)
        nandness1.append(temp1)
        nandness2.append(temp2)
        worsts.append(temp3)
        gains00.append(temp4)
        gains01.append(temp5)
        gains10.append(temp6)
        gains11.append(temp7)


    f = open(f'data/nandness1_{i}.dat', 'ab')
    pickle.dump(nandness1, f)
    f.close()

    f = open(f'data/nandness2_{i}.dat', 'ab')
    pickle.dump(nandness2, f)
    f.close()

    f = open(f'data/worsts_{i}.dat', 'ab')
    pickle.dump(worsts, f)
    f.close()

    f = open(f'data/gains00_{i}.dat', 'ab')
    pickle.dump(gains00, f)
    f.close()

    f = open(f'data/gains01_{i}.dat', 'ab')
    pickle.dump(gains01, f)
    f.close()

    f = open(f'data/gains10_{i}.dat', 'ab')
    pickle.dump(gains10, f)
    f.close()

    f = open(f'data/gains11_{i}.dat', 'ab')
    pickle.dump(gains11, f)
    f.close()
