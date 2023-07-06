import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
  return x**2 + 10*np.sin(x) + 10

def g(x):
  return (x-2)**2 - 4


def grad(l, x):
  return 2*x + 10*np.cos(x) + 2*l*(x-2)

def lagrangian(l, x):
  return f(x) + l*g(x)






def find_m(l):
  eta = 0.001
  x = 1
  max_iter = 1000
  it = 0
  while it < max_iter:
    x = x - eta*grad(l, x)
    it += 1
    if abs(grad(l,x)**2) < 1e-12:
      break
  return x


x = np.linspace(-4, 6, 1000)
y = f(x)
e = g(x)
l = np.linspace(0, 8, 100)
y_l = []


for i in l:
  # i = lambda = l
  y_min = find_m(i)
  y_l.append(lagrangian(i, y_min))


plt.plot(l, y_l, 'r', linewidth=2) 
plt.plot([0, 8], [10, 10], 'b--', linewidth=3)
plt.show()


"""
plt.figure(figsize=(6,5))
plt.plot([0, 0], [-50, 120], 'k-')
plt.plot([4, 4], [-50, 120], 'k-')

d = np.linspace(0.2, 10, 10)

for j in d:
  plt.plot(x, y + j*e, 'r:')

plt.plot(x, y, 'b', linewidth=2.5, label='$f(x)$')
plt.plot(x, e, 'g--', linewidth=1.5, label = '$f_1(x)$')
plt.plot(x, y+j*e, 'r:', label='$f_0(x) + \lambda f_1(x)$')

plt.ylim([-30, 40])
plt.legend(loc='best', fontsize=17)
plt.xlabel('$x$', fontsize=17)
plt.show()

"""


