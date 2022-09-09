#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats
import statsmodels.api as sm

df = np.genfromtxt("penguins.csv", delimiter = ",",  
                dtype = None, 
                encoding = None,
                names = True)
rows = np.where(df["species"] == "Adelie")
df_adelie = df[rows]
df_adelie_m = df_adelie[np.where(df_adelie["sex"] == "male")]
df_adelie_f = df_adelie[np.where(df_adelie["sex"] == "female")]

#print(df_adelie_m)
#print(df)

fig, ax = plt.subplots()
ax.hist(df_adelie_m['flipper_length_mm'], alpha = 0.75, label = "male")
ax.hist(df_adelie_f['flipper_length_mm'], alpha = 0.5, label = "female")
ax.set_xlabel("flipper length (mm)")
ax.set_ylabel("number of penguins")
ax.legend()
#plt.show()

# print(stats.ttest_ind(df_adelie_m['flipper_length_mm'],
#                 df_adelie_f['flipper_length_mm']))
                
fullmodel = smf.ols(formula = "flipper_length_mm ~ 1 + species + sex", data = df).fit()
reducedmodel = smf.ols(formula = "flipper_length_mm ~1 + sex", data = df).fit()
print(sm.stats.anova_lm(reducedmodel, fullmodel, typ = 1))
#print(results.summary())
#print(results.pvalues)