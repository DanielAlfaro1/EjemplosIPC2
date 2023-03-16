from tkinter import *
from tkinter import ttk

from TDA.ListaDoble import ListaDoble

ListaElementos = ListaDoble(1, 4)

def Cerrar(root):
    print("Cerrar")
    root.destroy()

def Agregar(Entrada):
    print(Entrada)
    ListaElementos.Agregar(Entrada)

def Imprimir():
    ListaElementos.Imprimir()

root = Tk() #Creamos elemento VENTANA
frm = ttk.Frame(root, padding=10) #Le damos forma o tamaño a la ventana
frm.grid() #Definimos un espacio para el contenido
ttk.Label(frm, text="Hello World!").grid(column=0, row=0) #Agregamos un label
Entrada1 = Entry(frm, bd=5) #Agregamos un cuadro de texto
Entrada1.grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=lambda:Cerrar(root)).grid(column=0, row=1) #agregamos un botón
ttk.Button(frm, text="Agregar", command=lambda:Agregar(Entrada1.get())).grid(column=1, row=1) #agregamos un botón
ttk.Button(frm, text="Imprimir", command=lambda:Imprimir()).grid(column=0, row=2) #agregamos un botón
root.mainloop() #iniciamos la ventana

