# Retropropagación simple

objetivo = 10
salida = 7

error = objetivo - salida

print("Error:", error)

# ajuste
peso = 0.5

peso = peso + (0.1 * error)

print("Nuevo peso:", peso)