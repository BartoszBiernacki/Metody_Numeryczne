import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def createRandomGraph(N):
    return nx.gnm_random_graph(N, 13*N, directed=True)


def power2(N, alpha, debug=False):  #funkcja zwracajaca listę wartości własnych i listę wektorów własnych
    B = nx.stochastic_graph(createRandomGraph(N))  # tworzy losowy skierowany graf i przypisuje stochastyczne wartości krawędziom
    if debug:
        nx.draw(B, with_labels=True)
        plt.show()
    H = nx.to_numpy_array(B).T  # zamienia graf ważony na macierz stochastyczną i transponuje
    G = alpha * H + (1 - alpha) * np.ones((N, N)) / N
    eigval, eigvect = np.linalg.eig(G) #zwraca listę z dwóch elem. 1 elem listy to lista wartości własnych, 2 elem. to lista wektorów własnych
    return  eigval, eigvect


print()
np.set_printoptions(precision = 3, suppress = True )    #2 cyfry po przecinku, bez notacji wykładniczej
wartosi1, wektory1 = power2(N=50, alpha=1)
if (abs(wartosi1) <= 1.000001).all():       #1.000001 zamiast 1 ze względnu na skończoną dokładność zapisu i obliczeń
    print(f'Test zdany: dla każdej wartości \u03BB prawdą jest, że |\u03BB| ≤ 1')
else:
    print(f'Test NIE zdany!: NIE jest prawdą, że dla każdej \u03BB:  |\u03BB| ≤ 1')
wartosi2, wektory2 = power2(N=50, alpha=0.6)
wartosi3, wektory3 = power2(N=50, alpha=0.2)

plt.figure(figsize=(9,6))
plt.scatter(wartosi1.real, wartosi1.imag, alpha=0.5, label='\u03B1 = 1') #wykres punktowy  2D wartosci własnych przy alpha = 1 (alpha = 0.5 oznacza transparecy = 0.5)
plt.scatter(wartosi2.real, wartosi2.imag, alpha=0.3, label='\u03B1 = 0.6 < 1') #wykres punktowy  2D wartosci własnych przy alpha = 0.2
plt.scatter(wartosi3.real, wartosi3.imag, alpha=0.3, label='\u03B1 = 0.2 < 1') #wykres punktowy  2D wartosci własnych przy alpha = 0.8
plt.legend()
t = np.linspace(0, 2*np.pi , 1000) #zwroci tablice 1000 punktów równoodległych na odcinku (0 , 2pi)
plt.plot(np.cos(t), np.sin(t), 'k') #chcę narysować parametrycznie okręg, kolor czrny

plt.axis("equal") #osie równej dlugosci

plt.title('Wartości własne macierzy Google zależnie od parametru \u03B1', fontdict={'fontname': 'monospace', 'fontsize': 12})
plt.xlabel('Re(\u03BB)')
plt.ylabel('Im(\u03BB)')
plt.show()

print()
print("Jak widać na przykładzie, im \u03B1 jest bliższe 0 tym średni moduł wartości własnej macierzy G jest mniejszy.")
print("Zbieżność metody potęgowej jest odwrotnie proporcjonalna do drugiej wartości własnej (co do modułu).")
print("Im większe \u03B1 tym większe baczenie na rzeczywiste połączenia (macierz H), "
      "widać to po tym, że gdy \u03B1 maleje to średni |\u03BB| również maleje.")
print("Z drugiej strony im mniejsze \u03B1 tym szybsza zbieżność.")