from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])

    while cola:
        nodo = cola.popleft()

        if nodo not in visitados:
            print(nodo, end=" ")
            visitados.add(nodo)

            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)

# Ejemplo de grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Ejecutar BFS desde A
bfs(grafo, 'A')