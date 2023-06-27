import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')

x = [1,2,3]
y = [3,4,2]
X, Y = np.meshgrid(x,y)
Z = X*Y
print(X)
print(Y)
print(Z)


ax.plot_surface(X, Y, Z)

ax.set_xlabel('Ox')
ax.set_ylabel('Oy')
ax.set_zlabel('Oz')
plt.show()