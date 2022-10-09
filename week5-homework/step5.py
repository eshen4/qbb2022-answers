#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
import bdg_loader

d0 = bdg_loader.load_data("D0crop.bdg")
d2 = bdg_loader.load_data("D2crop.bdg")
klf4 = bdg_loader.load_data("Klf4crop.bdg")
r1 = bdg_loader.load_data("R1crop.bdg")

fig, axs = plt.subplots(4)

axs[0].bar(d0["X"], d0["Y"], width = 100, color = "c")
axs[0].set_title("D0 H3K27ac")
axs[1].bar(d2["X"], d2["Y"], width = 100, color = "m")
axs[1].set_title("D2 H3K27ac")
axs[2].bar(klf4["X"], klf4["Y"], width = 100, color = "y")
axs[2].set_title("D2 Klf4")
axs[3].bar(r1["X"], r1["Y"], width = 100)
axs[3].set_title("Sox2 R1")
plt.tight_layout()
plt.savefig("step5.png")
plt.close(fig)


