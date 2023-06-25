import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')

x_data = np.arange(0,50, .1)
y_data = np.arange(0,50, .1)
z_data = np.sin(x_data)*np.cos(y_data)

X, Y = np.meshgrid(x_data, y_data)
Z = X*Y

ax.plot_surface(X, Y, Z)


plt.show()