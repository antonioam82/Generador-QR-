from tkinter import *
from tkinter import messagebox, filedialog
from unidecode import unidecode
from pyzbar.pyzbar import decode
import pyautogui
import cv2
import os

def abrir():
    ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR ARCHIVO",
                       filetypes =(("png files","*.png") ,("jpg files","*.jpg")))
    if ruta != "":
        archivo = cv2.imread(ruta)
        info = decode(archivo)
        if info != []:
            etiElement.configure(text="ELEMENTO INDENTIFICADO: "+str(info[0][0]))
        else:
            etiElement.configure(text="NO SE DETECTO CÓDIGO")

ventana = Tk()
ventana.title('LECTOR DE CÓDIGOS QR')
ventana.geometry("520x220")

etiElement = Label(ventana, text="CARGAR ARCHIVO PNG O JPG",width=71)
etiElement.place(x=9,y=65)

btnCargar = Button(ventana, text="CARGAR CÓDIGO",bg="khaki",width=22,command=abrir)
btnCargar.place(x=178,y=110)
btnScreen = Button(ventana, text="DETECTAR QR EN PANTALLA",bg="khaki")
btnScreen.place(x=178,y=155)

ventana.mainloop()

