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

    detectado, textos, esquinas, qrbinario = detector.detectAndDecodeMulti(imagen)

    if detectado:
        for texto, esquina in zip(textos, esquinas):
            if texto != "":
                coordenadas = esquina.astype(int)
                cv2.polylines (imagen, [coordenadas], isClosed=True, color=(245, 83, 2), thickness=2)
                xtexto, ytexto = coordenadas[0]
                
                cv2.putText(imagen, texto, (xtexto, max(25, ytexto - 10)), cv2.FONT_HERSHEY_COMPLEX,
                    0.8, (245, 83, 2), 2,)

    cv2.imshow('imagen', imagen)
    
    if cv2.waitKey(1) & 0xFF == 27: # esc para detener el programa
        break

camara.release()
cv2.destroyAllWindows()