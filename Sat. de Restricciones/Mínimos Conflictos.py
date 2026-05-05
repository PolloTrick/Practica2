# Min-Conflicts

import random

def conflictos(variable, valor, asignacion, grafo):
    return sum(1 for vecino in grafo[variable]
               if vecino in asignacion and asignacion[vecino] == valor)

def min_conflicts(grafo, colores, max_iter=100):
    # asignación inicial aleatoria
    asignacion = {n: random.choice(colores) for n in grafo}

    for _ in range(max_iter):
        conflictos_totales = [n for n in grafo if conflictos(n, asignacion[n], asignacion, grafo) > 0]

        if not conflictos_totales:
            return asignacion

        var = random.choice(conflictos_totales)

        mejor_color = min(colores, key=lambda c: conflictos(var, c, asignacion, grafo))
        asignacion[var] = mejor_color

    return None

# Ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

colores = ['Rojo', 'Verde', 'Azul']

print(min_conflicts(grafo, colores))