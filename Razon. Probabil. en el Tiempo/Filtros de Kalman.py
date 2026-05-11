# Filtro de Kalman simplificado

mediciones = [10, 12, 11, 13]

estimacion = mediciones[0]

for medida in mediciones[1:]:
    estimacion = (estimacion + medida) / 2

print("Estimación final:", estimacion)