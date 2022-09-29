#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import vcfParser

vcf = vcfParser.parse_vcf(sys.argv[1])
readdepth = [] #4
qualitydist = [] #1
allelefreq = [] #7
predictedeff = [] #2
#making all my empty lists
for i in vcf[1:]:
    for j in i[9:]:
        readdepth.append(j[4])
        qualitydist.append(j[1])
    allelefreq.append(i[7]['AF'])
    eff = i[7]['ANN']
    predeff = eff.split('|')
    predictedeff.append(predeff[2])
        
#go through vcf line by line
#for each line...
    #pull out individual plotted value
    #append into a list
effect = {}
for i in predictedeff:
    if i in effect.keys():
        effect[i] += 1
    else:
        effect[i] = 1

#dictionary to better parse through the info column

readdepth = [int(d) for d in readdepth if d != '.']
qualitydist = [float(d) for d in qualitydist if d != '.']
allelefreq = [float(d) for d in allelefreq if d != '.']
#the previous values that were parsed through by the vcf parser are saved as strings. this isn't going to work in our graphs

fig, axs = plt.subplots(2,2)
#setting up our plots to be 2 by 2 for a total of four figures
axs[0,0].hist(readdepth, density=True)
axs[0,0].set_title("depth of read distribution")
axs[0,0].set_xlabel("read depth")
axs[0,0].set_ylabel("probability of occurrence")
axs[0,0].set_yscale("log")
axs[0,1].hist(qualitydist, density=True)
axs[0,1].set_title("quality distribution")
axs[0,1].set_xlabel("quality")
axs[0,1].set_ylabel("count")
axs[1,0].hist(allelefreq, density=True)
axs[1,0].set_title("distribution of allele frequency")
axs[1,0].set_xlabel("allele frequency")
axs[1,0].set_ylabel("count")
axs[1,1].bar(effect.keys(), effect.values())
axs[1,1].set_title("predicted effects")
axs[1,1].set_xlabel("allelic effects")
axs[1,1].set_ylabel("count")
plt.tight_layout()
plt.savefig("step8.png")