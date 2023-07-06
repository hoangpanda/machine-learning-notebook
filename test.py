import numpy as np



a = [1,2,3] 
b = [1,2,3,4]

x, y = np.meshgrid(a, b)



x1 = x.ravel().reshape(1, -1)
print(x1)