# Plotting v_c(t) before flipping of switch

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

def vc(t):
    if t < 0:
        return 0
    else:
        return (4/3) * (1 - np.exp(-1.5e6 * t))

vc_vec = sp.vectorize(vc)
T = np.linspace(0, 5e-6, 100)
spice = np.loadtxt('2.8.dat')

plt.plot(T, vc_vec(T), label='analytical')
plt.plot(spice[:,0], spice[:,1], 'o', label='ngspice')
plt.xlabel('$t$')
plt.ylabel('$v_c(t)$')
plt.title('Voltage across Capacitor')
plt.grid()
plt.legend()
plt.savefig('../figs/2.png')
plt.show()
