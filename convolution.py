import numpy as np

x = np.array([[2], [-1]])
h = np.array([[-1], [2], [1]])

m = h.shape[0]

toeplitz_h = np.zeros((2 * m - 2, m - 1))

for i in range(m - 1):
    for j in range(i + 1):
        toeplitz_h[i, j] = h[i - j]

for i in range(m - 1, 2 * m - 2):
    for j in range(i - m + 1, m - 1):
        toeplitz_h[i, j] = h[i - j]

y = np.dot(toeplitz_h, x)
print(y, '\n')
print(np.convolve(x.T[0], h.T[0]))
