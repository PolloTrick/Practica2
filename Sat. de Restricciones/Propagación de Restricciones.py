# AC-3 (Arc Consistency)

from collections import deque

def ac3(grafo, dominios):
    cola = deque([(xi, xj) for xi in grafo for xj in grafo[xi]])

    while cola:
        xi, xj = cola.popleft()

        if revisar(xi, xj, dominios):
            if not dominios[xi]:
                return False
            for xk in grafo[xi]:
                if xk != xj:
                    cola.append((xk, xi))
    return True

def revisar(xi, xj, dominios):
    eliminado = False
    for x in dominios[xi][:]:
        if all(x == y for y in dominios[xj]):
            dominios[xi].remove(x)
            eliminado = True
    return eliminado

# Ejemplo
grafo = {
    'A': ['B'],
    'B': ['A']
}

dominios = {
    'A': ['Rojo', 'Verde'],
    'B': ['Rojo']
}

print(ac3(grafo, dominios))
print(dominios)