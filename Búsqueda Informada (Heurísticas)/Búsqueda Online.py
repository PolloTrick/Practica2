import random

# Simulación simple donde el agente no conoce todo el entorno

grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

def busqueda_online(inicio, objetivo):
    actual = inicio
    visitados = set()

    while actual != objetivo:
        print("Visitando:", actual)
        visitados.add(actual)

        vecinos = grafo.get(actual, [])
        no_visitados = [v for v in vecinos if v not in visitados]

        if not no_visitados:
            return False

        actual = random.choice(no_visitados)

    print("Llegó a:", objetivo)
    return True

busqueda_online('A', 'E')