import numpy as np
import time

import  scipy.integrate as calka

def trapez(f, a, b, h):
    x = np.arange(a, b+h, h)       # range(a, b, h) zrobi lsiste od a do b-h
    s = np.sum((f(x))) - 0.5*f(a) - 0.5*f(b)
    return s*h


def fun(x):
    return np.sin(x)

a = 0
b = np.pi
h = (b-a) / 100000000

t1 = time.perf_counter()
c = trapez(fun, a, b, h)
t2 = time.perf_counter()
print(f'wynik = {c} \t \t czas:{t2 - t1}')

t1 = time.perf_counter()
c = calka.quad(fun, a, b) [0]   # [0] zeby wyswietlic pierwszy wynik krotki (nie chcemy wyswietlac niepewnosci)
t2 = time.perf_counter()
print(f'wynik = {c} \t \t czas:{t2 - t1}')