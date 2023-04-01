from xml.dom import minidom

doc = minidom.parse("C:/Users/Stormy/Downloads/Entrada_Ejemplo_P2.xml")
CONFIG = doc.getElementsByTagName('CONFIG')
for ListElem1 in CONFIG: 
    listaMaquinas2 = ListElem1.getElementsByTagName("listaMaquinas")
    for Maquina2 in listaMaquinas2:
        Info2 = Maquina2.getElementsByTagName('Maquina')
        for MaquinasE in Info2:
            PinesX = MaquinasE.getElementsByTagName('pin')
            for Pin1 in PinesX:
                Elementos1 = Pin1.getElementsByTagName('elementos')
                for EleX in Elementos1:
                    ElementosInLista1 = EleX.getElementsByTagName('elemento') 
                    SimbX = str(ElementosInLista1[0].firstChild.nodeValue)
                    print(SimbX)
                    
                    for i in ElementosInLista1:
                        print('Test info Pines: ', i.firstChild.nodeValue)
                        TextField4.insert(END, " "+i.firstChild.nodeValue+"\n")
                        ListaElementosGamma.Append2(i.firstChild.nodeValue)