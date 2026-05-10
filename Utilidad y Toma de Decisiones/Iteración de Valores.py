# Iteración de Valores

print("=== ITERACIÓN DE VALORES ===")

estados = [0, 1]
recompensas = [5, 10]
gamma = 0.9
valores = [0, 0]

for iteracion in range(10):
    nuevos_valores = valores.copy()

    for estado in estados:
        nuevos_valores[estado] = recompensas[estado] + gamma * valores[estado]

    valores = nuevos_valores

print("Valores finales:")
for i, valor in enumerate(valores):
    print(f"Estado {i}: {valor:.2f}")