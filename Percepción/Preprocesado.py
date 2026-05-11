# Filtro promedio simple

imagen = [10, 20, 30, 40, 50]

filtro = []

for i in range(1, len(imagen)-1):
    promedio = (
        imagen[i-1] +
        imagen[i] +
        imagen[i+1]
    ) / 3

    filtro.append(promedio)

print("Imagen filtrada:", filtro)