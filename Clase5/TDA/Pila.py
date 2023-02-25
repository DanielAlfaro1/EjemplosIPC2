from .Nodo import Nodo

class Pila:

    def __init__(self):
        self.Inicio = None

    def Push(self, Dato):
        NuevoNodo = Nodo(Dato)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
        else:
            NuevoNodo.AsignarSiguiente(self.Inicio)
            self.Inicio = NuevoNodo

    def Pop(self):
        if self.Inicio == None:
            return None
        Auxiliar = self.Inicio
        self.Inicio = self.Inicio.Siguiente
        Auxiliar.AsignarSiguiente(None)
        return Auxiliar
    
    def Impimir(self):
        Retorno = "La pila tiene: ["
        if self.Inicio == None:
            return "La pila está vacía."
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Retorno += Auxiliar.ObtenerDato()
            if Auxiliar.Siguiente != None:
                Retorno += ", "
            Auxiliar = Auxiliar.Siguiente
        Retorno += "]"
        return Retorno