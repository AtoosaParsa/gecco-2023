import constants as c
import numpy as np
import random
import matplotlib.pyplot as plt
import pickle
from os.path import exists

from switch_float import switch

# first config:
stiffness = np.array([9.1, 6.1, 6.8, 2.3, 7.2, 9.5, 8.5, 7.3, 1.4, 6.6, 6.5, 6.2, 7.9, 8.1, 1.6, 7.4, 4.3, 3.8, 3.9, 8.1, 9.4, 5.8, 4.9, 3.1, 9.4, 8.2, 6.3, 7.2, 5.9, 8.3])
port1 = 29
port2 = 2

freqs = []
nandness1 = []
nandness2 = []
gains00 = []
gains01 = []
gains10 = []
gains11 = []
for freq in range(1, 55):
    print(freq, flush=True)
    temp1, temp2, temp3, temp4, temp5, temp6 = switch.evaluate2(stiffness, port1, port2, freq)
    freqs.append(freq)
    nandness1.append(temp1)
    nandness2.append(temp2)
    gains00.append(temp3)
    gains01.append(temp4)
    gains10.append(temp5)
    gains11.append(temp6)


f = open('nandness1_1.dat', 'ab')
pickle.dump(nandness1 , f)
f.close()

f = open('nandness2_1.dat', 'ab')
pickle.dump(nandness2 , f)
f.close()

f = open('gains00_1.dat', 'ab')
pickle.dump(gains00 , f)
f.close()

f = open('gains01_1.dat', 'ab')
pickle.dump(gains01 , f)
f.close()

f = open('gains10_1.dat', 'ab')
pickle.dump(gains10 , f)
f.close()

f = open('gains11_1.dat', 'ab')
pickle.dump(gains11 , f)
f.close()

# third config:
stiffness = np.array([5.7, 8.3, 1.4, 8.3, 4.7, 9.2, 9.3, 6.5, 2.7, 6.7, 3.7, 4.3, 5.1, 9.2, 5.6, 1.2, 3.8, 5.0, 4.1, 6.4, 7.0, 2.0, 6.0, 9.5, 5.3, 5.3, 9.5, 7.2, 5.2, 8.5])
port1 = 5
port2 = 24

freqs = []
nandness1 = []
nandness2 = []
gains00 = []
gains01 = []
gains10 = []
gains11 = []
for freq in range(1, 55):
    print(freq, flush=True)
    temp1, temp2, temp3, temp4, temp5, temp6 = switch.evaluate2(stiffness, port1, port2, freq)
    freqs.append(freq)
    nandness1.append(temp1)
    nandness2.append(temp2)
    gains00.append(temp3)
    gains01.append(temp4)
    gains10.append(temp5)
    gains11.append(temp6)


f = open('nandness1_2.dat', 'ab')
pickle.dump(nandness1 , f)
f.close()

f = open('nandness2_2.dat', 'ab')
pickle.dump(nandness2 , f)
f.close()

f = open('gains00_2.dat', 'ab')
pickle.dump(gains00 , f)
f.close()

f = open('gains01_2.dat', 'ab')
pickle.dump(gains01 , f)
f.close()

f = open('gains10_2.dat', 'ab')
pickle.dump(gains10 , f)
f.close()

f = open('gains11_2.dat', 'ab')
pickle.dump(gains11 , f)
f.close()