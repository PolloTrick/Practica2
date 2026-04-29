import random
import math

def funcion_objetivo(x):
    return -x**2 + 10

def vecino(x):
    return x + random.uniform(-1, 1)

def temple_simulado(inicial, temp, enfriamiento):
    actual = inicial
    mejor = actual

    while temp > 0.1:
        nuevo = vecino(actual)
        delta = funcion_objetivo(nuevo) - funcion_objetivo(actual)

        if delta > 0 or random.random() < math.exp(delta / temp):
            actual = nuevo

        if funcion_objetivo(actual) > funcion_objetivo(mejor):
            mejor = actual

        temp *= enfriamiento

    return mejor

print(temple_simulado(5, 100, 0.9))