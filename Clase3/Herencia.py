class Animal:
    Edad = 0

    def __init__(self, Nombre, Accion):
        self.Nombre = str(Nombre)
        self.Acciones = []
        self.Acciones.append(Accion)

    def ActuarTodo (self):
        AccionesString = ""
        for x in self.Acciones:
            AccionesString += str(x) + ", "
        return AccionesString
    
    def Hablar(self):
        return "Bla bla"

    def CumpleAnios(self):
        self.Edad += 1
    
    def Caracteristicas(self):
        return str("Nombre: " + str(self.Nombre)+ " Edad: "+ str(self.Edad))
    

class Mamifero (Animal):

    def __init__(self, Nombre, Accion, Pelaje, Sonido):
        super().__init__(Nombre, Accion)
        self.Pelaje = Pelaje
        self.Sonido = Sonido
    
    def AgregarAccion(self, Accion):
        self.Acciones.append(Accion)
    
    def ActuarTodo(self):
        return str(self.Nombre) + " puede: " + str(super().ActuarTodo())

    def Hablar(self):
        return super().Hablar()
        #return self.Sonido

    def Caracteristicas(self):
        return str("" +super().Caracteristicas()+ " Pelaje: " + str(self.Pelaje))

    def CumpleAnios(self):
        self.Edad += 7

class Ave (Animal):
    def __init__(self, Nombre, Accion, Plumaje, Canto):
        super().__init__(Nombre, Accion)
        self.Plumaje = Plumaje
        self.Canto = Canto
    
    def Hablar(self):
        return self.Canto
    
    
Perro = Mamifero("Firulais", "Correr", "Colocho Café", "Wow wow")
Perico = Ave("Pancho", "Volar", "Verde con Amarillo", "Cotorro Cotorro")

print("------------------Habla------------------")
print(Perro.Hablar())
print(Perico.Hablar())

print("------------------Acciones------------------")
print(Perro.ActuarTodo())
print(Perico.ActuarTodo())

print("------------------Caracteristicas------------------")
Perro.CumpleAnios()
Perro.CumpleAnios()
Perico.CumpleAnios()
print(Perro.Caracteristicas())
print(Perico.Caracteristicas())