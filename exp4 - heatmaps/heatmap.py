import constants as c
import numpy as np
import random
import matplotlib.pyplot as plt
import pickle
from os.path import exists

from switch_float import switch

# best configuration
stiffness = np.array([1.2, 5.5, 8.5, 6.7, 5.8, 5.8, 8.2, 7.5, 2.8, 9.6, 2.4, 3.4, 8.3, 4.6, 8.9, 9.6, 1.8, 2.4, 9.7, 2.4, 5.1, 1.9, 2.6, 9.6, 7.9, 5.8, 5.8, 3.2, 8.8, 8.8])
port1 = 29
port2 = 1

inds = []
nandness1_1 = []
nandness2_1 = []
worsts_1 = []
gains00_1 = []
gains01_1 = []
gains10_1 = []
gains11_1 = []
nandness1_2 = []
nandness2_2 = []
worsts_2 = []
gains00_2 = []
gains01_2 = []
gains10_2 = []
gains11_2 = []
for ind in range(0, 30):
    print(ind, flush=True)
    # if this is the source or one of the input ports, skip it
    if ind == 3 or ind == port1 or ind == port2:
        continue
    temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8, temp9, temp10, temp11, temp12, temp13, temp14 = switch.evaluate2(stiffness, port1, port2, ind)
    inds.append(ind)
    nandness1_1.append(temp1)
    nandness2_1.append(temp2)
    worsts_1.append(temp3)
    gains00_1.append(temp4)
    gains01_1.append(temp5)
    gains10_1.append(temp6)
    gains11_1.append(temp7)
    nandness1_2.append(temp8)
    nandness2_2.append(temp9)
    worsts_2.append(temp10)
    gains00_2.append(temp11)
    gains01_2.append(temp12)
    gains10_2.append(temp13)
    gains11_2.append(temp14)

f = open('nandness1_1.dat', 'ab')
pickle.dump(nandness1_1, f)
f.close()

f = open('nandness2_1.dat', 'ab')
pickle.dump(nandness2_1, f)
f.close()

f = open('worsts_1.dat', 'ab')
pickle.dump(worsts_1, f)
f.close()

f = open('gains00_1.dat', 'ab')
pickle.dump(gains00_1, f)
f.close()

f = open('gains01_1.dat', 'ab')
pickle.dump(gains01_1, f)
f.close()

f = open('gains10_1.dat', 'ab')
pickle.dump(gains10_1, f)
f.close()

f = open('gains11_1.dat', 'ab')
pickle.dump(gains11_1, f)
f.close()

f = open('nandness1_2.dat', 'ab')
pickle.dump(nandness1_2, f)
f.close()

f = open('nandness2_2.dat', 'ab')
pickle.dump(nandness2_2, f)
f.close()

f = open('worsts_2.dat', 'ab')
pickle.dump(worsts_2, f)
f.close()

f = open('gains00_2.dat', 'ab')
pickle.dump(gains00_2, f)
f.close()

f = open('gains01_2.dat', 'ab')
pickle.dump(gains01_2, f)
f.close()

f = open('gains10_2.dat', 'ab')
pickle.dump(gains10_2, f)
f.close()

f = open('gains11_2.dat', 'ab')
pickle.dump(gains11_2, f)
f.close()