# Etiquetado simple de líneas

lineas = [
    (0,0,5,5),
    (1,1,1,5)
]

for linea in lineas:
    x1, y1, x2, y2 = linea

    if x1 == x2:
        print("Línea vertical")
    elif y1 == y2:
        print("Línea horizontal")
    else:
        print("Línea diagonal")