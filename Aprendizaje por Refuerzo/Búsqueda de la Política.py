# Búsqueda de la Política

politicas = {
    "Politica_A": 10,
    "Politica_B": 25,
    "Politica_C": 15
}

mejor_politica = max(politicas, key=politicas.get)

print("Políticas disponibles:")
for politica, valor in politicas.items():
    print(f"{politica}: {valor}")

print("\nMejor política encontrada:")
print(mejor_politica)