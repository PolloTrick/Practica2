# Q-Learning

import numpy as np
import random

# Matriz Q
Q = np.zeros((3, 2))

alpha = 0.1
gamma = 0.9
epsilon = 0.2

for episodio in range(100):

    estado = random.randint(0, 2)

    # Exploración o explotación
    if random.uniform(0, 1) < epsilon:
        accion = random.randint(0, 1)
    else:
        accion = np.argmax(Q[estado])

    recompensa = random.randint(-5, 10)
    siguiente_estado = random.randint(0, 2)

    Q[estado, accion] = Q[estado, accion] + alpha * (
        recompensa + gamma * np.max(Q[siguiente_estado])
        - Q[estado, accion]
    )

print("Tabla Q aprendida:")
print(Q)