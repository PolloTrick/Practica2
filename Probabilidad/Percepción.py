# Percepción simple con visión artificial

import cv2 # type: ignore

imagen = cv2.imread("imagen.jpg")

if imagen is not None:
    print("Imagen cargada correctamente")
    print("Dimensiones:", imagen.shape)
else:
    print("No se encontró la imagen")