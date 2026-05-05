# Backjumping simplificado

def backjumping(grafo, colores, asignacion={}, conflictos={}):
    if len(asignacion) == len(grafo):
        return asignacion

    nodo = [n for n in grafo if n not in asignacion][0]
    conflictos[nodo] = set()

    for color in colores:
        valido = True
        for vecino in grafo[nodo]:
            if vecino in asignacion and asignacion[vecino] == color:
                conflictos[nodo].add(vecino)
                valido = False

        if valido:
            asignacion[nodo] = color
            resultado = backjumping(grafo, colores, asignacion, conflictos)

            if resultado:
                return resultado

            del asignacion[nodo]

    return None

# Ejemplo
grafo = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}

colores = ['Rojo', 'Verde']

print(backjumping(grafo, colores))