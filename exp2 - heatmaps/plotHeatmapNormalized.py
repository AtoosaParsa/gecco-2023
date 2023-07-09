import constants as c
import numpy as np
import random
import matplotlib.pyplot as plt
import pickle
from os.path import exists

from switch_float import switch

# change the output port and plot the responses
#switch.showPacking2(stiffness, port1, port2, 3, 5)
#switch.plotInOut2(stiffness, port1, port2, 5)


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
    for ind in range(0, 30):
        #print(ind, flush=True)
        # if this is the source or one of the input ports, skip it
        if ind == 3 or ind == port1[i] or ind == port2[i]:
            continue
        inds.append(ind)

    indices = np.array(inds)

    f = open(f'data/nandness1_{i}.dat', 'rb')
    nandness1 = np.array(pickle.load(f))
    f.close()

    f = open(f'data/nandness2_{i}.dat', 'rb')
    nandness2 = np.array(pickle.load(f))
    f.close()

    f = open(f'data/worsts_{i}.dat', 'rb')
    worsts = np.array(pickle.load(f))
    f.close()

    f = open(f'data/gains00_{i}.dat', 'rb')
    gains00 = np.array(pickle.load(f))
    f.close()

    f = open(f'data/gains01_{i}.dat', 'rb')
    gains01 = np.array(pickle.load(f))
    f.close()

    f = open(f'data/gains10_{i}.dat', 'rb')
    gains10 = np.array(pickle.load(f))
    f.close()

    f = open(f'data/gains11_{i}.dat', 'rb')
    gains11 = np.array(pickle.load(f))
    f.close()

    maxnandness1 = np.amax(nandness1)
    minnandness1 = np.amin(nandness1)
    nandness1_alphas = []
    counter = 0
    for ind in range(0, 30):
        ##print(ind)
        # if this is the source or one of the input ports, skip it
        if ind == 3 or ind == port1[i] or ind == port2[i]:
            # nandness at these ports is zero
            nandness1_alphas.append(0)
        else:
            nandness1_alphas.append((nandness1[counter]-minnandness1)/(maxnandness1-minnandness1))
            counter = counter + 1
        inds.append(ind)

    nandness1_alphas = np.array(nandness1_alphas)
    label='NAND-ness'
    #switch.showPacking(stiffnesses[i], port1[i], port2[i], nandness1_alphas, label)

    maxnandness2 = np.amax(nandness2)
    minnandness2 = np.amin(nandness2)
    nandness2_alphas = []
    counter = 0
    for ind in range(0, 30):
        ##print(ind)
        # if this is the source or one of the input ports, skip it
        if ind == 3 or ind == port1[i] or ind == port2[i]:
            # nandness at these ports is zero
            nandness2_alphas.append(0)
        else:
            nandness2_alphas.append((nandness2[counter]-minnandness2)/(maxnandness2-minnandness2))
            counter = counter + 1
        inds.append(ind)

    nandness2_alphas = np.array(nandness2_alphas)
    label='NAND-ness'
    #switch.showPacking(stiffnesses[i], port1[i], port2[i], nandness2_alphas, label)

    maxgains00 = np.amax(gains00)
    mingains00 = np.amin(gains00)
    gains00_alphas = []
    counter = 0
    for ind in range(0, 30):
        #print(ind)
        # if this is the source or one of the input ports, skip it
        if ind == 3 or ind == port1[i] or ind == port2[i]:
            # nandness at these ports is zero
            gains00_alphas.append(0)
        else:
            gains00_alphas.append((gains00[counter]-mingains00)/(maxgains00-mingains00))
            counter = counter + 1
        inds.append(ind)

    gains00_alphas = np.array(gains00_alphas)
    label='$Gain_{00}$'
    switch.showPacking(stiffnesses[i], port1[i], port2[i], gains00_alphas, label)

    maxgains01 = np.amax(gains01)
    mingains01 = np.amin(gains01)
    gains01_alphas = []
    counter = 0
    for ind in range(0, 30):
        #print(ind)
        # if this is the source or one of the input ports, skip it
        if ind == 3 or ind == port1[i] or ind == port2[i]:
            # nandness at these ports is zero
            gains01_alphas.append(0)
        else:
            gains01_alphas.append((gains01[counter]-mingains01)/(maxgains01-mingains01))
            counter = counter + 1
        inds.append(ind)

    gains01_alphas = np.array(gains01_alphas)
    label='$Gain_{01}$'
    switch.showPacking(stiffnesses[i], port1[i], port2[i], gains01_alphas, label)

    maxgains10 = np.amax(gains10)
    mingains10 = np.amin(gains10)
    gains10_alphas = []
    counter = 0
    for ind in range(0, 30):
        #print(ind)
        # if this is the source or one of the input ports, skip it
        if ind == 3 or ind == port1[i] or ind == port2[i]:
            # nandness at these ports is zero
            gains10_alphas.append(0)
        else:
            gains10_alphas.append((gains10[counter]-mingains10)/(maxgains10-mingains10))
            counter = counter + 1
        inds.append(ind)

    gains10_alphas = np.array(gains10_alphas)
    label='$Gain_{10}$'
    switch.showPacking(stiffnesses[i], port1[i], port2[i], gains10_alphas, label)

    maxgains11 = np.amax(gains11)
    mingains11 = np.amin(gains11)
    gains11_alphas = []
    counter = 0
    for ind in range(0, 30):
        #print(ind)
        # if this is the source or one of the input ports, skip it
        if ind == 3 or ind == port1[i] or ind == port2[i]:
            # nandness at these ports is zero
            gains11_alphas.append(0)
        else:
            gains11_alphas.append((gains11[counter]-mingains11)/(maxgains11-mingains11))
            counter = counter + 1
        inds.append(ind)

    gains11_alphas = np.array(gains11_alphas)
    label='$Gain_{11}$'
    switch.showPacking(stiffnesses[i], port1[i], port2[i], gains11_alphas, label)

