from tkinter import *
from pyzbar.pyzbar import decode
import cv2
import os

ventana = Tk()
ventana.title('LECTOR DE CÓDIGOS QR')
ventana.geometry("500x220")

etiElement = Label(ventana, text="CARGAR ARCHIVO PNG O JPG",width=68)
etiElement.place(x=9,y=70)

ventana.mainloop()
