# Gramática probabilística simple

gramatica = {
    "S": [("NP VP", 1.0)],
    "NP": [("Juan", 0.5), ("María", 0.5)],
    "VP": [("corre", 0.6), ("come", 0.4)]
}

for regla in gramatica:
    print(regla, "->", gramatica[regla])