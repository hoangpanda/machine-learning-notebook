from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans

def kmeans_display(X, label):
  K = np.amax(label) + 1
  X0 = X[label == 0, :]
  #print(type(X0))
  X1 = X[label == 1, :]
  X2 = X[label == 2, :]

  plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize = 4, alpha = .5)
  plt.plot(X1[:, 0], X1[:, 1], 'go', markersize = 4, alpha = .5)
  plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize = 4, alpha = .5)
  
  plt.axis('equal')
  plt.plot()
  plt.show()

def kmeans_init_centers(X, k):
  return X[np.random.choice(X.shape[0], k, replace=False)]

def kmeans_assign_labels(X, centers): 
  d = cdist(X, centers)
  # using axis=0 for find min of value index in each column in matrix
  # using axis=1 for find min of value index in each row in matrix
  return np.argmin(d, axis=1) 

def has_converged(centers, new_centers):
    # return True if two sets of centers are the same
    return (set([tuple(a) for a in centers]) == 
        set([tuple(a) for a in new_centers]))

def kmeans_update_centers(X, label, K):
  centers = np.zeros((K, X.shape[1]))
  for k in range(K):
    Xk = X[label == k, :]
    centers[k,:] = np.mean(Xk, axis = 0)
  return centers

def kmeans(X, K):
  centers = [kmeans_init_centers(X, K)]  
  labels = []
  it = 0
  while True:
    labels.append(kmeans_assign_labels(X, centers[-1]))
    new_centers = kmeans_update_centers(X, labels[-1], K)
    if has_converged(centers[-1], new_centers):
      break
    centers.append(new_centers)
    it += 1
  return (centers, labels, it)

def kmeans_by_sklearn(X, K):
  kmeans = KMeans(n_clusters=K, random_state=0).fit(X)
  #print(kmeans.cluster_centers_)
  kmeans_display(X, kmeans.predict(X))

# init 
means = np.array([[2,2], [8,3], [3,6]])
cov = [[1,0],[0,1]]
N = 500 
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

X = np.concatenate((X0,X1,X2), axis = 0)
K = 3

original_label = np.asarray([0]*N + [1]*N + [2]*N).T

# algorithm
centers, labels, it = kmeans(X,K)
#kmeans_display(X, labels[-1])
print(centers[-1])

kmeans_by_sklearn(X,K)


