import cv2 # libreria de opencv
import numpy as np 

camara = cv2.VideoCapture(0)

# settings de la camara
camara.set (cv2.CAP_PROP_FRAME_WIDTH, 1280)
camara.set (cv2.CAP_PROP_FRAME_HEIGHT, 720)

detector = cv2.QRCodeDetector()

while camara.isOpened():
    success, imagen = camara.read() 
    
    if not success:
        print ("No se pudo recibir la imagen de la cámara)")
        break

    texto, esquinas, qrbinario = detector.detectAndDecode (imagen)

    if texto != "" and esquinas is not None:
        coordenadas = esquinas[0].astype(int)
        
        cv2.polylines (imagen, [coordenadas], isClosed = True, color = (245, 83, 2), thickness = 4)
        xtexto, ytexto = coordenadas [0]
        y2texto = max (25, ytexto - 10)
        cv2.putText (imagen, texto, (xtexto, y2texto), cv2.FONT_HERSHEY_COMPLEX, 1, (245, 83, 2), 2)

    cv2.imshow('imagen', imagen)
    
    if cv2.waitKey(1) & 0xFF == 27: # esc para detener el programa
        break

camara.release()
cv2.destroyAllWindows()