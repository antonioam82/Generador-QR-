from tkinter import *
from pyzbar.pyzbar import decode
import pyautogui
import cv2
import os

ventana = Tk()
ventana.title('LECTOR DE CÓDIGOS QR')
ventana.geometry("500x220")

etiElement = Label(ventana, text="CARGAR ARCHIVO PNG O JPG",width=68)
etiElement.place(x=9,y=65)

btnCargar = Button(ventana, text="CARGAR CÓDIGO",bg="khaki",width=22)
btnCargar.place(x=169,y=110)
btnScreen = Button(ventana, text="DETECTAR QR EN PANTALLA",bg="khaki")
btnScreen.place(x=169,y=155)

ventana.mainloop()
