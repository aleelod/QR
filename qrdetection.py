import cv2 # libreria de opencv
import numpy as np 

camara = cv2.VideoCapture(0)

# settings de la camara
camara.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camara.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

detector = cv2.QRCodeDetector()

while camara.isOpened():
    success, imagen = camara.read() 
    
    if not success:
        print("No se pudo recibir la imagen de la cámara. Saliendo...")
        break

    link, esquinas, codigoqr = detector.detectAndDecode(imagen)

    if link != "" and esquinas is not None:
        x1 = esquinas[0][0][0]
        y1 = esquinas[0][0][1]
        x2 = esquinas[0][2][0]
        y2 = esquinas[0][2][1]

        cv2.rectangle(imagen, (int(x1), int(y1)), (int(x2), int(y2)), (245, 83, 2), 5)
        cv2.putText(imagen, str(link), (30, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (245, 83, 2), 2)

    cv2.imshow('imagen', imagen)
    
    if cv2.waitKey(1) & 0xFF == 27: # esc para detener el programa
        break

camara.release()
cv2.destroyAllWindows()