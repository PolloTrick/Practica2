# Detección simple de cambios

imagen = [10, 10, 10, 80, 80, 80]

for i in range(len(imagen)-1):
    diferencia = abs(imagen[i] - imagen[i+1])

    if diferencia > 20:
        print("Arista detectada en posición:", i)