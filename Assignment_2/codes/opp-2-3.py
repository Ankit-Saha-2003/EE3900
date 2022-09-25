# Computing the step response for a given impulse response

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt

a = 0.3

N = np.arange(-10, 11)
x = np.heaviside(N, 1)
h = a**(-N) * np.heaviside(-N, 1)
y = np.convolve(x, h)

plt.stem(np.arange(-5, 6), y[15:26])
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.title('Step Response')
plt.grid()
plt.savefig('../figs/fig-1.png')
plt.show()
