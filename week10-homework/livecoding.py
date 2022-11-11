#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import os

os.system("say 'Kate is great!'")
predictions = [] #predicted values
observations = [] #real values
genes = [] #gene names
descriptions = [] #gene description names based off globin

for i, line in enumerate(open(sys.argv[1])):
    if line.strip('"').startswith("##"):
        header = np.array(line.strip('"\r\n').split('\t'))
        obs_index = np.where(header == "E123")[0][0]
        #print(header)
        #print(obs_index)
    elif not line.strip('"').startswith("#"):
        fields = line.strip('"\r\n').split('\t')
        predictions.append(float(fields[4]))
        observations.append(float(fields[obs_index]))
        genes.append(fields[1])
        descriptions.append(fields[2])
        # if i < 10:
        #     print(fields)
        #     quit()


#time to make a graph
goi = ["PIM1", "SMYD3", "FADS1", "PRKAR2B", "GATA1", "MYC"]
goilocs = []

for g in goi:
    goilocs.append(np.where(np.array(genes) == g)[0][0])
for i in range(len(descriptions)):
    if "hemoglobin subunit" in descriptions[i]:
        goi.append(genes[i])
        goilocs.append(i)


cor = pearsonr(predictions, observations)
fig, ax = plt.subplots()        
ax.scatter(predictions, observations, c = "blue", s = 0.25, alpha = 1)
ax.set_xlabel("predicted K562 expression levels, \n10-fold cross validated")
ax.set_ylabel("K562 expression level (log10)")
line_xs = np.linspace(max(min(predictions) ,min(observations) ), min(max(predictions) ,max(observations)), 100)
line_ys = 0 + 1 * line_xs
ax.plot(line_xs, line_ys, c = "maroon")
ax.text(0.5, 3.75, "r^2 =" + str(round(cor.statistic**2, 2)) + "\nn = " + str(len(observations)))
for g, i in zip(goi, goilocs):
    ax.text(predictions[i], observations[i], g, color = "maroon", fontweight = "demi")
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
plt.tight_layout()
plt.savefig("3a_recreate.png")
plt.close()  