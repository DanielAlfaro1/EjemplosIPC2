from Lectura import LecturaXML
from TDA.Cola import Cola
from Dibujo import Dibujar

FichasNegras = Cola('Black')
FichasRojas = Cola('Red')
LecturaXML(FichasNegras, FichasRojas)

print("FICHAS ROJAS")
FichasRojas.Imprimir()
print("FICHAS NEGRAS")
FichasNegras.Imprimir()

print("COMESTIBLES DE ROJAS")
ListaComestibles = FichasRojas.MostrarComida(FichasNegras)
ListaComestibles.Imprimir()

Dibujar(FichasRojas, FichasNegras, ListaComestibles)
'''
FichasRojas.BuscarComida(FichasNegras)

print("FICHAS ROJAS")
FichasRojas.Imprimir()
print("FICHAS NEGRAS")
FichasNegras.Imprimir()

print("COMESTIBLES DE NEGRAS")
FichasNegras.BuscarComida(FichasRojas)

print("FICHAS ROJAS")
FichasRojas.Imprimir()
print("FICHAS NEGRAS")
FichasNegras.Imprimir()
'''