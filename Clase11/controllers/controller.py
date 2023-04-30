import xml.etree.ElementTree as ET
from .Contenido import ListaPulbicaciones, ListaPubs

def EjecutarUnHola(saludoPersonalizado=None):
    
    if (saludoPersonalizado != None):
        root = ET.fromstring(saludoPersonalizado)
        elnombre = ""
        for child in root:
            print('Texto', child.text)
            elnombre = child.text
        return(
            '''
            <Respuesta>
                <Codigo>200</Codigo>
                <Mensaje>Hola amigo, tu te llamas '''+elnombre+''', y te saludo.
            </Respuesta>
            '''
            )
    return ({
        "Codigo": 201,
        "Mensaje": ":3 Los quiero mucho pollitos"
    })

def ObtenerLista():
    TextoRespuesta = "<Respuesta>\n"
    TextoRespuesta += "<Codigo>200</Codigo>\n"
    TextoRespuesta += "<ListaPublicaciones>\n"
    for elemento in ListaPulbicaciones:
        TextoRespuesta += "<Publicacion>\n"
        TextoRespuesta += "<Autor>"+str(elemento["Autor"])+"</Autor>\n"
        TextoRespuesta += "<Contenido>"+str(elemento["Contenido"])+"</Contenido>\n"
        TextoRespuesta += "<FechaPublicacion>"+str(elemento["FechaPublicacion"])+"</FechaPublicacion>\n"
        TextoRespuesta += "</Publicacion>\n"
    TextoRespuesta += "</ListaPublicaciones>\n"
    TextoRespuesta += "</Respuesta>\n"
    return TextoRespuesta

def ObtenerPub(Parametros):
    '''
        <Peticion>
            <idPublicacion>1</idPublicacion>
        </Peticion>
    '''
    if Parametros != None:
        root = ET.fromstring(Parametros)
        id = -1
        for hijo in root:
            if hijo.tag == 'idPublicacion':
                id = int(hijo.text)
        if id == -1:
            return '''
                <Respuesta>
                    <Codigo>202</Codigo>
                    <Mensaje>Error: No se mandaron los parámetros correctos</Mensaje>
                </Respuesta>
            '''
        if id >= len(ListaPubs.Lista):
            return '''
                <Respuesta>
                    <Codigo>203</Codigo>
                    <Mensaje>Error: El id no existe en la DB.</Mensaje>
                </Respuesta>
            '''
        Publicacion = ListaPubs.Publicacion(id)
        return '''
                <Respuesta>
                    <Codigo>200</Codigo>
                    <Mensaje>Exito</Mensaje>
                    <Publicacion>
                        <Autor>'''+str(Publicacion.Autor)+'''</Autor>
                        <Contenido>'''+str(Publicacion.Contenido)+'''</Contenido>
                        <FechaPublicacion>'''+str(Publicacion.FechaPublicacion)+'''</FechaPublicacion>
                    </Publicacion>
                </Respuesta>
            '''
    return '''
        <Respuesta>
            <Codigo>201</Codigo>
            <Mensaje>Error: No mandaron parámetros</Mensaje>
        </Respuesta>
    '''

def EditarPublicacion(Parametros):
    '''
        <Peticion>
            <idPublicacion>1</idPublicacion>
            <Autor>asdfasdf</Autor>
            <Contenido>asdasdfasdfsdf</Contenido>
        </Peticion>
    '''
    if Parametros != None:
        root = ET.fromstring(Parametros)
        id = -1
        Autor = ""
        Contenido = ""

        for hijo in root:
            if hijo.tag == "idPublicacion":
                id = int(hijo.text)
            if hijo.tag == "Autor":
                Autor = str(hijo.text)
            if hijo.tag == "Contenido":
                Contenido = str(hijo.text)

        if id == -1:
            return '''
                <Respuesta>
                    <Codigo>202</Codigo>
                    <Mensaje>Error: No se mandaron los parámetros correctos</Mensaje>
                </Respuesta>
            '''
        if id >= len(ListaPubs.Lista):
            return '''
                <Respuesta>
                    <Codigo>203</Codigo>
                    <Mensaje>Error: El id no existe en la DB.</Mensaje>
                </Respuesta>
            '''
        ListaPulbicaciones[id]["Contenido"] = Contenido
        ListaPulbicaciones[id]["Autor"] = Autor
        ListaPubs.Editar(id, Autor, Contenido)
        return '''
            <Respuesta>
                <Codigo>200</Codigo>
                <Mensaje>Exito</Mensaje>
            </Respuesta>
        '''
    return '''
        <Respuesta>
            <Codigo>201</Codigo>
            <Mensaje>Error: No mandaron parámetros</Mensaje>
        </Respuesta>
    '''

'''
ACCIONES QUE PUEDO REALIZAR
    ->+ Detalle de una publicacion
    ->+ Editar una Publicación
    ->+ Crear una Publicación

    + Analizar contenido de una publicacion

'''

def CrearPublicacion(Parametros):
    '''
    <Peticion>
        <Autor>adsasdf</Autor>
        <Contenido>asdfasdf</Contenido>
        <FechaPublicacion>22-04-1956</FechaPublicacion>
    </Peticion>
'''
    if Parametros != None:
        root = ET.fromstring(Parametros)
        Autor = ""
        Contenido = ""
        FechaPublicacion = ""
        for hijo in root:
            if hijo.tag == "Autor":
                Autor = str(hijo.text)
            if hijo.tag == "Contenido":
                Contenido = str(hijo.text)
            if hijo.tag == "FechaPublicacion":
                FechaPublicacion = str(hijo.text)
        
        ListaPulbicaciones.append(
            {
                "Autor": Autor,
                "Contenido": Contenido,
                "FechaPublicacion": FechaPublicacion
            }
        )

        ListaPubs.Agregar(Autor, Contenido, FechaPublicacion)
        return '''
            <Respuesta>
                <Codigo>200</Codigo>
                <Mensaje>Exito</Mensaje>
                <idPublicacion>'''+str(len(ListaPubs.Lista)-1)+'''</idPublicacion>
            </Respuesta>
        '''
    return '''
        <Respuesta>
            <Codigo>201</Codigo>
            <Mensaje>Error: No mandaron parámetros</Mensaje>
        </Respuesta>
    '''

def Analizar(Parametros):
    '''
        <Peticion>
            <idPublicacion>1</idPublicacion>
            <PalabrasClave>
                <PalabraClave>algo</PalabraClave>
                <PalabraClave>esto</PalabraClave>
                ...
            </PalabrasClave>
        </Peticion>
    '''
    if Parametros != None:
        root = ET.fromstring(Parametros)
        id = -1
        PalabrasClave = []
        for hijo in root:
            if hijo.tag == 'idPublicacion':
                id = int(hijo.text)
            if hijo.tag == 'PalabrasClave':
                Palabras = hijo
                for Palabra in Palabras:
                    PalabrasClave.append(Palabra.text)
        
        if id == -1:
            return '''
                <Respuesta>
                    <Codigo>202</Codigo>
                    <Mensaje>Error: No se mandaron los parámetros correctos</Mensaje>
                </Respuesta>
            '''
        if id >= len(ListaPubs.Lista):
            return '''
                <Respuesta>
                    <Codigo>203</Codigo>
                    <Mensaje>Error: El id no existe en la DB.</Mensaje>
                </Respuesta>
            '''
        Cantidad = ListaPubs.Analizar(id, PalabrasClave)
        return '''
                <Respuesta>
                    <Codigo>200</Codigo>
                    <Mensaje>Exito</Mensaje>
                    <Resultado>'''+str(Cantidad)+'''</Resultado>
                </Respuesta>
            '''
    return '''
        <Respuesta>
            <Codigo>201</Codigo>
            <Mensaje>Error: No mandaron parámetros</Mensaje>
        </Respuesta>
    '''