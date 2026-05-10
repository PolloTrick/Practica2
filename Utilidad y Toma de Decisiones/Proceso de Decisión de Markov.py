# Proceso de Decisión de Markov (MDP)

print("=== MDP ===")

estados = ["Inicio", "Meta"]
acciones = ["Avanzar", "Esperar"]

# Recompensas
recompensas = {
    ("Inicio", "Avanzar"): 10,
    ("Inicio", "Esperar"): 2,
    ("Meta", "Avanzar"): 0,
    ("Meta", "Esperar"): 0
}

estado_actual = "Inicio"

for paso in range(3):
    print(f"\nEstado actual: {estado_actual}")

    mejor_accion = max(
        acciones,
        key=lambda a: recompensas.get((estado_actual, a), 0)
    )

    print(f"Mejor acción: {mejor_accion}")

    if mejor_accion == "Avanzar":
        estado_actual = "Meta"

print("\nProceso terminado.")
