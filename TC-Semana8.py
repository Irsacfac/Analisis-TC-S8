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
e = (N+1) * [True]
queens(a, 4, N-1)


def queensVegas(reinas):
    encontrado = False
    contador = 0
    while(not encontrado):
        encontrado = auxQueensVegas([], reinas, reinas-1)

def auxQueensVegas(Array, rRestantes, x):
    if rRestantes==0:
        print (Array)
        return True
    else:
        colDisponibles = columnasDisponibles(e, rRestantes, x)
        if(len(colDisponibles)==0):
            return False
        col = colDisponibles[random.randint(0, len(colDisponibles)-1)]
        e[col] = False
        b[col+rRestantes] = False
        d[(col-rRestantes)+x] = False
        Array.append(col)
        auxQueensVegas(Array, rRestantes-1, x)
            
def columnasDisponibles(Array, fila, x):
    disponibles = []
    for columna in range(len(Array)-1, 0, -1):
        if(Array[columna] and b[columna+fila] and d[(columna-fila)+x]):
            disponibles.append(columna)
    return disponibles
    
def cambio(a):
    a = not a
    return a

queensVegas(4)


def cicloFor(x,n):
    for i in range(n):
        x
