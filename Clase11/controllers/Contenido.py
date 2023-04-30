import re

class Publicaciones:
    def __init__(self):
        self.Lista = []
    
    def Agregar(self, Autor, Contenido, Fecha):
        self.Lista.append(PublicacionClase(Autor, Contenido, Fecha))

    def Editar(self, posicion, Autor, Contenido):
        if len(self.Lista) > posicion:
            self.Lista[posicion].Editar(Autor, Contenido)
            return True
        return False
    
    def Publicacion(self, posicion):
        return self.Lista[posicion]

    def Analizar(self, posicion, ListaPalabras):
        if len(self.Lista) > posicion:
            return self.Lista[posicion].Analizar(ListaPalabras)
        return 0

class PublicacionClase:

    def __init__(self, Autor, Contenido, Fecha):
        self.Autor = Autor
        self.Contenido = Contenido
        self.FechaPublicacion = Fecha

    def Editar(self, Autor, Contenido):
        self.Autor = Autor
        self.Contenido = Contenido

    def Analizar(self, PalabrasClave):
        Contador = 0
        if len(PalabrasClave) == 0:
            return 0
        #expresion = "(palabra1|palabra2|palabra3|palabra4)"
        expresion = "("
        posicion = 0
        for palabra in PalabrasClave:
            expresion += palabra
            posicion += 1
            if posicion < len(PalabrasClave):
                expresion += "|"
        expresion += ")"
        Apariciones = re.findall(expresion, self.Contenido)
        return len(Apariciones)

ListaPulbicaciones = [
    {"Autor": "Oscar",
     "Contenido": "Usemos diccionarios, los objetos me dan amsieda.",
     "FechaPublicacion": "22-04-2023 09:53:00"},
     {"Autor": "Luis",
     "Contenido": "Quiten ipc2 de la carrera porque se usa xml",
     "FechaPublicacion": "22-04-2023 09:53:00"}
]

ListaPubs = Publicaciones()
ListaPubs.Agregar("Oscar", "Usemos diccionarios, los objetos me dan amsieda.", "22-04-2023 09:53:00")
ListaPubs.Agregar("Luis", "Quiten ipc2 de la carrera porque se usa xml", "22-04-2023 09:53:00")