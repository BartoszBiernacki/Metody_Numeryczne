import numpy as np


def fun(x):
    return - np.log(1-x)/x


x = np.arange(0.001, 0.99999, 1e-3)
y = fun(x)

np.set_printoptions(precision=10)
# print(*y.tolist(), sep="\n")
print(*x.tolist(), sep="\n")