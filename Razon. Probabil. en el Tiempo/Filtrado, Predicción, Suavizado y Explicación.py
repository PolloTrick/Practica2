# Ejemplo simplificado

datos = [10, 12, 11, 13, 12]

# Filtrado: promedio móvil
filtrado = sum(datos) / len(datos)

# Predicción simple
prediccion = filtrado + 1

print("Filtrado:", filtrado)
print("Predicción:", prediccion)