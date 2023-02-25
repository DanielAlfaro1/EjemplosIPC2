from .Dato import *

class Nodo:

    def __init__(self, Columna, Fila):
        self.Ficha = Dato(Fila, Columna)
        self.Siguiente = None

    def ObtenerFila(self):
        return self.Ficha.ObtenerFila()
    
    def ObtenerColumna(self):
        return self.Ficha.ObtenerColumna()

    def SetFila (self, fila):
        self.Ficha.Fila = fila

    def SetColumna (self, columna):
        self.Ficha.Columna = columna