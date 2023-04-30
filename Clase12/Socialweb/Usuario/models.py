from django.db import models
from django.utils import timezone

# Create your models here.
class Publicacion(models.Model):
    autor = models.CharField(max_length=50)
    fecha_Publicacion = models.DateTimeField(default=timezone.now)
    Contenido = models.TextField()

    def Publicar(self):
        self.fecha_Publicacion = timezone.now()
        self.save()

    def __str__(self):
        return "El Autor es: "+str(self.autor) + "\nContenido: "+str(self.Contenido)

class Usuario(models.Model):
    UserName = models.TextField()

    def __str__(self):
        return "El nombre: " + str(self.UserName)


#NUEVO
class PalabrasClave(models.Model):
    Palabras = models.TextField()

    def __str__(self):
        PalabrasClave = ""
        for P in self.Palabras:
            PalabrasClave += str(P)+"\n"
        return "Las palabras son: " + PalabrasClave