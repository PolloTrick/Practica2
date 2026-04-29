import random

def funcion_objetivo(x):
    return -x**2 + 10

def crear_individuo():
    return random.uniform(-10, 10)

def cruzar(p1, p2):
    return (p1 + p2) / 2

def mutar(x):
    return x + random.uniform(-1, 1)

def genetico(poblacion_size, generaciones):
    poblacion = [crear_individuo() for _ in range(poblacion_size)]

    for _ in range(generaciones):
        poblacion = sorted(poblacion, key=funcion_objetivo, reverse=True)
        nueva = poblacion[:2]

        while len(nueva) < poblacion_size:
            p1, p2 = random.sample(poblacion[:5], 2)
            hijo = cruzar(p1, p2)
            hijo = mutar(hijo)
            nueva.append(hijo)

        poblacion = nueva

    return max(poblacion, key=funcion_objetivo)

print(genetico(10, 50))