# CSP - Coloreo de grafos

def es_valido(nodo, color, asignacion, grafo):
    for vecino in grafo[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

def csp_backtracking(asignacion, grafo, colores):
    if len(asignacion) == len(grafo):
        return asignacion

    # seleccionar variable no asignada
    nodo = [n for n in grafo if n not in asignacion][0]

    for color in colores:
        if es_valido(nodo, color, asignacion, grafo):
            asignacion[nodo] = color
            resultado = csp_backtracking(asignacion, grafo, colores)

            if resultado:
                return resultado

            del asignacion[nodo]

    return None

# Grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

colores = ['Rojo', 'Verde', 'Azul']

solucion = csp_backtracking({}, grafo, colores)
print(solucion)
