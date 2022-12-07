#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
import numpy.lib.recfunctions as rfn
import scipy
from scipy import stats
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import statsmodels.formula.api as smf
import statsmodels.api as sm
import pylab
from statsmodels.stats import multitest

#Part 1

input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
row_names = input_arr["t_name"]
# print(row_names)
# exit()
col_names = list(input_arr.dtype.names)

fpkm_values = input_arr[col_names[1:]]

#subset = np.array(subset)
#print(row_names)
#print(col_names)
#print(subset)
#exit()
fpkm_2d = rfn.structured_to_unstructured(fpkm_values, dtype=float)
# print(fpkm_2d)
# exit()
median = np.median(fpkm_2d, axis=1)
#print(median)
subset = fpkm_2d[np.where(median > 0)]
#print(subset)
transform = np.log2(subset + 0.1)
#print(transform)
#
# Z = linkage(transform, 'ward')
# fig = plt.figure(figsize=(10, 5))
# dn = dendrogram(Z)
# row_order = leaves_list(Z)
# plt.title("gene dendrogram")
# plt.xlabel("genes")
# plt.savefig("dendrogramcelltype.png")
#
# X = linkage(transform.T, 'ward')
# fig = plt.figure(figsize=(10, 5))
# dn = dendrogram(X)
# col_order = leaves_list(X)
# plt.title("gene dendrogram")
# plt.xlabel("genes")
# plt.savefig("dendrogramcelltypeflipped.png")
#
# fig, ax = plt.subplots()
# rows = transform[row_order,:]
# ordered = rows[:, col_order]
# im = ax.imshow(ordered,aspect="auto")
# fig.tight_layout()
# plt.savefig("heatmap.png")

#Part 2

sexes = []
stages = []
sexes = ['male', 'male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female']
stages = ['10', '11', '12', '13', '14', '10', '11', '12', '13', '14']
pval = []
bval = []
pval10 = []
bval10 = []

for i in range(transform.shape[0]):
    list_of_tuples = []
    for j in range(len(col_names[1:])):
        list_of_tuples.append((row_names[i],transform[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    leastsquares = smf.ols(formula = "fpkm ~ stage", data = longdf).fit()
    p_value = leastsquares.pvalues["stage"]
    beta = leastsquares.params["stage"]
    pval.append(p_value)
    bval.append(beta)
#print(pval)
for i in range(transform.shape[0]):
    list_of_tuples = []
    for j in range(len(col_names[1:])):
        list_of_tuples.append((row_names[i],transform[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
    leastsquares = smf.ols(formula = "fpkm ~ stage + sex", data = longdf).fit()
    p_value10 = leastsquares.pvalues["stage"]
    beta10 = leastsquares.params["stage"]
    pval10.append(p_value10)
    bval10.append(beta10)
#
# fig, ax = plt.subplots()
# sm.qqplot(np.array(pval), dist = scipy.stats.uniform, line = "45")
# plt.tight_layout()
# plt.savefig("qqplot.png")
# plt.close()

correction = multitest.multipletests(pval, alpha = 0.1, method = "fdr_bh")
reject = correction[0]
finalrows = row_names[median > 0]
# print(finalrows)
# exit()
significantrows = finalrows[reject]
#print(significantrows)
correction2 = multitest.multipletests(pval10, alpha = 0.1, method = "fdr_bh")
reject2 = correction2[0]
finalrows2 = row_names[median > 0]
# print(finalrows)
# exit()
significantrows2 = finalrows[reject2]
#print(significantrows2)
compare = set(significantrows) & set(significantrows2)
#print(compare)
percent = (len(compare)/len(significantrows))*100
#print(percent)

fig, ax = plt.subplots()
colors = []
for i in reject:
    if i == True:
        colors.append("cyan")
    else:
        colors.append("magenta")
ax.scatter(bval10, -np.log10(pval10), color = colors)
plt.savefig("volcano.png")
plt.close()