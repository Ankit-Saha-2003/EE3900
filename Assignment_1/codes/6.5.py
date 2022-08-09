# Plotting y(n) using the DFT matrix

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.linalg import dft

N = 20

def x(n):
    if n < 0 or n > 5:
        return 0
    elif n < 4:
        return n + 1
    else:
        return 6 - n

def delta(n):
    if n == 0:
        return 1
    else:
        return 0

def h(n):
    if n == 0:
        return 1
    elif n > 0:
        return delta(n) + delta(n-2) - 0.5*h(n-1)
    else:
        return 2*(delta(n+1) + delta(n-1) - h(n+1))

x_vec = sp.vectorize(x, otypes=[float])
h_vec = sp.vectorize(h, otypes=[float])

n_values = np.arange(N)
x_arr = x_vec(n_values)
h_arr = h_vec(n_values)

W = dft(N)
X = np.dot(W, x_arr)
H = np.dot(W, h_arr)
Y = X * H
y = np.dot(np.linalg.inv(W), Y)

plt.stem(n_values, np.real(y))
plt.title('Filter Output using DFT Matrix')
plt.ylabel('$y(n)$')
plt.xlabel('$n$')
plt.grid()
plt.savefig('../figs/6.5.png')
plt.show()

