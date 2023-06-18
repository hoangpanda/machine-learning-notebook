# import library important
from __future__ import print_function, division, unicode_literals
from sklearn import datasets, linear_model

# numpy using for process matrix
import numpy as np 
# matplotlib.pylot using for visualize data
import matplotlib.pyplot as plt

# height (cm)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

"""
plt.xlabel('height (cm)')
plt.ylabel('weight (cm)')
# plt.axis([min_ox, max_ox, min_oy, max_oy])
plt.axis([140, 190, 45, 75]) 
plt.plot(X, y, 'ro')
plt.show()
"""

# building model

# building Xbar 
one = np.ones((X.shape[0],1))
Xbar = np.concatenate((one,X), axis=1)

# calculating weights of the fitting line
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A),b)

# preparing fitting line
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(145, 185 , num=2, endpoint=True)
y0 = w_1*x0 + w_0

# drawing fitting line

plt.plot(X,y, 'ro')
plt.plot(x0,y0)
plt.axis([140, 190, 45, 75])
plt.xlabel('height (cm)')
plt.ylabel('weight (cm)')
plt.show()

# fit model by linear regression

# enable fit_intercept=False for calculating bias (w_0)
regr = linear_model.LinearRegression(fit_intercept=False)
regr.fit(Xbar, y)

print(w.T)
print(regr.coef_)