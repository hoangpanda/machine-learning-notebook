import numpy as np
import matplotlib.pyplot as plt
import sys
from sklearn import datasets, neighbors # K-nearest neighbors


# load data

iris = datasets.load_iris()
iris_x = iris.data 
iris_y = iris.target 

X0 = iris_x[iris_y==0, :]
print('\nSamples from class 0:\n', X0[:5,:])

