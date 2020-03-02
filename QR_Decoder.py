from pyzbar.pyzbar import decode
from PIL import Image
from VALID import ns
import os

while True:
    archiv = input("Archivo a decodificar: ")
    if archiv in os.listdir():
        info = decode(Image.open(archiv))
        print("\n")
        print(info)
    else:
        print("ARCHIVO NO ENCONTRADO")
    conti = input("\n¿Desea continuar?(n/s): ")
    if conti == "n":
        break
