import heapq

def a_estrella(grafo, inicio, objetivo, heuristica):
    cola = [(0 + heuristica(inicio), 0, inicio)]
    visitados = set()

    while cola:
        f, g, nodo = heapq.heappop(cola)

        if nodo == objetivo:
            return g

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino, costo in grafo[nodo]:
                if vecino not in visitados:
                    nuevo_g = g + costo
                    nuevo_f = nuevo_g + heuristica(vecino)
                    heapq.heappush(cola, (nuevo_f, nuevo_g, vecino))

    return None

# Grafo con pesos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [], 'E': [('F', 1)], 'F': []
}

def heuristica(nodo):
    return {'A':5,'B':3,'C':4,'D':2,'E':1,'F':0}[nodo]

print(a_estrella(grafo, 'A', 'F', heuristica))