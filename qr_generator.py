from tkinter import *
import qrcode

ventana = Tk()
ventana.title("QR Code Generator")
ventana.configure(background="light blue")
ventana.geometry("750x250")

Entry(ventana,font=('Arial',15,"bold"),width=45,justify="left").place(x=131,y=107)
Button(ventana,text="CREAR CÓDIGO",bg="light green").place(x=330,y=175)

ventana.mainloop()
