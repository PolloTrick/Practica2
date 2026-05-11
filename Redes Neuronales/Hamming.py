# Distancia de Hamming

cadena1 = "10101"
cadena2 = "10011"

distancia = 0

for i in range(len(cadena1)):
    if cadena1[i] != cadena2[i]:
        distancia += 1

print("Distancia:", distancia)