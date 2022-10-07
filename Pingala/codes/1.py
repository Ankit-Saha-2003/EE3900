# JEE 2019

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import scipy as sp

N = 20 
alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2

def a(n):
    if n < 1:
        return 0
    else:
        return (alpha**n - beta**n) / (alpha - beta)

def b(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return a(n-1) + a(n+1)

n_arr = np.arange(1, N+1)
a_vec = sp.vectorize(a)
a_arr = a_vec(n_arr)
print(abs(sum(a_arr) - a(N+2) + 1) / sum(a_arr))

geo_arr = np.logspace(1, N, num=N, base=0.1)
a_by_ten_arr = a_arr * geo_arr
print(abs(sum(a_by_ten_arr) - 10/89))

print(abs(b(N) - alpha**N - beta**N))

b_vec = sp.vectorize(b)
b_arr = b_vec(n_arr)
b_by_ten_arr = b_arr * geo_arr
print(abs(sum(b_by_ten_arr) - 8/89))

