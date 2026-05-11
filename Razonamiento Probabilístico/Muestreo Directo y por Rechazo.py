# Muestreo por rechazo

import random

muestras_validas = []

for _ in range(100):
    valor = random.random()

    # aceptar solo mayores a 0.5
    if valor > 0.5:
        muestras_validas.append(valor)

print("Cantidad de muestras válidas:",
      len(muestras_validas))