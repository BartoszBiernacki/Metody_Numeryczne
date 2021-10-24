import numpy as np
import copy
from random import seed
from random import random

def jacobi(a, b, x, N, debug=False):
    n = len(x)
    x_new = x[:]
    for k in range(N):
        for i in range(n):
            temp = b[i]
            for j in range (n):
                if(j!=i):
                    temp -= a[i][j] * x[j]
            x_new[i] = temp/a[i][i]
        x = x_new[:]
        if(debug):
            print(f'{k:3}', end='\t')
            for i in range(n):
                print(f'{x[i]:13.7f}', end='\t')
            print()
    return np.array(x)          #returning x as np.array, because I want to easlily set pricsion while printing result


def MPD(n):
    array = np.random.rand(n,n);            #fiil matrix nxn with random real wariables
    maks1 = abs(np.amin(array, axis=1));    #vector of absolut values of smallest value of each row, if i-th row = [-5, 4, 0] then maks1[i]=5
    maks2 = abs(np.amax(array, axis=1));    #vector of absolut values of biggest value of each row, if i-th row = [-5, 4, 0] then maks2[i]=4
    tmp = np.row_stack((maks1, maks2));     #matrix containing vestor maks1 and maks2 as rows
    true_maks = np.amax(tmp, axis=0);       #vector of biggest value of each column of matrix tmp -> contains maks values of each row of initial array ignoring sign
    np.fill_diagonal(array, n*true_maks + np.random.uniform(low=0.0, high=1.0));        #change diagonal of an array to make it diagonally dominant and still random

    # well, at that moment I noticed that ,,sum of elements in each row is not greater than n'' ,so more efficient would be following code:
    # np.fill_diagonal(array, abs(np.diagonal(array))+n);       #but I'm gonna leave it as it is.
    return array;


def test_of_jacobi_convergence_for_randomly_created_diagonally_dominant_matrices(dimension, sample, jacobi_iterations):
    print('************************************************* Jacobi test *********************************************')
    np.set_printoptions(precision=8)
    for i in range(sample):
        A = MPD(dimension);
        B = np.random.rand(dimension);
        X = np.random.rand(dimension);

        print(f'Jacobi test {i+1}, number of iterations = {jacobi_iterations}')
        print("Metoda Jackobiego: ")
        print(jacobi(A, B, X, jacobi_iterations))

        print("Sprawdzenie:")
        print(np.linalg.solve(A, B))
        print()
    print('***********************************************************************************************************')


def seidel(a, b, N, x=None):         #x is optional, because is not nescessary to find solutions
    n = len(b)                        #but if we want to fairly compare jacobi and seidel it would be good to have the same inital condition
    if(x == None):                   #use given X is exist or randomly create new x
        x = np.random.rand(n)

    for k in range(N):
        for i in range(n):
            sum = 0
            for j in range (n):
                if(j!=i):
                    sum += a[i][j] * x[j]
            sum = b[i] - sum
            x[i] = (1.0 / a[i][i]) * sum
    return np.array(x)

def test_of_seidel_convergence_for_randomly_created_diagonally_dominant_matrices(dimension,sample, seidel_iterations):
    print('************************************************* Seidel test *********************************************')
    np.set_printoptions(precision=8)
    for i in range(sample):
        A = MPD(dimension);
        B = np.random.rand(dimension);

        print(f'Seidel test {i + 1}, number of iterations = {seidel_iterations}')
        print("Metoda Seidla: ")
        print(seidel(A, B, seidel_iterations))

        print("Sprawdzenie:")
        print(np.linalg.solve(A, B))
        print()
    print('***********************************************************************************************************')


def create_random_X(dim):
    seed(1)
    X = []
    for i in range(dim):
        X.append(random())
    return X


def compare_convergence(dimension, samples, epsilon):
    print('************************************* Convergence comparation *********************************************')
    np.set_printoptions(precision=8)
    sum_of_Jacobi_terations = 0
    sum_of_Seidel_terations = 0
    for m in range(samples):
        A = MPD(dimension)
        B = np.random.rand(dimension)
        #X = np.random.rand(dimension)           #this way doesn't working jacobi and seigel operate on the same X even with coppy.coppy(X) aplied
        X = create_random_X(dimension)          #this way it does
        solved = np.linalg.solve(A, B)

        for i in range(100):
            Xj = copy.copy(X)                       #initializing
            Xj = jacobi(A, B, Xj, i)                #evaluating
            maks_diffrence = max(abs(solved - Xj))
            if(maks_diffrence < epsilon):
                print(f'In test [{m+1}] Jacobi converged after {i} iterations')
                sum_of_Jacobi_terations += i
                break
            if(i==90):
                print(f'In test [{m+1}] after {i} iterations Jacobi DOES NOT CONVERGED to given epsilon!!!')
                break

        for j in range(100):
            Xs = copy.copy(X)                           #initializing
            Xs = seidel(A, B, j, Xs)                    #evaluating
            maks_diffrence = max(abs(solved - Xs))
            if (maks_diffrence < epsilon):
                print(f'In test [{m + 1}] Seidel converged after {j} iterations')
                sum_of_Seidel_terations += j
                break
            if (j == 90):
                print(f'In test [{m + 1}] after {j} iterations Seidel DOES NOT CONVERGED to given epsilon!!!')
                break
        print()
    print(f'Speed of convergence tested  on {samples} linear system of equations {dimension}x{dimension} with minimal precisoin {epsilon}.')
    print(f'Seidel method is on average {sum_of_Jacobi_terations / sum_of_Seidel_terations :.2f} faster in finding roots.')
    print('***********************************************************************************************************')



test_of_jacobi_convergence_for_randomly_created_diagonally_dominant_matrices(dimension=5,sample=3, jacobi_iterations=4)
test_of_seidel_convergence_for_randomly_created_diagonally_dominant_matrices(dimension=5, sample=3, seidel_iterations=4)
compare_convergence(dimension=5, samples=4, epsilon=1e-12)