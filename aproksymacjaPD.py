import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

#zmodyfikowany sincus i Bessel
def fun(x, a, omega, phi, q):
    return (a*np.sin(omega * x + phi) / x) * np.i0(q*x)


numberOfPoints = 50
X = np.linspace(1, 5, num=numberOfPoints)
# Mamy X, generujemy zaszumione Y
Y = fun(x=X, a=2, omega=3, phi=4, q=1) + 1*np.random.normal(size=numberOfPoints)

# Dostanę dwie rzeczy: 1 - tablica parametrów, 2 - macierz kowariancji
params, covariance = opt.curve_fit(fun, xdata=X, ydata=Y)
plt.plot(X, Y, 'ro', label='data')    # red i punkty jako kółka
plt.plot(X, fun(X, *params), label='fit')
plt.plot(X, fun(X, 2, 3, 4, 1), label='true')
plt.legend()
plt.show()
