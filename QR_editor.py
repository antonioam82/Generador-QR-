import segno
import tkinter
from tkinter import *
from tkinter import messagebox, ttk, filedialog
import tkinter.scrolledtext as scrolledtext


class app():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("EDITOR QR")
        self.ventana.configure(bg='light blue',width=700,height=370)
        

        self.display=scrolledtext.ScrolledText(self.ventana,width=70,height=10,font=('Arial', 10))
        self.display.place(x=90,y=60)
        self.ventana.mainloop()

if __name__=="__main__":
    app()
