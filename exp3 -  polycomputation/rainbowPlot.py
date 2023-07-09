from glob import glob
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pickle
from switch_float import switch
import constants as c
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

sns.set_style("ticks")
sns.set_palette("hls", 8)

runs = c.RUNS
gens = c.numGenerations

#run_directory = "/home/sam/Archive/skriegma/XENO_3/run_{}/".format(RUN)
#all_of_gen_files = glob(run_directory + "allIndividualsData/Gen_*.txt")
#sorted_all_of_gen_files = sorted(all_of_gen_files, reverse=False)

line_hist = []
gen_age_fit_dict = {}

for gen in range(gens):
    gen_age_fit_dict[gen] = {0: 100.0}
    filename = 'gens1/gen{}.dat'.format(str(gen))
    temp = []
    with open(filename, "rb") as f:
        temp = pickle.load(f) # this is the population of this gen
        for i in range(len(temp)):
            this_fit = -1 * temp[i].indv.fitness
            this_age = temp[i].age

            if this_age not in gen_age_fit_dict[gen]:  # ord by fit anyway
                gen_age_fit_dict[gen][this_age] = this_fit  # most fit at each age level
            elif this_fit < gen_age_fit_dict[gen][this_age]:
                gen_age_fit_dict[gen][this_age] = this_fit
    f.close()
    #print(gen_age_fit_dict)
    #print("gen: "+str(gen))
    if gen > 0:
        for age in gen_age_fit_dict[gen-1]:

            if age+1 not in gen_age_fit_dict[gen] or gen == gens-1:  # extinction

                this_line = []
                n = 0
                #print("age "+str(age))
                while age-n > -1:
                    #if age not in gen_age_fit_dict[gen-1-n]:
                    #    break
                    this_line += [gen_age_fit_dict[gen-1-n][age-n]] # * 6 / 8.0]
                    n += 1
                # if len(this_line) > 1 and this_line[1] > this_line[0]:
                #     print this_line
                #print(this_line)
                #print(this_line[::-1])
                pre_fill = [None]*(gen-age)
                # post_fill = [None]*(gens-gen)
                line_hist += [pre_fill + list(this_line[::-1])]
                
#print(gen_age_fit_dict[gen])

fig, ax = plt.subplots(1, 1, figsize=(4, 3))

for line in line_hist:
    ax.plot(range(len(line)), line, linewidth=0.8)

ax.set_xlim([-10, gens])
ax.set_ylim([-0.1, 1])
#ax.text(50, 7, "Run {}".format(RUN), fontsize=20)
# ax.set_ylabel('Displacement')
# ax.set_xlabel('Generation')
# ax.set_xticklabels([0, 0, 200/50, 400/50, 600/50, 800/50, 1000/50], fontsize=12)
#ax.set_xticklabels([0, 0, 200, 400, 600, 800, 1000], fontsize=12)
#ax.set_yticklabels([0, 0, 2, 4, 6, 8], fontsize=12)
plt.xlabel("Generations")
plt.ylabel("Fitness")
plt.minorticks_on()
#plt.xticks(fontsize=28)
#plt.yticks(fontsize=28)
sns.despine()
plt.tight_layout()
plt.savefig("plot.png", bbox_inches='tight', dpi=600)
