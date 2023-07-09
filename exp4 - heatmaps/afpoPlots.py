import pickle
import matplotlib.pyplot as plt
from switch_float import switch
import constants as c
import numpy

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
plt.plot(list(range(1, gens+1)), mean_f, color='blue', label="Average", linewidth=2)
plt.fill_between(list(range(1, gens+1)), mean_f-std_f, mean_f+std_f, color='cornflowerblue', alpha=0.2, label="Standard Deviation", linewidth=1)
plt.xlabel("Generations", fontsize=32)
plt.ylabel("Fitness", fontsize=32)
plt.title("Evolutionary Search", fontsize=32)
plt.grid(which='minor', color='skyblue', linestyle=':', linewidth=0.3)
plt.grid(which='major', color='skyblue', linestyle='-', linewidth=0.5)
plt.minorticks_on()
plt.xticks(fontsize=28)
plt.yticks(fontsize=28)
plt.ylim((0, 0.77))
plt.tight_layout()
plt.legend(loc='upper right', fontsize=28)
plt.show()

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

plt.figure(figsize=(6.4,4.8))
plt.plot(list(range(1, gens+1)), mean_f, color='blue', label="Average", linewidth=2)
plt.fill_between(list(range(1, gens+1)), mean_f-std_f, mean_f+std_f, color='cornflowerblue', alpha=0.2, label="Standard Deviation", linewidth=1)
plt.xlabel("Generations", fontsize=32)
plt.ylabel("Average Fitness", fontsize=32)
plt.title("Evolutionary Search", fontsize=32)
plt.grid(which='minor', color='skyblue', linestyle=':', linewidth=0.3)
plt.grid(which='major', color='skyblue', linestyle='-', linewidth=0.5)
plt.minorticks_on()
plt.xticks(fontsize=28)
plt.yticks(fontsize=28)
plt.tight_layout()
plt.legend(loc='upper right', fontsize=28)
plt.show()
