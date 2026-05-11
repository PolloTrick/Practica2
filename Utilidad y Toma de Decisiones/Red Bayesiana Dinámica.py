# Red Bayesiana Dinámica

print("=== RED BAYESIANA DINÁMICA ===")

probabilidad_lluvia = 0.3

dias = 5

for dia in range(1, dias + 1):
    print(f"\nDía {dia}")

    if probabilidad_lluvia > 0.5:
        clima = "Lluvia"
    else:
        clima = "Soleado"

    print("Clima estimado:", clima)
    print("Probabilidad de lluvia:", round(probabilidad_lluvia, 2))

    # Actualización dinámica
    probabilidad_lluvia += 0.1
    