#!/usr/bin/env python3

"""
Calculates best line of fit and determines how good the fit was
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    # load the data
    X = []
    Y = []
    for line in open('data/data_1d.csv'):
        x, y = line.split(',')
        X.append(float(x))
        Y.append(float(y))
    X = np.array(X)
    Y = np.array(Y)

    plt.scatter(X, Y)
    plt.show()

    # solution to best line of fit
    # y_hat_i = a*x_i + b
    denominator = X.dot(X) - X.mean()**2
    a = (X.dot(Y) - X.mean()*Y.mean()) / denominator
    b = (Y.mean()*X.dot(X) - X.mean()*X.dot(Y)) / denominator

    # calculated predicted Y
    Yhat = a*X + b

    # plot result
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

if __name__ == "__main__":
    main()
