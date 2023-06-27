import numpy as np 
from mnist import MNIST # require `pip install python-mnist`
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#
mndata = MNIST('../MNIST/') # path to your MNIST folder 

