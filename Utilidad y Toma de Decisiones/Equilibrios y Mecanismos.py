# Teoría de Juegos: Equilibrios y Mecanismos

print("=== TEORÍA DE JUEGOS ===")

jugador1 = ["Cooperar", "Traicionar"]
jugador2 = ["Cooperar", "Traicionar"]

pagos = {
    ("Cooperar", "Cooperar"): (3, 3),
    ("Cooperar", "Traicionar"): (0, 5),
    ("Traicionar", "Cooperar"): (5, 0),
    ("Traicionar", "Traicionar"): (1, 1)
}

for j1 in jugador1:
    for j2 in jugador2:
        resultado = pagos[(j1, j2)]

        print(f"\nJugador 1: {j1}")
        print(f"Jugador 2: {j2}")
        print(f"Puntajes: {resultado}")

print("\nEquilibrio de Nash aproximado: Ambos traicionan.")
