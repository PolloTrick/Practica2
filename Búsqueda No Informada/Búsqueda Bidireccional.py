from collections import deque

def bidireccional(grafo, inicio, objetivo):
    if inicio == objetivo:
        return True

    cola_inicio = deque([inicio])
    cola_fin = deque([objetivo])

    visitados_inicio = {inicio}
    visitados_fin = {objetivo}

    while cola_inicio and cola_fin:
        if expandir(grafo, cola_inicio, visitados_inicio, visitados_fin):
            return True
        if expandir(grafo, cola_fin, visitados_fin, visitados_inicio):
            return True

    return False

def expandir(grafo, cola, visitados, otro_lado):
    nodo = cola.popleft()
    for vecino in grafo[nodo]:
        if vecino in otro_lado:
            return True
        if vecino not in visitados:
            visitados.add(vecino)
            cola.append(vecino)
    return False

grafo = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C']
}

print(bidireccional(grafo, 'A', 'D'))