from django.urls import path
from . import views

urlpatterns = [
    path('Estatica/', views.ListaPublicaciones, name='listaPublicaciones'),
    path('Dinamica/', views.ListaDinamica, name='listaDinamica'),
    path('DinamicaOrd/', views.ListaDinamica_Ord, name='ListaDinamica_Ord'),
    path('DinamicaUna/', views.ListaDinamica_Una, name='ListaDinamica_Una')
]