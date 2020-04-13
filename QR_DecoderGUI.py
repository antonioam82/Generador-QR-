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
        #print("ventana")
        self.ventana = Tk()
        self.ventana.title('LECTOR DE CÓDIGOS QR')
        self.ventana.geometry("520x235")
        self.ventana.configure(background = "SlateGray2")
        self.file_name=""
        self.arc=""

        self.display=scrolledtext.ScrolledText(self.ventana,width=66,foreground='black',height=3,padx=10, pady=10,font=('Arial', 10))
        self.display.place(x=9,y=50)

        self.btnCargar = Button(self.ventana, text="CARGAR CÓDIGO",bg="khaki",width=22,command=self.abrir)
        self.btnCargar.place(x=178,y=140)
        self.btnScreen = Button(self.ventana, text="DETECTAR QR EN PANTALLA",bg="khaki",command=self.screen_shot)
        self.btnScreen.place(x=178,y=175)
        self.btnCamara = Button(self.ventana, text="DETECTAR POR CAMARA",bg="khaki",width=22,command=self.inicia_camara)
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
        
    def visor(self):
        ret, frame=self.vid.get_frame()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0,0,image=self.photo,anchor=NW)#0,0
            self.camara.after(15,self.visor)
            
    def inicia_camara(self):
        t = threading.Thread(target=App())
        t.start()

class App:
    def __init__(self,font_video=0):
        #print("camara")
        self.appName = "QR camera"
        self.camara = Toplevel()
        self.camara.title(self.appName)
        self.camara['bg']='black'
        self.font_video=font_video
        self.vid=VideoCaptura(self.font_video)#!!!!!!!!!!!!!!!!!!!!!!!!!
        self.label=Label(self.camara,text=self.appName,font=15,bg='blue',
                         fg='white').pack(side=TOP,fill=BOTH)
        
        self.canvas=Canvas(self.camara,bg='red',width=self.vid.width,height=self.vid.height)
        self.canvas.pack()
        self.btnScreenshot = Button(self.camara,text="LEER",width=30,bg='goldenrod2',
                    activebackground='red',command=self.captura)
        self.btnScreenshot.pack(side=TOP,expand=1, fill=X)
        self.display=scrolledtext.ScrolledText(self.camara,width=86,background='black',foreground="light green",height=2,padx=10, pady=10,font=('Arial', 10))
        self.display.pack(side=TOP)

        self.visor()
        self.camara.mainloop()
        
    def leer(self):
        archivo = cv2.imread("cameraCapt.jpg")
        info = decode(archivo)
        if info != []:
            self.display.delete('1.0',END)
            self.display.insert(END,info[0][0])
        else:
            print("No se detecta código")
        
    def captura(self):
        ver,frame=self.vid.get_frame()
        if ver:
            image="cameraCapt.jpg"
            cv2.imwrite(image,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
            self.leer()
            
    def visor(self):
        #print("visor")
        ret, frame=self.vid.get_frame()
        #self.real_color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0,0,image=self.photo,anchor=NW)#0,0
            self.camara.after(15,self.visor)
#-------------------------------------------------------------------------------------------------------------------------            

class VideoCaptura:
    def __init__(self,font_video=0):
        #print("Vcap")
        self.vid = cv2.VideoCapture(font_video)
        if not self.vid.isOpened():
            raise ValueError("No se puede usar esta camara")
        self.width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
    def get_frame(self):
        if self.vid.isOpened():
            verif,frame=self.vid.read()
            if verif:
                return(verif,cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return(verif,None)
        else:
            return(verif,None)
        

    def __del__(self):
        print("OK")
        #if self.vid.isOpened():
        self.vid.release()
            #self.out.release()
                
if __name__=="__main__":
    main()    
        
          
           
        
         
        


