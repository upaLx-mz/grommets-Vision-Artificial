# Importar las librerias necesarias
from keras.models import load_model
from PIL import Image, ImageOps
from pathlib import Path
import cv2 as cv
import numpy as np

# Inicio del codigo
np.set_printoptions(suppress=True)


# Declarar la ruta del archivo a trabajar
ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "regco" / "regco_model.h5"
LABELS_PATH = ROOT / "models" / "regco" / "labels.txt"
with open(LABELS_PATH, "r") as f:
    etiquetas = f.readlines()

# Abrir el modelo de IA y sus etiquetas
modelo = load_model(MODEL_PATH, compile=False)
etiquetas = open(LABELS_PATH, 'r').readlines()

# Funcion para el analisis de imagenes en escala de grises
def analisisG(img):
    
    data = np.ndarray(shape=(1, 224, 224, 3), dtype = np.float32)
    
    recorte_pil = Image.fromarray(img)
    recorte = recorte_pil.convert("L")
    
    size = (224, 224)
    recorte = ImageOps.fit(recorte, size, Image.Resampling.LANCZOS)
    
    recorte_array = np.asarray(recorte)
    
    normalized_recorte_array = (recorte_array.astype(np.float32) / 127.5) - 1
    # normalized_recorte_array = np.expand_dims(normalized_recorte_array, axis=-1)
    
    recorte_3_canales = cv.cvtColor(normalized_recorte_array, cv.COLOR_GRAY2RGB)
    
    data[0] = recorte_3_canales
    
    
    prediction = modelo.predict(data) # type: ignore
    index = np.argmax(prediction)
    class_name = etiquetas[index]
    confidence_score = prediction[0][index]
    
    return class_name[2:], confidence_score

def analisisRGB(img):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype = np.float32)
    
    recortePil = Image.fromarray(img)
    recorte = recortePil.convert("RGB")
    
    size = (224, 224)
    recorte = ImageOps.fit(recorte, size, Image.Resampling.LANCZOS)
    
    recorteArray = np.asarray(recorte)
    recorteNormalizado = (recorteArray.astype(np.float32) / 127.5) - 1
    
    data[0] = recorteNormalizado
    
    prediction = modelo.predict(data) # type: ignore
    index = np.argmax(prediction)
    objeto = etiquetas[index]
    confianza = prediction[0][index]
    
    return objeto[2:], confianza

