import numpy as np
import matplotlib.pyplot as plt

# height
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T



one = np.ones((1,X.shape[0])).T
Xbar = np.concatenate((one, X), axis = 1)

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)

w = np.dot(np.linalg.pinv(A), b)
print(w)

# find min X

w0 = w[0][0]
w1 = w[1][0]

x_g = np.linspace(X.min() - 10, X.max() + 10, 2)
y_g = w1*x_g + w0

plt.plot(X, y, 'ro')
plt.plot(x_g, y_g, 'g', color='blue')
plt.axis('equal')
plt.show()