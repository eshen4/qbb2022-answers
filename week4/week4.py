#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

#exercise 2:
pca = np.genfromtxt("plink.eigenvec",
                    dtype = None, encoding = None,
                    names = ["ID1", "ID2", "PC1", "PC2", "PC3", "PC4", "PC5", "PC6",
                                "PC7", "PC8", "PC9", "PC10"])
#generating from text our plink.eigenvec file which was generated through a bash command in terminal

fig, ax = plt.subplots()
ax.scatter(pca["PC1"], pca["PC2"])
ax.set_title("genetic relatedness between principal components 1 and 2")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
plt.savefig("exercise2.png")
plt.close(fig)

#exercise 3:
af = np.genfromtxt("plink.frq",
                    dtype = None, skip_header = 1, encoding = None,
                    names = ["CHR", "SNP", "A1", "A2", "MAF", "NCHROBS"])
fig, ax = plt.subplots()
ax.hist(af["MAF"])
ax.set_title("distribution of allele frequency")
ax.set_xlabel("allelic frequency")
ax.set_ylabel("count")
plt.savefig("exercise3.png")
plt.close(fig)

#exercise 5:
CBman = np.genfromtxt("CB.qassoc",
                    dtype = None, skip_header = 1, encoding = None,
                    names = ["CHR", "SNP", "BP", "NMISS", "BETA", "SE", "R2",
                                "T", "P"])
# print(np.max(-np.log(CBman["P"])))
# exit()
a = np.argmax(-np.log(CBman["P"]))
aSNP = CBman["SNP"][a]
print(aSNP)
#this small section is actually for exercise 7 just to get the snp id for CB
fig, ax = plt.subplots()
Pval = 10e-05
#saved given pval as a separate variable
p = CBman["P"]
#saved our p values column from our generated file as a variable p to parse through with a for loop later
col = []
#empty list for the colors for each sample

for i in p:
#for variable in our p value column (saved as variable p)
    if i < Pval:
    #if the p value at the location is less than our set pval...
        col.append('magenta')
        #add the point to our color list as "magenta"
    else:
        col.append('cyan')
        #if the P value at the location is greater than or equal to our set p val, add the point to our color list as "cyan"
#i did this color part by myself!! like completely!! :) 
# print(col.count('magenta'))
# exit()
ax.scatter(np.arange(len(CBman)), -np.log(CBman["P"]), c = col)
#make our scatter with some variables -- our x is the length of our CBman file spaced out evenly, while our y is the negative log of our p values so that the highest point represents greatest association rather than the lowest (p values normally smaller is more significant). c = col defines the colors of our indvidual points.
ax.set_title("GWAS of CB1908_IC50")
ax.set_xlabel("Number of samples")
ax.set_ylabel("-log of P-values")
fig.savefig("CB_GWAS.png")
plt.close(fig)

GSman = np.genfromtxt("GS.qassoc",
                    dtype = None, skip_header = 1, encoding = None,
                    names = ["CHR", "SNP", "BP", "NMISS", "BETA", "SE", "R2",
                                "T", "P"])
b = np.argmax(-np.log(GSman["P"]))
bSNP = GSman["SNP"][b]
print(bSNP)
#this small section is actually for exercise 7 just to get the snp id for GS
fig, ax = plt.subplots()
Pval = 10e-05
p = GSman["P"]
col2 = []
for i in p:
    if i < Pval:
        col2.append('magenta')
    else:
        col2.append('cyan')
ax.scatter(np.arange(len(GSman)), -np.log(GSman["P"]), c = col2)
ax.set_title("GWAS of GS451_IC50")
ax.set_xlabel("Number of samples")
ax.set_ylabel("-log of P-values")
fig.savefig("GS_GWAS.png")
plt.close(fig)
