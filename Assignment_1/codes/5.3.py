# Verifying if the system is stab;e

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import scipy

def u(n):
    if n >= 0:
        return 1
    else:
        return 0

def h(n):
    return u(n) * (-0.5)**n + u(n-2) * (-0.5)**(n-2) 


vec_h = scipy.vectorize(h, otypes=[float])
N = np.arange(100)
print(np.sum(vec_h(N)))
