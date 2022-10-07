#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
import vcfParser

CBman = np.genfromtxt("CB.qassoc",
                    dtype = None, skip_header = 1, encoding = None,
                    names = ["CHR", "SNP", "BP", "NMISS", "BETA", "SE", "R2",
                                "T", "P"])
# generating from text my CB.qassoc file to read through the P values and find the correct SNP                        
a = np.argmax(-np.log(CBman["P"]))
#this is the index (row) for the values at our highest -log P, which is our SNP with the highest association
#print(a)
b = CBman["SNP"][a]
#this is the snp id for the largest -log p value (what we were trying to find)
#print(b)
vcf = vcfParser.parse_vcf("gwas_data/genotypes.vcf")
# print(vcf[0])
    #vcf[0] is header
# exit()
#parsing the genotypes vcf -- we will need to match our variable b with a vcf
for i in vcf:
#for variables in our parsed vcf...
    if i[2] == b:
    #if our SNP id (i[2] is the index for the SNP id) is equal to the id we obtained for variable b (associated to most significant P value)
        genotype = dict(zip(vcf[0][9:], i[9:]))
        #zips the two lists together for the dictionary - vcf header columns 9 and on, with the actual data in columns 9 and on (this is our genotype data!)
#print(genotype)
phenotype = np.genfromtxt("gwas_data/CB1908_IC50.txt",
                            dtype = None, skip_header = 1, encoding = None,
                            names = ["FID", "IID", "CB1908_IC50"])        
#generating from text my phenotypic data
#print(phenotype)
ref = []
het = []
alt = []
#establishing three empty lists for the reference, alternate, and heterozygous genotypes
for i in phenotype:
#for variable in our phenotype text
    d = str(i["FID"])+"_"+str(i["IID"])
    #establishing a variable to represent what we're looking for as a string. this is necessary because the vcf for our genotype data wrote the header differently compared to the phenotype data
    if genotype[d] == "0/0":
    #if the data connected to our string key in our genotype dictionary is equal to "0/0"...
        if i["CB1908_IC50"] != "NA":
        #another if statement because some of the phenotype data says "NA" instead of an actual value, so this is just saying if our value is NOT equal to that (we don't want NA)
            ref.append(float(i["CB1908_IC50"]))
            #append the values as floats at our location i in our third column of our phenotype file into our reference list
    elif genotype[d] == "0/1" or genotype[d] == "1/0":
    #same as above except this or statement is necessary because the vcf file wrote some hets as 1/0 and some as 0/1
        if i["CB1908_IC50"] != "NA":
             het.append(float(i["CB1908_IC50"]))
    elif genotype[d] == "1/1":
        if i["CB1908_IC50"] != "NA":
            alt.append(float(i["CB1908_IC50"]))
#print(alt)

fig, ax = plt.subplots()
#establishing the plot
data = [ref, het, alt]
#made a list for our data in the order ref, het, alt (previously defined variables)
ax.boxplot(data, labels = ["ref", "het", "alt"])
#plots our data variable all next to each other on the same figure axes but with different boxplots for each
ax.set_title("phenotypic effect size of each genotypic variation")
#set title for figure
fig.savefig("exercise6.png")
plt.close(fig)