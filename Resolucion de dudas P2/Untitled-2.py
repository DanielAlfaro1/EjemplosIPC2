from tkinter import Tk, Text
from tkinter import ttk
import tkinter as tk

class Lista:
    def __init__(self):
        self.Inicio = None
    
    def insertar(self, Nombre, Simbolo, Numero):
        if self.RevisarExistencia(Nombre, Simbolo, Numero) == True:
            print("Ya existe un elemento con alguno de esos 3 parámetros")
            return
        Elementito = Elemento(Nombre, Simbolo, Numero)
        aux = self.Inicio
        if aux == None:
            self.Inicio = Elementito
        else:
            while(aux.Siguiente != None):
                aux = aux.Siguiente
            aux.Siguiente = Elementito

    def imprimirTexto(self):
        aux = self.Inicio
        Texto = ""
        while (aux != None):
            Texto += aux.imprimirContenido()
            aux = aux.Siguiente
        return Texto
    
    def DevolverInicio(self):
        return self.Inicio
    
    def RevisarExistencia(self, Nombre, Simbolo, Numero):
        aux = self.Inicio
        while aux != None:
            if str.upper(aux.Nombre) == str.upper(Nombre):
                return True
            if str.upper(aux.Simbolo) == str.upper(Simbolo):
                return True
            if aux.Numero == Numero:
                return True
            aux = aux.Siguiente
        return False

class Elemento:
    def __init__(self, Nombre, Simbolo, Numero):
        self.Siguiente = None
        self.Nombre = Nombre
        self.Simbolo = Simbolo
        self.Numero = Numero
    
    def imprimirContenido(self):
        return "Nombre: " + str(self.Nombre) + " Simbolo: " + str(self.Simbolo) + " Numero: " + str(self.Numero) + "\n"


ListaElementos = Lista()
ListaElementos.insertar("Hierro", "Fe", 3)
ListaElementos.insertar("Hierro", "Fe", 3)
ListaElementos.insertar("Plata", "Au", 5)
ListaElementos.insertar("Piata", "AU", 7)
ListaElementos.insertar("Helio", "He", 2)
ListaElementos.insertar("Halio", "hO", 2)
ListaElementos.insertar("Oro", "Ag", 6)
ListaElementos.insertar("Oro", "A", 10)


print(ListaElementos.imprimirTexto())

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack()

text.insert('1.0', ListaElementos.imprimirTexto())

columnas = ("nombre", "Simbolo", "Numero Atómico")
treeview = ttk.Treeview (root, show = "headings", columns=columnas) # tabla
 
treeview.column ("nombre", width= 300 ) # indica una columna, no se muestra
treeview.column ("Simbolo", width = 100)
treeview.column ("Numero Atómico", width = 50 )

treeview.heading ("nombre", text = "Nombre") # mostrar encabezado de tabla
treeview.heading ("Simbolo", text = "Simbolo")
treeview.heading ("Numero Atómico", text = "Numero Atómico")

 
#nombre = ['Computadora1', 'Servidor', 'Computadora portátil']
#ipcode = ['10.13.71.223','10.25.61.186','10.25.11.163']
#para i en rango (min (len (nombre), len (ipcode))): # escribir datos
#    treeview.insert('', i, values=(name[i], ipcode[i]))
# root.mainloop () # ingrese el bucle de mensa
aux = ListaElementos.DevolverInicio()
i = 0
while (aux != None):
    treeview.insert('', i, values=(aux.Nombre, aux.Simbolo, aux.Numero))
    aux = aux.Siguiente

treeview.pack(side=tk.LEFT, fill=tk.BOTH)

root.mainloop()

