# Ejemplo de heurística: distancia estimada a la meta

def heuristica(nodo):
    valores = {
        'A': 5,
        'B': 3,
        'C': 4,
        'D': 2,
        'E': 1,
        'F': 0  # objetivo
    }
    return valores[nodo]

# Probar heurística
for nodo in ['A', 'B', 'C', 'D', 'E', 'F']:
    print(f"Heurística de {nodo}: {heuristica(nodo)}")