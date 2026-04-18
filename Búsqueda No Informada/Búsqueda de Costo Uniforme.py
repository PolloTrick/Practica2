import heapq

def costo_uniforme(grafo, inicio, objetivo):
    cola = [(0, inicio)]
    visitados = set()

    while cola:
        costo, nodo = heapq.heappop(cola)

        if nodo == objetivo:
            return costo

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino, peso in grafo[nodo]:
                if vecino not in visitados:
                    heapq.heappush(cola, (costo + peso, vecino))

# Grafo con pesos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [], 'E': [('F', 1)], 'F': []
}

print(costo_uniforme(grafo, 'A', 'F'))