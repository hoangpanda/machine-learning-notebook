from cvxopt import matrix, solvers
import numpy as np


P = matrix([[1., 0.], [0., 1.]])
q = matrix([-10., -10.])
