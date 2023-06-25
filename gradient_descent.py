import numpy as np

def grad(x):
  return 2*x - (np.cos(x))**2 + (np.sin(x))**2

def cost(x):
  return x**2 - (np.sin(x))*(np.cos(x))


def GD1(x, eta):
  it = 0
  for i in range(20000):
    x = x - eta*grad(x)
    it += 1
    if abs(grad(x)) < 1e-3:
      break

  return (x,it)

def GD2(x, eta, alpha):
  it = 0
  v1 = 0
  for i in range(20000):
    v1 = v1*alpha - eta*grad(x)
    x = x + v1
    it += 1
    if abs(grad(x)) < 1e-3:
      break

  return (x,it)

def GD3(x, eta, alpha):
  it = 0
  v1 = 0
  for i in range(20000):
    v1 = x - v1
    x = x - v1
    it += 1
    if abs(grad(x)) < 1e-3:
      break
  return (x,it)

x, it = GD1(5, 0.1)
print(x)
print(it)


x1, it1 = GD2(x, 0.1, 0.9)
print(x1)
print(it1)

x2, it2 = GD3(x, 0.1, 0.9)
print(x2)
print(it2)