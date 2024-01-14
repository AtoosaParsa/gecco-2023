import pickle
import matplotlib.pyplot as plt
from switch_float import switch
import constants as c
import numpy

import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

with open('nandness1_1.dat', "rb") as f:
    nandness1 = pickle.load(f)
f.close()

plt.figure(figsize=(6.4,4.8))
plt.plot(list(range(1, 55)), nandness1, color='blue', linewidth=2)
plt.xlabel("Frequency", fontsize=42)
plt.ylabel("NAND-ness", fontsize=42)
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.3)
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.5)
plt.minorticks_on()
plt.xticks(fontsize=28)
plt.yticks(fontsize=28)
#plt.ylim((0, 0.77))
plt.tight_layout()
plt.show()

with open('nandness2_1.dat', "rb") as f:
    nandness2 = pickle.load(f)
f.close()

plt.figure(figsize=(6.4,4.8))
plt.plot(list(range(1, 55)), nandness2, color='blue', linewidth=3)
plt.xlabel("Frequency", fontsize=32)
plt.ylabel("NAND-ness", fontsize=32)
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.3)
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.5)
plt.minorticks_on()
plt.xticks(fontsize=28)
plt.yticks(fontsize=28)
from matplotlib.ticker import StrMethodFormatter
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
#plt.ylim((0, 0.77))
plt.tight_layout()
plt.show()

with open('gains00_1.dat', "rb") as f:
    gains00 = pickle.load(f)
f.close()
with open('gains01_1.dat', "rb") as f:
    gains01 = pickle.load(f)
f.close()
with open('gains10_1.dat', "rb") as f:
    gains10 = pickle.load(f)
f.close()
with open('gains11_1.dat', "rb") as f:
    gains11 = pickle.load(f)
f.close()

plt.figure(figsize=(6.4,4.8))
plt.plot(list(range(1, 55)), gains00, color='orange', linewidth=2, label='$Gain_{00}$')
plt.plot(list(range(1, 55)), gains01, color='magenta', linewidth=2, label='$Gain_{01}$')
plt.plot(list(range(1, 55)), gains10, color='green', linewidth=2, label='$Gain_{10}$')
plt.plot(list(range(1, 55)), gains11, color='red', linewidth=2, label='$Gain_{11}$')
plt.xlabel("Frequency", fontsize=32)
plt.ylabel("Gains", fontsize=32)
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.3)
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.5)
plt.minorticks_on()
plt.xticks(fontsize=28)
plt.yticks(fontsize=28)
from matplotlib.ticker import StrMethodFormatter
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
plt.legend(loc='upper right', fontsize=32)
plt.tight_layout()
plt.show()
