def dls(grafo, nodo, objetivo, limite):
    if nodo == objetivo:
        return True
    if limite <= 0:
        return False

    for vecino in grafo[nodo]:
        if dls(grafo, vecino, objetivo, limite - 1):
            return True

    return False

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': ['F'], 'F': []
}

print(dls(grafo, 'A', 'F', 2))