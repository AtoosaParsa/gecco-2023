import constants as c
import numpy as np
import random
import matplotlib.pyplot as plt
import pickle
from os.path import exists

from switch_float import switch

stiffness = np.array([1.2, 5.5, 8.5, 6.7, 5.8, 5.8, 8.2, 7.5, 2.8, 9.6, 2.4, 3.4, 8.3, 4.6, 8.9, 9.6, 1.8, 2.4, 9.7, 2.4, 5.1, 1.9, 2.6, 9.6, 7.9, 5.8, 5.8, 3.2, 8.8, 8.8])
port1 = 29
port2 = 1

# change the ourput port and plot the responses
#switch.showPacking2(stiffness, port1, port2, 3, 5)
#switch.plotInOut2(stiffness, port1, port2, 5)

inds = []

for ind in range(0, 30):
    print(ind, flush=True)
    # if this is the source or one of the input ports, skip it
    if ind == 3 or ind == port1 or ind == port2:
        continue
    inds.append(ind)

indices = np.array(inds)

f = open('nandness1_1.dat', 'rb')
nandness1_1 = np.array(pickle.load(f))
f.close()

f = open('nandness2_1.dat', 'rb')
nandness2_1 = np.array(pickle.load(f))
f.close()

f = open('worsts_1.dat', 'rb')
worsts_1 = np.array(pickle.load(f))
f.close()

f = open('gains00_1.dat', 'rb')
gains00_1 = np.array(pickle.load(f))
f.close()

f = open('gains01_1.dat', 'rb')
gains01_1 = np.array(pickle.load(f))
f.close()

f = open('gains10_1.dat', 'rb')
gains10_1 = np.array(pickle.load(f))
f.close()

f = open('gains11_1.dat', 'rb')
gains11_1 = np.array(pickle.load(f))
f.close()

f = open('nandness1_2.dat', 'rb')
nandness1_2 = np.array(pickle.load(f))
f.close()

f = open('nandness2_2.dat', 'rb')
nandness2_2 = np.array(pickle.load(f))
f.close()

f = open('worsts_2.dat', 'rb')
worsts_2 = np.array(pickle.load(f))
f.close()

f = open('gains00_2.dat', 'rb')
gains00_2 = np.array(pickle.load(f))
f.close()

f = open('gains01_2.dat', 'rb')
gains01_2 = np.array(pickle.load(f))
f.close()

f = open('gains10_2.dat', 'rb')
gains10_2 = np.array(pickle.load(f))
f.close()

f = open('gains11_2.dat', 'rb')
gains11_2 = np.array(pickle.load(f))
f.close()

maxnandness1_1 = np.amax(nandness1_1)
minnandness1_1 = np.amin(nandness1_1)
nandness1_1_alphas = []
counter = 0
for ind in range(0, 30):
    print(ind)
    # if this is the source or one of the input ports, skip it
    if ind == 3 or ind == port1 or ind == port2:
        # nandness at these ports is zero
        nandness1_1_alphas.append(1)
    else:
        nandness1_1_alphas.append((nandness1_1[counter]-minnandness1_1)/(maxnandness1_1-minnandness1_1))
        counter = counter + 1
    inds.append(ind)
nandness1_1_alphas = np.array(nandness1_1_alphas)

maxnandness1_2 = np.amax(nandness1_2)
minnandness1_2 = np.amin(nandness1_2)
nandness1_2_alphas = []
counter = 0
for ind in range(0, 30):
    print(ind)
    # if this is the source or one of the input ports, skip it
    if ind == 3 or ind == port1 or ind == port2:
        # nandness at these ports is zero
        nandness1_2_alphas.append(1)
    else:
        nandness1_2_alphas.append((nandness1_2[counter]-minnandness1_2)/(maxnandness1_2-minnandness1_2))
        counter = counter + 1
    inds.append(ind)
nandness1_2_alphas = np.array(nandness1_2_alphas)

label='Metric'
#switch.showPacking(stiffness, port1, port2, nandness1_1_alphas, nandness1_2_alphas, label)

maxnandness2_1 = np.amax(nandness2_1)
minnandness2_1 = np.amin(nandness2_1)
nandness2_1_alphas = []
counter = 0
for ind in range(0, 30):
    print(ind)
    # if this is the source or one of the input ports, skip it
    if ind == 3 or ind == port1 or ind == port2:
        # nandness at these ports is zero
        nandness2_1_alphas.append(0)
    else:
        nandness2_1_alphas.append((nandness2_1[counter]-minnandness2_1)/(maxnandness2_1-minnandness2_1))
        counter = counter + 1
    inds.append(ind)

nandness2_1_alphas = np.array(nandness2_1_alphas)

maxnandness2_2 = np.amax(nandness2_2)
minnandness2_2 = np.amin(nandness2_2)
nandness2_2_alphas = []
counter = 0
for ind in range(0, 30):
    print(ind)
    # if this is the source or one of the input ports, skip it
    if ind == 3 or ind == port1 or ind == port2:
        # nandness at these ports is zero
        nandness2_2_alphas.append(0)
    else:
        nandness2_2_alphas.append((nandness2_2[counter]-minnandness2_2)/(maxnandness2_2-minnandness2_2))
        counter = counter + 1
    inds.append(ind)

nandness2_2_alphas = np.array(nandness2_2_alphas)

print(nandness2_1_alphas)
print(nandness2_2_alphas)
label='Metric'

switch.showPacking(stiffness, port1, port2, nandness2_1_alphas, nandness2_2_alphas, label)
switch.showPacking(stiffness, port1, port2, nandness2_2_alphas, nandness2_1_alphas, label)
