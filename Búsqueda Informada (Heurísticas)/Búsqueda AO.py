# Grafo AND-OR simplificado
grafo = {
    'A': [['B', 'C'], ['D']],  # A puede ir a (B y C) o a D
    'B': [['E']],
    'C': [['F']],
    'D': [],
    'E': [],
    'F': []
}

heuristica = {
    'A': 5, 'B': 3, 'C': 4,
    'D': 2, 'E': 1, 'F': 0
}

def ao_estrella(nodo):
    if nodo not in grafo or not grafo[nodo]:
        return heuristica[nodo]

    costos = []

    for opcion in grafo[nodo]:
        costo = sum(ao_estrella(hijo) for hijo in opcion)
        costos.append(costo)

    return min(costos)

print(ao_estrella('A'))