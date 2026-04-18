def dfs(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()

    if nodo not in visitados:
        print(nodo, end=" ")
        visitados.add(nodo)

        for vecino in grafo[nodo]:
            dfs(grafo, vecino, visitados)

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': ['F'], 'F': []
}

dfs(grafo, 'A')