# Filtrado de partículas simple

import random

particulas = [random.randint(0, 10) for _ in range(100)]

promedio = sum(particulas) / len(particulas)

print("Estimación por partículas:", promedio)