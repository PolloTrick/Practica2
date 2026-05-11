# Recuperación simple de datos

documentos = [
    "inteligencia artificial",
    "aprendizaje automático",
    "redes neuronales"
]

consulta = "redes"

for doc in documentos:
    if consulta in doc:
        print("Documento encontrado:", doc)