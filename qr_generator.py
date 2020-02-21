from tkinter import *
import qrcode

ventana = Tk()
ventana.title("QR Code Generator")
ventana.configure(background="light blue")
ventana.geometry("750x250")
input_text=StringVar()

def create_code():
    if input_text.get()!="":
        data = input_text.get()
        img = qrcode.make(data)
        img.save("my_qrcode.png")
Label(ventana,text="RUTA O DIRECCIÓN",bg="light blue").place(x=322,y=85)
Entry(ventana,font=('Arial',15),width=45,justify="left",textvariable=input_text).place(x=131,y=107)
Button(ventana,text="CREAR CÓDIGO",bg="light green",command=create_code).place(x=330,y=175)

ventana.mainloop()


