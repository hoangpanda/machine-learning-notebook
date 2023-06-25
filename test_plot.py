import numpy as np
import matplotlib.pyplot as plt
import random

np.random.seed(2)

N = 10

#print(np.random.permutation(N)) 

x = np.array([1,2,3,4])
y = np.array([1,2,3,9])
z = np.dot(x.T, y)
print(np.sign(z)[0])

