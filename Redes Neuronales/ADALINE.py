# ADALINE simple

entradas = [1, 2, 3]
pesos = [0.2, 0.4, 0.6]

salida = 0

for i in range(len(entradas)):
    salida += entradas[i] * pesos[i]

print("Salida ADALINE:", salida)