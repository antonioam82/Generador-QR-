from tkinter import *
from tkinter import messagebox, filedialog
import tkinter.scrolledtext as scrolledtext
import threading
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode
import pyautogui
import time
import numpy as np
import cv2
import os

def abrir():
    ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR ARCHIVO",
                    filetypes =(("png files","*.png") ,("jpg files","*.jpg")))
    if ruta != "":
        archivo = cv2.imread(ruta)
        info = decode(archivo)
        if info != []:
            display.delete('1.0',END)
            display.insert(END,info[0][0])

def screen_shot():
    pyautogui.screenshot("QRsearch_screenshoot.jpg")
    archivo = cv2.imread("QRsearch_screenshoot.jpg")
    info = decode(archivo)
    if info != []:
        display.delete('1.0',END)
        display.insert(END,info[0][0])
    else:
        messagebox.showwarning("QR NO ENCONTRADO","NO SE DETECTÓ CÓDIGO")
    os.remove("QRsearch_screenshoot.jpg")

ventana = Tk()
ventana.title('LECTOR DE CÓDIGOS QR')
ventana.geometry("520x235")
ventana.configure(background="SlateGray2")
file_name=""

display = scrolledtext.ScrolledText(ventana,width=66,foreground='black',height=3,padx=10, pady=10,font=('Arial', 10))
display.place(x=9,y=50)
btnCargar = Button(ventana, text="CARGAR CÓDIGO",bg="khaki",width=22,command=abrir).place(x=178,y=140)
btnScreen = Button(ventana, text="DETECTAR QR EN PANTALLA",bg="khaki",command=screen_shot).place(x=178,y=175)
btnCamara = Button(ventana, text="USAR CAMARA",bg="khaki",width=22).place(x=178,y=205)

ventana.mainloop()



