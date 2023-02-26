from .Dato import *

class NodoDibujo:

    def __init__(self, Columna, Fila, Color, Borde):
        self.Ficha = Ficha(Columna, Fila, Color, Borde)
        self.Siguiente = None

    def ObtenerFila(self):
        return self.Ficha.ObtenerFila()
    
    def ObtenerColumna(self):
        return self.Ficha.ObtenerColumna()
    
    def ObtenerColor(self):
        return self.Ficha.ObtenerColor()
    
    def ObtenerBorde(self):
        return self.Ficha.ObtenerBorde()
    
    def SetFila(self, fila):
        self.Ficha.SetFila(fila)
    
    def setColumna(self, columna):
        self.Ficha.setColumna(columna)
    
    def setColor(self, color):
        self.Ficha.setColor(color)

    def setBorde(self, borde):
        self.Ficha.setBorde(borde)
