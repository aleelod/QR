import cv2 #libreria de opencv
import numpy as np 

camara = cv2.VideoCapture(2)

# settings de la camara
camara.set (cv2.CAP_PROP_FRAME_WIDTH, 1280)
camara.set (cv2.CAP_PROP_FRAME_HEIGHT, 720)

detector = cv2.QRCodeDetector()

