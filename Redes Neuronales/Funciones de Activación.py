# Función Sigmoide

import math

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

print(sigmoide(2))