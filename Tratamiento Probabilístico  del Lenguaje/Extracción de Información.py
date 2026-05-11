# Extracción simple de información

texto = "Juan vive en Guadalajara"

palabras = texto.split()

nombre = palabras[0]
ciudad = palabras[-1]

print("Nombre:", nombre)
print("Ciudad:", ciudad)