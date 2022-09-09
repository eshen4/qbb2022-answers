#!/usr/bin/env python

import matplotlib.pyplot as plt
#importing matplot functions to be referred to as variable plt

x = [1, 2, 3, 4, 5] #creating list to plot
y = [1, 4, 9, 16, 25] #creating list to plot

x2 = [2, 4, 6]
y2 = [8, 64, 216]

fig, ax = plt.subplots(nrows = 2)
#creates a figure and axes. subplots also allows for multiple figures/panels per plot.
#(len(ax))
ax[0].plot(x, y, label = "x^2")
ax[1].plot(x2, y2, label = "x^3")
ax[0].legend()
ax[1].legend()
plt.savefig("day3livecoding.png")
plt.close(fig)
