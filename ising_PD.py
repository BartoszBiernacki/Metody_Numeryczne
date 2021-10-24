import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar as root

def step(spins, M, T):
    for i in range(N):
        x = np.random.randint(N)    # losuję jeden spin do zmiany
        suma = np.sum(spins) - spins[x]
        DeltaE = 2*spins[x]*suma    # liczę różnicę energii
        if DeltaE < 0 or np.random.rand() < np.exp(-DeltaE/T):
            spins[x] *= -1
            M += 2*spins[x]
    return spins, M

def fun(x, params):
    N = params[0]
    T = params[1]
    return np.tanh((N-1)*x/T) - x


def myRoot(x, params):
    def localFunction(x):
        return fun(x, params)
    return root(localFunction, method='secant', x0=1, x1=2).root


def setAxis():
    plt.axis([T1, T2, -1.1, 1.1])
    plt.xlabel("T")
    plt.ylabel("m")


nTimeSteps = 15    # liczba krokow symulacji
N = 1000     # rozmiar układu
nTempSteps = 150    #   licza temperatur do zasymulowania
T1 = 100     # najmniejsza rozwazana temperatura układu
T2 = 2000   # najwieksza rozwazana temperatura ukladu
Temps = np.linspace(T1, T2, nTempSteps)

m = np.zeros(nTempSteps)    # tablica ze srednia magetyzacja od temperatury
i = 0   # iterator tablicy m oraz iterator progresu

fig = plt.figure()

Tdynamic = []
mDynamic = []

yTheory = []
for T in Temps:
    spins = np.ones(N)  # tablica spinow
    M = N  # magnetyzja = suma spinow
    for t in range(nTimeSteps):     #   petla obliczajaca magnetyzacje przy danej temperaturze
        spins, M = step(spins, M, T)
    m[i] = M / N    # srednia magnetyzacja
    i = i+1

    Tdynamic.append(T)
    mDynamic.append(M/N)
    yTheory.append(myRoot(M/N, [N, T]))     # wartosc teoretyczna

    #   rysuj dynamicznie bo nie chce mi sie czekac do konca symulacji
    setAxis()
    plt.plot(Tdynamic, mDynamic, label="Symulacja")
    plt.plot(Tdynamic, yTheory, label="Teoria")
    plt.legend()
    plt.pause(0.01)     # bez tego wykres sie nie uaktualnia
    plt.clf()           # czyszcze wczescniejsza serie
    print(f'{(i / len(Temps))*100: .1f} %')     # progres symulacji na konsole


setAxis()
plt.plot(Temps, m, label="Symulacja")
plt.plot(Temps, yTheory, label="Teoria")
plt.legend()
plt.show()
