import numpy as np
import matplotlib.pyplot as plt


np.random.seed(2)


means = [[2, 2], [4, 2]]
cov = [[.3, .2], [.2, .3]]
N = 10

X0 = np.random.multivariate_normal(means[0], cov, N).T
X1 = np.random.multivariate_normal(means[1], cov, N).T

X = np.concatenate((X0,X1), axis=1)

y = np.concatenate((np.ones((1, N)), -1*np.ones((1,N))), axis=1)

y_label = y[0]

Xbar = np.concatenate((np.ones((1, 2*N)), X), axis=0)

x_1 = X[0][y_label==1]
y_1 = X[1][y_label==1]

x_2 = X[0][y_label==-1]
y_2 = X[1][y_label==-1]



# algorithm

def h(w, x):
  return np.sign(np.dot(w.T, x))

def has_converged(X, y, w):
  return np.array_equal(h(w, X), y)

def perceptron_1(X, y, w_init):
  w = [w_init]
  d = X.shape[0]
  N = X.shape[1]
  #print(d)
  
  while True:
    mix_id = np.random.permutation(N)
    for i in range(N):
      xi = X[:, mix_id[i]].reshape(d,1) # data
      yi = y[0, mix_id[i]] # label
      if h(w[-1], xi)[0] != yi:
        w_new = w[-1] + xi*yi
        w.append(w_new)

    if has_converged(X, y, w[-1]):
      break
   # print('cc')
  return w

def perceptron_2(X, y, w_init):
    w = [w_init]
    N = X.shape[1]
    mis_points = []
    while True:
        # mix data 
        mix_id = np.random.permutation(N)
        for i in range(N):
            xi = X[:, mix_id[i]].reshape(3, 1)
            yi = y[0, mix_id[i]]
            if h(w[-1], xi)[0] != yi:
                mis_points.append(mix_id[i])
                w_new = w[-1] + yi*xi 

                w.append(w_new)
                
        if has_converged(X, y, w[-1]):
            break
    return (w)
  

def draw_line(w):
  w0, w1, w2 = w[0], w[1], w[2]
  if w2 != 0:
    x11, x12 = 1, 5
    return plt.plot([x11, x12], [-(w0 + x11*w1)/w2, -(w0 + x12*w1)/w2], 'k')
    

# init w_init

d = Xbar.shape[0]
w_init = np.random.rand(d, 1)

w_answer = perceptron_1(Xbar, y, w_init)

#print(w_answer)


#draw_line(w_answer)
#plt.plot(x_1, y_1, '^b', color='red')
#plt.plot(x_2, y_2, 'ro', color='blue')
#plt.axis('equal')
#plt.xlim(1,8)
#plt.ylim(1,5)
#plt.show()


# animation
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation


