import random





N = 4
b = ((2*N)+1) * [True]
d = ((2*N)-1) * [True]

def queens(Array, cantReinas):
    #en el array almacenamos nuestra respuesta
    x = cantReinas-1;
    #x: valor utilizado para recalcular los valores de la diagonal descendente
    if cantReinas==0:
        print (Array)
    else:
        for i in range (cantReinas, 0, -1):
            if (b[Array[i]+cantReinas] and d[(Array[i]-cantReinas)+x]):
                b[Array[i]+cantReinas]=False
                d[(Array[i]-cantReinas)+x]=False
                swap(Array, cantReinas, i)
                queens(Array, cantReinas-1, x)
                swap(Array, cantReinas, i)
                b[Array[i]+cantReinas]=True
                d[(Array[i]-cantReinas)+x]=True

def AuxQueens(Array, reinasRestantes):
    #en el array almacenamos nuestra respuesta
    x = reinasRestantes-1;
    #x: valor utilizado para recalcular los valores de la diagonal descendente
    if reinasRestantes==0:
        print (Array)
    else:
        for i in range (reinasRestantes, 0, -1):
            if (b[Array[i]+reinasRestantes] and d[(Array[i]-reinasRestantes)+x]):
                b[Array[i]+reinasRestantes]=False
                d[(Array[i]-reinasRestantes)+x]=False
                swap(Array, reinasRestantes, i)
                queens(Array, reinasRestantes-1, x)
                swap(Array, reinasRestantes, i)
                b[Array[i]+reinasRestantes]=True
                d[(Array[i]-reinasRestantes)+x]=True

def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

a = [0,1,2,3,4]
#arreglo n+1 en donde ignoramos la primer posicion(ya que trabajaremoss apartir de 1 en lugar de 0, como normalmente se hace)
#queens(a, 4, N-1)

def queensVegas(cantReinas):
    if(cantReinas<=3):
        return
    else:
        encontrado = False
        cont = 0
        while((not encontrado) and cont<=(50000)):
            colDisponibles = (cantReinas+1)*[True]
            encontrado = AuxQueensVegas(cantReinas, colDisponibles)
            cont+=1

def AuxQueensVegas(cantReinas, colDisponibles):
    Array = []
    x = cantReinas-1
    dAsc = ((2*N)+1) * [True]
    dDes = ((2*N)-1) * [True]
    for fila in range(cantReinas, 0, -1):
        colLibres = columnasDisponibles(colDisponibles, cantReinas, dAsc, dDes)
        if (len(colLibres)==1):
            return False
        columna = random.randint(1, len(colLibres)-1)
        
        Array.append(columna)
        colDisponibles[columna] = False
        dAsc[columna+cantReinas] = False
        dDes[(columna-cantReinas)+x] = False
        cantReinas = cantReinas-1
    print(Array)
    return True

def columnasDisponibles(colDisponibles, cantReinas, dAscendente, dDescendente):
    lista = []
    for columna in range(len(colDisponibles)):
        if((colDisponibles[columna]) and (dAscendente[columna+cantReinas]) and (dDescendente[(columna-cantReinas)+(len(colDisponibles)-2)])):
            lista.append(columna)
    return lista

def cambio(a):
    a = not a
    return a


def cicloFor(x,n):
    for i in range(n):
        x
