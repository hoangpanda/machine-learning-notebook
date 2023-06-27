import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis=1)

regr = linear_model.LinearRegression(fit_intercept=False)
regr.fit(Xbar, y)

print(regr.coef_)