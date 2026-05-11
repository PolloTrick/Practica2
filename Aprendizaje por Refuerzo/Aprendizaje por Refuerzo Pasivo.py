# Aprendizaje por Refuerzo Pasivo

import random

estados = ["A", "B", "C"]
recompensas = {"A": 1, "B": -1, "C": 5}

# Política fija
politica = {
    "A": "B",
    "B": "C",
    "C": None
}

estado_actual = "A"
total_recompensa = 0

while estado_actual:
    print(f"Estado actual: {estado_actual}")
    total_recompensa += recompensas[estado_actual]
    estado_actual = politica[estado_actual]

print("Recompensa total:", total_recompensa)
