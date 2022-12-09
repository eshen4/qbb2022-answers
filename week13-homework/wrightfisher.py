#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn

#part 1
def wrightfisher(allelefreq, popsize):
    genfreq = [allelefreq]
    while (allelefreq !=1) and (allelefreq !=0):
        sample = np.random.binomial(n=popsize, p=allelefreq)
        allelefreq = sample/popsize
        genfreq.append(allelefreq)
    return(genfreq)

#part 2
def lineplot(mccoy):
    x = range(len(mccoy))
    y = mccoy
    # print(x)
    # print(y)
    # exit()
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_title("allele frequency over time (af = 0.5, pop = 10)")
    ax.set_xlabel("generation number")
    ax.set_ylabel("allele frequency")
    plt.savefig("exercise2.png")
    plt.close()

tests = []
#part 3
# for i in range(1000):
#     tests.append(len(wrightfisher(0.5, 100)))
#
# print(len(tests))
# fig, ax = plt.subplots()
# ax.hist(tests)
# ax.set_title("allele frequency variation")
# ax.set_xlabel("allele frequency")
# ax.set_ylabel("proportion of variants")
# plt.savefig("exercise3.png")
# plt.close()

#part 4
# popsizes = [100, 420, 1000, 5000, 100000, 1000000]
# for i in popsizes:
#     tests.append(len(wrightfisher(0.5, i)))
# #print(len(tests))
# fig, ax = plt.subplots()
# ax.plot(popsizes, tests)
# ax.set_title("allele frequency over populations")
# ax.set_xlabel("populations")
# ax.set_xticklabels(popsizes)
# ax.set_ylabel("fixation time")
# plt.savefig("exercise4.png")
# plt.close()

#part 5
allelefreqs = [0.19, 0.28, 0.37, 0.46, 0.55, 0.64, 0.73, 0.82, 0.91, 0.99]

for i in allelefreqs:
    freqs = []
    for j in range(100):
        freqs.append(len(wrightfisher(i,100)))
    tests.append(freqs)

fig, ax = plt.subplots()
ax.violinplot(tests)
ax.set_title("variation in allele frequency with a population of 100")
ax.set_xlabel("allele frequencies")
ax.set_xticklabels(allelefreqs)
ax.set_ylabel("variants")
plt.savefig("exercise5.png")
plt.close()





