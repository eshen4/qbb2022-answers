#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )

fig, ax = plt.subplots()
ax.hist( ac, density=True )
ax.set_yscale("log")
ax.set_ylim([10e-6, 0.005])
ax.set_title(vcf)
#plt.show()
fig.savefig( vcf + "update.png" )

fs.close()

