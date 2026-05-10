# Iteración de Políticas

print("=== ITERACIÓN DE POLÍTICAS ===")

estados = [0, 1]
acciones = ["A", "B"]

# Recompensas de ejemplo
recompensas = {
    (0, "A"): 5,
    (0, "B"): 10,
    (1, "A"): 2,
    (1, "B"): 8
}

politica = {}

for estado in estados:
    mejor_accion = None
    mejor_valor = float('-inf')

    for accion in acciones:
        valor = recompensas[(estado, accion)]

        if valor > mejor_valor:
            mejor_valor = valor
            mejor_accion = accion

    politica[estado] = mejor_accion

print("Política óptima:")
for estado, accion in politica.items():
    print(f"Estado {estado}: Acción {accion}")