#!/usr/bin/env python3

"""
Linear regression where y is cubic
"""

import numpy as np
import matplotlib.pyplot as plt

# load the data
X = []
Y = []
for line in open('data/data_poly.csv'):
    x, y = line.split(',')
    x = float(x)
    X.append([1, x, x*x])
    Y.append(float(y))

# conver to numpy arrays
X = np.array(X)
Y = np.array(Y)

# plot data
plt.scatter(X[:,1], Y)
plt.show()

# calculate weights
w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))
print(w)
Yhat = np.dot(X, w)

# plot it all together
plt.scatter(X[:,1], Y)
plt.plot(sorted(X[:,1]), sorted(Yhat))
plt.show()

# compute R^2
d1 = Y - Yhat
d2 = Y - Y.mean()
SSres = d1.dot(d1)
SStot = d2.dot(d2)
Rsquared = 1 - SSres/SStot
print("R^2 = {}".format(Rsquared))
