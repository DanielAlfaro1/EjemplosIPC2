from .Nodo import Nodo

class Lista:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Limite = 0

    def Push(self, Dato):
        NuevoNodo = Nodo(Dato)
        self.Limite += 1
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            NuevoNodo.Siguiente = self.Inicio
            self.Inicio = NuevoNodo
    
    def Insertar(self, Dato):
        NuevoNodo = Nodo(Dato)
        self.Limite += 1
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo

    def Pop(self):
        if self.Inicio == None:
            return None
        Auxiliar = self.Inicio
        if self.Inicio == self.Final:
            #Si el inicio es el mismo nodo del final, indicamos que final sea None
            self.Final = None
        self.Inicio = self.Inicio.ObtenerSiguiente()
        Auxiliar.Siguiente = None
        return Auxiliar
    
    def Buscar(self, Dato):
        if self.Inicio == None:
            return None
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerDato() == Dato:
                #Encontró el dato
                return Auxiliar
            else:
                #Pasamos al siguiente nodo
                Auxiliar = Auxiliar.Siguiente
        #No encontró el dato
        return None

    def EliminarIndice(self, posicion):
        if self.Inicio == None:
            #Lista vacía
            return None
        if posicion >= self.Limite:
            #Posición es mayor al número de nodos
            return None
        Auxiliar = self.Inicio
        Previo = None
        if posicion == 0:
            #Si la posición es la inicial
            if self.Inicio == self.Final:
                #Si solo hay un nodo, damos None a Final
                self.Final = None
            self.Inicio = self.Inicio.Siguiente
            Auxiliar.Siguiente = None
            return Auxiliar
        Contador = 0
        while Auxiliar != None:
            if Contador == posicion:
                #Indicamos a siguiente que se salte auxiliar
                Previo.Siguiente = Auxiliar.Siguiente
                if Auxiliar == self.Final:
                    #Si el auxiliar es igual al Final, debemos mover el final
                    self.Final = Previo
                #Eliminamos el enlace de Auxiliar con la lista
                Auxiliar.Siguiente = None
                return Auxiliar
            else:
                #Desplazamos el nodo auxiliar y añadimos 1 al contador
                Previo = Auxiliar
                Auxiliar = Auxiliar.Siguiente
                Contador += 1

    def Impimir(self):
        Retorno = "La lista tiene: ["
        if self.Inicio == None:
            return "La lista está vacía."
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Retorno += Auxiliar.ObtenerDato()
            if Auxiliar.Siguiente != None:
                Retorno += ", "
            Auxiliar = Auxiliar.Siguiente
        Retorno += "]"
        return Retorno