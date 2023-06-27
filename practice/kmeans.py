import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

np.random.seed(11)

means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500

X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

label = np.asarray([[0]*N + [1]*N + [2]*N]).T


X = np.concatenate((X0,X1,X2), axis = 0)
K = 3

def kmeans_display(X, label):
  K = max(label) + 1
  print(label)

  X0 = X[label==0,:]
  X1 = X[label==1,:]
  X2 = X[label==2,:]
  plt.plot(X0[:,0], X0[:,1], 'b^', color='red', markersize=3, alpha=.8)
  plt.plot(X1[:,0], X1[:,1], 'ro', color='blue', markersize=3, alpha=.8)
  plt.plot(X2[:,0], X2[:,1], 'rs', color='green', markersize=3, alpha=.8)
  plt.axis('equal')
  plt.show()

def kmeans_init_centers(X, K):
  return X[np.random.choice(X.shape[0], K, replace=False)]

def kmeans_assign_labels(X, centers):
  D = cdist(X, centers)
 # return D
  return np.argmin(D, axis=1)

def kmeans_update_centers(X, K, label):
  centers = np.zeros((K, X.shape[1]))
  for k in range(K):
    Xk = X[label==k, :]
    centers[k, :] = np.mean(Xk, axis=0)
  return centers;

def has_converged(new_centers, old_centers):
  return np.array_equal(new_centers, old_centers)

def kmeans(X, K):
  centers = [kmeans_init_centers(X, K)]
  label = []

  while True:
    label.append(kmeans_assign_labels(X, centers[-1]))
    new_centers = kmeans_update_centers(X, K , label[-1])

    if has_converged(new_centers, centers[-1]):
      break

    centers.append(new_centers)

  return centers, label


centers, label = kmeans(X, K)

kmeans_display(X, label[-1])



