import pickle
import matplotlib.pyplot as plt
from switch_float import switch
import constants as c
import numpy

import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

runs = 5
gens = c.numGenerations
fitnesses = numpy.zeros([runs, gens])
temp = []
individuals = []
for r in range(1, runs+1):
    with open(f'savedRobotsAfpoSeed{r}.dat', "rb") as f:
        for g in range(1, gens+1):
            try:
                temp.append(-1 * pickle.load(f).fitness)
            except EOFError:
                break
        fitnesses[r-1] = temp
        temp = []
    f.close()

mean_f = numpy.mean(fitnesses, axis=0)
std_f = numpy.std(fitnesses, axis=0)

plt.figure(figsize=(6.4,4.8))
plt.plot(list(range(1, gens+1)), mean_f, color='green', label="Best", linewidth=3)
plt.fill_between(list(range(1, gens+1)), mean_f-std_f, mean_f+std_f, color='green', alpha=0.2, linewidth=1)

temp = []
individuals = []
for r in range(1, runs+1):
    with open(f'avgFitnessAfpoSeed{r}.dat', "rb") as f:
        for g in range(1, gens+1):
            try:
                temp.append(pickle.load(f))
            except EOFError:
                break
        fitnesses[r-1] = temp
        temp = []
    f.close()

mean_f = numpy.mean(fitnesses, axis=0)
std_f = numpy.std(fitnesses, axis=0)

plt.plot(list(range(1, gens+1)), mean_f, color='cyan', label="Average", linewidth=2)
plt.fill_between(list(range(1, gens+1)), mean_f-std_f, mean_f+std_f, color='cyan', alpha=0.2, linewidth=1)

plt.xlabel("Generations", fontsize=42)
plt.ylabel("Fitness", fontsize=42)
plt.title("Evolutionary Search", fontsize=42)
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.3)
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.5)
plt.minorticks_on()
plt.xticks(fontsize=42)
plt.yticks(fontsize=42)
#plt.ylim((0, 0.77))
plt.ylim((0, 1))
plt.tight_layout()
plt.legend(loc='upper right', fontsize=32)
plt.show()
