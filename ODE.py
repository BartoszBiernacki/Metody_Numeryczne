import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation


def pendulum(u, t):
    gamma = -0.1
    du = np.zeros(2)
    du[0] = u[1]
    du[1] = gamma*u[1] - np.sin(u[0])
    return du

def update(i):
    plt.clf()
    plt.axis([-2, 2, -2, 2])
    plt.plot([0, x1[i]], [0, y1[i]])
    plt.plot([x1[i]], [y1[i]], 'o')


u0 = [np.pi/2, 0]   # warunki poczatkowe
tmax = 1000     # calkowity czas symulacji
N = 2000    # liczba krokow symulacji
t = np.linspace(0, tmax, N)

wynik = odeint(pendulum, u0, t)
theta = wynik[:, 0]   # wszystkie wiersze i zerowa kolumna

x1 = np.sin(theta)
y1 = -np.cos(theta)

fig = plt.figure()
anim = animation.FuncAnimation(fig, update, frames=N, interval=20)
plt.show()