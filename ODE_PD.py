import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation


def pendulum(u, t):
    theta1 = u[0]
    omega1 = u[1]
    theta2 = u[2]
    omega2 = u[3]

    du = np.zeros(4)

    du[0] = omega1
    newOmega1Licznik = -3*np.sin(theta1) - np.sin(theta1 - 2*theta2) - 2*np.sin(theta1 - theta2)*(pow(omega2, 2) + pow(omega1, 2)*np.cos(theta1 - theta2))
    newOmega1Mianownik = 3 -np.cos(2*theta1 - 2*theta2)
    du[1] = newOmega1Licznik/newOmega1Mianownik

    du[2] = omega2
    newOmega2Licznik = 2*np.sin(theta1 - theta2)*(2*pow(omega1, 2) + 2*np.cos(theta1) + pow(omega2, 2)*np.cos(theta1 - theta2))
    newOmega2Mianownik = 3 - np.cos(2*theta1 - 2*theta2)
    du[3] = newOmega2Licznik/newOmega2Mianownik
    return du


def update(i):
    plt.clf()
    plt.axis([-3, 3, -3, 1])
    plt.plot([0, x1[i]], [0, y1[i]])
    plt.plot([x1[i]], [y1[i]], 'o')
    plt.plot([x1[i], x2[i]], [y1[i], y2[i]])
    plt.plot([x2[i]], [y2[i]], 'o')


u0 = [np.pi/2, 0, np.pi/2, 0]   # warunki poczatkowe
tmax = 2000     # calkowity czas symulacji
N = 5000    # liczba krokow symulacji
t = np.linspace(0, tmax, N)

wynik = odeint(pendulum, u0, t)
theta1 = wynik[:, 0]   # wszystkie wiersze i zerowa kolumna
theta2 = wynik[:, 2]

x1 = np.sin(theta1)
y1 = -np.cos(theta1)
x2 = x1 + np.sin(theta2)
y2 = y1 - np.cos(theta2)

fig = plt.figure()
anim = animation.FuncAnimation(fig, update, frames=N, interval=(1000/60))
plt.show()
