#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats
import statsmodels.api as sm

df = np.genfromtxt("joinfull.txt",
                    dtype = None, 
                    encoding = None,
                    names = ["Proband_id", "Father_count", 
                            "Mother_count", "Father_age", "Mother_age"])

fig, ax = plt.subplots()
ax.scatter(df["Mother_age"], df["Mother_count"], label = "Maternal mutation count vs age")
ax.set_xlabel("Mother age")
ax.set_ylabel("Maternal mutation count")
plt.savefig("ex2_a.png")
plt.close(fig)

fig, ax = plt.subplots()
ax.scatter(df["Father_age"], df["Father_count"], label = "Paternal mutation count vs age")
ax.set_xlabel("Father age")
ax.set_ylabel("Paternal mutation count")
plt.savefig("ex2_b.png")

plt.close(fig)

mommodel = smf.ols(formula = "Mother_count ~ 1 + Mother_age", data= df).fit()
popmodel = smf.ols(formula = "Father_count ~ 1 + Father_age", data= df).fit()
print(mommodel.summary())
print(popmodel.summary())

fig, ax = plt.subplots()
ax.hist(df["Mother_count"], alpha = 0.75, label = "female")
ax.hist(df["Father_count"], alpha = 0.5, label = "male")
ax.set_xlabel("Mutation count")
ax.set_ylabel("Frequency of mutations")
ax.legend()
plt.savefig("ex2_c.png")
plt.close(fig)

print(stats.ttest_ind(df["Mother_count"],
                df["Father_count"]))
                
new_data = df[0]
new_data.fill(0)
new_data["Father_age"] = 50.5
print(popmodel.predict(new_data))