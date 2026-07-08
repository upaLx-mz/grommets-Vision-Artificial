# IMPORTAR PRIMERAS LIBRERIAS
import os
import sys
import logging

# DEFINIR RUTA DE LIB
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# IMPORTAR LAS DEMAS LIBRERIAS
import cv2 as cv
import numpy as np
from lib import analisys
from pathlib import Path

def __init__():
    
    ROOT = Path(__file__).resolve().parent.parent
    LOG_PATH = ROOT / "out" / "log.txt"
    
    objetos = []
    resultados = []
    
    camara = cv.VideoCapture(0)
    if not camara.isOpened():
        print("No se puede acceder a la camara.")
        exit()
    
    logging.basicConfig(
        filename=LOG_PATH,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        encoding="utf-8",
        filemode="w"
    )
    
    logging.info("Inicio del programa")
    
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
            logging.info("Fin del programa")
            break
        elif key == ord('s'):
            objeto1, resultado1 = analisys.analisisRGB(roi1)
            objeto2, resultado2 = analisys.analisisRGB(roi2)
            objeto3, resultado3 = analisys.analisisRGB(roi3)
            
            objetos = [objeto1, objeto2, objeto3]
            resultados = [resultado1, resultado2, resultado3]
            
            logging.info(objetos)
            logging.info(resultados)
            logging.info("------------------")
            
            if "NOK\n" in objetos or "Faltante\n" in objetos:
                print("No pasa")
            else:
                print("Si pasa")
            
        
        
    camara.release()
    cv.destroyAllWindows()
    exit()

__init__()