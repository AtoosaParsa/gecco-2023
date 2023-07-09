import numpy as np
import random
import matplotlib.pyplot as plt
import pickle
from os.path import exists
import subprocess as sub
import sys

from switch_float import switch

# best solution from one of the runs
stiffness = np.array([9.1, 6.1, 6.8, 2.3, 7.2, 9.5, 8.5, 7.3, 1.4, 6.6, 6.5, 6.2, 7.9, 8.1, 1.6, 7.4, 4.3, 3.8, 3.9, 8.1, 9.4, 5.8, 4.9, 3.1, 9.4, 8.2, 6.3, 7.2, 5.9, 8.3])
ind1 = 29
ind2 = 2

#switch.showPacking(stiffness, ind1, ind2)
#switch.plotInOut(stiffness, ind1, ind2, noise=-50)

with open('data/means_g00.dat', "rb") as f:
    means_g00 = pickle.load(f)
f.close()
with open('data/means_g01.dat', "rb") as f:
    means_g01 = pickle.load(f)
f.close()
with open('data/means_g10.dat', "rb") as f:
    means_g10 = pickle.load(f)
f.close()
with open('data/means_g11.dat', "rb") as f:
    means_g11 = pickle.load(f)
f.close()
with open('data/std_g00.dat', "rb") as f:
    std_g00 = pickle.load(f)
f.close()
with open('data/std_g01.dat', "rb") as f:
    std_g01 = pickle.load(f)
f.close()
with open('data/std_g10.dat', "rb") as f:
    std_g10 = pickle.load(f)
f.close()
with open('data/std_g11.dat', "rb") as f:
    std_g11 = pickle.load(f)
f.close()

# add different percentages of gaussian white noise to the input signals (not the source), the percentage is percentage of the amplitude
noise = np.array([-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0.1, 10, 20, 30, 40, 50])

plt.figure(figsize=(6.4,4.8))
plt.plot(noise, means_g00, color='green', label="$Gain_{00}$", linewidth=2)
plt.fill_between(noise, np.array(means_g00)-np.array(std_g00), np.array(means_g00)+np.array(std_g00), color='green', alpha=0.2)
plt.plot(noise, means_g01, color='orange', label="$Gain_{01}$", linewidth=2)
plt.fill_between(noise, np.array(means_g01)-np.array(std_g01), np.array(means_g01)+np.array(std_g01), color='orange', alpha=0.2)
plt.plot(noise, means_g10, color='red', label="$Gain_{10}$", linewidth=2)
plt.fill_between(noise, np.array(means_g10)-np.array(std_g10), np.array(means_g10)+np.array(std_g10), color='red', alpha=0.2)
plt.plot(noise, means_g11, color='blue', label="$Gain_{11}$", linewidth=2)
plt.fill_between(noise, np.array(means_g11)-np.array(std_g11), np.array(means_g11)+np.array(std_g11), color='blue', alpha=0.2)
#plt.plot(noise, np.array(means_g00)*np.array(means_g01)*np.array(means_g10)/np.array(means_g11), color='magenta', label="$NAND-ness$")
plt.xlabel("SNR [dB]", fontsize=42)
plt.ylabel("Gain", fontsize=42)
plt.title("Robustness Analysis", fontsize=42)
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.3)
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.5)
plt.tight_layout()
plt.xticks(fontsize=32)
plt.yticks(fontsize=32)
plt.legend(loc='upper right', fontsize=32)
plt.show()

print(np.array(means_g00)*np.array(means_g01)*np.array(means_g10)/np.array(means_g11))

plt.figure(figsize=(6.4,4.8))
plt.plot(noise, np.array(means_g00)*np.array(means_g01)*np.array(means_g10)/np.array(means_g11), color='magenta')
plt.xlabel("SNR [dB]", fontsize=42)
plt.ylabel("NAND-ness", fontsize=42)
plt.title("Robustness Analysis", fontsize=42)
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.3)
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.5)
plt.tight_layout()
plt.xticks(fontsize=32)
plt.yticks(fontsize=32)
#plt.legend(loc='upper right', fontsize=32)
plt.show()

switch.plotInOut(stiffness, ind1, ind2, noise=-20)
