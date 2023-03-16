from .Nodo import Nodo

class ListaDoble:

    def __init__(self, Id, MaximoElementos):
        self.Cabeza = None
        self.Final = None
        self.Id = Id
        self.Maximo = MaximoElementos
        self.Contador = 0

    def Agregar(self, SimbElement):
        NuevoNodo = Nodo(SimbElement)
        if self.Existe(SimbElement):
            print('Este elemento ya estaba registrado en el pin')
            return
        if self.Contador == self.Maximo:
            print('Ya no se pueden agregar más elementos a este pin')
            return
        if self.Cabeza == None:
            self.Cabeza = NuevoNodo
            self.Final = NuevoNodo
        else:
            self.Final.Siguiente = NuevoNodo
            NuevoNodo.Anterior = self.Final
            self.Final = NuevoNodo
        self.Contador += 1
        
    def Existe(self, SimbElement):
        aux = self.Cabeza
        if aux == None:
            return False
        else:
            while aux != None:
                if aux.Dato == SimbElement:
                    return True
                aux = aux.Siguiente
            return False
        
    def Imprimir(self):
        aux = self.Cabeza
        while aux != None:
            print(aux.Dato)
            aux = aux.Siguiente