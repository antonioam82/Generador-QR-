import segno
import tkinter
import os
import pyperclip
import cv2
import time
import threading
from tkinter import *
from tkinter import messagebox, ttk, filedialog, colorchooser
import tkinter.scrolledtext as scrolledtext

lista = ['M1','M2','M3','M4']

class app():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("QR CREATOR")
        self.ventana.configure(bg='light blue',width=740,height=315)
        self.size = IntVar()
        self.size.set(1)
        self.version = StringVar()
        self.version.set("1")
        self.new_file = ""
        self.SQblack = "#000000"
        self.SQwhite = "#ffffff"

        self.display=scrolledtext.ScrolledText(self.ventana,width=70,height=10,font=('Arial', 10))
        self.display.place(x=30,y=30)
        self.copy = Button(self.ventana,text="COPY TEXT",command=self.init_copy)
        self.copy.place(x=30,y=198)
        self.clear = Button(self.ventana,text="CLEAR TEXT",command=self.clear)
        self.clear.place(x=101,y=198)
        self.btnCreate = Button(self.ventana,text="CREATE CODE",bg="light green",width=15,command=self.create_qr)
        self.btnCreate.place(x=228,y=240)
        self.lblSiz = Label(self.ventana,text="SIZE:",bg="light blue")
        self.lblSiz.place(x=593,y=30)
        self.btnSiz = Entry(self.ventana,width=9,textvariable=self.size)
        self.btnSiz.place(x=630,y=30)
        self.etiCol = Label(self.ventana,text="COLORS:",bg="light blue")
        self.etiCol.place(x=573,y=117)
        self.btnDark = Button(self.ventana,text="DARK",width=8,command=self.darkpart_color)
        self.btnDark.place(x=573,y=137)
        self.lblCo1 = Label(bg="black",width=5)
        self.lblCo1.place(x=646,y=139)
        self.btnCo2 = Button(self.ventana,text="LIGHT",width=8,command=self.lightpart_color)
        self.btnCo2.place(x=573,y=165)
        self.lblCo2 = Label(self.ventana,bg="white",width=5)
        self.lblCo2.place(x=646,y=165)
        self.lblVer = Label(self.ventana,text="VERSION:",bg="light blue")
        self.lblVer.place(x=570,y=70)
        self.entryVer = Entry(self.ventana,width=9,textvariable=self.version)
        self.entryVer.place(x=630,y=70)
        self.btnView = Button(self.ventana,text="DISPLAY CODE",bg="gold2",width=15,command=self.view_code)
        self.btnView.place(x=575,y=240)
        
        self.ventana.mainloop()

    def create_qr(self):
        self.new_file = filedialog.asksaveasfilename(initialdir="/",title="SAVE",defaultextension=".png",filetypes=[('png files','*.png'),
                                               ('svg files','*.svg'),('eps files','*.eps'),('txt files','*.txt')])
        if self.new_file != "":
            name,self.ex = os.path.splitext(self.new_file)
            if self.version.get() not in lista and self.version.get().isdigit():
                ver = int(self.version.get())
                self.microcode = False
            else:
                ver = self.version.get()
                self.microcode = True
            try:
                if self.ex != ".txt":
                    qr = segno.make(self.display.get('1.0',END),version=ver,micro=self.microcode)
                    qr.save(self.new_file,scale=self.size.get(),dark=self.SQblack,light=self.SQwhite)
                else:
                    qr = segno.make(self.display.get('1.0',END),micro=self.microcode)
                    qr.save(self.new_file)
                messagebox.showinfo("TASK COMPLETED","Code created successfully")
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
                break

    def darkpart_color(self):
        _,color = colorchooser.askcolor()
        if color is not None:
            self.SQblack = color
            self.lblCo1.configure(bg=color)
            
    def lightpart_color(self):
        _,color = colorchooser.askcolor()
        if color is not None:
            self.SQwhite = color
            self.lblCo2.configure(bg=color)
    
    def view_code(self):
        if self.new_file != "" and self.ex == ".png":
            try:
                code = cv2.imread(self.new_file)
                cv2.imshow(self.new_file.split('/')[-1],code)
            except Exception as e:
                messagebox.showwarning("ERROR",str(e))
        else:
            messagebox.showinfo("CAN NOT DISPLAY","Can not display the file.")
            
            
    def init_copy(self):
        messagebox.showinfo("COPYING","select text and copy")
        t = threading.Thread(target=self.copy_text)
        t.start()

if __name__=="__main__":
    app()
