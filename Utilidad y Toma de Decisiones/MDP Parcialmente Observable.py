# MDP Parcialmente Observable (POMDP)

import random

print("=== POMDP ===")

estados_reales = ["Seguro", "Peligro"]
observaciones = ["Ruido Bajo", "Ruido Alto"]

# Estado oculto
estado_real = random.choice(estados_reales)

# Observación parcial
if estado_real == "Seguro":
    observacion = random.choice(["Ruido Bajo", "Ruido Alto"])
else:
    observacion = "Ruido Alto"

print("Observación recibida:", observacion)

# Decisión basada en observación
if observacion == "Ruido Alto":
    accion = "Precaución"
else:
    accion = "Continuar"

print("Acción tomada:", accion)
print("Estado real:", estado_real)
