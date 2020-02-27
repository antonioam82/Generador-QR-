import tkinter
from tkinter import *
from tkinter import messagebox, ttk
import tkinter.scrolledtext as scrolledtext
import qrcode
import threading

def create_code():
    print(display.get('1.0',END))
    if input_text.get()!="":
        try:
            data = input_text.get()
            img = qrcode.make(data)
            img.save("my_qrcode.png")
            messagebox.showinfo("QR CREADO","Código creado con éxito")
        except:
            messagebox.showwarning("ERROR","HUBO UN PROBLEMA AL GENERAR EL CÓDIGO")
    else:
        messagebox.showwarning("ERROR","Introduce dirección")

def create_codeT():
    #if display.get('2.0',END)!="":
    try:
        data = display.get('1.0',END)
        img = qrcode.make(data)
        img.save("my_qrcode.png")
        messagebox.showinfo("QR CREADO","Código creado con éxito")
    except:
        messagebox.showwarning("ERROR","HUBO UN PROBLEMA AL GENERAR EL CÓDIGO")
    #else:
        #messagebox.showwarning("ERROR","Introduce texto")

def inicia(t):
    if t == "w":
        t = threading.Thread(target=create_code)
        t.start()
    else:
        t = threading.Thread(target=create_codeT)
        t.start()

root = tkinter.Tk()
color = "light blue"
nb = ttk.Notebook(width=750, height=250)
input_text=StringVar()
nb.pressed_index = None

f1 = tkinter.Frame(nb, background=color)
f2 = tkinter.Frame(nb, background=color)
f3 = tkinter.Frame(nb, background=color)

#ELEMENTOS PESTAÑA "f1"
Label(f1,text="RUTA O DIRECCIÓN",bg="light blue").place(x=322,y=74)
Entry(f1,font=('Arial',15),width=45,justify="left",textvariable=input_text).place(x=131,y=97)
Button(f1,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('w')).place(x=330,y=174)
#ELEMENTOS PESTAÑA "f2"
display=scrolledtext.ScrolledText(f2,width=66,foreground='black',height=1,padx=10, pady=10,font=('Arial', 10))
display.place(x=131,y=100)
Label(f2,text="TEXTO:",bg="light blue").place(x=88,y=95)
Button(f2,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('t')).place(x=330,y=174)

nb.add(f1, text='WEB', padding=3)
nb.add(f2, text='TEXTO', padding=3)
nb.add(f3, text='ARCHIVO', padding=3)
nb.pack(expand=1, fill='both')

root.mainloop()


