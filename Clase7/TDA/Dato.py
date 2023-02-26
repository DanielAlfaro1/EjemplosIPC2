class Dato:
    
    def __init__ (self, Fila, Columna):
        self.Fila = Fila
        self.Columna = Columna
    
    def ObtenerFila(self):
        return self.Fila
    
    def ObtenerColumna(self):
        return self.Columna
    
class Ficha:
    def __init__(self, Columna, Fila, Color, Borde):
        self.Columna = Columna
        self.Fila = Fila
        self.Color = Color
        self.Borde = Borde

    def ObtenerFila(self):
        return self.Fila
    
    def ObtenerColumna(self):
        return self.Columna
    
    def ObtenerColor(self):
        return self.Color
    
    def ObtenerBorde(self):
        return self.Borde
    
    def SetFila(self, fila):
        self.Fila = fila
    
    def setColumna(self, columna):
        self.Columna = columna
    
    def setColor(self, color):
        self.Color = color

    def setBorde(self, borde):
        self.Borde = borde