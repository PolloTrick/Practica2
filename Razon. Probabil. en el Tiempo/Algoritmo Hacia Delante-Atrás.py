# Forward-Backward simplificado

observaciones = [0.9, 0.8, 0.7]

adelante = []
acumulado = 1

for obs in observaciones:
    acumulado *= obs
    adelante.append(acumulado)

atras = []
acumulado = 1

for obs in reversed(observaciones):
    acumulado *= obs
    atras.append(acumulado)

print("Hacia delante:", adelante)
print("Hacia atrás:", atras[::-1])