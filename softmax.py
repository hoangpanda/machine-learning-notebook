import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt

np.random.seed(1)
N = 2
d = 2
C = 3

X = np.random.rand(d, N) # (d,N) shape of matrix
Y = np.random.randint(0, 3, (N,))
#print(Y)


# one hot coding
def convert_labels(y, C = C):
  """
    convert 1d label to a matrix label: each column of this 
    matrix coresponding to 1 element in y. In i-th column of Y, 
    only one non-zeros element located in the y[i]-th position, 
    and = 1 ex: y = [0, 2, 1, 0], and 3 classes then return

            [[1, 0, 0, 1],
             [0, 0, 1, 0],
             [0, 1, 0, 0]]
  """
  Y = sparse.coo_matrix((np.ones_like(y), (y, np.arange(len(y)))), shape=(C,len(y))).toarray()
  return Y

# data, (row, col)

def data_display(X, labels):
#  print(X)
#  print(labels)
  #X = X.T
  X0 = X[labels==0,:]
  X1 = X[labels==1,:]
  X2 = X[labels==2,:]
#  print(X0)
  plt.plot(X0[:, 0], X0[:, 1], 'go', alpha = .5, markersize=4)
  plt.plot(X1[:, 0], X1[:, 1], '^b', alpha = .5, markersize=4)
  plt.plot(X2[:, 0], X2[:, 1], 'rs', alpha = .5, markersize=4)
  plt.show()

def soft_max_normal(z):
  # z: column
  e_z = np.exp(z)
  a = e_z/e_z.sum(axis = 0)
  return a
  
def soft_max(X, y, w_init):
  W = [w_init]
  c = w_init.shape[1]
  y = convert_labels(y, c)

#  return 1
  N = X.shape[1]  
  d = X.shape[0]
  eta = .05
  tol = 1e-4

  max_cnt = 2000
  cnt = 0
  check_w = 20
  while cnt < max_cnt:
    mix_id = np.random.permutation(N)
    for i in mix_id:
      xi = X[:, i].reshape(d, 1)
      yi = y[:, i].reshape(c, 1)
      # SGD
      ai = soft_max_normal(np.dot(W[-1].T, xi))
    #  print(np.dot(W[-1].T, xi))
      w_new = W[-1] + eta*xi.dot((yi-ai).T)
    #  print('cc:', xi.dot((yi-ai).T))
      cnt += 1

      if cnt % check_w == 0:
        if np.linalg.norm(w_new - W[-check_w]) < tol:
          return W

      W.append(w_new)
  return W


# generate data
means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

# each column is a datapoint
X = np.concatenate((X0, X1, X2), axis = 0).T 
# extended data
X = np.concatenate((np.ones((1, 3*N)), X), axis = 0)
C = 3

original_label = np.asarray([0]*N + [1]*N + [2]*N).T
#data_display(X.T, original_label)

#print(X)
#print(original_label)
C = 3

# solve
d = X.shape[0]
w_init = np.random.randn(d, C)
#print('w_init:')
#print(w_init)

W = soft_max(X, original_label, w_init)
#print('w after:')
print(W[-1])

z = np.array([[-3.20312071],
              [ 1.98314001],
              [-0.46140181]])



"""
[[0.00512   ]
 [0.91545016]
 [0.07942984]]
"""







