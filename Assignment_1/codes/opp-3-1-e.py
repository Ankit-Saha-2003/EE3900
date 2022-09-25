# Computing the Z-transform of a given signal

# Name: Ankit Saha
# Roll number: AI21BTECH11004

from lcapy import delta
from lcapy.discretetime import n

x = delta(n - 1)
X = x.ZT()
print(X)
