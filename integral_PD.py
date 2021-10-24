import numpy as np
import time
import scipy.integrate as calka


def trapez(f, a, b, h):
    x = np.arange(a, b+h, h)       # range(a, b, h) zrobi lsistę od a do b-h dlatego b+h
    s = np.sum((f(x))) - 0.5*f(a) - 0.5*f(b)
    return s*h


def fun(x):
    return np.sin(np.sinh(x))


def richardson(f, a, b, k):
    integrals = np.zeros((k+1, k+1))    # ilosc elem w tablicy o 1 wieksza niz k
    for row in range(len(integrals)):     # oblicz I[x][0] (sumowanie)
        h = ( (b-a)/10) / pow(base=2, exp=row)
        x = np.arange(a, b + h, h)
        s = np.sum((f(x))) - 0.5 * f(a) - 0.5 * f(b)
        integrals[row][0] = s*h                             # macierz [wiersz][kolumna]
    for col in range(len(integrals)):               # oblicz macierz całek (ekstrapolacja)
        for row in range(len(integrals)):
            if(row + (col+1) <= k):
                integrals[row][col+1] = (pow(4, col+1)*integrals[row+1][col] - integrals[row][col])/(pow(4, col+1)-1)
    # print(integrals)      # <-- można odkomentować i sobie podejrzeć macierz całek Richardsona
    return integrals[0][k]


a = 0
b = 5
h = (b-a) / 100000000

c = 1
t = 1

print("\nW ramach eksperymentowania testowałem różne funkcje\n"
      "poniższy wynik jest dla f(x) = sin(sinh(x)) od 0 do 5\n")

t1 = time.perf_counter()
c = trapez(fun, a, b, h)
t2 = time.perf_counter()
print(f'Wynik = {c: .15f} \t czas:{t2 - t1: .15f}   Metoda z zajec')

t1 = time.perf_counter()
c = calka.quad(fun, a, b)[0]   # [0] zeby wyswietlic tylko pierwszy wynik krotki (nie chcemy wyswietlac niepewnosci)
t2 = time.perf_counter()
print(f'Wynik = {c: .15f} \t czas:{t2 - t1: .15f}   Metoda wbudowana')

t1 = time.perf_counter()
c = richardson(fun, a, b, k=10)
t2 = time.perf_counter()
print(f'Wynik = {c: .15f} \t czas:{t2 - t1: .15f}   Metoda praca domowa')

