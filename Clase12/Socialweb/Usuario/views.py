from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publicacion
#Cambio
from .forms import PubForm, AnalizarForm
#Fin Cambio
from .ObjetoPublicacion import ObjPub

import xml.etree.ElementTree as ET

import requests

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

def VistaUnaPublicacion(request, pk):
    UnaPublicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'Publicacion/Pub_Detalle.html', {'publicacion':UnaPublicacion})

def Nueva_Pub(request):
    if request.method == "POST":
        form = PubForm(request.POST)
        if form.is_valid():
            Pub = form.save(commit=False)
            print(form.data)
            Pub.fecha_Publicacion = timezone.now()
            Pub.save()
            return redirect('detalles_pub', pk=Pub.pk)
    else:
        form = PubForm()
    return render(request, 'Publicacion/Form_Pub.html', {'form': form})

def Edit_Pub(request, pk):
    UnaPublicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = PubForm(request.POST, instance=UnaPublicacion)
        if form.is_valid():
            Pub = form.save(commit=False)
            print(form.data)
            Pub.fecha_Publicacion = timezone.now()
            Pub.save()
            return redirect('detalles_pub', pk=Pub.pk)
    else:
        form = PubForm(instance=UnaPublicacion)
    return render(request, 'Publicacion/Form_Edit_Pub.html', {'form': form})

def PublicacionesOnline(request):
    url = 'http://127.0.0.1:5000/ObtenerPublicaciones'
    r = requests.get(url)
    print("Se hace peticion")
    print(r.content)
    root = ET.fromstring(r.content)
    ListaPublicaciones = []
    for child in root:
        print('Contenido', child)
        if child.tag == 'ListaPublicaciones':
            indice = 0
            for Publicaciones in child.findall('Publicacion'):
                print(Publicaciones)
                autor = ""
                contenido = ""
                fecha = ""
                for hijoPubl in Publicaciones:
                    if hijoPubl.tag == 'Autor':
                        autor = hijoPubl.text
                    elif hijoPubl.tag == 'Contenido':
                        contenido = hijoPubl.text
                    elif hijoPubl.tag == 'FechaPublicacion':
                        fecha = hijoPubl.text
                ListaPublicaciones.append(ObjPub(autor, contenido, fecha, indice))
                indice += 1
    print(ListaPublicaciones)
    Publicaciones = Publicacion.objects.filter(fecha_Publicacion__lte = timezone.now()).order_by('-fecha_Publicacion')
    return render(request, 'PublicacionOnline/Lista_Pubs_Din.html', {'Publicaciones': ListaPublicaciones})

def PublicacionOnline(request, pk):
    url = 'http://127.0.0.1:5000/ObtenerPublicacion'

    Peticion = '''
        <Peticion>
            <idPublicacion>'''+str(pk)+'''</idPublicacion>
        </Peticion>
    '''

    r = requests.post(url, data=Peticion)
    root = ET.fromstring(r.content)
    UnaPublicacion = None
    Codigo = 0
    Mensaje = ""
    for child in root:
        if child.tag == 'Codigo':
            Codigo = child.text
        if child.tag == 'Mensaje':
            Mensaje = child.text
        if child.tag == 'Publicacion':
            autor = ""
            contenido = ""
            fecha = ""
            for hijoPubl in child:
                if hijoPubl.tag == 'Autor':
                    autor = hijoPubl.text
                elif hijoPubl.tag == 'Contenido':
                    contenido = hijoPubl.text
                elif hijoPubl.tag == 'FechaPublicacion':
                    fecha = hijoPubl.text
            UnaPublicacion = ObjPub(autor, contenido, fecha, pk)
    if str(Codigo) == '200':
        return render(request, 'PublicacionOnline/Pub_Detalle.html', {'publicacion':UnaPublicacion})
    return render(request, 'PublicacionOnline/Pub_Detalle.html', {'publicacion':ObjPub(Mensaje, Mensaje, Mensaje, pk)})

#NUEVO
def Analizar(request, pk):
    url = 'http://127.0.0.1:5000/ObtenerPublicacion'

    Peticion = '''
        <Peticion>
            <idPublicacion>'''+str(pk)+'''</idPublicacion>
        </Peticion>
    '''

    r = requests.post(url, data=Peticion)
    root = ET.fromstring(r.content)
    UnaPublicacion = None
    Codigo = 0
    Mensaje = ""
    for child in root:
        print('Contenido', child)
        if child.tag == 'Codigo':
            Codigo = child.text
        if child.tag == 'Mensaje':
            Mensaje = child.text
        if child.tag == 'Publicacion':
            autor = ""
            contenido = ""
            fecha = ""
            for hijoPubl in child:
                if hijoPubl.tag == 'Autor':
                    autor = hijoPubl.text
                elif hijoPubl.tag == 'Contenido':
                    contenido = hijoPubl.text
                elif hijoPubl.tag == 'FechaPublicacion':
                    fecha = hijoPubl.text
            UnaPublicacion = ObjPub(autor, contenido, fecha, pk)
    if request.method == "POST":
        form = AnalizarForm(request.POST)
        if form.is_valid():
            Datos = form.data
            PalabrasClave = "<PalabrasClave>\n"

            for palabra in str(Datos['Palabras']).split(','):
                PalabrasClave += "<PalabraClave>"+palabra+"</PalabraClave>\n"
            PalabrasClave += "</PalabrasClave>\n"
            url = 'http://127.0.0.1:5000/AnalizarPublicacion'
            Peticion = '''
                <Peticion>
                    <idPublicacion>'''+str(pk)+'''</idPublicacion>
                    '''+PalabrasClave+'''
                </Peticion>'''

            r = requests.post(url, data=Peticion)
            root = ET.fromstring(r.content)
            Codigo = 0
            Mensaje = ""
            Cantidad = 0
            for child in root:
                if child.tag == 'Codigo':
                    Codigo = child.text
                if child.tag == 'Mensaje':
                    Mensaje = child.text
                if child.tag == 'Resultado':
                    Cantidad = child.text
            if str(Codigo) != '200':
                return render(request, 'PublicacionOnline/Form_Analizar.html', {'form': form, 'Cantidad': Mensaje, 'publicacion': UnaPublicacion})
            return render(request, 'PublicacionOnline/Form_Analizar.html', {'form': form, 'Cantidad': Cantidad, 'publicacion': UnaPublicacion})
    else:
        form = AnalizarForm()
    Cantidad = 0
    return render(request, 'PublicacionOnline/Form_Analizar.html', {'form': form, 'Cantidad': Cantidad, 'publicacion': UnaPublicacion})


def Nueva_PubOnline(request):
    if request.method == "POST":
        form = PubForm(request.POST)
        if form.is_valid():
            print(form.data)
            Datos = form.data

            url = 'http://127.0.0.1:5000/CrearPublicacion'

            Peticion = '''
                <Peticion>
                    <Autor>'''+str(Datos['autor'])+'''</Autor>
                    <Contenido>'''+str(Datos['Contenido'])+'''</Contenido>
                    <FechaPublicacion>'''+str(timezone.now())+'''</FechaPublicacion>
                </Peticion>
            '''

            r = requests.post(url, data=Peticion)
            print(r.content)
            root = ET.fromstring(r.content)
            Codigo = 0
            Mensaje = ""
            Indice = 0
            for child in root:
                if child.tag == 'Codigo':
                    Codigo = child.text
                if child.tag == 'Mensaje':
                    Mensaje = child.text
                if child.tag == 'idPublicacion':
                    Indice = int(child.text)
            if str(Codigo) == '200':
                return redirect('detalles_pubOnline', pk=Indice)
            return render(request, 'PublicacionOnline/Form_Pub.html', {'form': form})
        return render(request, 'PublicacionOnline/Form_Pub.html', {'form': form})
    else:
        form = PubForm()
    return render(request, 'PublicacionOnline/Form_Pub.html', {'form': form})

def Edit_PubOnline(request, pk):
    
    url = 'http://127.0.0.1:5000/ObtenerPublicacion'

    Peticion = '''
        <Peticion>
            <idPublicacion>'''+str(pk)+'''</idPublicacion>
        </Peticion>
    '''

    r = requests.post(url, data=Peticion)
    root = ET.fromstring(r.content)
    UnaPublicacion = None
    Codigo = 0
    Mensaje = ""
    for child in root:
        if child.tag == 'Codigo':
            Codigo = child.text
        if child.tag == 'Mensaje':
            Mensaje = child.text
        if child.tag == 'Publicacion':
            autor = ""
            contenido = ""
            fecha = ""
            for hijoPubl in child:
                if hijoPubl.tag == 'Autor':
                    autor = hijoPubl.text
                elif hijoPubl.tag == 'Contenido':
                    contenido = hijoPubl.text
                elif hijoPubl.tag == 'FechaPublicacion':
                    fecha = hijoPubl.text
            UnaPublicacion = Publicacion()
            UnaPublicacion.autor = autor
            UnaPublicacion.Contenido= contenido
            UnaPublicacion.fecha_Publicacion = fecha

    if request.method == "POST":
        form = PubForm(request.POST, instance=UnaPublicacion)
        if form.is_valid():
            Datos = form.data
            url = 'http://127.0.0.1:5000/EditarPublicacion'

            Peticion = '''
                <Peticion>
                    <idPublicacion>'''+str(pk)+'''</idPublicacion>
                    <Autor>'''+str(Datos['autor'])+'''</Autor>
                    <Contenido>'''+str(Datos['Contenido'])+'''</Contenido>
                </Peticion>
            '''

            r = requests.post(url, data=Peticion)
            root = ET.fromstring(r.content)
            UnaPublicacion = None
            Codigo = 0
            Mensaje = ""
            for child in root:
                print('Contenido', child)
                if child.tag == 'Codigo':
                    Codigo = child.text
                if child.tag == 'Mensaje':
                    Mensaje = child.text
            if str(Codigo) == '200':
                return redirect('detalles_pubOnline', pk=pk)
    else:
        form = PubForm(instance=UnaPublicacion)
    return render(request, 'Publicacion/Form_Edit_Pub.html', {'form': form})