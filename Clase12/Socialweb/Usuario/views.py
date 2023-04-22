from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

# Create your views here.
def ListaPublicaciones(request):
    return render(request, 'Publicacion/Lista_Pubs.html', {})

def ListaDinamica(request):
    Publicaciones = Publicacion.objects.filter(fecha_Publicacion__lte = timezone.now()).order_by('-fecha_Publicacion')
    return render(request, 'Publicacion/Lista_Pubs_Din.html', {'Publicaciones': Publicaciones})

def ListaDinamica_Ord(request):
    Publicaciones = Publicacion.objects.filter(fecha_Publicacion__lte = timezone.now()).order_by('fecha_Publicacion')
    return render(request, 'Publicacion/Lista_Pubs_Din.html', {'Publicaciones': Publicaciones})

def ListaDinamica_Una(request):
    Publicaciones = Publicacion.objects.filter(autor='Luis')
    return render(request, 'Publicacion/Lista_Pubs_Din.html', {'Publicaciones': Publicaciones})
