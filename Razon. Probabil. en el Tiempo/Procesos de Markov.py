# Cadena de Markov simple

import random

estados = {
    "Soleado": ["Soleado", "Lluvioso"],
    "Lluvioso": ["Soleado", "Lluvioso"]
}

estado_actual = "Soleado"

for _ in range(5):
    estado_actual = random.choice(estados[estado_actual])
    print("Estado actual:", estado_actual)