import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo mi viejo")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("No se pudo jefe a la vuelta")
        break
    
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    cv.imshow("Previre", gray)
    
    key = cv.waitKey(1)
    
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv.imwrite("Captura.png", gray) 
    
    
cap.release()
cv.destroyAllWindows()