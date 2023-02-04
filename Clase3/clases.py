class Complejo:

    Real = 0

    def __init__(self, ParteReal, ParteImaginaria):
        self.Real = ParteReal
        self.Imaginaria = ParteImaginaria
    
    def NumeroString(self):
        #return ""+self.Real+self.Imaginario+"i"
        return ""+str(self.Real) + " " +str(self.Imaginaria)+"i"
    
    def Suma(self, ParteReal, ParteImaginaria):
        self.Real = self.Real + float(ParteReal)
        self.Imaginaria = self.Imaginaria + float(ParteImaginaria)

x = Complejo(2.50, 10)
print(x.Real)
print(x.NumeroString())
x.Suma("5.2", 0.5)
print(x.NumeroString())

class Perro:

    Tipo = 'Canino'

    def __init__(self, nombre):
        self.Nombre = nombre
        self.__trucos = [] #Atributo privado
    
    def AgregarTruco(self, Truco):
        self.__trucos.append(str(Truco))
    
    def MostrarTrucos(self):
        for truco in self.__trucos:
            print(self.Nombre,"hace:", truco)
    
    def DevolverTrucos(self):
        return self.__trucos

n = Perro('Borneo') #Objeto 1
x = Perro('Firulais') #Objeto 2
print("------------------------------------------")
print("Tipo Animal:",n.Tipo, "\nNombre:",n.Nombre)
print("------------------------------------------")
print("Tipo Animal:",x.Tipo, "\nNombre:",x.Nombre)

#Cambiar atributos sin método
print("---------------------CAMBIO DE ATRIBUTO---------------------")
n.Tipo = 'Canido'
x.Nombre = 'Fido'

print("------------------------------------------")
print("Tipo Animal:",n.Tipo, "\nNombre:",n.Nombre)
print("------------------------------------------")
print("Tipo Animal:",x.Tipo, "\nNombre:",x.Nombre)

#Atributos privados
print("---------------------Uso de atributos privados---------------------")
n.AgregarTruco("Dar la pata")
n.AgregarTruco("Hacerse el morido")

n.MostrarTrucos()

x.AgregarTruco("Saltar en un aro")
x.AgregarTruco("Comer cereal con cuchara")

print("------------------------------------------")
print("Trucos de ", x.Nombre)
for truco in x.DevolverTrucos():
    print(truco)
print("------------------------------------------")