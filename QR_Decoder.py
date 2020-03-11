#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyzbar.pyzbar import decode
from VALID import ns
from unidecode import unidecode
import cv2
import os
info = ""

while True:
    print("----------------------------------QR DECODER----------------------------------")
    archiv = (input("QR a leer: "))
    
    if archiv in os.listdir():
        try:
            img = cv2.imread(archiv)
            info = decode(img)
            if info != []:
                print("\n")
                print(info)
            else:
                print("INTRODUCE UN CÓDIGO QR VÁLIDO")
        except:
            print("HUBO UN PROBLEMA AL EFECTUAR LA OPERACIÓN")
    else:
        print("ARCHIVO NO ENCONTRADO")
    conti = ns(input("\n¿Desea continuar?(n/s): "))
    if conti == "n":
        break



