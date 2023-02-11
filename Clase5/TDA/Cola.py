from .Nodo import Nodo

class Cola:

    def __init__(self):
        self.Inicio = None
        self.Final = None

    def Insertar(self, Dato):
        NuevoNodo = Nodo(Dato)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.Siguiente = NuevoNodo
            self.Final = NuevoNodo
    
    def Pop(self):
        if self.Inicio == None:
            return None
        Auxiliar = self.Inicio
        if self.Inicio == self.Final:
            self.Final = None
        self.Inicio = self.Inicio.Siguiente
        Auxiliar.Siguiente = None
        return Auxiliar

    def Impimir(self):
        Retorno = "En la cola del banco están formados: ["
        if self.Inicio == None:
            return "La cola está vacía."
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Retorno += Auxiliar.ObtenerDato()
            if Auxiliar.Siguiente != None:
                Retorno += ", "
            Auxiliar = Auxiliar.Siguiente
        Retorno += "]"
        return Retorno