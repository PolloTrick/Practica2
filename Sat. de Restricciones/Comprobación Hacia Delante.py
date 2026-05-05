# Forward Checking - CSP

def es_valido(nodo, color, asignacion, grafo):
    for vecino in grafo[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

def forward_checking(grafo, colores, asignacion={}):
    if len(asignacion) == len(grafo):
        return asignacion

    nodo = [n for n in grafo if n not in asignacion][0]

    for color in colores:
        if es_valido(nodo, color, asignacion, grafo):
            nueva_asignacion = asignacion.copy()
            nueva_asignacion[nodo] = color

            # Reducir dominios de vecinos
            dominios_validos = True
            for vecino in grafo[nodo]:
                if vecino not in nueva_asignacion:
                    posibles = [c for c in colores if es_valido(vecino, c, nueva_asignacion, grafo)]
                    if not posibles:
                        dominios_validos = False
                        break

            if dominios_validos:
                resultado = forward_checking(grafo, colores, nueva_asignacion)
                if resultado:
                    return resultado

    return None

# Ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

colores = ['Rojo', 'Verde', 'Azul']

print(forward_checking(grafo, colores))