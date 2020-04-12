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

os.chdir(r'C:\Users\Antonio\Documents\AAM images')

class main:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('LECTOR DE CÓDIGOS QR')
        self.ventana.geometry("520x235")
        self.ventana.configure(background = "SlateGray2")
        self.file_name=""
        #cap = cv2.VideoCapture(0)

        self.display=scrolledtext.ScrolledText(self.ventana,width=66,foreground='black',height=3,padx=10, pady=10,font=('Arial', 10))
        self.display.place(x=9,y=50)

        self.btnCargar = Button(self.ventana, text="CARGAR CÓDIGO",bg="khaki",width=22,command=self.abrir)
        self.btnCargar.place(x=178,y=140)
        self.btnScreen = Button(self.ventana, text="DETECTAR QR EN PANTALLA",bg="khaki",command=self.screen_shot)
        self.btnScreen.place(x=178,y=175)
        self.btnCamara = Button(self.ventana, text="USAR CAMARA",bg="khaki",width=22)
        self.btnCamara.place(x=178,y=205)

        self.ventana.mainloop()

    def abrir(self):
        ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR ARCHIVO",
                    filetypes =(("png files","*.png") ,("jpg files","*.jpg")))
        if ruta != "":
            archivo = cv2.imread(ruta)
            info = decode(archivo)
            if info != []:
                self.display.delete('1.0',END)
                self.display.insert(END,info[0][0])
            else:
                messagebox.showwarning("ERROR","NO SE DETECTÓ CÓDIGO")
    def screen_shot(self):
        pyautogui.screenshot("QRsearch_screenshoot.jpg")
        archivo = cv2.imread("QRsearch_screenshoot.jpg")
        info = decode(archivo)
        if info != []:
            self.display.delete('1.0',END)
            self.display.insert(END,info[0][0])
        else:
            messagebox.showwarning("QR NO ENCONTRADO","NO SE DETECTÓ CÓDIGO")
        os.remove("QRsearch_screenshoot.jpg")


        

if __name__=="__main__":
    main()
        



