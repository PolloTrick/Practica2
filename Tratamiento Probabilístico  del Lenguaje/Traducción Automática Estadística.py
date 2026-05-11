# Traductor simple

diccionario = {
    "hola": "hello",
    "mundo": "world",
    "gato": "cat"
}

frase = ["hola", "mundo"]

traduccion = []

for palabra in frase:
    traduccion.append(diccionario.get(palabra, palabra))

print("Traducción:", " ".join(traduccion))