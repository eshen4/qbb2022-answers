#Write a program to simulate sequencing 5x coverage of a 1Mbp genome with 100bp reads and plot the histogram of coverage. Note you do not need to actually output the sequences of the reads, you can just randomly sample positions in the genome and record the coverage. You do not need to consider the strand of each read. The start position of each read should have a uniform random probabilty at each possible starting position (1 through 999,901). You can record the coverage in an array of 1M positions. Overlay the histogram with a Poisson distribution with lambda=5

#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

values = [0] * 1000000
#print(values)
for i in range(50000):
    randgene = np.random.randint(0, 999900)
    #returns random integers from low to high (0 to 999900)
    for j in range(randgene, randgene+100):
        values[j] +=1
# print(np.sum(values))
x = np.array(values)

zeros = np.where(x==0)
print(len(zeros[0]))
poi = poisson.pmf(x, 5) * 1000000
print(poi)


fig, ax = plt.subplots()
ax.hist(x, density=True, color = 'c')
mu = 5
#here mu is lambda
ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8)
plt.savefig("ex1_2.png")
plt.close(fig)

