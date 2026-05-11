# Aprendizaje por Refuerzo Activo

import random

acciones = ["izquierda", "derecha"]

for episodio in range(5):
    accion = random.choice(acciones)

    if accion == "derecha":
        recompensa = 10
    else:
        recompensa = -5

    print(f"Episodio {episodio+1}")
    print(f"Acción: {accion}")
    print(f"Recompensa: {recompensa}\n")