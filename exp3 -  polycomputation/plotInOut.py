import constants as c
import numpy as np
import random
import matplotlib.pyplot as plt
import pickle
from os.path import exists

from switch_float import switch

runs = c.RUNS
gens = c.numGenerations


# running the best individuals
temp = []
rubish = []
a = np.array([1.2, 5.5, 8.5, 6.7, 5.8, 5.8, 8.2, 7.5, 2.8, 9.6, 2.4, 3.4, 8.3, 4.6, 8.9, 9.6, 1.8, 2.4, 9.7, 2.4, 5.1, 1.9, 2.6, 9.6, 7.9, 5.8, 5.8, 3.2, 8.8, 8.8])
#a = np.array([7.4, 7.4, 7.8, 6.1, 6.1, 6.4, 3.6, 5.1, 6.3, 3.4, 9.5, 5.7, 1.6, 1.1, 5.9, 7.7, 2.9, 3.7, 4.7, 8.,  8.2, 6.8, 6.6, 1.5, 3.5, 9.,  3.8, 1.1, 2.6, 8.7])
#a = np.array([10, 10, 10, 10, 10, 1, 10, 10, 1, 10, 10, 10, 10, 10, 10, 10, 10, 1, 10, 10, 10, 10, 10, 1, 1, 10, 10, 1, 10, 1])
#a = np.array([1, 1, 1, 1, 1, 10, 1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 10, 10, 1, 1, 10, 1, 10])
print(switch.evaluate(a, 29, 1))
switch.showPacking(a, 29, 1)
output=switch.plotInOut(a, 29, 1)
#print(output)
#metric = (abs(1-output[0]) + abs(1-output[1]) + abs(1-output[2]) + abs(0-output[3]))/4
#print(metric)
with open('lastGeneration.dat', "rb") as f:
    for r in range(1, runs+1):
        # population of the last generation
        temp = pickle.load(f)
        # show the genomes of the last generation
        print(len(temp))
        for i in range(len(temp)):
            print(list(temp[i].genome))
            print(temp[i].fitnesses)
            print(temp[i].nandness)
            print()
        temp = []
f.close()
