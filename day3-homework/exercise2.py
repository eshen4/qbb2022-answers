#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np

pca = np.genfromtxt("plink.eigenvec",
                    dtype = None,
                    encoding = None,
                    names = ["ID1",  "ID2", "PC1", "PC2", "PC3"])
#print(pca)
#print(pca.shape)

fig, ax = plt.subplots()
ax.scatter(pca["PC1"], pca["PC2"], label = "PCA 1 and 2")

ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
#plt.show()
plt.savefig("ex2_a.png")

fig, ax = plt.subplots()
ax.scatter(pca["PC1"], pca["PC3"], label = "PCA 1 and 3")
ax.set_xlabel("PC1")
ax.set_ylabel("PC3")
plt.savefig("ex2_b.png")
plt.close(fig)