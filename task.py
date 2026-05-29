import numpy as np

# Controlla il file readme.md per i dettagli su ciascun sub-task
def prodotto_scalare(v1: list, v2: list) -> float:
        v1 = np.array(v1)
        v2 = np.array(v2)
        return float(np.dot(v1, v2))

def rango_matrice(m: list) -> int:
        matrice = np.array(rango_matrice)
        return int(np.linalg.matrix_rank(matrice))

def risolvi_sistema_lineare(A: list, b: list) -> np.ndarray:
    A = np.array(A)
    b = np.array(b)
    return np.linalg.solve(A, b)


def correlazione_matrici(m1: list, m2: list) -> np.ndarray:

        m1 = np.array(m1)
        m2 = np.array(m2)

        v1 = m1.flatten()
        v2 = m2.flatten()

        return np.corrcoef(v1, v2)

def operazioni_elemento_per_elemento(v1: list) -> tuple:






def main():
    print("Sub-task 1:", prodotto_scalare([1, 2, 3], [4, 5, 6]))
    print("Sub-task 1:", rango_matrice([[1, 2], [3, 4]]))
    print("Sub-task 3:", risolvi_sistema_lineare([[2, 1], [1, 3]], [5, 7]))
    print("Sub-task 4:", correlazione_matrici([[1, 2], [3, 4]], [[2, 4], [6, 8]]))
    print("Sub-task 5:", operazioni_elemento_per_elemento([0, 0.5, 1, -0.5]))

if __name__ == "__main__":
    main()
