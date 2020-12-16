import segno
import tkinter
import os
import pyperclip
import cv2
import time
import threading
from tkinter import *
from tkinter import messagebox, ttk, filedialog
import tkinter.scrolledtext as scrolledtext

lista = ['M1','M2','M3','M4']

class app():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("EDITOR QR")
        self.ventana.configure(bg='light blue',width=740,height=315)
        self.size = IntVar()
        self.size.set(1)
        self.version = StringVar()
        self.version.set("1")
        self.new_file = ""

        self.display=scrolledtext.ScrolledText(self.ventana,width=70,height=10,font=('Arial', 10))
        self.display.place(x=30,y=30)
        self.copy = Button(self.ventana,text="COPY TEXT",command=self.init_copy)
        self.copy.place(x=30,y=198)
        self.clear = Button(self.ventana,text="CLEAR TEXT",command=self.clear)
        self.clear.place(x=101,y=198)
        self.btnCreate = Button(self.ventana,text="CREATE CODE",bg="light green",width=15,command=self.create_qr)
        self.btnCreate.place(x=225,y=240)
        self.lblSiz = Label(self.ventana,text="SIZE:",bg="light blue")
        self.lblSiz.place(x=593,y=30)
        self.btnSiz = Entry(self.ventana,width=9,textvariable=self.size)
        self.btnSiz.place(x=630,y=30)
        self.btnDark = Button(self.ventana,text="DARK SQRE")
        self.btnDark.place(x=573,y=120)
        self.lblCo1 = Label(bg="black",width=5)
        self.lblCo1.place(x=646,y=122)
        self.btnCo2 = Button(self.ventana,text="LIGHT SQRE")
        self.btnCo2.place(x=571,y=148)
        self.lblCo2 = Label(self.ventana,bg="white",width=5)
        self.lblCo2.place(x=646,y=150)
        self.lblVer = Label(self.ventana,text="VERSION:",bg="light blue")
        self.lblVer.place(x=570,y=70)
        self.entryVer = Entry(self.ventana,width=9,textvariable=self.version)
        self.entryVer.place(x=630,y=70)
        self.btnView = Button(self.ventana,text="VIEW CODE",bg="gold2",width=15,command=self.view_code)
        self.btnView.place(x=575,y=240)
        
        self.ventana.mainloop()

    def create_qr(self):
        self.new_file = filedialog.asksaveasfilename(initialdir="/",title="Guardar en",defaultextension=".png",filetypes=[('png files','*.png'),
                                               ('svg files','*.svg'),('eps files','*.eps'),('txt files','*.txt')])
        if self.new_file != "":
            name,ex = os.path.splitext(self.new_file)
            if self.version.get() not in lista:
                ver = int(self.version.get())
                self.microcode = False
            else:
                ver = self.version.get()
                self.microcode = True
            try:
                if ex != ".txt":
                    qr = segno.make(self.display.get('1.0',END),version=ver,micro=self.microcode)
                    qr.save(self.new_file,scale=self.size.get())
                else:
                    qr = segno.make(self.display.get('1.0',END),micro=self.microcode)
                    qr.save(self.new_file)
                messagebox.showinfo("TAREA COMPLETADA","Código creado con éxito")
            except Exception as e:
                messagebox.showwarning("ERROR",str(e))

    def clear(self):
        self.display.delete('1.0',END)
                
    def copy_text(self):
        self.display.delete('1.0',END)
        self.ultima_copia = pyperclip.paste().strip()
        while True:
            time.sleep(0.1)
            self.copia = pyperclip.paste().strip()
            if self.copia != self.ultima_copia:
                self.display.insert(END,self.copia)
                self.ultima_copia = self.copia 
                print("Done!")
                break

    def view_code(self):
        if self.new_file != "":
            try:
                code = cv2.imread(self.new_file)
                cv2.imshow(self.new_file.split('/')[-1],code)
            except Exception as e:
                messagebox.showwarning("ERROR",str(e))
            
    def init_copy(self):
        print("copiando")
        t = threading.Thread(target=self.copy_text)
        t.start()

if __name__=="__main__":
    app()

