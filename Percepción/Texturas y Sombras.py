# Simulación de sombra

intensidad_luz = 100

objetos = [20, 40, 60]

for objeto in objetos:
    sombra = intensidad_luz - objeto
    print("Sombra:", sombra)