# Ponderación de verosimilitud

eventos = [0.2, 0.5, 0.8]
pesos = [1, 2, 3]

resultado = sum(e * p for e, p in zip(eventos, pesos))
normalizacion = sum(pesos)

print("Resultado ponderado:",
      resultado / normalizacion)