import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([12, 13, 30, -2, 6, 11])
cs = CubicSpline(x, y, bc_type='natural')    # warunki arbitralne jak z wykładu

numberOfPoints = 1000
xFit = np.linspace(-2, 7, numberOfPoints)
yFit = cs(xFit)

params = cs.c.T


def fun(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d


for i in range(5):
    plt.plot(xFit, fun(xFit - x[i], *params[i]))
    print(params[i])


print(params)


plt.plot(x, y, 'ro', label='data')
plt.plot(xFit, yFit, label='fit')
plt.legend()
plt.ylim(-30, 40)
plt.show()


