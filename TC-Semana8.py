import random

N = 4
b = ((2*N)+1) * [True]
d = ((2*N)-1) * [True]

def queens(A, m, x):
    if m==0:
        print (A)
    else:
        for i in range (m, 0, -1):
            if (b[A[i]+m] and d[(A[i]-m)+x]):
                b[A[i]+m]=False
                d[(A[i]-m)+x]=False
                swap(A, m, i)
                queens(A, m-1, x)
                swap(A, m, i)
                b[A[i]+m]=True
                d[(A[i]-m)+x]=True

def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

a = [0,1,2,3,4]
queens(a, 4, N-1)


def queensVegas(Array, rRestanets, x):
    if rRestantes==0:
        print (A)
    else:
        for i in range (rRestates, 0, -1):
            colDisponibles = columnasDisponibles(Array)
            if(len(colDisponibles)==0):
                return
            
def columnasDIsponibles(Array, fila, x):
    disponibles = []
    for columna in range(len(Array)-1, 0, -1):
        if(Array[columna]):
            disponibles.append(columna)
    return disponibles
    
def cambio(a):
    a = not a
    return a


def cicloFor(x,n):
    for i in range(n):
        x
