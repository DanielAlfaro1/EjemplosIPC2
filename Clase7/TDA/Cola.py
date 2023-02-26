from .Nodo import Nodo

class Cola:

    def __init__(self, Color):
        self.Cabeza = None
        self.Cola = None
        self.Color = Color

    def Insertar(self, Columna, Fila):
        NuevoNodo = Nodo(Columna, Fila)
        if self.Cabeza == None:
            self.Cabeza = NuevoNodo
            self.Cola = NuevoNodo
        else: 
            self.Cola.Siguiente = NuevoNodo
            self.Cola = NuevoNodo
    
    def SetLimites(self, Filas, Columnas):
        self.LimiteVertical = Filas
        self.LimiteHorizontal = Columnas

    def Imprimir(self):
        Auxiliar = self.Cabeza
        while Auxiliar != None:
            print("Fila: " + str(Auxiliar.ObtenerFila()))
            print("Columna: "+ str(Auxiliar.ObtenerColumna()))
            Auxiliar = Auxiliar.Siguiente

    def BuscarComida(self, FichasContrarias):
        Auxiliar = self.Cabeza
        while Auxiliar != None:
            Fila = Auxiliar.ObtenerFila()
            Columna = Auxiliar.ObtenerColumna()
            #Comer1: Fila+1, Columna+1
            if FichasContrarias.BuscarPosicion(Fila+1, Columna+1):
                print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(Fila+1)+" Columna: "+str(Columna+1))
                if (Fila+2 < self.LimiteVertical and Columna+2<self.LimiteHorizontal):
                    FichasContrarias.EliminarPosicion(Fila+1, Columna+1)
                    self.MoverAuxiliar(Auxiliar, Fila+2, Columna+2)
            #Comer1: Fila-1, Columna+1
            elif FichasContrarias.BuscarPosicion(Fila-1, Columna+1):
                print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(Fila-1)+" Columna: "+str(Columna+1))
                if (Fila-2 >= 0 and Columna+2<self.LimiteHorizontal):
                    FichasContrarias.EliminarPosicion(Fila-1, Columna+1)
                    self.MoverAuxiliar(Auxiliar, Fila-2, Columna+2)
            #Comer1: Fila-1, Columna-1
            elif FichasContrarias.BuscarPosicion(Fila-1, Columna-1):
                print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(Fila-1)+" Columna: "+str(Columna-1))
                if (Fila-2 >= 0 and Columna-2 >= 0):
                    FichasContrarias.EliminarPosicion(Fila-1, Columna-1)
                    self.MoverAuxiliar(Auxiliar, Fila-2, Columna-2)
            #Comer1: Fila-1, Columna+1
            elif FichasContrarias.BuscarPosicion(Fila+1, Columna-1):
                print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(Fila+1)+" Columna: "+str(Columna-1))
                if (Fila+2 < self.LimiteVertical and Columna-2 >= 0):
                    FichasContrarias.EliminarPosicion(Fila+1, Columna-1)
                    self.MoverAuxiliar(Auxiliar, Fila+2, Columna-2)
            Auxiliar = Auxiliar.Siguiente

        
    def BuscarPosicion(self, Fila, Columna):
        Auxiliar = self.Cabeza
        while Auxiliar != None:
            #print("Fila: "+str(Fila+1) + " Columna: "+str(Columna+1))
            #print(Auxiliar.ObtenerFila(), Auxiliar.ObtenerColumna())
            if (Auxiliar.ObtenerFila() == Fila and Auxiliar.ObtenerColumna() == Columna):
                return True
            Auxiliar = Auxiliar.Siguiente
        return False
    
    def EliminarPosicion(self, Fila, Columna):
        Auxiliar = self.Cabeza
        Anterior = None
        while Auxiliar != None:
            if (Auxiliar.ObtenerFila() == Fila and Auxiliar.ObtenerColumna() == Columna):
                if Auxiliar == self.Cabeza:
                    self.Cabeza = Auxiliar.Siguiente
                    Auxiliar.Siguiente = None
                else:
                    Anterior.Siguiente = Auxiliar.Siguiente
                    Auxiliar.Siguiente = None
                    if (Auxiliar == self.Cola):
                        self.Cola = Anterior
                return
            Anterior = Auxiliar
            Auxiliar = Auxiliar.Siguiente

    def MoverAuxiliar(self, Ficha, NuevaFila, NuevaColumna):
        Ficha.SetFila(NuevaFila)
        Ficha.SetColumna(NuevaColumna)

    def MostrarComida(self, FichasContrarias):
        ListaComestibles = Cola('White')
        Auxiliar = self.Cabeza
        while Auxiliar != None:
            Fila = Auxiliar.ObtenerFila()
            Columna = Auxiliar.ObtenerColumna()
            #Comer1: Fila+1, Columna+1
            if FichasContrarias.BuscarPosicion(Fila+1, Columna+1):
                print("Ficha en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(Fila+1)+" Columna: "+str(Columna+1))
                if (Fila+2 < self.LimiteVertical and Columna+2<self.LimiteHorizontal):
                    ListaComestibles.Insertar((Columna+1), (Fila+1))
            #Comer1: Fila-1, Columna+1
            elif FichasContrarias.BuscarPosicion(Fila-1, Columna+1):
                print("Ficha en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(Fila-1)+" Columna: "+str(Columna+1))
                if (Fila-2 >= 0 and Columna+2<self.LimiteHorizontal):
                    ListaComestibles.Insertar((Columna+1), (Fila-1))
            #Comer1: Fila-1, Columna-1
            elif FichasContrarias.BuscarPosicion(Fila-1, Columna-1):
                print("Ficha en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(Fila-1)+" Columna: "+str(Columna-1))
                if (Fila-2 >= 0 and Columna-2 >= 0):
                    ListaComestibles.Insertar((Columna-1), (Fila-1))
            #Comer1: Fila+1, Columna-1
            elif FichasContrarias.BuscarPosicion(Fila+1, Columna-1):
                print("Ficha en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(Fila+1)+" Columna: "+str(Columna-1))
                if (Fila+2 < self.LimiteVertical and Columna-2 >= 0):
                    ListaComestibles.Insertar((Columna-1), (Fila+1))
            Auxiliar = Auxiliar.Siguiente
        return ListaComestibles