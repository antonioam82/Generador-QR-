#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from tkinter import *
from tkinter import messagebox, ttk, filedialog
import tkinter.scrolledtext as scrolledtext
import qrcode
import threading

def create_code(ti):
    global data
    try:
        if ti == "w":
            data = input_text.get()
        if ti == "t":
            data = display.get('1.0',END)
        #print(data)
        img = qrcode.make(data)
        img.save("my_qrcode"+formato)
        messagebox.showinfo("QR CREADO","Código creado con éxito")
    except:
        messagebox.showwarning("ERROR","HUBO UN PROBLEMA AL GENERAR EL CÓDIGO")

def abrir_archivo(ex,n):
    global data
    ruta = filedialog.askopenfilename(initialdir = "/",
           title = "Seleccione Archivo",filetypes = ((ex+" files","*."+ex),
           ("all files","*.*")))
    data = str(ruta.split("/")[-1])
    label_file[n].configure(text="ELEMENTO SELECCIONADO: "+data)
 
    #print(data)

def inicia(t):
        t = threading.Thread(target=create_code,args=t)
        t.start()

def cambia_formato(f,tf):
    global formato, texto_formato
    formato = f
    texto_formato = tf
    for el in bts:
        el.configure(text=texto_formato)

root = tkinter.Tk()
root.title("QR Code Generator")
color = "light blue"
nb = ttk.Notebook(width=997, height=250)#765
input_text=StringVar()
input_text2=StringVar()
nb.pressed_index = None
formato = ".png"
texto_formato = "FORMATO: PNG"

f1 = tkinter.Frame(nb, background=color)
f2 = tkinter.Frame(nb, background=color)
f3 = tkinter.Frame(nb, background=color)
f4 = tkinter.Frame(nb, background=color)
f5 = tkinter.Frame(nb, background=color)
f6 = tkinter.Frame(nb, background=color)
f7 = tkinter.Frame(nb, background=color)

#ELEMENTOS PESTAÑA "f1"
Label(f1,text="DIRECCIÓN WEB",bg="light blue").place(x=331,y=74)
Entry(f1,font=('Arial',15),width=45,justify="left",textvariable=input_text).place(x=131,y=97)
Button(f1,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('w')).place(x=330,y=174)
etiFormato1=Label(f1,text=texto_formato,bg="light blue")
etiFormato1.place(x=751,y=66)#780
Button(f1,text="PNG",width=15,bg="light green",command=lambda:cambia_formato('.png','FORMATO: PNG')).place(x=754,y=97)
Button(f1,text="JPG",width=15,bg="light green",command=lambda:cambia_formato('.jpg','FORMATO: JPG')).place(x=754,y=130)
#ELEMENTOS PESTAÑA "f2"
display=scrolledtext.ScrolledText(f2,width=66,foreground='black',height=1,padx=10, pady=10,font=('Arial', 10))
display.place(x=131,y=97)
Label(f2,text="TEXTO:",bg="light blue").place(x=88,y=95)
Button(f2,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('t')).place(x=330,y=174)
etiFormato2=Label(f2,text=texto_formato,bg="light blue")
etiFormato2.place(x=751,y=66)
Button(f2,text="PNG",width=15,bg="light green",command=lambda:cambia_formato('.png','FORMATO: PNG')).place(x=754,y=97)#754
Button(f2,text="JPG",width=15,bg="light green",command=lambda:cambia_formato('.jpg','FORMATO: JPG')).place(x=754,y=130)
#ELEMENTOS PESTAÑA "f3"
Button(f3,text="PNG",width=15,bg="light green",command=lambda:cambia_formato('.png','FORMATO: PNG')).place(x=754,y=97)#754
Button(f3,text="JPG",width=15,bg="light green",command=lambda:cambia_formato('.jpg','FORMATO: JPG')).place(x=754,y=130)
Button(f3,text="BUSCAR PNG",fg="black",width=15,bg="light green",command=lambda:abrir_archivo("png",0)).place(x=321,y=130)
Button(f3,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('m')).place(x=330,y=174)
etiElemen1=Label(f3,text="NINGÚN ELEMENTO SELECIONADO",bg="light blue",width=80)
etiElemen1.place(x=97,y=70)
etiFormato3=Label(f3,text=texto_formato,bg="light blue")
etiFormato3.place(x=751,y=66)
#ELEMENTOS PESTAÑA "f4"
Button(f4,text="PNG",width=15,bg="light green",command=lambda:cambia_formato('.png','FORMATO: PNG')).place(x=754,y=97)#754
Button(f4,text="JPG",width=15,bg="light green",command=lambda:cambia_formato('.jpg','FORMATO: JPG')).place(x=754,y=130)
Button(f4,text="BUSCAR JPG",fg="black",width=15,bg="light green",command=lambda:abrir_archivo("jpg",1)).place(x=321,y=130)
Button(f4,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('m')).place(x=330,y=174)
etiElemen2=Label(f4,text="NINGÚN ELEMENTO SELECIONADO",bg="light blue",width=80)
etiElemen2.place(x=97,y=70)
etiFormato4=Label(f4,text=texto_formato,bg="light blue")
etiFormato4.place(x=751,y=66)
#ELEMENTOS PESTAÑA "f5"
Button(f5,text="PNG",width=15,bg="light green",command=lambda:cambia_formato('.png','FORMATO: PNG')).place(x=754,y=97)#754
Button(f5,text="JPG",width=15,bg="light green",command=lambda:cambia_formato('.jpg','FORMATO: JPG')).place(x=754,y=130)
Button(f5,text="BUSCAR MP3",fg="black",width=15,bg="light green",command=lambda:abrir_archivo("mp3",2)).place(x=321,y=130)
Button(f5,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('m')).place(x=330,y=174)
etiElemen3=Label(f5,text="NINGÚN ELEMENTO SELECIONADO",bg="light blue",width=80)
etiElemen3.place(x=97,y=70)
etiFormato5=Label(f5,text=texto_formato,bg="light blue")
etiFormato5.place(x=751,y=66)
#ELEMENTOS PESTAÑA "f6"
Button(f6,text="PNG",width=15,bg="light green",command=lambda:cambia_formato('.png','FORMATO: PNG')).place(x=754,y=97)#754
Button(f6,text="JPG",width=15,bg="light green",command=lambda:cambia_formato('.jpg','FORMATO: JPG')).place(x=754,y=130)
Button(f6,text="BUSCAR PDF",fg="black",width=15,bg="light green",command=lambda:abrir_archivo("pdf",3)).place(x=321,y=130)
Button(f6,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('m')).place(x=330,y=174)
etiElemen4=Label(f6,text="NINGÚN ELEMENTO SELECIONADO",bg="light blue",width=80)
etiElemen4.place(x=97,y=70)
etiFormato6=Label(f6,text=texto_formato,bg="light blue")
etiFormato6.place(x=751,y=66)
#ELEMENTOS PESTAÑA "f7"
Button(f7,text="PNG",width=15,bg="light green",command=lambda:cambia_formato('.png','FORMATO: PNG')).place(x=754,y=97)#754
Button(f7,text="JPG",width=15,bg="light green",command=lambda:cambia_formato('.jpg','FORMATO: JPG')).place(x=754,y=130)
Button(f7,text="BUSCAR VIDEO",fg="black",width=15,bg="light green",command=lambda:abrir_archivo("mp4",4)).place(x=321,y=130)
Button(f7,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('m')).place(x=330,y=174)
etiElemen5=Label(f7,text="NINGÚN ELEMENTO SELECIONADO",bg="light blue",width=80)
etiElemen5.place(x=97,y=70)
etiFormato7=Label(f7,text=texto_formato,bg="light blue")
etiFormato7.place(x=751,y=66)

bts = [etiFormato1,etiFormato2,etiFormato3,etiFormato4,etiFormato5,etiFormato6,etiFormato7]
label_file = [etiElemen1,etiElemen2,etiElemen3,etiElemen4,etiElemen5]

nb.add(f1, text='WEB', padding=3)
nb.add(f2, text='TEXTO', padding=3)
nb.add(f3, text='PNG', padding=3)
nb.add(f4, text='JPG',padding=3)
nb.add(f5, text='MP3',padding=3)
nb.add(f6, text='PDF',padding=3)
nb.add(f7, text='MP4',padding=3)
nb.pack(expand=1, fill='both')

root.mainloop()

