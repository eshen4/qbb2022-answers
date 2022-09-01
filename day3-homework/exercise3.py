#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

join = np.genfromtxt("jointable.txt",
                    dtype = None, 
                    encoding = None, 
                    names = ["subj", "pop", "suppop", "sex", "fam", "PC1", "PC2", "PC3"])
#print(join[3]["PC1"])
pops = np.unique(join["pop"])
# pc1 = join["PC1"]
# pc2 = join["PC2"]
#print(pops)
#print(pop_col)

fig, ax = plt.subplots()
for pop in pops:
    x = []
    y = []
    #print(pop)
    for i in range(join.shape[0]): #for loop is pulling out individuals in the population. i represents the rows, and the .shape gives total individuals
    #for i in range(# of samples)?
        # print(pop_col[i])
        # print(pc1[i])
        if join[i]["pop"] == pop: #if the population hits a specific value in i
           x.append(join[i]["PC1"])
           y.append(join[i]["PC2"])
    ax.scatter(x, y, label = pop)
    ax.legend(loc="upper center", mode="expand", ncol=6, fontsize=5)
    ax.set_title("PC1 vs PC2 Across Population")
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
#plt.show()
fig.savefig("pop.png")
plt.close(fig)

fig, ax = plt.subplots()
suppops = np.unique(join["suppop"])
for sup in suppops:
    x = []
    y = []
    for i in range(join.shape[0]):
        if join[i]["suppop"] == sup:
            x.append(join[i]["PC1"])
            y.append(join[i]["PC2"])
    ax.scatter(x, y, label = sup)
    ax.legend()
    ax.set_title("PC1 vs PC2 Across Continental Super Populations")
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
fig.savefig("suppop.png")
plt.close(fig)

fig, ax = plt.subplots()
sexes = np.unique(join["sex"])
for sx in sexes:
    x = []
    y = []
    for i in range(join.shape[0]):
        if join[i]["sex"] == sx:
            x.append(join[i]["PC1"])
            y.append(join[i]["PC2"])
    ax.scatter(x, y, label = sx)
    ax.legend()
    ax.set_title("PC1 vs PC2 Across Sexes")
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
fig.savefig("sexes.png")

plt.close(fig)