# Manto de Markov simplificado

red = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

nodo = "B"

print("Manto de Markov de", nodo, ":", red[nodo])