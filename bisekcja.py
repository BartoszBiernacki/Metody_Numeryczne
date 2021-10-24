def bisection(f, a, b, d, debug = False):
    """
    metoda bisekcji
    f - zadana funkcja
    a,b końce przedziału
    d - precyzja obliczeń
    """
    left = a
    right = b
    i =0
    while((right - left)/2 > d):
        mid = (left + right)/2
        if debug:
            if i == 0:
                print('Krok \t\t x0 \t\t\t epsilon')
            else:
                print(f'{i:4} \t {mid:12} \t {(right - left):12}')
        if f(left)*f(mid) < 0:
            right = mid
        elif f(mid)*f(right) < 0:
            left = mid
        elif f(mid) == 0:
            return mid
        else:
            return None
        i = i+1
    return mid

def fun(x):
    return x**2 - x -1

a = float(input('Podaj lewy brzeg badanego przedziału: '))
b = float(input('Podaj prawy brzeg badanego przedziału: '))
d = float(input('Podaj precyzję obliczeń: '))

x = bisection(fun, a, b, d, True)
if x ==None:
    print('Brak miejsc zerowych')
else:
     print(f'\n Miejsce zerowe to {x:.12f}')