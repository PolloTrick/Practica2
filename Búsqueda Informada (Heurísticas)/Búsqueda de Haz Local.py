import random

def funcion_objetivo(x):
    return -x**2 + 10

def vecinos(x):
    return [x + random.uniform(-1, 1) for _ in range(3)]

def haz_local(k, iteraciones):
    estados = [random.uniform(-10, 10) for _ in range(k)]

    for _ in range(iteraciones):
        todos = []
        for estado in estados:
            todos.extend(vecinos(estado))

        estados = sorted(todos, key=funcion_objetivo, reverse=True)[:k]

    return max(estados, key=funcion_objetivo)

print(haz_local(3, 50))