import numpy as np
import matplotlib.pyplot as plt


def step(spins, M, T):
    for i in range(N):
        x = np.random.randint(N)    # losuję jeden spin do zmiany
        suma = np.sum(spins) - spins[x]
        DeltaE = 2*spins[x]*suma    # liczę różnicę energii
        if DeltaE < 0 or np.random.rand() < np.exp(-DeltaE/T):
            spins[x] *= -1
            M += 2*spins[x]
    return spins, M

nsteps = 100    # liczba krokow symulacji
N = 1000     # rozmiar układu
T = 1000     # temperatura układu

spins = np.ones(N)  # tablica spinow
M = N   # magnetyzja = suma spinow
m = np.zeros(nsteps)    # tablica magnetyzacji na spin w kolejnych krokach czasowych

for t in range(nsteps):
    spins, M = step(spins, M, T)
    m[t] = M/N

fig = plt.figure()
plt.axis([0, nsteps, -1.1, 1.1])
plt.plot(range(nsteps), m)
plt.show()
