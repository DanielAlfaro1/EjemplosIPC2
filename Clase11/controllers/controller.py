import xml.etree.ElementTree as ET

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