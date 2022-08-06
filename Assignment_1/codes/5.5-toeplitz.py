# Plotting the convolution of x(n) and h(n) by using a Toeplitz matrix
# y(n) = x(n) (*) h(n)

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt
import scipy

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

vec_x = scipy.vectorize(x, otypes=[float])
vec_h = scipy.vectorize(h, otypes=[float])

N = np.linspace(0, 19, 20)
x_array = vec_x(N)
h_array = vec_h(N)

m = h_array.shape[0]
toeplitz_h = np.zeros((2 * m - 1, m))

for i in range(m):
    for j in range(i + 1):
        toeplitz_h[i, j] = h_array[i - j]

for i in range(m, 2 * m - 1):
    for j in range(i - m + 1, m):
        toeplitz_h[i, j] = h_array[i - j]

y_array = np.dot(toeplitz_h, x_array)

plt.stem(N, y_array[:20])
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.title('Filter Output using Convolution by Toeplitz Matrix')
plt.savefig('../figs/5.5-toeplitz.png')
plt.show()
