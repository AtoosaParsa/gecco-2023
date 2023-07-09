import numpy as np
import random
import matplotlib.pyplot as plt
import pickle
from os.path import exists
import subprocess as sub
import sys

from switch_float import switch

#cleaning up  the data files
sub.call(f"rm -rf data2", shell=True)
sub.call(f"mkdir data2/", shell=True)

# best solution from one of the runs
stiffness = np.array([9.1, 6.1, 6.8, 2.3, 7.2, 9.5, 8.5, 7.3, 1.4, 6.6, 6.5, 6.2, 7.9, 8.1, 1.6, 7.4, 4.3, 3.8, 3.9, 8.1, 9.4, 5.8, 4.9, 3.1, 9.4, 8.2, 6.3, 7.2, 5.9, 8.3])
ind1 = 29
ind2 = 2

#switch.showPacking(stiffness, ind1, ind2)
#switch.plotInOut(stiffness, ind1, ind2, noise=0.5)

means_g00 = []
means_g01 = []
means_g10 = []
means_g11 = []
std_g00 = []
std_g01 = []
std_g10 = []
std_g11 = []
# add different percentages of gaussian white noise to the input signals (not the source), the percentage is percentage of the amplitude
for n in [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0.1, 10, 20, 30, 40, 50]:
    # run each case 10 times and take the average and std
    g00=[]
    g01=[]
    g10=[]
    g11=[]
    print(n, flush=True)
    for count in np.arange(10):
        _, t1, t2, t3, t4 = switch.evaluate(stiffness, ind1, ind2, n)
        g00.append(t1)
        g01.append(t2)
        g10.append(t3)
        g11.append(t4)
    means_g00.append(np.mean(g00, axis=0))
    std_g00.append(np.std(g00, axis=0))
    means_g01.append(np.mean(g01, axis=0))
    std_g01.append(np.std(g01, axis=0))
    means_g10.append(np.mean(g10, axis=0))
    std_g10.append(np.std(g10, axis=0))
    means_g11.append(np.mean(g11, axis=0))
    std_g11.append(np.std(g11, axis=0))

# save everything
f = open('data2/means_g00.dat', 'ab')
pickle.dump(means_g00, f)
f.close()
f = open('data2/means_g01.dat', 'ab')
pickle.dump(means_g01, f)
f.close()
f = open('data2/means_g10.dat', 'ab')
pickle.dump(means_g10, f)
f.close()
f = open('data2/means_g11.dat', 'ab')
pickle.dump(means_g11, f)
f.close()
f = open('data2/std_g00.dat', 'ab')
pickle.dump(std_g00, f)
f.close()
f = open('data2/std_g01.dat', 'ab')
pickle.dump(std_g01, f)
f.close()
f = open('data2/std_g10.dat', 'ab')
pickle.dump(std_g10, f)
f.close()
f = open('data2/std_g11.dat', 'ab')
pickle.dump(std_g11, f)
f.close()