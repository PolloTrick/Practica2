# Monte Carlo simple para cadena de Markov

import random

estados = ["Soleado", "Lluvioso"]

estado_actual = "Soleado"

for i in range(10):
    estado_actual = random.choice(estados)
    print("Estado:", estado_actual)