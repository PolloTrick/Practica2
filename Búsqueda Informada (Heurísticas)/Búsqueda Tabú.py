import random

def vecinos(solucion):
    return [solucion + random.randint(-1, 1) for _ in range(5)]

def funcion_objetivo(x):
    return -x**2 + 10  # máximo en x=0

def tabu_search(inicial, iteraciones, tamaño_tabu):
    actual = inicial
    mejor = actual
    lista_tabu = []

    for _ in range(iteraciones):
        candidatos = vecinos(actual)
        candidatos = [c for c in candidatos if c not in lista_tabu]

        if not candidatos:
            break

        actual = max(candidatos, key=funcion_objetivo)

        if funcion_objetivo(actual) > funcion_objetivo(mejor):
            mejor = actual

        lista_tabu.append(actual)
        if len(lista_tabu) > tamaño_tabu:
            lista_tabu.pop(0)

    return mejor

print(tabu_search(5, 50, 5))