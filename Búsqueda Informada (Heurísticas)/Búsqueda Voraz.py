import heapq

def voraz(grafo, inicio, objetivo, heuristica):
    cola = [(heuristica(inicio), inicio)]
    visitados = set()

    while cola:
        h, nodo = heapq.heappop(cola)

        if nodo == objetivo:
            return True

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    heapq.heappush(cola, (heuristica(vecino), vecino))

    return False

# Grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': ['F'], 'F': []
}

def heuristica(nodo):
    return {'A':5,'B':3,'C':4,'D':2,'E':1,'F':0}[nodo]

print(voraz(grafo, 'A', 'F', heuristica))