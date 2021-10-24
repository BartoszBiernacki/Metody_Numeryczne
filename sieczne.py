def secant_method(f, x1, x2, mode, N=10, d=0.0012, debug=False):
    print("")
    """
    metoda siecznych
    f - zadana funkcja
    x1, x2 dowolne punkty początkowe
    N - Liczba iteracji
    d - precyzja
    """
    if x1 == x2:
        return None

    if (mode == 1):
        for i in range(N):
            x3 = x2 - (f(x2)*(x1 - x2)) /(f(x1) - f(x2))
            if debug:
                if i == 0:
                    print('Krok \t\t x0')
                else:
                    print(f'{i:4} \t {x3:12}')
            if i == 0:
                if f(x1) == 0:
                    return x1
                elif f(x2) ==0:
                    return x2
            elif f(x3) == 0:
                print(f'f(x_{i}) = {f(x3)} (na tyle ile pozwala precyzja obliczeń --> przerywam kolejne iteracje')
                return x3
            else:
                x1 = x2
                x2 = x3
        return x3
    else:
        i = 0
        while True:
            x3 = x2 - (f(x2) * (x1 - x2)) / (f(x1) - f(x2))
            if debug:
                if i == 0:
                    print('Krok \t\t x0 \t\t\t różnica x0 między kolejnymi iteracjami')
                else:
                    print(f'{i:4} \t {x3:12} \t {abs(x3 - x2):12}')
            if i == 0:
                if f(x1) == 0:
                    return x1
                elif f(x2) == 0:
                    return x2
            elif f(x3) == 0:
                return x3
            elif abs(x3 - x2) < d:
                return x3
            else:
                x1 = x2
                x2 = x3
            i = i + 1




def fun(x):
    return x**2 - x -1

x1 = float(input('Podaj x1: '))
x2 = float(input('Podaj x2: '))
print('Jeśli chcesz liczyć z ustaloną ilością iteracji wpisz 1')
print('Jeśli chcesz liczyć do momentu gdy odległość między pierwiastkami w kolejnych iteracjach jest mniejsza niż określona wartość wpisz inną liczę np. 0')
mode = float(input('Twój wybór: '))
if mode == 1:
    N = int(input('Podaj liczbę iteracji: '))
    x = secant_method(fun, x1, x2, mode, N=N, debug=True)
else:
    d = float(input('Podaj graniczną odległość między pierwiastki kolejnych iteracji: '))
    x = secant_method(fun, x1, x2, mode, d=d, debug=True)

if x == None:
    print("Uruchom program ponownie i podaj x1 inny niż x2")
else:
    print(f'\n Miejsce zerowe to {x:12}')