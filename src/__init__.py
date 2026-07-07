# IMPORTAR PRIMERAS LIBRERIAS
import os
import sys

# DEFINIR RUTA DE LIB
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# IMPORTAR LAS DEMAS LIBRERIAS
from lib import analisys
import cv2 as cv
import numpy as np

def __init__():
    camara = cv.VideoCapture(0)
    if not camara.isOpened():
        print("No se puede acceder a la camara.")
        exit()
    
    while 1:
        ret, frame = camara.read()
        
        if not ret:
            print("No se puede acceder al video")
            break
        
        frame = cv.flip(frame, 1)

        cv.rectangle(frame, (270,248), (494,472), (0,255,0), 3)
        cv.rectangle(frame, (528,278), (752,502), (0,255,0), 3)
        cv.rectangle(frame, (786,248), (1010,472), (0,255,0), 3)

        roi1 = frame[248:472, 270:494]
        roi2 = frame[278:502, 528:752]
        roi3 = frame[248:472, 786:1010]
        
        cv.imshow("Preview", frame)
        
        key = cv.waitKey(1)
        
        if key == 27:
            break
        elif key == ord('s'):
            objeto1, resultado1 = analisys.analisisRGB(roi1)
            objeto2, resultado2 = analisys.analisisRGB(roi2)
            objeto3, resultado3 = analisys.analisisRGB(roi3)
            
            print(f"Resultado de recorte 1: {objeto1} detectado con un {resultado1}")
            print(f"Resultado de recorte 2: {objeto2} detectado con un {resultado2}")
            print(f"Resultado de recorte 3: {objeto3} detectado con un {resultado3}")
        
    camara.release()
    cv.destroyAllWindows()
    exit()

__init__()