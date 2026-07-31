import cv2 as cv


def camaras(maxCam = 10):
    camarasDisp = []
    
    for index in range(maxCam):
        cap = cv.VideoCapture(index, cv.CAP_DSHOW)

        if cap.isOpened:
            ret, _ = cap.read()
            
            if ret:
                camarasDisp.append(index)
            
            cap.release()
        
        return camarasDisp

def elegir():
    print("Buscando camaras disponibles...")
    
    cam = camaras()
    
    if not cam:
        print("No se encontro ninguna camara")
        exit()
    
    print("\n Camaras disponibles:")
    for i, j in enumerate(cam):
        print(f"[{i}] Cámara indice {j}")
    
    while 1:
        try:
            seleccion = int(input("\n Selecciona el numero de la cámara a usar: "))
            if 0 <= seleccion < len(cam):
                return cam[seleccion]
            else:
                print("Numero fuera de rango, intentar de nuevo")
            
        except ValueError:
            print("Por favor ingresar un numero valido")