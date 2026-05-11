# Gramática lexicalizada simple

reglas = {
    "NP": [("perro", 0.6), ("gato", 0.4)],
    "VP": [("ladra", 0.7), ("maulla", 0.3)]
}

for categoria in reglas:
    print(categoria, ":", reglas[categoria])