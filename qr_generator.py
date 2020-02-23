from tkinter import *
from tkinter import messagebox
import qrcode
import threading

ventana = Tk()
ventana.title("QR Code Generator")
ventana.configure(background="light blue")
ventana.geometry("750x250")
input_text=StringVar()

def inicia():
    t = threading.Thread(target=create_code)
    t.start()

def create_code():
    global img, size
    if input_text.get()!="":
        try:
            data = input_text.get()
            img = qrcode.make(data)
            img.save("my_qrcode.png")
            messagebox.showinfo("QR CREADO","Código creado con éxito")
        except:
            messagebox.showwarning("ERROR","HUBO UN PROBLEMA AL GENERAR EL CÓDIGO")
    else:
        messagebox.showwarning("ERROR","Elemento no especificado")
        
Label(ventana,text="RUTA O DIRECCIÓN",bg="light blue").place(x=322,y=85)
Entry(ventana,font=('Arial',15),width=45,justify="left",textvariable=input_text).place(x=131,y=107)
Button(ventana,text="CREAR CÓDIGO",bg="light green",command=inicia).place(x=330,y=175)

ventana.mainloop()



#from tkinter import *
#from tkinter import messagebox
#import tkinter.scrolledtext as scrolledtext
#import qrcode
#import threading

#ventana = Tk()
#ventana.title("QR Code Generator")
#ventana.configure(background="light blue")
#ventana.geometry("750x250")

#def inicia():
    #t = threading.Thread(target=create_code)
    #t.start()

#def create_code():
    #global img, size
    #texto = display.get('1.0',END)
    #if len(texto) > 1:
        #try:
           #data = texto
            #img = qrcode.make(data)
            #img.save("my_qrcode.png")
            #messagebox.showinfo("QR CREADO","Código creado con éxito")
        #except:
            #messagebox.showwarning("ERROR","HUBO UN PROBLEMA AL GENERAR EL CÓDIGO")
    #else:
        #messagebox.showwarning("ERROR","Elemento no especificado")
        
#Button(ventana,text="CREAR CÓDIGO",fg="black",bg="light green",command=inicia).place(x=330,y=197)
#display=scrolledtext.ScrolledText(ventana,width=66,foreground='black',height=1,padx=10, pady=10,font=('Arial', 10))
#display.place(x=131,y=100)
#Label(ventana,text="TEXTO:",bg="light blue").place(x=88,y=95)

#ventana.mainloop()

