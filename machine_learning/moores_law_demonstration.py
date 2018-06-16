#!/usr/bin/env python3

import re

import numpy as np
import matplotlib.pyplot as plt

X = []
Y = []

non_decimal = re.compile(r'[^\d]+')

for line in open('data/moore.csv'):
    r = line.split('\t')
    x = int(non_decimal.sub('', r[2].split('[')[0]))
    y = int(non_decimal.sub('', r[1].split('[')[0]))
    X.append(x)
    Y.append(y)

X = np.array(X)
Y = np.array(Y)

plt.scatter(X, Y)
plt.show()

# try this model
Y = np.log(Y)

plt.scatter(X, Y)
plt.show()

# find best line of fit
denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean() * X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator

Yhat = a*X + b

plt.scatter(X, Y)
plt.plot(X, Yhat, 'r')
plt.show()

# calculate r-squared to see how good our prediction was
d1 = Y - Yhat
d2 = Y - Y.mean()
SSres = d1.dot(d1)
SStot = d2.dot(d2)
Rsquared = 1 - SSres/SStot
print("R^2 = {}".format(Rsquared))

# log(tc) = a*year + b
# tc = exp(b) * exp(a * year)
# 2*tc = 2 * exp(b) * exp(a * year) = exp(ln(2)) * exp(b) * exp(a * year)
#      = exp(b) * exp(a * year + ln(2))
# exp(b)*exp(a*year2) = exp(b)*exp(a*year1 + ln2)
# a*year2 = a*year1 + ln2
# year2 = year1 + ln2/a
print("time to double:", np.log(2)/a, "years")
