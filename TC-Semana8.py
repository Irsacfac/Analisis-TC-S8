import random
from time import time

N = 4
b = ((2*N)+1) * [True]
d = ((2*N)-1) * [True]

def queens(A, m, x):
    tInicial = time()
    auxQueens(A, m, x, tInicial)

def auxQueens(A, m, x, T):
    if m==0:
        print (A)
        tFinal = time()
        tEjecucion = tFinal - T
        print("El tiempo de ejecución backtracking fue: ", tEjecucion)
        return True
    else:
        for i in range (m, 0, -1):
            if (b[A[i]+m] and d[(A[i]-m)+x]):
                b[A[i]+m]=False
                d[(A[i]-m)+x]=False
                swap(A, m, i)
                if(auxQueens(A, m-1, x, T)):
                    return True
                swap(A, m, i)
                b[A[i]+m]=True
                d[(A[i]-m)+x]=True
        return False

def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp



def queensVegas(reinas):
    encontrado = False
    contador = 0
    tInicial = time()
    while(not encontrado):
        B = ((2*N)+1) * [True]
        D = ((2*N)-1) * [True]
        E = (N+1) * [True]
        encontrado = auxQueensVegas([], reinas, reinas-1, B, D, E, tInicial)
        contador+=1
    return

def auxQueensVegas(Array, rRestantes, x, B, D, E, T):
    if rRestantes==0:
        print (Array)
        tFinal = time()
        tEjecucion =  tFinal - T
        print("El tiempo de ejecución LasVegas fue: ", tEjecucion)
        return True
    else:
        colDisponibles = columnasDisponibles(E, rRestantes, x, B, D, E,)
        if(len(colDisponibles)==0):
            return False
        col = colDisponibles[random.randint(0, len(colDisponibles)-1)]
        E[col] = False
        B[col+rRestantes] = False
        D[(col-rRestantes)+x] = False
        Array.append(col)
        return auxQueensVegas(Array, rRestantes-1, x, B, D, E, T)
            
def columnasDisponibles(Array, fila, x, B, D, E,):
    disponibles = []
    for columna in range(len(Array)-1, 0, -1):
        if(Array[columna] and B[columna+fila] and D[(columna-fila)+x]):
            disponibles.append(columna)
    return disponibles


a = [0,1,2,3,4]
e = (N+1) * [True]
queens(a, N, N-1)
queensVegas(N)
