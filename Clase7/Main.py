from Lectura import LecturaXML
from TDA.Cola import Cola

FichasNegras = Cola()
FichasRojas = Cola()
LecturaXML(FichasNegras, FichasRojas)

print("FICHAS ROJAS")
FichasRojas.Imprimir()
print("FICHAS NEGRAS")
FichasNegras.Imprimir()

print("COMESTIBLES DE ROJAS")
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
