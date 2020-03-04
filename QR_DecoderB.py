from VALID import ns
import cv2
import os
info = ""

dtector = cv2.QRCodeDetector()

while True:
    print("----------------------------------QR DECODER----------------------------------")
    archiv = input("QR a leer: ")
    
    if archiv in os.listdir():
        img = cv2.imread(archiv)
        data,bbox,sc=dtector.detectAndDecode(img)
        if bbox is not None:
            print("\n")
            print("ELEMENTO: ",data)
        else:
            print("EL ARCHIVO HA DE SER UN CÓDIGO QR")
    else:
        print("ARCHIVO NO ENCONTRADO")
    conti = ns(input("\n¿Desea continuar?(n/s): "))
    if conti == "n":
        break
