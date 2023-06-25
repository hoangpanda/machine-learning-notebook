import numpy as np
import matplotlib.pyplot as plt




# height (cm)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

one = np.ones((X.shape[0],1)) 
Xbar = np.concatenate((one, X), axis=1)

A = np.dot(Xbar.T, Xbar)
B = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), B)
print(w)

w0 = w[0][0]
w1 = w[1][0]
x0 = np.linspace(145, 185)
y0 = w1*x0 + w0

plt.plot(x0, y0, 'b')
plt.plot(X, y, 'ro')
plt.axis('equal')
plt.xlabel('height (cm)')
plt.ylabel('weight (cm)')
plt.show()
