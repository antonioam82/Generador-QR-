from tkinter import *
from tkinter import messagebox, filedialog
import tkinter.scrolledtext as scrolledtext
from unidecode import unidecode
import threading
from pyzbar.pyzbar import decode
import pyautogui
import cv2
import os

def screen_shoot():
    pyautogui.screenshot("screenshoot.jpg")
    archivo = cv2.imread("screenshoot.jpg")
    info = decode(archivo)
    if info != []:
        display.insert(END,info[0][0])
    else:
        messagebox.showwarning("ERROR","NO SE DETECTÓ CÓDIGO")
    os.remove("screenshoot.jpg")

def abrir():
    ruta = filedialog.askopenfilename(initialdir="/",title="SELECCIONAR ARCHIVO",
                       filetypes =(("png files","*.png") ,("jpg files","*.jpg")))
    if ruta != "":
        archivo = cv2.imread(ruta)
        info = decode(archivo)
        if info != []:
            display.insert(END,info[0][0])
        else:
            messagebox.showwarning("ERROR","NO SE DETECTÓ CÓDIGO")

def inicia():
    t = threading.Thread(target = screen_shoot())
    t.start

ventana = Tk()
ventana.title('LECTOR DE CÓDIGOS QR')
ventana.geometry("520x220")
ventana.configure(background = "light blue")
file_name=""

display=scrolledtext.ScrolledText(ventana,width=66,foreground='black',height=1,padx=10, pady=10,font=('Arial', 10))
display.place(x=9,y=50)

btnCargar = Button(ventana, text="CARGAR CÓDIGO",bg="khaki",width=22,command=abrir)
btnCargar.place(x=178,y=110)
btnScreen = Button(ventana, text="DETECTAR QR EN PANTALLA",bg="khaki",command=inicia)
btnScreen.place(x=178,y=155)

ventana.mainloop()



