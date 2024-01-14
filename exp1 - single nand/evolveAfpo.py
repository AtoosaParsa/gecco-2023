from afpo import AFPO
import os
import constants as c
import random
import subprocess as sub
import sys

# input the seed
seed = int(sys.argv[1])

#cleaning up  the data files
sub.call(f"rm -rf gens{seed}", shell=True)
sub.call(f"mkdir gens{seed}/", shell=True)

try:
    os.remove(f"savedRobotsLastGenAfpoSeed{seed}.dat")
except OSError:
    pass
try:
    os.remove(f"avgFitnessAfpoSeed{seed}.dat")
except OSError:
    pass
try:
    os.remove(f"savedRobotsAfpoSeed{seed}.dat")
except OSError:
    pass

runs = c.RUNS
for r in range(1, runs+1):
    print("*********************************************************", flush=True)
    print("seed: "+str(seed), flush=True)
    randomSeed = seed
    random.seed(seed)
    afpo = AFPO(seed)
    afpo.Evolve()
    #afpo.Show_Best_Genome()
        


