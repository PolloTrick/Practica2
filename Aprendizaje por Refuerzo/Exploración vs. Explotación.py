# Exploración vs Explotación

import random

valores = [5, 10, 3]
epsilon = 0.3

for intento in range(10):

    if random.random() < epsilon:
        accion = random.randint(0, 2)
        tipo = "Exploración"
    else:
        accion = valores.index(max(valores))
        tipo = "Explotación"

    print(f"Intento {intento+1}")
    print(f"{tipo}: Acción {accion}")