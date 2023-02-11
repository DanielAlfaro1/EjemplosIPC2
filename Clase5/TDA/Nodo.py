class Nodo:

    def __init__(self, Dato):
        self.Dato = Dato
        self.Siguiente = None

    def ObtenerSiguiente(self):
        return self.Siguiente

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo
    
    def ObtenerDato(self):
        return self.Dato