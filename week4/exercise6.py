#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
import vcfParser

CBman = np.genfromtxt("CB.qassoc",
                    dtype = None, skip_header = 1, encoding = None,
                    names = ["CHR", "SNP", "BP", "NMISS", "BETA", "SE", "R2",
                                "T", "P"])
# print(CBman[1])
# exit()
                                
a = np.argmax(-np.log(CBman["P"]))
#this is the index (row) for the values at our highest -log P, which is our SNP with the highest association
#print(a)
b = CBman["SNP"][a]
#this is the snp id for the largest -log p value
#print(b)
vcf = vcfParser.parse_vcf("gwas_data/genotypes.vcf")
# print(vcf[0])
    #vcf[0] is header
# exit()
#parsing the genotypes vcf -- we will need to match our variable b with a vcf
for i in vcf:
    if i[2] == b:
        genotype = dict(zip(vcf[0][9:], i[9:]))
        #zips the two lists together for the dictionary!
#print(genotype)
phenotype = np.genfromtxt("gwas_data/CB1908_IC50.txt",
                            dtype = None, skip_header = 1, encoding = None,
                            names = ["FID", "IID", "CB1908_IC50"])        
#print(phenotype)
ref = []
het = []
alt = []
for i in phenotype:
    d = str(i["FID"])+"_"+str(i["IID"])
    if genotype[d] == "0/0":
        if i["CB1908_IC50"] != "NA":
            ref.append(float(i["CB1908_IC50"]))
    elif genotype[d] == "0/1" or genotype[d] == "1/0":
        if i["CB1908_IC50"] != "NA":
             het.append(float(i["CB1908_IC50"]))
    elif genotype[d] == "1/1":
        if i["CB1908_IC50"] != "NA":
            alt.append(float(i["CB1908_IC50"]))
#print(alt)
fig, ax = plt.subplots()
data = [ref, het, alt]
ax.boxplot(data, labels = ["ref", "het", "alt"])
ax.set_title("phenotypic effect size of each genotypic variation")
fig.savefig("exercise6.png")
plt.close(fig)