# Plotting x(n)

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

N = 20
n_arr = np.arange(N)
x_vec = sp.vectorize(x)

plt.stem(n_arr, x_vec(n_arr))
plt.grid()
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.savefig('../figs/fig-1.png')
plt.show()
