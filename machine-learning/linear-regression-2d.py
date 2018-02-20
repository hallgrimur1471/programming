#!/usr/bin/env python3

"""
Linear regression where every x is multi dimensional
(2d in this case)
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# load the data
X = []
Y = []
for line in open('data/data_2d.csv'):
    x1, x2, y = line.split(',')
    X.append([float(x1), float(x2), 1])
    Y.append(float(y))

# turn X and Y into numpy arrays
X = np.array(X)
Y = np.array(Y)

# pot the data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], Y)
plt.show()

# calculate weights
w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Y))

Yhat = np.dot(X, w)

# compute R^2
d1 = Y - Yhat
d2 = Y - Y.mean()
SSres = d1.dot(d1)
SStot = d2.dot(d2)
Rsquared = 1 - SSres/SStot
print("R^2 = {}".format(Rsquared))
