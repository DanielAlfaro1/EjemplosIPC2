documento = open("../Archivos/EjemploLectura.txt")

print(documento)

for linea in documento:
    print(linea)
documento.close()
documento = open("../Archivos/EjemploLectura.txt")
texto1 = documento.readlines()
for linea in texto1:
    if linea.startswith("Como"):
        print(linea)

documento = open("../Archivos/EjemploLectura.txt", 'w')
texto = "estoy sobreescribiendo.\nAhora en tu texto ya no está lo de antes"
documento.write(texto)
documento.close()

documento = open("../Archivos/EjemploLectura.txt")
texto = documento.readlines()
for linea in texto:    
    print(linea)
documento.close()

documento = open("../Archivos/EjemploLectura.txt", 'w')
textito = ""
for linea in texto1:
    textito += linea
documento.write(textito)
documento.close()