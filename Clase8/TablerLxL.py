class NodoFila:

    def __init__(self, LimiteColumnas, Nombre, Codigo, Color, PosicionCol, Posicion):
        self.Dato = DatoFila(Nombre, Codigo, Color, Posicion, LimiteColumnas, PosicionCol)
        self.Siguiente = None
        self.Anterior = None

class DatoFila:
    def __init__(self, Nombre, Codigo, Color, Posicion, LimiteColumnas, PosicionCol):
        self.Lista = ListaColumnas(LimiteColumnas)
        self.Lista.Insertar(Nombre, Codigo, Color, PosicionCol)
        self.PosFila = Posicion

class NodoColumna:
    def __init__(self, Nombre, Codigo, Color, Posicion):
        self.Dato = DatoColumna(Nombre, Codigo, Color, Posicion)
        self.Siguiente = None
        self.Anterior = None

class DatoColumna:
    def __init__(self, Nombre, Codigo, Color, Posicion):
        self.Nombre = Nombre
        self.Codigo = Codigo
        self.Color = Color
        self.PosColumna = Posicion

class ListaColumnas():
    def __init__(self, LimiteColumnas):
        self.LimiteColumnas = LimiteColumnas
        self.Cabeza = None
        self.Cola = None
    
    def Insertar(self, Nombre, Codigo, Color, Posicion):
        if Posicion >= self.LimiteColumnas:
            print('La posicion está fuera de rango')
            return
        NuevoNodo = NodoColumna(Nombre, Codigo, Color, Posicion)
        if self.Cabeza == None:
            self.Cabeza = NuevoNodo
            self.Cola = NuevoNodo
        else:
            Auxiliar = self.Cabeza
            Anterior = None
            while Auxiliar != None:
                if Auxiliar.Dato.PosColumna > Posicion:
                    if Auxiliar == self.Cabeza:
                        self.Cabeza = NuevoNodo
                    if Anterior != None:
                        Anterior.Siguiente = NuevoNodo
                        NuevoNodo.Anterior = Anterior
                    Auxiliar.Anterior = NuevoNodo
                    NuevoNodo.Siguiente = Auxiliar
                    return
                if Auxiliar.Dato.PosColumna == Posicion:
                    print('No se ingresa, porque esta posicion ya esta ocupada')
                    return
                Anterior = Auxiliar
                Auxiliar = Auxiliar.Siguiente
            self.Cola.Siguiente = NuevoNodo
            NuevoNodo.Anterior = self.Cola
            self.Cola = NuevoNodo

class ListaFilas:

    def __init__(self, LimiteFilas):
        self.Cabeza = None
        self.Cola = None
        self.LimiteFilas = LimiteFilas

    def CrearFila(self, LimiteColumnas, Nombre, Codigo, Color, PosicionCol, Posicion):
        if Posicion >= self.LimiteFilas:
            print("la posicion está fuera del rango")
            return
        NuevaFila = NodoFila(LimiteColumnas, Nombre, Codigo, Color, PosicionCol, Posicion)
        if self.Cabeza == None:
            self.Cabeza = NuevaFila
            self.Cola = NuevaFila
        else:
            Auxiliar = self.Cabeza
            Anterior = None
            while Auxiliar != None:
                if Auxiliar.Dato.PosFila > Posicion:
                    if Auxiliar == self.Cabeza:
                        self.Cabeza = NuevaFila
                    if Anterior != None:
                        Anterior.Siguiente = NuevaFila
                        NuevaFila.Anterior = Anterior
                    Auxiliar.Anterior = NuevaFila
                    NuevaFila.Siguiente = Auxiliar
                    return
                if Auxiliar.Dato.PosFila == Posicion:
                    Auxiliar.Dato.Lista.Insertar(Nombre, Codigo, Color, PosicionCol)
                    return
                Anterior = Auxiliar
                Auxiliar = Auxiliar.Siguiente
            self.Cola.Siguiente = NuevaFila
            NuevaFila.Anterior = self.Cola
            self.Cola = NuevaFila
