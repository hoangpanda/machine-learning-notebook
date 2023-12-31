# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals
import math
import numpy as np 
from matplotlib.backends.backend_pdf import PdfPages

import matplotlib.pyplot as plt

x = np.linspace(-4, 6, 1000)


def f0(x):
    return x**2 + 10*np.sin(x) + 10
def f1(x):
    return (x - 2)**2 - 4

y = f0(x)

z = f1(x)

def grad(l, x):
    return 2*x + 10*np.cos(x)+2*l*(x-2)

def Lagrange(l, x):
    return x**2 + 10*np.sin(x) + 10 + l*((x - 2)**2 - 4)
    
def sol(l, x0, eta):
    max_iter = 1000;
    it = 0
    x = x0  
    while it < max_iter:
        it += 1 
        x -= eta*grad(l, x);
        if grad(l, x)**2 < 1e-12:
            break
    return x 

p = Lagrange(0, 0)

l = np.linspace(0, 8, 100);
yl = []
for i in range(len(l)):
    x0 = sol(l[i], 1, 0.001)
    yl.append(Lagrange(l[i], x0))
    
print(np.amax(yl))
with PdfPages('dual_func2.pdf') as pdf:   
    fig = plt.figure(figsize=(6, 5)) 
    plt.plot(l, yl, 'r', linewidth = 2, label = '$g(\lambda)$')
    plt.plot([0, 8], [p, p], 'b--', linewidth = 4, label = '$p^*$')
    plt.legend(loc = "best", fontsize = 17)
    plt.ylim([-8, 12])
    plt.xlabel('$\lambda$', fontsize = 20)
    pdf.savefig() 

    plt.show()    
    plt.close()             
