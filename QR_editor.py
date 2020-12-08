import segno
import tkinter
from tkinter import *
from tkinter import messagebox, ttk, filedialog
import tkinter.scrolledtext as scrolledtext


class app():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("EDITOR QR")
        self.ventana.configure(bg='light blue',width=800,height=370)
        self.size = IntVar()
        self.version = IntVar()

        self.display=scrolledtext.ScrolledText(self.ventana,width=70,height=10,font=('Arial', 10))
        self.display.place(x=30,y=30)
        self.btnCreate = Button(self.ventana,text="CREATE CODE",bg="light green",width=15,command=self.create_qr)
        self.btnCreate.place(x=225,y=240)
        self.lblSiz = Label(self.ventana,text="SIZE:",bg="light blue")
        self.lblSiz.place(x=633,y=145)
        self.btnSiz = Entry(self.ventana,width=9,textvariable=self.size)
        self.btnSiz.place(x=670,y=145)
        self.lblVer = Label(self.ventana,text="VERSION:",bg="light blue")
        self.lblVer.place(x=610,y=180)
        self.entryVer = Entry(self.ventana,width=9,textvariable=self.version)
        self.entryVer.place(x=670,y=180)
        self.btnView = Button(self.ventana,text="VIEW CODE",bg="gold2",width=15)
        self.btnView.place(x=615,y=240)
        
        self.ventana.mainloop()

    def create_qr(self):
        qr = segno.make(self.display.get('1.0',END),version=self.version.get(),micro=False)
        qr.save("editedQR.png",scale=self.size.get())
            

if __name__=="__main__":
    app()

