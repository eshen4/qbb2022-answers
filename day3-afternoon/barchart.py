#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
genesperchrom = np.genfromtxt("genes_per_chrom.txt", 
                dtype = None, 
                encoding = None, 
                names = ["gene_count", "chrom_name"])

fig, ax = plt.subplots()
ax.bar(genesperchrom["chrom_name"], genesperchrom["gene_count"])
plt.show()

# print(genesperchrom["gene_count"])
