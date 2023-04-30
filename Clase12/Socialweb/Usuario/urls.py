from django.urls import path
from . import views

urlpatterns = [
    path('Estatica/', views.ListaPublicaciones, name='listaPublicaciones'),
    path('Dinamica/', views.ListaDinamica, name='listaDinamica'),
    path('DinamicaOrd/', views.ListaDinamica_Ord, name='ListaDinamica_Ord'),
    path('DinamicaUna/', views.ListaDinamica_Una, name='ListaDinamica_Una'),
    path('Pub/<int:pk>/', views.VistaUnaPublicacion, name='detalles_pub'),
    path('NuevaPub/', views.Nueva_Pub, name='nueva_pub'),
    path('EditPub/<int:pk>/', views.Edit_Pub, name='edit_pub'),
    path('DinamicaOnline/', views.PublicacionesOnline, name='listaDinamicaOnline'),

    path('Analizar/<int:pk>/', views.Analizar, name='Analizar'),
    path('PubOnline/<int:pk>/', views.PublicacionOnline, name='detalles_pubOnline'),
    path('NuevaPubOnline/', views.Nueva_PubOnline, name='nueva_pubOnline'),
    path('EditPubOnline/<int:pk>/', views.Edit_PubOnline, name='edit_pubOnline'),
]