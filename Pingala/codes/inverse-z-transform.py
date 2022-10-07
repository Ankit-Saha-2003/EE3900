# Finding the inverse Z-transform of a rational function

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import sympy
from lcapy.discretetime import z

def invZ(num, den):
    N = np.sum(num * np.logspace(0, len(num) - 1, num=len(num), base=z))
    D = np.sum(den * np.logspace(0, len(den) - 1, num=len(den), base=z))
    return (N/D).IZT()

sympy.pprint(invZ([1], [1, -1, -1]))
sympy.pprint(invZ([1, 2], [1, -1, -1]))
