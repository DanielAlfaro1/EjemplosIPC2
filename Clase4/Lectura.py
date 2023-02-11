from xml.dom import minidom
from Acceso import *
doc = minidom.parse("../Archivos/Ejemplo.xml")

print("-----------Acceso global-----------")
JuegosViejos = doc.getElementsByTagName("JuegosViejos")
ListaPlataformas = doc.getElementsByTagName("Plataforma")

for Plataforma in ListaPlataformas:
    print(HijosATexto(Plataforma))
    
print("-----------Acceso específico-----------")
JuegosViejos = doc.getElementsByTagName("JuegosViejos")
print("Tamaño JuegosViejos: ", len(JuegosViejos))
for JuegoViejo in JuegosViejos:
    ListaPlataformas = JuegoViejo.getElementsByTagName("ListaPlataformas")
    print("Tamaño ListaPlatformas:", len(ListaPlataformas))
    for UnaPlataforma in ListaPlataformas:
        Plataformas = UnaPlataforma.getElementsByTagName("Plataforma")
        print("Tamaño Plataformas:", len(Plataformas))
        for Plataforma in Plataformas:
            print(HijosATexto(Plataforma))
