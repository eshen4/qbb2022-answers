#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

values = [0] * 1000000
#print(values)
for i in range(150000):
    randgene = np.random.randint(0, 999900)
    #returns random integers from low to high (0 to 999900)
    for j in range(randgene, randgene+100):
        values[j] +=1
# print(np.sum(values))
x = np.array(values)

fig, ax = plt.subplots()
ax.hist(x, density=True, color = 'c')
mu = 15
#here mu is lambda
ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8)
plt.savefig("ex1_4.png")
plt.close(fig)

zeros = np.where(x==0)
print(len(zeros[0]))
poi = poisson.pmf(x, 15) * 1000000
print(poi)