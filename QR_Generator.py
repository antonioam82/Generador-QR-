#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from unidecode import unidecode
from tkinter import *
from tkinter import messagebox, ttk, filedialog
import tkinter.scrolledtext as scrolledtext
import qrcode
import pyperclip
import time
import cv2
import threading
import os

def guarda_en():
    global archivoGuardar
    archivoGuardar=filedialog.asksaveasfilename(initialdir="/",title="Guardar en",defaultextension=formato)
    return archivoGuardar
    
def estado_ver(s,i):
    btv[i].configure(state=s)

def create_data(ti):
    global data, nom_archiv, vcard
    if ti == "w":
        data = unidecode(input_text.get())
    elif ti == "t":
        data = unidecode(display.get('1.0',END))
    
def create_code():
    global data, archi, vcard
    try:
        if data != "":
            img = qrcode.make(data)
            archi = guarda_en()
            if archi != "": 
                img.save(archi)
                messagebox.showinfo("QR CREADO","Código creado con éxito")
                estado_ver('normal',index)
    except:
        messagebox.showwarning("ERROR","HUBO UN PROBLEMA AL GENERAR EL CÓDIGO")
    
def ver_codigo():
    try:
        im = cv2.imread(archi)
        cv2.imshow(archivoGuardar.split("/")[-1],im)
    except:
        messagebox.showwarning("ERROR","HUBO UN PROBLEMA AL MOSTRAR EL CÓDIGO")

def abrir_archivo(ex,n):
    global data, nom_archiv, file
    nom_archiv = ""
    data = ""
    for el in btv:
        el.configure(state='disabled')
    #estado_ver('disabled')
    for i in label_file:
        i.configure(text="NINGÚN ELEMENTO SELECCIONADO")
    ruta = filedialog.askopenfilename(initialdir = "/",
           title = "Seleccione Archivo",filetypes = ((ex+" files","*."+ex),
           ("all files","*.*")))
    if ruta != "":
        lista_ruta = ruta.split("/")
        data = str(lista_ruta[-1])
        file,ex=os.path.splitext(data)
        file = unidecode(file)
        label_file[n].configure(text="ELEMENTO SELECCIONADO: "+data)

def inicia(ti,ind):
    global index
    index = ind
    create_data(ti)
    t = threading.Thread(target=create_code)
    t.start()

def cambia_formato(f,tf):
    global formato, texto_formato
    formato = f
    texto_formato = tf
    for el in bts:
        el.configure(text=texto_formato)

def paste_text():
    global ultima_copia
    display.delete('1.0',END)
    ultima_copia = pyperclip.paste().strip()
    while True:
        time.sleep(0.1)
        copia = pyperclip.paste().strip()
        if copia != ultima_copia:
            display.insert(END,copia)
            ultima_copia = copia 
            print("Done!")
            break

def inicia_copia():
    messagebox.showinfo("COPIAR TEXTO","Seleccione el texto a pegar y escoje la opción \'Copiar\'")
    t1 = threading.Thread(target=paste_text)
    t1.start()

root = tkinter.Tk()
root.title("QR Code Generator")
color = "light blue"
ultima_copia = ""
nb = ttk.Notebook(width=997, height=250)#765
input_text=StringVar()
#nb.pressed_index = None
formato = ".png"
texto_formato = "FORMATO: PNG"
data = ""
file = ""
archi = ""

f1 = tkinter.Frame(nb, background=color)
f2 = tkinter.Frame(nb, background=color)
f3 = tkinter.Frame(nb, background=color)
f4 = tkinter.Frame(nb, background=color)
f5 = tkinter.Frame(nb, background=color)
f6 = tkinter.Frame(nb, background=color)
f7 = tkinter.Frame(nb, background=color)
f8 = tkinter.Frame(nb, background=color)

#ELEMENTOS PESTAÑA "f1"
Label(f1,text="DIRECCIÓN WEB",bg="light blue").place(x=331,y=74)
Entry(f1,font=('Arial',15),width=45,justify="left",textvariable=input_text).place(x=131,y=97)
Button(f1,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('w',0)).place(x=330,y=174)
etiFormato1=Label(f1,text=texto_formato,bg="light blue")
etiFormato1.place(x=751,y=66)#780
btnVer1 = Button(f1,text="VER CÓDIGO",bg="gold2",width=15,command=ver_codigo,state='disabled')
btnVer1.place(x=754,y=174)
#ELEMENTOS PESTAÑA "f2"
display=scrolledtext.ScrolledText(f2,width=66,foreground='black',height=1,padx=10, pady=10,font=('Arial', 10))
display.place(x=131,y=97)
Label(f2,text="TEXTO:",bg="light blue").place(x=88,y=95)
Button(f2,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('t',1)).place(x=330,y=174)
etiFormato2=Label(f2,text=texto_formato,bg="light blue")
etiFormato2.place(x=751,y=66)
btnVer2 = Button(f2,text="VER CÓDIGO",bg="gold2",width=15,command=ver_codigo,state='disabled')
btnVer2.place(x=754,y=174)
btnPegar = Button(f2,text="PEGAR UN TEXTO",bg="light gray",command=inicia_copia)
btnPegar.place(x=131,y=150)
#ELEMENTOS PESTAÑA "f3"
Button(f3,text="BUSCAR PNG",fg="black",width=15,bg="light green",command=lambda:abrir_archivo("png",0,2)).place(x=321,y=130)
Button(f3,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('m',2)).place(x=330,y=174)
etiElemen1=Label(f3,text="NINGÚN ELEMENTO SELECCIONADO",bg="light blue",width=80)
etiElemen1.place(x=97,y=70)
etiFormato3=Label(f3,text=texto_formato,bg="light blue")
etiFormato3.place(x=751,y=66)
btnVer3 = Button(f3,text="VER CÓDIGO",bg="gold2",width=15,command=ver_codigo,state='disabled')
btnVer3.place(x=754,y=174)
#ELEMENTOS PESTAÑA "f4"
Button(f4,text="BUSCAR JPG",fg="black",width=15,bg="light green",command=lambda:abrir_archivo("jpg",1)).place(x=321,y=130)
Button(f4,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('m',3)).place(x=330,y=174)
etiElemen2=Label(f4,text="NINGÚN ELEMENTO SELECCIONADO",bg="light blue",width=80)
etiElemen2.place(x=97,y=70)
etiFormato4=Label(f4,text=texto_formato,bg="light blue")
etiFormato4.place(x=751,y=66)
btnVer4 = Button(f4,text="VER CÓDIGO",bg="gold2",width=15,command=ver_codigo,state='disabled')
btnVer4.place(x=754,y=174)
#ELEMENTOS PESTAÑA "f5"
Button(f5,text="BUSCAR MP3",fg="black",width=15,bg="light green",command=lambda:abrir_archivo("mp3",2)).place(x=321,y=130)
Button(f5,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('m',4)).place(x=330,y=174)
etiElemen3=Label(f5,text="NINGÚN ELEMENTO SELECCIONADO",bg="light blue",width=80)
etiElemen3.place(x=97,y=70)
etiFormato5=Label(f5,text=texto_formato,bg="light blue")
etiFormato5.place(x=751,y=66)
btnVer5 = Button(f5,text="VER CÓDIGO",bg="gold2",width=15,command=ver_codigo,state='disabled')
btnVer5.place(x=754,y=174)
#ELEMENTOS PESTAÑA "f6"
Button(f6,text="BUSCAR PDF",fg="black",width=15,bg="light green",command=lambda:abrir_archivo("pdf",3)).place(x=321,y=130)
Button(f6,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('m',5)).place(x=330,y=174)
etiElemen4=Label(f6,text="NINGÚN ELEMENTO SELECCIONADO",bg="light blue",width=80)
etiElemen4.place(x=97,y=70)
etiFormato6=Label(f6,text=texto_formato,bg="light blue")
etiFormato6.place(x=751,y=66)
btnVer6 = Button(f6,text="VER CÓDIGO",bg="gold2",width=15,command=ver_codigo,state='disabled')
btnVer6.place(x=754,y=174)
#ELEMENTOS PESTAÑA "f7"
Button(f7,text="BUSCAR VIDEO",fg="black",width=15,bg="light green",command=lambda:abrir_archivo("mp4",4)).place(x=321,y=130)
Button(f7,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('m',6)).place(x=330,y=174)
etiElemen5=Label(f7,text="NINGÚN ELEMENTO SELECCIONADO",bg="light blue",width=80)
etiElemen5.place(x=97,y=70)
etiFormato7=Label(f7,text=texto_formato,bg="light blue")
etiFormato7.place(x=751,y=66)
btnVer7 = Button(f7,text="VER CÓDIGO",bg="gold2",width=15,command=ver_codigo,state='disabled')
btnVer7.place(x=754,y=174)
#ELEMNTOS PESTAÑA "f8"
Button(f8,text="BUSCAR GIF",fg="black",width=15,bg="light green",command=lambda:abrir_archivo("gif",5)).place(x=321,y=130)
Button(f8,text="CREAR CÓDIGO",fg="black",bg="light green",command=lambda:inicia('m',7)).place(x=330,y=174)
etiElemen6=Label(f8,text="NINGÚN ELEMENTO SELECCIONADO",bg="light blue",width=80)
etiElemen6.place(x=97,y=70)
etiFormato8=Label(f8,text=texto_formato,bg="light blue")
etiFormato8.place(x=751,y=66)
btnVer8 = Button(f8,text="VER CÓDIGO",bg="gold2",width=15,command=ver_codigo,state='disabled')
btnVer8.place(x=754,y=174)

bts = [etiFormato1,etiFormato2,etiFormato3,etiFormato4,etiFormato5,etiFormato6,etiFormato7,etiFormato8]
label_file = [etiElemen1,etiElemen2,etiElemen3,etiElemen4,etiElemen5,etiElemen6]
pestas = [f1,f2,f3,f4,f5,f6,f7,f8]
btv = [btnVer1,btnVer2,btnVer3,btnVer4,btnVer5,btnVer6,btnVer7,btnVer8]

for i in pestas:
    Button(i,text="PNG",width=15,bg="light green",command=lambda:cambia_formato('.png','FORMATO: PNG')).place(x=754,y=97)
    Button(i,text="JPG",width=15,bg="light green",command=lambda:cambia_formato('.jpg','FORMATO: JPG')).place(x=754,y=130)
    
nb.add(f1, text='WEB', padding=3)
nb.add(f2, text='TEXTO', padding=3)
nb.add(f3, text='PNG', padding=3)
nb.add(f4, text='JPG',padding=3)
nb.add(f5, text='MP3',padding=3)
nb.add(f6, text='PDF',padding=3)
nb.add(f7, text='MP4',padding=3)
nb.add(f8, text='GIF',padding=3)
nb.pack(expand=1, fill='both')

root.mainloop()
