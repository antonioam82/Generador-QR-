#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyzbar.pyzbar import decode
#from VALID import ns
from unidecode import unidecode
import cv2
import os
info = ""

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

while True:
    print("----------------------------------QR DECODER----------------------------------")
    archiv = (input("QR a leer: "))
    
    if archiv in os.listdir():
        try:
            img = cv2.imread(archiv)
            info = decode(img)
            if info != []:
                print("\nELEMENTO IDENTIFICADO: ",info[0][0])
            else:
                print("EL ARCHIVO HA DE SER UN CÓDIGO QR")
        except:
            print("HUBO UN PROBLEMA AL EFECTUAR LA OPERACIÓN")
    else:
        print("ARCHIVO NO ENCONTRADO")
    conti = ns(input("\n¿Desea continuar?(n/s): "))
    if conti == "n":
        break



