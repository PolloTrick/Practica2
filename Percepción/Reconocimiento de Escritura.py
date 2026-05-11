# Reconocimiento simple de letras

letras = {
    "A": "/\\",
    "B": "|3"
}

entrada = "/\\"

for letra in letras:
    if letras[letra] == entrada:
        print("Letra reconocida:", letra)