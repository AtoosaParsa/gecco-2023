import constants as c
import numpy as np
import random
import matplotlib.pyplot as plt
import pickle
from os.path import exists

from switch_float import switch

runs = 5
gens = c.numGenerations


# running the best individuals
temp = []
rubish = []
#a = np.array([10, 10, 10, 10, 10, 1, 10, 10, 1, 10, 10, 10, 10, 10, 10, 10, 10, 1, 10, 10, 10, 10, 10, 1, 1, 10, 10, 1, 10, 1])
#a = np.array([1, 1, 1, 1, 1, 10, 1, 1, 10, 1, 1, 1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 10, 10, 1, 1, 10, 1, 10])
switch.showPacking(np.round(np.random.uniform(1, 10, size=30), decimals=1), 14, 16)
#print(switch.plotInOut(a))

for r in range(1, runs+1):
    with open(f'savedRobotsLastGenAfpoSeed{r}.dat', "rb") as f:
        # population of the last generation
        temp = pickle.load(f)
        # best individual of last generation
        best = temp[0]
        print(best.indv.genome1)
        print(best.indv.genome2)
        print(best.indv.genome3)
        switch.showPacking(best.indv.genome1, best.indv.genome2, best.indv.genome3)
        print(switch.plotInOut(best.indv.genome1, best.indv.genome2, best.indv.genome3))
        print("fitness: " + str(best.indv.fitness))
        temp = []
    f.close()
