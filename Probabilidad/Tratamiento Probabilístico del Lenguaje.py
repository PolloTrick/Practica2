# Conteo probabilístico de palabras

from collections import Counter

texto = "hola mundo hola inteligencia artificial"

palabras = texto.split()

conteo = Counter(palabras)

total = sum(conteo.values())

for palabra, cantidad in conteo.items():
    print(palabra, "->", cantidad / total)