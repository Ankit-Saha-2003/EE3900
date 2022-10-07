# Plotting y(n)

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def x(n):
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return x(n-1) + x(n-2)

def y(n):
    if n < 0:
        return 0
    else:
        return x(n-1) + x(n+1)

N = 20
n_arr = np.arange(N)
y_vec = sp.vectorize(y)

plt.stem(n_arr, y_vec(n_arr))
plt.grid()
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.savefig('../figs/fig-2.png')
plt.show()
