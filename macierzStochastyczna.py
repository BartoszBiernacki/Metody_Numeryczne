import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def power(A,N,debug=False):
    B = nx.stochastic_graph(A)  #przypisuje wartość z ważonymi krawędziami (stochastycznie)
    H = nx.to_numpy_array(B)    #zamienia graf ważony na macierz ważoną (przejść / stochastyczną)
    H = H.T #transopnujemy macierz, bo mamy zamienione kolumny z wierszami wzgledem prezentacji (umowa co jest czym)
    x_size, y_size = H.shape    #w x_size będzie ilość kolumn, a w y_size ilość wierszy macierzy H
    X = np.zeros(x_size)
    X[0] = 1
    for i in range (N):
        X = np.dot(H,X)
        if debug:
            print(X)
    return X


def power2(A):  #funkcja zwracajaca listę wartości własnych i listę wektorów własnych
    B = nx.stochastic_graph(A)  # przypisuje wartość z ważonymi krawędziami (stochastycznie)
    H = nx.to_numpy_array(B).T  # zamienia graf ważony na macierz ważoną (przejść / stochastyczną) i transponuje
    eigval, eigvect = np.linalg.eig(H) #zwraca listę z dwóch elem. 1 elem listy to lista wartości własnych, 2 elem. to lista wektorów własnych
    return  eigval, eigvect


np.set_printoptions(precision = 3, suppress = True )    #2 cyfry po przecinku, bez notacji wykładniczej

edgelist = [(1,2), (1,3), (2,4), (3,2), (3,5), (4,2), (4,5), (4,6), (5,6), (5,7), (5,8),
            (6,8), (7,1), (7,5), (7,8), (8,6), (8,7)]
A = nx.DiGraph(edgelist)    #graf skierowany z połączeń
#nx.draw(A, with_labels=True)
#plt.show()

#power(A,300, debug=True)
wartosi , wektory = power2(A)
print(wartosi)
print()
#wektory są w kolumnach, a nie w wierszach dlatego tak robimy
print(wektory[:,0]) #po wszystkich wierszach i z każdego wiersza pierwszą kolumnę

plt.scatter(wartosi.real, wartosi.imag) #wykres punktowy  2D wartosci własnych
t = np.linspace(0, 2*np.pi , 1000) #zwroci tablice 1000 punktów równoodległych na odcinku (0 , 2pi)
plt.plot(np.cos(t), np.sin(t), 'k') #chcę narysować parametrycznie okręg, kolor czrny
plt.axis("equal") #osie równej dlugosci

plt.show()