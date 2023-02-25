class Dato:
    
    def __init__ (self, Fila, Columna):
        self.Fila = Fila
        self.Columna = Columna
    
    def ObtenerFila(self):
        return self.Fila
    
    def ObtenerColumna(self):
        return self.Columna
    
class Ficha:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y