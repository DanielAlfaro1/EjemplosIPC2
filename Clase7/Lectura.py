from xml.dom import minidom

def LecturaXML(FichasNegras, FichasRojas):
    cantRows = 0
    cantCols = 0
    doc = minidom.parse("./Clase7/Entrada.xml")

    print("-------- Leyendo documento --------")
    Damas = doc.getElementsByTagName("Damas")
    #Damas
    for Dama in Damas:
        #Lectura del tablero
        Tablero = Dama.getElementsByTagName("Tablero")
        #Damas/Tablero
        for Dato in Tablero:
            Filas = Dato.getElementsByTagName("Fila")
            #Damas/Tablero/Filas
            Columnas = Dato.getElementsByTagName("Columna")
            #Damas/Tablero/Columnas
            
            cantRows = int(Filas[0].firstChild.nodeValue)
            cantCols = int(Columnas[0].firstChild.nodeValue)
            print("Filas: " + str(cantRows))
            print("Columnas: "+ str(cantCols))
            FichasNegras.SetLimites(cantRows, cantCols)
            FichasRojas.SetLimites(cantRows, cantCols)
        #Lectura de las fichas
        Fichas = Dama.getElementsByTagName("Fichas")
        #Damas/Fichas
        for Datos in Fichas:
            #Fichas Rojas
            Rojas = Datos.getElementsByTagName("Rojas")
            #Damas/Fichas/Rojas
            for Ficha in Rojas:
                print("Rojas")
                Posicion = Ficha.getElementsByTagName("Posicion")
                #Damas/Fichas/Rojas/Posicion
                for Parametros in Posicion:
                    Fila = Parametros.getElementsByTagName("Fila")
                    #Damas/Fichas/Rojas/Posicion/Fila
                    Columna = Parametros.getElementsByTagName("Columna")
                    #Damas/Fichas/Rojas/Posicion/Columna
                    print(str(Fila[0].firstChild.nodeValue) + ", "+ str(Columna[0].firstChild.nodeValue))
                    FichasRojas.Insertar(int(Columna[0].firstChild.nodeValue), int(Fila[0].firstChild.nodeValue))
            #Fichas Negras
            Negras = Datos.getElementsByTagName("Negras")
            #Damas/Fichas/Negras
            for Ficha in Negras:
                print("Negras")
                Posicion = Ficha.getElementsByTagName("Posicion")
                #Damas/Fichas/Negras/Posicion
                for Parametros in Posicion:
                    Fila = Parametros.getElementsByTagName("Fila")
                    #Damas/Fichas/Rojas/Posicion/Fila
                    Columna = Parametros.getElementsByTagName("Columna")
                    #Damas/Fichas/Rojas/Posicion/Columna
                    print(str(Fila[0].firstChild.nodeValue) + ", "+ str(Columna[0].firstChild.nodeValue))
                    FichasNegras.Insertar(int(Columna[0].firstChild.nodeValue), int(Fila[0].firstChild.nodeValue))