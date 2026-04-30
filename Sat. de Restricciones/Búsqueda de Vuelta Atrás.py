# Backtracking - N Reinas

def es_seguro(tablero, fila, col):
    for i in range(fila):
        if tablero[i] == col or \
           tablero[i] - i == col - fila or \
           tablero[i] + i == col + fila:
            return False
    return True

def resolver_n_reinas(n):
    tablero = [-1] * n

    def backtrack(fila):
        if fila == n:
            return True

        for col in range(n):
            if es_seguro(tablero, fila, col):
                tablero[fila] = col

                if backtrack(fila + 1):
                    return True

                tablero[fila] = -1

        return False

    if backtrack(0):
        return tablero
    return None

# Ejecutar
n = 4
solucion = resolver_n_reinas(n)
print(solucion)