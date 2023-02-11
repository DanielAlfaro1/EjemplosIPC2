import xml

def HijosATexto(objeto):

    if type(objeto) == xml.dom.minidom.Element:
        hijos = ""
        for elemento in objeto.childNodes:
            hijos = hijos + ", "+str(HijosATexto(elemento)).strip('\n').strip(' ')
        #return str("[Padre: "+ str(objeto.nodeName)+ ", hijo(s): "+hijos+"]")
        return str("["+str(objeto.nodeName)+ ":" + hijos+"]")
    else:
        return str(objeto.nodeValue)