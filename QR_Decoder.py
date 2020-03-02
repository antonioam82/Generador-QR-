from pyzbar.pyzbar import decode
from PIL import Image
from VALID import ns
import cv2
import os
info = ""

dtector = cv2.QRCodeDetector()

while True:
    print("----------------------------------QR DECODER----------------------------------")
    archiv = input("Archivo a decodificar: ")
    
    if archiv in os.listdir():
        img = cv2.imread(archiv)
        data,bbox,sc=dtector.detectAndDecode(img)
        if bbox is not None:
            info = decode(img)
            print("\n")
            print(info)
        else:
            print("EL ARCHIVO HA DE SER UN CÓDIGO QR")
    else:
        print("ARCHIVO NO ENCONTRADO")
    conti = ns(input("\n¿Desea continuar?(n/s): "))
    if conti == "n":
        break


