#pip install opencv-python

import cv2
import os

ruta_guardado='C:/Users/rober/Downloads/captura.jpg'
camara=0

def capturar_y_guardar_foto(ruta_guardado, camara):
    # Inicializar la cámara (0 indica la cámara predeterminada)
    cap = cv2.VideoCapture(camara)

    # Verificar si la cámara se abrió correctamente
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return

    # Capturar una imagen
    ret, frame = cap.read()

    # Guardar la imagen en la ruta especificada
    cv2.imwrite(ruta_guardado, frame)

    # Liberar la cámara
    cap.release()

    print(f"Foto capturada y guardada en: {os.path.abspath(ruta_guardado)}")

# Llama al método para capturar y guardar la foto
capturar_y_guardar_foto(ruta_guardado, camara)