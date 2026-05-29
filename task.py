import numpy
import numpy as np
from numpy.ma.core import concatenate


# Controlla il file readme.md per i dettagli su ciascun sub-task

def prodotto_scalare(v1: list, v2: list) -> float:
    """Sub-task 1: Prodotto Scalare."""
    if(len(v1) != len(v2)):
        return ("Prodotto Scalare non valido - Dimensioni diverse")
    ris=numpy.dot(v1, v2)
    return ris

def rango_matrice(m: list) -> int:
    """Sub-task 2: Calcola il rango di una matrice."""
    from numpy.linalg import matrix_rank
    k=len(m)
    flag=1
    for i in range(k):
        if(len(m[i])!=len(m)):
            flag=0
    if (flag==0):
        return ("Rango non valido - Matrice non quadrata")
    rank=matrix_rank(m)
    return rank

def risolvi_sistema_lineare(A: list, b: list) -> np.ndarray:
    """Sub-task 3: Risolvere un Sistema Lineare."""
    k = len(A)
    flag = 0
    for i in range(k):
        if (len(A[i]) == len(b)):
            flag = 1
    if (flag == 0):
        return ("Sistema non risolvibile")
    sol=np.linalg.solve(A,b)
    return sol
    pass

def correlazione_matrici(m1: list, m2: list) -> np.ndarray:
    """Sub-task 4: Correlazione tra Matrici 2x2."""
    if(len(m1) != 2 or len(m1[0]) != 2 or len(m1[1]) != 2):
        return ("La prima matrice non è 2x2")
    if(len(m2) != 2 or len(m2[0]) != 2 or len(m2[1]) != 2):
        return ("La seconda matrice non è 2x2")
    arr1 = np.array(m1)
    arr2 = np.array(m2)
    ris=numpy.corrcoef(arr1, arr2)
    return ris

def operazioni_elemento_per_elemento(v1: list) -> tuple:
    """Sub-task 5: Restituisce (seno, coseno, arcoseno, arcocoseno) elemento per elemento calcolati sul primo array."""
    k=len(v1)
    v2=[]
    for i in range(k):
        v2.append(np.sin(np.array(v1) * np.pi / 180. ))

    for i in range(k):
        v2.append(np.cos(np.array(v1) * np.pi / 180.))

    for i in range(k):
    return (v2)


def main():
    print("Sub-task 1:", prodotto_scalare([5, 7, 3], [4, 5, 6]))
    print("Sub-task 1:", rango_matrice([[2, 4, 1], [0, 1,0],[1,4,0]]))
    print("Sub-task 3:", risolvi_sistema_lineare([[1, 0],[0,1]], [3,4]))
    print("Sub-task 4:", correlazione_matrici([[1, 2], [3, 4]], [[2, 4], [6, 8]]))
    print("Sub-task 5:", operazioni_elemento_per_elemento([0, 0.5, 1, -0.5]))

if __name__ == "__main__":
    main()
