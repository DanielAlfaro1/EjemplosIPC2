class ElDato:
        
        def __init__(self, Numero, Cadena):
            self.Numero = Numero
            self.Cadena = Cadena

class Nodo:

    def __init__(self, Numero, Cadena):
        self.Dato = ElDato(Numero, Cadena)
        self.Siguiente = None

    def ObtenerSiguiente(self):
        return self.Siguiente

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo
    
    def ObtenerDato(self):
        return self.Dato

    def ObtenerNumero(self):
        return self.Dato.Numero
    
    def Imprimir(self):
        return str(self.Dato.Numero) + "-" + str(self.Dato.Cadena)