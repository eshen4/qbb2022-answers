#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

#exercise 2:
pca = np.genfromtxt("plink.eigenvec",
                    dtype = None, encoding = None,
                    names = ["ID1", "ID2", "PC1", "PC2", "PC3", "PC4", "PC5", "PC6",
                                "PC7", "PC8", "PC9", "PC10"])
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

fig, ax = plt.subplots()
Pval = 10e-05
p = CBman["P"]
col = []

for i in p:
    if i < Pval:
        col.append('magenta')
    else:
        col.append('cyan')
# print(col.count('magenta'))
# exit()
ax.scatter(np.arange(len(CBman)), -np.log(CBman["P"]), c = col)
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
