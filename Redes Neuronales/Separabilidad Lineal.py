# Separabilidad lineal simple

puntos = [
    [1,1],
    [2,2],
    [8,8],
    [9,9]
]

for punto in puntos:
    if punto[0] + punto[1] < 10:
        print(punto, "Clase A")
    else:
        print(punto, "Clase B")