import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


def fun(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d


numberOfPoints = 30
X = np.linspace(-5, 5, num=numberOfPoints)
# Mamy X, generujemy zaszumione Y
Y = fun(x=X, a=2, b=-5, c=4, d=-1) + 30*np.random.normal(size=numberOfPoints)

# Dostanę dwie rzeczy: 1 - tablica parametrów, 2 - macierz kowariancji
params, covariance = opt.curve_fit(fun, xdata=X, ydata=Y)
plt.plot(X, Y, 'ro')    # red i punkty jako kółka
# plt.plot(X, fun(X, params[0], params[1], params[2], params[3]))
plt.plot(X, fun(X, *params))    # równoważne z powyższym ale bardziej elastyczne
plt.plot(X, fun(X, 2, -5, 4, -1))
plt.show();

np.set_printoptions(precision=3, suppress=True)  #dokładność do trzech cyfr i bez notacji wykładniczej
print(params)
print(covariance)
print(np.sqrt(np.diag(covariance)))    #odchylenia standardowe

